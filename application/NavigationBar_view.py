import tkinter as Tk
from tkinter import font as tkFont


class NavigationBar(Tk.Frame):
    def __init__(self, parent, **kwargs):
        Tk.Frame.__init__(self, parent, **kwargs)
        self.parent = parent
        self.nav_bar_button_font = tkFont.Font(size=18)

    def make_navbar(self):
        search_button = Tk.Button(self,
                                  text=" Current \n Jobs",
                                  command=self.parent.MainWindow.display_searchpage,
                                  font=self.nav_bar_button_font)
        customer_button = Tk.Button(self,
                                    text="Current\nClients",
                                    command=self.parent.MainWindow.display_customerpage,
                                    font=self.nav_bar_button_font)
        archive_button = Tk.Button(self,
                                   text="Job\nArchives",
                                   command=lambda: self.parent.MainWindow.display_searchpage(archive=True),
                                   font=self.nav_bar_button_font)
        search_button.grid(row=0, padx=5, pady=5)
        customer_button.grid(row=1, padx=5, pady=5, ipadx=5)
        archive_button.grid(row=2, padx=5, pady=5)



