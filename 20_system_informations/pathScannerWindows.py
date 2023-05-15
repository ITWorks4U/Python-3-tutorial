#!/usr/bin/python3

"""
	Scanning the folders from a certain drive.

	required installed api: psutil
	Python: pip.exe install psutil

	This script runs on Windows only.
"""

import os, psutil, settings as s, platform as p

#	----------
#	Scanning drives on
#	Windows.
#	----------
def scanDrives() -> None:
	for d in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
		
		if (os.path.exists("%s:" % d)):
			s.localDrives.append(d)
		#end if
	#end for
#end function

#	----------
#	displaying volume usages
#	of a certain directory, disk etc.
#	----------
def scanVolumes() -> None:
	s.printSep()

	for d in s.localDrives:
		#	appending ':\' after the volume name, e.g. C:\, D:\, ...
		drive = d + ":\\"
		print(f'scanning current drive: {d}')

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

	if machine == 'Windows':
		try:
			scanDrives()
			scanVolumes()
		except IOError as ioe:
			print(f'I/O error {ioe.strerror} <=> {ioe.args}')
		except Exception as ex:
			print(f'critical error: {ex.args}')
		#end try-catch
	else:
		print(f"This script isn't supposed to run under {machine}.")
	#end if
#end entry point