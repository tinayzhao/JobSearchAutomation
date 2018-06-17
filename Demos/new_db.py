import sqlite3

#Database File

sqlite_file = 'cs_database.sqlite'
conn = sqlite3.connect(sqlite_file)
cur = conn.cursor()

def create_table(table_name, first_column, first_type): 
	cur.execute('CREATE TABLE {tn} ({fc} {ft})'.format(tn = table_name, fc = first_column, ft = first_type))
	conn.commit()

def list_tables():
	res = conn.execute("SELECT name FROM sqlite_master WHERE type='table';")
	for name in res:
		print(name[0])

def check_schema(table_name):
	res = conn.execute("SELECT sql FROM sqlite_master WHERE name='{tn}';".format(tn=table_name))
	for s in res:
		print(s)

def view_contents(table_name):
	r = cur.execute("SELECT * from {tn}".format(tn = table_name))
	results = cur.fetchall()
	print(results)

def add_row(table_name, column_name, content):
	cur.execute("INSERT INTO {tn} ({cn}) VALUES ('{ct}')".format(tn = table_name, cn = column_name, ct = content))

def populate_table(table_name, column_name, data):
	for row in data[0]:
		c = row.getText()
		add_row(table_name, column_name, c)
	conn.commit()

def get_row(table_name, column_name, content):
	cur.execute("SELECT * FROM {tn} WHERE {cn}='{ct}'".format(tn = table_name, cn = column_name, ct = content))
	all_rows = cur.fetchall()
	print(all_rows)

def close_db():
	conn.commit()
	conn.close()

