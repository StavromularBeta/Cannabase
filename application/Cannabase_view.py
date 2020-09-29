import tkinter as Tk
import BannerBar_view as Bb
import NavigationBar_view as Nb
import MainWindow_view as Mw


class MainApplication(Tk.Frame):
    def __init__(self, parent, **kwargs):
        Tk.Frame.__init__(self, parent, **kwargs)
        self.BannerBar = Bb.BannerBar(self, bg='#60992d', width=1300)
        self.MainWindow = Mw.MainWindow(self, bg='#e0fcf4')
        self.NavigationBar = Nb.NavigationBar(self, bg='#a1e44d', height=900)
        self.BannerBar.pack(side='top', fill='x')
        self.BannerBar.pack_propagate(0)
        self.NavigationBar.pack(side='left', ipady=5, fill='y')
        self.NavigationBar.pack_propagate(0)
        self.MainWindow.pack(side='right', fill='both',  expand=True)
        self.MainWindow.pack_propagate(0)
        self.BannerBar.make_banner()
        self.NavigationBar.make_navbar()
        self.MainWindow.display_searchpage()


root = Tk.Tk()
height = root.winfo_screenheight() - 80
width = root.winfo_screenwidth() - 15
root.geometry(f'{width}x{height}+0-40')
MainApplication(root).grid()
root.mainloop()
