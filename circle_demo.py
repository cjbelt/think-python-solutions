from swampy.Gui import *
import random

def draw_circle():
    global last_circle
    circle = canvas.circle([random.randint(0, 400), random.randint(0, 400)], 50, fill='red')
    last_circle = circle
    return circle

def change_color():
    try:
        last_circle.config(fill=entry.get())
    except NameError:
        entry.insert(END, '\tYou have to draw a circle first!')
    except tkinter.TclError:
        entry.insert(END, '\tInvalid color name!')

g = Gui()
g.title('Circle Party!')
canvas = g.ca(width=500, height=500, bg='white')
g.bu(text='Draw circle.', command=draw_circle)
entry = g.en(text='red')
g.bu(text='Change color', command=change_color)

g.mainloop()
