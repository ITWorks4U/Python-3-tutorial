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

	Since a constructor is defined, it
	overrides a previously defined
	constructor.

	A constructor and also destructor doesn't
	comes with a return value and like in other
	OOP languages these are typeless.
'''

class Simple:
	"""
		Default constructor. If not given
		and no other constructor is defined,
		this is used automatically => basic class usage.py
	"""
	#	constructor
	def __init__(self) -> None:
		self.classObject = None
		print("Basic constructor.")
	#end constructor

	"""
		Extended constructor. Comes with
		an argument. By default this argument
		is defined as a tuple.

		Since this constructor is defined,
		it overrides the default constructor.
	"""
	def __init__(self, arg = tuple()) -> None:
		self.classObject = arg
		print("Extended constructor #1")
	#end extended constructor #1

	"""
		Extended constructor.
		Since this constructor is defined,
		an instance of this class can only
		be done, if two arguments are given.
	
	def __init__(self, a: int, b: int) -> None:
		self.classObject = list(a+b)
		print("Extended constructor #2")
	#end extended constructor #2
	"""

	"""
		Destructor (in other languages: Finalizer).
		By default it's called everytime,
		when this class object is no longer in use
		or deleted by yourself.

		Can be defined by yourself to do
		some cleanup options.

		Be careful: If any exception may appear during
		destructing, this >>could<< be able caught, but also
		causes undefined behaviors on runtime!
	"""
	def __del__(self):
		print("Destructor is called.")
	#end destructor
#end class

#	--------------
#	create an instance
#	of the class
#	--------------
s = Simple()
print(f's = {type(s)}, classObject = {type(s.classObject)}')

#	--------------
#	create an instance
#	of the class, too
#
#	works only, if code
#	above is either commented out
#	or fixed, and the second constructor
# 	is available, otherwise this error is printed on console:
#
#	Traceback (most recent call last):
#		File "constructor destructor.py", line 83, in <module>
#			s = Simple()
#	TypeError: __init__() missing 2 required positional arguments: 'a' and 'b'
#	--------------
# t = Simple(100,200)
# print(f's = {type(t)}, classObject = {type(t.classObject)}')