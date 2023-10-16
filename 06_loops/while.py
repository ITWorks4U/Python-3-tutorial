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

	video tutorial:	https://youtu.be/AK44C_uZ9u4
	timestamp:		01:08:44
"""

a = 0

print("---	incrementation	---")
while a < 10:
	print(a)

	#	make sure to modify a, otherwise
	#	this loop never ends
	a = a + 1
#end while

print("---	decrementation	---")
while a > 0:
	a -= 1
	print(a)
#end while

#	you also can add brackets for your condition(s)
while (a != 0):
	pass
#end while

#	in Python a do-while-loop doesn't exist