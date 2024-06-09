#	Welcome to python (3) programming!

Python (3) is really easy to learn. It allows you to start
with programming without any knowledge.

Python is an interpreter language, means, you don't have
to do any datatype definitions. Every variable, here an object,
can easy be defined and also reinterpreted by any other value.

##	However, there are >some< points to know:

-	by using blocks, see conditions, loops, functions, ... it's required
	to know, which command/s is/are part of the block
-	in contrast to any other language, it's neccessary to know
	which kind of indention you're using; there're two of them:
-	using space bar(s)
-	using tab(s)

	because Python won't agree a mix of both, you must use one of them
	hint: you also can display whitespace(s) and tab(s)
	(any editor): view -> display whitespaces (or similar expression)

##	commentaries

-	commentaries allows you to documenting your code or reading foreign code to understand that
-	commentaries aren't in use for the interpreter

####	There're two kinds of commentaries:
-	single line commentaries allows you to comment anything in >>this<< lines	=>	starting with '#'
-	multiple lines allows you to comment multiple lines	=>	use ''' comment ''' or """ comment """
-	for multiple commentaries it's required to use the identical characters, otherwise on runtime you'll see your error(s)

##	Which python version is in use in this tutorial?

Python 3.10

##	Why is it important to know the difference between Python / Python 3?

Basicly, there's a difference between Python and Python 3: "How to use the correct interpreter!"
Some python code can still be written with Python 2.7. A (very) old version, which might still
be in use. Usually you're using the newest version (by default), which is Python 3.
At this moment it's 3.12.

In Windows you don't need to know any difference between the python interpreter versions.
You can just use:
>>	python.exe [any file(s) you want to run]	<<

However, outside of Windows, e. g. Linux, macOS, ... it's important to know which interpreter shall
be used.

When you use:

>>	python [any file(s) you want to run]	<<

then it's the python 2(!!) interpreter by default

For Python 3 you have to use:

>>	python3 [any file(s) you want to run]	<<

##	Do I need additional packages?

Some exercises need additional packages, e. g. accessing a database, using some awesome stuff, ...
Basicly, you don't need to use additional packages, except for some sub projects.

##	How to install additional packages?

-	use pip[3/.exe] install [package name]
-	similar to the python interpreter it's also required which pip you're using

for Windows:
>>	pip.exe list	<<	(listing all the packages, which are installed on your system)
>>	pip.exe install [package]	<< (installing the package, IF correct written AND ALSO available)

outside of Windows:
>>	pip3 list	<<	(using for Python 3; similar to pip.exe list)
>>	pip3 install [package]	<<	(you now know what to do here)