import sqlite3
import pandas as pd
from selenium import webdriver

#Database Demo File

sqlite_file = 'cs_database.sqlite'
conn = sqlite3.connect(sqlite_file)
cur = conn.cursor()

def create_table(table_name, columns, types): 
	command = 'CREATE TABLE {tn} ({fc} {ft},'.format(tn = table_name, fc = columns[0], ft = types[0])
	for i in range(1, len(columns)):
		command += '{c} {t}'.format(c = columns[i], t = types[i])
		if i != len(columns) - 1:
			command += ','
	command += ')'
	cur.execute(command)
	conn.commit()

def list_tables():
	res = conn.execute("SELECT name FROM sqlite_master WHERE type='table';")
	for name in res:
		print(name[0])

def get_column_name(table_name, index):
	res = cur.execute("PRAGMA table_info({tn})".format(tn=table_name))
	track = 0
	for i in res:
		if index == track:
			return i[1]
		track+=1

def check_schema(table_name):
	res = conn.execute("SELECT sql FROM sqlite_master WHERE name='{tn}';".format(tn=table_name))
	for s in res:
		print(s)

def view_contents(table_name):
	r = cur.execute("SELECT * from {tn}".format(tn = table_name))
	results = cur.fetchall()
	print(results)

def add_row2(table_name, column_name, content):
	cur.execute("INSERT INTO {tn} ({cn}) VALUES ('{ct}')".format(tn = table_name, cn = column_name, ct = content))

def add_row(table_name, column_list, row_values):
	command = "INSERT INTO {tn} (".format(tn = table_name)
	index = 0
	for i in column_list:
		if index != len(column_list) - 1:
			command += "{cn}, ".format(cn = i)
			index += 1
		else: 
			command += "{cn}) ".format(cn = i)
	command += "VALUES ("
	index = 0
	for j in row_values:
		if "'" not in j:
			if index != len(column_list) - 1:
				command += "'{ct}', ".format(ct = j)
				index += 1
			else: 
				command += "'{ct}') ".format(ct = j)
		else: 
			if index != len(column_list) - 1:
				command += "'{{ct}}', ".format(ct = j)
				index += 1
			else: 
				command += "'{{ct}}') ".format(ct = j)
	cur.execute(command)

#0 refers to static
#1 refers to Selenium
def populate_table(table_name, web_scraper, data):
	column_list = []
	for i in range(0, len(data)):
		column_name = get_column_name(table_name, i)
		column_list.append(column_name)
	for i in range(0, len(data[0])):
		row_values = []
		j = 0
		while j < len(data):
			val = data[j][i]
			if type(val) is str:
				row_values.append(val)
			else:
				if web_scraper == 0:
					row_values.append(val.getText())
				else:
					if type(val) is str:
						row_values.append(val)
					else:
						row_values.append(val.text)
			j += 1
		add_row(table_name, column_list, row_values)
	conn.commit()

def get_row(table_name, column_name, content):
	cur.execute("SELECT * FROM {tn} WHERE {cn}='{ct}'".format(tn = table_name, cn = column_name, ct = content))
	all_rows = cur.fetchall()
	print(all_rows)

def drop_table(table_name):
	cur.execute("DROP TABLE {tn}".format(tn = table_name))
	conn.commit()

def get_connect():
	cur = conn.cursor()
	return conn

def close_db():
	conn.commit()
	conn.close()

def print_table(table_name):
	print(pd.read_sql_query("SELECT * FROM {tn}".format(tn = table_name), conn))



