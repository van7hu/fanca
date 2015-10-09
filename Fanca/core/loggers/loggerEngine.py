from Fanca.CONFIG import *
from Fanca.commons.jsonsocket import Server

from Fanca.core.loggers.windows.windowsFileLoggerEngine import WindowsFileLoggerEngine

class LoggerEngine:
    def __init__(self, configOptions):
        server = Server(LOG_ENGINE_HOST, LOG_ENGINE_PORT)
        print 'LoggerEngine: Start waitting for command'

        logger_type = int(configOptions.logger_type)
        if logger_type == 0:
            print 'LoggerEngine: Using Windows.FileLoggerEngine'
            WindowsFileLoggerEngine(server, configOptions)
