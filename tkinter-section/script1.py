from tkinter import *

window = Tk()

def convert_kg():
    kg = float(e1_value.get())
    g = kg * 1000.0
    lb = kg * 2.20462
    oz = kg * 35.274
    t_g.insert(END, g)
    t_lb.insert(END, lb)
    t_oz.insert(END, oz)


b1 = Button(window, text = "Convert", command = convert_kg)
b1.grid(row = 0, column = 2)

e1_value = StringVar()
e1 = Entry(window, textvariable = e1_value, width = 16)
e1.grid(row = 0, column = 1)

l1 = Label(text = "Kg")
l1.grid(row = 0, column = 0)

#------
t_g = Text(window, height = 1, width = 20)
t_g.grid(row = 1, column = 0)

t_lb = Text(window, height = 1, width = 20)
t_lb.grid(row = 1, column = 1)

t_oz = Text(window, height = 1, width = 20)
t_oz.grid(row = 1, column = 2)


window.mainloop()
