#	What kind of collections exists?

-	lists		(linear, unordered collection of multiple elements)
-	tuple		(unordered collection of fixed elements)
-	set			(linear, ordered collection of unique elements)
-	dictionary	(ordered collection of key-value-pairs, where the keys are ordered by default; the key is unique)

##	How to define a collection?

for lazy people:
-	use [] for a list
-	() for a tuple
-	{} for a DICTIONARY

What about a set? => {}, but in that case it won't be a set

###	How to define it correctly
assigning an instance of these collections to an object with the full collection name, like:

a = list()
b = tuple()
c = set()
d = dict()

It's much better to understand what kind of code is supposed for.
By the way, you _may_ also use ```list = list()```, but this is hard to read and understand.