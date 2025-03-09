###
#	removing an element from a collection while iterating
###

collection = [0,1,2,3,4,5]

for item in collection:
	if item == 2:
		collection.remove(item)
	else:
		print(item)
	#end if
#end for

'''
	expected result:	[0,1,3,4,5]
	gotten result:		[0,1,4,5]

	Because by collection.remove(item=2) the collection will
	be modified as well. So after the function call the collection
	already contains [0,1,3,4,5]. For the next iteration step the
	internal counter walks to the next position, where item 4 is
	located.
'''