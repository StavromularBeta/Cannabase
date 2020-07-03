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
customer_list = ['Ray Ketabi', 'Whistler Medical Marijuana Corp', 'Ethos Logistics', 'CanLabs', 'Grassroots Cannabis Growers', 'Eric Smith', 'Eagle Logistics', 'Christine Mareike Klem', 'Brandon Grieve-Heringa', 'Meg Ragarim', 'Nathaniel Simpson']
for item in customer_list:
    cannajobs_entry.new_customer_entry((0,item,1))