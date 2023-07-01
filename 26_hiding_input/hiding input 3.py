#!/usr/bin/python3

"""
	You could also write your own
	function, which covers your
	input by using getch module.

	Usually, this module isn't installed
	by default. If so, it must be installed
	manually.

	take a look of all packages, which are
	installed on your system:

	Windows:
		pip.exe list

	Linux/macOS/else:
		pip3 list (for python 3 only)
		pip list (for python 2 only)

	installing the required package,
	if this is required:

	Windows:
		pip.exe install <package>

	Linux/macOS/else:
		pip3 install <package> (python 3 only)
		pip install <package> (python 2 only)

	in that case: pip(3)(.exe) install getch
"""
import getch

def hidingInput(message: str) -> str:
	print(message, end='')
	hidden = list()

	while True:
		symbol = getch.getch()

		if symbol == '\n' or symbol == '\r':
			break
		#end if

		#	displaying an asterisk as an replacement character
		print('*', end='', flush=True)
		hidden.append(symbol)
	#end while

	return "".join(hidden)
#end function

userName = input('enter username: ')
userPassword = hidingInput('enter password: ')

#	any authentification here...
print(f'user {userName} has been logged in')