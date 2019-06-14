import tkinter as Tk
from tkinter import font as tkFont


class BannerBar(Tk.Frame):
    def __init__(self, parent):
        Tk.Frame.__init__(self, parent)
        self.banner_font = tkFont.Font(size=48, weight='bold')

    def make_banner(self):
        main_banner = Tk.Label(self, text="Cannabase", font=self.banner_font)
        main_banner.grid()
