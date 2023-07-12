#!/usr/bin/python3

"""
	How to use functions in python, which were written
	in C. It contains simple function calls without
	typical C structures (not tested for macros, pointers, struct/union).
	C++ might work on the same way, but it's also not tested.

	Before you start make sure you've built your library first.
"""

from ctypes import c_double, c_int, CDLL

def squareMultiplication(list_in):
	"""calling C function: void squareMultiplication(int n, double *array_in, double *array_out);"""

	n = len(list_in)

	#	important: list_in must come with an asterisk, otherwise you'll get an error
	c_arr_in = (c_double * n)(*list_in)
	c_arr_out = (c_double * n)()

	python_c_square(c_int(n), c_arr_in, c_arr_out)
	return c_arr_out[:]
#end function

#	####	start	#####

#	full path must be used to load the library
#	depending on your system the abolute path may be:
#
#	Linux / possibly macOS as well: /home/......./c_library.dll
#	Windows (depending on your used drive) C:\\.......\\c_library.dll
libPath = '<your absolute path with the library here>'

try:
	#	loading the library
	basic_function_lib = CDLL(libPath)
	print('library found and sucessfully loaded...')

	#	-----------
	#	prints 'Hello' on your output
	#	-----------

	#	attempting to call the certain function -> might not be found on your IDE
	#	if so, then type your function to call by hand
	printHelloForPython = basic_function_lib.sayHelloFromC

	#	defining the resulting type of your function
	#	for void it's None
	printHelloForPython.restype = None

	#	calling the C function
	printHelloForPython()
	#	-----------

	#	-----------
	#	do a square multiplication with 1,000,000 elements
	#	-----------
	python_c_square = basic_function_lib.squareMultiplication
	python_c_square.restype = None
	squaredResult = squareMultiplication(range(1000000))

	for i, j in enumerate(squaredResult):
		print(f'{i}: {j}')
	#end for
	#	-----------
except Exception as e:
	print(f'error: {e.args}')
#end try