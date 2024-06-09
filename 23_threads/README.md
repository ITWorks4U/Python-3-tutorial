#	Time to start with "parallel" operations!

In contrast to child processes, a thread is supposed to be used for parallel instructions.

###	How to create a thread

use:
```
from threading import Thread
t = Thread(target=<function for thread>) # basic function with None as return only
t.start()
```

###	pitfalls
-	unexpected application behavior, if you don't mind
-	you can easy create a __deadlock__
-	a thread does not comes with a *stop()* function => you must use *join()* instead

###	What kind of threads exists?
1.	parallel threads (means: while your main application runs, a thread may also run on the same layer => by using a GUI, you'll see the difference)
2.	background threads (often called: **daemon thread** => run a task in the background to save resources and **not** blocking an another thread, like the GUI-thread)

###	terminating a thread
use:
```
t.join()
```

###	Where are these required?

to learn about how to use them
sometimes to control a specific piece of your code, e. g. a thread shall read a file only, whereas an another thread shall write to a file only => has much more undefined behaviors than you expect at the moment => use mutex / semaphores to handle such situations smarter