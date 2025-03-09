###
#	appending a collection to itself...
###

'''
	What happens, if a collection shall be append or extend itself?
	This is only possible for lists. It's unable for a tuple, set and dictionary.

	A tuple has no options to add or remove elements.
	A set comes with "add()", but adding itself is unhashable, thus you'll get a TypeError.
	A dictionary comes with "update()" to add a sub dictionary, but it can't add itself
	multiple times. If a dictionary already contains a sub dictionary, then nothing happens.

	for a list only:
		Theoretically an infinite recursion would occour, but Python has
		a fallback for that stupid kind of pitfall.

		You'll see "[...]" as a mark for: "Bro, why are you so stupid? Don't do this."
'''

# collection = list()
# collection = tuple()
# collection = set()
collection = dict()
print(collection)

for _ in range(10):
	if isinstance(collection, list):
		#	list only
		collection.append(collection)
	elif isinstance(collection, set):
		#	set only => raises a TypeError
		collection.add(collection)
	elif isinstance(collection, dict):
		#	dictionary only
		collection[0] = 'a'
		collection.update(collection)
	else:
		#	fur tuple only
		print(f'unable to modify a tuple...')
	#end if

	print(f'elements in collection = {len(collection)} => {collection}')
#end for

