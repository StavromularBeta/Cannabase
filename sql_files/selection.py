from connector import Connector


class Selection(Connector):
    def __init__(self):
        super(Selection, self).__init__()
        super(self.__class__, self).__init__()
        self.table_names = {1: 'cannajobs',
                            2: 'cannajobs_tests'}
        self.cannajobs_field_names = {1: 'id',
                                      2: 'job_number',
                                      3: 'tests',
                                      4: 'receive_date',
                                      5: 'status',
                                      6: 'complete_date'
                                      }
        self.cannajobs_tests_field_names = {1: 'id',
                                            2: 'job_number',
                                            3: 'test_type',
                                            4: 'submit_date',
                                            5: 'status',
                                            6: 'complete_date',
                                            }

    def select_all_from_table(self, table_number, print_view=None):
        query = "SELECT * FROM " + self.table_names[table_number]
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

