#	Purpose

usually, when a certain condition case is going to use, you had to use multiple if-elif-else blocks
like in other programming languages it's much better to have cases to work with, when a certain condition is satisfied
usually, Python didn't came with a normal way for switch-case

###	Python <= 3.9

use a combination of a function and a dictionary

###	Python >= 3.10

use match (other languages: switch) followed by case (other languages: case)
unlike to other languages:
-	there's no __break__ in your code
-	by comparing multiple cases for one purpose, use a single "or" => |
-	the default case is just: >>case _<<