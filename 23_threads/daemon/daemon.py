#!/usr/bin/python3

"""
	Running a thread or multiple threads
	in the background, to avoid to block
	the main thread.

	Sometimes it's recommended to do this,
	especially the thread runs forever in theory.

	Since a thread is marked as daemon, this runs
	in the background and does no longer affect
	the main thread, however, this makes no
	guarantee, that all background threads stops
	their activities, when the application has been
	terminated!

	video tutorial:	https://youtu.be/AK44C_uZ9u4
	timestamp:		04:56:05
"""

from time import sleep
from random import random
from threading import Thread
import signal as sig

#	------------
#	global values
#	------------
value = 0
onContinue = True

#	------------
#	signal handler (Ctrl + C, kill <process id>)
#	------------
def handler(signal, frame):
	global onContinue
	onContinue = False
#end function

#	------------
#	outsourced thread function
#	------------
def task():
	global value
	currentValue = value

	while onContinue:
		if value != currentValue:
			print(f'new value: {value}')
			currentValue = value
		#end if

		#	------------
		#	wait 100ms for
		#	the next turn
		#	------------
		sleep(0.1)
	#end while

	#	------------
	#	Is that ever
	#	be able to reach?
	#	------------
	print('the end')
#end function

#	------------
#	main
#	------------
sig.signal(sig.SIGINT, handler)
sig.signal(sig.SIGTERM, handler)

print('Starting...')

'''
	Since t is now a background thread,
	this won't longer block the main thread
	at the end, however, t may still running
	when the main application has been terminated.

	Try to run that sample without the daemon argument
	or daemon = False. :o)
'''
t = Thread(target=task, daemon=True)
t.start()

for _ in range(5):
	v = random() * 3
	sleep(v)

	value = v
#end for

print('Main thread done.')

#	waiting up to 3 seconds
#	for the next instruction(s)
t.join(timeout=3)
print(f'Everything worked well, right? By the way, is t still alive? {t.is_alive()}')

#	to make sure, that also the thread is now finished
#	this can be done by setting onContinue = False
#	or raising an expected signal
onContinue = False
# sig.raise_signal(sig.SIGINT)

#	finally, wait 1s => "the end" must be shown on the console
sleep(1)
print(f'Checking again: Is t still alive? {t.is_alive()}')