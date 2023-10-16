#!/usr/bin/python3

"""
	How to debugging code in python 3.

	By using an IDE you can set a breakpoint in front
	of your line number. By running your script on the
	default way, your running process will be paused,
	when a breakpoint has been reached.

	You're also able to run your application with
	a debugging process.

	useful commands for debugging:
	next - go to the next procedure detected
	continue - continue your process
	jump <line-nbr> - go to a specific line number
	quit - terminate the debugging process

	video tutorial:	https://youtu.be/AK44C_uZ9u4
	timestamp:		04:30:22
"""

#	importing the module for debugging
import pdb

def suspicious():
	counter = 0

	while counter < 100:
		pass
	#end while
#end function

#	you can also run a specific funtion for your debugging process, like:
#	pdb.run('function'), where the name of the function must exist
#	pdb.run('function(x=100)') with an argument and its value
#
#	not recommended
# pdb.run('suspicious()')

#	using that instead:
#	pdb.runcall(func: (**_P@runcall), *args: _P.args, **kwds: _P.kwargs)
#	using your function to call
#	if any arguments are required, move that to args or kwds, depending on your
#	amount and type of arguments
pdb.runcall(suspicious)

#	if your function takes counter as argument
# pdb.runcall(suspicious, 0)

#	unlike to pdb.set_trace() no exception will be thrown by using 'quit'