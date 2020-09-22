import tkinter as Tk
from MainWindows import HomepageWindow as Hpw,\
                        GraphsWindow as Grw,\
                        SearchWindow as Srw,\
                        EditAddWindow as Eaw,\
                        JobpageWindow as Jpw,\
                        CustomerWindow as Ctw,\
                        CustomerPageWindow as Cpw


class MainWindow(Tk.Frame):
    def __init__(self, parent, **kwargs):
        Tk.Frame.__init__(self, parent, **kwargs)
        self.HomepageWindow = Hpw.HomepageWindow(self)
        self.GraphsWindow = Grw.GraphsWindow(self)
        self.SearchWindow = Srw.SearchWindow(self)
        self.EditAddWindow = Eaw.EditAddWindow(self)
        self.JobpageWindow = Jpw.JobpageWindow(self, bg='#e0fcf4')
        self.CustomerWindow = Ctw.CustomerWindow(self)
        self.CustomerPageWindow = Cpw.CustomerpageWindow(self)

    def clear_main_window(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.HomepageWindow = Hpw.HomepageWindow(self)
        self.GraphsWindow = Grw.GraphsWindow(self)
        self.SearchWindow = Srw.SearchWindow(self)
        self.EditAddWindow = Eaw.EditAddWindow(self)
        self.JobpageWindow = Jpw.JobpageWindow(self, bg='#e0fcf4')
        self.CustomerWindow = Ctw.CustomerWindow(self)
        self.CustomerPageWindow = Cpw.CustomerpageWindow(self)

    def display_customerpage(self):
        self.clear_main_window()
        self.CustomerWindow.customers(view=True)
        self.CustomerWindow.grid(padx=5, pady=5)

    def display_searchpage(self, search=None, archive=None):
        self.clear_main_window()
        if search and archive:
            self.SearchWindow.display_all_jobs(search, archive=True, view=True)
            self.SearchWindow.search_jobs(archive=True, view=True)
        elif search:
            self.SearchWindow.display_all_jobs(search, view=True)
            self.SearchWindow.search_jobs(view=True)
        elif archive:
            self.SearchWindow.display_all_jobs(archive=True, view=True)
            self.SearchWindow.search_jobs(archive=True, view=True)
        else:
            self.SearchWindow.display_all_jobs(view=True)
            self.SearchWindow.search_jobs(view=True)
        self.SearchWindow.grid(padx=5, pady=5)

    def display_jobpage(self, customer, archive=None, view=None):
        self.clear_main_window()
        self.JobpageWindow.get_relevant_intake_photos(customer)
        self.JobpageWindow.get_relevant_exit_pdf_links(customer)
        self.JobpageWindow.get_relevant_customer_good_copies(customer)
        if archive:
            if view:
                self.JobpageWindow.generate_jobpage(customer, archive=True, view=True)
                self.JobpageWindow.update_job_information(customer, archive=True, view=True)
                self.JobpageWindow.display_job_notes(customer, archive=True, view=True)
                self.JobpageWindow.display_tests(customer, archive=True, view=True)
            else:
                self.JobpageWindow.generate_jobpage(customer, archive=True)
                self.JobpageWindow.update_job_information(customer, archive=True)
                self.JobpageWindow.display_job_notes(customer, archive=True)
                self.JobpageWindow.display_tests(customer, archive=True)
        else:
            if view:
                self.JobpageWindow.generate_jobpage(customer, view=True)
                self.JobpageWindow.update_job_information(customer, view=True)
                self.JobpageWindow.display_job_notes(customer, view=True)
                self.JobpageWindow.display_tests(customer, view=True)
            else:
                self.JobpageWindow.generate_jobpage(customer)
                self.JobpageWindow.update_job_information(customer)
                self.JobpageWindow.display_job_notes(customer)
                self.JobpageWindow.display_tests(customer)
        self.JobpageWindow.grid(padx=5, pady=5)

    def display_client_page(self, client, view=None):
        self.clear_main_window()
        if view:
            self.CustomerPageWindow.generate_customerpage(client, view=True)
        else:
            self.CustomerPageWindow.generate_customerpage(client)
        self.CustomerPageWindow.grid()

