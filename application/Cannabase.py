import tkinter as Tk
import BannerBar as Bb
import NavigationBar as Nb
import MainWindow as Mw


class MainApplication(Tk.Frame):
    def __init__(self, parent):
        Tk.Frame.__init__(self, parent)
        self.BannerBar = Bb.BannerBar(self)
        self.MainWindow = Mw.MainWindow(self)
        self.NavigationBar = Nb.NavigationBar(self)
        self.BannerBar.pack(side='top', fill='x')
        self.NavigationBar.pack(side='left', fill='y')
        self.MainWindow.pack(side='right', fill='both', expand=True)
        self.BannerBar.make_banner()
        self.NavigationBar.make_navbar()
        self.MainWindow.display_homepage()


root = Tk.Tk()
root.geometry('1240x900')
MainApplication(root).grid()
root.mainloop()