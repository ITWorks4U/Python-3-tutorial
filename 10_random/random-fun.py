#!/usr/bin/python3

'''
	Have some fun with random numbers?
	Here you'll have it.

	To be able to use a random number,
	we have to import a module, which
	allows us to work with random operations.

	Attention: If you're using a module, which
	has the exactly name of one of your files,
	then it might crash on runtime. In that case
	this file was named with "random-fun.py"
	instead of "random.py".

	video tutorial:	https://youtu.be/AK44C_uZ9u4
	timestamp:		02:28:52
'''

#	required module to work with
#	mostly a module may have an alias
#	to work with the alias instead
import random as r

#	prints a random number between [0, 1)
print(r.random())

#	using a fixed collection to select a
#	random number from it...
collection = (0,1,2,3,4,5,6,7,8,9)
print(r.choice(collection))

#	...or combine this with a loop
#	and a switch statement (:
for i in range(10):
	colorID = r.choice(collection)

	#	up to python version 9
	cs = {
		0: 'zero',
		1: 'one',
		2: 'two',
		3: 'three',
		4: 'four',
		5: 'five',
		6: 'six',
		7: 'seven',
		8: 'eight',
		9: 'nine'
	}

	print(cs.get(colorID, 'unknown number'))

	#	for python version 10+
	match colorID:
		case 0:
			print('zero')
		case 1:
			print('one')
		case 2:
			print('two')
		case 3:
			print('three')
		case 4:
			print('four')
		case 5:
			print('five')
		case 6:
			print('six')
		case 7:
			print('seven')
		case 8:
			print('eight')
		case 9:
			print('nine')
		case _:
			print('unknown number')
		#end case
	#end match
#end for