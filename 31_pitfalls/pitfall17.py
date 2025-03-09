###
#	calling a function before this function is defined
###

'''
	Since python is written in C, the behavior is rather different than in C itself.
	In C you can call a function earlier, than its definition, like:

	test();

	void test(void) {
		//	...
	}

	The compiler gives you a warning and automatically assumes, that the function call
	might be an integer function without parameters.

	However, this won't work in Python.
'''

function()

def function():
	print()
	#...
#end function
