#!/usr/bin/python3

'''
	In Python classes any class object
	is public by default, but can also
	defined as protected or private.

	In contrast to other OOP languages
	there's no 'public', 'protected' or
	'private'.

	However, the access is not identical
	in contrast to other OOP languages.
'''

class Point:
	x = 0			#	"public"
	_y = 0			#	"protected"
	__z = 0			#	"private"

	def __init__(self, x, y, z) -> None:
		self.x = x
		self._y = y
		self.__z = z
	#end constructor

	def getX(self):
		return self.x
	#end method

	def getY(self):
		return self._y
	#end method

	def getZ(self):
		return self.__z
	#end method
#end class

p = Point(x=10, y=-7, z=6)

#	attention: You need {} 3 times!
#	By using  {{p.getX()}} => 'p.getX()' as word returns only.
print(f'your coorinates: {{{p.getX()}, {p.getY()}, {p.getZ()}}}')

#	-------------
#	accessing to protected and
#	private objects from outside: only private members
#	can't be accessed from outside
#	-------------
print(f'your coorinates: {{{p.x}, {p._y}, {p.__z}}}')