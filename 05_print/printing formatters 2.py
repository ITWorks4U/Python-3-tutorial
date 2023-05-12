#!/usr/bin/python3

"""
	Unlike using C-style formatters
	with their disadvantages, use
	a smarter way instead.
"""

stringVal = "This is a simple text."
numberVal = 100
booleanVal = False

#	------------------
#	automatically formatting
#	by the system => the sequence
#	will be processed 1 : 1
#	------------------
print("{}, {}, {}".format(stringVal, numberVal, booleanVal))

#	------------------
#	determine on which position
#	which argument is going to
#	print on the console
#	------------------
print("{2}, {0}, {1}".format(stringVal, numberVal, booleanVal))

#	------------------
#	using f literal at the beginning
#	and using the object inside of
#	the brackets
#	------------------
print(f"{stringVal}, {numberVal}, {booleanVal}")

#	------------------
#	replacing a certain expression
#	with another one
#	=> https://docs.python.org/3/tutorial/inputoutput.html#the-string-format-method
#	------------------
print('This {food} is {adjective}.'.format(food='spam', adjective='absolutely horrible'))

#	------------------
#	have some fun with loops
#	------------------
for x in range(1, 11):
	print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))
#end for