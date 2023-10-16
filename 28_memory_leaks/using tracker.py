#!/usr/bin/python3

"""
	Using a foreign library, like pympler.
	Reference: https://github.com/pympler/pympler

	This allows us to give a summary or a difference
	of the actions.
"""

from pympler.tracker import ObjectTracker

fp = None
tracker = ObjectTracker()

def readAFile(fileName: str):
	global fp
	print(f'opening file {fileName}...')

	# fp = open(fileName)
	# #	raising an exception here for any reason
	# raise Exception('oops')
	# print('closing file...')
	# fp.close()

	with open(fileName) as fp:
		raise Exception('oops')
	#end with

#end function

def main():
	try:
		readAFile('using tracker.py')
	except Exception as e:
		print(f'error: {e.args[0]}')
	finally:
		print(f'file pointer has been closed: {fp.closed}')

		tracker.print_diff()
	#end try
#end main

if __name__ == '__main__':
	main()
#end entry point