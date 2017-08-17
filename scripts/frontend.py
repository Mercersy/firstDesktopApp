try:
  from tkinter import *
except ImportError:
  from Tkinter import *
from backend import Database

database = Database("projs.db")

class Window(object):

    def __init__(self, window):
        self.window = window
        self.window.wm_title("Project List")

        l1 = Label(window, text = "Title")
        l1.grid(row = 0, column = 0)

        l2 = Label(window, text = "Date")
        l2.grid(row = 2, column = 0)

        l3 = Label(window, text = "Skills")
        l3.grid(row = 4, column = 0)

        l4 = Label(window, text = "Details")
        l4.grid(row = 6, column = 0)

        self.title_text = StringVar()
        self.e1 = Entry(window, textvariable = self.title_text)
        self.e1.grid(row = 0, column = 1)

        self.date_text = StringVar()
        self.e2 = Entry(window, textvariable = self.date_text)
        self.e2.grid(row = 2, column = 1)

        self.skills_text = StringVar()
        self.e3 = Entry(window, textvariable = self.skills_text)
        self.e3.grid(row = 4, column = 1)

        self.details_text = StringVar()
        self.e4 = Entry(window, textvariable = self.details_text)
        self.e4.grid(row = 6, column = 1)

        self.list1 = Listbox(window, height = 11, width = 35)
        self.list1.grid(row = 0, column = 2, rowspan = 7, columnspan = 2)

        sb1 = Scrollbar(window)
        sb1.grid(row = 0, column = 4, rowspan = 7)

        self.list1.configure(yscrollcommand = sb1.set)
        sb1.configure(command = self.list1.yview)

        self.list1.bind('<<ListboxSelect>>', self.get_selected_row)

        b1 = Button(window, text = "View All", width = 12, command = self.view_command)
        b1.grid(row = 0, column = 5)

        b2 = Button(window, text = "Search", width = 12, command = self.search_command)
        b2.grid(row = 1, column = 5)

        b3 = Button(window, text = "Add Entry", width = 12, command = self.add_command)
        b3.grid(row = 2, column = 5)

        b4 = Button(window, text = "Update Entry", width = 12, command = self.update_command)
        b4.grid(row = 3, column = 5)

        b5 = Button(window, text = "Delete", width = 12, command = self.delete_command)
        b5.grid(row = 4, column = 5)

        b6 = Button(window, text = "Import...", width = 12)
        b6.grid(row = 5, column = 5)

        b7 = Button(window, text = "Close", width = 12, command = window.destroy)
        b7.grid(row = 6, column = 5)


    def get_selected_row(self, event):
        index = self.list1.curselection()[0]
        self.selected_tuple = self.list1.get(index)
        self.e1.delete(0,END)
        self.e1.insert(END, self.selected_tuple[1])
        self.e2.delete(0,END)
        self.e2.insert(END, self.selected_tuple[2])
        self.e3.delete(0,END)
        self.e3.insert(END, self.selected_tuple[3])
        self.e4.delete(0,END)
        self.e4.insert(END, self.selected_tuple[4])

    def view_command(self):
        self.list1.delete(0, END)
        for row in database.view():
            self.list1.insert(END, row)

    def search_command(self):
        self.list1.delete(0, END)
        for row in database.search(self.title_text.get(), self.date_text.get(),\
                                    self.skills_text.get(), self.details_text.get()):
            self.list1.insert(END, row)

    def add_command(self):
        database.insert(self.title_text.get(), self.date_text.get(), \
                        self.skills_text.get(), self.details_text.get())
        self.list1.delete(0, END)
        self.list1.insert(END, (self.title_text.get(), self.date_text.get(), \
                            self.skills_text.get(), self.details_text.get()))

    def delete_command(self):
        database.delete(self.selected_tuple[0])

    def update_command(self):
        database.update(self.selected_tuple[0], self.title_text.get(), \
                        self.date_text.get(), self.skills_text.get(), self.details_text.get())

window = Tk()
Window(window)
window.mainloop()
