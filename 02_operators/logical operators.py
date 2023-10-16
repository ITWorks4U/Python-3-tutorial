#!/usr/bin/python3

"""
	locical operators are in use to compare
	two or more values and their result
	returns true or false

	video tutorial:	https://youtu.be/AK44C_uZ9u4
	timestamp:		00:10:06
"""

#	values to use
a = True
b = False

print("--- locical operations ---")

print(a)
print(b)

#	combining true and false (in technical language: 1 and 0), where the result is always false (0)
#	similar in other higher languages: a && b
print(a and b)

#	combining true or false, where the result is false only,
#	if all values are false, otherwise true
print(a or b)

#	negation of their value(s)
print(not a)
print(not b)
print(not not a)

#	!(a && b) = !a || !b
#	!(true and false) = !true or !false = false or true = true
print(not(a and b))


print(not(a or b))
print(not(a and not b))
print(not(a or not b))
print(not(not a and b))
print(not(not a or b))