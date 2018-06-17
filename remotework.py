import requests
import bs4
import csv
import datetime
import new_db


#Basic Web Scraper (uses Requests and BeautifulSoup)

#Requests the webpage and checks for errors
def get_webpage(url):
	res = requests.get(url)
	now = datetime.datetime.now()
	try:
		res.raise_for_status()
	except Exception as e:
		print(e)
	print('Updated as of '  + now.strftime('%m/%d/%y %I:%M:%f'))
	return res

#Use Beautiful Soup to select data
def get_data(res, *classId):	
	soup = bs4.BeautifulSoup(res.text, "lxml")
	columns = []
	for c in classId: 
		col = soup.select('.' + c)
		columns.append(col)
	return columns


#run this
webpage = get_webpage('https://weworkremotely.com/categories/remote-programming-jobs')
data = get_data(webpage, 'company')
#new_db.create_table('Remote_work', 'Company', 'TEXT')
#new_db.populate_table('Remote_work', 'Company', data)
new_db.get_row('Remote_work', 'Company', 'Bitovi')[0]
#create_table('Remote_work', 'Company', 'TYPE')

