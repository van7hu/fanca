import sys

class FancaBody:
	def __init__(self, config):
		self.project_dir = config.get('executors', 'project_dir')
		self.getConfigExecutor(config)
		self.getConfigManagement(config)
		self.getConfigLogger(config)
		
	def getConfigExecutor(self, config):
		self.executor_type = config.get('executors', 'executor_type')
		self.test_case_generation_engine = config.get('executors', 'test_case_generation_engine')
		if self.executor_type == '0':
			self.command = config.get('executors', 'command')
			self.follow_fork = config.get('executors', 'follow_fork')
			self.process_name = config.get('executors', 'process_name')
		
		if self.test_case_generation_engine == '0':
			self.generalMutatorGetOptions(config)

	def getConfigMonitor(self, config):
		self.monitor_type = config.get('monitors', 'monitor_type')
	
	def getConfigLogger(self, config):
		self.logger_type = config.get('loggers', 'logger_type')
		self.logger_dir = config.get('loggers', 'logger_dir')
	
	def getConfigManagement(self, config):
		self.management_engine = config.get('managements', 'management_engine')
		self.iteration = config.get('managements', 'iteration')
	
	# some helpers functions
	def generalMutatorGetOptions(self, config):
		self.samples_dir = config.get('executors', 'samples_dir')
		self.iteration_per_sample = config.get('executors', 'iteration_per_sample')
		self.output_dir = config.get('executors', 'output_dir')
		self.output_filename = config.get('executors', 'output_filename')
