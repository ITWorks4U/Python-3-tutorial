#	How to read from a file or write it from?

in both cases just use open() function

##	important things
-	by default a file is going to read => this can be managed by the "mode" argument
-	when you're using a stream (file stream, network stream, ...) YOU have to make sure to use the resource at the correct time, so it you don't longer need a resource YOU have to release this resource, otherwise it might result to undefined behaviors
-	make sure you're able to access to your file to write to or read from => if the file is corrupted, you don't have access to the file, it does not exist, ... an error on runtime will appear
-	in case of an error your resource IS NOT RELEASED by default

###	writing to a file

example:
```
fc = open(fileName, mode='w')

''' do operations here '''

fc.close()
```

###	reading from a file

example:
```
fc = open(fileName, mode='r')

'''	do operations here	'''

fc.close()
```

###	How to use it smarter?

-	in contrast to the default way, where YOU have to close the resource, you can also let do this from the system automatically

```
with open(fileName, mode=...) as fc
	'''	your operations here '''

```

-	by using >>with<< a temporary resource is in use
-	when the block has been left, the resource is also automatically released
-	also very useful in case of an error