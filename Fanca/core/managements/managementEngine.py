import time
from threading import Thread
from Fanca.commons.jsonsocket import Client
from Fanca.CONFIG import *


from Fanca.core.managements.mutatorManagementEngine import GeneralMutatorManagementEngine



class ManagementEngine:
    def __init__(self, configDict):
        if int(configDict['management_engine']) == 0:
            print 'Management Engine: Using GeneralMutatorManagementEngine'
            GeneralMutatorManagementEngine(configDict)