###
#	concatenating strings
###

from timeit import timeit
from threading import Thread
from datetime import timedelta

'''
	Even a small change may do a big difference.

	concatenate1() concatenates a string 5,000
	times, whereas word can be stored 5,000 times
	to a new memory address

	you'll get:
	-	lack of memory
	-	more amount of time to do operations

	concatenate2() is a bit better than the first function,
	because 'abc' will be stored into a single list and
	finally this will be converted into a single word
'''
def concatenate1() -> str:
	word = ''

	for _ in range(5000):
		word += 'abc'
	#end for

	return word
#end function

def concatenate2() -> str:
	collection = list()

	for _ in range(5000):
		collection.append('abc')
	#end for

	return ''.join(collection)
#end function

'''
	Even concatenate function will be repeated 1,000,000 times (default argument by timeit()) and the
	elapsed time amount can easily be converted into a human readable time.
'''

def threadFunction1() -> None:
	print(f'time amount for concatenate1: {timedelta(seconds=timeit(concatenate1))}')
#end function

def threadFunction2() -> None:
	print(f'time amount for concatenate2: {timedelta(seconds=timeit(concatenate2))}')
#end function

if __name__ == '__main__':
	th0 = Thread(target=threadFunction1)
	th1 = Thread(target=threadFunction2)

	th0.start()
	th1.start()

	print(f'nothing to do here...')

	th1.join()
	th0.join()
	
	print('Done!')
#end entry point
