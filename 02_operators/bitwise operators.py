#!/usr/bin/python3

"""
	bitwise operators are in use to
	compare each bit of the values each other
	to receive a new value

	also in use to move a numeric value by n bits
	left or right

	often used on low level programming, however,
	in that case it's much better to use C programming (:
"""

print("--- bitwise operations ---")

#	values to use
a = 10
b = 20

print(a & b)
print(a | b)
print(a ^ b)
print(~a)
print(a >> 4)
print(b << 4)

print("-------------------------------------")

a = 0b01001001													#	73
b = 0b00101010													#	42

print(a & b)
print(a | b)
print(a ^ b)
print(~a)
print(a >> 4)
print(b << 4)