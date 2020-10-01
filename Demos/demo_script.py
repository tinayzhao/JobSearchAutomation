from new_db import drop_table, create_table, populate_table, export_csv, get_column_name, get_rows, get_all_columns
from remotework import get_webpage, get_data, find_links
from airtable import Airtable
import secret

#Test Requests and Beautiful Soup

#webpage = get_webpage("https://weworkremotely.com/categories/remote-programming-jobs")

#Prints Request object
#print(webpage)

#prints content of the Request object (HTML code of the website requested)
#print(webpage.content)

#
#prints data in final format
#print(data)\

webpage = get_webpage("https://weworkremotely.com/categories/remote-programming-jobs")
data = get_data(webpage, 'company', 'title')

drop_table("Remote_work")
create_table('Remote_work', ['Company', 'Position', 'Link'], ['TEXT', 'TEXT', 'TEXT'])
populate_table('Remote_work', 0, data)


#Airtable API
all_rows = get_rows('Remote_work')
columns = get_all_columns('Remote_work')


remotetable = Airtable('app7MGkIIuH9oeI5V', 'Remote Jobs', secret.API_KEY)

for i in all_rows:
	row = {}
	for j in range(0, len(columns)):
		row[columns[j][1]] = i[j]
	print(row)
	remotetable.insert(row)