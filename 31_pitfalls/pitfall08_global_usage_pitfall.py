###
#	not know the difference between local and global objects
###

'''
	In contrast to other programming languages, where global objects / variables can
	easily be used in functions, Python only allows you to read the object.

	If you want to modify the "global" object, you have to mark that with
	>>global<<.

	Hint: Don't use global in your application unless you have to do this.
'''

data = 'Hello'

def caller() -> None:
	global data
	data += ' World!'

	print(data)
#end function

caller()