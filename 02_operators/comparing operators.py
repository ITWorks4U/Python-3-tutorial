#!/usr/bin/python3

"""
	comparing allows you to check one
	or more values each other

	returns true or false only

	video tutorial:	https://youtu.be/AK44C_uZ9u4
	timestamp:		00:10:06
"""

a = 10
b = 20

#	for boolean output: use %s (string)
print("--- comparing operations ---")

#	assuming, that 10 is equal to 20 => returns false
print(a == b)

#	assuming, that 10 is unequal to 20 => returns true
print(a != b)

#	a (10) is greater than b (20) => false
print(a > b)

#	a (10) is smaller than b (20) => true
print(a < b)

#	a (10) is greater than or equal to b (20) => false
print(a >= b)

#	a (10) is smaller than or equal to b (20) => true
print(a <= b)