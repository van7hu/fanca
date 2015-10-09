from Defines            import *
from DebuggerException  import *
from PyDbgEng           import *
from UserModeSession    import *

from ctypes import *
from comtypes.gen import DbgEng

###########################################################
class ProcessAttacher(UserModeSession):
    '''
    debug an existing process.
    '''

    ###########################################################
    def __init__(self, pid, event_callbacks_sink = None, output_callbacks_sink = None, dbg_eng_dll_path = None, symbols_path = None):
        PyDbgEng.__init__(self, event_callbacks_sink, output_callbacks_sink, dbg_eng_dll_path, symbols_path)

        # attach to process
        self.dbg_eng_log("ProcessAttacher.__init__: about to attach to process with pid %d" % pid)
        self.idebug_client.AttachProcess(Server=UserModeSession.NO_PROCESS_SERVER, ProcessId = pid, AttachFlags = DbgEng.DEBUG_ATTACH_DEFAULT)

