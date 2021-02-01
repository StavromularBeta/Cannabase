import tkinter as Tk
import os, sys, inspect
# below 3 lines add the parent directory to the path, so that SQL_functions can be found.
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
parentdir = os.path.dirname(parentdir)
sys.path.insert(0, parentdir+'/sql_files/')
import editentry
import selection
import datetime
import addel
from tkinter import font as tkFont


class CustomerpageWindow(Tk.Frame):
    def __init__(self, parent, **kwargs):
        Tk.Frame.__init__(self, parent, **kwargs)
        self.parent = parent
        self.config(bg="#e0fcf4")
        self.edit_entry = editentry.EditEntry()
        self.selection = selection.Selection()
        self.addel = addel.AdDel()
        self.search_table_field_font = tkFont.Font(size=18, weight='bold')
        self.search_table_results_font = tkFont.Font(size=12, weight='bold')
        self.test_converter = {2: "Metals (ICP)",
                               3: "Basic Potency",
                               33: "Deluxe Potency",
                               4: "Afloxtoxins",
                               5: "Pesticides",
                               7: "Terpenes",
                               8: "Solvents",
                               9: "Other Tests",
                               1: "Micro A",
                               6: "Micro B",
                               10: "Fungal ID",
                               11: "Shrooms"
                               }
        self.main_customerpage_frame = Tk.Frame(self)
        self.customer_scroll_frame_canvas = Tk.Frame(self)
        self.customer_scroll_frame = Tk.Frame(self)

    def clear_customerpage_window(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.customer_scroll_frame_canvas = Tk.Frame(self)
        self.customer_scroll_frame = Tk.Frame(self)
        self.main_customerpage_frame = Tk.Frame(self)

    def generate_customerpage(self, client, view=None):
        self.clear_customerpage_window()
        self.create_scrolling_window()
        self.populate_customer_information_box(client)
        if view:
            self.gather_customer_jobs(client, view=True)
        else:
            self.gather_customer_jobs(client)
        self.main_customerpage_frame.grid(row=0, sticky=Tk.W)
        self.customer_scroll_frame.grid(row=1)
        self.filler_canvas = Tk.Canvas(self, bg="#e0fcf4", highlightbackground="#e0fcf4", width=1100, height=600)
        self.filler_canvas.grid(row=4, column=4, columnspan=1)

    def create_scrolling_window(self):
        display_all_customers_canvas = Tk.Canvas(self.customer_scroll_frame,
                                                 width=1180,
                                                 height=650,
                                                 scrollregion=(0, 0, 0, 20000),
                                                 bg="#e0fcf4",
                                                 highlightbackground="#e0fcf4")
        all_entries_scroll = Tk.Scrollbar(self.customer_scroll_frame,
                                          orient="vertical",
                                          command=display_all_customers_canvas.yview,
                                          bg='#e0fcf4')
        self.customer_scroll_frame_canvas = Tk.Frame(self,
                                                    bg='#e0fcf4')  # I don't understand why this needs to be here
        display_all_customers_canvas.configure(yscrollcommand=all_entries_scroll.set)
        all_entries_scroll.pack(side='right',
                                fill='y')
        display_all_customers_canvas.pack(side="left",
                                          fill='y')
        display_all_customers_canvas.create_window((0, 0),
                                                   window=self.customer_scroll_frame_canvas,
                                                   anchor='nw')

    def populate_customer_information_box(self, client):
        Tk.Label(self.main_customerpage_frame,
                 text=client[2],
                 font=self.search_table_field_font,
                 bg='#e0fcf4').grid(sticky=Tk.W)

    def gather_customer_jobs(self, client, view=None):
        Tk.Label(self.customer_scroll_frame_canvas,
                 text="Active Jobs",
                 font=self.search_table_field_font,
                 bg='#e0fcf4').grid(row=0, columnspan=3, sticky=Tk.W)
        rowcounter = 1
        for item in self.selection.select_from_cannajobs_table_with_conditions_equals(4, (client[2],)):
            if view:
                Tk.Button(self.customer_scroll_frame_canvas,
                          text=item[1],
                          command=lambda item=item: self.parent.display_jobpage(item, view=True),
                          font=self.search_table_results_font,
                          bg='#e0fcf4').grid(row=rowcounter, column=0)
            else:
                Tk.Button(self.customer_scroll_frame_canvas,
                          text=item[1],
                          command=lambda item=item: self.parent.display_jobpage(item),
                          font=self.search_table_results_font,
                          bg='#e0fcf4').grid(row=rowcounter, column=0)
            testlist = []
            for subitem in item[2].split(","):
                testlist.append(self.test_converter[int(subitem)])
                Tk.Label(self.customer_scroll_frame_canvas,
                         text=", ".join(testlist),
                         font=self.search_table_results_font,
                         bg='#e0fcf4').grid(row=rowcounter, column=1)
            Tk.Label(self.customer_scroll_frame_canvas,
                     text=str(item[4]),
                     font=self.search_table_results_font,
                     bg='#e0fcf4').grid(row=rowcounter, column=2)
            rowcounter += 1
        Tk.Label(self.customer_scroll_frame_canvas,
                 text="Archived Jobs",
                 font=self.search_table_field_font,
                 bg='#e0fcf4').grid(row=rowcounter, columnspan=3, sticky=Tk.W)
        rowcounter += 1
        for year in ['2021', '2020']:
            for item in self.selection.select_from_cannajobs_archive_table_with_conditions_equals_year(year, 4, (client[2],)):
                if view:
                    Tk.Button(self.customer_scroll_frame_canvas,
                              text=item[1],
                              command=lambda item=item: self.parent.display_jobpage(item, archive=True, view=True),
                              font=self.search_table_results_font,
                              bg='#e0fcf4').grid(row=rowcounter, column=0)
                else:
                    Tk.Button(self.customer_scroll_frame_canvas,
                              text=item[1],
                              command=lambda item=item: self.parent.display_jobpage(item, archive=True),
                              font=self.search_table_results_font,
                              bg='#e0fcf4').grid(row=rowcounter, column=0)
                testlist = []
                for subitem in item[2].split(","):
                    testlist.append(self.test_converter[int(subitem)])
                    Tk.Label(self.customer_scroll_frame_canvas,
                             text=", ".join(testlist),
                             font=self.search_table_results_font,
                             bg='#e0fcf4').grid(row=rowcounter, column=1)
                Tk.Label(self.customer_scroll_frame_canvas,
                         text=str(item[4]),
                         font=self.search_table_results_font,
                         bg='#e0fcf4').grid(row=rowcounter, column=2)
                rowcounter += 1

