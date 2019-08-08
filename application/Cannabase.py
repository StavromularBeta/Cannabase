import tkinter as Tk
import BannerBar as Bb
import NavigationBar as Nb
import MainWindow as Mw


class MainApplication(Tk.Frame):
    def __init__(self, parent, **kwargs):
        Tk.Frame.__init__(self, parent, **kwargs)
        self.BannerBar = Bb.BannerBar(self)
        self.MainWindow = Mw.MainWindow(self)
        self.NavigationBar = Nb.NavigationBar(self)
        self.BannerBar.pack(side='top', fill='x')
        self.NavigationBar.pack(side='left', fill='y', padx=5, pady=5)
        self.MainWindow.pack(side='right', fill='both', expand=True)
        self.BannerBar.make_banner()
        self.NavigationBar.make_navbar()
        self.MainWindow.display_searchpage()


root = Tk.Tk()
root.geometry('1200x900')
MainApplication(root).grid()
root.mainloop()