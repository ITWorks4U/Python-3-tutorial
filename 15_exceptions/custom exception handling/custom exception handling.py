#!/usr/bin/python3

"""
	Defining an own exception class
	for our purpose.

	To trigger a custom exception, this
	must be thrown. In Python it's raised.
"""

#	-----------
#	custom exception class
#	-----------
class MathError(Exception):
	def __init__(self, message):
		self.__message = message
	#end constructor

	def printError(self):
		return self.__message
	#end method
#end class

#	-----------
#	function, which may throw (raise)
#	an exception
#	-----------
def divide(n: int, k: int):
	if k == 0:
		#	-----------
		#	must be done, otherwise the
		#	custom exception is never been
		#	triggered and maybe never been handled
		#	e. g. no basic exception handling is given
		#	-----------
		raise MathError("k must not be 0!")
	#end if

	return n/k
#end function

#	-----------
#	running
#	-----------
try:
	n,k = 100,10
	print(f'{n}/{k} = {divide(n,k)}')

	n,k = 42,0
	print(f'{n}/{k} = {divide(n,k)}')
except MathError as me:
	print(me.printError())
except ValueError:
	print("Illegal usage of divide function detected.")
except:
	print("An error has been detected")
#end try-except