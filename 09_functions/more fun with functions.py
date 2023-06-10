#!/usr/bin/python3

"""
	have some other fun with functions :o) 
"""

#	--------------
#	Who says, that a function has to
#	return a single value only?
#	--------------
def swag():
	return list(), dict(), tuple(), "123", 42, "Deal with it!"
#end function

for s in swag():
	print(s)
#end for

#	--------------
#	...no comment...
#	--------------
def meme(a, b, c, d, e, f) -> None:
	print(f'This function is going to {a}{b}{c}{d}{e}{f}.')
#end function

b = 'b'
r = 'r'
meme(b,r,r,r,r,r)