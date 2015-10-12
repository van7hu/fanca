import time, datetime, copy
from multiprocessing import Process, Queue

from Fanca.core.executors.generatorEngine import GeneratorEngine
from Fanca.core.executors.executorEngine import ExecutorEngine
from Fanca.core.loggers.loggerEngine import LoggerEngine

class GeneralMutatorManagementEngine:
    def __init__(self, configDict):
        # Start fuzzing now
        iteration_to_fuzz = configDict['iteration']
        iteration_index = 0
        
        temp = str(time.time())
        
        while iteration_index < iteration_to_fuzz:
            iteration_index = iteration_index + 1
            print str(iteration_index)+'. Begin iteration #'+str(iteration_index)
            
            # make new test case from GeneratorEngine
            print 'MutatorManagementEngine: Request for making new testcase'
            generatorQueue = Queue()
            generatorDict = copy.deepcopy(configDict)
            generatorQueue.put(generatorDict)

            t = Process(target=GeneratorEngine, args=(generatorQueue, iteration_index,))
            t.start()
            t.join()
            ret = generatorQueue.get()
            generatorQueue.close()
            if(ret['fin']=='max'):
                print 'MutatorManagementEngine: Maximum number sample reached, halt now.'
                while True:
                    pass
            
            # run the ExecutorEngine
            print 'MutatorManagementEngine: Request to run executor'
            executorQueue = Queue()
            executorDict = copy.deepcopy(configDict)
            executorQueue.put(executorDict)

            t = Process(target=ExecutorEngine, args=(executorQueue,))
            t.start()
            t.join()
            log_data = executorQueue.get()
            print '################log_data = '+str(log_data)
            executorQueue.close()
            
            need_to_write_log = False
            
            if log_data['fin']=='normal':   
                log_data['cmd']='log_str'
                if iteration_index % int(configDict['normal_iteration_count']) == 0:
                    print ''
                    print 'GeneralMutatorManagementEngine: Send normal iteration log to LoggerEngine'
                    log_data['str'] = 'At '+str(datetime.datetime.now()) + ': Iteration '+str(iteration_index)+' reached!'
                    need_to_write_log = True
            else:
                log_data['cmd']='log_exception'
                log_data['str'] = 'At '+str(datetime.datetime.now()) + ', Iteration '+str(iteration_index)+': '+log_data['rule']+', '+log_data['description']\
                    +log_data['status']
                need_to_write_log = True
            
            # if  need_to_write_log = True
            if  need_to_write_log:
                print 'MutatorManagementEngine: Request LoggerEngine'
                loggerQueue = Queue()
                loggerDict = copy.deepcopy(configDict)
                loggerQueue.put(loggerDict)
                
                t = Process(target=LoggerEngine, args=(loggerQueue, log_data, iteration_index, temp))
                t.start()
                t.join()
