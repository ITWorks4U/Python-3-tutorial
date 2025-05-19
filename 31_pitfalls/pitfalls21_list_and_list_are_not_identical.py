###
#	Assuming, that list() and [] is identical.
###

'''
	A list, tuple, set or dictionary allows you to work with
	a collection and it's advantages. However, the kind of
	usage may also differ.

	By using a list you can use list() or []. Since the next
	work is simple, e. g. "adding an element", "remove something", ...
	both types are the same.

	Unless you're initializing an another collection to your
	collection.
'''

list0 = list()
list1 = []

summary = f'''
	#elements list0:
	{len(list0)}

	elements:
	{list0}

	#elemens list1:
	{len(list1)}

	elements:
	{list1}
'''

print(summary)

###
#	------------------------
###

#NOTE:	It doesn't matter what kind of sub
#		collection you're using.
collection = {0,1,2,3,4,5,6,7,8,9}

list2 = list(collection)
list3 = [collection]

summary = f'''
	#elements list2:
	{len(list2)}

	elements:
	{list2}

	#elemens list3:
	{len(list3)}

	elements:
	{list3}
'''

print(summary)