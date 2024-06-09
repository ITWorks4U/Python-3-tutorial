##	Purpose

very often in use for pseudo random numbers => not a "real" randomizing operation

###	basics
-	import the random module
-	use the function random() to receive a "random" number between [0, 1) => the lowest number is 0, whereas 1 is the highest possible value

-	by default, you're using __random.random()__, which looks odd and makes you cry => use an alias to work smarter, like

```
	import random as r
	r.random()
```

fun fact, other functions, like signal.signal() are also like pain in the a**

###	examples

-	lottery (available here and also available under execises/stuff folder)
-	password generator (available under 14_strings)
-	for games (like yathzee, or Mastermind => take a look to the Mastermind folder => execises/Mastermind)