from connector import Connector


class Selection(Connector):
    def __init__(self):
        super(Selection, self).__init__()
        super(self.__class__, self).__init__()
        self.table_names = {1: 'cannajobs'}
        self.cannajobs_field_names = {1: 'id',
                                      2: 'job_number',
                                      3: 'tests',
                                      4: 'receive_date',
                                      5: 'status'
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



