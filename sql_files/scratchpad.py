from createtb import CreateTb
from dbviews import DbViews
from addel import AdDel
from selection import Selection

Rolodex_entry = AdDel()
Rolodex_selection = Selection()
#fake_entry = ["6", "a", "b", "1", "abc", "cash", True, "online"]
#Rolodex_entry.new_rolodex_entry(fake_entry)
Rolodex_selection.select_all_from_table(1, True)
