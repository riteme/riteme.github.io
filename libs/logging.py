from enum import IntEnum

class LoggingLevel(IntEnum):
    DEBUG = 1
    INFO = 2
    WARN = 3
    ERROR = 4
    FATAL = 5
    NONE = 6

LOGGING_LEVEL = LoggingLevel.INFO

def debug(message):
    if LOGGING_LEVEL <= LoggingLevel.DEBUG:
        print("(DEBUG)", message)

def info(message):
    if LOGGING_LEVEL <= LoggingLevel.INFO:
        print("(info)", message)

def warn(message):
    if LOGGING_LEVEL <= LoggingLevel.WARN:
        print("(warn)", message)

def error(message):
    if LOGGING_LEVEL <= LoggingLevel.ERROR:
        print("(ERROR)", message)

def fatal(message, exit_code = -1):
    if LOGGING_LEVEL <= LoggingLevel.FATAL:
        print("(FATAL)", message)
    exit(exit_code)
