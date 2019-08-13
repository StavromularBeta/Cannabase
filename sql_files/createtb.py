from connector import Connector
import datetime


class CreateTb(Connector):
    def __init__(self):
        super(CreateTb, self).__init__()
        super(self.__class__, self).__init__()
        self.table_dictionary = {1: """ CREATE TABLE IF NOT EXISTS cannajobs (
                                                    id integer PRIMARY KEY,
                                                    job_number text,
                                                    tests text,
                                                    client_name text,
                                                    receive_date date,
                                                    status int,
                                                    complete_date date) """,
                                 2: """ CREATE TABLE IF NOT EXISTS cannajobs_tests (
                                                   id integer PRIMARY KEY,
                                                   job_number text,
                                                   test_type int,
                                                   submit_date date,
                                                   status int,
                                                   complete_date date) """,
                                 3: """ CREATE TABLE IF NOT EXISTS cannajobs_test_notes (
                                                   id integer PRIMARY KEY,
                                                   job_number text,
                                                   note text,
                                                   note_date date)""",
                                 4: """ CREATE TABLE IF NOT EXISTS cannajobs""" + str(datetime.date.today().year) + """(
                                                   id integer PRIMARY KEY,
                                                   current_id int,
                                                   job_number text,
                                                   tests text,
                                                   client_name text,
                                                   receive_date date,
                                                   complete_date date) """,
                                 5: """ CREATE TABLE IF NOT EXISTS cannajobs_tests""" + str(datetime.date.today().year) + """ (
                                                   id integer PRIMARY KEY,
                                                   current_id int,
                                                   job_number text,
                                                   test_type int,
                                                   submit_date date,
                                                   complete_date date) """,
                                 6: """ CREATE TABLE IF NOT EXISTS cannajobs_test_notes""" + str(datetime.date.today().year) + """ (
                                                   id integer PRIMARY KEY,
                                                   job_number text,
                                                   note text,
                                                   note_date date)"""
                                 }

    def create_table(self, dictionary_index):
        query = self.table_dictionary[dictionary_index]
        return self.connector(query)


db = CreateTb()
db.create_table(1)
db.create_table(2)
db.create_table(3)
db.create_table(4)
db.create_table(5)
db.create_table(6)