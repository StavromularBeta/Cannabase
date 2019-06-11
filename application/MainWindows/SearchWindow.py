import tkinter as Tk
import sys
sys.path.append("/Users/PeterLevett/PycharmProjects/Cannabase/Cannabase/sql_files")
import selection as sel


class SearchWindow(Tk.Frame):
    def __init__(self, parent):
        Tk.Frame.__init__(self, parent)
        self.parent = parent
        self.jobs_display_frame = Tk.Frame(self)
        self.search_frame = Tk.Frame(self)
        self.all_jobs_display_frame = Tk.Frame(self)
        self.selection = sel.Selection()

    def clear_search_window(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.jobs_display_frame = Tk.Frame(self)
        self.search_frame = Tk.Frame(self)
        self.all_jobs_display_frame = Tk.Frame(self)


        # job number, receive date, tests, status
    def display_all_jobs(self, search=None):
        self.clear_search_window()
        display_all_jobs_canvas = Tk.Canvas(self.jobs_display_frame, width=450, height=800, scrollregion=(0, 0, 0, 2000))
        all_entries_scroll = Tk.Scrollbar(self.jobs_display_frame, orient="vertical", command=display_all_jobs_canvas.yview)
        self.all_jobs_display_frame = Tk.Frame(self)  # I don't understand why this needs to be here.
        display_all_jobs_canvas.configure(yscrollcommand=all_entries_scroll.set)
        all_entries_scroll.pack(side='right', fill='y')
        display_all_jobs_canvas.pack(side="left", fill='y')
        display_all_jobs_canvas.create_window((0, 0), window=self.all_jobs_display_frame, anchor='nw')
        Tk.Label(self.all_jobs_display_frame, text="Job Number").grid(row=0, column=0)
        Tk.Label(self.all_jobs_display_frame, text="Tests").grid(row=0, column=1)
        Tk.Label(self.all_jobs_display_frame, text="Submission Date").grid(row=0, column=2)
        Tk.Label(self.all_jobs_display_frame, text="Status").grid(row=0, column=3)
        Tk.Label(self.all_jobs_display_frame, text="Complete Date").grid(row=0, column=4)
        if search:
            self.return_jobs(search)
        else:
            self.return_jobs()
        self.jobs_display_frame.grid(row=0, column=0)

    def return_jobs(self, search=None):
        if search:
            all_jobs_data = search
        else:
            all_jobs_data = self.selection.select_all_from_table(1)
        first_customer_row = 1
        for item in all_jobs_data:
            job_number = item[1]
            tests = item[2]
            date_submitted = item[3]
            status = item[4]
            complete_date = item[5]
            Tk.Button(self.all_jobs_display_frame,
                      text=job_number,
                      command=lambda item=item: self.parent.display_jobpage(item)).grid(row=first_customer_row, column=0)
            Tk.Label(self.all_jobs_display_frame, text=tests).grid(row=first_customer_row, column=1)
            Tk.Label(self.all_jobs_display_frame, text=date_submitted).grid(row=first_customer_row, column=2)
            Tk.Label(self.all_jobs_display_frame, text=status).grid(row=first_customer_row, column=3)
            Tk.Label(self.all_jobs_display_frame, text=complete_date).grid(row=first_customer_row, column=4)
            first_customer_row += 1

    def search_jobs(self):
        self.search_frame = Tk.Frame(self)
        Tk.Label(self.search_frame, text="Search Jobs").grid(row=0, column=0)
        search_result_frame = Tk.Frame(self.search_frame)
        search_result_frame.grid(row=1, column=0, columnspan=3)
        self.option_variable = Tk.StringVar(search_result_frame)
        self.option_variable.set('Job Number')
        search_options = Tk.OptionMenu(search_result_frame, self.option_variable, "Job Number", "Active")
        search_options.grid(row=0)
        self.search_entry_field = Tk.Entry(search_result_frame)
        self.search_entry_field.grid(row=0, column=1)
        Tk.Button(search_result_frame, text="search", command=self.search_database_for_jobs).grid(row=0, column=2)
        Tk.Button(search_result_frame, text="all", command=self.parent.display_searchpage).grid(row=0, column=3)
        self.search_frame.grid(row=0, column=1, sticky=Tk.NW)

    def search_database_for_jobs(self):
        search_type = self.option_variable.get()
        entry_field = self.search_entry_field.get()
        if search_type == "Job Number":
            search_results = self.selection.select_from_cannajobs_table_with_conditions(2, (entry_field,))
        elif search_type == "Active":
            search_results = self.selection.select_from_cannajobs_table_with_conditions(5, (entry_field,))
        self.parent.display_searchpage(search_results)

