"""
	Unlike to other proramming / scripting languages
	python strictly differs global and local
	variables / objects.

	Mostly you don't realize that, but sometimes
	this is really important to know when to modify
	a global object in an own section.
"""

######################
#	usually, this is a global object, which
#	can also be used in a function like below...
######################
#	This won't cause an error.
######################
#!/usr/bin/python3
expression = 'global expression'

def surprise() -> None:
	print(f'in function call: {expression}')
#end function

print(f'before function call: {expression}')
surprise()
print(f'after function call: {expression}')
######################

######################
#	...,however, by modifying this object in
#	the function it has a different result
#	depending on when we start to modify...
######################
#	This won't cause an error, too.
######################
#!/usr/bin/python3
expression = 'global expression'

def surprise() -> None:
	expression = 100
	print(f'in function call: {expression}')
#end function

print(f'before function call: {expression}')
surprise()
print(f'after function call: {expression}')
######################

######################
#	...by the way, it's not allowed to
#	accessing a "global" object inside a function
#	and modifying it later...
######################
#	Since this is not marked as a syntax error,
#	it causes an error on runtime! Some IDE's won't
#	detect that!
######################
#!/usr/bin/python3

expression = 'global expression'

def surprise() -> None:

	#	error: we're unable to call expression,
	#	since it's not defined yet
	print(f'in function call #1: {expression}')

	expression = 100
	print(f'in function call #2: {expression}')
#end function

print(f'before function call: {expression}')
surprise()
print(f'after function call: {expression}')
######################

######################
#	...unless you're going to mark the
#	expression with global keyword
######################
#	This won't cause an error.
######################
#!/usr/bin/python3

expression = 'global expression'

def surprise() -> None:
	#	notification for the python interpreter, that
	#	this expression already exists outside
	#	and this shall be able to modify in this
	#	function
	#
	#	after global <object> there's no other instruction here
	global expression

	print(f'in function call #1: {expression}')
	expression = 100
	print(f'in function call #2: {expression}')
#end function

print(f'before function call: {expression}')
surprise()
print(f'after function call: {expression}')
######################

######################
#	When you're using an argument for your
#	function, then this can't be set with
#	the global keyword.
######################
#	This is a syntax error and in an IDE
#	you're able to see that.
######################
#!/usr/bin/python3

collection = ['abc', 123, True, False, None]

def willNotWork(collection: list) -> None:
	#	will not work, because collection
	#	is an argument and this is unable
	#	to use with the global keyword
	global collection

	print(f'collection before modification: {collection}')
	
	collection = [753, '42 is the answer']
	print(f'collection after modification: {collection}')
#end function

print(f'collection before function call: {collection}')
willNotWork(collection)
print(f'collection after modification: {collection}')