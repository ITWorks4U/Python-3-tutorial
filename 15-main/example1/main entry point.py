#!/usr/bin/python3

"""
	A main represents the main entry point for
	our application.

	In contrast to higher programming languages,
	like C, C++, Java, C#, ...
	python doesn't need a main entry point.

	However, with a main, you can control
	your progam sequence much better.

	video tutorial:	https://youtu.be/AK44C_uZ9u4
	timestamp:		02:57:37
"""

#	Since you're using a main function, this is NOT
#	the main entry point for python. It's "just"
#	a normal function.
def main():
	print('This is our "main" function.')

	#...
#end "main"

#	that's the real main entry point:
if __name__ == '__main__':
	#	this code might be a bit uncommon,
	#	but it's often in use for larger projects
	#
	#	the __main__ is a system command, which checks,
	#	if >>this<< python script has been launched by
	#	the python interpreter to identify this as
	#	the main script
	#
	#	for more details look to example2
	
	#	normal function call
	main()
#end "real main"