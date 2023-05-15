#!/usr/bin/python3

"""
	Some operations with threading.
	----------
	functions:
	-	simulating "heavy process"
	-	file I/O with threads
	-	file I/O with mutex
	----------
"""

import time as t
from threading import Thread

import module.test as s
import module.fileIO as f
import module.mutexFileIO as m

#	----------
#	simulating "heavy process"
#
#	using 5 threads
#	----------
def testThread() -> None:
	print('starting with threads')
	begin = t.process_time()

	try:
		#	creating 5 threads
		t0 = Thread(target=s.doSomething)
		t1 = Thread(target=s.doSomething)
		t2 = Thread(target=s.doSomething)
		t3 = Thread(target=s.doSomething)
		t4 = Thread(target=s.doSomething)

		#	starting threads
		t0.start()
		t1.start()
		t2.start()
		t3.start()
		t4.start()

		print("-----------")

		#	after finishing collect each thread
		t4.join()
		t3.join()
		t2.join()
		t1.join()
		t0.join()
	except Exception as ex:
		print(f'error: {ex.args}')
	finally:
		end = t.process_time()
		print(f'elapsed time amount: {end-begin}s')
	#end try-catch
#end function

#	----------
#	repeating "heavy process" by
#	using mutex
#	----------
def testMutex() -> None:
	print('starting with mutex')
	begin = t.process_time()

	try:
		t0 = Thread(target=s.function1Mutex)
		t1 = Thread(target=s.function2Mutex)

		t0.start()
		t1.start()

		print("-----------")

		t1.join()
		t0.join()
	except Exception as ex:
		print(f'error: {ex.args}')
	finally:
		end = t.process_time()
		print(f'elapsed time amount: {end-begin}')
	#end try-catch
#end function

#	----------
#	using threads for I/O
#	----------
def fileTestThread() -> None:
	file = "test.txt"
	begin = t.process_time()

	try:
		print("starting file operations with threading...")

		#	the syntax for args is a bit weired, however, this works
		#	in that way only
		writeThread = Thread(target=f.writeToFile, args=(file, ))
		readThread = Thread(target=f.readFromFile, args=(file, ))

		writeThread.start()
		readThread.start()

		print("-----------")

		readThread.join()
		writeThread.join()
	except Exception as ex:
		print(f"{ex.args}")
	finally:
		end = t.process_time()
		print(f"elapsed time amount: {end-begin}s")
	#end try-finally
#end function

#	----------
#	using mutex for I/O
#	----------
def fileTestMutex() -> None:
	file = "test.txt"
	begin = t.process_time()

	try:
		print("starting file operations with threading...")

		writeThread = Thread(target=m.writeToFile, args=(file, ))
		readThread = Thread(target=m.readFromFile, args=(file, ))

		writeThread.start()
		readThread.start()

		print("-----------")

		readThread.join()
		writeThread.join()
	except Exception as ex:
		print(f"{ex.args}")
	finally:
		end = t.process_time()
		print(f"elapsed time amount: {end-begin}s")
	#end try-finally
#end function

#entry point
if __name__ == '__main__':
	pass

	#	----------
	#	test the efficiency by using
	#	one or more of the function
	#	calls below
	#	----------
	
	# testThread()
	# testMutex()
	# fileTestThread()
	# fileTestMutex()
#end entry point