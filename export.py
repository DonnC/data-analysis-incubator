# export sqlite3 database to excel/csv with pandas

import pandas as pd
import sqlite3
import sys
import argparse
import os
from time import sleep

def check_arg(args=None):
	parser = argparse.ArgumentParser(description='export database data to csv or excel file')

	parser.add_argument('-d', '--database',
						help = 'full database file path. Support sqlite3 databases only',
						required = 'True')
	
	parser.add_argument('-t', '--table',
						help = 'database table name',
						required = 'True')

	parser.add_argument('-n', '--name',
						help = 'new file name')

	parser.add_argument('-f', '--format',
						help = 'csv or xlsx format',
						required = 'True',
						choices = ('csv', 'xlsx'))

	parser.add_argument('-V', '--version', action='version', version='%(prog)s 1.0')

	results = parser.parse_args(args)
	return results

def check_file_exist(filename):
	if os.path.isfile(filename):
		return True

	else:
		return None

def do_export(db, df, to, fname):
	if to == 'csv' and fname:
		new = fname + '.csv'
		df.to_csv(new)
		print("[INFO] Exported to csv as ", new)

	elif to == 'csv' and fname == None:
		new = db + '.csv'
		df.to_csv(new)
		print("[INFO] Exported to csv as ", new)

	elif to == 'xlsx' and fname == None:
		new = fname + '.xlsx'
		df.to_excel(new)
		print("[INFO] Exported to excel as ", new)

	elif to == 'xlsx' and fname == None:
		new = db + '.xlsx'
		df.to_excel(new)
		print("[INFO] Exported to excel as ", new)

def convert(database, table, export_to, new_filename = None):
	if database.endswith('.db') or database.endswith('.sqlite3'):
		pass

	else:
		database = database + '.db'

	if not check_file_exist(database):
		# remove trailing file formats
		if database.endswith('.db'):
			database = database[:-3]

		elif database.endswith('.sqlite3'):
			database = database[:-8]
		
		print("[WARNING] Database file '{file}' does not exist or not supported".format(file=database))
		sleep(3)
		sys.exit()

	try:
		conn = sqlite3.connect(database)

		query = "SELECT * FROM %s" %table
		df = pd.read_sql_query(query, conn)
		sleep(1)
		conn.close()

		df.drop_duplicates(inplace=True)
		print("[INFO] Attempting to export..")
		do_export(database, df, export_to, new_filename)
		sleep(3)
		
	except Exception as e:
	    print("[ERROR] There was a problem converting file ", e)

def run():
	r = check_arg(sys.argv[1:])
	
	# try converting
	convert(r.database, r.table, r.format, r.name)

	print("[INFO] Operation complete")

if __name__ == "__main__":
	run()

