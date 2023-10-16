#!usr/bin/python3

"""
	Signal handling allows to to react to
	signals. For instance, these are: pressing Ctrl+C
	in an endless loop or whenever the process has been
	killed or there was an error by used shared memory or ...

	Often misinterpreted: exceptions and interrupts
	aren't equal!

	an exception triggers at a specific time or place
	an interrupt may appear at any time anywhere

	A signal can handled by:
	- real handling (system based or customized)
	- blocking (may terminate the application with exit code > 0)
	- ignoring (may ignore the signal, however, not every signal can be ignored)

	This example demonstrates an endless loop,
	where the interrupt signal has been ignored.

	You can press CTRL + C as often as you want,
	but no action is able to do.

	There're other ways to terminate this application:
	- terminating the process
	- killing the process
	- set an alarm to terminate the application automatically

	video tutorial:	https://youtu.be/AK44C_uZ9u4
	timestamp:		04:11:12
"""

#	-----------
#	required modules
#	signal: accessing to signal types
#	and handling
#	sys: system based operations in
#	cooperation with signal
#	-----------
import signal as sig, sys as system

#	-----------
#	"global" state for
#	signal handling
#	-----------
state = True

#	-----------
#	handler function, which is
#	going to be trigger, whenever
#	at any time a interrupt has
#	been detected, e. g. CTRL + C
#
#	first argument:
#		represents signal number
#	second argument:
#		shows on which line the
#		signal handler function has
#		been triggered
#	-----------
def cleanUp(signal, frame):
	print(f'handling signal {signal} <=> ({sig.Signals(signal).name})')
	print(f'{frame}')

	#	any clean up operations here

	#	-----------
	#	resetting alarm
	#
	#	if alarm is set and during
	#	the time amount no signal has been
	#	triggered, the application will be
	#	terminated with an error exit code
	#	-----------
	# sig.alarm(0)

	#	-----------
	#	it's necessary, that the system
	#	handling function also needs a
	#	kind of "break", otherwise the
	#	endless loop will be continued
	#
	#	the whole process could be terminated
	#	or a boolean value could be switched
	#	-----------
	#	to modify the global state,
	#	inside of this function it must
	#	be marked as global (without any assignment)
	#	to modify the state...
	#	-----------
	global state
	state = False

	#	-----------
	#	... or, if required, terminate
	#	the application with exit() function
	#	-----------
	#system.exit(0)
#end function

#	-----------
#	registering signals
#	for our purpose
#	-----------
def registerSignals():
	#	-----------
	#	signal interrupt (CTRL + C) is now
	#	marked as ignored
	#	-----------
	sig.signal(sig.SIGINT, sig.SIG_IGN)

	#	-----------
	#	termination signal is now
	#	registered for handling
	#	-----------
	sig.signal(sig.SIGTERM, cleanUp)

	#	-----------
	#	Some signals can also be blocked,
	#	however, it's not smart to do this,
	#	unless, you really know, what you do.
	#
	#	for instance: SIGTERM could also be marked
	#	as SIG_BLOCK => on termination the signal handling
	#	function is not in use and the application itself
	#	returns an error exit code (143 or else)
	#	-----------
	#	a signal segmentation fault (illegal memory access, ...)
	#	is marked as blocked, but this may cause an undefined behavior
	#	-----------
	sig.signal(sig.SIGSEGV, sig.SIG_BLOCK)

	#	-----------
	#	in contrast to other programming
	#	languages, like C, the SIGKILL can't be
	#	used for handling, ignoring or blocking
	#
	#	by using this command an OSError: [Errno 22] Invalid argument
	#	will be printed on console
	#	-----------
	# sig.signal(sig.SIGKILL, cleanUp)

	#	-----------
	#	if given, then after a time
	#	amount of x seconds the application
	#	will be terminated
	#
	#	it doesn't matter, if a signal has been
	#	triggered or not; the exit code may differ
	#
	#	in that case the application exits with code 142
	#
	#	see also: https://docs.python.org/3.10/library/signal.html
	#	-----------
	# sig.alarm(5)
#end function

#	-----------
#	starting...
#	-----------
def main():
	print("Waiting patiently...")

	#	-----------
	#	Usually, by pressing CTRL + C
	#	a KeyboardError results and you
	#	assumed to handle this "exception"
	#	with an exception handling.
	#
	#	It works, too, however, since this
	#	is a signal, it must be handled in
	#	another way.
	#	-----------
	#	state is set to True at the beginning
	#	and will be switched to False in
	#	signal handling function
	#	-----------

	while state:
		pass
	#end while
#end main

if __name__ == "__main__":
	registerSignals()
	main()
#end entry point