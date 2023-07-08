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

		#	the syntax for args is a bit weired, however, it requires
		#	an argument, followed by a comma
		#	a space behind the comma is unnecessary
		writeThread = Thread(target=f.writeToFile, args=(file,))
		readThread = Thread(target=f.readFromFile, args=(file,))

		#	instead of using args, you can also use kwargs, which
		#	represents a dictionary of string (key) and any (value):
		#
		#	attention: the key in kwargs must be a single expression only
		#	and it must be the argument name, otherwise an error appears
		writeThread = Thread(target=f.writeToFile, kwargs={'fileName' : file})
		readThread = Thread(target=f.readFromFile, kwargs={'fileName' : file})

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
#	using an indepented thread
#	----------
def fileTestThreadIndepented():
	#	Unlike to the regular threads, which runs parallel
	#	to the main thread, sometimes it's required to run
	#	a thread, where the main thread has no need to wait
	#	until the thread(s) is/are finished.
	#
	#	Since a thread is marked as a daemon thread, it runs
	#	in the background. Similar to other programming languages
	#	this thread has been detached.
	#
	#	Usually, once a thread has been finished it can't be collected
	#	by the main thread. However, in python you can also to this without
	#	any consequences by default.
	#
	#	Background threads are very often in use on a GUI,
	#	to prevent to freeze the application.
	file = "test.txt"
	begin = t.process_time()

	try:
		print("starting file operations with indepented threads...")

		#	with daemon = True (defaults to False) this thread runs as a
		#	background service
		writeThread = Thread(target=f.writeToFile, kwargs={'fileName' : file}, daemon=True)
		readThread = Thread(target=f.readFromFile, kwargs={'fileName' : file}, daemon=True)

		writeThread.start()
		readThread.start()

		print("-----------")

		#	When we omit these instructions our application might be terminated
		#	in less than 1ms, but the threads might still running!
		#
		#	One of the main advantages of daemon threads is that they can run in the background
		#	without blocking the main program. This is useful for tasks that are not critical to
		#	the functioning of the program, such as logging or monitoring.
		#
		#	Another advantage of daemon threads is that they can be used to perform periodic tasks,
		#	such as cleaning up temporary files or sending heartbeat signals,
		#	without the need for a separate scheduler.
		#
		#	However, there are also some disadvantages to using daemon threads:
		#		-	since daemon threads are not critical to the functioning of the program,
		#			they may be terminated abruptly if the main program exits before they
		#			have completed their execution => our test.txt doesn't contain all lines
		#
		#		=>	this can lead to unexpected behavior and potential data loss

		# readThread.join()
		# writeThread.join()
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

		writeThread = Thread(target=m.writeToFile, args=(file,))
		readThread = Thread(target=m.readFromFile, args=(file,))

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
	# fileTestThreadIndepented()
	# fileTestMutex()
#end entry point