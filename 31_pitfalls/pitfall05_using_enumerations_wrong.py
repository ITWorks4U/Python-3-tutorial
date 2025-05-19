###
#	wrong usage of enumerations
###

'''
	An enumeration class can't be instanciated like
	a normal class. You have to use enum_class.propery.

	By using name, you'll get the property name,
	whereas by using value, you'll get the property value.
'''
from enum import Enum

class Fruits(Enum):
	Apple = 0
	Pinapple = 1
	Cherry = 2
	Banana = 3
#end enum

# f = Fruits()
# print(f.Apple.value())

print(Fruits.Apple.name)
print(Fruits.Apple.value)
