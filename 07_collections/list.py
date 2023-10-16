#!/usr/bin/python3

"""
	A list is a dynamically collection,
	which holds any type. It can easily
	being used to iterate trough the
	collection, adding new elements,
	removing elements, etc.

	Don't be confused from other languages,
	because there a [] is an array, whereas
	a list has a specific definition.

	video tutorial:	https://youtu.be/AK44C_uZ9u4
	timestamp:		01:30:24
"""

#	create a list with n elements
aSimpleList = [1, 2, 3, "A", "B", "C", True, False, 7, 5, 3]

#	let create an empty list (easier to read that)
anEmptyList = list()

#	this can also be used (harder to read that correctly)
anotherList = []

#	can be used, but this is also much harder to
#	read that in a correct form, thus avoid this one
#list = list()

#	---------------
#	accessing
#	---------------
print(aSimpleList)															#	print the whole list

for element in aSimpleList:													#	using a loop
	print(element)
# end for

print(aSimpleList[3])														#	get element on position n (n = 0, 1, 2, ..., k-1)
print(aSimpleList[4:9])														#	print an interval between [n,k], WHERE n is the position and k is the current element to use
print(aSimpleList[-2])														#	start backwards from the list

#	---------------
#	modifiying
#	---------------
aSimpleList.append(True)													#	appending an element to the end of the list
aSimpleList.insert(5, None)													#	insert a new element on position n
aSimpleList.extend([951,"ABC"])												#	add a sub list
aSimpleList += [True, False, None]											#	same as above

aSimpleList.remove(None)													#	remove an element, which must be in the list
print(aSimpleList.pop())													#	remove the last element, which can be used for other stuff
print(aSimpleList.pop(6))													#	remove element on position n, which can be used for other stuff
#aSimpleList -= [7,5,3]														#	not available for a list

print(aSimpleList)