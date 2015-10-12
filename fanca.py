import sys, os
import helpers.init

from   Fanca.core.managements.managementEngine import ManagementEngine


#
# initialize environment


# append our ROOT to PYTHON_PATH, need to be fixed, getcwd() does not work, must use getpwd()?
#sys.path.append(os.path.dirname(os.path.realpath(__file__)))

if __name__=='__main__':
    
    configDict = helpers.init.getOpts()
    ManagementEngine(configDict)
