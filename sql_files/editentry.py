from connector import Connector


class EditEntry(Connector):
    def __init__(self):
        super(EditEntry, self).__init__()
        super(self.__class__, self).__init__()
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
                                            6: 'complete_date'
                                            }

    def edit_cannajobs_entry(self, field, update, customer_id):
        query = 'UPDATE cannajobs SET ' + self.cannajobs_field_names[field] + " = '" + str(update) + "' WHERE id = " +\
                str(customer_id)
        return self.connector(query)

    def edit_cannajobs_tests_entry(self, field, update, customer_id):
        query = 'UPDATE cannajobs_tests SET ' + self.cannajobs_tests_field_names[field] + " = '" + str(update) +\
                "' WHERE id = " + str(customer_id)
        return self.connector(query)
