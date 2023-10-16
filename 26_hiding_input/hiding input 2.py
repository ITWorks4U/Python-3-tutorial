#!/usr/bin/python3

"""
	An another way to hide the
	user input is by using the
	module maskpass.

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

	in that case: pip(3)(.exe) install maskpass

	video tutorial:	https://youtu.be/AK44C_uZ9u4
	timestamp:		05:38:28
"""

import maskpass as secret

userName = input('enter username: ')
userPassword = secret.askpass('enter password: ')

#	any authentification here...
print(f'user {userName} has been logged in')