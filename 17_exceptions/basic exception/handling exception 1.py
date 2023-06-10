#!/usr/bin/python3

"""
	At any time an error may appear.
	It's your job to let detect such kind
	of errors and handle these.

	If unhandled, the application crashes
	with a full stack trace, where this
	exception has been triggered.
"""

"""
#	-----------
#	trying to read a file,
#	which doesn't exist or
#	no access rights are given,
#	or file is corrupted or else
#
#	Traceback (most recent call last):
#		File "handling exception 1.py", line 25, in <module>
#			with open(file="Non existing file here", mode="r") as f:
#	FileNotFoundError: [Errno 2] No such file or directory: 'Non existing file here'
#	-----------
with open(file="Non existing file here", mode="r") as f:
	print(f.read())
#end with
"""

#	-----------
#	again by handling
#	the exception
#	-----------

try:
	"""
		critical area; inside of this area
		any error on any time may appear and
		is possible to handle, if the current exception
		can be catched up...
	"""

	with open(file="Non existing file here", mode="r") as f:
		print(f.read())
	#end with
except FileNotFoundError as fnff:
	#	-----------
	#	handes IO errors, like file not found
	#	and prints the error message to the console
	#	-----------

	print(f'got an error: {fnff.strerror}')
except Exception as e:
	#	-----------
	#	handler for common exceptions, which
	#	hasn't been handled before
	#
	#	basic exception is not required;
	#	works also: except:
	#
	#	prints error number and error message
	#	to the console
	#
	#	since this is the super class, every
	#	child exception behind that block will
	#	never been triggered
	#	-----------

	print(f'critical error detected: {e.args}')
except NotImplementedError as nie:
	#	-----------
	#	is never been triggered
	#	-----------

	pass
else:
	#	-----------
	#	--optional--
	#	runs only, if no exception has been triggered
	#
	#	became obsolete
	#	-----------

	print("...else block, if no error has been detected...")
finally:
	#	-----------
	#	--optional--
	#	code, that always runs
	#	it doesn't matter, if an exception
	#	has been triggered or not
	#
	#	if used, it always comes as the last instruction
	#	-----------

	print("...finally block...")
#end try-catch