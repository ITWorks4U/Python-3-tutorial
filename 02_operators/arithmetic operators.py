#!/usr/bin/python3

"""
	arithmetical operators are the basic
	math operations like addition,
	subtraction, etc.

	video tutorial:	https://youtu.be/AK44C_uZ9u4
	timestamp:		00:10:06
"""

#	values to use
a = 10
b = 20

#	arithmetic operations
print("--- arithmetic operations ---")
print(a+b)
print(a-b)
print(a*b)
print(a/b)														#	result may be a relational number
print(a//b)														#	result is a decimal number only
print(a%b)
print(a**b)

#	assignments
print("--- assigning operations ---")
result = a + b
print(result)

result += a														#	equal to: result = result + a
print(result)

result -= b														#	equal to: result = result - b
print(result)

result += 1														#	Attention! In Python there is no result++
print(result)