#!/usr/bin/python3

"""
	Using enumerations for any purpose.

	An "enumeration" is "just" a class,
	which inhertits Enum class from
	enum module.

	video tutorial:	https://youtu.be/AK44C_uZ9u4
	timestamp:		03:06:53
"""

#	required module to load
from enum import Enum as E

class Food(E):
	Apple = 1,
	Bulb = 2,
	Banana = 3,
	Burger = 4,
	Toast = 5
	#...
#end enumeration

#	-------------
#	A normal usage
#	is now impossible.
#	-------------
# f = Food()
# print(f'{f.Apple}, {f.Banana}', {f.Toast})

#	-------------
#	Use this instead.
#	-------------
print(f'{Food.Apple}, {Food.Banana}, {Food.Toast}')