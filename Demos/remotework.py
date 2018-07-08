import requests
import bs4

'''
Basic Web Scraper (Built with Requests and BeautifulSoup)
----------------------------------------------------------
Before You Start:
1. Check site's robot.txt.
2. Familiarize yourself with the source code of the webpage
'''

#Requests the webpage and checks for errors
def get_webpage(url):
	res = requests.get(url)
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
	columns.append(find_links(res))
	return columns

def find_links(res):
    soup = bs4.BeautifulSoup(res.text, "lxml")
    link_lst = []
    for a in soup.find_all('a', href=True):
        if "/remote-jobs/" in a['href']:
            link_lst.append(a['href'])
    return link_lst