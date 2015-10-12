from ConfigParser import SafeConfigParser
import sys, getopt, os

def getOpts():  
    config =  SafeConfigParser()
    
    options, remainder = getopt.getopt(sys.argv[1:], 'f:')
    for opt, arg in options:
        if opt == '-f':
            configFilename = arg
            config.read(configFilename)
            return getConfigDict(config)
        else:
            config = None
            printUsage()
            return {}


def printUsage():
        print 'Usage: python fanca.py -f config_file'

def getConfigDict(config):
    config_dict = {}
   
    config_dict['project_dir'] = config.get('executors', 'project_dir')

    # get the configuration for Executor
    config_dict['executor_type'] = config.get('executors', 'executor_type')
    config_dict['test_case_generation_engine'] = config.get('executors', 'test_case_generation_engine')
    if config_dict['executor_type'] == '0':
        config_dict['command']  = config.get('executors', 'command')
        config_dict['windows_debugger_type']  = config.get('executors', 'windows_debugger_type')
        config_dict['follow_fork']  = config.get('executors', 'follow_fork')
        config_dict['process_name']  = config.get('executors', 'process_name')

    if config_dict['test_case_generation_engine'] == '0':
        config_dict['mutator_generator_engine'] = config.get('executors', 'mutator_generator_engine')
        config_dict['samples_dir'] = config.get('executors', 'samples_dir')
        config_dict['iteration_per_sample'] = config.get('executors', 'iteration_per_sample')
        config_dict['output_dir'] = config.get('executors', 'output_dir')
        config_dict['output_filename'] = config.get('executors', 'output_filename')

        config_dict['sample_list'] = [ f for f in os.listdir(config_dict['samples_dir']) if os.path.isfile(os.path.join(config_dict['samples_dir'],f)) ]
        config_dict['sample_count'] = len(config_dict['sample_list'])
        config_dict['sample_list_current'] = 0

    # get the configuration for Monitor
    config_dict['monitor_type'] = config.get('monitors', 'monitor_type')

    #get configuration  for Logger
    config_dict['logger_type'] = config.get('loggers', 'logger_type')
    config_dict['logger_dir'] = config.get('loggers', 'logger_dir')
    config_dict['normal_iteration_count'] = config.get('loggers', 'normal_iteration_count')

    # get configuration for ManagementEngine
    config_dict['management_engine'] = config.get('managements', 'management_engine')
    config_dict['iteration'] = config.get('managements', 'iteration')
    
    return config_dict

