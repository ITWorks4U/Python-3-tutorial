#!/usr/bin/python3

#	-----------
#	handling module errors
#	-----------

try:
	from module import Brrrr
except ImportError as ie:
	print(f'expected module could not be imported: {ie.args}')
#end try-catch

#	-----------
#	handling missing
#	classes
#	-----------

#	normal processing here
from module import Simple

try:
	s = Simple()
	print(s.showContentType())

	t = Simple("123")
	print(t.showContentType())

	#	-----------
	#	caused a NameError, because "Bruh" is unknown
	#	-----------
	b = Bruh()
except NameError as ne:
	print("found that error: %s" % ne.args)
#end try-except