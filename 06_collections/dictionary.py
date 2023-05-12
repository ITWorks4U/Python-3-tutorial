#!/usr/bin/python3

"""
	A dictionary is a dynamic collection
	of a key and value pair for any type.

	It can easily being used to iterate
	trough the collection, adding new elements,
	removing elements, etc.
"""

#	define a dictionary
aSimpleDictionary = {
	'red' : 0xFF0000,
	'yellow' : 0xFFFF00,
	'green' : 0xFF00,
	'blue' : 0xFF
}

#	define an empty dictionary
anEmptyDictionary = dict()
alsoAnEmptyDictionary = {}

#	---------------
#	accessing
#	---------------
print(aSimpleDictionary)											#	print the whole dictionary

for key in aSimpleDictionary.keys():								#	using a loop
	print(hex(aSimpleDictionary[key]))
#end for

print("---------------")
#	---------------
#	modifiying
#	---------------
aSimpleDictionary.update({'white' : 0xFFFFFF, 'black' : 0})			#	add new elements to the dictionary
_ = aSimpleDictionary.pop('yellow')									#	removing an element somewhere in the dictionary by given key
_ = aSimpleDictionary.popitem()										#	removing the last element from the dictionary

print(aSimpleDictionary)
print("---------------")

#	---------------
#	have fun with dictionaries
#	---------------
print("all keys: {0}", aSimpleDictionary.keys())					#	get the keys
print("all values: {0}", aSimpleDictionary.values())				#	get the values
print("print me all: {0}", aSimpleDictionary.items())				#	print each element from the dictionary as a list of tuples

print("---------------")
#	---------------
#	*****	converting a list to a dictionary	*****
#	---------------
aSimpleList = [1, 2, 3, "A", "B", "C", False, 7, 5]					#	first way to convert a list to a dictionary
iterator = iter(aSimpleList)
aNewDictionary = dict(zip(iterator, iterator))
print(aNewDictionary)

aNewDictionary.clear()												#	removing all elements

for i in range(0, len(aSimpleList)):								#	second way to convert a list to a dictionary
	aNewDictionary.update({i : aSimpleList[i]})
# end for

print(aNewDictionary)