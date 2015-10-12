from Fanca.CONFIG import *
from Fanca.commons.jsonsocket import Server

from Fanca.core.loggers.windows.windowsFileLoggerEngine import WindowsFileLoggerEngine

class LoggerEngine:
    def __init__(self, loggerQueue, executorQueue, iteration_index):      
        config = loggerQueue.get()
        logger_type =  int(config['logger_type'])
        
        # put the config back, and choose betwwne logger type
        loggerQueue.put(config)
        if logger_type == 0:           
            print 'LoggerEngine: Using Windows.FileLoggerEngine'
            WindowsFileLoggerEngine(loggerQueue, executorQueue, iteration_index)
