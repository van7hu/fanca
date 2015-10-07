from Fanca.CONFIG import *
from Fanca.commons.jsonsocket import Server
from Fanca.core.executors.monitors.windows.windowsDebugEngine import WindowsDebugEngine

class ExecutorEngine:
	def __init__(self, configOptions):
		server = Server(DEBUG_ENGINE_HOST, DEBUG_ENGINE_PORT)
		print 'ExecutorEngine: Start waitting for command'
		
		executor_type = int(configOptions.executor_type)
		if  executor_type == 0:
			print 'ExecutorEngine: Using WindowsDebugEngine'
			WindowsDebugEngine(server, configOptions)