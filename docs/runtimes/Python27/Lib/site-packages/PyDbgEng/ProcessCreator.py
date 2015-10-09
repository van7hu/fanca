from Defines            import *
from DebuggerException  import *
from PyDbgEng           import *
from UserModeSession    import *

from ctypes import *
from comtypes.gen import DbgEng

###########################################################
class ProcessCreator(UserModeSession):
    '''
    debug a new process.
    '''

    follow_forks = False

    ###########################################################
    def __init__(self, command_line, follow_forks = True, event_callbacks_sink = None, output_callbacks_sink = None, dbg_eng_dll_path = None, symbols_path = None):
        PyDbgEng.__init__(self, event_callbacks_sink, output_callbacks_sink, dbg_eng_dll_path, symbols_path)

        # set creation flags
        self.follow_forks = follow_forks        
        if self.follow_forks:
            creation_flags = DbgEng.DEBUG_PROCESS
        else:
            creation_flags = DbgEng.DEBUG_ONLY_THIS_PROCESS

        # create debuggee process
        self.dbg_eng_log("ProcessCreator.__init__: about to create process with command line '%s'" % command_line)
        self.idebug_client.CreateProcess(Server=UserModeSession.NO_PROCESS_SERVER, CommandLine = command_line, CreateFlags = creation_flags)
