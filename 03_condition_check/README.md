#	Condition checks

Condition checks allows you to compare one, two or more values to each other.
Everytime a condition check returns true a certain block of code(s) is able to execute.

##	(very) important things

- condition checks (also for loops, functions and classes) must have an indentation (white space OR tabs only
- do NOT merge your python code with both intendentions, it's a syntax error (it seems since Python 3.10+ it's now allowed, but not tested)
- be careful, which code is a part of a condition check (also for a loop, a function or a class); means: every code, which has the same indentation like the last code above, is automatically a part of this condition, loop, etc.
- every special block of code (condition, loop, etc.) must have at least a code; it's a syntax error, if this field is empty; even a commentary as a dummy holder is also not valid; if an implementation is in further use, then use the keyword: pass or use a muliline commentary bloc
- if you're not sure about the indentations in your code, then you can activate the white spaces, depending on the editor you're usin
- hint: it's not required, but for a better design and reading, mark your indentation at the end with an commentary, like: #end if, #end for or else

##	How to use condition checks wrong:

As mentioned before it's easy to use the wrong kind of condition checks.

example:
	a == b means:	if the values of a and b are equal

often wrongly interpreted:
-	a and b means:	if the values of a and b differs to zero
-	a is b means:	if a and b refers to the identical object
-	a & b means:	the binary expression (0, 1) of a and b are
					compared to each other and returns
					a new value

					a:	00001010 (10)
					b:	00010100 (20)

					a & b:
						00000000 (0)