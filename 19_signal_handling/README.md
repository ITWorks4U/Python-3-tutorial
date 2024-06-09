#	Oops, I did it (again)!

Looks similar to an exception, right?
Well, an exception and an interrupt might have a similar behavior: it pauses / stops the current instruction to "handle" a special case, but these are __NOT__ the same!

###	How to handle

In contrast to an exception, you can try to use an exception handling, but you often don't see a positive result.

required steps:
1.	import signal
2.	define a signal handler function
3.	register your possible signal

example:
```
import signal

def signalHandler(signal, frame):
	#.....

signal.signal(signal.SIGINT, signalHandler)
```