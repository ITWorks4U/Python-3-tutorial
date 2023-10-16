#!/usr/bin/python3

"""
	Writing anything into a file.

	It works only, if you've granted
	access to the path / file and if
	no error occurred before.

	first step: opening a file stream with
	write, appending or updating option

	second step: writing into the file

	last step: closing the file stream

	To write something into a file, use:
	write(__s: str) -> int <=> returns the number of written bytes
	writelines(__lines: Iterable[str], /) -> None

	video tutorial:	https://youtu.be/AK44C_uZ9u4
	timestamp:		01:51:01
"""
#	---------------
#	default way for writing
#	---------------
destination = open(file="result.txt", mode="w", encoding="utf-8")
_ = destination.write("This is a simple text!")
_ = destination.write("\n")
destination.writelines(["a,b,c,1,2,3,:-)"])
_ = destination.write("\n")
destination.close()

#	---------------
#	second option to write
#	to a file:
#	---------------
with open("result.txt", "a") as destination:
	destination.writelines([str(i) for i in range(10)])
	_ = destination.write("\n")
# end with

#	---------------
#	third way (unusual way, but possible, too)
#	uses the print function instead
#	---------------
with open('result.txt', encoding="utf-7", mode='a') as destination:
	print("C", "C++", "Python", "C#", "Java", "...", file=destination, end='')
	_ = destination.write("\n")
#end with

#	---------------
#	using binary form
#	attention: binary form won't accepting an encoding format
#	---------------
someBytes = b'\xC3\xA9'
with open('result.dat', mode='+ab') as destination:
	destination.write(someBytes)
#end with