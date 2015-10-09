import os
import Fanca.core.executors.generators.mutators.simple_replacer

class SimpleReplacerGenerator:
    def __init__(self, server, configOptions):
        samples_dir = configOptions.samples_dir
        output_dir = configOptions.output_dir
        output_filename = configOptions.output_filename
        iteration_per_sample = int(configOptions.iteration_per_sample)

        print 'SimpleReplacerGeneratorEngine: Getting sample file list'
        sample_list = self.getSampleFileList(samples_dir)
        print 'SimpleReplacerGeneratorEngine: Number of sample found: ' + str(len(sample_list))
        sample_count = len(sample_list)
        sample_list_current = 0

        connection_counter = 0
        make_output_counter = 0

        print 'SimpleReplacerGeneratorEngine: Start waitting for command'

        data_all_samples_used = {'fin': 'max'}

        while True:
            server.accept()
            connection_counter = connection_counter + 1

            print  str(connection_counter) + '. SimpleReplacerGeneratorEngine: Receiving connection'
            recv = server.recv()

            if recv['cmd'] == 'make_output':
                make_output_counter = make_output_counter + 1
                print str(make_output_counter) + '. SimpleReplacerGeneratorEngine: Got request to make new test case'
                if (((make_output_counter-1) % iteration_per_sample) == 0) and (make_output_counter != 1):
                    print 'SimpleReplacerGeneratorEngine: Maxium iteration per sample reached, change the sample'
                    sample_list_current = sample_list_current + 1
                if (sample_list_current+1) > sample_count:
                    print 'SimpleReplacerGeneratorEngine: We have iterated over all samples, Halt now'
                    server.send(data_all_samples_used)

                    while True:
                        pass
                else:
                    print 'SimpleReplacerGeneratorEngine: make output from current sample: ' + str(sample_list[sample_list_current])
                    self.simpleReplacerWrapper(os.path.join(samples_dir, sample_list[sample_list_current]), os.path.join(output_dir, output_filename))
                    print 'SimpleReplacerGeneratorEngine: Test case generated'
                    print 'SimpleReplacerGeneratorEngine: input: ' + os.path.join(samples_dir, sample_list[sample_list_current])
                    print 'SimpleReplacerGeneratorEngine: output: ' + os.path.join(output_dir, output_filename)
                    data_ok = {'fin': 'ok', 'origin': os.path.join(samples_dir, sample_list[sample_list_current])}
                    server.send(data_ok)

    # some helper functions
    def getSampleFileList(self, sample_dir):
        onlyfiles = [ f for f in os.listdir(sample_dir) if os.path.isfile(os.path.join(sample_dir,f)) ]
        return onlyfiles
    def simpleReplacerWrapper(self, input_filename, output_filename):
        Fanca.core.executors.generators.mutators.simple_replacer.main(input_filename, output_filename)
