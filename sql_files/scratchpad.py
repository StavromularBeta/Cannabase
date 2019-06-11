from addel import AdDel
from selection import Selection
from editentry import EditEntry
import datetime

cannajobs_entry = AdDel()
cannajobs_selection = Selection()
# job number, receive date, tests, status
cannajobs_selection.select_all_from_table(1, True)
print('----')
cannajobs_selection.select_all_from_table(2, True)
#cannajobs_edit = EditEntry()
#cannajobs_edit.edit_cannajobs_entry(5, 1, 2)
#cannajobs_selection.select_all_from_table(1, True)