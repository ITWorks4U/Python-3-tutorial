#!/usr/bin/python3

'''
	Methods are functions, which
	are available only in the certain class.

	Constructors and destructor are also
	"functions", however, these are special.

	Every (special) function must have at
	least one argument -> self, otherwise
	it's a syntax error. >>self<< is not
	required, you can use any expression
'''

class Simple:
	def __init__(blah, arg = None) -> None:
		print("Instance created.")
		blah.object = arg
	#end constructor

	'''
		Optional. Since no operations are
		required during destructing, this
		destructor can be removed.
	'''
	def __del__(blah) -> None:
		print("Instance destroyed.")
	#end destructor

	'''
		Returning instance object.
	'''
	def thisObject(blah):
		return blah.object
	#end method
#end class

#	prints the same output
s = Simple()
print(f'{s.object} <=> {type(s.object)}')
print(f'{s.thisObject()} <=> {type(s.thisObject())}')

#	does NOT print the identical output like above
#	the first one prints the address location of the
#	instance, the second one prints, that s.thisObject
#	is a method
print(f'{s.thisObject} <=> {type(s.thisObject)}')
del s

print("-------------")

#	-------------
#	other usages of Simple class
#	-------------
s = Simple(int)
print(f'{s.object} <=> {type(s.object)}')
del s

print("-------------")

s = Simple(float)
print(f'{s.object} <=> {type(s.object)}')
del s

print("-------------")

s = Simple(dict())
print(f'{s.object} <=> {type(s.object)}')
del s