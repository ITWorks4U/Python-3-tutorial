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

a = 10

print("---	single steps	---")

#	start from 0 to a-1 --> [0,1,2,3,...,9]
for i in range(a):
	print(i)
# end for

print("---	starting from a certain position	---")

#	start from 5 to a-1 --> [5,6,7,8,9]
for i in range(5, a):
	print(i)
#end for

print("---	modifying step range	---")

#	start from 0 to a-1, but take 2 steps instead --> [0,2,4,6,8]
for i in range(0, a, 2):
	print(i)
#end for

print("---	ignoring counter value	---")

#	using _ if you don't need an element
for _ in range(a):
	print("...")
# end for

print("---	compressed in one line	---")

#	press everything into one line
[print(i) for i in range(a)]

print("---	using a collection ('for each')	---")

#	...like a tuple
for i in (3,6,9,12,15,18):
	print(i)
# end for

print("---	enumerating	---")

#	using enumerate to handle with two variables
#	to reveal on which position is which element
for pos,val in enumerate((3,6,9,12,15,18)):
	print(pos, ":", val)
# end for