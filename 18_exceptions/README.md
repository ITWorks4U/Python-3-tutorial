#	That was not supposed!

Mistakes happens. Often not intended, but sometimes these are on purpose.
Imagine, you're reading from the keyboard or from a file and want to interprete the current word as an integer.
Usually, you're using ```int(string_expression)``` to convert it into a correct type, however, when your __string_expression__ is not covered by numeric characters [0-9], then an error is going to raise. => By the way, use regular expressions (see #25) to handle such cases much more smarter.

###	How to handle

```
try:
	# code you might think, that this could or will cause an error => often called: CRITICAL AREA
except [Exception [as e]]:
	#	catching your (specific) exception and receive a detailed error, if given, to see, what realyl happend
finally:
	#	always executing code; no matter, if an exception has been raised before or not => this is the last instruction of your block
```

in some cases you might also see this:
```
try:
	#...
except:
	#...
else:
	#	code, which executes only, if no exception has been raised
```
Well, __this__ is also able to use, but it's deprecated. Since you can cover all instructions in your critical area, there's no more need to use an __else__ statement.

###	An exception is like an interrupt, right?

Yes, but acutally no. An occurred exception can similar be used like an interrupt, but these are __NOT__ the same. => Take a look to #19 for __signal handling__.