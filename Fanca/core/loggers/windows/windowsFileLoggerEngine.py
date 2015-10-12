import os, time, shutil
from Fanca.CONFIG import *


class WindowsFileLoggerEngine:
    # We use the same logging technique as of Peach fuzzer 2.3.9, though not exactly
    def __init__(self, loggerQueue, log_data, iteration_index, temp):
        # from log_dir, create new directory for each test based on time
        config = loggerQueue.get()

        log_dir = config['logger_dir']
        log_dir = os.path.join(log_dir, temp)
        try:
            os.mkdir(log_dir)
        except:
            pass
        print "WindowsWindowsFileLoggerEngine: Logging to directory: " + log_dir

        # open log file in unbuffered mode
        logFileHandler = open(os.path.join(log_dir, temp+'.log'), 'a', 0)

            # the data received will be in the form of a dict with the key
            # 1. cmd
            # - cmd = log_str
            #       2. str = 'the string to be written to log file'
            # - cmd = log_exception
            #       2. str = 'the string to be written to log file'
            #       3. sample_filename = 'The sample file was used to make the fuzzed_filename', absolutepath + filename
            #       4. fuzzed_filename = 'The file was used to fuzz', absolute path + file name
            #       5. iteration_count = interger_type of iteration has passed since fuzzing
        if log_data['cmd'] == 'log_str':
            print 'WindowsFileLoggerEngine: Write to log file'
            logFileHandler.write(log_data['str'] + '\n')

        elif log_data['cmd'] == 'log_exception':
            print 'WindowsFileLoggerEngine: Write to log file'
            logFileHandler.write(log_data['str'] + '\n')
            # mkdir based on iteration_count
            log_exception_directory = os.path.join(log_dir, str(iteration_index))
            os.mkdir(log_exception_directory)

            iteration_per_sample = int(config['iteration_per_sample'])
            output = os.path.join(config['output_dir'], config['output_filename'])
            samples_dir = config['samples_dir']
            sample_list = [ f for f in os.listdir(samples_dir) if os.path.isfile(os.path.join(samples_dir,f)) ]
            sample_count = len(sample_list)
            sample_list_current = iteration_index / iteration_per_sample
            input = os.path.join(samples_dir, sample_list[sample_list_current])
            
            
            shutil.copyfile(input, os.path.join(log_exception_directory, os.path.basename(input)))
            shutil.copyfile(output, os.path.join(log_exception_directory, \
                os.path.basename(output)))
        
        
        logFileHandler.close()