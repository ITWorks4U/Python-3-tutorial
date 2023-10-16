#!/usr/bin/python3

#required for random colors
import random as r

'''
	Mastermind: Guess for colors, which are
	created randomly by the system.

	version 3:
		-	random colors by system
		-	using collections instead of multiple single objects
		-	using functions for more professional skill with
			the ability for a better code maintenance
		-	user enters four colors (can be different or multiple)
		-	analyzing each color on each possible position
		-	counting points for the correct color on the correct
			position and also the correct color on a wrong position
		-	unlike to version 2 since we're using real random colors,
			we also have no idea which colors are in use
		-	adding a loop to have 5 guesses
		-	finally, the correct collection will be printed at the
			end of the application

	video tutorial:	https://youtu.be/AK44C_uZ9u4
	not shown in the video
'''

#	holds four random colors
systemColors = list()

#	in use for random color selection,
#	where the number represents the random color
randomNumberCollection = (0,1,2,3,4,5,6,7)

#	number of guesses
guessCounter = 0

#	holds our four color guesses
guessCollectionUser = list()

#	Since you're using python version 10+, you can also
#	use the match key for a switch-case.
#
#	To make sure to play the game with a lower python 3
#	version, we're using the 'classic way'.
def createRandomColor(colorID: int) -> None:
	cs = {
		0: 'red',
		1: 'yellow',
		2: 'green',
		3: 'blue',
		4: 'orange',
		5: 'purple',
		6: 'black',
		7: 'white'
	}

	systemColors.append(cs.get(colorID))
#end function

#	using four 'real' random colors
for _ in range(4):
	createRandomColor(r.choice(randomNumberCollection))
#end for

#	defining collections and variables for the game, which
#	must be able to modify inside of analyzeGuesses() function
colorsDone = [False, False, False, False]
colorsGuesses = [False, False, False, False]

pointsForColorAndPosition = 0
pointsForColorsOnly = 0
alreadyGuessed = False

#	Analyzing the guesses.
#
#	In combination with two loops we're comparing
#	color i (system color) with color j (guessed color).
#	If true, then this color is marked as 'done'.
#
#	In the second stage we try to figure out if the
#	first color might be on position 2, 3, and/or 4.
#	Similar to the other colors.
def analyzeGuesses() -> None:
	global pointsForColorAndPosition
	global pointsForColorsOnly
	global alreadyGuessed

	#	step 1: check, if the system color on position i is equal to
	#			the color from input on position j
	for i in range(len(systemColors)):
		for j in range(len(guessCollectionUser)):

			#	also check, if this color has not already been
			#	guessed before
			onCheck = (
				systemColors[i] == guessCollectionUser[j] and
				not colorsDone[i] and not colorsGuesses[j]
			)

			if onCheck:
				pointsForColorAndPosition += 1
				colorsDone[i] = True
				colorsGuesses[j] = True
			#end if
		#end for
	#end for

	#	step 2:	check, which color might be on an another position instead
	for i in range(len(systemColors)):
		if not colorsDone[i]:
			for j in range(len(guessCollectionUser)):

				#	To avoid to handle the color on the same
				#	position (again). Since we know, that the color j on position i is identical,
				#	we will skip this step.
				if i == j:
					continue
				#end if

				#	we also check, if the current guessed color in combination with the
				#	next 
				onCheck = (
					not colorsGuesses[j] and guessCollectionUser[j] == systemColors[i] and
					not colorsDone[i] and not colorsGuesses[j]
				)

				if onCheck:
					pointsForColorsOnly += 1
					colorsDone[i] = True
					colorsGuesses[j] = True
				#end if
			#end for
		#end if
	#end for

	#	if we also have reached the maximum points for all (correct) colors,
	#	this flag will be set to true
	if pointsForColorAndPosition == 4 or pointsForColorsOnly == 4:
		alreadyGuessed = True
	#end if

	#	optional: printing the current state to the console
	print(f"correct color and position: {pointsForColorAndPosition}")
	print(f"correct colors only: {pointsForColorsOnly}")
#end function

#	main application
print('***Mastermind***')
print('Try to guess the correct colors. These colors are valid: red, yellow, green, blue, black, white, brown, magenta')
print('You have up to 5 guesses! Good luck!')

#	We're using up to 5 rounds to guess
#	the correct color combination.
for i in range(5):
	guessCounter += 1
	print(f'current guess: {guessCounter}')
	guessCollectionUser = input("enter four colors: ").split()
	print('Analyzing...')
	analyzeGuesses()

	#	"if alreadyGuessed:" works, too
	if alreadyGuessed == True:
		break
	#end if
#end for

#	finally, print the current combination
#	to the console
print()
print('********************')
print(f'These were the current colors: {systemColors}')
print('********************')
print()

print('Game over.')