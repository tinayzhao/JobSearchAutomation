from new_db import drop_table, create_table, populate_table, export_csv, get_column_name
from remotework import get_webpage, get_data, find_links
from airtable import Airtable

#Test Requests and Beautiful Soup
drop_table("Remote_work")
webpage = get_webpage("https://weworkremotely.com/categories/remote-programming-jobs")
data = get_data(webpage, 'company', 'title')

#SQL Table Creation
create_table('Remote_work', ['Company', 'Position', 'Link'], ['TEXT', 'TEXT', 'TEXT'])
populate_table('Remote_work', 0, data)
print(get_column_name("Remote_work", 0))
#Export to CSV
#export_csv('Remote_work')

#Airtable API
#remotetable = Airtable('app7MGkIIuH9oeI5V', 'Remote Work', 'key4RKPGoJAzzJzAO')
