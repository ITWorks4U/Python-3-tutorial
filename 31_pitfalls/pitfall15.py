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
	if False and e == IndexError:													#	won't work => index of 'e' is never equal to a class
		print(f'e == IndexError			=> {e.args}')
	elif False and e is IndexError:													#	since 'e' >>IS<< not an IndexError this won't work for you
		print(f'e is IndexError			=> {e.args}')
	elif False and e.__eq__(IndexError):											#	can be used, but this is deprecated and may have
		print(f'e.__eq__(IndexError)	=> {e.args}')								#	side effects (depending on which Python version you're working on)
	elif False and e.equals(IndexError):											#	won't work, because equals is not a method for an exception
		print(f'e.equals(IndexError)	=> {e.args}')
	elif False and type(e) == IndexError():											#	won't work => type of e (general exception) is unequal to
		print(f'type(e) == IndexError	=>	{e.args}')								#	an IndexError
	elif False and type(e) == type(IndexError):										#	nice try, but it doesn't also work
		print(f'type(e) == type(IndexError)	=>	{e.args}')
	elif isinstance(e, IndexError):													#	this is what you really need
		print(f'isinstace()... {e.args}')
	else:
		print(f'any exception: {type(e)} => {e.args}')
	#end if
#end try
