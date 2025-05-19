###
#	sub conditioning for exceptions
###

'''
	What kind of way(s) do you know how to separate a sub or specific exception?
	Consider this simple sample:

	By trying to attept an element on position 4 (the 5th element) of four elements
	only, an IndexError occurs. Quite easy. But which kind of sub exception test
	reveals the correct way?
'''

collection = [0,1,2,3]

try:
	_ = collection[4]

except Exception as e:
	#	won't work => index of 'e' is never equal to a class
	if False and e == IndexError:
		print(f'e == IndexError			=> {e.args}')

	#	since 'e' >>IS<< not an IndexError this won't work for you
	elif False and e is IndexError:
		print(f'e is IndexError			=> {e.args}')

	#	can be used, but this is deprecated and may have
	#	side effects (depending on which Python version you're working on)
	elif False and e.__eq__(IndexError):
		print(f'e.__eq__(IndexError)	=> {e.args}')

	#	won't work, because "equals" is not a method for an exception
	#	__eq__ won't also work
	elif False and e.equals(IndexError):
		print(f'e.equals(IndexError)	=> {e.args}')

	#	won't work => type of e (general exception) is unequal to
	#	an IndexError
	elif False and type(e) == IndexError():
		print(f'type(e) == IndexError	=>	{e.args}')

	#	nice try, but it doesn't also work
	elif False and type(e) == type(IndexError):
		print(f'type(e) == type(IndexError)	=>	{e.args}')

	#	this is what you really need
	elif isinstance(e, IndexError):
		print(f'isinstace()... {e.args}')

	#	any other exception (case) here
	else:
		print(f'any exception: {type(e)} => {e.args}')
	#end if

	#NOTE:
	#	Don't try to use a match pattern to determine
	#	which sub exception could be the correct one.

	#	Irrefutable pattern is allowed only for the last case statement
	# match e:
	# 	case IndexError:
	# 		print("That's an index error.")
	# 	case ValueError:
	# 		pass
	# 	case _:
	# 		pass
		#end cases
	#end match
#end try
