import time, datetime
from Fanca.commons.jsonsocket import Client, Server
from Fanca.CONFIG import *

class GeneralMutatorManagementEngine:
    def __init__(self, configOptions):
        # Start fuzzing now
        iteration_to_fuzz = configOptions.iteration
        iteration_index = 0
        data_request_new_testcase = {'cmd': 'make_output'}
        data_request_run_debugger = {'cmd': 'run'}

        smeClient = Client()
        smeClient.connect(LOG_ENGINE_HOST, LOG_ENGINE_PORT)
        smeClient.send({'cmd': 'log_str', 'str': 'Fuzzing started at '+str(datetime.datetime.now())})

        # server to wait for reply from executor engine
        managementServer = Server(MANAGEMENT_ENGINE_HOST, MANAGEMENT_ENGINE_PORT)


        while iteration_index <= iteration_to_fuzz:
            iteration_index = iteration_index + 1
            print str(iteration_index) + '. GeneralMutatorManagementEngine: Begin new iteration'
            smeClient = Client()

            print 'GeneralMutatorManagementEngine: Connect and request new test case from GeneratorEngine'
            smeClient.connect(GENERATOR_ENGINE_HOST, GENERATOR_ENGINE_PORT)
            smeClient.send(data_request_new_testcase)
            recv = smeClient.recv()
            if recv['fin'] == 'ok':
                print 'GeneralMutatorManagementEngine: Got new test case'
                original_sample = recv['origin']
            elif recv['fin'] == 'max':
                print 'GeneralMutatorManagementEngine: Maximum samples reached,  halt now'
                while True:
                    pass

            print 'GeneralMutatorManagementEngine: Connect and request run process from ExecutorEngine'
            smeClient.connect(DEBUG_ENGINE_HOST, DEBUG_ENGINE_PORT)
            smeClient.send(data_request_run_debugger)
            smeClient.close()
            print
            print 'GeneralMutatorEngine: Start server and waitting for reply from ExecutorEngine'
            print ''

            # In the case of exception occured, the reply for exception always comes first, so,
            # 1. wait for reply from exception
            # 2. wait for reply from normal, discard it, then proceed to exception handling
            managementServer.accept()
            debuggerRecv = managementServer.recv()
            if debuggerRecv['fin'] == 'exception':
                managementServer.accept()
                managementServer.recv()


            if debuggerRecv['fin'] == 'normal':
                if iteration_index % int(configOptions.normal_iteration_count) == 0:
                    smeClient.connect(LOG_ENGINE_HOST, LOG_ENGINE_PORT)
                    print ''
                    print 'GeneralMutatorManagementEngine: Send normal iteration log to LoggerEngine'
                    x = 'At '+str(datetime.datetime.now()) + ': Iteration '+str(iteration_index)+' reached!'
                    smeClient.send({'cmd': 'log_str', 'str': x})
                    smeClient.recv()
            if debuggerRecv['fin'] == 'exception':
                smeClient.connect(LOG_ENGINE_HOST, LOG_ENGINE_PORT)
                print ''
                print 'GeneralMutatorManagementEngine: Send exeption log to LoggerEngine'
                # additional info need to be sent and logged here
                # e.g. stacktrace, exploitabilities ...
                strLog = 'At '+str(datetime.datetime.now()) + ', Iteration '+str(iteration_index)+': '+debuggerRecv['bucket']
                smeClient.send({'cmd': 'log_exception', 'str': strLog, 'management_iteration': iteration_index,'buff': debuggerRecv['buff'], 'bucket': debuggerRecv['bucket'],
                        'original_sample':original_sample})
                smeClient.recv()
