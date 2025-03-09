###
#	Using a return statement instead of yielding.
###

'''
	Example:
	"You have a huge number. Get all even numbers." Sounds easy, right?
	You can just use a loop to filter even numbers by "a % 2 == 0".
	Depending on the system you're working on, the processes, which runs
	on your system, ... this may results to a high performance issue.
	Even for modern computer systems.

	A return statement waits to return a result, until the result is able to return.
	A yield statement is able to return to the caller immediately without leaving a procedure until
	the full process has been completed.

	The function "evenNumbersReturnOnly" returns a list of integers.
	The function "evenNumbersYieldOnly" returns a generator of list[int], Any, None.

	By the way, it might be a really bad idea to print the result(s) on console or
	write the result(s) into a file and open the file with a basic editor.
'''

from timeit import timeit
from datetime import timedelta
from threading import Thread

n = 500500500

def evenNumbersReturnOnly():
	even = [x for x in range(n) if x % 2 == 0]
	
	#NOTE:	NOT recommended
	# print(f'even: {even}')

	# with open("even_return.txt", mode="w", encoding="latin-1") as dest:
	# 	print(even, file=dest)
	# #end with

	return even
#end function

def evenNumbersYieldOnly():
	yield [x for x in range(n) if x % 2 == 0]
#end function

def threadReturn() -> None:
	print(f'time amount for threadReturn: {timedelta(seconds=timeit(stmt=evenNumbersReturnOnly, number=1))}')
#end function

def threadYield() -> None:
	#NOTE:	NOT recommended
	# print(f'even: ')
	# for y in evenNumbersYieldOnly():
	# 	print(y, end="")
	# #end for
	# print()

	# with open("even_yield.txt", mode="w", encoding="latin-1") as dest:
	# 	for y in evenNumbersYieldOnly():
	# 		print(y, end="", file=dest)
	# 	#end for

	# 	print(file=dest)
	# #end with

	print(f'time amount for threadYield: {timedelta(seconds=timeit(stmt=evenNumbersYieldOnly, number=1))}')
#end function

def main() -> None:
	t0 = Thread(target=threadReturn)
	t1 = Thread(target=threadYield)

	t0.start()
	t1.start()

	t1.join()
	t0.join()
#end main

if __name__ == "__main__":
	main()
#end entry point
