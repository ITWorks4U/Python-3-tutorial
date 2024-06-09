#	Purpose

-	usually, defining a variable / an object on top of your code it's called a "global variable" => on any time and on any situation your global statement can be read and also modified
-	Python(3) strictly differs global and local variables / objects
-	mostly you don't realize that, but sometimes this is really important to know when to modify a global object in an own section

###	how to read / write a global expression

-	in both cases make sure your object is available (no class member, ...) => "just" on top of your code
-	use >>global<< keyword to let the python interpreter to know, that you want to read / modify a variable

###	useful examples
-	to easy access to an object
-	in combination with threads to let control sequences from outside