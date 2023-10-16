#!/usr/bin/python3

"""
	Working with functions.

	Functions allows you to write
	a code once and call it multiple
	times.

	Like conditions, loops, classes, ...
	functions comes with a block indent
	and every code within this indent area
	is part of the function.

	return type for a function: anything

	- None 				<=>	no return value (similar to void in C, C++, Java, C#, ...)
	- certain type		<=>	type to work with => no error occurs, if the return value is unused
	- multiple types	<=>	you're also welcome to return multiple objects at the same time

	video tutorial:	https://youtu.be/AK44C_uZ9u4
	timestamp:		02:02:16
"""

#	--------------
#	before a function can be called,
#	it must be defined first, otherwise it's
#	an error on runtime (similar to C++)
#	--------------
#aSimpleFunction()

'''
	A simple function without a parameter.
	By default, it returns nothing, which
	is equal to a void function in other
	programming languages.
'''
def aSimpleFunction():						#	definition of a function
	print("I was called!")
# end function

print("--------------")
for i in range(10):
	aSimpleFunction()						#	calling this function 10 times
# end for

#	--------------
#	In C this works, however,
#	in python it won't, because
#	our function requires no arguments
#	--------------
#aSimpleFunction(1,2,3,4)

#	--------------
#	function with a single argument
#	to call -> causes an error, if
#	no argument is given
#	--------------

print("--------------")
'''
	Comes with a single argument only.
	A function in python may have more than
	one different return type.
'''
def aFunctionWithReturnValues(value):
	if value == 0:
		return bool(value)
	# end if

	if value == 1:
		return int(value)
	# end if

	if value == 2:
		return float(value)
	# end if

	if value == 3:
		return str(value)
	# end if

	return None
# end function

for i in range(5):
	retVal = aFunctionWithReturnValues(i)
	print(f"calling function for {i} and I receive that type: {retVal}")
# end for