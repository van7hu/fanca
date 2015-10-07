from ConfigParser import SafeConfigParser
import sys, getopt

class FancaGetopts:
	def __init__(self):
		options, remainder = getopt.getopt(sys.argv[1:], 'f:')
		for opt, arg in options:
			if opt == '-f':
				self.configFilename = arg

	def printUsage(self):
		print 'Usage: python fanca.py -f config_file'
	
class FancaInitor:
	
	def __init__(self, configFilename):
		self.config = SafeConfigParser()
		self.config.read(configFilename)
	