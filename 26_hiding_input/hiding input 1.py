#!/usr/bin/python3

"""
	Hiding the input
	by using getpass module.

	This allows us to enter from keyboard,
	where we don't see how much characters
	the user has typed in.

	If this module might not be installed
	on your system, so take a look of all packages,
	which are installed on your system yet:

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

	in that case: pip(3)(.exe) install getpass

	video tutorial:	https://youtu.be/AK44C_uZ9u4
	timestamp:		05:38:28
"""

import getpass as secret

userName = input('enter username: ')
userPassword = secret.getpass('enter password: ')

#	any authentification here...
print(f'user {userName} has been logged in')