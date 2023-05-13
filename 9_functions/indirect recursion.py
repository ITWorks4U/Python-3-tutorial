#!/usr/bin/python3

'''
	Recursions are the preversion of
	loops and allows you to repeat
	any instruction(s) until
	a certain condition is true
	to leave that recursive function.

	Make sure to have an exit point,
	otherwise the application crashes.

	'direct recursion' means: this
	function calls itself n times

	'indirect recursion' means:
	a function calls another function,
	where that function calls the
	previous function

	Recursion functions are often used
	in math and writing less code
	to receive the result very quickly.
'''

"""
	func1(a)

	if a is 0, then leave the recursion of doom
	otherwise call func2(a)

	func2(a)

	if a is even, divide a by 2
	otherwise multiply a with 3 and add 1

	call func1(a)
"""

def func1(a):
	if a == 1:
		return 0
	#end if

	return func2(a)
#end function

def func2(a):
	if a % 2 == 0:
		a /= 2
	else:
		a = 3 * a + 1
	#end if

	print(f'{a:0.0f}', end=' => ')

	return func1(a)
#end function

#	--------------
#	testing...
#	--------------
number=73
print(f'func({number}) = {func1(number)}')