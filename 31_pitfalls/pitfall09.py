###
#	using the wrong comparison
###
a = 'abc'
b = 'abc'.lower()

#	usually, a and b have an identical content, however,
#	these are also different

#	this compares, if the content of a and b are identical:
print(a == b)

#	however, this checks, if a and b are on the same memory address:
print(a is b)

###
#	summary
###

'''
	By using >>is<< this won't check the content of a and b. Even a and b
	have an identical content, the location of b differs to a, because
	lower() returns a new string, which is going to store to b.

	If a and b starts with an identical content, it doesn't matter
	what kind of types are in use, then the >>is<< operator returns true as well.
'''

###
#	hint:
###
#	receiving the location (memory address) for used object
#	that's the reference value for >>is<<
print(hex(id(a)))
print(hex(id(b)))
