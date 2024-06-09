#	Time to start with "parallel" operations!

Well, child processes can be used to do this, but these are not really supposed to do that.

###	How to create a child process

-	use the fork() function to do this

###	pitfalls
-	unexpectd application behavior, if you don't mind
-	you can easy create a __deadlock__
-	a sub process it __not__ identical to a thread

###	What kind of processes exists?
1.	orphan process (the parent process terminates earlier than its child)
2.	zombie process (the child process terminates earlier than its parent)

###	Waiting for a child
use:
```
import os

......

os.wait() => forces to wait to terminate the parent process until the child process has been terminated
```

###	Where are these required?

to learn about how to use them
sometimes to control a specific piece of your code, e. g. a process shall read a file only, whereas an another process shall write to a file only => has much more undefined behaviors than you expect at the moment