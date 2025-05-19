###
#	overloading functions / class methods
###

#	usually, you would write function overloading like this one:
def add(a: int, b: int) -> int:
	return a + b
#end function

def add(a: float, b: float) -> float:
	return a + b
#end function

def add(a: str, b: str) -> str:
	return a + b
#end function

'''
	expected result:
	>>add<< exists 3 times with different types to use

	real result:
	Python doesn't comes with a type expression like
	int, float, str, ..., thus Python doesn't care about
	to use a specific function / class method for a specific type.

	Therefore, the last detected >>add<< function is in use for anything,
	which can be used with + (like addition of numbers, string concatenation, ...)

	to solve this, use:
'''
from functools import singledispatch

'''
	define an abstract function
	This can also be called as well, but it raises
	a specific exception to tell, that this shall
	not be used.
'''
@singledispatch
def add(a,b) -> int:
	raise Exception('Do not use this function...')
#end function

'''
	By using @<function_name>.register<class_type>
	the interpreter checks, if the parameters are
	the specific type. If so, then this function is
	in use. If not, then Python tries to figure out
	if an another overloaded function exists.

	In case of no other function can be found, then
	the basic function is called instead.
'''
#	This function can only be used for integers.
@add.register(int)
def _(a,b) -> int:
	return a + b
#end function

#	only in use for floating points
@add.register(float)
def _(a,b) -> float:
	return a + b
#end function

#	only in use for strings
@add.register(str)
def _(a,b) -> str:
	return a + b
#end function

print(add(10,20))					#	works well
print(add(10.0, 20))				#	works well
print(add('Hello', ' world!'))		#	works well
# print(add('Hello', 8))			#	error
# print(add(0, ' world!'))			#	error
print(add(5, int(' 123')))			#	also works well

print('---------------------------------------')

'''
	However, by using a class with method overloading procedures
	this won't work. These are not supposed
	to use for classes.

	By trying to use typing.overload, multipledispatch.dispatch
	(pip[3|.exe] install multipledispatch) the results differ and
	often causes errors, like NotImplementedError, RecursionError, ...

	So, in classes there're no known methods yet, which allows
	to overload methods.
'''
from multipledispatch import dispatch
# from typing import overload
class Adder():
	def __init__(self) -> None:
		pass
	#end constructor

	@dispatch(int, int)
	# @overload
	def add(self, a, b) -> int:
		return a + b
	
		#by using overload instead:
		# ...
	#end method

	@dispatch(float, float)
	# @overload
	def add(self, a, b) -> float:
		return a + b
	
		# ...
	#end method

	@dispatch(str, str)
	# @overload
	def add(self, a, b) -> str:
		return a + b
	
		# ...
	#end method

	#	only for overload
	#	NOTE:	Theoretically, calling add(a,b) for a = int and b = int
	#			the add method for integers shall be called
	#			as expected, however, the basic add method (a and b for Any)
	#			will be called instead. Means: a RecursionError occour,
	#			because we're calling add over and over again...
	# def add(self, a, b):
	# 	if isinstance(a,int) and isinstance(b,int):
	# 		return self.add(a,b)
	# 	elif isinstance(a,float) and isinstance(b,float):
	# 		return self.add(a,b)
	# 	elif isinstance(a,str) and isinstance(b,str):
	# 		return self.add(a,b)
		
	# 	raise Exception("Unable to use add in a correct way...")
	# #end method

	#...
#end class

obj = Adder()
print(obj.add(a = 5, b = 9))
print(obj.add(a = 9.5, b = -3.210123456789e-3))
print(obj.add(a = 'Hello', b = ' World!'))