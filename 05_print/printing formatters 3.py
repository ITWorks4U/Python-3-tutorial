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