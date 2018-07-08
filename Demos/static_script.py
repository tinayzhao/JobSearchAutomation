import new_db
from remotework import get_webpage, get_data

webpage = get_webpage()
data = get_data(webpage, 'company', 'title')
new_db.create_table('Remote_work', ['Company', 'Position'], ['TEXT', 'TEXT'])
new_db.populate_table('Remote_work', data)
new_db.list_tables()
