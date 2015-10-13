from winappdbg import Debug, HexDump, win32, Crash
import copy

class Wappdbger:
    def __init__(self, executorQueue):
        self.executorQueue = executorQueue

    def debuggerEventHandler(self, event):
        code = event.get_event_code()
        crash = Crash(event)
        if code == win32.EXCEPTION_DEBUG_EVENT and crash.firstChance:
            
            status, rule, description = crash.isExploitable()
            if rule=='Unknown' or rule=='Breakpoint':
                return
               
            print 'WindowsDebugEngine: We found interesting exception'
            print 'WindowsDebugEngine: %08x, %s, %s, %s' % (code, rule, description, status)

            self.executorQueue.put({'fin':'exception', 'rule': rule, 'description': description, 'status': status})
                

    def createDebugger(self, command):
        debug = Debug(self.debuggerEventHandler, bKillOnExit=True)
        argv = command.split()
        debug.execv(argv)
        debug.loop()
        