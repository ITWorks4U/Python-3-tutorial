#!/usr/bin/python3

"""
	Unlike in the most programming / scripting languages
	Python doesn't comes with a switch-case.

	We should use if, elif, elif, ..., else instead, however,
	by using a combination of functions and dictionaries
	we can simulate a switch-case.
"""

#	----------------
#	"normal" usage of
#	a condition check
#	----------------
numberToUse = 0

if numberToUse == 0:
	print(type(numberToUse))
elif numberToUse == 1:
	print(type(list(numberToUse)))
elif numberToUse == 2:
	print(numberToUse)
#....
else:
	print(numberToUse)
# end if

print("----------------")

#	----------------
#	using a "switch-case"
#	----------------
def switchCase(number):
	case = {
		0:	"zero",
		1:	"one",
		2:	"two",
		3:	"tree",
		4:	"four"
	}

	return case.get(number, "unknown number")
# end function

print("Give me the result of 0: {}".format(switchCase(0)))
print("Give me the result of 4: {}".format(switchCase(4)))
print("Give me the result of 10: {}".format(switchCase(10)))
