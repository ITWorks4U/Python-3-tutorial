#	Purpose

-	modules (other python scripts) offers you to access to functions, classes, etc.

###	using a module

-	there're 4 different ways to use a module:
1.	import >module 0, module 1, ..., module n-1<
2.	import >module 0, ..., module n-1< as >alias<
3.	from >module n< import >part k< as >alias<, part p as >alias<, ... 
4.	from >module n< import *

###	important / pitfalls

-	by default, the python interpreter looks in the current dictionary, where >>this<< module could be
-	if existing, it will be imported instead a system module, which has the identical name
-	if you've written your own string class and named that to "string.py", then the import below might fail, if the required functions, classes, etc. to import were not found 