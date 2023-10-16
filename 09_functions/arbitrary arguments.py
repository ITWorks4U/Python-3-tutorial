#!/usr/bin/python3

"""
	In Python it's also possible to
	add arbitrary arguments. It's usage
	might be a bit uncommon.

	Don't be confused with * and you're
	also knows C/C++. These aren't pointers
	in python.

	video tutorial:	https://youtu.be/AK44C_uZ9u4
	timestamp:		02:02:16
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