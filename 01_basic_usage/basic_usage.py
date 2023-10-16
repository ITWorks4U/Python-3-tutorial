#!/usr/bin/python3																				#	shebang command

'''
	Python 3 is really easy to learn. It allows you to start
	with programming without any knowledge.
	
	Python is an interpreter language, means, you don't have
	to do any datatype definitions. Every variable, here an object,
	can easy be defined and also reinterpreted by any other value.
	
	However, there are >some< points to know:
	-	by using blocks, see conditions, loops, functions, ... it's required
		to know, which command/s is/are part of the block
	-	in contrast to any other language, it's neccessary to know
		which kind of indention you're using; there're two of them:
			-	using space bar(s)
			-	using tab(s)

		because Python won't agree a mix of both, you must use one of them
		hint: you also can display whitespace(s) and tab(s)
		(any editor): view -> display whitespaces (or similar expression)

	Now, have fun with Python 3!

	video tutorial:	https://youtu.be/AK44C_uZ9u4
	timestamp:		00:01:47
'''

#	simple print command
#	everything is a word on output or by reading from keyboard / file
print("Hello World!")
print("1, 2, 3")

#	declaring an integer (in Python 3 any integer is a long type without a limitation)
number = 123
print(number)

#	now it's a float type (redefinition of number)
number = 123.456789
print(number)

#	convert it to a word
number = str(number)
print(number)

#--------------------------

'''
	Python comes with a dynamic interpretation of types,
	however, it also contains data types for a
	special purpose
	
	with type(a_given_type) you can get the type
'''

print(type(10))																					#	integer
print(type(12345.6789))																			#	float (Python won't comes with a double type)
print(type("ABC"))																				#	string
print(type(True))																				#	boolean
print(type(None))																				#	similar to NULL in C/C++
print(type([1,2,3]))																			#	list
print(type({1,2,3}))																			#	set
print(type({1:'A', 2:'B', 3:'C'}))																#	dictionary
print(type((1,2,3)))																			#	tuple