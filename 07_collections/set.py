#!/usr/bin/python3

"""
	A set is a dynamic collection,
	which holds any type. It can easily
	being used to iterate trough the
	collection, adding new elements,
	removing elements, however, it has
	some limitations in contrast to
	a list.

	video tutorial:	https://youtu.be/AK44C_uZ9u4
	timestamp:		01:30:24
"""

#	define a set
aSimpleSet = {1, 2, 3, 7, 5, 3, None, "ABC", "DEF", "XYZ", "ABC"}

#	an empty set
anEmptySet = set()

"""
	Looks like a set, however, this expression doesn't
	define a set, it's a dictionary instead.
"""
notASet = {}
print(type(notASet))

#	---------------
#	accessing
#	---------------
print(aSimpleSet)																	#	prints the whole set

for element in aSimpleSet:															#	using a loop
	print(element)
# end for

#	---------------
#	modifiying
#	---------------
aSimpleSet.add(False)																#	adding a new element to the set, if not already existing
aSimpleSet.pop()																	#	removing the last added element only

aSimpleSet.remove(7)																#	removing a given element, where this element MUST exist
aSimpleSet.discard(False)															#	try to remove a given element, if existing

#	won't work with sets
# print(aSimpleSet[0])

print(aSimpleSet)

#	---------------
#	have some fun with sets
#	---------------
A = {1, 2, 3, False, None}
B = {"A", "B", "C", 1, 2, 3}

print(A.union(B))																	#	A U B
print(A.intersection(B))															#	A ∩ B