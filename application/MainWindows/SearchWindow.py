import tkinter as Tk
import datetime
import os, sys, inspect
import tempfile
import win32api
import win32print
# below 3 lines add the parent directory to the path, so that SQL_functions can be found.
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
parentdir = os.path.dirname(parentdir)
sys.path.insert(0, parentdir + '/sql_files/')
import selection as sel
import addel as addel
from tkinter import font as tkFont


class SearchWindow(Tk.Frame):
    def __init__(self, parent, **kwargs):
        Tk.Frame.__init__(self, parent, **kwargs)
        self.print_filter_jobs = []
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
                               9: "Oth",
                               1: "M.A",
                               6: "M.B",
                               10: "F.ID",
                               11: "Mushrooms"
                               }

    def clear_search_window(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.jobs_display_frame = Tk.Frame(self, bg="#7afdd6")
        self.search_frame = Tk.Frame(self, borderwidth=1, relief='solid', bg='#e0fcf4')
        self.all_jobs_display_frame = Tk.Frame(self, bg="#7afdd6")
        self.test_filter_frame = Tk.Frame(self.search_frame, bg="#e0fcf4")

    def display_all_jobs(self, search=None, archive=None, view=None, want_full_archives=None):
        self.clear_search_window()
        display_all_jobs_canvas = Tk.Canvas(self.jobs_display_frame,
                                            width=1200,
                                            height=500,
                                            scrollregion=(0, 0, 0, 50000),
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
        if search and archive:
            if view:
                self.return_jobs(search, archive=True, view=True)
            else:
                self.return_jobs(search, archive=True)
        elif search:
            if view:
                self.return_jobs(search, view=True)
            else:
                self.return_jobs(search)
        elif archive and want_full_archives:
            if view:
                self.return_jobs(archive=True, view=True)
            else:
                self.return_jobs(archive=True)
        elif archive:
            pass
        else:
            if view:
                self.return_jobs(view=True)
            else:
                self.return_jobs()
        self.jobs_display_frame.grid(row=1, column=0, pady=5)
        self.filler_canvas = Tk.Canvas(self, bg="#e0fcf4", highlightbackground="#e0fcf4", width=1100, height=600)
        self.filler_canvas.grid(row=4, column=4, columnspan=1)

    def return_jobs(self, search=None, archive=None, view=None):
        all_jobs_data_list = []
        years_list = ['2021', '2020']
        if search:
            for item in search:
                all_jobs_data = item
                all_jobs_data_list.append(all_jobs_data)
        for item in years_list:
            # Moved this above the for loop, so that anything searched doesn't get displayed twice. 23Apr21
            # if search:
            #    all_jobs_data = search
            #    all_jobs_data_list.append(all_jobs_data)
            if archive and search:
                break
            elif archive:
                all_jobs_data = self.selection.select_from_cannajobs_archive_table_year(item)
                all_jobs_data_list.append(all_jobs_data)
            else:
                all_jobs_data = self.selection.select_all_from_table_descending(1)
                if len(all_jobs_data_list) < 1:
                    all_jobs_data_list.append(all_jobs_data)
        first_customer_row = 1
        for all_jobs_data in all_jobs_data_list:
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
                    if archive:
                        if view:
                            Tk.Button(self.all_jobs_display_frame,
                                      text=job_number,
                                      command=lambda item=item: self.parent.display_jobpage(item, archive=True, view=True),
                                      highlightbackground="#e0fcf4",
                                      font=self.search_table_results_font,
                                      bg="#e0fcf4").grid(row=first_customer_row,
                                                         column=0,
                                                         sticky=Tk.W,
                                                         padx=2,
                                                         pady=2)
                        else:
                            Tk.Button(self.all_jobs_display_frame,
                                      text=job_number,
                                      command=lambda item=item: self.parent.display_jobpage(item, archive=True),
                                      highlightbackground="#e0fcf4",
                                      font=self.search_table_results_font,
                                      bg="#e0fcf4").grid(row=first_customer_row,
                                                         column=0,
                                                         sticky=Tk.W,
                                                         padx=2,
                                                         pady=2)
                    else:
                        if view:
                            Tk.Button(self.all_jobs_display_frame,
                                      text=job_number,
                                      command=lambda item=item: self.parent.display_jobpage(item, view=True),
                                      highlightbackground="#e0fcf4",
                                      font=self.search_table_results_font,
                                      bg="#e0fcf4").grid(row=first_customer_row,
                                                         column=0,
                                                         sticky=Tk.W,
                                                         padx=2,
                                                         pady=2)
                        else:
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
                    if archive:
                        if view:
                            Tk.Button(self.all_jobs_display_frame,
                                      text=job_number,
                                      command=lambda item=item: self.parent.display_jobpage(item, archive=True, view=True),
                                      fg='#613a3a',
                                      highlightbackground="#e0fcf4",
                                      font=self.search_table_results_font,
                                      bg="#e0fcf4").grid(row=first_customer_row,
                                                         column=0,
                                                         sticky=Tk.W,
                                                         padx=2,
                                                         pady=2)
                        else:
                            Tk.Button(self.all_jobs_display_frame,
                                      text=job_number,
                                      command=lambda item=item: self.parent.display_jobpage(item, archive=True),
                                      fg='#613a3a',
                                      highlightbackground="#e0fcf4",
                                      font=self.search_table_results_font,
                                      bg="#e0fcf4").grid(row=first_customer_row,
                                                         column=0,
                                                         sticky=Tk.W,
                                                         padx=2,
                                                         pady=2)
                    else:
                        if view:
                            Tk.Button(self.all_jobs_display_frame,
                                      text=job_number,
                                      command=lambda item=item: self.parent.display_jobpage(item, view=True),
                                      fg='#613a3a',
                                      highlightbackground="#e0fcf4",
                                      font=self.search_table_results_font,
                                      bg="#e0fcf4").grid(row=first_customer_row,
                                                         column=0,
                                                         sticky=Tk.W,
                                                         padx=2,
                                                         pady=2)
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

    def search_jobs(self, archive=None, view=None):
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
        if archive or view:
            pass
        else:
            Tk.Button(search_result_frame,
                      text="Archive Jobs",
                      command=self.archive_jobs,
                      highlightbackground="#e0fcf4",
                      font=self.search_table_results_font).grid(row=0, column=2, sticky=Tk.E)
        if archive or view:
            pass
        else:
            Tk.Button(search_result_frame,
                      text="Delete Archived Jobs",
                      command=self.delete_archived_jobs_from_current_table,
                      highlightbackground="#e0fcf4",
                      font=self.search_table_results_font).grid(row=0, column=3, sticky=Tk.W)
        if archive:
            Tk.Button(search_result_frame,
                      text="search archives",
                      command=lambda: self.search_database_for_jobs(archive=True),
                      highlightbackground="#e0fcf4",
                      font=self.search_table_results_font).grid(row=1, column=0, sticky=Tk.E)
        else:
            Tk.Button(search_result_frame,
                      text="search active",
                      command=self.search_database_for_jobs,
                      highlightbackground="#e0fcf4",
                      font=self.search_table_results_font).grid(row=1, column=0, sticky=Tk.E)
        if archive:
            Tk.Button(search_result_frame,
                      text="all archives (SLOW)",
                      command=lambda: self.parent.display_searchpage(archive=True, want_full_archives=True),
                      highlightbackground="#e0fcf4",
                      font=self.search_table_results_font).grid(row=1, column=1, sticky=Tk.W)
        else:
            Tk.Button(search_result_frame,
                      text="all active",
                      command=self.parent.display_searchpage,
                      highlightbackground="#e0fcf4",
                      font=self.search_table_results_font).grid(row=1, column=1, sticky=Tk.W)
            Tk.Button(search_result_frame,
                      text="print active",
                      command=self.print_active_jobs_list,
                      highlightbackground="#e0fcf4",
                      font=self.search_table_results_font).grid(row=1, column=2, sticky=Tk.W)
            Tk.Button(search_result_frame,
                      text="print filtered",
                      command=self.print_filtered_active_jobs_list,
                      highlightbackground="#e0fcf4",
                      font=self.search_table_results_font).grid(row=1, column=3, sticky=Tk.W)
        filter_checkboxes_frame = Tk.Frame(self.search_frame, bg='#e0fcf4')
        filter_checkboxes_frame.grid(row=2, column=0, columnspan=3, padx=5, ipadx=2, ipady=2, pady=5)
        # Checkboxes
        self.metals = Tk.IntVar()
        self.metals_checkbox = Tk.Checkbutton(filter_checkboxes_frame,
                                              text='2) metals',
                                              variable=self.metals,
                                              bg='#e0fcf4').grid(row=0, column=1)
        self.basic_potency = Tk.IntVar()
        self.basic_potency_checkbox = Tk.Checkbutton(filter_checkboxes_frame,
                                                     text='3) basic potency',
                                                     variable=self.basic_potency,
                                                     bg='#e0fcf4').grid(row=0, column=2)
        self.deluxe_potency = Tk.IntVar()
        self.deluxe_potency_checkbox = Tk.Checkbutton(filter_checkboxes_frame,
                                                      text='3a) deluxe potency',
                                                      variable=self.deluxe_potency,
                                                      bg='#e0fcf4').grid(row=0, column=3)
        self.toxins = Tk.IntVar()
        self.toxins_checkbox = Tk.Checkbutton(filter_checkboxes_frame,
                                              text='4) Aflotoxins',
                                              variable=self.toxins,
                                              bg='#e0fcf4').grid(row=0, column=4)
        self.pesticides = Tk.IntVar()
        self.pesticides_checkbox = Tk.Checkbutton(filter_checkboxes_frame,
                                                  text='5) Pesticides',
                                                  variable=self.pesticides,
                                                  bg='#e0fcf4').grid(row=0, column=5)
        self.terpenes = Tk.IntVar()
        self.terpenes_checkbox = Tk.Checkbutton(filter_checkboxes_frame,
                                                text='7) Terpenes',
                                                variable=self.terpenes,
                                                bg='#e0fcf4').grid(row=1, column=1)
        self.solvents = Tk.IntVar()
        self.solvents_checkbox = Tk.Checkbutton(filter_checkboxes_frame,
                                                text='8) Solvents',
                                                variable=self.solvents,
                                                bg='#e0fcf4').grid(row=1, column=2)
        self.other = Tk.IntVar()
        self.other_checkbox = Tk.Checkbutton(filter_checkboxes_frame,
                                             text='Other',
                                             variable=self.other,
                                             bg='#e0fcf4').grid(row=1, column=3)
        self.micro_a = Tk.IntVar()
        self.micro_a_checkbox = Tk.Checkbutton(filter_checkboxes_frame,
                                               text='1) Micro A',
                                               variable=self.micro_a,
                                               bg='#e0fcf4').grid(row=0, column=0)
        self.micro_b = Tk.IntVar()
        self.micro_b_checkbox = Tk.Checkbutton(filter_checkboxes_frame,
                                               text='6) Micro B',
                                               variable=self.micro_b,
                                               bg='#e0fcf4').grid(row=1, column=0)
        self.fungal_id = Tk.IntVar()
        self.fungal_id_checkbox = Tk.Checkbutton(filter_checkboxes_frame,
                                                 text='Fungal ID',
                                                 variable=self.fungal_id,
                                                 bg='#e0fcf4').grid(row=1, column=4)
        self.mushrooms = Tk.IntVar()
        self.mushrooms_checkbox = Tk.Checkbutton(filter_checkboxes_frame,
                                                 text='Psilocybin',
                                                 variable=self.mushrooms,
                                                 bg='#e0fcf4').grid(row=1, column=5)
        if archive:
            Tk.Button(filter_checkboxes_frame,
                      text="Filter by Test (ONLY)",
                      command=lambda: self.filter_jobs_by_test(archive=True,
                                                               and_or_status="ONLY")).grid(row=2, column=0)
            Tk.Button(filter_checkboxes_frame,
                      text="Filter by Test (AND)",
                      command=lambda: self.filter_jobs_by_test(archive=True,
                                                               and_or_status="AND")).grid(row=2, column=1)
            Tk.Button(filter_checkboxes_frame,
                      text="Filter by Test (OR)",
                      command=lambda: self.filter_jobs_by_test(archive=True)).grid(row=2, column=2)
        else:
            Tk.Button(filter_checkboxes_frame,
                      text="Filter by Test (ONLY)",
                      command=lambda: self.filter_jobs_by_test(and_or_status="ONLY")).grid(row=2, column=0)
            Tk.Button(filter_checkboxes_frame,
                      text="Filter by Test (AND)",
                      command=lambda: self.filter_jobs_by_test(and_or_status="AND")).grid(row=2, column=1)
            Tk.Button(filter_checkboxes_frame,
                      text="Filter by Test (OR)",
                      command=self.filter_jobs_by_test).grid(row=2, column=2)
        self.search_frame.grid(row=0, column=0, sticky=Tk.NW)

    def search_database_for_jobs(self, archive=None):
        search_type = self.option_variable.get()
        entry_field = self.search_entry_field.get()
        if archive:
            search_results_list = []
            for item in ['2020','2021']:
                if search_type == "Job Number":
                    search_results = self.selection.select_from_cannajobs_archive_table_with_conditions_year(item, 2, (entry_field,))
                elif search_type == "Active":
                    search_results = self.selection.select_from_cannajobs_archive_table_with_conditions_year(item, 6, (entry_field,))
                elif search_type == "Client Name":
                    search_results = self.selection.select_from_cannajobs_archive_table_with_conditions_year(item, 4, (
                    '%' + entry_field + '%',))
                search_results_list.append(search_results)
            self.parent.display_searchpage(search_results_list, archive=True)
        else:
            if search_type == "Job Number":
                search_results = self.selection.select_from_cannajobs_table_with_conditions(2, (entry_field,))
            elif search_type == "Active":
                search_results = self.selection.select_from_cannajobs_table_with_conditions(6, (entry_field,))
            elif search_type == "Client Name":
                search_results = self.selection.select_from_cannajobs_table_with_conditions(4,
                                                                                            ('%' + entry_field + '%',))
            self.parent.display_searchpage([search_results])

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

    def delete_archived_jobs_from_current_table(self):
        self.add_delete.delete_archived_cannjob_entry_from_current()
        self.add_delete.delete_archived_cannjob_test__entry_from_current()
        self.add_delete.delete_archived_cannjob_test_notes_entry_from_current()

    def filter_jobs_by_test(self, archive=None, and_or_status=None):
        jobs_to_display = []
        filter_dictionary = {1: self.micro_a.get(),
                             2: self.metals.get(),
                             3: self.basic_potency.get(),
                             33: self.deluxe_potency.get(),
                             4: self.toxins.get(),
                             5: self.pesticides.get(),
                             6: self.micro_b.get(),
                             7: self.terpenes.get(),
                             8: self.solvents.get(),
                             9: self.other.get(),
                             10: self.fungal_id.get(),
                             11: self.mushrooms.get()}
        if archive:
            jobs_to_filter = []
            for item in ['2021','2020']:
                jobs_to_filter.append(self.selection.select_from_cannajobs_archive_table_year(item))
        else:
            jobs_to_filter = [self.selection.select_all_from_table_descending(1)]
        for jobs_list in jobs_to_filter:
            for item in jobs_list:
                tests_string = item[2]
                tests_list = tests_string.split(',')
                if and_or_status == "ONLY":
                    number_of_tests = len(tests_list)
                    number_of_hits = 0
                    checked_box_count = sum(filter_dictionary.values())
                    for subitem in tests_list:
                        if filter_dictionary[int(subitem)] == 1:
                            number_of_hits += 1
                    if number_of_tests == number_of_hits == checked_box_count:
                        print('match!')
                        jobs_to_display.append(item)
                elif and_or_status == "AND":
                    number_of_hits = 0
                    checked_box_count = sum(filter_dictionary.values())
                    for subitem in tests_list:
                        if filter_dictionary[int(subitem)] == 1:
                            number_of_hits += 1
                    if number_of_hits == checked_box_count:
                        print('match!')
                        jobs_to_display.append(item)
                else:
                    for subitem in tests_list:
                        if filter_dictionary[int(subitem)] == 1:
                            jobs_to_display.append(item)
        jobs_to_display = list(dict.fromkeys(jobs_to_display))
        jobs_to_display = [[item] for item in jobs_to_display]
        if archive:
            self.parent.display_searchpage(search=jobs_to_display, archive=True)
        else:
            self.parent.display_searchpage(search=jobs_to_display, print_filter=jobs_to_display)

    def print_active_jobs_list(self):
        filename = tempfile.mktemp(".txt")
        active_jobs = self.selection.select_all_from_table_descending(1)
        file_string = "ACTIVE CANNABIS JOBS LIST (Generated on: " + datetime.date.today().strftime("%d/%m/%Y") + ")\n\n"
        file_string += "JOB       RECEIVED       CLIENT                                                 TESTS\n\n"
        for item in active_jobs:
            client_padding = 55 - len(item[3])
            file_string += "W" + str(item[1]) + "   " + str(item[4]) + "     " + str(item[3]) +\
                           (" "*client_padding) + str(item[2]) + '\n\n'
        print(file_string)
        open(filename, "w").write(file_string)
        win32api.ShellExecute(
            0,
            "print",
            filename,
            '/d:"%s"' % win32print.GetDefaultPrinter(),
            ".",
           0
       )

    def print_filtered_active_jobs_list(self):
        filename = tempfile.mktemp(".txt")
        file_string = "ACTIVE (FILTERED) CANNABIS JOBS LIST (Generated on: " + datetime.date.today().strftime("%d/%m/%Y") + ")\n\n"
        file_string += "JOB       RECEIVED       CLIENT                                                 TESTS\n\n"
        for subitem in self.print_filter_jobs:
            for item in subitem:
                client_padding = 55 - len(item[3])
                file_string += "W" + str(item[1]) + "   " + str(item[4]) + "     " + str(item[3]) +\
                               (" "*client_padding) + str(item[2]) + '\n\n'
        open(filename, "w").write(file_string)
        win32api.ShellExecute(
            0,
            "print",
            filename,
            '/d:"%s"' % win32print.GetDefaultPrinter(),
            ".",
           0
        )
