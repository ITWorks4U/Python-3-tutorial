#!/usr/bin/python3

"""
	Offers simple arithmetic
	operations, which are going
	to test by using unit tests.
"""

#	-------------
#	custom exception class
#	-------------
class MathException(Exception):
	#constructor
	def __init__(self, errorMessage: str) -> None:
		self.errMsg = errorMessage
	#end constructor
#end class

#	-------------
#	custom math class
#	-------------
class BasicMath():
	__illegalArguments = 'illegal argument usage; int is required'
	__divideByZero = 'division by zero is not allowed'

	def addition(self, a: int, b: int) -> int:
		if not isinstance(a, int) or not isinstance(b, int):
			raise MathException(self.__illegalArguments)
		#end if

		return a+b
	#end method

	def subtraction(self, a: int, b: int) -> int:
		if not isinstance(a, int) or not isinstance(b, int):
			raise MathException(self.__illegalArguments)
		#end if

		return a - b
	#end function

	def multiply(self, a: int, b: int) -> int:
		if not isinstance(a, int) or not isinstance(b, int):
			raise MathException(self.__illegalArguments)
		#end if

		return a * b
	#end function

	def divide(self, a: int, b: int) -> int:
		if not isinstance(a, int) or not isinstance(b, int):
			raise MathException(self.__illegalArguments)
		#end if

		if b == 0:
			raise MathException(self.__divideByZero)
		#end if

		return a / b
	#end function
#end class