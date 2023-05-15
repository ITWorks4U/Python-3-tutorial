#!/usr/bin/python3

"""
	File operations for with and without threading.

	Offers to write something into a file
	and also read from it.

	Attention: The file might have a size of
	up to 900 MB!

	Doesn't comes with exception handling!
"""

#	100,000,000
max_count = 100000000

#	1,000,000
million = 1000000

#	----------
#	writing the number range (0,1,...,99,999,999)
#	into file (fileName)
#	----------
def writeToFile(fileName: str) -> None:
	print(f'trying to write to file: {fileName}')

	with open(file=fileName, mode="w", encoding='utf-8') as f:
		#	repeat that 100,000,000 times
		for i in range(max_count):
			_ = f.write(str(i) + '\n')

			#	inform the user on each 1,000,000 steps
			if i % million == 0:
				print(f'step {i}')
			#end if
		#end for
	#end with

	print('Done with writing!')
#end function

#	----------
#	reading certain file (fileName)
#	----------
def readFromFile(fileName: str) -> None:
	print(f'trying to read from file: {fileName}')

	with open(file=fileName, mode='r', encoding='utf-8') as f:
		for i, line in enumerate(f, start=0):

			#	print each 1,000,000th line
			if i % million == 0:
				print(line)
			#end if
		#end for
	#end with

	print('Done with reading!')
#end function