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
	print('Updated as of '  + now.strftime('%m/%d/%y %I:%M:%f'))
	return res

#Use Beautiful Soup to return data
def get_data(res, *classId):	
	soup = bs4.BeautifulSoup(res.text, "lxml")
	columns = []
	for c in classId: 
		col = soup.select('.' + c)
		columns.append(col)
	return columns


#run this
webpage = get_webpage()
data = get_data(webpage, 'company')
#new_db.create_table('Remote_work', 'Company', 'TEXT')
#new_db.populate_table('Remote_work', 'Company', data)
new_db.get_row('Remote_work', 'Company', 'Bitovi')[0]
#create_table('Remote_work', 'Company', 'TYPE')

