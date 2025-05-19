###
#	Calling a function / class method wrong.
###

'''
	You're calling a function to do stuff.
	The arguments in your function may have a default value, so you can also
	call your function without arguments.

	By calling your function with arguments, then the specific order of your
	arguments may cause a logical error on runtime.

	The function writeToLog() has been called in the wrong way.
	Unlike the order of "log type" and "message" the function call
	will be "message" and "log type" and this is a logical error.

	Since Python is a interpreter language this small pitfall may
	cause a huge mess in your application.
'''

from enum import Enum

class LogType(Enum):
	NORMAL = 0
	WARNING = 1
	ERROR = 2
	CRITICAL = 3
	DEBUG = 4
#end enum class

def writeToLog(logType: LogType = LogType.NORMAL, message: str = "") -> None:
	type_of_log = LogType.NORMAL.name

	match logType:
		case LogType.WARNING:
			type_of_log = LogType.WARNING.name
		case LogType.ERROR:
			type_of_log = LogType.ERROR.name
		case LogType.CRITICAL:
			type_of_log = LogType.CRITICAL.name
		case LogType.DEBUG:
			type_of_log = LogType.DEBUG.name
		#end cases
	#end match

	print(f'message: {message}	<=>	type: {type_of_log}')
#end function


#	any code here...
#	Surprised? :-)
writeToLog("An error has been detected!", LogType.ERROR)