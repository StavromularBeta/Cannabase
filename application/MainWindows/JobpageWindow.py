import tkinter as Tk
import sys
sys.path.append("/Users/PeterLevett/PycharmProjects/Cannabase/Cannabase/sql_files")
import editentry
import selection
import datetime


class JobpageWindow(Tk.Frame):
    def __init__(self, parent):
        Tk.Frame.__init__(self, parent)
        self.parent = parent
        self.basic_information_window = Tk.Frame(self)
        self.update_information_frame = Tk.Frame(self)
        self.test_display_frame = Tk.Frame(self)
        self.update_entry = Tk.Entry(self.update_information_frame)
        self.edit_entry = editentry.EditEntry()
        self.selection = selection.Selection()
        self.cannajobs_converter = {'Job Number': 2,
                                    'Tests': 4,
                                    'Receive Date': 3,
                                    'Status': 5
                                    }

    def clear_jobpage_window(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.basic_information_window = Tk.Frame(self)
        self.update_information_frame = Tk.Frame(self)
        self.test_display_frame = Tk.Frame(self)

    def generate_jobpage(self, job):
        self.basic_information_window.grid(row=0, column=0)
        Tk.Label(self.basic_information_window, text="Job Number: " + str(job[1])).grid(row=1, column=0, sticky=Tk.W)
        Tk.Label(self.basic_information_window, text="Receive Date: " + str(job[3])).grid(row=3, column=0, sticky=Tk.W)
        if job[4] == 0:
            Tk.Label(self.basic_information_window, text="Status: Incomplete").grid(row=4, column=0, sticky=Tk.W)
        else:
            Tk.Label(self.basic_information_window, text="Completed On: " + str(job[5])).grid(row=4, column=0, sticky=Tk.W)


    def update_job_information(self, job):
        self.update_information_frame.grid(row=1, column=0)
        self.update_entry.grid(row=0, column=0, columnspan=2)
        option_variable = Tk.StringVar(self.update_information_frame)
        option_variable.set('Status')
        update_options = Tk.OptionMenu(self.update_information_frame,
                                       option_variable,
                                       "Status",
                                       "Tests",).grid(row=1, column=0)
        update_entry_button = Tk.Button(self.update_information_frame,
                                        text="Update",
                                        command=lambda: self.update_db(job, option_variable)).grid(row=1, column=1)

    def display_tests(self, job):
        self.test_display_frame.grid(row=2, column=0)
        active_tests = self.selection.select_from_cannajobs_tests__table_with_conditions(2, (str(job[1]),))
        row_count = 0
        for test in active_tests:
            if int(test[4]) == 0:
                test_label = Tk.Label(self.test_display_frame, text=test[2]).grid(row=row_count, column=0)
                test_button = Tk.Button(self.test_display_frame,
                                        text='Complete',
                                        command=lambda i=[test[0], job]: self.update_test_db(i[0], i[1])).grid(row=row_count, column=1)
                row_count += 1
            else:
                test_label = Tk.Label(self.test_display_frame, text=str(test[2])).grid(row=row_count, column=0)
                completed_on = Tk.Label(self.test_display_frame, text='Completed on: ' + str(test[5])).grid(row=row_count, column=1)
                reset_button = Tk.Button(self.test_display_frame,
                                         text='Reset',
                                         command=lambda i=[test[0], job]: self.reset_test_db(i[0], i[1])).grid(row=row_count, column=2)
                row_count += 1

    def update_db(self, job, option_variable):
        desired_update = self.update_entry.get()
        self.edit_entry.edit_cannajobs_entry(self.cannajobs_converter[option_variable.get()], desired_update, job[0])
        self.edit_entry.edit_cannajobs_entry(6, datetime.date.today(), job[0])
        self.clear_jobpage_window()
        self.parent.display_jobpage(job)

    def update_test_db(self, id, job):
        self.edit_entry.edit_cannajobs_tests_entry(5, 1, id)
        self.edit_entry.edit_cannajobs_tests_entry(6, datetime.date.today(), id)
        self.parent.display_jobpage(job)

    def reset_test_db(self, id, job):
        self.edit_entry.edit_cannajobs_tests_entry(5, 0, id)
        self.edit_entry.edit_cannajobs_tests_entry(6, datetime.date(2000, 1, 1), id)
        self.parent.display_jobpage(job)
