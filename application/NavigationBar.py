import tkinter as Tk
from tkinter import font as tkFont


class NavigationBar(Tk.Frame):
    def __init__(self, parent):
        Tk.Frame.__init__(self, parent)
        self.parent = parent
        self.nav_bar_button_font = tkFont.Font(size=18)

    def make_navbar(self):
        search_button = Tk.Button(self,
                                  text=" Current \n Jobs",
                                  command=self.parent.MainWindow.display_searchpage,
                                  font=self.nav_bar_button_font)
        edit_add_button = Tk.Button(self,
                                    text="Enter\nNew Job",
                                    command=self.parent.MainWindow.display_editaddpage,
                                    font=self.nav_bar_button_font)
        search_button.grid(row=0)
        edit_add_button.grid(row=1)



