#!/usr/bin/python3

"""
	Regular expressions are a well tool
	to check a certain expression.

	Checking, if an expression is a number:

	Typically, you're using int(expression)
	to try to convert it into a number,
	howver, it fails with an exception,
	if the expression doesn't contain
	numerical characters only.
	=>	This could be handled with an exception handling.

	Our you could use a regular expression,
	which checks, if a certain expression
	passes trough a defined filter or not.
	=>	In that case no exception handling is necessary.

	For more details, take a look to this video:
	https://www.youtube.com/watch?v=vvFPWHHto00

	(German commentary, English text)
"""

#	importing regular expression module
import re

#	defining a filter, where each expression
#	must satisfy this filter condition
#
#	the expression with any length (0,1,2,...)
#	must have characters in a range of 0 to 9
filter = "^(-|\+)?[0-9]+$"

expressions = ('123', 'Is mayonnaise also an instrument?', 2390472397492984927429648236, '0', '-10', '+73', list(), 'Hello regular expression in python 3!')

for e in expressions:
	try:
		if re.match(filter, e):
			print(f'"{e}" is a number')
		else:
			print(f'"{e}" is a not number')
		#end if
	except TypeError as te:
		print(f'error for "{e}" detected: {te.args}')
#end for