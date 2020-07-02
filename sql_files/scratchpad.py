from addel import AdDel
from selection import Selection
from editentry import EditEntry
import datetime

cannajobs_entry = AdDel()
cannajobs_selection = Selection()
# job number, receive date, tests, status
#cannajobs_edit = EditEntry()
#cannajobs_edit.edit_cannajobs_entry(1, 452, 1)
#cannajobs_selection.select_all_from_table(4, True)
#print('----')
#cannajobs_entry.delete_canna_customer_entry((191,))
cannajobs_selection.select_all_from_customer_table_descending(7, True)