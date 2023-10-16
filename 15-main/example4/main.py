#!usr/bin/python3

"""
	Using a main function in python.

	Like in other programming languages
	the main() represents the
	starting section, however, in Python
	there's no main by default required
	or given.

	In this example, this python script
	has the "main()" and accesses to
	the other modules (python scripts).

	video tutorial:	https://youtu.be/AK44C_uZ9u4
	timestamp:		02:57:37
"""

#	required to use the functions
#	and classes
import classes as cl
import functions as func

#	-----------
#	"main()"
#	-----------
def main():
	#	-----------
	#	using functions
	#	-----------
	func.Function()
	func.F()

	b = 'b'
	r = 'r'
	func.Goes(b,r,r,r,r)

	#	-----------
	#	using classes
	#	-----------
	s = cl.Simple()
	print(f'{s.Display()}')

	print(f'{cl.Food.Apple}')
	func.printFood(cl.Food.Banana)

	#	-----------
	#	prints type of enumeration
	#	-----------
	f = cl.E
	print(f)
	#	-----------
#end function

#	-----------
#	forced entry point
#
#	usually comes at the end
#	of a script to make sure,
#	that the called function(s)
#	has been detected before
#	-----------
if __name__ == '__main__':
	main()
#end if