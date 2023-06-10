#!/usr/bin/python3

"""
	using custom modules in python
"""

class Simple:
	def __init__(self, arg = list()):
		self.__content = arg
	#end constructor

	def showContentType(self):
		return self.__content
	#end method

	"""
		any other methods here...
	"""
#end class

class AnotherClass:
	pass
# end class