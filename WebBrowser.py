import urllib.request
from html.parser import HTMLParser
from swampy.Gui import *

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
        self.go_btn = self.bu(text='Go', command=self.load_site)
        self.endrow()
        self.canvas = self.sc(width=600, height=1000, bg='white')
        self.canvas.width = self.canvas.canvas.get_width()
        self.canvas.height = self.canvas.canvas.get_height()
        self.parser = BrowserParser(self.canvas)
        self.load_site()

    def load_site(self, event=None):
        try:
            request = urllib.request.urlopen(self.site_text.get(0.0, END))
            content = request.read().decode('utf-8', errors='ignore')

            self.canvas.canvas.clear()
            self.parser.reset_layout()
            self.parser.feed(content)
            self.canvas.canvas.scroll_config()
            self.ind += 1
            self.history.append(self.site_text.get(0.0, END))

            if self.ind < len(self.history) - 1:
                self.history = self.history[:self.ind + 1]

        except Exception as e:
            print(e)
            self.canvas.canvas.clear()
            self.canvas.canvas.text([20, 20], text="Error: Cannot load this page.")

    def back(self, event=None):
        if self.ind > 0:
            self.site_text.delete(0, END)
            self.ind -= 1
            self.site_text.insert(0, self.history[self.ind])
            self.load_site()

class BrowserParser(HTMLParser):
    def __init__(self, canvas):
        super().__init__()
        self.canvas = canvas
        self.reset_layout()

    def reset_layout(self):
        self.cursor_x, self.cursor_y = self.canvas.canvas.canvas_coords([15, 15])
        self.line_height = 25
        self.font_family = 'Arial'
        self.font_size = 12
        self.weight = 'normal'
        self.slant = 'roman'
        self.color = 'black'

        self.in_script_or_style = False

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)

        if tag in ('script', 'style'):
            self.in_script_or_style = True
            return

        if tag == 'body':
            bg_color = attrs_dict.get('bgcolor', 'white')
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

        elif tag == 'a':
            # TODO: add link handling

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
        # TODO: add link handling

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

            self.canvas.canvas.text(
                [self.cursor_x, self.cursor_y],
                text=word_to_draw,
                font=current_font,
                fill=self.color,
                anchor='nw'
            )

            # TODO: add link handling

            self.cursor_x += word_width

    def flush_line(self):
        self.cursor_x = self.canvas.canvas.canvasx(15)
        self.cursor_y -= self.line_height

if __name__ == '__main__':
    # request = urllib.request.urlopen('https://www.google.com')
    # site = request.read().decode('latin-1')
    # htp = HTMLParser()
    # htp.feed(site)
    browser = Browser()
    browser.mainloop()
