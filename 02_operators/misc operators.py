#!/usr/bin/python3

"""
	any other operators, like
	memberships or identities

	are more in use for data structures
	or by using a specific object

	video tutorial:	https://youtu.be/AK44C_uZ9u4
	timestamp:		00:10:06
"""

a = 10
b = 20
tupleOfNumbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

#	membership operations (often used to check, if
#	a number is in a collection or not)
print("--- membership operations ---")
print(a in tupleOfNumbers)										#	claim, that a is a part ot the tuple: true
print(b in tupleOfNumbers)										#	claim, that b is a part of the tuple: false
print(a not in tupleOfNumbers)
print(b not in tupleOfNumbers)

#	identity operations (often used for object comparising,
#	e. g. if two objects refers to the exactly memory,
#	check, if a sub class is a part of a super class, etc.)
print("--- identity operations ---")
print(a is b)													#	claim, that a is identical to b: false
print(a is not b)