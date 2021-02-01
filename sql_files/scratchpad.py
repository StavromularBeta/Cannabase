from addel import AdDel
from selection import Selection
from editentry import EditEntry
import datetime

cannajobs_entry = AdDel()
cannajobs_selection = Selection()
cannajobs_edit = EditEntry()
# job number, receive date, tests, status
#cannajobs_selection.select_all_from_table_descending(7, True)
#cannajobs_entry.delete_canna_customer_entry((258,))
cannajobs_selection.select_all_from_table_descending(1, True)
#cannajobs_edit = EditEntry()
#cannajobs_edit.edit_cannajobs_entry(1, 452, 1)
#print('----')
#cannajobs_entry.delete_canna_customer_entry((193,))