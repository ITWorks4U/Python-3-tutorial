#!/usr/bin/python3

"""
	Using a main function in python.

	Like in other programming languages
	the main() represents the
	starting section, however, in Python
	there's no main by default required
	or given.

	In this example, this python script
	offers classes only.
"""
from enum import Enum as E

#	-----------
#	class
#	-----------
class Simple:
	#	basically obsolete, since it's (re-)defined
	#	in constructor
	# __class_object = None

	#constructor
	def __init__(self, arg = tuple()):
		self.__class_object = arg
	#end constructor

	def Display(self):
		return self.__class_object
	#	end method
#end class

#	-----------
#	enumeration
#	-----------
class Food(E):
	Apple = 1,
	Bulb = 2,
	Banana = 3,
	Burger = 4,
	Toast = 5
	#...
#end enumeration

#	-----------
#	any other classes
#	or enumerations
#	here...
#	-----------