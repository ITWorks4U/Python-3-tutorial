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

	video tutorial:	https://youtu.be/AK44C_uZ9u4
	timestamp:		02:02:16
'''

"""
	calculating the fibonacci series
	attention: if you have ENOUGH time in your life, or if you
	want to see the death of the sun,
	then you also >could< try to use a value of 50 or higher :o)

	Fn = Fn-1 + Fn-2
	F0 = 0 and F1 = 1
"""

def fibonacci(a):
	if a == 0:
		return 0
	#end if

	if a == 1 or a == 2:
		return 1
	#end if

	return fibonacci(a-1) + fibonacci(a-2)
#end function


#	print function can also be used with special formatting
for i in range(30):
	print("F(%d) = %d" % (i, fibonacci(i)))
#end for