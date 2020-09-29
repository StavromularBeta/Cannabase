import tkinter as Tk
import os, sys, inspect
# below 3 lines add the parent directory to the path, so that SQL_functions can be found.
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
parentdir = os.path.dirname(parentdir)
sys.path.insert(0, parentdir+'/sql_files/')
import addel as ad
import selection as sel
import datetime
from tkinter import font as tkFont


class EditAddWindow(Tk.Frame):
    def __init__(self, parent, **kwargs):
        Tk.Frame.__init__(self, parent, **kwargs)
        self.parent = parent
        self.config(bg="#e0fcf4")
        self.large_bold_font_choice = tkFont.Font(size=16, weight='bold')
        self.smaller_bold_font_choice = tkFont.Font(size=12, weight='bold')
        self.add_delete_query = ad.AdDel()
        self.select_query = sel.Selection()
        self.add_new_job_frame = Tk.Frame(self,
                                          bg='#e0fcf4')
        self.job_notes_frame = Tk.Frame(self,
                                        bg='#e0fcf4')
        self.jobnumber_entry = Tk.Entry(self.add_new_job_frame)
        self.client_name_entry = Tk.Entry(self.add_new_job_frame)
        self.job_notes = Tk.Text(self.job_notes_frame,
                                 borderwidth=1,
                                 width=65,
                                 height=20,
                                 wrap="word")
        self.existing_client_variable = Tk.StringVar(self.add_new_job_frame)
        self.existing_client_variable.set("New Client")
        # Checkboxes
        self.metals = Tk.IntVar()
        self.metals_checkbox = Tk.Checkbutton(self.add_new_job_frame,
                                              text='2) metals',
                                              variable=self.metals,
                                              bg='#e0fcf4')
        self.basic_potency = Tk.IntVar()
        self.basic_potency_checkbox = Tk.Checkbutton(self.add_new_job_frame,
                                                     text='3) basic potency',
                                                     variable=self.basic_potency,
                                                     bg='#e0fcf4')
        self.deluxe_potency = Tk.IntVar()
        self.deluxe_potency_checkbox = Tk.Checkbutton(self.add_new_job_frame,
                                                      text='3a) deluxe potency',
                                                      variable=self.deluxe_potency,
                                                      bg='#e0fcf4')
        self.toxins = Tk.IntVar()
        self.toxins_checkbox = Tk.Checkbutton(self.add_new_job_frame,
                                              text='4) Aflotoxins',
                                              variable=self.toxins,
                                              bg='#e0fcf4')
        self.pesticides = Tk.IntVar()
        self.pesticides_checkbox = Tk.Checkbutton(self.add_new_job_frame,
                                                  text='5) Pesticides',
                                                  variable=self.pesticides,
                                                  bg='#e0fcf4')
        self.terpenes = Tk.IntVar()
        self.terpenes_checkbox = Tk.Checkbutton(self.add_new_job_frame,
                                                text='7) Terpenes',
                                                variable=self.terpenes,
                                                bg='#e0fcf4')
        self.solvents = Tk.IntVar()
        self.solvents_checkbox = Tk.Checkbutton(self.add_new_job_frame,
                                                text='8) Solvents',
                                                variable=self.solvents,
                                                bg='#e0fcf4')
        self.other = Tk.IntVar()
        self.other_checkbox = Tk.Checkbutton(self.add_new_job_frame,
                                             text='Other',
                                             variable=self.other,
                                             bg='#e0fcf4')
        self.micro_a = Tk.IntVar()
        self.micro_a_checkbox = Tk.Checkbutton(self.add_new_job_frame,
                                               text='1) Micro A',
                                               variable=self.micro_a,
                                               bg='#e0fcf4')
        self.micro_b = Tk.IntVar()
        self.micro_b_checkbox = Tk.Checkbutton(self.add_new_job_frame,
                                               text='6) Micro B',
                                               variable=self.micro_b,
                                               bg='#e0fcf4')
        self.fungal_id = Tk.IntVar()
        self.fungal_id_checkbox = Tk.Checkbutton(self.add_new_job_frame,
                                                 text='Fungal ID',
                                                 variable=self.fungal_id,
                                                 bg='#e0fcf4')
        self.mushrooms = Tk.IntVar()
        self.mushrooms_checkbox = Tk.Checkbutton(self.add_new_job_frame,
                                                 text='Psilocybin',
                                                 variable=self.mushrooms,
                                                 bg='#e0fcf4')
        self.existing_client_list = ['New Client']
        self.filter_list = ['#', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                            'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        for item in self.select_query.select_all_from_customer_table_descending(7):
            self.existing_client_list.append(item[2])

    def clear_edit_add_frame(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.add_new_job_frame = Tk.Frame(self,
                                          bg='#e0fcf4')
        self.job_notes_frame = Tk.Frame(self,
                                        bg='#e0fcf4')
        self.jobnumber_entry = Tk.Entry(self.add_new_job_frame)
        self.client_name_entry = Tk.Entry(self.add_new_job_frame)
        self.job_notes = Tk.Text(self.job_notes_frame,
                                 borderwidth=1,
                                 width=65,
                                 height=20,
                                 wrap="word")
        # Checkboxes
        self.metals = Tk.IntVar()
        self.metals_checkbox = Tk.Checkbutton(self.add_new_job_frame,
                                              text='2) metals',
                                              variable=self.metals,
                                              bg='#e0fcf4')
        self.basic_potency = Tk.IntVar()
        self.basic_potency_checkbox = Tk.Checkbutton(self.add_new_job_frame,
                                                     text='3) basic potency',
                                                     variable=self.basic_potency,
                                                     bg='#e0fcf4')
        self.deluxe_potency = Tk.IntVar()
        self.deluxe_potency_checkbox = Tk.Checkbutton(self.add_new_job_frame,
                                                      text='3a) deluxe potency',
                                                      variable=self.deluxe_potency,
                                                      bg='#e0fcf4')
        self.toxins = Tk.IntVar()
        self.toxins_checkbox = Tk.Checkbutton(self.add_new_job_frame,
                                              text='4) Aflotoxins',
                                              variable=self.toxins,
                                              bg='#e0fcf4')
        self.pesticides = Tk.IntVar()
        self.pesticides_checkbox = Tk.Checkbutton(self.add_new_job_frame,
                                                  text='5) Pesticides',
                                                  variable=self.pesticides,
                                                  bg='#e0fcf4')
        self.terpenes = Tk.IntVar()
        self.terpenes_checkbox = Tk.Checkbutton(self.add_new_job_frame,
                                                text='7) Terpenes',
                                                variable=self.terpenes,
                                                bg='#e0fcf4')
        self.solvents = Tk.IntVar()
        self.solvents_checkbox = Tk.Checkbutton(self.add_new_job_frame,
                                                text='8) Solvents',
                                                variable=self.solvents,
                                                bg='#e0fcf4')
        self.other = Tk.IntVar()
        self.other_checkbox = Tk.Checkbutton(self.add_new_job_frame,
                                             text='Other',
                                             variable=self.other,
                                             bg='#e0fcf4')
        self.micro_a = Tk.IntVar()
        self.micro_a_checkbox = Tk.Checkbutton(self.add_new_job_frame,
                                               text='1) Micro A',
                                               variable=self.micro_a,
                                               bg='#e0fcf4')
        self.micro_b = Tk.IntVar()
        self.micro_b_checkbox = Tk.Checkbutton(self.add_new_job_frame,
                                               text='6) Micro B',
                                               variable=self.micro_b,
                                               bg='#e0fcf4')
        self.fungal_id = Tk.IntVar()
        self.fungal_id_checkbox = Tk.Checkbutton(self.add_new_job_frame,
                                                 text='Fungal ID',
                                                 variable=self.fungal_id,
                                                 bg='#e0fcf4')
        self.mushrooms = Tk.IntVar()
        self.mushrooms_checkbox = Tk.Checkbutton(self.add_new_job_frame,
                                                 text='Psilocybin',
                                                 variable=self.mushrooms,
                                                 bg='#e0fcf4')

    def edit_add(self):
        new_job_entry_frame = self.generate_new_job_frame()
        new_job_entry_frame.grid(row=0, column=0, sticky=Tk.W, padx=5, ipadx=2, ipady=2)
        self.generate_job_notes_frame()
        self.job_notes_frame.grid(row=0, column=1, rowspan=3, sticky=Tk.NW)
        self.filler_canvas = Tk.Canvas(self, bg="#e0fcf4", highlightbackground="#e0fcf4", width=1100, height=600)
        self.filler_canvas.grid(row=4, column=4, columnspan=1)

        # job number, receive date, tests, status
    def generate_new_job_frame(self):
        Tk.Label(self.add_new_job_frame,
                 text="New Job Entry",
                 bg='#e0fcf4',
                 font=self.large_bold_font_choice).grid(row=0, columnspan=2, sticky= Tk.W)
        Tk.Label(self.add_new_job_frame,
                 text="Job Number",
                 bg='#e0fcf4').grid(row=1, sticky=Tk.W)
        Tk.Label(self.add_new_job_frame,
                 text="New Client Name",
                 bg='#e0fcf4').grid(row=2, sticky=Tk.W)
        self.jobnumber_entry.grid(row=1, column=1, columnspan=2, sticky=Tk.W)
        self.client_name_entry.grid(row=2, column=1, columnspan=2, sticky=Tk.W)
        Tk.Label(self.add_new_job_frame,
                 text="Existing Client Name",
                 bg='#e0fcf4').grid(row=3, sticky=Tk.W)
        self.filter_variable = Tk.StringVar(self.add_new_job_frame)
        self.filter_variable.set(self.filter_list[0])
        f = Tk.OptionMenu(self.add_new_job_frame, self.filter_variable, *self.filter_list)
        f.grid(row=3, column=1, sticky=Tk.W)
        Tk.Button(self.add_new_job_frame,
                  text="Filter",
                  command=lambda: self.filter_customer_list(self.filter_variable.get())).grid(row=3,
                                                                                              column=2,
                                                                                              sticky=Tk.W)
        Tk.Label(self.add_new_job_frame,
                 text="Requested Tests",
                 font=self.large_bold_font_choice,
                 bg='#e0fcf4').grid(row=5, columnspan=2, sticky= Tk.W)
        Tk.Label(self.add_new_job_frame,
                 text="Health Canada Cannabis Tests",
                 font=self.smaller_bold_font_choice,
                 bg='#e0fcf4').grid(row=6, columnspan=2, sticky=Tk.W)
        self.micro_a_checkbox.grid(row=7, column=0, sticky=Tk.W)
        self.metals_checkbox.grid(row=8, column=0, sticky=Tk.W)
        self.basic_potency_checkbox.grid(row=9, column=0, sticky=Tk.W)
        self.deluxe_potency_checkbox.grid(row=10, column=0, sticky=Tk.W)
        self.toxins_checkbox.grid(row=11, column=0, sticky=Tk.W)
        self.pesticides_checkbox.grid(row=12, column=0, sticky=Tk.W)
        self.micro_b_checkbox.grid(row=13, column=0, sticky=Tk.W)
        self.terpenes_checkbox.grid(row=14, column=0, sticky=Tk.W)
        self.solvents_checkbox.grid(row=15, column=0, sticky=Tk.W)
        Tk.Label(self.add_new_job_frame,
                 text="Other Tests",
                 font=self.smaller_bold_font_choice,
                 bg='#e0fcf4').grid(row=16, columnspan=2, sticky=Tk.W)
        self.other_checkbox.grid(row=17, column=0, sticky=Tk.W)
        self.fungal_id_checkbox.grid(row=18, column=0, sticky=Tk.W)
        self.mushrooms_checkbox.grid(row=19, column=0, sticky=Tk.W)
        Tk.Button(self, text="Enter Job", command=self.input_entry).grid(row=2, column=0, pady=10, sticky=Tk.W)
        self.filler_canvas = Tk.Canvas(self, width=1100, height=600, bg="#e0fcf4", highlightbackground="#e0fcf4")
        self.filler_canvas.grid(row=3, column=1, columnspan=1, sticky=Tk.W)
        return self.add_new_job_frame

    def filter_customer_list(self, letter):
        self.clear_edit_add_frame()
        self.edit_add()
        if letter == '#':
            self.filtered_client_list = [item for item in self.existing_client_list if not item[0] in self.filter_list]
        else:
            self.filtered_client_list = [item for item in self.existing_client_list if str(item[0]) == str(letter)]
        if len(self.filtered_client_list) == 0:
            self.filtered_client_list.insert(0, "No Clients")
        w = Tk.OptionMenu(self.add_new_job_frame, self.existing_client_variable, *self.filtered_client_list)
        w.grid(row=4, column=0, columnspan=2, sticky=Tk.W)

    def input_entry(self):
        job_number = self.jobnumber_entry.get()
        if self.test_for_blank_job(job_number) is True:
            #This prevents you from entering a blank job number.
            self.clear_edit_add_frame()
            self.edit_add()
            return False
        if self.existing_client_variable.get() == "New Client" or len(self.client_name_entry.get()) != 0:
            client_name = self.client_name_entry.get()
            self.add_delete_query.new_customer_entry((0, client_name, 1))
        else:
            client_name = self.existing_client_variable.get()
        current_job_note = self.job_notes.get("1.0", 'end-1c')
        test_list = self.generate_tests_list(True)
        job_entry = (job_number,
                     test_list,
                     client_name,
                     datetime.date.today(),
                     0,
                     datetime.date(2000, 1, 1))
        self.add_delete_query.new_cannajobs_entry(job_entry)
        for item in self.generate_tests_list():
            test_entry = (job_number,
                          item,
                          datetime.date.today(),
                          0,
                          datetime.date(2000, 1, 1))
            self.add_delete_query.new_cannajobs_tests_entry(test_entry)
        note_entry = (job_number,
                      current_job_note,
                      datetime.date.today())
        self.add_delete_query.new_cannajobs_test_notes_entry(note_entry)
        self.clear_edit_add_frame()
        self.edit_add()

    def generate_tests_list(self, string_return=None):
        counter = 0
        test_number_list = [2, 3, 33, 4, 5, 7, 8, 9, 1, 6, 10, 11]
#       1-9 correspond to health canada testing numbers, 10 is fungal ID, 11 is mushrooms.
        test_list = [self.metals.get(),
                     self.basic_potency.get(),
                     self.deluxe_potency.get(),
                     self.toxins.get(),
                     self.pesticides.get(),
                     self.terpenes.get(),
                     self.solvents.get(),
                     self.other.get(),
                     self.micro_a.get(),
                     self.micro_b.get(),
                     self.fungal_id.get(),
                     self.mushrooms.get()]
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

    def generate_job_notes_frame(self):
        Tk.Label(self.job_notes_frame,
                 text='Job Notes',
                 font=self.large_bold_font_choice,
                 bg='#e0fcf4').grid(row=0, column=0, sticky=Tk.W)
        self.job_notes.grid(row=1, column=0, padx=5, pady=5)
        start_note = 'Space for job notes!'
        self.job_notes.insert('end-1c', start_note)

    def test_for_blank_job(self, job_number):
        if len(job_number) == 0:
            return True



