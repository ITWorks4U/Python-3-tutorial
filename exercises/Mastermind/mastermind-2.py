#!/usr/bin/python3

'''
	Mastermind: Guess for colors, which are
	created randomly by the system.

	version 2:
		-	still fixed colors
		-	user enters four colors (can be different or multiple)
		-	analyzing first input with first color; if this doesn't
			match, then check the first color with the second, third
			and fourth color(s) instead; similar to the other colors
		-	counting points for the correct color on the correct
			position and also the correct color on a wrong position
		-	unlike to version 1 we don't get an information, if the
			first color on the first position is correct or not,
			which makes the game harder for us
		-	runs the application once only

	video tutorial:	https://youtu.be/AK44C_uZ9u4
	timestamp:		01:22:40
'''

#	"random" colors
c1 = 'red'
c2 = 'green'
c3 = 'blue'
c4 = 'yellow'

#	the correct color on the correct position
pointsForColorAndPosition = 0

#	the correct color on a wrong position
pointsForColorsOnly = 0

#	determines, which system color has already
#	been handled and which not
doneC1 = False
doneC2 = False
doneC3 = False
doneC4 = False

#	same for user guess
doneG1 = False
doneG2 = False
doneG3 = False
doneG4 = False

print('***Mastermind***')
print('Try to guess the correct colors. These colors are valid: red, yellow, green, blue, black, white, brown, magenta')

#	entering four colors, separated by a space
colors = input("enter four colors: ").split()
color1 = colors[0]
color2 = colors[1]
color3 = colors[2]
color4 = colors[3]

print('Analyzing...')

#	First check, if the first color is
#	on the first position. Similar for
#	color 2 on the second position etc.
#
#	If true, pointsForColorAndPosition is
#	raised by 1.
if color1 == c1:
	pointsForColorAndPosition += 1
	doneC1 = True
	doneG1 = True
#end if

if color2 == c2:
	pointsForColorAndPosition += 1
	doneC2 = True
	doneG2 = True
#end if

if color3 == c3:
	pointsForColorAndPosition += 1
	doneC3 = True
	doneG3 = True
#end if

if color4 == c4:
	pointsForColorAndPosition += 1
	doneC4 = True
	doneG4 = True
#end if

#	Second check, if the first color is
#	not on the first position, but maybe
#	on the second, third and/or fourth
#	position.
#
#	for the other colors, we're checking:
#		second color: position 1, 3, 4
#		third color: position 1, 2, 4
#		fourth color: position 1, 2, 3
#
#	If true, pointsForColorsOnly is raised
#	by one.
if not doneC1:
	if not doneG2 and color1 == c2:
		pointsForColorsOnly += 1
		doneC1 = True
		doneG2 = True
	#end if

	if not doneG3 and c1 == color3:
		pointsForColorsOnly += 1
		doneC1 = True
		doneG3 = True
	#end if
	
	if not doneG4 and c1 == color4:
		pointsForColorsOnly += 1
		doneC1 = True
		doneG4 = True
	#end if
#end if

if not doneC2:
	if not doneG1 and c2 == color1:
		pointsForColorsOnly += 1
		doneC2 = True
		doneG1 = True
	#end if
	
	if not doneG3 and c2 == color3:
		pointsForColorsOnly += 1
		doneC2 = True
		doneG3 = True
	#end if
	
	if not doneG4 and c2 == color4:
		pointsForColorsOnly += 1
		doneC2 = True
		doneG4 = True
	#end if
#end if

if not doneC3:
	if not doneG1 and c3 == color1:
		pointsForColorsOnly += 1
		doneC3 = True
		doneG1 = True
	#end if
	
	if not doneG2 and c3 == color2:
		pointsForColorsOnly += 1
		doneC3 = True
		doneG2 = True
	#end if
	
	if not doneG4 and c3 == color4:
		pointsForColorsOnly += 1
		doneC3 = True
		doneG4 = True
	#end if
#end if

if not doneC4:
	if not doneG1 and c4 == color1:
		pointsForColorsOnly += 1
		doneC4 = True
		doneG1 = True
	#end if
	
	if not doneG2 and c4 == color2:
		pointsForColorsOnly += 1
		doneC4 = True
		doneG2 = True
	#end if
	
	if not doneG3 and c4 == color3:
		pointsForColorsOnly += 1
		doneC4 = True
		doneG3 = True
	#end if
#end if

#	summary
if pointsForColorAndPosition == 4:
	print(f"Impressive. You've guessed the correct colors and their positions!")
else:
	print(f"correct color and position: {pointsForColorAndPosition}")
	print(f"correct colors only: {pointsForColorsOnly}")
#end if

print('Game over.')