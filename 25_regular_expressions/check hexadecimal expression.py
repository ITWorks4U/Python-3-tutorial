#!/usr/bin/python3

"""
	Regular expressions are a well tool
	to check a certain expression.

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

	For more details, take a look to this video:
	https://www.youtube.com/watch?v=vvFPWHHto00

	(German commentary, English text)
"""

#	----------
#	checking, if the expression is in hexadecimal form:
#
#	^(0x|0X)?([A-Fa-f0-9]+)(H|h)?$
#		-	may start with 0x or 0X
#		-	contains A-F, a-f or 0-9 at least once
#		-	may end with h or H
#
#		will pass:
#		0x1h
#		0xFdaaH
#		0xface
#		Affe
#	----------

import re

conditionHex = "^(0x|0X)?([A-Fa-f0-9]+)(H|h)?$"
buffer = input("enter a hexadecimal expression any length: ")

if re.match(conditionHex, buffer):
	print(f'Your input is hexadecimal. Trying to convert it to decimal, octal and binary... Just for fun. :)')

	try:
		#	In python this preinitialization isn't necessary,
		#	however, it may be a good guideline for your
		#	processing.
		newHex = ""

		#	disposing h or H at the end, if existing, because it will
		#	cause an error on converting
		if buffer.endswith('H') or buffer.endswith('h'):
			newHex = buffer[:-1]
		else:
			newHex = buffer
		#end if
		
		print(f'decimal form: {int(newHex, 16)}, octal form: {oct(int(newHex, 16))}, binary form: {bin(int(newHex, 16))}')
	except Exception as e:
		print(f'error: {e.args}')
	#end try
else:
	print('Sorry, but this is not a hexadecimal expression.')
#end if