from swampy.Gui import *
import math

class VectorEditor(Gui):
    def __init__(self):
        Gui.__init__(self)
        self.canvas = self.ca(width=600, height=400, bg='white')
        self.canvas.bind('<ButtonPress-1>', self.start)
        self.canvas.bind('<ButtonRelease-1>', self.draw)
        self.row()
        self.bu(text="Draw Circle", command=Callable(self.select_cursor, 'circle'))
        self.bu(text="Draw Line", command=Callable(self.select_cursor, 'line'))
        self.bu(text="Draw Rectangle", command=Callable(self.select_cursor, 'rect'))
        self.endrow()

        self.row()
        self.la(text="Selected: ")
        self.obj_label = self.la(text="")
        self.size_en = self.en(text="")
        self.resize_btn = self.bu(text="Resize", command=self.resize_item)
        self.endrow()

        self.row()
        self.bu(text="Save", command=self.save)
        self.bu(text="New Canvas", command=self.canvas.clear)

    def start(self, event=None):
        if hasattr(event.widget, 'obj') and event.widget.obj:
            return

        self.start_x, self.start_y = self.canvas.canvas_coords([event.x, event.y])

    def distance(self, x, y):
        return math.sqrt((x - self.start_x)**2 + (y - self.start_y)**2)

    def draw(self, event=None):
        if hasattr(event.widget, 'obj') and event.widget.obj:
            event.widget.obj = False
            return

        x, y = self.canvas.canvas_coords([event.x, event.y])

        if self.cursor == 'circle':
            item = self.canvas.circle([self.start_x, self.start_y], self.distance(x, y), 'red')
        elif self.cursor == 'line':
            item = self.canvas.line([[self.start_x, self.start_y], [x, y]], width=5, fill='red')
        elif self.cursor == 'rect':
            item = self.canvas.rectangle([[self.start_x, self.start_y], [x, y]], fill='red')

        item = VectorItem(item, self)
        self.selected = item

    def select_cursor(self, cursor):
        self.cursor = cursor

    def resize_item(self):
        radius = float(self.size_en.get())

        if self.selected.type() == 'oval':
            self.selected.move_coord(0, -radius/2, radius/2)
            self.selected.move_coord(1, radius/2, -radius/2)
        elif self.selected.type() == 'line':
            start, end = self.selected.coords()
            size = float(self.selected.get_size())
            new_size = float(self.size_en.get())
            x1, y1 = start
            x2, y2 = end
            dy = y2 - y1
            dx = x2 - x1
            sine = dy/size
            cosine = dx/size
            new_dx = cosine * new_size
            new_dy = sine * new_size
            self.selected.move_coord(1, new_dx - dx, new_dy - dy)
        elif self.selected.type() == 'rectangle':
            start, end = self.selected.coords()
            x1, y1 = start
            x2, y2 = end
            w = x2 - x1
            h = y2 - y1
            area = w * h
            new_area = float(self.size_en.get())
            dx = (h / area * new_area) + x1 - x2
            dy = (h / area * new_area) + y1 - y2
            self.selected.move_coord(1, dx, dy)


    def save(self):
        """Save"""


class VectorItem(Item):
    def __init__(self, item, editor):
        self.canvas = item.canvas
        self.editor = editor
        self.tag = item.tag
        self.bind('<ButtonPress-1>', self.select)

    def get_size(self):
        if self.type() == 'oval':
            start, end = self.bbox()
            x1, y1 = start
            x2, y2 = end
            return (x2- x1) / 2
        elif self.type() == 'line':
            start, end = self.coords()
            x1, y1 = start
            x2, y2 = end
            return math.sqrt((x1-x2)**2 + (y1-y2)**2)
        elif self.type() == 'rectangle':
            start, end = self.coords()
            x1, y1 = start
            x2, y2 = end
            return math.fabs((x2-x1) * (y2-y1))


    def select(self, event=None):
        self.editor.selected = self
        self.editor.size_en.delete(0, END)
        self.editor.size_en.insert(0, self.get_size())
        event.widget.obj = True

if __name__ == '__main__':
    v = VectorEditor()
    v.mainloop()
