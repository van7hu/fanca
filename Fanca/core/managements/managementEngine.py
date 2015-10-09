import time
from threading import Thread
from Fanca.commons.jsonsocket import Client
from Fanca.CONFIG import *
from Fanca.core.executors.generatorEngine import GeneratorEngine
from Fanca.core.executors.executorEngine import ExecutorEngine
from Fanca.core.loggers.loggerEngine import LoggerEngine

from Fanca.core.managements.mutatorManagementEngine import GeneralMutatorManagementEngine



class ManagementEngine:
    def __init__(self, configOptions):
        t1 = Thread(target=self.initGeneratorEngine, args=(configOptions,))
        t2 = Thread(target=self.initExecutorEngine, args=(configOptions,))
        t3 = Thread(target=self.initLoggerEngine, args=(configOptions,))
        print 'ManagementEngine: Start new thread for GeneratorEngine'
        t1.start()
        print 'ManagementEngine: Start new thread for ExecutorEngine'
        t2.start()
        print 'ManagementEngine: Start new thread for LoggerEngine'
        t3.start()
        # sleep 5 seconds waitting for those thread started fully
        time.sleep(5)

        if int(configOptions.management_engine) == 0:
            print 'Management Engine: Using GeneralMutatorManagementEngine'
            GeneralMutatorManagementEngine(configOptions)

    def initGeneratorEngine(self, configOptions):
        GeneratorEngine(configOptions)

    def initExecutorEngine(self, configOptions):
        ExecutorEngine(configOptions)

    def initLoggerEngine(self, configOptions):
        LoggerEngine(configOptions)
