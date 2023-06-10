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

	What happens here?
"""

import os

#	----------
#	create a new
#	child process
#	----------

_ = os.fork()
_ = os.fork()
_ = os.fork()
_ = os.fork()

print("Hi there!")

"""
	after each fork a new child process
	has been created, however, the number
	of new processes exceeds drastically,
	if you don't mind

	in that case 16 processes are running
	1 main process and 15 child processes

	It's unclear, when the main process
	may end. This could be after the first
	output or sometimes later

	every child process, which is "still alive"
	after main termination becomes orphan and will
	be collected and handled by the init process
	(process-ID: 1)
"""