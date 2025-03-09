###
#	handling a collection of exceptions in the wrong way
###

collection = [0,1,2,3,4]

'''
	wrong:
'''
# try:
# 	argument = collection[6]
# except ValueError, IndexError as e:
# 	print(f'exception type: {type(e)} <=> {e.args}')
# #end try

'''
	correct:

	A bunch of exceptions shall be capsuled into normal brackets only.
	If you use: [] or {}, then an another unhandled exception will be
	raised with: "catching classes that do not inherit from BaseException is not allowed"

	Funny, right? ;-)
'''
try:
	argument = collection[6]
except (ValueError, IndexError) as e:
	print(f'exception type: {type(e)} <=> {e.args}')
#end try
