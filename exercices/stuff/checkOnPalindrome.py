#!/usr/bin/python3

'''
	Checking, if a word is a palindrome.
	A word is a palindrome only, if it can be
	read from left to right and also from
	right to left.
'''

buffer = input('enter a word, which might be a palindrome: ')

#	assuming, that a palindrome is already given
onPalindrome = True

#	--------------
#	if the buffer has 0 or 1 character(s),
#	then it's already a palindrome
#	--------------
if len(buffer) > 1:
	#	--------------
	#	limit to work with
	#	--------------
	limit = 0

	if len(buffer) % 2 == 0:
		#	the word has an even number of characters
		limit = len(buffer) // 2
	else:
		#	otherwise the given word has an odd number of characters
		limit = (len(buffer) - 1) // 2
	#end if

	#	--------------
	#	checking on palindrome
	#	--------------
	posLeft = 0
	posRight = len(buffer) - 1

	#	--------------
	#	continuing checking, until a palindrome is not given
	#	or the limit has been reached from right
	#	--------------
	while True:
		lChar = buffer[posLeft]
		rChar = buffer[posRight]

		#	check, if these characters are unequal
		if lChar != rChar:
			onPalindrome = False
			break
		#end if

		if posRight == limit:
			#	leaving loop
			break
		else:
			posLeft += 1
			posRight -= 1
		#end if
	#end while
#end if

#	--------------
#	summary
#	--------------
print(f'Is your given input "{buffer}" a palindrome?: {onPalindrome}')