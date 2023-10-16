#!/usr/bin/python3

"""
	None is an object like int, float,
	list, ... and represents nothing.

	It's similar to NULL/nullptr in C/C++,
	null in Java, C#.

	None isn't the same like false, 0 or an
	empty string. It's an unique data type to
	define an undefined state of an object.

	video tutorial:	https://youtu.be/AK44C_uZ9u4
	timestamp:		02:40:05
"""

#	-------------
#	How to understand the
#	datatype none in Python.
#	-------------
undefined = None
print("You will see this:", undefined)
print("-------------")

stringObject = "Test string"

#	-------------
#	What will happen?
#	Do we receive an error?
#	-------------
print(f"Are these both objects equal? {undefined.__eq__(stringObject)}")
print(f"Are these both objects equal? {stringObject == undefined}")
print(f"Are these both objects equal? {stringObject is undefined}")
print("-------------")

#	-------------
#	define None
#	for functions
#	-------------
def nonsenseFunction():
	pass
# end function

for i in range(10):
	print(f'{i}: {nonsenseFunction()}')
#end for
print("-------------")

#	-------------
#	returning any type depending
#	on value
#
#	any integer. bool -> float
#	list -> tuple
#	dictionary, tuple -> None
#	default -> False
#	-------------
def receiveAnyValue(value: int):
	if value == 1 or value == 2 or value == 3:
		return float(value)
	elif value == []:
		return tuple(value)
	elif value == {} or value == ():
		return None
	#end if

	return False
# end function

collection = (1,2,3,[],{},(),True,"ABC")

for c in collection:
	print(f'c = {type(c)} <=> {type(receiveAnyValue(c))}')
#end for