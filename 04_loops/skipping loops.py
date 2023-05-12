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

a = 0

print("---	skipping a value	---")
while a < 10:
	a = a + 1

	#	skipping the loop, if a certain
	#	condition is true
	if a == 5 or a == 9:
		continue
	#end if

	print(a)
#end while

print("---	leaving the loop too early	---")
while a > 0:
	a -= 1
	print(a)

	#	leaving the loop, if a certain
	#	condition is true
	if a == 3:
		break
	#end if
#end while