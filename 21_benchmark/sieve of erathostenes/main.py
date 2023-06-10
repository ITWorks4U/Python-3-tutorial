#!/usr/bin/python3

"""
	customized example to
	to find prime numbers by
	using the sive of erathostenes
"""

from SieveOfErathostenes import SieveOfErathostenes as Sieve
from TimeSummary import TimeSummary as tsum
import time as t
import SieveException

try:
	begin = t.time()

	#	by default it starts from 2 to 50000
	#
	#	-----------
	#	attention: by using an upper boundary like:
	#	upper_bound=500500500
	#
	#	It takes some minutes depending on your system
	#	whereas over 26,000,000 primes were found and
	#	the result text file has a size of up to 300 MB!
	#	-----------
	soa = Sieve()
	primes = soa.sieve()
	print("found {0} prime numbers".format(len(primes)))
	end = t.time()
	
	ts = tsum()
	ts.summary(end-begin)

	with open(file="sieve.txt", mode="w") as f:
		for i in primes:
			print(i, file=f)
		#end for
	#end while
except SieveException as se:
	print(se.printMessage())
except Exception as ex:
	print(f"{ex.args}")
#end try-except