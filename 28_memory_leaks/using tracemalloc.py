#!/usr/bin/python3

"""
	The tracemalloc module allows us to "listen" to
	the used allocated memory during runtime.

	In combination with debugging a memory leak can easily be
	detected.
"""
import tracemalloc

fp = None

#	number of frames (similar to lines), which will be traced
tracemalloc.start(100)

def readAFile():
	global fp
	print('opening file...')
	fp = open('python_a-z.py')

	raise Exception('oops')

	print('closing file...')
	fp.close()
	fp = None
#end function

def main():
	try:
		readAFile()
	except Exception as e:
		print(f'error: {e.args[0]}')
	finally:
		if fp is None:
			print('fp is None (again)')
		else:
			print(f'Has this file pointer been closed? {fp.closed}')
		#end if

		"""
			We're taking the current snapshot and
			try to figure out, which informations
			can we get.
		"""
		snapshot = tracemalloc.take_snapshot()
		top_stats = snapshot.statistics('traceback')

		for stat in top_stats:
			print(f'# memory blocks: {stat.count}, size: {stat.size} bytes')

			for line in stat.traceback.format():
				print(line)
			#end for
		#end for
	#end try
#end main

if __name__ == '__main__':
	main()
#end entry point