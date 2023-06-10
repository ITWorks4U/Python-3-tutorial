#!/usr/bin/python3

"""
	Since you're using python in version 10 or higher,
	you're also able to use a 'real' switch-case: match
"""

#	----------------
#	using a "switch-case"
#	----------------
def switchCase(number):
	match number:
		case 0:
			return 'zero'
		case 1:
			return 'one'
		case 4:
			return 'four'
		#... and so on

		# default block
		case _:
			return 'unknown number'
		#end cases
	#end match
# end function

print("Give me the result of 0: {}".format(switchCase(0)))
print("Give me the result of 4: {}".format(switchCase(4)))
print("Give me the result of 10: {}".format(switchCase(10)))