#!/usr/bin/python3

"""
	Unlike to enter over and over again
	username, password, host and database
	use an ini file, which contains the
	required settings followed by
	a reader for ini files.
"""

import mysql.connector as conn
import IniReader as reader

try:
	r = reader.IniReader('connection.ini')
	r.readFromIni()

	if r.onCompleted():
		with conn.connect(host=r.Host, user=r.UserName, password=r.Password, database=r.Database) as mysql:
			print('connection established')
		#end with
	else:
		print('missing settings for connection')
	#end if
except Exception as e:
	print(f'error: {e.args}')
#end try