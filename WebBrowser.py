import urllib.request
import urllib.parse
from html.parser import HTMLParser
from swampy.Gui import *
import PIL.Image
import PIL.ImageTk
import gzip

class Browser(Gui):
    def __init__(self):
        Gui.__init__(self)
        self.history = []
        self.ind = -1
        self.row()
        self.back_btn = self.bu(text='Back', command=self.back)
        self.site_text = self.te(width=100, height=5)
        self.site_text.insert(0.0, "http://www.python.org")
        self.site_text.bind('<Return>', self.load_site)
        self.go_btn = self.bu(text='Go', command=self.go_to_site)
        self.endrow()
        self.canvas = self.sc(width=600, height=1000, bg='white')
        self.canvas.width = self.canvas.canvas.get_width()
        self.canvas.height = self.canvas.canvas.get_height()
        self.parser = BrowserParser(self.canvas, self)
        self.load_site()

    def load_site(self, event=None):
        try:
            request = urllib.request.Request(self.site_text.get(0.0, END).strip(), headers={'User-Agent': 'Mozilla/5.0'})
            response = urllib.request.urlopen(request)
            raw_data = response.read()

            if response.headers.get('Content-Encoding') == 'gzip':
                raw_data = gzip.decompress(raw_data)

            content = raw_data.decode('utf-8', errors='ignore')

            self.canvas.canvas.clear()
            self.parser.reset_layout()
            self.parser.images = []
            self.parser.feed(content)
            self.canvas.canvas.scroll_config()
            self.ind += 1
            self.history.append(self.site_text.get(0.0, END))

        except Exception as e:
            print(e)
            self.canvas.canvas.clear()
            self.canvas.canvas.text([20, 20], text="Error: Cannot load this page.")

    def back(self, event=None):
        if self.ind > 0:
            self.site_text.delete(0.0, END)
            self.ind -= 1
            self.site_text.insert(0.0, self.history[self.ind])
            self.load_site()

    def go_to_site(self, event=None):
        self.load_site()

        if self.ind < len(self.history) - 1:
            self.history = self.history[:self.ind + 1]

class BrowserParser(HTMLParser):
    def __init__(self, canvas, browser):
        super().__init__()
        self.browser = browser
        self.canvas = canvas
        self.images = []
        self.reset_layout()

    def reset_layout(self):
        self.cursor_x, self.cursor_y = self.canvas.canvas.canvas_coords([15, 15])
        self.line_height = 25
        self.font_family = 'Arial'
        self.font_size = 12
        self.weight = 'normal'
        self.slant = 'roman'
        self.color = 'black'
        self.underline = False
        self.link = False
        self.link_href = ''

        self.in_script_or_style = False

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        styles = self.parse_inline_styles(attrs_dict.get('style', ''))

        if tag in ('script', 'style'):
            self.in_script_or_style = True
            return

        if tag == 'body':
            bg_color = attrs_dict.get('bgcolor', 'white') or styles.get("background-color") or '#ffffff'
            self.canvas.canvas.config(bg=bg_color)

        elif tag == 'h1':
            self.flush_line()
            self.font_size = 22
            self.weight = 'bold'
            self.line_height = 30

        elif tag == 'h2':
            self.flush_line()
            self.font_size=16
            self.weight = 'bold'
            self.line_height = 24

        elif tag in ['b', 'strong']:
            self.weight = 'bold'

        elif tag in ['i', 'em']:
            self.slant = 'italic'

        elif tag in ['p', 'div']:
            self.flush_line()
            self.cursor_y += 10

        elif tag == 'br':
            self.flush_line()

        elif tag in ['p', 'div', 'h1', 'h2']:
            if 'background-color' in styles:
                block_color = styles['background-color']
                self.canvas.canvas.rectangle([self.canvas.canvas.canvas_coords([0, self.cursor_y]), self.canvas.canvas.canvas_coords([0 + self.canvas.width, self.cursor_y + 120])], block_color)

        elif tag == 'a':
            self.link = True
            self.link_href = urllib.parse.urljoin(self.browser.site_text.get(0.0, END).strip(), attrs_dict.get('href', ''))
            self.color = 'blue'
            self.underline = True

        elif tag == 'img':
            src = attrs_dict.get('src')

            if src:
                img_url = urllib.parse.urljoin(self.browser.site_text.get(0.0, END).strip(), src)
                self.render_image(img_url)

        if 'color' in styles:
            self.color = styles['color']


    def handle_endtag(self, tag):
        if tag in ['script', 'style']:
            self.in_script_or_style = False
            return

        if tag in ['h1', 'h2', 'h3', 'h4']:
            self.flush_line()
            self.font_size = 12
            self.weight = 'normal'
            self.line_height = 25
        elif tag in ['b', 'strong']:
            self.weight = 'normal'
        elif tag in ['i', 'em']:
            self.slant = 'roman'
        elif tag in ['p', 'div']:
            self.flush_line()
        elif tag == 'a':
            self.link = False
            self.link_href = ''
            self.color = 'black'
            self.underline = False

    def handle_data(self, data):
        if self.in_script_or_style:
            return

        text = data.strip()

        if not text:
            return

        current_font = tkinter.font.Font(
            family=self.font_family,
            size=self.font_size,
            weight=self.weight,
            slant=self.slant
        )

        words = data.split()

        for idx, word in enumerate(words):
            word_to_draw = word + (' ' if idx < len(words) - 1 else '')
            word_width = current_font.measure(word_to_draw)

            if self.cursor_x + word_width > self.canvas.width - 15 or word == '\n':
                self.flush_line()

            ca_text = self.canvas.canvas.text(
                [self.cursor_x, self.cursor_y],
                text=word_to_draw,
                font=current_font,
                fill=self.color,
                underline=int(self.underline),
                anchor='nw'
            )

            if self.link:
                url = urllib.parse.urljoin(self.browser.site_text.get(0.0, END).strip(), self.link_href)
                ca_text.bind('<Button-1>', Callable(self.enter_link, url))
                ca_text.bind('<Enter>', self.change_cursor)
                ca_text.bind('<Leave>', self.change_cursor)

            self.cursor_x += word_width

    def parse_inline_styles(self, style_str):
        styles = {}

        if not style_str:
            return styles

        for item in style_str.split(';'):
            if ':' in item:
                key, value = item.split(':', 1)
                styles[key.strip().lower()] = value.strip().lower()

        return styles

    def flush_line(self):
        self.cursor_x = -self.canvas.width/2 + 15
        self.cursor_y -= self.line_height

    def render_image(self, url):
        req = urllib.request.urlopen(url)
        photo = PIL.ImageTk.PhotoImage(PIL.Image.open(req))
        self.images.append(photo)

        if self.cursor_x + photo.width() > self.canvas.width - 15:
            self.flush_line()

        self.canvas.canvas.image([self.cursor_x, self.cursor_y], image=photo, anchor='nw')
        self.cursor_y -= photo.height() + 10
        self.flush_line()

    def enter_link(self, url, event=None):
        self.browser.site_text.delete(0.0, END)
        self.browser.site_text.insert(0.0, url)
        self.browser.load_site()

    def change_cursor(self, event=None):
        if '7' in event.type:
            self.canvas.canvas.configure(cursor='hand2')
        else:
            self.canvas.canvas.configure(cursor='')

if __name__ == '__main__':
    # request = urllib.request.urlopen('https://www.google.com')
    # site = request.read().decode('latin-1')
    # htp = HTMLParser()
    # htp.feed(site)
    browser = Browser()
    browser.mainloop()
