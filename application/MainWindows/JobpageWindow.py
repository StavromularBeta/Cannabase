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

class JobpageWindow(Tk.Frame):
    def __init__(self, parent, **kwargs):
        Tk.Frame.__init__(self, parent, **kwargs)
        self.parent = parent
        self.notes_for_job_frame = Tk.Frame(self, borderwidth=1, relief='solid')
        self.job_notes = Tk.Text(self.notes_for_job_frame,
                                 borderwidth=1,
                                 width=65,
                                 height=20,
                                 wrap="word")
        self.title_font = tkFont.Font(size=16, weight='bold')
        self.basic_information_window = Tk.Frame(self, borderwidth=1, relief='solid')
        self.update_information_frame = Tk.Frame(self, borderwidth=1, relief='solid')
        self.test_display_frame = Tk.Frame(self, borderwidth=1, relief='solid')
        self.update_entry = Tk.Entry(self.update_information_frame)
        self.job_number_font = tkFont.Font(size=16, weight='bold')
        self.edit_entry = editentry.EditEntry()
        self.selection = selection.Selection()
        self.addel = addel.AdDel()
        self.cannajobs_converter = {'Job Number': 2,
                                    'Tests': 3,
                                    'Client Name': 4,
                                    'Receive Date': 5,
                                    'Status': 6
                                    }
        self.test_converter = {2: "Metals (ICP)",
                               3: "Basic Potency",
                               33: "Deluxe Potency",
                               4: "Afloxtoxins",
                               5: "Pesticides",
                               7: "Terpenes",
                               8: "Solvents",
                               9: "Other Tests"
                               }

    def clear_jobpage_window(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.basic_information_window = Tk.Frame(self, borderwidth=1, relief='solid')
        self.update_information_frame = Tk.Frame(self)
        self.test_display_frame = Tk.Frame(self, borderwidth=1, relief='solid')
        self.notes_for_job_frame = Tk.Frame(self, borderwidth=1, relief='solid')
        self.job_notes = Tk.Text(self.notes_for_job_frame,
                                 borderwidth=1,
                                 width=65,
                                 height=20,
                                 wrap="word")

    def generate_jobpage(self, job):
        self.basic_information_window.grid(row=0, column=0, sticky=Tk.NW, padx=5, pady=5, ipadx=2, ipady=2)
        Tk.Label(self.basic_information_window, text="Job Number: " + str(job[1]), font=self.job_number_font).grid(row=1, column=0, sticky=Tk.W)
        Tk.Button(self.basic_information_window,
                  text="Delete Job",
                  command=lambda: self.delete_job(job[0], job[1])).grid(row=1, column=3, sticky=Tk.W)
        Tk.Label(self.basic_information_window, text="Client: " + str(job[3])).grid(row=3, column=0, sticky=Tk.W)
        Tk.Label(self.basic_information_window, text="Recieve Date: " + str(job[4])).grid(row=4, column=0, sticky=Tk.W)
        if job[5] == 0:
            Tk.Label(self.basic_information_window, text="Status: Incomplete").grid(row=5, column=0, sticky=Tk.W)
        else:
            Tk.Label(self.basic_information_window, text="Completed On: " + str(job[6])).grid(row=5, column=0, sticky=Tk.W)


    def update_job_information(self, job):
        self.update_information_frame.grid(row=0, column=1, sticky=Tk.W, padx=5, pady=5, ipadx=2, ipady=2)
        if job[5] == 0:
            Tk.Label(self.update_information_frame, text="This Job is Incomplete.").grid(row=1, column=0, sticky=Tk.W)
            Tk.Button(self.update_information_frame,
                      text="Press To Complete",
                      command=lambda: self.update_db(job, 1)).grid(row=0, column=0, sticky=Tk.NW)
        else:
            Tk.Label(self.update_information_frame, text="This Job is Complete.").grid(row=0, column=0, sticky=Tk.W)
            Tk.Button(self.update_information_frame,
                      text="Press To Reset",
                      command=lambda: self.update_db(job, 0)).grid(row=1, column=0, sticky=Tk.NW)

        self.filler_canvas = Tk.Canvas(self, width=1100, height=600)
        self.filler_canvas.grid(row=3, column=1, columnspan=1)

    def display_tests(self, job):
        self.test_display_frame.grid(row=1, column=0, sticky=Tk.NW, padx=5, ipadx=2, ipady=2)
        active_tests = self.selection.select_from_cannajobs_tests__table_with_conditions(2, (str(job[1]),))
        Tk.Label(self.test_display_frame, text="Tests", font=self.title_font).grid(row=0, column=0, sticky=Tk.W)
        row_count = 1
        for test in active_tests:
            if int(test[4]) == 0:
                test_label = Tk.Label(self.test_display_frame, text=self.test_converter[int(test[2])]).grid(row=row_count, column=0)
                test_button = Tk.Button(self.test_display_frame,
                                        text='Complete',
                                        command=lambda i=[test[0], job]: self.update_test_db(i[0], i[1])).grid(row=row_count, column=1)
                row_count += 1
            else:
                test_label = Tk.Label(self.test_display_frame, text=self.test_converter[int(test[2])]).grid(row=row_count, column=0)
                completed_on = Tk.Label(self.test_display_frame, text='Completed on: ' + str(test[5])).grid(row=row_count, column=1)
                reset_button = Tk.Button(self.test_display_frame,
                                         text='Reset',
                                         command=lambda i=[test[0], job]: self.reset_test_db(i[0], i[1])).grid(row=row_count, column=2)
                row_count += 1

    def display_job_notes(self, job):
        self.notes_for_job_frame.grid(row=2, column=0, rowspan=1, columnspan=3, sticky=Tk.NW, pady=5,  padx=5, ipadx=2, ipady=2)
        try:
            for item in self.selection.select_latest_cannajobs_test_notes_for_job(job[1]):
                latest_job_note = item[2]
            self.job_notes.insert('end-1c', latest_job_note)
        except UnboundLocalError:
            bummer_note = "Didn't find a startup note :("
            self.job_notes.insert('end-1c', bummer_note)
        Tk.Label(self.notes_for_job_frame, text="Job Notes", font=self.title_font).grid(row=0, column=0, sticky=Tk.W)
        Tk.Button(self.notes_for_job_frame, text="Update Notes", command=lambda: self.update_notes(job)).grid(row=3,
                                                                                                              column=0,
                                                                                                              pady=5,
                                                                                                              sticky=Tk.W)
        self.job_notes.grid(row=1, column=0, sticky=Tk.W, padx=2, pady=2)

    def update_db(self, job, desired_update):
        self.edit_entry.edit_cannajobs_entry(6, desired_update, job[0])
        if int(desired_update) == 1:
            self.edit_entry.edit_cannajobs_entry(7, datetime.date.today(), job[0])
        else:
            self.edit_entry.edit_cannajobs_entry(7, datetime.date(2000, 1, 1), job[0])
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

    def delete_job(self, id, job):
        self.addel.delete_cannajob_entry((id,))
        self.addel.delete_cannajob_tests((job,))
        self.addel.delete_cannajob_test_notes((job,))
        self.parent.display_searchpage()

    def update_notes(self, job):
        entry = (job[1],
                 self.job_notes.get("1.0", 'end-1c'),
                 datetime.date.today())
        self.addel.new_cannajobs_test_notes_entry(entry)
        self.parent.display_jobpage(job)
