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

#	starting the debugging
#	attention: when we're terminating the
#	debugging process with 'quit' an unhandled
#	exception during process time may occur
#
#	in our case we don't mind that
pdb.set_trace()

#	using a snipped for debugging
counter = 0

while counter < 100:
	pass
#end while