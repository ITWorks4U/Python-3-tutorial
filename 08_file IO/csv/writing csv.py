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

#	identical to a normal IO operation, where the comma
#	will be a separator for the csv file => must be imported
#	and set in MS Excel, OO calc, LO calc, ...
#
#	the encoding is optional
with open("test.csv", mode="w", encoding="ascii") as f:
	print("C, C++, Python, Java, C#", file=f, end='')
#end with