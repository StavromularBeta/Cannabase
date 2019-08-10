import tkinter as Tk
import sys
sys.path.append("/Users/PeterLevett/PycharmProjects/Cannabase/Cannabase/sql_files")


class ArchiveWindow(Tk.Frame):
    def __init__(self, parent, **kwargs):
        Tk.Frame.__init__(self, parent, **kwargs)
        self.parent = parent
        self.main_archive_frame = Tk.Frame(self, borderwidth=1, relief='solid')

    def clear_archive_frame(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.main_archive_frame = Tk.Frame(self, borderwidth=1, relief='solid')

    def display_archive(self):
        Tk.Label(self.main_archive_frame, text='Archive Page').grid(row=0, column=0, sticky=Tk.W)
        self.main_archive_frame.grid(row=0, column=0, sticky=Tk.W)
        filler_canvas = Tk.Canvas(self, width=1100, height=800)
        filler_canvas.grid(row=1, column=0)
