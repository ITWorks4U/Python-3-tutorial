#!/usr/bin/python3

"""
	You're also able to overwrite class methods.
	To do this, implement the certain method, which starts
	with __, like __eq__, __add__ etc.

	Fun fact: We've already used a method override, see constructor
	or destructor. :o)

	video tutorial:	https://youtu.be/AK44C_uZ9u4
	timestamp:		03:06:53
"""

class Simple():
	def __init__(self, a: int, b: int) -> None:
		self.a = a
		self.b = b
	#end constructor

	#	auto implementation for __eq__
	def __eq__(self, __value: object) -> bool:
		return self.a == __value.a and self.b == __value.b
	#end method

	#	custom implementation
	def __add__(self, o):
		return self.a + o.a, self.b + o.b
	#end method

	def __sub__(self, o):
		return self.a - o.a, self.b - o.b
	#end method

#end class

s1 = Simple(10,20)
s2 = Simple(10,21)

print(f'Are s1 and s2 equal? {s1.__eq__(s2)}')
print(f's1 + s2: {s1.__add__(s2)}')
print(f's1 - s2: {s1.__sub__(s2)}')