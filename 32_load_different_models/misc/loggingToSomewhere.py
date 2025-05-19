try:
	#same result here:	this works only for main
	from misc.loggingType import LoggingType
except ImportError:
	#this works for (config/)settings.py
	from loggingType import LoggingType
#end try

def loggingSomething(message: str, logType: LoggingType = LoggingType.NORMAL) -> None:
	#	"any logging"
	print(f"{message} of type {logType}")
#end function