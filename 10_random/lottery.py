#!/usr/bin/python3

'''
	Playing lottery.

	6 unique numbers of 49 available numbers can be chosen
	for a lottery game.

	Finally, a super number in the range of 0-9 can
	also be used.

	Have fun. (:
'''

import random as rnd

initCollection = list()

#	--------------
#	generating lottery numbers 1-49
#	--------------
for i in range(49):
	initCollection.append(i+1)
#end for

#	--------------
#	taking 6 unique numbers
#	--------------
lottery = list()

while len(lottery) != 6:
	current = rnd.choice(initCollection)

	if current not in lottery:
		lottery.append(current)

		#	the alternate way is to remove
		#	the number from initCollection,
		#	thus it's no need to check, if
		#	the current number is not already
		#	in lottery list
	#end if
#end while

#	--------------
#	also adding a super number at the end
#	--------------
superNumber = list()
for i in range(10):
	superNumber.append(i)
#end for

#	--------------
#	output
#	--------------
print(f'current lottery numbers: {lottery} with super number: {rnd.choice(superNumber)}')