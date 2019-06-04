from connector import Connector


class AdDel(Connector):
    def __init__(self):
        super(AdDel, self).__init__()
        super(self.__class__, self).__init__()

    def new_cannajobs_entry(self, values):
        # job number, receive date, tests, status
        values_tuple = (values[0], values[1], values[2], values[3])
        query = 'INSERT INTO cannajobs (job_number, tests, receive_date, status) VALUES (?,?,?,?)'
        return self.connector(query, values_tuple)
