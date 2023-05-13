#!/usr/bin/python3

"""
	Inheritance allows you to extend
	a class with new functionalities.
"""
#	basic class
class Simple:
	def myObject(self):
		return "base"
	#end method
#end class

#	-------------
#	extended class for Simple
#	-------------
class Derived(Simple):
	def myObject(self):
		return 123
	#end method

	'''
		returning the value from
		the super class instead
	'''
	def superObject(self):
		return super().myObject()
	#end method
#end class

#	-------------
#	usages
#	-------------
s = Simple()
print(f'{s.myObject()} <=> {type(s.myObject())}')

print("-------------")

d = Derived()
print(f'{d.myObject()} <=> {type(d.myObject())}')
print(f'{d.superObject()} <=> {type(d.superObject())}')