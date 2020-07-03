import tkinter as Tk
import os, sys, inspect
# below 3 lines add the parent directory to the path, so that SQL_functions can be found.
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
parentdir = os.path.dirname(parentdir)
sys.path.insert(0, parentdir+'/sql_files/')
import selection as sel
import addel as addel
from tkinter import font as tkFont


class CustomerWindow(Tk.Frame):
    def __init__(self, parent, **kwargs):
        Tk.Frame.__init__(self, parent, **kwargs)
        self.parent = parent
        self.config(bg="#e0fcf4")
        self.Selection = sel.Selection()
        self.AddDelete = addel.AdDel()
        self.search_table_field_font = tkFont.Font(size=18, weight='bold')
        self.search_table_results_font = tkFont.Font(size=12, weight='bold')
        self.customer_page_main_frame = Tk.Frame(self)
        self.customer_list_display_frame = Tk.Frame(self)
        self.customer_search_info_box = Tk.Frame(self)

    def clear_customer_window(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.customer_page_main_frame = Tk.Frame(self)
        self.customer_list_display_frame = Tk.Frame(self)
        self.customer_search_info_box = Tk.Frame(self)

    def customers(self):
        self.clear_customer_window()
        self.get_full_customer_list()
        self.create_info_box()

    def create_info_box(self):
        self.customer_search_info_box = Tk.Frame(self)
        Tk.Label(self.customer_search_info_box,
                 text="Cannabis Clients",
                 bg="#e0fcf4",
                 fg="#613a3a",
                 font=self.search_table_field_font).grid(row=0, column=0)
        Tk.Label(self.customer_list_display_frame,
                 text="Client",
                 bg="#e0fcf4",
                 fg="#613a3a",
                 font=self.search_table_field_font).grid(row=0, column=0, sticky=Tk.W)
        Tk.Label(self.customer_list_display_frame,
                 text="Organization",
                 bg="#e0fcf4",
                 fg="#613a3a",
                 font=self.search_table_field_font).grid(row=0, column=1, sticky=Tk.W, padx=15)
        self.customer_search_info_box.grid(row=0, column=0, sticky=Tk.W)

    def get_full_customer_list(self):
        display_all_customers_canvas = Tk.Canvas(self.customer_page_main_frame,
                                                 width=1180,
                                                 height=750,
                                                 scrollregion=(0, 0, 0, 20000),
                                                 bg="#e0fcf4",
                                                 highlightbackground="#e0fcf4")
        all_entries_scroll = Tk.Scrollbar(self.customer_page_main_frame,
                                          orient="vertical",
                                          command=display_all_customers_canvas.yview,
                                          bg='#e0fcf4')
        self.customer_list_display_frame = Tk.Frame(self,
                                                    bg='#e0fcf4') # I don't understand why this needs to be here
        display_all_customers_canvas.configure(yscrollcommand=all_entries_scroll.set)
        all_entries_scroll.pack(side='right',
                                fill='y')
        display_all_customers_canvas.pack(side="left",
                                          fill='y')
        display_all_customers_canvas.create_window((0, 0),
                                                   window=self.customer_list_display_frame,
                                                   anchor='nw')
        row_counter = 1
        for item in self.Selection.select_all_from_customer_table_descending(7):
            Tk.Button(self.customer_list_display_frame,
                      text=item[2],
                      bg="#e0fcf4",
                      font=self.search_table_results_font,
                      command=lambda item=item: self.parent.display_client_page(item),
                      ).grid(row=row_counter, column=0, sticky=Tk.W)
            if item[1] == str(0):
                pass
            else:
                Tk.Label(self.customer_list_display_frame,
                         text=item[1],
                         bg="#e0fcf4",
                         font=self.search_table_results_font).grid(row=row_counter, column=1, sticky=Tk.W, padx=15)
            row_counter += 1
        self.customer_page_main_frame.grid(row=1, column=0)




