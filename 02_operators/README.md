#	Operators in python

Like in other programming languages operators are in use for different purpose.
You should know the difference between:
-	arithmetic operations ("simple math")
-	assignment operations
-	comparing
-	logic
-	bitwise
-	other left

##	Important: Don't use the wrong operations!

It sounds odd, but it's easy to use the wrong operators.
In example: "Check, if two varables (a,b) are the same."
correct:	a == b
wrong:		a is b, a & b, a and b (might have different usage or results) 

Since these operations are correct in syntax, their logic differs!

##	Where to use the operators?
###	arithmetic operations

-	for "simple" math, like: add, subtract, multiply, divide, modulo, ...

###	assignment operations

-	"just" to assign a value or a result to a varaible: a = 4+5

###	comparing

-	very often in use for condition checks, like: a == b

###	logical operations

-	are very similar to comparing operations: returns "True" or "False"
-	can also be in use to compare two or more objects, like: a and b

###	bitwise operations

-	are often in use for micro controller purpose
-	are not in use to compare, "just" to assign a new result to an object very fast

###	"other" operations left

-	memberships, like: "Check, if a value is in a set." => a in b, where b is a collection, like list, set, tuple or dictionary
-	identical checks, like: "Check, if two values are identical." => a is b, where a and b have the same value AND ALSO refers to the memory address