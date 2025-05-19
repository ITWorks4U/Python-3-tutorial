from misc.loggingToSomewhere import loggingSomething
from misc.loggingType import LoggingType
from config.settings import loadConfig

loadConfig()
loggingSomething(message="next steps here...", logType=LoggingType.DEBUG)