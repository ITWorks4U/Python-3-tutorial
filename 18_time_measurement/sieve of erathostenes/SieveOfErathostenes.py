#!/usr/bin/python3

"""
	customized example to
	to find prime numbers by
	using the sive of erathostenes
"""

import SieveException

class SieveOfErathostenes:
	#	-----------
	#	contains primes
	__primeList = list()
	#	-----------

	#	-----------
	#	constructor; lower boundary is fixed, upper boundary can be determined
	#	or the default value are in use
	#	-----------
	def __init__(self, upper_bound: int = 50000) -> None:
		self.__lower_bound = 2
		self.__upper_bound = upper_bound
	#end constructor

	#	-----------
	#	determine all prime numbers within known boundaries
	#
	#	returns:
	#		a list of all primes
	#	-----------
	def sieve(self) -> list:
		#	-----------
		#	check for correct boundaries
		#	-----------
		if self.__lower_bound == self.__upper_bound:
			raise SieveException("Boundaries are equal.")
		#end if

		if self.__upper_bound < self.__lower_bound:
			raise SieveException("Upper bound is lower than lower bound.")
		#end if
		#	-----------

		prime_table = list()

		for i in range(self.__upper_bound + 1):
			prime_table.append(True)
		#end for

		while (self.__lower_bound * self.__lower_bound <= self.__upper_bound):
			if prime_table[self.__lower_bound]:
				for i in range(self.__lower_bound ** 2, self.__upper_bound + 1, self.__lower_bound):
					prime_table[i] = False
				#end for
			#end if

			self.__lower_bound += 1
		#end while

		for i in range(self.__upper_bound + 1):
			if i >= 2 and prime_table[i]:
				self.__primeList.append(i)
			#end if
		#end for

		return self.__primeList
	#end method
#end class