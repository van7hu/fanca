from Fanca.CONFIG import *
from Fanca.commons.jsonsocket import Server
from Fanca.core.executors.monitors.windows.windowsDebugEngine import WindowsDebugEngine

class ExecutorEngine:
    def __init__(self, executorQueue):   
        config = executorQueue.get()
        executor_type = int(config['executor_type'])
        
        # put config back to the Queue
        executorQueue.put(config)
        if  executor_type == 0:
            print 'ExecutorEngine: Using WindowsDebugEngine'

            WindowsDebugEngine(executorQueue)
