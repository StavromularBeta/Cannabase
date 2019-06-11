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
        self.jobnumber_entry = Tk.Entry(self.add_new_job_frame)
        # Checkboxes
        self.metals = Tk.IntVar()
        self.metals_checkbox = Tk.Checkbutton(self.add_new_job_frame, text='2) metals', variable=self.metals)
        self.basic_potency = Tk.IntVar()
        self.basic_potency_checkbox = Tk.Checkbutton(self.add_new_job_frame,
                                                     text='3) basic potency',
                                                     variable=self.basic_potency)
        self.deluxe_potency = Tk.IntVar()
        self.deluxe_potency_checkbox = Tk.Checkbutton(self.add_new_job_frame,
                                                      text='3a) deluxe potency',
                                                      variable=self.deluxe_potency)
        self.toxins = Tk.IntVar()
        self.toxins_checkbox = Tk.Checkbutton(self.add_new_job_frame, text='4) Aflotoxins', variable=self.toxins)
        self.pesticides = Tk.IntVar()
        self.pesticides_checkbox = Tk.Checkbutton(self.add_new_job_frame, text='5) Pesticides', variable=self.pesticides)
        self.terpenes = Tk.IntVar()
        self.terpenes_checkbox = Tk.Checkbutton(self.add_new_job_frame, text='7) Terpenes', variable=self.terpenes)
        self.solvents = Tk.IntVar()
        self.solvents_checkbox = Tk.Checkbutton(self.add_new_job_frame, text='8) Solvents', variable=self.solvents)
        self.other = Tk.IntVar()
        self.other_checkbox = Tk.Checkbutton(self.add_new_job_frame, text='Other', variable=self.other)

    def clear_edit_add_frame(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.add_new_job_frame = Tk.Frame(self)
        self.jobnumber_entry = Tk.Entry(self.add_new_job_frame)
        self.metals = Tk.IntVar()
        self.metals_checkbox = Tk.Checkbutton(self.add_new_job_frame, text='2) metals', variable=self.metals)
        self.basic_potency = Tk.IntVar()
        self.basic_potency_checkbox = Tk.Checkbutton(self.add_new_job_frame,
                                                     text='3) basic potency',
                                                     variable=self.basic_potency)
        self.deluxe_potency = Tk.IntVar()
        self.deluxe_potency_checkbox = Tk.Checkbutton(self.add_new_job_frame,
                                                      text='3a) deluxe potency',
                                                      variable=self.deluxe_potency)
        self.toxins = Tk.IntVar()
        self.toxins_checkbox = Tk.Checkbutton(self.add_new_job_frame, text='4) Aflotoxins', variable=self.toxins)
        self.pesticides = Tk.IntVar()
        self.pesticides_checkbox = Tk.Checkbutton(self.add_new_job_frame, text='5) Pesticides', variable=self.pesticides)
        self.terpenes = Tk.IntVar()
        self.terpenes_checkbox = Tk.Checkbutton(self.add_new_job_frame, text='7) Terpenes', variable=self.terpenes)
        self.solvents = Tk.IntVar()
        self.solvents_checkbox = Tk.Checkbutton(self.add_new_job_frame, text='8) Solvents', variable=self.solvents)
        self.other = Tk.IntVar()
        self.other_checkbox = Tk.Checkbutton(self.add_new_job_frame, text='Other', variable=self.other)

    def edit_add(self):
        edit_add_label = Tk.Label(self, text="Edit/Add")
        new_job_entry_frame = self.generate_new_job_frame()
        edit_add_label.grid(row=0)
        new_job_entry_frame.grid(row=1)

        # job number, receive date, tests, status
    def generate_new_job_frame(self):
        Tk.Label(self.add_new_job_frame, text="New Job Entry").grid(row=0, columnspan=2)
        Tk.Label(self.add_new_job_frame, text="Job Number").grid(row=1, sticky=Tk.W)
        self.jobnumber_entry.grid(row=1, column=1, columnspan=2, sticky=Tk.W)
        self.metals_checkbox.grid(row=2, column=1, sticky=Tk.W)
        self.basic_potency_checkbox.grid(row=3, column=1, sticky=Tk.W)
        self.deluxe_potency_checkbox.grid(row=4, column=1, sticky=Tk.W)
        self.toxins_checkbox.grid(row=5, column=1, sticky=Tk.W)
        self.pesticides_checkbox.grid(row=6, column=1, sticky=Tk.W)
        self.terpenes_checkbox.grid(row=7, column=1, sticky=Tk.W)
        self.solvents_checkbox.grid(row=8, column=1, sticky=Tk.W)
        self.other_checkbox.grid(row=9, column=1, sticky=Tk.W)
        Tk.Button(self, text="Enter Job", command=self.input_entry).grid(row=2, column=0, columnspan=2, pady=10)
        return self.add_new_job_frame

    def input_entry(self):
        job_number = self.jobnumber_entry.get()
        test_list = self.generate_tests_list(True)
        job_entry = (job_number,
                     test_list,
                     datetime.date.today(),
                     0,
                     datetime.date.today())
        self.add_delete_query.new_cannajobs_entry(job_entry)
        for item in self.generate_tests_list():
            test_entry = (job_number,
                          item,
                          datetime.date.today(),
                          0,
                          datetime.date.today())
            self.add_delete_query.new_cannajobs_tests_entry(test_entry)
        self.clear_edit_add_frame()
        self.edit_add()

    def generate_tests_list(self, string_return=None):
        counter = 0
        test_number_list = [2,3,33,4,5,7,8,9]
        test_list = [self.metals.get(),
                     self.basic_potency.get(),
                     self.deluxe_potency.get(),
                     self.toxins.get(),
                     self.pesticides.get(),
                     self.terpenes.get(),
                     self.solvents.get(),
                     self.other.get()]
        active_tests = []
        for item in test_list:
            if item > 0:
                active_tests.append(test_number_list[counter])
            counter += 1
        if string_return:
            active_test_string = str()
            for item in active_tests:
                active_test_string = active_test_string + str(item) + ','
            return active_test_string[:-1]
        else:
            return active_tests


