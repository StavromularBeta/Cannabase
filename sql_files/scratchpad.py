from addel import AdDel
from selection import Selection
from editentry import EditEntry
import datetime

cannajobs_entry = AdDel()
cannajobs_selection = Selection()
# job number, receive date, tests, status
fake_entry = ["W136101", datetime.date.today(), 135, False]
fake_tests_entry = ["W136101", 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
cannajobs_entry.new_cannajobs_entry(fake_entry)
cannajobs_entry.new_cannajobs_tests_entry(fake_tests_entry)
cannajobs_selection.select_all_from_table(1, True)
cannajobs_selection.select_all_from_table(2, True)
#cannajobs_edit = EditEntry()
#cannajobs_edit.edit_cannajobs_entry(5, 1, 2)
#cannajobs_selection.select_all_from_table(1, True)