#!/usr/bin/python3

"""
	customized example to
	to find prime numbers by
	using the sive of erathostenes
"""

class SieveException(Exception):
	#constructor
	def __init__(self, err_msg: str) -> None:
		self.__err_message = err_msg
	#end constructor

	def printMessage(self) -> str:
		return self.__err_message
	#end method
#end class