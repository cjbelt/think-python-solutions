from swampy.Gui import *

g = Gui()
g.title('Gui')
button = g.bu(text='Press me.')
label = g.la(text='Press the button.')

def make_label():
    g.la(text='Thank you.')

button2 = g.bu(text='No, press me!', command=make_label)

canvas = g.ca(width=500, height=500)
canvas.config(bg='white')
item = canvas.circle([0, 0], 100, fill='red')
item.config(fill='yellow', outline='orange', width=10)
canvas.rectangle([[0, 0], [200, 100]], fill='blue', outline='orange', width=10)
canvas.oval([[0, 0], [100, 200]], outline='orange', width=10)
canvas.line([[0,100], [100, 200], [200, 100]], width=10)
canvas.polygon([[0, 100], [100, 200], [200, 100]], fill='red', outline='orange', width=10)
entry = g.en(text='Default text.')
print(entry.get())
text = g.te(width= 100, height=5)
text.insert(END, 'A line of text.')
text.insert(1.1, 'nother')
text.delete(1.2, END)
print(text.get(0.0, END))
g.mainloop()
