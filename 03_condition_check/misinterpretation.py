#!/usr/bin/python3

a = 10
b = 20

"""
	a == b means:	if the values of a and b are equal

	often wrongly interpreted:
	-	a and b means:	if the values of a and b differs to zero
	-	a is b means:	if a and b refers to the identical object
	-	a & b means:	the binary expression (0, 1) of a and b are
						compared to each other and returns
						a new value

						a:	00001010 (10)
						b:	00010100 (20)

						a & b:
							00000000 (0)
"""
print("these aren't typical condition checks...")

#	-------------------
#	locical expressions
#	-------------------
if a and b:
	print("a and b differs to zero")
#end if

if not a and b:
	print("a is or b must be zero")
#end if

#	~~~~~~~~~~~~~~~~~~~~
b = 0

if a and not b:
	print("a is or b must be zero")
#end if

b = 20
#	~~~~~~~~~~~~~~~~~~~~

#	-------------------
#	object comparison expression
#	-------------------
if a is b:
	print("a is b")
#end if

if not a is b:
	print("a is not b")
#end if

#identical to condition check above
if a is not b:
	print("a is not b")
#end if

#	-------------------
#	binary expression
#	-------------------
if a & b:
	print("Hooray, a 'condition check'!")
else:
	print("Wait a minute...?!?")
#end if