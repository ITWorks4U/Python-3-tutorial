
###
#	basic pitfall:	using space and tab in one block
###

'''
	Python allows you to use space(s) and tab(s) to
	define a block of instructions. This may be:
	-	functions
	-	class
	-	loops
	-	conditions
	-	switch => match
	-	exception handling

	However, Python won't deal with both types
	in a single block. But you're welcome to use
	for each single block your own type of block space.
'''

def function() -> None:
	#	here are tabs
	a = 5
	b = 99

	#...
#end function

def function2() -> None:
    #   here are spaces
    a = 5
    b = 99

    #...
#end function

function()
function2()
