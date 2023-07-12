#!/usr/bin/python3

"""
	Regular expressions are a well tool
	to check a certain expression.

	Checking, if an expression is a number:

	Typically, you're using int(expression)
	to try to convert it into a number,
	however, it fails with an exception,
	if the expression doesn't contain
	numerical characters only.
	=>	This could be handled with an exception handling.

	Or you could use a regular expression,
	which checks, if a certain expression
	passes trough a defined filter or not.
	=>	In that case no exception handling is necessary.

	A regular expression can only be used on words!
	Since a word with a length n characters (n = 0, 1, 2, ..., k-1)
	is given, a regular expression can be used to define a filter
	to check, if this certain word passes the filter or not.

	Typicial filters are:
	-	^[A-Za-z0-9]+$
		-	any word with at least one character
		-	may contain a character between A-Z, a-z or 0-9
	
	-	^$
		-	empty words only (have a length of 0 characters)
	
	...
	
	When you're trying to use other objects, like numbers, collections,
	or else, the regular expression check usually fails and must be
	covered with an exception handling.

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