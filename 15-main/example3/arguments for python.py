#!/usr/bin/python3

"""
	Arguments for your script / application are
	often in use to control a specific sequence,
	e. g. --help for printing a help, -v for verbose,
	...

	Remember: Each argument IS A WORD!

	If your given arguments shall be handled as an another
	type, then make sure that this is able to do.

	You could do that by separating each argument, which
	is a high amount of wasted time, or you could use
	regular expressions or else.

	video tutorial:	https://youtu.be/AK44C_uZ9u4
	timestamp:		02:57:37
"""

#	contains functions and objects
#	to work with arguments
import sys

if __name__ == '__main__':

	#	argv := argument vector => contains each argument...
	print(f'arguments passed: {len(sys.argv)}')

	#...including your own python script (similar to C/C++)
	for i,a in enumerate(sys.argv):
		print(f'argument {i}: {a}')
	#end for
#end main