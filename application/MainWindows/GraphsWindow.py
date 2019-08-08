import tkinter as Tk


class GraphsWindow(Tk.Frame):
    def __init__(self, parent, **kwargs):
        Tk.Frame.__init__(self, parent, **kwargs)
        self.parent = parent

    def graphs(self):
        graphs_label = Tk.Label(self, text="Graphs")
        graphs_label.grid()
