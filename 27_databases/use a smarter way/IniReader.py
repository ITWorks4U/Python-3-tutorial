#!/usr/bin/python3

class IniReader():
	#	host name
	Host = None

	#	database
	Database = None

	#	username
	UserName = None

	#	password
	Password = None

	#	required keys to get the
	#	certain values
	__host = 'host'
	__user = 'user'
	__passwd = 'password'
	__db = 'database'

	def __init__(self, source: str) -> None:
		if not isinstance(source, str):
			raise Exception('source must be a string')
		elif len(source) == 0:
			raise Exception('source must not be empty')
		#end if

		self.source = source
	#end constructor

	"""
		since a config file, like .ini is used,
		we're reading line by line and must remove
		the last character, which is a newline ('\n)
		except for our last line. Unless, it also has
		a newline, too.
	"""
	def readFromIni(self):
		with open(self.source) as src:
			all = src.readlines()

			for line in all:
				splitted = line.split('=')

				if splitted[0] == self.__host:
					#	getting the current line without
					#	the newline (username and password
					# 	are handled identical)
					self.Host = splitted[1][:-1]
				elif splitted[0] == self.__user:
					self.UserName = splitted[1][:-1]
				elif splitted[0] == self.__passwd:
					self.Password = splitted[1][:-1]
				elif splitted[0] == self.__db:
					#	since database is the last entry without
					#	a newline, the complete value can be used
					self.Database = splitted[1]
				#end if
			#end for
		#end with
	#end method

	"""
		Just check, if everything is satisfied.
	"""
	def onCompleted(self):
		return len(self.Database) > 0 and len(self.Host) > 0 and len(self.UserName) > 0 and len(self.Password) > 0
	#end method
#end class