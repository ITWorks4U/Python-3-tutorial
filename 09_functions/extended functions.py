#!/usr/bin/python3

"""
	In Python it's also possible to
	add arbitrary arguments. It's usage
	might be a bit uncommon.

	Don't be confused with * and you're
	also knows C/C++. These aren't pointers
	in python.
"""

#	--------------
#	calling a function with
#	any amount of arguments
#	--------------

'''
	Arbitrary arguments allows us to call a function
	with a different number of arguments.
	These are often shortened to *args in Python documentations.
'''
def arbitraryArguments(*args):
	print("Number of arguments: ", len(args))

	for i in args:
		print("argument:", i)
	# end for
# end function

arbitraryArguments(1,2,3,'True',{},(),[],'Hi there!')
arbitraryArguments(123)
arbitraryArguments()

print("--------------")

#	--------------
#	calling a function with
#	a key-value-pair of
#	arguments
#	--------------

'''
	Arbitrary keyword arguments are in use to
	handle with a dictionary. These are often
	shorened to *kwargs in Python documentations.
'''
def arbitraryKeywordArguments(**kwargs):
	for key in kwargs.keys():
		print(f'key: {key}, value: {kwargs[key]}')
	# end for
# end function

arbitraryKeywordArguments(user = "ITWorks4U", location = "YouTube", source = "https://github.com/ITWorks4U")

#	--------------
#	converting a list into
#	a dictionary and calling
#	the function to see
#	the result
#	--------------

aSimpleList = [1, 2, 3, "A", "B", "C", False, 7, 5]
aNewDictionary = dict()

for i in range(0, len(aSimpleList)):
	aNewDictionary.update({str(i) : aSimpleList[i]})
# end for

#	important: aNewDictionary must start with two stars
arbitraryKeywordArguments(**aNewDictionary)

print("--------------")

#	--------------
#	a function also may
#	comes with a dynamic
#	number of arguments
#
#	see: print() function
#	--------------

def dynamicFunction(defVal = "My own defined value!"):
	print(defVal)
# end function

dynamicFunction(123)
dynamicFunction("ABC")
dynamicFunction()

print("--------------")

#	--------------
#	adding a+b+c, where b and c
#	have default values by default
#
#	hint: if you want to make sure, that
#	'a' shall be an integer on function call,
#	then write: a: int
#
#	for the interpreter a might still be any
#	type, however, it helps you to read
#	the parameter(s) correctly
#
#	since default arguments are in use it's not
#	allowed to add another arguments without
#	a default value
#	--------------
def add(a: int, b = -10, c = 500):
	return a + b + c
#end function

print(add(999))
print(add(100,c=-147,b=158))

print("--------------")

#	--------------
#	returning more than 1 object
#	--------------
def swag():
	return list(), dict(), tuple(), "123", 42
#end function

collection=swag()
print(collection)