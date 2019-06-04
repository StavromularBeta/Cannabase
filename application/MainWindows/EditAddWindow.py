import tkinter as Tk
import sys
sys.path.append("/Users/PeterLevett/PycharmProjects/Cannabase/Cannabase/sql_files")
import addel as ad
import datetime


class EditAddWindow(Tk.Frame):
    def __init__(self, parent):
        Tk.Frame.__init__(self, parent)
        self.parent = parent
        self.add_delete_query = ad.AdDel()
        self.add_new_job_frame = Tk.Frame(self)
        self.e1 = Tk.Entry(self.add_new_job_frame)
        self.e2 = Tk.Entry(self.add_new_job_frame)

    def clear_edit_add_frame(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.add_new_job_frame = Tk.Frame(self)
        self.e1 = Tk.Entry(self.add_new_job_frame)
        self.e2 = Tk.Entry(self.add_new_job_frame)

    def edit_add(self):
        edit_add_label = Tk.Label(self, text="Edit/Add")
        new_job_entry_frame = self.generate_new_job_frame()
        edit_add_label.grid(row=0)
        new_job_entry_frame.grid(row=1)

        # job number, receive date, tests, status
    def generate_new_job_frame(self):
        Tk.Label(self.add_new_job_frame, text="New Job Entry").grid(row=0, columnspan=2)
        Tk.Label(self.add_new_job_frame, text="Job Number").grid(row=1, sticky=Tk.W)
        Tk.Label(self.add_new_job_frame, text="Tests").grid(row=2, sticky=Tk.W)
        self.e1.grid(row=1, column=1, columnspan=2, sticky=Tk.W)
        self.e2.grid(row=2, column=1, columnspan=2, sticky=Tk.W)
        Tk.Button(self, text="Enter Job", command=self.input_entry).grid(row=3, column=0, columnspan=2, pady=10)
        return self.add_new_job_frame

    def input_entry(self):
        job_number = self.e1.get()
        tests = self.e2.get()
        job_entry = (job_number,
                     datetime.date.today(),
                     tests,
                     0)
        self.add_delete_query.new_cannajobs_entry(job_entry)
        self.clear_edit_add_frame()
        self.edit_add()
