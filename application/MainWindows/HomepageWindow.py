import tkinter as Tk


class HomepageWindow(Tk.Frame):
    def __init__(self, parent):
        Tk.Frame.__init__(self, parent)
        self.parent = parent

    def Homepage(self):
        homepage_label = Tk.Label(self, text="Homepage")
        homepage_label.grid()
