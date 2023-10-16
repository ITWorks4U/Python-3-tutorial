#!/usr/bin/python3

"""
	Memory leaks may appear by using any programming language
	and represents a critical area.

	Usually, when a resource is in use we ensure, that this
	resource will be released automatically by the garbage collector.

	However, the garbage collector is a non deterministic process,
	thus we don't know when this process starts and in case of
	an error, allocated memory might not be released.

	In combination with debugging a memory leak can easily be
	detected.

	video tutorial:	https://youtu.be/AK44C_uZ9u4
	timestamp:		05:57:06
"""

fp = None

def readAFile():
	global fp
	print('opening file...')

	#	Usually, open should be do with
	#	the with block to release the
	#	allocated memory automatically.
	#	No matter, if an exception ocurrs or not.
	fp = open('simple memory leak.py')

	raise Exception('oops')

	#	since an exception raises, these instructions
	#	below are now unavailable => the allocated
	#	memory is now lost while the application is still running
	print('closing file...')
	fp.close()
#end function

def main():
	try:
		readAFile()
	except Exception as e:
		print(f'error: {e.args[0]}')
	finally:
		print(f'file pointer has been closed: {fp.closed}')
	#end try
#end main

if __name__ == '__main__':
	main()
#end entry point