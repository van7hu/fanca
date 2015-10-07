import sys, os
from helpers.fancaInitor import FancaInitor, FancaGetopts
from helpers.fancaBody import FancaBody

from   Fanca.core.managements.managementEngine import ManagementEngine



# initialize environment
#

# append our ROOT to PYTHON_PATH, need to be fixed, getcwd() does not work, must use getpwd()?
#sys.path.append(os.path.dirname(os.path.realpath(__file__)))

options = FancaGetopts()

if not hasattr(options, 'configFilename'):
	options.printUsage()
	sys.exit()

init = FancaInitor(options.configFilename)

configOptions = FancaBody(init.config)

ManagementEngine(configOptions)


 


