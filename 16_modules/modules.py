#!/usr/bin/python

"""
	How to use modules.

	Modules (other python scripts) offers you
	to access to functions, classes etc, which
	are defined elsewhere.

	There're 3 different ways to use a module:
	#1	import >module 0, module 1, ..., module n-1<
	#2	import >module 0, ..., module n-1< as >alias<
	#3	from >module n< import >part k< as >alias<, part p as >alias<, ... 

	Attention: By default, the python interpreter
	looks in the current dictionary, where >>this<<
	script lies, if the imported modules also lies
	there.

	If these are found there, these will be used instead,
	thus if you've written your own string class and named
	that to "string.py", then the import below might fail,
	if the required functions, classes, etc. to import
	were not found. => #3
"""

#	---------------
#	1 (importing more than one module)
#	---------------
import os, platform
print(f"You're running this script on this location: {os.getcwd()}.")
print(f"Your system: {platform.system()}, release: {platform.release()}, version: {platform.version()}")

print("---------------")

#	---------------
#	2 (using random)
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
#	3 (using lowercase of the
# 	alphabet from string class)
#	---------------
from string import ascii_lowercase as al
print(f'using al: length: {len(al)}, to upper: {al.upper()}, is decimal: {al.isdecimal()}')

print("---------------")

#	---------------
#	using customized
#	modules
#	---------------
from custom_module import Simple as si, AnotherClass as ac

s = si()
print(s.showContentType())

a = ac()
print(a)