from airtable import Airtable
import secret

table = Airtable('app7MGkIIuH9oeI5V', 'Remote Jobs', secret.API_KEY)

#populates airtable
def populate_airtable(rows, columns):
	for i in rows:
		row = {}
		for j in range(0, len(columns)):
			row[columns[j][1]] = i[j]
		table.insert(row)

def airtable_info(rows, columns):
	info = []
	for i in rows:
		row = {}
		for j in range(0, len(columns)):
			row[columns[j][1]] = i[j]
		info.append(row)
	return info

#replace info
def update_airtable(rows, columns):
	table.mirror(airtable_info(rows, columns))

def filter_get(formula1):
	lst = table.get_all(formula=formula1)
	res = []
	for i in lst:
		info = i["fields"]
		sub = [info["Company"], info["Position"], info["Link"]]
		res.append(sub)
	return res

def remind(lst, index):
	lst = lst[0]
	print("Apply for " + lst[1] + " at " + lst[0] + " here: " + lst[2] + "!!!!")



