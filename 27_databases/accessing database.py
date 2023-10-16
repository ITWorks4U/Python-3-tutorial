#!/usr/bin/python3

"""
	Accessing to a database server, like mysql.
	With python you're able to do this.

	attention:
		-	these examples worked on a local installed
			mysql server only
		-	therefore we're using an external user,
			with access rights to a certain database,
			table and commands
			=> make sure to have an external user
			created before
		-	a test database with the name 'test' has been used
		-	followed by a table with the name 'TestTable'
		-	this contained 2 rows:
			-	ID (int)
			-	description (varchar(50))
		
		-	on other DBMS this might not work (correctly)
	
	Usually no db package comes with python.
	The package mysql-connector-python is used.
	Similar packages might work as well, but these weren't tested.

	To check, if you have installed this package, type:
		pip3 list | grep mysql-connector-python

		(UNIX/Linux / possible macOS only)
		for windows:
			pip.exe list and then you must look (:

	video tutorial:	https://youtu.be/AK44C_uZ9u4
	timestamp:		05:44:12
"""

import getpass as gp
import mysql.connector as conn

name = input('enter username: ')
passwd = gp.getpass('enter password: ')
host = input('enter host: ')
db = input('enter database: ')

try:
	with conn.connect(host=host, user=name, password=passwd, database=db) as mysql:
		#	testing the connection
		print('connection established')

		#	pointer for sql commands
		cursor = mysql.cursor()

		#	send a query
		cursor.execute('select * from TestTable;')

		#	receive n rows (n = 0,1,2,...)
		result = cursor.fetchall()

		if len(result) > 0:
			for r in result:
				print(r)
			#end for
		else:
			print('empty set')
		#end if
	#end with
except Exception as e:
	print(f'error: {e.args}')
#end try