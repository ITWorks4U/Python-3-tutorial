#!/usr/bin/python3

import random as r
import signal as s

'''
	Mastermind: Guess for colors, which are
	created randomly by the system.

	version 4:
		-	using a class
		-	handling signal
		-	using multiline strings
		-	fixing logic error on color analyzing

	video tutorial:	https://youtu.be/AK44C_uZ9u4
	not shown in the video
'''

class MasterMind():
	def __init__(self) -> None:
		"""
			Initialize a new instance of the game mastermind.
		"""

		#	private objects
		self.__systemColors = list()
		self.__randomNumberCollection = (0,1,2,3,4,5,6,7)
		self.__guessCounter = 0
		self.__guessCollectionUser = list()
		self.__stopGame = False
		self.__colorCollection = ('red', 'yellow', 'green', 'blue', 'orange', 'purple', 'black', 'white')

		#	public objects
		self.alreadyGuessed = False
		self.colorsDone = [False, False, False, False]
		self.colorsGuesses = [False, False, False, False]
		self.pointsForColorAndPosition = 0
		self.pointsForColorsOnly = 0

		for _ in range(4):
			self.__createRandomColor(r.choice(self.__randomNumberCollection))
		#end for
	#end constructor

	def __createRandomColor(self, colorID: int) -> None:
		"""
			On start four colors are selected
			randomly, thus you don't know,
			which colors are in use.
		"""
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

		self.__systemColors.append(cs.get(colorID))
	#end method

	def __analyzeGuesses(self) -> None:
		"""
			Analyzing the four colors and try
			to figure out, which one of these
			colors are on the correct position
			and also exist.
		"""
		for i in range(len(self.__systemColors)):
			for j in range(len(self.__guessCollectionUser)):

				#	if the current color has not been guessed yet
				onCheck = (
					self.__systemColors[i] == self.__guessCollectionUser[j] and
					not self.colorsDone[i] and not self.colorsGuesses[j]
				)

				if onCheck:
					self.pointsForColorAndPosition += 1
					self.colorsDone[i] = True
					self.colorsGuesses[j] = True
				#end if
			#end for
		#end for

		for i in range(len(self.__systemColors)):
			if not self.colorsDone[i]:
				for j in range(len(self.__guessCollectionUser)):
					if i == j:
						continue
					#end if

					onCheck = (
						not self.colorsGuesses[j] and self.__guessCollectionUser[j] == self.__systemColors[i] and
						not self.colorsDone[i] and not self.colorsGuesses[j]
					)

					if onCheck:
						self.pointsForColorsOnly += 1
						self.colorsDone[i] = True
						self.colorsGuesses[j] = True
					#end if
				#end for
			#end if
		#end for

		if self.pointsForColorAndPosition == 4 or self.pointsForColorsOnly == 4:
			self.alreadyGuessed = True
		#end if
	#end method

	def __onCorrectLength(self) -> bool:
		"""
			Make sure, that we have exactly 4 elements
		"""
		return len(self.__guessCollectionUser) == 4
	#end method

	def __checkInput(self) -> None:
		"""
			Check, if the four elements are located in
			the defined color collection. If not, then
			the game ends earlier.
		"""
		for color in self.__guessCollectionUser:
			if color not in self.__colorCollection:
				self.__stopGame = True
			#end if
		#end for

		if self.__stopGame:
			print('ERROR: No four colors have been typed in or the colors were wrongly typed in... Exiting game.')
		#end if
	#end method

	def startGame(self):
		"""
			Starting the game.
		"""
		for _ in range(5):
			self.__guessCounter += 1
			print(f'current guess: {self.__guessCounter}')
			
			self.__guessCollectionUser = input("enter four colors: ").split()

			if not self.__onCorrectLength():
				print('ERROR: There are no four colors detected. Exiting game...')
				self.__stopGame = True
			#end if

			self.__checkInput()

			if self.alreadyGuessed or self.__stopGame:
				break
			#end if

			print('Analyzing...')
			self.__analyzeGuesses()

			print(f'current correct guesses: {self.pointsForColorAndPosition}, correct color: {self.pointsForColorsOnly}')
		#end for
	#end method

	def printSummary(self) -> str:
		return f"""
********************
These were the current colors: {self.__systemColors}
********************
"""
	#end method

	#	if Ctrl + C (^C) has been pressed,
	#	the game ends earlier with exit code 0
	def registerSignals(self, signal, frame):
		self.__stopGame = True
	#end function
#end class

def main():
	title = f"""***Mastermind***
These colors are valid: red, yellow, green, blue, black, white, brown, magenta
Entering four colors separated by a space bar to try to figure out which colors are in use.
You have up to 5 guesses! Good luck!
"""
	print(title)

	#	new instance for the game
	m = MasterMind()

	#	registering signal
	s.signal(signalnum=s.SIGINT, handler=m.registerSignals)

	#	starting the game
	m.startGame()

	#	only, if you still have no idea which colors
	#	has been chosen
	if not m.alreadyGuessed:
		print(m.printSummary())
	#end if

	del m
#end main

if __name__ == '__main__':
	main()
	print('Game over.')
#end entry point