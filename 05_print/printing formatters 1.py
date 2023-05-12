#!/usr/bin/python3

"""
	using formatters for output;
	similar to C programming

	this can be used to force to use a
	specific expression of that type

	in contrast to C an error on
	runtime appears, if a wrong formatter
	is in use

	typical formatters:
		-	%c	<=>	single character
		-	%s	<=>	any string
		-	%d	<=>	decimal expression
		...

		for more informations, take a look there:
		-	https://docs.python.org/3/tutorial/inputoutput.html
		-	https://www.geeksforgeeks.org/string-formatting-in-python-using/
"""

stringVal = "This is a simple text."
numberVal = 100
booleanVal = False

#	------------------
#	using C-style formatters
#	------------------

#	formatting argument as a word
print("%s" % stringVal)
print("%d" % numberVal)

#	for a boolean expression
#	you can use %d as well as %s
print("%d" % booleanVal)
print("%s" % booleanVal)

#	in C this 'works', but not here
# 	=> TypeError: %d format: a number is required, not str
# print("%d" % stringVal)

#	------------------
#	using linear C-style formatters
#	important: the sequence must be identical with
#	the formatters and the length of the arguments
#	must be the number of used formatters
#	------------------
print("%s %d %s" % (stringVal, numberVal, booleanVal))