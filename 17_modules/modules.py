#!/usr/bin/python

"""
	How to use modules.

	Modules (other python scripts) offers you
	to access to functions, classes, etc.

	There're 4 different ways to use a module:
	#1	import >module 0, module 1, ..., module n-1<
	#2	import >module 0, ..., module n-1< as >alias<
	#3	from >module n< import >part k< as >alias<, part p as >alias<, ... 
	#4	from >module n< import *

	Attention: By default, the python interpreter
	looks in the current dictionary, where >>this<<
	module could be. If existing, it will be imported
	instead a system module, which has the identical name.

	If you've written your own string class and named
	that to "string.py", then the import below might fail,
	if the required functions, classes, etc. to import
	were not found. => #3
"""

#	---------------
#	1:	importing everything from a module
#		it also allows to import multiple modules
#	---------------
import os, platform
print(f"You're running this script on this location: {os.getcwd()}.")
print(f"Your system: {platform.system()}, release: {platform.release()}, version: {platform.version()}")

print("---------------")

#	---------------
#	2:	using an alias
#	unlike to write randmom.random()
#	you're able to write r.random()
#	---------------
import random as r
pool = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!"§$%&/()=?_:;#'

#	create a random string by using an amount of characters (n)
def randomString(n: int):
	return ''.join(r.choices(pool, k = n))
#end function

for c in (1,2,4,8,16,32,64,128,256):
	print(f'using {c} character(s) for: {randomString(c)}')
#end for

print("---------------")

#	---------------
#	3	importing sub classes, certain functions,
#		or else by using from command
#
#		using lowercase of the alphabet from string class
#	---------------
from string import ascii_lowercase as al
print(f'using al: length: {len(al)}, to upper: {al.upper()}, is decimal: {al.isdecimal()}')

print("---------------")

#	---------------
#	4	importing everything like 1, but by using
#		an asterisks symbol
#	---------------
from string import *

#
#	...have some fun here
#

print("---------------")

#	---------------
#	bonus: using customized modules
#	---------------
import custom_module as cm

s0 = cm.Simple()
print(s0.showContentType())

s1 = cm.Simple(123)
print(s1.showContentType())

cm.Meme('b', 'r', 'r', 'r', 'r', 'r')

print(f'What is the meaning of life? {cm.answerOfEverything}')
print(f'Whis number is the best? {cm.bestNumberOfAllTime} <=> {int(cm.bestNumberOfAllTime)}')