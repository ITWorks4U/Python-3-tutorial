#!/usr/bin/python3

"""
	custom module for
	exception handling
"""

class Simple:
	def __init__(self, arg = list()):
		self.__content = arg
	#end constructor

	def showContentType(self):
		return self.__content
	#end method

	"""
		many other methods here...
	"""
#end class

class NotSoSimple:
	pass
# end class