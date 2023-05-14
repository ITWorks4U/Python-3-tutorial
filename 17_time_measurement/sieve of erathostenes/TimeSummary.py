#!/usr/bin/python3

"""
	customized example to
	to find prime numbers by
	using the sive of erathostenes
"""
import math

#	-----------
#	customized way to determine
#	the amount of time
#	-----------
class TimeSummary:
	def summary(self, elapsed_time) -> None:
		if not isinstance(elapsed_time, float):
			raise Exception("Wrong data type was in use!")
		#end if

		days = math.ceil(elapsed_time // 86400)
		hours = math.ceil(elapsed_time // 3600)
		minutes = math.ceil(elapsed_time // 60)
		seconds = math.ceil(elapsed_time % 60)
		millis = math.ceil(elapsed_time // 1000)

		#	correction of some time values
		if millis == 1000:
			seconds += 1
			millis = 0
		#end if

		if seconds == 60:
			minutes += 1
			seconds = 0
		#end if

		if minutes == 60:
			hours += 1
			minutes = 0
		#end if

		if hours == 24:
			days += 1
			hours = 0
		#end if

		print("elapsed time: {0} days, {1} hours, {2} minutes, {3} seconds, {4} milli seconds".format(days, hours, minutes, seconds, millis))
	#end method
#end class
