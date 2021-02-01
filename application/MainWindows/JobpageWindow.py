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
from PIL import Image, ImageTk
import glob


class JobpageWindow(Tk.Frame):
    def __init__(self, parent, **kwargs):
        Tk.Frame.__init__(self, parent, **kwargs)
        self.parent = parent
        self.jobpage_text_font = tkFont.Font(size=10, weight='bold')
        self.jobpage_font = tkFont.Font(size=10, weight='bold')
        self.picture_frame = Tk.Frame(self,
                                      bg="#e0fcf4",
                                      highlightbackground='#613a3a',
                                      highlightcolor='#613a3a',
                                      highlightthickness=2)
        self.picture_sub_frame = Tk.Frame(self.picture_frame,
                                          bg="#e0fcf4")
        self.notes_for_job_frame = Tk.Frame(self,
                                            bg="#e0fcf4",
                                            highlightbackground='#613a3a',
                                            highlightcolor='#613a3a',
                                            highlightthickness=2)
        self.job_notes = Tk.Text(self.notes_for_job_frame,
                                 borderwidth=1,
                                 width=70,
                                 height=10,
                                 font=self.jobpage_text_font,
                                 wrap="word")
        self.text_reports = Tk.Text(self.notes_for_job_frame,
                                    borderwidth=1,
                                    width=70,
                                    height=15,
                                    font=self.jobpage_text_font,
                                    wrap="word")
        self.title_font = tkFont.Font(size=16, weight='bold')
        self.basic_information_window = Tk.Frame(self,
                                                 bg="#e0fcf4",
                                                 highlightbackground='#613a3a',
                                                 highlightcolor='#613a3a',
                                                 highlightthickness=2)
        self.update_information_frame = Tk.Frame(self,
                                                 bg="#e0fcf4",
                                                 highlightbackground='#613a3a',
                                                 highlightcolor='#613a3a',
                                                 highlightthickness=2)
        self.test_display_frame = Tk.Frame(self,
                                           bg="#e0fcf4",
                                           highlightbackground='#613a3a',
                                           highlightcolor='#613a3a',
                                           highlightthickness=2)
        self.links_display_frame = Tk.Frame(self,
                                            bg="#e0fcf4",
                                            highlightbackground='#613a3a',
                                            highlightcolor='#613a3a',
                                            highlightthickness=2)
        self.good_copies_display_frame = Tk.Frame(self,
                                                  bg="#e0fcf4",
                                                  highlightbackground='#613a3a',
                                                  highlightcolor='#613a3a',
                                                  highlightthickness=2)
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
                               9: "Other Tests",
                               1: "Micro A",
                               6: "Micro B",
                               10: "Fungal ID",
                               11: "Shrooms"
                               }

    def clear_jobpage_window(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.picture_frame = Tk.Frame(self,
                                      bg="#e0fcf4",
                                      highlightbackground='#613a3a',
                                      highlightcolor='#613a3a',
                                      highlightthickness=2)
        self.picture_sub_frame = Tk.Frame(self.picture_frame, bg="#e0fcf4")
        self.basic_information_window = Tk.Frame(self,
                                                 bg="#e0fcf4",
                                                 highlightbackground='#613a3a',
                                                 highlightcolor='#613a3a',
                                                 highlightthickness=2)
        self.update_information_frame = Tk.Frame(self,
                                                 bg="#e0fcf4",
                                                 highlightbackground='#613a3a',
                                                 highlightcolor='#613a3a',
                                                 highlightthickness=2)
        self.test_display_frame = Tk.Frame(self,
                                           bg="#e0fcf4",
                                           highlightbackground='#613a3a',
                                           highlightcolor='#613a3a',
                                           highlightthickness=2)
        self.links_display_frame = Tk.Frame(self,
                                            bg="#e0fcf4",
                                            highlightbackground='#613a3a',
                                            highlightcolor='#613a3a',
                                            highlightthickness=2)
        self.good_copies_display_frame = Tk.Frame(self,
                                                  bg="#e0fcf4",
                                                  highlightbackground='#613a3a',
                                                  highlightcolor='#613a3a',
                                                  highlightthickness=2)
        self.notes_for_job_frame = Tk.Frame(self,
                                            bg="#e0fcf4",
                                            highlightbackground='#613a3a',
                                            highlightcolor='#613a3a',
                                            highlightthickness=2)
        self.job_notes = Tk.Text(self.notes_for_job_frame,
                                 borderwidth=1,
                                 width=70,
                                 height=10,
                                 font=self.jobpage_text_font,
                                 wrap="word")
        self.text_reports = Tk.Text(self.notes_for_job_frame,
                                    borderwidth=1,
                                    width=70,
                                    height=15,
                                    font=self.jobpage_text_font,
                                    wrap="word")

    def generate_jobpage(self, job, archive=None, view=None):
        self.basic_information_window.grid(row=0, column=0, sticky=Tk.NW, padx=2, pady=5, ipadx=2, ipady=2)
        Tk.Label(self.basic_information_window,
                 text="Job Number: " + str(job[1]),
                 font=self.job_number_font,
                 bg="#e0fcf4").grid(row=1, column=0, sticky=Tk.W)
        if view:
            pass
        else:
            if archive:
                Tk.Button(self.basic_information_window,
                          text="Delete Job",
                          command=lambda: self.delete_job(job[0], job[1], archive=True)).grid(row=1, column=3, sticky=Tk.W)
            else:
                Tk.Button(self.basic_information_window,
                          text="Delete Job",
                          command=lambda: self.delete_job(job[0], job[1])).grid(row=1, column=3, sticky=Tk.W)
        client = self.selection.select_from_canna_customers_table_with_conditions_equals(3, (str(job[3]),))
        client = [item for item in client]
        if view:
            Tk.Button(self.basic_information_window,
                      text="Client: " + str(job[3]),
                      command=lambda: self.parent.display_client_page(client[0], view=True),
                      font=self.jobpage_font,
                      bg="#e0fcf4").grid(row=3, column=0, sticky=Tk.W)
        else:
            Tk.Button(self.basic_information_window,
                      text="Client: " + str(job[3]),
                      command=lambda: self.parent.display_client_page(client[0]),
                      font=self.jobpage_font,
                      bg="#e0fcf4").grid(row=3, column=0, sticky=Tk.W)
        Tk.Label(self.basic_information_window,
                 text="Recieve Date: " + str(job[4]),
                 font=self.jobpage_font,
                 bg="#e0fcf4").grid(row=4, column=0, sticky=Tk.W)
        if job[5] == 0:
            Tk.Label(self.basic_information_window,
                     text="Status: Incomplete",
                     font=self.jobpage_font,
                     bg="#e0fcf4").grid(row=5, column=0, sticky=Tk.W)
        else:
            Tk.Label(self.basic_information_window,
                     text="Completed On: " + str(job[6]),
                     font=self.jobpage_font,
                     bg="#e0fcf4").grid(row=5, column=0, sticky=Tk.W)

    def update_job_information(self, job, archive=None, view=None):
        self.update_information_frame.grid(row=0, column=1, sticky=Tk.W, padx=2, pady=5, ipadx=15, ipady=25)
        if job[5] == 0:
            Tk.Label(self.update_information_frame,
                     text="This Job is Incomplete.",
                     font=self.jobpage_font,
                     bg="#e0fcf4").grid(row=1, column=0, sticky=Tk.W)
            if archive or view:
                pass
            else:
                Tk.Button(self.update_information_frame,
                          text="Press To Complete",
                          command=lambda: self.update_db(job, 1)).grid(row=0, column=0, sticky=Tk.NW)
        else:
            Tk.Label(self.update_information_frame,
                     text="This Job is Complete.",
                     font=self.jobpage_font,
                     bg="#e0fcf4").grid(row=0, column=0, sticky=Tk.W)
            if archive or view:
                pass
            else:
                Tk.Button(self.update_information_frame,
                          text="Press To Reset",
                          command=lambda: self.update_db(job, 0)).grid(row=1, column=0, sticky=Tk.NW)
        self.filler_canvas = Tk.Canvas(self, bg="#e0fcf4", highlightbackground="#e0fcf4", width=1100, height=600)
        self.filler_canvas.grid(row=4, column=4, columnspan=1)

    def display_tests(self, job, archive=None, view=None):
        self.test_display_frame.grid(row=1, column=3, sticky=Tk.NW, padx=5, pady=5, ipadx=2, ipady=2)
        if archive:
            years = ['2020', '2021']
            active_tests = ""
            for item in years:
                active_tests = self.selection.select_from_cannajobs_tests_archive__table_with_conditions(item,
                                                                                                         2,
                                                                                                         (str(job[1]),))
                if len(active_tests.fetchall()) >= 1:
                    active_tests = self.selection.select_from_cannajobs_tests_archive__table_with_conditions(item,
                                                                                                             2,
                                                                                                             (str(job[1]),))
                    break
                else:
                    continue
        else:
            active_tests = self.selection.select_from_cannajobs_tests__table_with_conditions(2, (str(job[1]),))
        Tk.Label(self.test_display_frame,
                 text="Tests",
                 font=self.title_font,
                 bg="#e0fcf4").grid(row=0, column=0, sticky=Tk.W)
        row_count = 1
        for test in active_tests:
            if int(test[4]) == 0:
                Tk.Label(self.test_display_frame,
                         text=self.test_converter[int(test[2])],
                         font=self.jobpage_font,
                         bg="#e0fcf4").grid(row=row_count, column=0)
                if archive or view:
                    pass
                else:
                    Tk.Button(self.test_display_frame,
                              text='Complete',
                              command=lambda i=[test[0], job]: self.update_test_db(i[0], i[1])).grid(row=row_count, column=1)
                row_count += 1
            else:
                Tk.Label(self.test_display_frame,
                         text=self.test_converter[int(test[2])],
                         font=self.jobpage_font,
                         bg="#e0fcf4").grid(row=row_count, column=0)
                Tk.Label(self.test_display_frame,
                         text='Completed on: ' + str(test[5]),
                         font=self.jobpage_font,
                         bg="#e0fcf4").grid(row=row_count, column=1)
                if archive or view:
                    pass
                else:
                    Tk.Button(self.test_display_frame,
                              text='Reset',
                              command=lambda i=[test[0], job]: self.reset_test_db(i[0], i[1])).grid(row=row_count, column=2)
                row_count += 1

    def display_job_notes(self, job, archive=None, view=None):
        self.notes_for_job_frame.grid(row=1,  rowspan=3, column=0, columnspan=2, sticky=Tk.NW, pady=5,  padx=2, ipadx=2, ipady=2)
        try:
            if archive:
                years = ['2020', '2021']
                for year in years:
                    for item in self.selection.select_from_archive_cannajob_test_notes(year, job[1]):
                        latest_job_note = item[2]
                        self.job_notes.insert('end-1c', latest_job_note)
                        if latest_job_note:
                            break
            else:
                for item in self.selection.select_latest_cannajobs_test_notes_for_job(job[1]):
                    latest_job_note = item[2] + '\n\n'
                    self.job_notes.insert('end-1c', latest_job_note)
        except UnboundLocalError:
            bummer_note = "Didn't find a startup note :("
            self.job_notes.insert('end-1c', bummer_note)
        Tk.Label(self.notes_for_job_frame,
                 text="Job Notes",
                 font=self.title_font,
                 bg="#e0fcf4").grid(row=0, column=0, sticky=Tk.W)
        target = r'T:\ANALYST WORK FILES\Peter\Rover\reports\ '
        jobnumber = str(job[1])
        first_3_digits = jobnumber[0:3]
        last_digits = '000x'
        filename = target[:-1] + first_3_digits + last_digits + '\\' + jobnumber + '\\' + jobnumber + '.txt'
        filename = filename.replace('/', '-')
        try:
            with open(filename, 'r') as f:
                self.text_reports.insert("current", f.read())
        except FileNotFoundError:
            pass
        if view:
            Tk.Button(self.notes_for_job_frame,
                      text="Update Notes",
                      command=lambda: self.update_notes(job, view=True)).grid(row=2,
                                                                              column=0,
                                                                              pady=5,
                                                                              sticky=Tk.W)
        else:
            Tk.Button(self.notes_for_job_frame,
                      text="Update Notes",
                      command=lambda: self.update_notes(job)).grid(row=2,
                                                                   column=0,
                                                                   pady=5,
                                                                   sticky=Tk.W)
        self.job_notes.grid(row=1, column=0, columnspan=3, sticky=Tk.W, padx=2, pady=2)
        Tk.Label(self.notes_for_job_frame,
                 text="Analytical Reports",
                 font=self.title_font,
                 bg="#e0fcf4").grid(row=3,
                                    column=0,
                                    sticky=Tk.W)
        self.text_reports.grid(row=4, column=0, columnspan=3, sticky=Tk.W, padx=2, pady=2)

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

    def delete_job(self, id, job, archive=None):
        if archive:
            archive_years = ['2020','2021']
            for item in archive_years:
                self.addel.delete_cannajob_entry_archive((id,), item)
                self.addel.delete_cannajob_tests_archive((job,), item)
                self.addel.delete_cannajob_test_notes_archive((job,), item)
        else:
            self.addel.delete_cannajob_entry((id,))
            self.addel.delete_cannajob_tests((job,))
            self.addel.delete_cannajob_test_notes((job,))
        self.parent.display_searchpage()

    def update_notes(self, job, view=None):
        entry = (job[1],
                 self.job_notes.get("1.0", 'end-1c'),
                 datetime.date.today())
        self.addel.new_cannajobs_test_notes_entry(entry)
        if view:
            self.parent.display_jobpage(job, view=True)
        else:
            self.parent.display_jobpage(job)

    def get_relevant_intake_photos(self, job):
        self.picture_frame.grid(row=1, column=2, rowspan=3, sticky=Tk.NW, pady=5,  padx=2, ipadx=2, ipady=2)
        self.picture_sub_frame.pack()
        display_all_jobs_canvas = Tk.Canvas(self.picture_frame,
                                            width=330,
                                            height=505,
                                            bg="#e0fcf4",
                                            highlightbackground = '#e0fcf4',
                                            scrollregion=(0, 0, 0, 15000),)
        all_entries_scroll = Tk.Scrollbar(self.picture_frame,
                                          orient="vertical",
                                          bg="#e0fcf4",
                                          command=display_all_jobs_canvas.yview,)
        self.picture_sub_frame = Tk.Frame(self.picture_frame, bg="#e0fcf4")
        display_all_jobs_canvas.configure(yscrollcommand=all_entries_scroll.set)
        all_entries_scroll.pack(side='right',
                                fill='y')
        display_all_jobs_canvas.pack(side="left",
                                     fill='y')
        display_all_jobs_canvas.create_window((0, 0),
                                              window=self.picture_sub_frame,
                                              anchor='nw')
        path = r"""T:\ANALYST WORK FILES\Peter\Easy Interactive Tools\ """
        path = path[:-1]
        image_search_token = path + job[1] + "*.jpg"
        picture_list = []
        for infile in glob.glob(image_search_token):
            im = Image.open(infile)
            filename = im.filename
            im = im.resize((300, 300), Image.ANTIALIAS)
            render = ImageTk.PhotoImage(im)
            img = Tk.Label(self.picture_sub_frame, image=render, bg="#e0fcf4")
            img.image = render
            picture_list.append([img, filename[-16:]])
        for item in picture_list:
            Tk.Label(self.picture_sub_frame, text=item[1], font=self.jobpage_font, bg="#e0fcf4").pack()
            item[0].pack()

    def get_relevant_exit_pdf_links(self, job):
        self.links_display_frame.grid(row=2, column=3, sticky=Tk.NW, padx=5, pady=5, ipadx=2, ipady=2)
        path = r"""U:\COPY\Cannabis Benchsheets\ """
        path = path[:-1]
        link_search_token = path + r"**\* " + job[1][-4:] + ".pdf"
        self.link_list = []
        self.brief_link_list = []
        for infile in glob.glob(link_search_token, recursive=True):
            self.filter_and_append_links_to_list(infile, job)
        self.link_list_variable = Tk.StringVar(self.links_display_frame)
        Tk.Label(self.links_display_frame,
                 text="Bench Sheets & COCs",
                 font=self.title_font,
                 bg="#e0fcf4").grid(row=0, column=0, sticky=Tk.W)
        Tk.Label(self.links_display_frame,
                 text="(Complete jobs only)",
                 bg="#e0fcf4").grid(row=1, column=0, sticky=Tk.W)
        try:
            self.link_list_variable.set(self.brief_link_list[0])
            f = Tk.OptionMenu(self.links_display_frame, self.link_list_variable, *self.brief_link_list)
            f.grid(row=2, column=0, sticky=Tk.W)
            Tk.Button(self.links_display_frame,
                      text="View pdf file",
                      command=lambda: self.open_link_using_preferred_software(self.link_list_variable.get())).grid(row=3,
                                                                                                                   column=0,
                                                                                                                   sticky=Tk.W)
        except IndexError:
            Tk.Label(self.links_display_frame,
                     text="no scanned bench sheets found.",
                     bg="#e0fcf4").grid(row=2, column=0, sticky=Tk.W)

    def filter_and_append_links_to_list(self, infile, job):
        splitter = r"\ "
        split_file = infile.split(splitter[:-1])
        file_id = infile.split(splitter[:-1])[-2][1:4]
        job_id = job[1][0:3]
        if file_id == 'hem':
            self.link_list.append(infile)
            self.brief_link_list.append(split_file[-1])
        elif str(file_id) == str(job_id):
            self.link_list.append(infile)
            self.brief_link_list.append(split_file[-1])
        else:
            pass

    def get_relevant_customer_good_copies(self, job):
        self.good_copies_display_frame.grid(row=3, column=3, sticky=Tk.NW, padx=5, pady=5, ipadx=2, ipady=2)
        path = r"""U:\CLIENT GOOD COPIES\CANNABIS + DRUGS\ """
        path = path[:-1]
        link_search_token = path + r"**\* " + job[1][-4:] + ".pdf"
        self.good_copy_list = []
        self.brief_good_copy_list = []
        for infile in glob.glob(link_search_token, recursive=True):
            self.filter_and_append_good_copies_to_list(infile, job)
        path = r"""U:\CLIENT GOOD COPIES\ """
        path = path[:-1]
        link_search_token = path + r"* " + job[1][-4:] + ".pdf"
        for infile in glob.glob(link_search_token):
            self.filter_and_append_good_copies_to_list(infile, job)
        self.good_copy_variable = Tk.StringVar(self.good_copies_display_frame)
        Tk.Label(self.good_copies_display_frame,
                 text="Client Good Copies",
                 font=self.title_font,
                 bg="#e0fcf4").grid(row=0, column=0, sticky=Tk.W)
        Tk.Label(self.good_copies_display_frame,
                 text="(Complete jobs only)",
                 bg="#e0fcf4").grid(row=1, column=0, sticky=Tk.W)
        try:
            self.good_copy_variable.set(self.brief_good_copy_list[0])
            f = Tk.OptionMenu(self.good_copies_display_frame, self.good_copy_variable, *self.brief_good_copy_list)
            f.grid(row=2, column=0, sticky=Tk.W)
            Tk.Button(self.good_copies_display_frame,
                      text="View pdf file",
                      command=lambda: self.open_good_copy_using_preferred_software(self.good_copy_variable.get())).grid(row=3,
                                                                                                                        column=0,
                                                                                                                        sticky=Tk.W)
        except IndexError:
            Tk.Label(self.good_copies_display_frame,
                     text="no good copies found.",
                     bg="#e0fcf4").grid(row=2, column=0, sticky=Tk.W)

    def filter_and_append_good_copies_to_list(self, infile, job):
        splitter = r"\ "
        split_file = infile.split(splitter[:-1])
        file_id = infile.split(splitter[:-1])[-2][1:4]
        job_id = job[1][0:3]
        if file_id in ['LIE', 'EMP', '-Z ']:
            self.good_copy_list.append(infile)
            self.brief_good_copy_list.append(split_file[-1])
        elif str(file_id) == str(job_id):
            self.good_copy_list.append(infile)
            self.brief_good_copy_list.append(split_file[-1])
        else:
            pass

    def open_link_using_preferred_software(self, link):
        os.startfile(self.link_list[self.brief_link_list.index(link)])

    def open_good_copy_using_preferred_software(self, link):
        os.startfile(self.good_copy_list[self.brief_good_copy_list.index(link)])
