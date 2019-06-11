import tkinter as Tk


class NavigationBar(Tk.Frame):
    def __init__(self, parent):
        Tk.Frame.__init__(self, parent)
        self.parent = parent

    def make_navbar(self):
        search_button = Tk.Button(self, text="Search", command=self.parent.MainWindow.display_searchpage)
        edit_add_button = Tk.Button(self, text="Edit/Add", command=self.parent.MainWindow.display_editaddpage)
        search_button.grid(row=0)
        edit_add_button.grid(row=1)



