#!/usr/bin/python3

"""
	Let python create a random generated password
	for you.

	video tutorial:	https://youtu.be/AK44C_uZ9u4
	timestamp:		02:47:07
"""

import random as r

#	contains alphanumeric characters in capital and normal form, followed
#	by numbers and some bonus characters
characterCollection = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuwvxyz0123456789!"§$%&/()=?_:;-.,+*#`´µ<>|@~'
lengths = (5,10,20,50,100)

def createRandomPassword(length: int) -> None:
	#	since a string is immutable, we're unable to modify
	#	a temporary string directly; we're using a list
	#	as a buffer instead
	holder = list()

	for _ in range(length):
		holder.append(r.choice(characterCollection))
	#end for

	#	converting the list into a string
	randomPassword = "".join(holder)
	print(f'your random created password with a length of {len(randomPassword)} characters: {randomPassword}')
#end for

#	running...
for l in lengths:
	createRandomPassword(l)
#end for