#	Looping code

-	very often to repeat an instruction again and again until a condition is no longer given
-	often in combination with additional condition checks

##	different ways to looping
-	iterations (for, while)
-	recursion (you won't be happy, if you don't mind)
-	goto (basicly it's not possible to use it in Python, but with additional package(s) it's also possible)

##	how to skip or leave a loop
-	continue <=> continue your loop with the next possible step without care about the current step
-	break <=> leave your loop immediately

###	attention
-	condition checks (also for loops, functions and classes) must have an indentation (white space OR tabs only)
-	do __NOT__ merge your python code with both intendentions, it's a syntax error (it seems since Python 3.10+ it's now allowed, but not tested)
-	be careful, which code is a part of a condition check (also for a loop, a function or a class); means: every code, which has the same indentation like the last code above, is automatically a part of this condition, loop, etc.
-	every special block of code (condition, loop, etc.) must have at least a code; it's a syntax error, if this field is empty; even a commentary as a dummy holder is also not valid; if an implementation is in further use, then use the keyword: pass or use a muliline commentary block
-	if you're not sure about the indentations in your code, then you can activate the white spaces, depending on the editor you're using
-	hint: it's not required, but for a better design and reading, mark your indentation at the end with an commentary, like: #end if, #end for or else