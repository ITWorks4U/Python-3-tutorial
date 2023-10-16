#!/usr/bin/python3

"""
	3n+1 problem:

	if n is even => n/2
	if n is odd  => 3*n + 1
	if n is 1    => terminate

	video tutorial:	https://youtu.be/AK44C_uZ9u4
	timestamp:		04:39:53
"""

#	-----------
#	there're two ways
#	for time measurement:
#
#	time module
#	timeit module
#	-----------
from timeit import default_timer as timer

#	-----------
#	recursive way
#	-----------
def solve_recursive(number: int) -> int:
	print(f'{number:0.0f}', end=' => ')

	if number == 1:
		return 1
	#end if

	#	if number is even
	if number % 2 == 0:
		return solve_recursive(number/2)
	#end if

	#	otherwise number is odd
	return solve_recursive(3 * number + 1)
#end function

#	-----------
#	iterative way
#	-----------
def solve_loop(number: int) -> int:
	while number != 1:
		print(f'{number:0.0f}', end=' => ')

		if number % 2 == 0:
			number /= 2
		else:
			number = 3 * number + 1
		#end if
	#end while

	return 1
#end function

#	main
def main():
	n = 73

	#	-----------
	begin_r = timer()
	print(f'func({n}) = {solve_recursive(n)}')
	end_r = timer()
	summary_r = end_r-begin_r
	print(f'elapsed time amount: {summary_r}s')
	#	-----------

	print("-----------")

	#	-----------
	begin_i = timer()
	print(f'func({n}) = {solve_loop(n)}')
	end_i = timer()
	summary_i = end_i-begin_i
	print(f'elapsed time amount: {summary_i}s')
	#	-----------

	print("-----------")

	#	-----------
	if summary_r < summary_i:
		print(f"recursive function was faster by {summary_i-summary_r}s")
	else:
		print(f"iterative function was faster by {summary_r-summary_i}s")
	#end if

	print("-----------")

#end main

#	entry point
if __name__ == '__main__':
	main()
#end entry point