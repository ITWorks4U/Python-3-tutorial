#!/usr/bin/python3

"""
	Python comes with four kinds of loops:
		while, for, "for each", recursion
	
	while:
		while a condition is true, this statement(s) repeats
	
	for:
		sequential iteration from a certain start value
		to its destination value
	
	"for each":
		in python identical to for
		often i use for a list, set
	
	recursion:
		-	it's not really a typical loop, more
			a call of itself
		-	mostly used to calculate very quickly, but be careful
		-	if you don't mind, then your application crashes
"""

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

print("---	F(30) = ...	---")
a = 30

if a < 0:
	print("unable to calculate the fibonacci series")
else:
	retVal = fibonacci(a)
	print(" F(30) = ", retVal)
#end if

print("---	using a loop instead	---")

#	print function can also be used with special formatting
for i in range(a+1):
	print("F(%d) = %d" % (i, fibonacci(i)))
#end for