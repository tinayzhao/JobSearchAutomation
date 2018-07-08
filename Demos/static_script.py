import new_db
from remotework import get_webpage, get_data, find_links

webpage = get_webpage("https://weworkremotely.com/categories/remote-programming-jobs")
find_links(webpage)




#data = get_data(webpage, 'company', 'title')



#new_db.create_table('Remote_work', ['Company', 'Position'], ['TEXT', 'TEXT'])
#new_db.populate_table('Remote_work', data)
#new_db.list_tables()
