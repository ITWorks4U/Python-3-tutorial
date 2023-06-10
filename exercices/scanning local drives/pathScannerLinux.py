#!/usr/bin/python3

"""
	Scanning the folders from a certain root path.
	
	required installed api: psutil
	Python 2: pip install psutil
	Python 3: pip3 install psutil

	This script runs on UNIX/Linux/macos only.
"""

import os, psutil, settings as s, platform as p

#	----------
#	displaying volume usages
#
#	path: starting point
#	----------
def scanVolumes(path: str) -> None:
	s.printSep()
	print(f'scanning current path: {path}')
	s.printSep(char='=')

	for d in os.listdir(path):
		drive = path + d
		print(f'current path: {drive}')

		disk = psutil.disk_usage(drive)
		summary = list()
		summary.append(s.humanSize(disk.total))
		summary.append(s.humanSize(disk.used))
		summary.append(s.humanSize(disk.free))

		print(f'total: {summary[0]}, used: {summary[1]}, free: {summary[2]} (', end='')

		if not s.onFreeSpace(disk.total, disk.free):
			print(f'path {drive} has less than {s.minFreeSpace * 100}% free space left')
		#end if

		s.printSep()
	#end for

	s.printSep(char='', additionalNewLine=True)
#end function

#entry point
if __name__ == '__main__':
	machine = p.system()

	if machine != 'Windows':
		try:
			paths = ("/", "/home/", "/mnt/", "/dev/", "/opt/")

			for p in paths:
				scanVolumes(path=p)
			#end for
		except IOError as ioe:
			print(f'I/O error: {ioe.strerror} <=> {ioe.errno}')
		except Exception as ex:
			print(f'critical error: {ex.args}')
		#end try-catch
	else:
		print(f"Can't run this script under {machine}")
#end entry point