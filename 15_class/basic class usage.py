#!/usr/bin/python3

"""
	A class is a data structure which
	holds anything what you want.

	It comes with a constructor, destructor
	by default, may contain methods (= functions)
	and anything else.

	To accessing to the class object, it must
	be created before.

	It's not required to define attributes at the
	beginning of the class, these can also be
	defined somewhere in a method, but causes
	a worse reading.
"""

#	definition of a class
class Simple:
	#	define a class attribute
	#	(which is public by default)
	myOwnObject = None
#end class

#	creating an object of class Simple
s = Simple()
print(s.myOwnObject)
del s

#	since s is deleted, there's no
#	possible to access to the object
#	by using s
# print(s.myOwnObject)

#	it's also possible to call
#	that object directly;
#	looks similar to a static object
#	and there's no difference in Python
print(Simple.myOwnObject)