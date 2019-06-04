from connector import Connector


class EditEntry(Connector):
    def __init__(self):
        super(EditEntry, self).__init__()
        super(self.__class__, self).__init__()
        self.cannajobs_field_names = {1: 'id',
                                      2: 'job_number',
                                      3: 'tests',
                                      4: 'receive_date',
                                      5: 'status'
                                      }

    def edit_cannajobs_entry(self, field, update, customer_id):
        query = 'UPDATE cannajobs SET ' + self.rolodex_field_names[field] + " = '" + update + "' WHERE id = " +\
                str(customer_id)
        print(query)
        return self.connector(query)
