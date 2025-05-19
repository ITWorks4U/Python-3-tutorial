###
#	call expression in class properties, functions, ...
###

'''
	It makes no sense to use a call expression behind a class property,
	a function / class method, etc.

	Perhaps you tested something and forgot to undo your last change.
	Well, python may gives you a warning, and usually nothing happens
	on runtime, however, this can also have a nasty undefined behavior.
'''

class Test():
	def __init__(self, data: int = 0) -> None:
		self.__data: int = data
	#end constructor

	#NOTE:	Don't do this.
	@property
	def Data(self) -> int('123'):
		return self.__data
	#end property
#end class

t = Test()
print(f'{t.Data}')

t1 = Test(500)
print(f'{t1.Data}')

t2 = Test('abc')
print(f'{t2.Data}')
