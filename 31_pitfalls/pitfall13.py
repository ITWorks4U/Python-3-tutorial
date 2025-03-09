###
#	handling with floating values won't give
#	you always a correct value to deal with...
###

'''
	wrong way:

	Since a floating point arithmetic operation
	doesn't comes with a clean rounded number,
	(0.3 * 3) + 0.1 => 0.9999999999...
	whereas 1.0 is expected.
'''
# a = (0.3 * 3) + 0.1
# b = 1.0

# print(f'a == b, right? => {a == b}')

'''
	correct way:

	this must be rounded with the math module

	optionally, >>a<< can be converted into a floating point
	value
'''
from math import ceil

a = float(ceil((0.3 * 3) + 0.1))
b = 1.0

print(f'a == b, right? => {a == b}')
