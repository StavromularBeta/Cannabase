import os, sys, inspect
import sqlite3
# below 3 lines add the parent directory to the path, so that SQL_functions can be found.
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)


class Connector(object):
    def __init__(self):
        self.database_target = parentdir + "/database/Cannabase.db"

    def connector(self, query, arguments=None):
        db_connection = sqlite3.connect(self.database_target)
        cursor = db_connection.cursor()
        if arguments:
            # arguments has to be in the form of a tuple.
            cursor.execute(query, arguments)
        else:
            cursor.execute(query)
        db_connection.commit()
        returned_query = cursor
        # db_connection.close() removed because selection.py wasn't working, kept saying cannot op. on closed db.
        return returned_query
