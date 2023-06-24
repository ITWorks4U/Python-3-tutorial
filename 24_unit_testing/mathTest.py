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
	def __init__(self, errorMessage: str) -> None:
		self.__errMsg = errorMessage
	#end constructor

	def getErrorMessage(self) -> str:
		return self.__errMsg
	#end method
#end class

class BasicMath():
	def add(self, a: int, b: int) -> int:
		if not isinstance(a, int) or not isinstance(b, int):
			raise MathException('illegal argument usage; int is required')
		#end if

		return a+b
	#end method

	def sub(arg1: int, arg2: int) -> int:
		if not isinstance(arg1, int) or not isinstance(arg2, int):
			raise MathException('one of the arguments is not decimal')
		#end if

		return arg1 - arg2
	#end function

	def mul(arg1: int, arg2: int) -> int:
		if not isinstance(arg1, int) or not isinstance(arg2, int):
			raise MathException('one of the arguments is not decimal')
		#end if

		return arg1 * arg2
	#end function

	def div(arg1: int, arg2: int) -> int:
		if not isinstance(arg1, int) or not isinstance(arg2, int):
			raise MathException('one of the arguments is not decimal')
		#end if

		if arg2 == 0:
			raise MathException('division by zero is not allowed')
		#end if

		return arg1 / arg2
	#end function
#end class