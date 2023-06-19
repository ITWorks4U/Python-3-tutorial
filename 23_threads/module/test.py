#!/usr/bin/python3

"""
	test for
	no threading, threading
	and for mutex threading
"""

#	1,000,000,000
max_count = 1000000000

#	-----------
#	a simple function
#	without / with threads
#	-----------
def doSomething() -> None:
	print('using default function...')

	#	repeat that 1,000,000,000 times
	for _ in range(max_count):
		pass
	#end for

	print('Done!')
#end function

#	-----------
#	example functions
#	with mutex
#	-----------
#	register that this thread
#	is going to block
#	the file operation
#	----------
#	there's no guarantee, that this
#	operation can be locked during
#	processing
#	----------
#	mutex := mutual exclusion
#	block a shared resource, e. g. a file
#	until the operation is finished
#
#	every other thread, which might also use
#	this shared resource must wait
#	----------
#	unlike
#	with mutex:
#		...
#
#	you also can write:
#	mutex.aquire()
#	...
#	mutex.release()
#
#	The second mutex instruction, however, will never
#	been released automatically,
#	when an exception / signal occurred!
#	----------
#	Be careful with locked mutex and
#	dependencies to other threads, otherwise
#	a deadlock will appear!
#	----------

import threading
mutex = threading.Lock()

def function1Mutex() -> None:
	print('using function 1 with mutex')

	mutex.acquire()
	for _ in range(max_count):
		pass
	#end for

	mutex.release()

	print('Done with mutex 1!')
#end function

def function2Mutex() -> None:
	print('using function 2 with mutex')

	with mutex:
		for _ in range(max_count):
			pass
		#end for
	#end with

	print('Done with mutex 2!')
#end function