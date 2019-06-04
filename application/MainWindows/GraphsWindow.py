import tkinter as Tk


class GraphsWindow(Tk.Frame):
    def __init__(self, parent):
        Tk.Frame.__init__(self, parent)
        self.parent = parent

    def graphs(self):
        graphs_label = Tk.Label(self, text="Graphs")
        graphs_label.grid()
