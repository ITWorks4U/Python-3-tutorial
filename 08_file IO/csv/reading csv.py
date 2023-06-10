#!/usr/bin/python3

"""
	A CSV file (comma separated values) is often
	in use for MS Access, Libre Office Calc etc.
	to display content in a well format.

	In contrast to a "normal" file the values
	has a separator to hold a value in a certain
	cell.

	Basicly a csv file is a simple text file.

	There're also other ways to handle csv files,
	like using module csv, pandas, ...
"""

#	make sure the csv file extists... :o)
with open("test.csv", mode="r", encoding='ascii') as f:
	for line in f.readlines():
		for element in line.split(','):
			print(element, end='')
		#end for

		print()
	#end for
#end with