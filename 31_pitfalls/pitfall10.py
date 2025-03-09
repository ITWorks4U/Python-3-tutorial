###
#	using a switch statement / match statement wrong
###

'''
	To handle multiple cases as once, these must be
	capsuled into brackets. But not separated by commatas,
	because the case collection is now a tuple.

	Therefore the single number 0..9 can't be matched with
	any tuple.
'''
for i in [0,1,2,3,4,5,6,7,8,9,(0,2,4,6,8),(1,3,5,7,9)]:
	match i:
		case (0,2,4,6,8):
			print(f'number {i} is even...')
		case (1,3,5,7,9):
			print(f'number {i} is odd...')
		case _:
			print(f'unknown what to do here with... {i}')
		#end cases
	#end match
#end for

'''
	Use "|" instead to separate the values isolated.
'''
for i in [0,1,2,3,4,5,6,7,8,9]:
	match i:
		case (0|2|4|6|8):
			print(f'number {i} is even...')
		case (1|3|5|7|9):
			print(f'number {i} is odd...')
		case _:
			print(f'unknown what to do here with... {i}')
		#end cases
	#end match
#end for
