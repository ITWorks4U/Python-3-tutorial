#!/usr/bin/python3

"""
	Like in other OOP programming languages
	you're also able to define abstract classes.

	A class is defined as abstact, if at least
	one method is marked as abstract.

	Since an abstract class exists, this can't be
	instanciated. It's just an interface, like a
	blueprint, where each sub class must implement
	each abstract method.

	video tutorial:	https://youtu.be/AK44C_uZ9u4
	timestamp:		03:06:53
"""

#	abc = abstract base class
from abc import ABC, abstractmethod
import math

class GeometricObject(ABC):
	#	marks the method below as abstract, thus
	#	every child class must implement this
	#	method
	@abstractmethod
	def calculateArea(self):
		pass
	#end method
#end class

class Rectangle(GeometricObject):
	def __init__(self, a: int, b: int) -> None:
		self.a = a
		self.b = b
	#end constructor

	def calculateArea(self):
		return self.a * self.b
	#end method
#end class

class Circle(GeometricObject):
	def __init__(self, r: int) -> None:
		self.r = r
	#end constructor

	def calculateArea(self):
		return math.pi * self.r * self.r
	#end method
#end class

if __name__ == '__main__':
	#	You're not allowed to create an instance
	#	of your abstract / interface class.
	# g = GeometricObject()
	# print(g.calculateArea())

	r = Rectangle(a=5,b=7)
	print(f'area of rectangle: {r.calculateArea()}')

	c = Circle(r=5)
	print(f'area of circle: {c.calculateArea()}')
#end entry point