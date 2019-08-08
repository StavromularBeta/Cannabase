import tkinter as Tk


class HomepageWindow(Tk.Frame):
    def __init__(self, parent, **kwargs):
        Tk.Frame.__init__(self, parent, **kwargs)
        self.parent = parent

    def Homepage(self):
        homepage_label = Tk.Label(self, text="Homepage")
        homepage_label.grid()
