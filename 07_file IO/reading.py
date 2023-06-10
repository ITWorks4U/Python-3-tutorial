#!/usr/bin/python3

"""
	Reading from a file.

	It works only, if the required
	file exists, you've granted access
	and this file is able to use,
	otherwise an error occurs.

	To read a file use open() function:
	open(file, mode, buffering, encoding, errors, newline, closefd, opener), where:
		-	file		:=	file to use
		-	mode		:=	how to use that file
			'r'	-	reading (default) <=> file must exist
			'w'	-	writing <=> truncates content of file, if
					exsiting, otherwise create a new file
			'x'	-	opening for exclusive creation;
					fails, if the file already exists
			'a'	-	appending content to a file, if exists,
					otherwise creating a new file and fill it with content
			't'	-	open in text mode (default)
			'b'	-	open in binary mode
			'+'	-	open a file for updating (reading and writing)
		-	buffering	:=	used for setting buffering policy
		-	encoding	:=	the encoding format (e. g. ASCII, UTF-7, UTF-8, ...)
		-	errors		:=	string specifying how to handle encoding/decoding errors
		-	newline		:=	how newlines mode works (available values: None, ' ', '\n', 'r', and '\r\n')
		-	closefd		:=	True by default; if not given, an exception will be raised
		-	opener		:=	a custom opener; must return an open file descriptor

	you're also welcome to use one of its
	overloaded functions, too

	see also: https://www.programiz.com/python-programming/methods/built-in/open
"""
#	---------------
#	first option to read a file:
#	---------------
source = open("lorem_ipsum.txt", "r")

#	print line by line
for line in source:
	print(line)
#end for

#	closes the file stream
source.close()
print("Source is closed? ", source.closed)
print("---------------")

#	---------------
#	second option to
#	read a file
#	---------------
source = open("lorem_ipsum.txt", mode="r", encoding="ascii")

#	using read() function instead
print(source.read())
source.close()
print("Source is closed? ", source.closed)
print("---------------")

#	---------------
#	third option to
#	read a file:
#	---------------
#	using with command => automatically closes the
#	file stream after completing with your operations
with open("lorem_ipsum.txt", "r") as source:
	print(source.read())
# end with
print("Source is closed? ", source.closed)