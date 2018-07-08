import new_db
from remotework import get_webpage, get_data, find_links

new_db.drop_table("Remote_work")
webpage = get_webpage("https://weworkremotely.com/categories/remote-programming-jobs")
data = get_data(webpage, 'company', 'title')
new_db.create_table('Remote_work', ['Company', 'Position', 'Link'], ['TEXT', 'TEXT', 'TEXT'])
new_db.populate_table('Remote_work', data)
new_db.print_table('Remote_work')
