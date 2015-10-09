from Defines            import *
from DebuggerException  import *
from PyDbgEng           import *

from ctypes import *
from comtypes.gen import DbgEng

###########################################################
class DumpFileOpener(PyDbgEng):
    '''
    open crash dump file
    '''

    ###########################################################
    def __init__(self, dump_file, event_callbacks_sink = None, output_callbacks_sink = None, dbg_eng_dll_path = None, symbols_path = None):
        PyDbgEng.__init__(self, event_callbacks_sink, output_callbacks_sink, dbg_eng_dll_path, symbols_path)

        # open dump file
        self.dbg_eng_log("DumpFileOpener.__init__: about to open dump file %s" % dump_file)
        self.idebug_client.OpenDumpFile(dump_file)
        
        # Finish initialization by waiting for the event that
        # caused the dump.  This will return immediately as the
        # dump file is considered to be at its event.
        self.idebug_control.WaitForEvent(DbgEng.DEBUG_WAIT_DEFAULT, INFINITE)
