from connector import Connector


class AdDel(Connector):
    def __init__(self):
        super(AdDel, self).__init__()
        super(self.__class__, self).__init__()

    def new_cannajobs_entry(self, values):
        values_tuple = (values[0], values[1], values[2], values[3], values[4], values[5])
        query = 'INSERT INTO cannajobs (job_number, tests, client_name, receive_date, status, complete_date) VALUES (?,?,?,?,?,?)'
        return self.connector(query, values_tuple)

    def new_cannajobs_tests_entry(self, values):
        values_tuple = (values[0], values[1], values[2], values[3], values[4])
        query = 'INSERT INTO cannajobs_tests (job_number, test_type, submit_date, status, complete_date) VALUES (?,?,?,?,?)'
        return self.connector(query, values_tuple)

    def delete_cannajob_entry(self, id):
        query = 'DELETE FROM cannajobs WHERE id = ?'
        return self.connector(query, id)

    def delete_cannajob_tests(self, job_number):
        query = 'DELETE FROM cannajobs_tests WHERE job_number = ?'
        return self.connector(query, job_number)
