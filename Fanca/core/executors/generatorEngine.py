from Fanca.commons.jsonsocket import Server
from Fanca.CONFIG import *

from Fanca.core.executors.generators.mutatorGenerator import SimpleReplacerGenerator

class GeneratorEngine:
    def __init__(self, configOptions):
        server = Server(GENERATOR_ENGINE_HOST, GENERATOR_ENGINE_PORT)
        print 'GeneratorEngine: Start waitting for command'

        generator_type = int(configOptions.test_case_generation_engine)
        if generator_type == 0:
            print 'GeneratorEngine: Using SimpleReplacerGenerator'
            SimpleReplacerGenerator(server, configOptions)
