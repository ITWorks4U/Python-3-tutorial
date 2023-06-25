#!/usr/bin/python3

"""
	Regular expressions are a well tool
	to check a certain expression.

	For more details, take a look to this video:
	https://www.youtube.com/watch?v=vvFPWHHto00

	(German commentary, English text)

	Checking, if a given email-address may
	be valid or not.
"""

import re

"""
	filtering any email-address by using these conditions:
	-	starting with any expression of small letters,
		at least one and up to 10 characters
	-	followed by @
	-	using a fixed provider name, like:
		gmail, gmx or hotmail, ...
	-	followed by a dot
	-	ends with com, info or de
"""
filter = "^[a-z]{1,10}@(gmail|gmx|hotmail)\.(com|info|de)$"

"""
	the whole expression (buffer) must pass trough the filter, where

	re.match:
		-	starts from left only
	re.search:
		-	looking anywhere in the buffer,
			if the filter can be spotted there
	
	returns a Match[str] object, which 
"""
buffer = input('verify your email-address: ')
if re.match(filter, buffer):
	print('email-address is verified')
else:
	print('email-address has not the expected format')
#end if