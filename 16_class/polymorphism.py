#!/usr/bin/python3

"""
	Polymorphism allows us to control
	derived classes from the base class
	and vice versa.

	In contrast to other OOP languages,
	Python also supports polymorphism,
	however, this is a bit weired...
"""

class GeometricObject():
	def __init__(this) -> None:
		print("base constructor")
	#end constructor

	def __del__(this) -> None:
		print("base destructor")
	#end destructor

	def identifyObject(this) -> None:
		#	do nothing here
		pass
	#end method
#end class

class Circle(GeometricObject):
	def __init__(this) -> None:
		print("circle constructor")
	#end constructor

	def __del__(this) -> None:
		print("circle destructor")
	#end destructor

	def identifyObject(this) -> str:
		return "Circle of life. *cough*"
	#end method
#end class

class Rectangle(GeometricObject):
	def __init__(this) -> None:
		print("rectangle constructor")
	#end constructor

	def __del__(this) -> None:
		print("rectangle destructor")
	#end destructor

	def identifyObject(this) -> str:
		return "No (rect-)angle."
	#end method
#end class

def main() -> None:
	'''
		"Polymorphism" is in use by any collection
		and you can "walk" trough your objects...
	'''
	polymorphism = (GeometricObject(), Circle(), Rectangle())

	for p in polymorphism:
		print(p.identifyObject())
	#end for
#end main

if __name__ == '__main__':
	main()
#end entry point