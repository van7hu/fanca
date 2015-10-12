from winappdbg import Debug, HexDump, win32, Crash
import copy

class Wappdbger:
    def __init__(self, executorQueue):
        print 'Wappdbger object inited'
        self.executorQueue = executorQueue

    def debuggerEventHandler(self, event):
        code = event.get_event_code()
        crash = Crash(event)
        if code == win32.EXCEPTION_DEBUG_EVENT and not crash.isOurBreakpoint and not crash.isSystemBreakpoint and crash.firstChance:
            if crash.isOurBreakpoint or crash.isSystemBreakpoint or not crash.firstChance:
                return
            
            status, rule, description = crash.isExploitable()
            print 'WindowsDebugEngine: We found interesting exception'
            print 'WindowsDebugEngine: %s, %s, %s' % (rule, description, status)

            self.executorQueue.put({'fin':'exception', 'rule': rule, 'description': description, 'status': status})
        else:
            #print 'Not interesting event.'
            pass
        
    def createDebugger(self, command):
        debug = Debug(self.debuggerEventHandler, bKillOnExit=True)
        argv = command.split()
        debug.execv(argv)
        debug.loop()
        