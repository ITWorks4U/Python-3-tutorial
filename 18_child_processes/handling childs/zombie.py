#!/usr/bin/python3

"""
	When the child process ends too early,
	then it becomes to a zombie.

	in UNIX/linux/mac os start a new terminal and
	type ps -efl | grep -v grep | grep zombie
	to see what's happening here

	in Windows type:
	(CMD) tasklist or (powershell) get-process
"""

import os, time

#	----------
pid = os.fork()

if pid == 0:
	#	child process
	print(f'child process with process id: {os.getpid()}, parent process: {os.getppid()}')
	time.sleep(1)
	print("child process ends...")
elif pid > 0:
	#	parent proces
	print(f'parent process with process id: {os.getpid()}, pid returned: {pid}')
	print('"Mommy comes back very soon!"')

	try:
		while True:
			pass
		#end while
	except KeyboardInterrupt:
		pass
	#end try-except

	print(f"Wait! What's happened with pid-ID: {pid}?")
	print("parent process ends...")
else:
	#	in case of a fork wasn't successful
	print("fork() failed")
#end if