import os
import Fanca.core.executors.generators.mutators.simple_replacer

class MutatorGenerator:
    def __init__(self, generatorQueue, iteration_index):
        generatorDict = generatorQueue.get()
        iteration_per_sample = int(generatorDict['iteration_per_sample'])
        output = os.path.join(generatorDict['output_dir'], generatorDict['output_filename'])
        samples_dir = generatorDict['samples_dir']
        print 'GeneralMutatorManagementEngine: Getting sample file list'
        sample_list = [ f for f in os.listdir(samples_dir) if os.path.isfile(os.path.join(samples_dir,f)) ]
        sample_count = len(sample_list)
        print 'GeneralMutatorManagementEngine: Number of sample found: ' + str(sample_count)
        
        sample_list_current = iteration_index / iteration_per_sample
        if((sample_list_current+1) > sample_count):
            generatorQueue.put({'fin': 'max'})
        else:
            input = os.path.join(samples_dir, sample_list[sample_list_current])
            if int(generatorDict['mutator_generator_engine'])==0:
                print 'MutatorGenerator: Using SimpleReplacerGenerator engine'
                self.simpleReplacerWrapper(input, output)
                generatorQueue.put({'fin': 'ok'})
        
    def simpleReplacerWrapper(self, input_filename, output_filename):
        Fanca.core.executors.generators.mutators.simple_replacer.main(input_filename, output_filename)
