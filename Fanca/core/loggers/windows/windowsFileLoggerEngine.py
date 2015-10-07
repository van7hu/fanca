import os, time
from Fanca.CONFIG import *


class WindowsFileLoggerEngine:
	# We use the same logging technique as of Peach fuzzer 2.3.9, though not exactly
	def __init__(self, server, configOptions):
		# from log_dir, create new directory for each test based on time
		temp = str(time.time())
		
		log_dir = configOptions.logger_dir
		log_dir = os.path.join(log_dir, temp)
		os.mkdir(log_dir)
		print "WindowsWindowsFileLoggerEngine: Logging to directory: " + log_dir
		
		# open log file in unbuffered mode
		logFileHandler = open(os.path.join(log_dir, temp+'.log'), 'w', 0)
		
		connection_counter = 0
		
		print 'WindowsFileLoggerEngine: Start waitting for command'
		
		while True:
			server.accept()
			connection_counter = connection_counter + 1
			
			print str(connection_counter) + '. WindowsFileLoggerEngine: Receiving connection'
			recv = server.recv()
			# the data received will be in the form of a dict with the key
			# 1. cmd
			# - cmd = log_str
			#	2. str = 'the string to be written to log file'
			# - cmd = log_exception
			#	2. str = 'the string to be written to log file'
			#	3. sample_filename = 'The sample file was used to make the fuzzed_filename', absolutepath + filename
			#	4. fuzzed_filename = 'The file was used to fuzz', absolute path + file name
			#	5. iteration_count = interger_type of iteration has passed since fuzzing
			if recv['cmd'] == 'log_str':
				print "WindowsFileLoggerEngine: recv['cmd']: " + recv['cmd']
				print 'WindowsFileLoggerEngine: Write to log file'
				logFileHandler.write(recv['str'] + '\n')
				# send nothing back to management engine, indicate that logging finished
				server.send('')
			elif recv['cmd'] == 'log_exception':
				print "WindowsFileLoggerEngine: recv['cmd']: " + recv['cmd']
				print 'WindowsFileLoggerEngine: Write to log file'
				logFileHandler.write(recv['str'] + '\n')
				# mkdir based on iteration_count
				log_exception_directory = self.log_dir + str(recv['iteration_count']) + "\\"
				os.mkdir(log_exception_directory)
				shutil.copyfile(recv['sample_filename'], os.path.join(log_exception_directory, os.path.basename(recv['sample_filename'])))
				shutil.copyfile(recv['fuzzed_filename'], os.path.join(log_exception_directory, os.path.basename(recv['fuzzed_filename'])))
				# send nothing back to management engine, indicate that logging finished
				server.send('')