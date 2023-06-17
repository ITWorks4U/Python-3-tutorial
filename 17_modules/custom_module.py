#!/usr/bin/python3

"""
	using custom modules in python
"""

class Simple:
	def __init__(self, arg = list()):
		self.__content = arg
	#end constructor

	def showContentType(self) -> str:
		return f'You got: {self.__content}, which is a type of {type(self.__content)}'
	#end method

	"""
		any other methods here...
	"""
#end class

class AnotherClass:
	pass
# end class

"""
	using functions...
"""
def Meme(a,b,c,d,e,f) -> None:
	print(f'This function goes {a}{b}{c}{d}{e}{f}!')
#end function

"""
	or use some "constants", where in
	python no constants really exists yet
"""
answerOfEverything = 42
bestNumberOfAllTime = "1001001"