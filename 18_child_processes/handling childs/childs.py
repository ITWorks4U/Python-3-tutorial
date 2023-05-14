#!/usr/bin/python3

"""
	creating child process(es)
	by using fork

	a child process runs parallel
	to the main process

	on every time a new child process
	has been successfully created, this
	gets a new process-ID, uses the same
	program counter, CPU registers, open files, ...

	Unlike to fork.py the child process
	will be handled correctly.
"""

import os

#	----------
pid = os.fork()

if pid == 0:
	#	child process
	print(f'child process with process id: {os.getpid()}')
elif pid > 0:
	#	parent proces
	print(f'parent process with process id: {os.getpid()}, pid returned: {pid}')
else:
	#	in case of a fork wasn't successful
	print("fork() failed")
#end if