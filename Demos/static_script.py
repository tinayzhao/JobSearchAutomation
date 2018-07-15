from new_db import drop_table, create_table, populate_table, export_csv, get_column_name, get_rows, get_all_columns
from remotework import get_webpage, get_data, find_links
from airtable import Airtable
import secret

#Uses Airtable API client wrapper in Python: https://github.com/gtalarico/airtable-python-wrapper

#Test Requests and Beautiful Soup
drop_table("Remote_work")
webpage = get_webpage("https://weworkremotely.com/categories/remote-programming-jobs")
data = get_data(webpage, 'company', 'title')

#SQL Table Creation
create_table('Remote_work', ['Company', 'Position', 'Link', 'PostDate', 'UpdateDate'], ['TEXT', 'TEXT', 'TEXT', 'TEXT', 'TEXT'])
populate_table('Remote_work', 0, data)


#Export to CSV
#export_csv('Remote_work')

#Airtable API
all_rows = get_rows('Remote_work')
columns = get_all_columns('Remote_work')
remotetable = Airtable('app7MGkIIuH9oeI5V', 'Jobs', secret.API_KEY)

for i in all_rows:
	row = {}
	for j in range(0, len(columns)):
		row[columns[j][1]] = i[j]
	remotetable.insert(row)
	
