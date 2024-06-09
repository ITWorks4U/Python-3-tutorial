#!/usr/bin/python3

"""
	contains objects, functions, ...
	for both systems
"""

#	----------
#	list of local drives
#	----------
localDrives = list()

#	----------
#	Minimal free space
#	for each directory, disk, etc.
#	----------
minFreeSpace = 0.15

#	----------
#	print separators
#	----------
def printSep(char: str ='-', additionalNewLine: bool = False) -> None:
	for _ in range(25):
		print(char, end='')
	#end for

	print()

	if additionalNewLine:
		print()
	#end if
#end function

#	----------
#	converting the system
#	size in bytes to a
#	human readable size
#	----------
def humanSize(size: int) -> str:
	KBYTES = float(1024)						#	1,024			bytes = 1KB
	MBYTES = (KBYTES ** 2)						#	1,048,576		bytes = 1MB
	GBYTES = (KBYTES ** 3)						#	1,073,741,824	bytes = 1GB
	TBYTES = (KBYTES ** 4)						#	1,099511628e12	bytes = 1TB

	if size < KBYTES:
		return "{0} {1}".format(size, "Bytes" if (size == 0 or size > 1) else "Byte")
	elif size >= KBYTES and size < MBYTES:
		return "{0:.2f} KB".format(size / KBYTES)
	elif size >= MBYTES and size < GBYTES:
		return "{0:.2f} MB".format(size / MBYTES)
	elif size >= GBYTES and size < TBYTES:
		return "{0:.2f} GB".format(size / GBYTES)
	#end if

	return "{0:.2f} TB".format(size / TBYTES)
#end function

#	----------
#	Determine free
#	space left.
#	----------
def onFreeSpace(total_size: int, space_left: int) -> bool:
	if total_size > 0:
		result = (space_left / total_size)

		#	printing as a human readable value
		print("{0:.2f}%)".format(result * 100))

		return (result >= minFreeSpace)
	#end if

	print("0%)")
	return False
#end function