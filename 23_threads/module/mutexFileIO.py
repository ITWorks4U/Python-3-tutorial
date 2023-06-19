#!/usr/bin/python3

"""
	File operations with threading.

	Offers to write something into a file
	and also read from it.

	Unlike to fileIO.py these operations
	works with mutex only.

	mutex := mutual exclusion

	Doesn't comes with exception handling!
"""

#	----------
#	offers to use
#	mutex
#	----------
import threading
mutex = threading.Lock()

#	100,000,000
max_count = 100000000

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
def writeToFile(fileName: str) -> None:
	with mutex:
		print(f'by using mutex trying to write to file: {fileName}')

		with open(file=fileName, mode='w', encoding='utf-8') as f:
			#	repeat that 100,000,000 times
			for i in range(max_count):
				_ = f.write(str(i+1) + '\n')

				#	inform the user on each 1,000,000 steps
				if i % 1000000 == 0:
					print(f'step {i}')
				#end if
			#end for
		#end with

		print('Done with writing!')
	#end with
#end function

def readFromFile(fileName: str) -> None:
	with mutex:
		print(f'by using mutex trying to read from file: {fileName}')

		with open(file=fileName, mode='r', encoding='utf-8') as f:
			for i, line in enumerate(f, start=0):

				#	print each 1,000,000th line
				if i % 1000000 == 0:
					print(line)
				#end if
			#end for
		#end with

		print('Done with reading!')
	#end with
#end function