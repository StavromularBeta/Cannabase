from connector import Connector
import datetime


class AdDel(Connector):
    def __init__(self):
        super(AdDel, self).__init__()
        super(self.__class__, self).__init__()

    # New Entries

    def new_cannajobs_entry(self, values):
        values_tuple = (values[0], values[1], values[2], values[3], values[4], values[5])
        query = 'INSERT INTO cannajobs (job_number, tests, client_name, receive_date, status, complete_date) VALUES (?,?,?,?,?,?)'
        return self.connector(query, values_tuple)

    def new_cannajobs_tests_entry(self, values):
        values_tuple = (values[0], values[1], values[2], values[3], values[4])
        query = 'INSERT INTO cannajobs_tests (job_number, test_type, submit_date, status, complete_date) VALUES (?,?,?,?,?)'
        return self.connector(query, values_tuple)

    def new_cannajobs_test_notes_entry(self, values):
        values_tuple = (values[0], values[1], values[2])
        query = 'INSERT INTO cannajobs_test_notes (job_number, note, note_date) VALUES (?,?,?)'
        return self.connector(query, values_tuple)


    # Delete Entries

    def delete_cannajob_entry(self, id):
        query = 'DELETE FROM cannajobs WHERE id = ?'
        return self.connector(query, id)

    def delete_cannajob_tests(self, job_number):
        query = 'DELETE FROM cannajobs_tests WHERE job_number = ?'
        return self.connector(query, job_number)

    def delete_cannajob_test_notes(self, job_number):
        query = 'DELETE FROM cannajobs_test_notes WHERE job_number = ?'
        return self.connector(query, job_number)

    # Archive

    def archive_cannajob_entry(self):
        query = 'INSERT OR IGNORE INTO cannajobs' + str(datetime.date.today().year) + ' SELECT * FROM cannajobs WHERE ' +\
            "'01-01-2000' < complete_date <= '" + str(datetime.date.today() - datetime.timedelta(days=3))+"'"
        return self.connector(query)

    def archive_cannajob_tests_entry(self):
        query = 'INSERT OR IGNORE INTO cannajobs_tests' + str(datetime.date.today().year) + ' SELECT * FROM cannajobs_tests WHERE ' +\
            'job_number IN (SELECT job_number FROM cannajobs' + str(datetime.date.today().year) + ')'
        return self.connector(query)

    def archive_cannajob_test_notes_entry(self):
        query = 'INSERT OR IGNORE INTO cannajobs_test_notes' + str(datetime.date.today().year) + ' SELECT * FROM cannajobs_test_notes WHERE ' +\
            'job_number IN (SELECT job_number FROM cannajobs' + str(datetime.date.today().year) + ')'
        return self.connector(query)

