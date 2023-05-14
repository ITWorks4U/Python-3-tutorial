#!/usr/bin/python3

"""
	Measuring time for any process(es)
	helps you to take a look on the
	efficiency of your code.
"""

#	-----------
#	there're two ways
#	for time measurement:
#
#	time module
#	timeit module
#	-----------
import time as t

"""
	calculating the fibonacci series
	attention: if you have ENOUGH time in your life, or if you
	want to see the death of the sun,
	then you also >could< try to use a value of 50 or higher :o)

	Fn = Fn-1 + Fn-2
	F0 = 0 and F1 = 1
"""
def fibonacci(a):
	if a == 0:
		return 0
	#end if

	if a == 1 or a == 2:
		return 1
	#end if

	return fibonacci(a-1) + fibonacci(a-2)
#end function

#	-----------
#	entry point
#	-----------
def main():
	ctr = 40

	#	print function can also be used with special formatting
	for i in range(ctr+1):
		start = t.process_time()
		print("F(%d) = %d" % (i, fibonacci(i)))
		end = t.process_time()

		print(f'elapsed time amount: {end-start}s')
	#end for
#end main

if __name__ == '__main__':
	main()
#end entry point