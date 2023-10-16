#!/usr/bin/python3

"""
	custom module for
	exception handling

	video tutorial:	https://youtu.be/AK44C_uZ9u4
	timestamp:		03:55:37
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