#!/usr/bin/python3

"""
	often misinterpreted: exception and interrupt
	aren't equal

	an exception triggers at a specific time or place
	an interrupt may appear at any time anywhere

	this example demonstrates an endless loop
	and can be handled only by pressing CTRL+C
"""

try:
	#	endless loop
	print("Waiting patiently...")

	while (True):
		pass
	#end while
except KeyboardInterrupt as k:
	#	-----------
	#	this is wrongly interpreted
	#	as an exception, where this
	#	is an interruption
	#
	#	k.args has no information for us
	#	-----------
	print(f"CTRL + C has been pressed: {k.args}")
except Exception as e:
	#	-----------
	#	fun fact: the basic exception class can't
	#	handle this interrupt correctly
	#
	#	you'll see the that:
	#	Waiting patiently...
	#	^CFinally!
	#	Traceback (most recent call last):
	#		File "handling exception 2.py", line >LINE_NBR<, in <module>
	#			pass
	#	KeyboardInterrupt
	#	-----------
	print(f'{e.args}')
finally:
	print("Finally!")
#end try-except