import time
from Fanca.commons.jsonsocket import Client
from Fanca.CONFIG import *

class GeneralMutatorManagementEngine:
	def __init__(self, configOptions):
		# Start fuzzing now
		iteration_to_fuzz = configOptions.iteration
		iteration_index = 0
		data_request_new_testcase = {'cmd': 'make_output'}
		data_request_run_debugger = {'cmd': 'run'}
		data_request_log_str = {'cmd': 'log_str', 'str': 'Sample string logged'}
		data_request_log_exception = {'cmd': 'log_exception'}
		while iteration_index <= iteration_to_fuzz:
			iteration_index = iteration_index + 1
			print str(iteration_index) + '. GeneralMutatorManagementEngine: Begin new iteration'
			smeClient = Client()
			
			print 'GeneralMutatorManagementEngine: Connect and request new test case from SimpleReplacerGeneratorEngine'
			smeClient.connect(GENERATOR_ENGINE_HOST, GENERATOR_ENGINE_PORT)
			smeClient.send(data_request_new_testcase)
			recv = smeClient.recv()
			if recv['fin'] == 'ok':
				print 'GeneralMutatorManagementEngine: Got new test case'
			elif recv['fin'] == 'max':
				print 'GeneralMutatorManagementEngine: Maximum samples reached,  halt now'
				while True:
					pass
			
			print 'GeneralMutatorManagementEngine: Connect and request run process from WindowsDebugEngine'
			smeClient.connect(DEBUG_ENGINE_HOST, DEBUG_ENGINE_PORT)
			smeClient.send(data_request_run_debugger)
			debuggerRecv = smeClient.recv()
			
			print 'GeneralMutatorManagementEngine: Connect and request new test case from SimpleReplacerGeneratorEngine'
			smeClient.connect(LOG_ENGINE_HOST, LOG_ENGINE_PORT)
			if debuggerRecv['fin'] == 'normal':
				smeClient.send(data_request_log_str)
				smeClient.recv()
			if debuggerRecv['fin'] == 'exception':
				smeClient.send(data_request_log_exception)
				smeClient.recv()