#	What does it main()?

-	acutally you've never used a main() before
-	by default, python don't use and don't need a "main()"
-	even a main() is defined, it won't be handled as a main() in other languages, like C, C++, C#, Java, ... => it's "just" a normal function, which can hold n instructions, but this is not going to call automatically
-	to define a "main", often called: "entry point", you have to use a condidtion check => fun fact: you also do not need that, but it looks more professional

###	How to define a "main()"

write:

```
if __name__ == '__main__':
	#code....

```

> __name__:
represents the file name, which shall be the current "main", when it's in use by the python interpreter