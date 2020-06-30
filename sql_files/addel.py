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

    def new_customer_entry(self, values):
        values_tuple = (values[0], values[1], values[2])
        query = 'INSERT INTO canna_customers (company_id, client_name, status) VALUES (?,?,?)'
        return self.connector(query, values_tuple)

    def new_cannajobs_tests_entry(self, values):
        values_tuple = (values[0], values[1], values[2], values[3], values[4])
        query = 'INSERT INTO cannajobs_tests (job_number, test_type, submit_date, status, complete_date) VALUES (?,?,?,?,?)'
        return self.connector(query, values_tuple)

    def new_cannajobs_test_notes_entry(self, values):
        values_tuple = (values[0], values[1], values[2])
        query = 'INSERT INTO cannajobs_test_notes (job_number, note, note_date) VALUES (?,?,?)'
        return self.connector(query, values_tuple)


    # Delete Entries and archive entries

    def delete_cannajob_entry(self, id):
        query = 'DELETE FROM cannajobs WHERE id = ?'
        return self.connector(query, id)

    def delete_canna_customer_entry(self, id):
        query = 'DELETE FROM canna_customers WHERE id = ?'
        return self.connector(query, id)

    def delete_cannajob_tests(self, job_number):
        query = 'DELETE FROM cannajobs_tests WHERE job_number = ?'
        return self.connector(query, job_number)

    def delete_cannajob_test_notes(self, job_number):
        query = 'DELETE FROM cannajobs_test_notes WHERE job_number = ?'
        return self.connector(query, job_number)

    def delete_cannajob_entry_archive(self, id, table_name):
        query = 'DELETE FROM cannajobs' + table_name + ' WHERE id = (?)'
        return self.connector(query, id)

    def delete_cannajob_tests_archive(self, job_number, table_name):
        query = 'DELETE FROM cannajobs_tests' + table_name + ' WHERE job_number = (?)'
        return self.connector(query, job_number)

    def delete_cannajob_test_notes_archive(self, job_number, table_name):
        query = 'DELETE FROM cannajobs_test_notes' + table_name + ' WHERE job_number = (?)'
        return self.connector(query, job_number)

    def delete_archived_cannjob_entry_from_current(self):
        query = 'DELETE FROM cannajobs WHERE job_number IN (SELECT job_number FROM cannajobs' +\
                str(datetime.date.today().year) + ')'
        return self.connector(query)

    def delete_archived_cannjob_test__entry_from_current(self):
        query = 'DELETE FROM cannajobs_tests WHERE job_number IN (SELECT job_number FROM cannajobs' +\
                str(datetime.date.today().year) + ')'
        return self.connector(query)

    def delete_archived_cannjob_test_notes_entry_from_current(self):
        query = 'DELETE FROM cannajobs_test_notes WHERE job_number IN (SELECT job_number FROM cannajobs' +\
                str(datetime.date.today().year) + ')'
        return self.connector(query)

    # Archive entries

    def archive_cannajob_entry(self):
        query = 'INSERT OR IGNORE INTO cannajobs' + str(datetime.date.today().year) + ' SELECT * FROM cannajobs WHERE ' +\
            "('2000-01-02' < complete_date )"
        print(query)
        return self.connector(query)

    def archive_cannajob_tests_entry(self):
        query = 'INSERT OR IGNORE INTO cannajobs_tests' + str(datetime.date.today().year) + ' SELECT * FROM cannajobs_tests WHERE ' +\
            'job_number IN (SELECT job_number FROM cannajobs' + str(datetime.date.today().year) + ')'
        return self.connector(query)

    def archive_cannajob_test_notes_entry(self):
        query = 'INSERT OR IGNORE INTO cannajobs_test_notes' + str(datetime.date.today().year) + ' SELECT * FROM cannajobs_test_notes WHERE ' +\
            'job_number IN (SELECT job_number FROM cannajobs' + str(datetime.date.today().year) + ')'
        return self.connector(query)

