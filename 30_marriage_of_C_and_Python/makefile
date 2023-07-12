#	Building the library for python.
#
#	important:	your library to create must be compiled with
#				with -Wall, -shared, -fPIC and -O2 flags, where:
#
#				-Wall		display all warnings, if any
#				-shared		enabling to share your library for foreign systems
#				-fPIC		"force Position Independent Code"
#
#							the generated machine code is not dependent on being
#							located at a specific address in order to work
#
#							see also: https://stackoverflow.com/questions/5311515/gcc-fpic-option
#				-O2			Optimisazion of your code.
#
#							see also: https://stackoverflow.com/questions/655382/meaning-of-gcc-o2
#
#	attention:	Depending on your used system you must
#				select the specific target!
#
#				This was tested on Linux only.
#				Not tested on Windows or macOS.
#
#	appendix:	the commands are suppressed for output by using @ in front of them

#	by default, a dummy target is in use
nothing:
					$(error You must use a specific target depending on your system.)

Linux:
					@gcc -o c_library.dll -Wall -shared -fPIC -O2 lib.c lib.h
					$(info Linux library has been successfully built.)

Windows:
					@gcc.exe -o c_library.dll -Wall -shared -fPIC -O2 lib.c lib.h
					$(info Windows library has been successfully built.)

Mac:
					@gcc -o c_library.dll -Wall -shared -fPIC -O2 lib.c lib.h
					$(info Library for macOS has been successfully built.)

clean:
#	depending on your OS the remove
#	command may differ
#
#	for Windows:	del c_library.dll
#	otherwise:		rm c_library.dll
#
#	make also sure, that your file to remove exists :o)

					@rm c_library.dll
					$(info Library removed.)