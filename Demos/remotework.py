import requests
import bs4
import csv
import datetime
import new_db

'''
Basic Web Scraper (Built with Requests and BeautifulSoup)
----------------------------------------------------------
Before You Start:
1. Check site's robot.txt.
2. Browse source code of the site
'''

'''
Requests the webpage and checks for errors
'''
def get_webpage():
	res = requests.get('https://weworkremotely.com/categories/remote-programming-jobs')
	now = datetime.datetime.now()
	try:
		res.raise_for_status()
	except Exception as e:
		print(e)
	return res

#Use Beautiful Soup to return data based off classId
def get_data(res, *classId):	
	soup = bs4.BeautifulSoup(res.text, "lxml")
	columns = []
	for c in classId: 
		col = soup.select('.' + c)
		columns.append(col)
	#print(columns[0])
	#print("")
	#print("")
	#print(columns[1])
	return columns



#run this
#webpage = get_webpage()
#data = get_data(webpage, 'company', 'title')
#new_db.create_table('Remote_work7', ['Company', 'Position'], ['TEXT', 'TEXT'])
#new_db.populate_table('Remote_work7', data)
#new_db.print_table('Remote_work7')
new_db.list_tables()

#new_db.create_table('Remote_work', 'Company', 'TEXT')
#new_db.populate_table('Remote_work', 'Company', data)
#new_db.view_contents('Remote_work')
#print("")
#new_db.get_row('Remote_work', 'Company', 'Bitovi')
#create_table('Remote_work', 'Company', 'TYPE')


