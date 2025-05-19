
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
	-	match (switch in other languages)
	-	exception handling

	However, Python won't deal with both types
	in a single block. But you're welcome to use
	your own type of block space for each unique block.

	In summary:	Since you're using an indentation (spaces or tabs),
	you're still forced to use the same indentation type.
'''

#	tabs are used here only
def function1() -> int:
	#	here are tabs
	a = 5
	b = 99

	def sub_a(a,b) -> int:
		return a + b
	#end sub function

	return sub_a(a,b)
#end function

#	spaces are used here only
def function2() -> int:
    #   here are spaces
    a = 5
    b = 99

    def sub_a(a,b) -> int:
        return a + b
    #end sub function

    return sub_a(a,b)
#end function

message = f"""
	function1:	{function1()}
	function2:	{function2()}
"""

print(message)