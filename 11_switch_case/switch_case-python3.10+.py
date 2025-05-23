#!/usr/bin/python3

"""
	Since you're using python in version 3.10 or higher,
	you're also able to use a 'real' switch-case: match

	video tutorial:	https://youtu.be/AK44C_uZ9u4
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

#	----------------
#	using multiple cases
#	----------------
def switchCase2(number):
	match number:
		case 0 | 1:
			return "0 or 1 returned here"
		case 2:
			return "2 only"
		#...

		#end cases
	#end match
#end function

print(f'again: {switchCase2(0)}')
print(f'again: {switchCase2(1)}')
print(f'again: {switchCase2(2)}')
print(f'again: {switchCase2(9)}')