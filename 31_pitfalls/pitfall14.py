###
#	checking, if a file exists
###

'''
	Good idea, wrongly realized.

	With os.path.exists(file_descriptor_or_path) it checks, if the
	argument exists. True returns, if existing, false otherwise.

	But this function also returns true for an existing path.
	What's next? Try to open the path as a file...? Bad idea.

	Fun fact:
	often used:
		-	os.path.exists(file_or_path)
		-	pathlib.Path.exists(file_or_path)

	Looks similar, almost identical, but the behavior of both functions differs.

	os.path.exists():
		returns True, if the path or file exists
		False otherwise
		
		The function also returns False on any OSError without any consequences.

	Path.exists():
		similar to os.path.exists()

		However, on any OSError this could re-raise the OSError, if a sub function
		called "_ignore_error" returns False. (see:	pathlib.py::_ignore_error)
'''

import os

fd = None
fileNames = ['pitfall14.py', '/home', 'C:\\', '¯\\_(ツ)_/¯']

for fileName in fileNames:
	if os.path.exists(fileName):
		try:
			with open(fileName) as fd:
				#do something...
				pass
			#end with
		except Exception as e:
			print(f'error for "{fileName}": {e.args}')
		#end try
	else:
		print(f'certain "{fileName}" does not exist')
	#end if
#end for
