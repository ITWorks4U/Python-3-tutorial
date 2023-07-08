#!/usr/bin/python3

"""
	The module memory_profile allows us to take
	a more detailed look about allocated and
	released memory.

	However, when an exception appears,
	this profile is not completed, which means,
	we're not able to receive a detailed information.

	By default memory_profiler is not installed.
	=> pip3 install memory_profiler (Linux/macOS)
	=> pip.exe install memory_profiler (Windows)

	In combination with debugging a memory leak can easily be
	detected.
"""

from memory_profiler import profile
fp = None

@profile
def readAFile():
	global fp
	print('opening file...')
	fp = open('python_a-z.py')

	raise Exception('oops')

	print('closing file...')
	fp.close()
	fp = None
#end function

@profile
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
	#end try
#end main

if __name__ == '__main__':
	main()
#end entry point