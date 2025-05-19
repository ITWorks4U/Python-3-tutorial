###
#	Do a little mistake, which may cause a huge problem.
###

'''
	In OOP it's really important how to define a class
	and their class variables, too.

	Test_0, Test_1 comes with a collection of type list.
	Since both classes are different, their behavior is also different.
'''
from timeit import timeit
from datetime import timedelta

###
#	definition of constants
###
__MAX_OUTER = 50
__MAX_INNER = 100

###
#	definition of both classes
###

class Test_0():
	class_list = list()
#end class

class Test_1():
	def __init__(self):
		self.class_list = list()
	#end constructor
#end class

###
#	function usage
###
def function_0() -> None:
	for _ in range(__MAX_OUTER):
		#NOTE:
		#	Since t is going to "initialize" on each loop,
		#	don't think that the collection will also be
		#	cleared during runtime! The Python interpreter
		#	still uses the already existing collection and
		#	the next elements can still be append, whereas
		#	the previous data elements still exist!
		#
		#	Best way to avoid this pitfall:
		#	- use __init__ (like Test_1)
		#	- use a "destructor" (__del__) to clean up the mess
		t = Test_0()

		for i in range(__MAX_INNER):
			t.class_list.append(i)
		#end for

		# print(f"t.class_list contains: {t.class_list}")

		#	By the way, don't think to delete object t to assume,
		#	that t will be fully created on the next turn.
		#	Your list still exists. Perhaps your class instance, too.
		#
		#	The Python interpreter might also ingnore that command.
		# del t
	#end for
#end function

def function_1() -> None:
	for _ in range(__MAX_OUTER):
		#NOTE:	In contrast to Test_0, Test 1 comes with the __init__ instruction ("constructor").
		#		This forces the Python interpreter to create a new empty list to work with.
		#		However, your instance t might still exist during runtime!
		t = Test_1()

		for i in range(__MAX_INNER):
			t.class_list.append(i)
		#end for

		# print(f"t.class_list contains: {t.class_list}")
	#end for
#end function

if __name__ == "__main__":
	collection_0 = list()
	collection_1 = list()

	#	Bonus content:
	#	How long is the least and most time amount? This might be different
	#	on your local machine.
	for i in range(500):
		collection_0.append(timedelta(seconds=timeit(function_0, number=1)))
		collection_1.append(timedelta(seconds=timeit(function_1, number=1)))
	#end for

	summary = f"""
	.:collection_0:.

	highest time amount:	{max(collection_0)}
	least time amount:	{min(collection_0)}

	.:collection_1:.

	highest time amount:	{max(collection_1)}
	least time amount:	{min(collection_1)}
	"""

	print(summary)
#end entry point
