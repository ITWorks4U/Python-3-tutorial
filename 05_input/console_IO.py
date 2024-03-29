#!/usr/bin/python3

"""
	Reading from keyboard, storing that
	content to a variable, etc.

	Every input is always a string (word), so
	it will cause an error on runtime if you're
	trying to use a different usage, e. g. interpreting
	this input as a number, even it's not a number.

	video tutorial:	https://youtu.be/AK44C_uZ9u4
	timestamp:		00:58:59
"""

#	-------------------
#	enter anything, which is going
#	to convert to a string by default
#	-------------------
buffer = input("enter anything: ")
print(f'Your input: {buffer}, its a type of "{type(buffer)}", and it has a length of {len(buffer)} characters.')

#	-------------------
#	interpreting the input
#	as an integer => make
#	sure, this is possible
#
#	in some later sections, you'll
#	learn some mechanics to
#	handle such kind of errors
#	-------------------
print("-------------------")
buffer = input("give me a number: ")
print(f'Your input: {buffer}, its a type of "{type(buffer)}", and it has a length of {len(buffer)} characters.')

#	try to convert this input to an integer, IF possible
buffer = int(buffer)
print(f"after successfully converting your input ({buffer}) has now this type: {type(buffer)}")

print("-------------------")
#	-------------------
#	fun fact: every decimal number with
#	leading zeros won't use the leading zeros
#	unless you're using that format: 0xd
#	leading with zeros x times ->
#	x := number of zeros to use
#	-------------------

number = 00000
print("default number: ", number)
print("formatted version #1: %05d" % number)
print("formatted version #2: {0:05d}".format(number))
print(f"formatted version #3: {number:05d}")

#	have a space of x chars before the output starts
print("Don't be confused with that form: {0:5d}".format(number))

print("-------------------")
#	-------------------
#	entering two "numbers" and calculating
#	the product of them
#	-------------------
buffer = input("give me two numbers: ")

"""
	split() splits the input into a list
	of n elements depending on the required
	token

	in contrast to other languages it's not
	possible to use multiple tokens (yet)

	regular expressions are often used
	for multiple tokens

	in that case we're using each comma
	as a token
"""
buffer = buffer.split(",")
a = int(buffer[0])
b = int(buffer[1])
print("product of a*b is ", (a*b))

#	-------------------
#	... or use the short version:
#	-------------------
a,b = [int(i) for i in input("give me two numbers: ").split(",")]
print("product of a*b is ", (a*b))