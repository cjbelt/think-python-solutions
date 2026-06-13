from swampy.Gui import *

g = Gui()
g.title('button demo')

def create_button():
    g.bu(text='Click me, NOW!', command=create_label)

def create_label():
    g.la(text='Nice job!')

g.bu(text='Click me.', command=create_button)
g.mainloop()
