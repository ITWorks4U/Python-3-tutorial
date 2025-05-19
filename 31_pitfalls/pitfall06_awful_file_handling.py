###
#	bad exception handling
###

import sys

#NOTE: sys.argv[0] returns your current file
file = sys.argv[0]

'''
	Awful. Honestly...

	Your command to use a file may fail, if the file doesn't exist,
	you mistyped the name, the file is corrupted, you don't have
	access rights, ...
'''
file = open(file)

try:
	for line in file:
		print(line)
	#end for
except Exception as e:
	print(f'failed: {e.args}')
finally:
	file.close()
#end try


'''
	Not even better...

	Since your attempt can be handled by
	using an exception handler, the file object
	>>may<< only exist in your try block. Usually
	Python helps you out, so "file" is also available
	in the finally block.
'''
try:
	file = open(file)

	for line in file:
		print(line)
	#end for
except Exception as e:
	print(f'failed: {e.args}')
finally:
	file.close()
#end try

'''
	Best way:

	By using a with block this allows you
	to close the file stream automatically.
	No matter, if an exception may appear or not.

	Finally, the finally block may now be obsolete.
'''
try:
	with open(file) as file:
		for line in file:
			print(line)
		#end for
	#end with
except Exception as e:
	print(f'failed: {e.args}')
finally:
	pass
#end try
