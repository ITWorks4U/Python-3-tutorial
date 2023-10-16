#!/usr/bin/python3

"""
	using additional arguments
	from print function

	full offer of print() function:
	print(*values: object, sep: str | None = " ", end: str | None = "\n", file: SupportsWrite[str] | None = None, flush: Literal[False] = False) -> None

	where:
		-	*values	:=	any amount of arguments
		-	sep		:=	string inserted between values, space by default
		-	end		:=	text to print after print(), new line by default
		-	file	:=	a file-like object (stream); defaults to the current sys.stdout
		-	flush	:=	whether to forcibly flush the stream

	returns nothing

	video tutorial:	https://youtu.be/AK44C_uZ9u4
	timestamp:		00:38:15
"""

stringVal = "This is a simple text."

#	------------------
#	overriding end => no new line
#	for the next output
#	------------------
print(stringVal, end=' Bazinga!')
print("Is that on the new line?")

#	------------------
#	modifying separators
#	------------------
print("C", "C++", "Python", "C#", "Java", "...")
print("C", "C++", "Python", "C#", "Java", "...", sep="/")
print("C", "C++", "Python", "C#", "Java", "...", sep=" nonsense separator ")
#end for

#	------------------
#	print the output into a file instead
#	------------------
with open('outsourced.txt', encoding="utf-8", mode='w') as f:
	print("C", "C++", "Python", "C#", "Java", "...", file=f, end='')
#end with

#	------------------
#	flushing the output
#	------------------
from time import sleep

for i in range(10):
	'''
		if flush=True, then the previous output
		will be replaced with the new output

		\b tells the system to jump one position back
	'''
	print(f'{i}', end='\b', flush=True)
	sleep(0.5)
#end for