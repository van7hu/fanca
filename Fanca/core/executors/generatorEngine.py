
from Fanca.core.executors.generators.mutatorGenerator import MutatorGenerator

class GeneratorEngine:
    def __init__(self, generatorQueue, iteration_index):
        config = generatorQueue.get()
        type = int(config['test_case_generation_engine'])
        
        generatorQueue.put(config)
        if type == 0:
            print 'GeneratorEngine: Using MutatorGenerator'
            MutatorGenerator(generatorQueue, iteration_index)
