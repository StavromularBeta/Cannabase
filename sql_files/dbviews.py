from connector import Connector


class DbViews(Connector):
    def __init__(self):
        super(DbViews, self).__init__()
        super(self.__class__, self).__init__()

    def master_table_query(self):
        query = " SELECT * FROM sqlite_master "
        return self.connector(query)


