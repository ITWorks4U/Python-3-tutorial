#!/usr/bin/python3

"""
	condition checks allows you to compare
	one, two or more values to each other

	everytime a condition check returns true
	a certain block of code(s) is able
	to execute

	video tutorial:	https://youtu.be/AK44C_uZ9u4
	timestamp:		00:30:24
"""

#	let's have two values
a = 10
b = 20

'''
	VERY IMPORTANT:
		- condition checks (also for loops, functions and classes)
		  must have an indentation (white space OR tabs only)

		- do NOT merge your python code with both intendentions,
		  it's a syntax error (it seems since Python 3.10+ it's now allowed,
		  but not tested)

		- be careful, which code is a part of a condition check (also
		  for a loop, a function or a class); means: every code, which has
		  the same indentation like the last code above, is automatically
		  a part of this condition, loop, etc.

		- every special block of code (condition, loop, etc.) must have
		  at least a code; it's a syntax error, if this field is empty;
		  even a commentary as a dummy holder is also not valid;
		  if an implementation is in further use, then use the keyword: pass
		  or use a muliline commentary block

		- if you're not sure about the indentations in your code, then you
		  can activate the white spaces, depending on the editor you're using

		- hint: it's not required, but for a better design and reading, mark
		  your indentation at the end with an commentary, like: #end if, #end for or else
'''

if a == b:														#	checks, if a is equal to b => false
	print("a is equal to b")									#	then this text shall be printed
# end if														#	optional -> helps you to have an overview

if a != b:														#	checks, if a is unequal to b => true
	print("a is not equal to b")								#	this prints to the console
# end if

if a != b:
	#	using pass to skip the current block
	#	for later purpose
	pass
# end if

"""
	an else block defines the default way, if the
	condition(s) above is/are false
"""
if a == b:
	print("both values are equal")
else:
	print("both values are not equal")
# end if