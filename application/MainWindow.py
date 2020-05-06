import tkinter as Tk
from MainWindows import HomepageWindow as Hpw,\
                        GraphsWindow as Grw,\
                        SearchWindow as Srw,\
                        EditAddWindow as Eaw,\
                        JobpageWindow as Jpw


class MainWindow(Tk.Frame):
    def __init__(self, parent, **kwargs):
        Tk.Frame.__init__(self, parent, **kwargs)
        self.HomepageWindow = Hpw.HomepageWindow(self)
        self.GraphsWindow = Grw.GraphsWindow(self)
        self.SearchWindow = Srw.SearchWindow(self)
        self.EditAddWindow = Eaw.EditAddWindow(self)
        self.JobpageWindow = Jpw.JobpageWindow(self, bg="#e0fcf4")

    def clear_main_window(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.HomepageWindow = Hpw.HomepageWindow(self)
        self.GraphsWindow = Grw.GraphsWindow(self)
        self.SearchWindow = Srw.SearchWindow(self)
        self.EditAddWindow = Eaw.EditAddWindow(self)
        self.JobpageWindow = Jpw.JobpageWindow(self, bg="#e0fcf4")

    def display_homepage(self):
        self.clear_main_window()
        self.HomepageWindow.Homepage()
        self.HomepageWindow.grid()

    def display_graphspage(self):
        self.clear_main_window()
        self.GraphsWindow.graphs()
        self.GraphsWindow.grid()

    def display_searchpage(self, search=None, archive=None):
        self.clear_main_window()
        if search and archive:
            self.SearchWindow.display_all_jobs(search, archive=True)
            self.SearchWindow.search_jobs(archive=True)
        elif search:
            self.SearchWindow.display_all_jobs(search)
            self.SearchWindow.search_jobs()
        elif archive:
            self.SearchWindow.display_all_jobs(archive=True)
            self.SearchWindow.search_jobs(archive=True)
        else:
            self.SearchWindow.display_all_jobs()
            self.SearchWindow.search_jobs()
        self.SearchWindow.grid(padx=5, pady=5)

    def display_editaddpage(self):
        self.clear_main_window()
        self.EditAddWindow.edit_add()
        self.EditAddWindow.grid(padx=5, pady=5)

    def display_jobpage(self, customer, archive=None):
        self.clear_main_window()
        self.JobpageWindow.get_relevant_intake_photos(customer)
        if archive:
            self.JobpageWindow.generate_jobpage(customer, archive=True)
            self.JobpageWindow.update_job_information(customer, archive=True)
            self.JobpageWindow.display_job_notes(customer, archive=True)
            self.JobpageWindow.display_tests(customer, archive=True)
        else:
            self.JobpageWindow.generate_jobpage(customer)
            self.JobpageWindow.update_job_information(customer)
            self.JobpageWindow.display_job_notes(customer)
            self.JobpageWindow.display_tests(customer)
        self.JobpageWindow.grid(padx=5, pady=5)
