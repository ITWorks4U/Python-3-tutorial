#!/usr/bin/python3

#	using Food enumeration only
from classes import Food

"""
	Using a main function in python.

	Like in other programming languages
	the main() represents the
	starting section, however, in Python
	there's no main by default required
	or given.

	In this example, this python script
	offers functions only.

	video tutorial:	https://youtu.be/AK44C_uZ9u4
	timestamp:		02:57:37
"""
#	-----------
#	simple functions
#	-----------
def Function():
	print("This is a simple function call.")
#end function

def F():
	pass
#end function

def Goes(a,b,c,d,e):
	print(f'This function goes "{a}{b}{c}{d}{e}"!')
#end function

def printFood(f: Food):
	print(f'{f}')
#end function

#	any other functions here