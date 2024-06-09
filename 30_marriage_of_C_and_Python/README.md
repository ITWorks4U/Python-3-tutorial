#	The companion of Python and C

-	sometimes it's required to use a function, often written in C, for python
-	since Python does not comes with data types, it's hard to understand which type from a C library can be used correctly for python and vice versa

##	contents

1.	accessing to a C function, which prints a text to the console
2.	accessing to a C function, which calculates the square multiplication for a number range and returns it result back to Python

###	need to know

-	using ctypes module (shall already comes with Python)
-	written and tested only under a Linux Mint 21.1 Cinnamon
-	the C source file(s) must be converted into a library, e. g. .dll, .so, ... with specific arguments form a C compiler (here: gnu gcc)
-	not sure, if a C++ library can also be used like a C library