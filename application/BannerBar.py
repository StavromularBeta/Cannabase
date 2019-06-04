import tkinter as Tk


class BannerBar(Tk.Frame):
    def __init__(self, parent):
        Tk.Frame.__init__(self, parent)

    def make_banner(self):
        main_banner = Tk.Label(self, text="Cannabase")
        main_banner.grid()
