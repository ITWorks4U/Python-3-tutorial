###
#	wrong usage of parameter
###

'''
	The idea: function may have an argument of type list.
	If given, then the argument can easily be used. If not,
	then arg becomes to a list.

	However, this instruction is logically wrong, because
	on each function call the Python interpreter looks into
	the internal list. If arg already exists, then no new list
	is going to create.
'''
def function(arg = list()) -> None:
	arg.append('abc')
	return arg
#end function

'''
	Since arg of expected type list is None by default
	on each function call, since arg hasn't been set by calling,
	is going to use as a new list.
'''
def function(arg: list = None) -> None:
	if arg is None:
		arg = list()
	#end if

	arg.append('abc')
	return arg
#end function

collection = list()

for _ in range(10):
	tmp = function()
	print(tmp)
#end for
