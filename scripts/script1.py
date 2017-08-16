'''
A program that stores my proj information:
Title, Date
Skills, Details

User can:
View all records
Search an entry
Add entry
Update entry
Delete
Close
'''

from tkinter import *

window = Tk()

window.title("ProjList")

l1 = Label(window, text = "Title")
l1.grid(row = 0, column = 0)

l2 = Label(window, text = "Date")
l2.grid(row = 2, column = 0)

l3 = Label(window, text = "Skills")
l3.grid(row = 4, column = 0)

l4 = Label(window, text = "Details")
l4.grid(row = 6, column = 0)

title_text = StringVar()
e1 = Entry(window, textvariable = title_text)
e1.grid(row = 0, column = 1)

date_text = StringVar()
e2 = Entry(window, textvariable = date_text)
e2.grid(row = 2, column = 1)

skills_text = StringVar()
e3 = Entry(window, textvariable = skills_text)
e3.grid(row = 4, column = 1)

details_text = StringVar()
e4 = Entry(window, textvariable = details_text)
e4.grid(row = 6, column = 1)

list1 = Listbox(window, height = 6, width = 35)
list1.grid(row = 0, column = 2, rowspan = 7, columnspan = 2)

sb1 = Scrollbar(window)
sb1.grid(row = 0, column = 4, rowspan = 7)

list1.configure(yscrollcommand = sb1.set)
sb1.configure(command = list1.yview)

b1 = Button(window, text = "View All", width = 12)
b1.grid(row = 0, column = 5)

b2 = Button(window, text = "Search", width = 12)
b2.grid(row = 1, column = 5)

b3 = Button(window, text = "Add Entry", width = 12)
b3.grid(row = 2, column = 5)

b4 = Button(window, text = "Update Entry", width = 12)
b4.grid(row = 3, column = 5)

b5 = Button(window, text = "Delete", width = 12)
b5.grid(row = 4, column = 5)

b6 = Button(window, text = "Close", width = 12)
b6.grid(row = 5, column = 5)

window.mainloop()
