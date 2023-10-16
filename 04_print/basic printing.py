#!/usr/bin/python3

"""
	Printing something to the console
	by using print().

	This function also comes with a
	set of additional arguments to work
	with that.

	video tutorial:	https://youtu.be/AK44C_uZ9u4
	timestamp:		00:38:15
"""

#	------------------
#	basic usages
#	------------------

#	prints a newline
print()

#	using double quotas for a word...
print("123ABC")

#	single qoutas works also well
print('123ABC')

print("------------------")

#	------------------
#	printing more than one expression
#	------------------

stringVal = "This is a simple text."
numberVal = 100
booleanVal = False

#	print every variable including comma in
#	that linear order
print(stringVal, numberVal, booleanVal)

#	do a concatenation of two or more >>words<<
#	will be converted to a 'single word'
print(stringVal + str(numberVal) + str(booleanVal))