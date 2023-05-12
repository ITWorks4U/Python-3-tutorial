#!/usr/bin/python3

"""
	any other operators, like
	memberships or identities

	are more in use for data structures
	or by using a specific object
"""

a = 10
b = 20
tupleOfNumbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

print("--- membership operations ---")
print(a in tupleOfNumbers)										#	claim, that a is a part ot the tuple: true
print(b in tupleOfNumbers)										#	claim, that b is a part of the tuple: false
print(a not in tupleOfNumbers)
print(b not in tupleOfNumbers)

#	identity operations
print("--- identity operations ---")
print(a is b)													#	claim, that a is identical to b: false
print(a is not b)