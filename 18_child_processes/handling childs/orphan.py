#!/usr/bin/python3

"""
	When the main process ends too early,
	then the child process becomes orphan
	and the init process collect that.
"""

import os, time

#	----------
pid = os.fork()

if pid == 0:
	#	child process
	print(f'child process with process id: {os.getpid()}, parent process: {os.getppid()}')
	time.sleep(5)

	#	----------
	#	at this point the child
	#	process is now orphan
	#	----------
	print(f'child process with process id: {os.getpid()}, parent process: {os.getppid()}')
	print("child process ends...")
elif pid > 0:
	#	parent proces
	print(f'parent process with process id: {os.getpid()}, pid returned: {pid}')
	time.sleep(1)
	print("parent process ends...")
else:
	#	in case of a fork wasn't successful
	print("fork() failed")
#end if