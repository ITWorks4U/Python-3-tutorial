#!/usr/bin/python3

'''
	Mastermind: Guess for colors, which are
	created randomly by the system.

	version 1:
		-	fixed colors
		-	user enters four colors (can be different or multiple)
		-	analyzing first input with first color only, similar to
			second color with second input etc.
		-	count the points at the end of the application
		-	runs the application once only
'''

#	"random" colors
c1 = 'red'
c2 = 'green'
c3 = 'blue'
c4 = 'yellow'
points = 0

print('***Mastermind***')
print('Try to guess the correct colors. These colors are valid: red, yellow, green, blue, black, white, brown, magenta')

#	entering four colors, separated by a space
colors = input("enter four colors: ").split()
color1 = colors[0]
color2 = colors[1]
color3 = colors[2]
color4 = colors[3]

print('Analyzing...')
if color1 == c1:
	points += 1
	print('First color guess is correct!')						#	:o)
else:
	print('First color guess is incorrect!')					#	:o(
#end if

if color2 == c2:
	points += 1
	print('Second color guess is correct!')
else:
	print('Second color guess is incorrect!')
#end if

if color3 == c3:
	points += 1
	print('Third color guess is correct!')
else:
	print('Third color guess is incorrect!')
#end if

if color4 == c4:
	points += 1
	print('Fourth color guess is correct!')
else:
	print('Fourth color guess is incorrect!')
#end if

#	summary
if points == 4:
	print("Impressive. You've guessed the correct combination!")
#end if

print('Game over.')