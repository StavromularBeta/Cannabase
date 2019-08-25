from connector import Connector
import datetime


class Selection(Connector):
    def __init__(self):
        super(Selection, self).__init__()
        super(self.__class__, self).__init__()
        self.table_names = {1: 'cannajobs',
                            2: 'cannajobs_tests',
                            3: 'cannajobs_test_notes',
                            4: 'cannajobs' + str(datetime.date.today().year),
                            5: 'cannajobs_tests' + str(datetime.date.today().year),
                            6: 'cannajobs_test_notes' + str(datetime.date.today().year)}
        self.cannajobs_field_names = {1: 'id',
                                      2: 'job_number',
                                      3: 'tests',
                                      4: 'client_name',
                                      5: 'receive_date',
                                      6: 'status',
                                      7: 'complete_date'
                                      }
        self.cannajobs_tests_field_names = {1: 'id',
                                            2: 'job_number',
                                            3: 'test_type',
                                            4: 'submit_date',
                                            5: 'status',
                                            6: 'complete_date',
                                            }
        self.cannajobs_archive_field_names = {1: 'id',
                                              2: 'current_id',
                                              3: 'job_number',
                                              4: 'tests',
                                              5: 'client_name',
                                              6: 'receive_date',
                                              7: 'complete_date'
                                              }
        self.cannajobs_tests_archive_field_names = {1: 'id',
                                                    2: 'current_id',
                                                    3: 'job_number',
                                                    4: 'test_type',
                                                    5: 'submit_date',
                                                    6: 'complete_date',
                                                    }

    def select_all_from_table(self, table_number, print_view=None):
        query = "SELECT * FROM " + self.table_names[table_number]
        if print_view:
            for item in self.connector(query):
                print(item)
        else:
            return self.connector(query)

    def select_all_from_table_descending(self, table_number, print_view=None):
        query = "SELECT * FROM " + self.table_names[table_number] + " ORDER BY id DESC"
        if print_view:
            for item in self.connector(query):
                print(item)
        else:
            return self.connector(query)

    def select_from_cannajobs_table_with_conditions(self, field_number, condition, print_view=None):
        query = "SELECT * FROM cannajobs WHERE " + self.cannajobs_field_names[field_number] + " = (?)"
        if print_view:
            for item in self.connector(query, condition):
                print(item)
        else:
            return self.connector(query, condition)

    def select_from_cannajobs_tests__table_with_conditions(self, field_number, condition, print_view=None):
        query = "SELECT * FROM cannajobs_tests WHERE " + self.cannajobs_tests_field_names[field_number] + " = (?)"
        if print_view:
            for item in self.connector(query, condition):
                print(item)
        else:
            return self.connector(query, condition)

    def select_from_cannajobs_archive_table_with_conditions(self, field_number, condition, print_view=None):
        query = "SELECT * FROM cannajobs2019 WHERE " + self.cannajobs_archive_field_names[field_number] + " = (?)"
        if print_view:
            for item in self.connector(query, condition):
                print(item)
        else:
            return self.connector(query, condition)

    def select_from_cannajobs_tests_archive__table_with_conditions(self, field_number, condition, print_view=None):
        query = "SELECT * FROM cannajobs_tests2019 WHERE " + self.cannajobs_tests_archive_field_names[field_number] + " = (?)"
        if print_view:
            for item in self.connector(query, condition):
                print(item)
        else:
            return self.connector(query, condition)

    def select_latest_cannajobs_test_notes_for_job(self, job, print_view=None):
        job = (str(job),)
        query = "SELECT * FROM cannajobs_test_notes WHERE job_number = (?) ORDER BY id DESC LIMIT 1 "
        if print_view:
            for item in self.connector(query, job):
                print(item)
        else:
            return self.connector(query, job)
