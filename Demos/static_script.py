import new_db
from remotework import get_webpage, get_data, find_links

webpage = get_webpage("https://weworkremotely.com/categories/remote-programming-jobs")
data = get_data(webpage, 'company', 'title')
print(len(data))
print("")
print(data[0])
print("")
print(data[1])
print("")
print(data[2])
#new_db.create_table('Remote_work', ['Company', 'Position', 'Link'], ['TEXT', 'TEXT', 'TEXT'])
new_db.populate_table('Remote_work', data)
new_db.print_table('Remote_work')



#data = get_data(webpage, 'company', 'title')



#new_db.create_table('Remote_work', ['Company', 'Position'], ['TEXT', 'TEXT'])
#new_db.populate_table('Remote_work', data)
#new_db.list_tables()
