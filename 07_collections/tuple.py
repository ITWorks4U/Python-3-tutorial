#!/usr/bin/python3

"""
	A tuple is a static collection,
	which holds any type.
	
	In contrast to a list or set,
	no elements can be added or removed
	after creation.

	video tutorial:	https://youtu.be/AK44C_uZ9u4
	timestamp:		01:30:24
"""

#	define a tuple with fixed elements
aSimpleTuple = (7,5,3, True, False, "Hello World!")

#	define an empty tuple
anEmptyTuple = tuple()

#	same as above, but harder to interpret it correctly
anotherEmptyTuple = ()

#	---------------
#	accessing
#	---------------
print(aSimpleTuple)															#	print the whole tuple

for element in aSimpleTuple:												#	using a loop
	print(element)
# end for

print(aSimpleTuple.count(True))												#	count how often an element exists in our tuple
print(aSimpleTuple.index(True))												#	get the position of an element

#	---------------
#	modifiying
#	---------------
'''
	A tuple is a fixed structure. It won't allows us
	to modify the elements.
'''

#	---------------
#	have some fun with tuples
#	---------------
t = (1,2,3)																	#	define a new tuple
(a, b, c) = t																#	refering a tuple of variables to tuple t

if (a,b,c) == (1,2,3):														#	let compare (a,b,c) with (1,2,3)
	print("Hooray")
# end if