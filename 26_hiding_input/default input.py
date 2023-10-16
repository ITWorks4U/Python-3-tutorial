#!/usr/bin/python3

"""
	Imagine, you're writing an application,
	which takes a username and a password
	for an authentification or else.

	usually, we're using input(promt: str) -> str function,
	to read from the keyboard, however, this is
	really unsecure, of course.

	video tutorial:	https://youtu.be/AK44C_uZ9u4
	timestamp:		05:38:28
"""

userName = input('enter username: ')
userPassword = input('enter password: ')

#	any authentification here...
print(f'user {userName} has been logged in')