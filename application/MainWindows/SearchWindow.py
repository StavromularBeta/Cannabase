import tkinter as Tk
import datetime
import os, sys, inspect
# below 3 lines add the parent directory to the path, so that SQL_functions can be found.
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
parentdir = os.path.dirname(parentdir)
sys.path.insert(0, parentdir+'/sql_files/')
import selection as sel
import addel as addel
from tkinter import font as tkFont


class SearchWindow(Tk.Frame):
    def __init__(self, parent, **kwargs):
        Tk.Frame.__init__(self, parent, **kwargs)
        self.parent = parent
        self.config(bg="#e0fcf4")
        self.jobs_display_frame = Tk.Frame(self, bg="#7afdd6")
        self.search_frame = Tk.Frame(self, borderwidth=1, relief='solid', bg='#e0fcf4')
        self.all_jobs_display_frame = Tk.Frame(self, bg="#7afdd6")
        self.selection = sel.Selection()
        self.add_delete = addel.AdDel()
        self.search_table_field_font = tkFont.Font(size=18, weight='bold')
        self.search_table_results_font = tkFont.Font(size=12, weight='bold')
        self.job_id_font = tkFont.Font(size=15)
        self.test_converter = {2: "Metal",
                               3: "Potency",
                               33: "dPotency",
                               4: "Toxins",
                               5: "Pests",
                               7: "Terps",
                               8: "Solv",
                               9: "Oth"
                               }

    def clear_search_window(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.jobs_display_frame = Tk.Frame(self, bg="#7afdd6")
        self.search_frame = Tk.Frame(self, borderwidth=1, relief='solid', bg='#e0fcf4')
        self.all_jobs_display_frame = Tk.Frame(self, bg="#7afdd6")

    def display_all_jobs(self, search=None, archive=None):
        self.clear_search_window()
        display_all_jobs_canvas = Tk.Canvas(self.jobs_display_frame,
                                            width=1180,
                                            height=700,
                                            scrollregion=(0, 0, 0, 2000),
                                            bg="#e0fcf4",
                                            highlightbackground="#e0fcf4")
        all_entries_scroll = Tk.Scrollbar(self.jobs_display_frame,
                                          orient="vertical",
                                          command=display_all_jobs_canvas.yview,
                                          bg='#e0fcf4')
        self.all_jobs_display_frame = Tk.Frame(self,
                                               bg='#e0fcf4')  # I don't understand why this needs to be here.
        display_all_jobs_canvas.configure(yscrollcommand=all_entries_scroll.set)
        all_entries_scroll.pack(side='right',
                                fill='y')
        display_all_jobs_canvas.pack(side="left",
                                     fill='y')
        display_all_jobs_canvas.create_window((0, 0),
                                              window=self.all_jobs_display_frame,
                                              anchor='nw')
        Tk.Label(self.all_jobs_display_frame,
                 text="W#",
                 fg='#613a3a',
                 font=self.search_table_field_font,
                 highlightbackground="#e0fcf4",
                 bg="#e0fcf4").grid(row=0, column=0, sticky=Tk.W, padx=2, pady=2)
        Tk.Label(self.all_jobs_display_frame,
                 text="Tests",
                 fg='#613a3a',
                 font=self.search_table_field_font,
                 highlightbackground="#e0fcf4",
                 bg="#e0fcf4").grid(row=0, column=1, sticky=Tk.W, padx=2, pady=2)
        Tk.Label(self.all_jobs_display_frame,
                 text="Client",
                 fg='#613a3a',
                 font=self.search_table_field_font,
                 highlightbackground="#e0fcf4",
                 bg="#e0fcf4").grid(row=0, column=4, sticky=Tk.W, padx=2, pady=2)
        Tk.Label(self.all_jobs_display_frame,
                 text="Submission Date",
                 fg='#613a3a',
                 font=self.search_table_field_font,
                 highlightbackground="#e0fcf4",
                 bg="#e0fcf4").grid(row=0, column=2, sticky=Tk.E, padx=2, pady=2)
        Tk.Label(self.all_jobs_display_frame,
                 text="Complete Date",
                 fg='#613a3a',
                 font=self.search_table_field_font,
                 highlightbackground="#e0fcf4",
                 bg="#e0fcf4").grid(row=0, column=3, sticky=Tk.W, padx=2, pady=2)
        if search:
            self.return_jobs(search)
        if archive:
            self.return_jobs(archive=True)
        else:
            self.return_jobs()
        self.jobs_display_frame.grid(row=1, column=0, pady=5)

    def return_jobs(self, search=None, archive=None):
        if search:
            all_jobs_data = search
        elif archive:
            all_jobs_data = self.selection.select_all_from_table_descending(4)
        else:
            all_jobs_data = self.selection.select_all_from_table_descending(1)
        first_customer_row = 1
        for item in all_jobs_data:
            job_number = item[1]
            tests = item[2]
            tests = self.convert_testnumber_to_string(tests)
            client_name = item[3]
            date_submitted = item[4]
            if str(item[6]) == '2000-01-01':
                complete_date = "Incomplete"
            else:
                complete_date = item[6]
            if (first_customer_row % 2) == 1:
                Tk.Button(self.all_jobs_display_frame,
                          text=job_number,
                          command=lambda item=item: self.parent.display_jobpage(item),
                          highlightbackground="#e0fcf4",
                          font=self.search_table_results_font,
                          bg="#e0fcf4").grid(row=first_customer_row,
                                             column=0,
                                             sticky=Tk.W,
                                             padx=2,
                                             pady=2)
                Tk.Label(self.all_jobs_display_frame,
                         text=tests,
                         highlightbackground="#e0fcf4",
                         font=self.search_table_results_font,
                         bg="#e0fcf4").grid(row=first_customer_row, column=1, sticky=Tk.W, padx=2, pady=2)
                Tk.Label(self.all_jobs_display_frame,
                         text=client_name,
                         highlightbackground="#e0fcf4",
                         font=self.search_table_results_font,
                         bg="#e0fcf4").grid(row=first_customer_row, column=4, sticky=Tk.W, padx=2, pady=2)
                Tk.Label(self.all_jobs_display_frame,
                         text=date_submitted,
                         highlightbackground="#e0fcf4",
                         font=self.search_table_results_font,
                         bg="#e0fcf4").grid(row=first_customer_row, column=2, sticky=Tk.E, padx=2, pady=2)
                if complete_date == "Incomplete":
                    Tk.Label(self.all_jobs_display_frame,
                             fg='#FF0000',
                             text=complete_date,
                             highlightbackground="#e0fcf4",
                             font=self.search_table_results_font,
                             bg="#e0fcf4").grid(row=first_customer_row, column=3, sticky=Tk.W, padx=2, pady=2)
                else:
                    Tk.Label(self.all_jobs_display_frame,
                             text=complete_date,
                             highlightbackground="#e0fcf4",
                             font=self.search_table_results_font,
                             bg="#e0fcf4").grid(row=first_customer_row, column=3, sticky=Tk.W, padx=2, pady=2)
                first_customer_row += 1
            else:
                Tk.Button(self.all_jobs_display_frame,
                          text=job_number,
                          command=lambda item=item: self.parent.display_jobpage(item),
                          fg='#613a3a',
                          highlightbackground="#e0fcf4",
                          font=self.search_table_results_font,
                          bg="#e0fcf4").grid(row=first_customer_row,
                                             column=0,
                                             sticky=Tk.W,
                                             padx=2,
                                             pady=2)
                Tk.Label(self.all_jobs_display_frame,
                         text=tests,
                         fg='#613a3a',
                         highlightbackground="#e0fcf4",
                         font=self.search_table_results_font,
                         bg="#e0fcf4").grid(row=first_customer_row, column=1, sticky=Tk.W, padx=2, pady=2)
                Tk.Label(self.all_jobs_display_frame,
                         text=client_name,
                         fg='#613a3a',
                         highlightbackground="#e0fcf4",
                         font=self.search_table_results_font,
                         bg="#e0fcf4").grid(row=first_customer_row, column=4, sticky=Tk.W, padx=2, pady=2)
                Tk.Label(self.all_jobs_display_frame,
                         text=date_submitted,
                         fg='#613a3a',
                         highlightbackground="#e0fcf4",
                         font=self.search_table_results_font,
                         bg="#e0fcf4").grid(row=first_customer_row, column=2, sticky=Tk.E, padx=2, pady=2)
                if complete_date == "Incomplete":
                    Tk.Label(self.all_jobs_display_frame,
                             fg='#FF0000',
                             text=complete_date,
                             highlightbackground="#e0fcf4",
                             font=self.search_table_results_font,
                             bg="#e0fcf4").grid(row=first_customer_row, column=3, sticky=Tk.W, padx=2, pady=2)
                else:
                    Tk.Label(self.all_jobs_display_frame,
                             text=complete_date,
                             fg='#613a3a',
                             highlightbackground="#e0fcf4",
                             font=self.search_table_results_font,
                             bg="#e0fcf4").grid(row=first_customer_row, column=3, sticky=Tk.W, padx=2, pady=2)
                first_customer_row += 1

    def search_jobs(self, archive=None):
        self.search_frame = Tk.Frame(self, bg='#e0fcf4')
        if archive:
            Tk.Label(self.search_frame,
                     text="Search Archived Jobs",
                     font=self.search_table_field_font,
                     fg="#613a3a",
                     bg="#e0fcf4").grid(row=0, column=0)
        else:
            Tk.Label(self.search_frame,
                     text="Search Current Jobs",
                     font=self.search_table_field_font,
                     fg="#613a3a",
                     bg="#e0fcf4").grid(row=0, column=0)
        search_result_frame = Tk.Frame(self.search_frame, bg="#e0fcf4")
        search_result_frame.grid(row=1, column=0, columnspan=3, padx=5, ipadx=2, ipady=2, pady=5)
        self.option_variable = Tk.StringVar(search_result_frame)
        self.option_variable.set('Job Number')
        search_options = Tk.OptionMenu(search_result_frame, self.option_variable, "Job Number", "Active", "Client Name")
        search_options.config(font=self.search_table_results_font)
        search_options["menu"].config(font=self.search_table_results_font)
        search_options.config(bg="#e0fcf4")
        search_options["menu"].config(bg="#e0fcf4")
        search_options["menu"].config(fg="#613a3a")
        search_options.grid(row=0)
        self.search_entry_field = Tk.Entry(search_result_frame,
                                           highlightbackground="#e0fcf4",
                                           font=self.search_table_results_font)
        self.search_entry_field.grid(row=0, column=1)
        Tk.Button(search_result_frame,
                  text="Archive Jobs",
                  command=self.archive_jobs,
                  highlightbackground="#e0fcf4",
                  font=self.search_table_results_font).grid(row=0, column=2, sticky=Tk.E)
        Tk.Button(search_result_frame,
                  text="search",
                  command=self.search_database_for_jobs,
                  highlightbackground="#e0fcf4",
                  font=self.search_table_results_font).grid(row=1, column=0, sticky=Tk.E)
        Tk.Button(search_result_frame,
                  text="all",
                  command=self.parent.display_searchpage,
                  highlightbackground="#e0fcf4",
                  font=self.search_table_results_font).grid(row=1, column=1, sticky=Tk.W)
        self.search_frame.grid(row=0, column=0, sticky=Tk.NW)

    def search_database_for_jobs(self):
        search_type = self.option_variable.get()
        entry_field = self.search_entry_field.get()
        if search_type == "Job Number":
            search_results = self.selection.select_from_cannajobs_table_with_conditions(2, (entry_field,))
        elif search_type == "Active":
            search_results = self.selection.select_from_cannajobs_table_with_conditions(6, (entry_field,))
        elif search_type == "Client Name":
            search_results = self.selection.select_from_cannajobs_table_with_conditions(4, (entry_field,))
        self.parent.display_searchpage(search_results)

    def convert_testnumber_to_string(self, tests):
        tests_list_numbers = tests.split(",")
        tests_list_strings = []
        for item in tests_list_numbers:
            tests_list_strings.append(self.test_converter[int(item)])
        return ', '.join(tests_list_strings)

    def archive_jobs(self):
        self.add_delete.archive_cannajob_entry()
        self.add_delete.archive_cannajob_tests_entry()
        self.add_delete.archive_cannajob_test_notes_entry()


