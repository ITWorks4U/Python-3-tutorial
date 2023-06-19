#!/usr/bin/python3

"""
	Some operations without threading.
"""

import time as t

from module.test import doSomething
from module.fileIO import readFromFile, writeToFile

#	----------
#	simple test
#	without threading
#	----------
def test() -> None:
	begin = t.process_time()

	#	simulating "heavy operations"
	for i in range(5):
		print(f'run {i+1}')
		doSomething()
		print('----------')
	#end for

	end = t.process_time()
	print(f'elapsed time: {end-begin}s')
#end function

#	----------
#	do this again with file I/O
#	----------
#	depending on your machine,
#	other running processes etc.
#	this could take a long time
#	----------
#	The numbers in a range from (0, 1, ..., 99,999,999)
#	are going to write to a file and also
#	read from it.
#
#	attention: the result file has a size
#	of up to 900MB
#	----------
def fileTest() -> None:
	file = "test.txt"
	begin = t.process_time()

	try:
		writeToFile(fileName=file)
		print('-----------')
		readFromFile(fileName=file)
	except Exception as ex:
		print(f'{ex.args}')
	finally:
		end = t.process_time()
		print(f'elapsed time: {end-begin}s')
	#end try-catch
#end function

#entry point
if __name__ == '__main__':
	test()
	#fileTest()
#end entry point