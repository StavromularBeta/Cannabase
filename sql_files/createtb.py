from connector import Connector


class CreateTb(Connector):
    def __init__(self):
        super(CreateTb, self).__init__()
        super(self.__class__, self).__init__()
        self.table_dictionary = {1: """ CREATE TABLE IF NOT EXISTS cannajobs (
                                           id integer PRIMARY KEY,
                                           job_number text,
                                           tests int,
                                           receive_date date,
                                           status BOOLEAN ) """
                                 }

    def create_table(self, dictionary_index):
        query = self.table_dictionary[dictionary_index]
        return self.connector(query)


db = CreateTb()
db.create_table(1)