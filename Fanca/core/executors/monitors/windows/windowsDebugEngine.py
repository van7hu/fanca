import psutil, time
from multiprocessing import Process

from Fanca.core.executors.monitors.windows.debugger import Debugger
from Fanca.core.executors.monitors.windows.wappdbger import Wappdbger
from Fanca.core.executors.monitors.windows.CONFIG import *
from Fanca.commons.jsonsocket import Server

class WindowsDebugEngine:
    def __init__(self, executorQueue):
        config = executorQueue.get()
        
        command = config['command']
        follow_fork = config['follow_fork']
        process_name = config['process_name']

        if follow_fork == 'True':
            follow_fork = True
        else:
            follow_fork = False
        
        normal_data = {'fin': 'normal'}

        if config['windows_debugger_type']=='pydgbeng':
            print 'WindowsDebugEngine: Using PyDbgEng'
            debuggerProcess = Process(target=self.runCommand, args=(command, follow_fork))
        else:
            print 'WindowsDebugEngine: Using winappdbg'
            debuggerProcess = Process(target=self.runCommandWinappdbg, args=(command, executorQueue))
        
        print 'WindowsDebugEngine: Start process to run debugger'
        debuggerProcess.start()

        print "WindowsDebugEngine: Checks CPU usage'" + process_name + "', if it is zero, debugger will be terminate."
        time.sleep(1)
        

        self.checkProcessCpuUsage(process_name)
        debuggerProcess.terminate()


        if executorQueue.empty():
            executorQueue.put(normal_data)            
        else:
            exception_data = executorQueue.get_nowait()
            executorQueue.put(exception_data)
        
        

    def runCommand(self, command, follow_fork):      
        debugger = Debugger()
        print 'WindowsDebugEngine, runCommand(): Start new Process to run the debugger'
        print 'Command: '+command
        debugger.createDebugger(command, follow_fork)

    def runCommandWinappdbg(self, command, executorQueue):
        wappdbger = Wappdbger(executorQueue)
        print 'WindowsDebugEngine, runCommandWinappdbg(): start new Process to run debugger'
        wappdbger.createDebugger(command)
    
    # some helper functions
    def checkProcessCpuUsage(self, process_name):
        pid = self.findProcess(process_name)

        cpu_index = 0
        if pid == 0:
            print 'WindowsDebugEngine, checkProcessCpuUsage(): No process founded '+process_name
        else:
            while cpu_index < DEBUG_ENGINE_CPU_COUNTER:
                x = psutil.Process(pid).get_cpu_percent(1)
                if x > 0:
                    print 'WindowsDebugEngine: CPU times is greater than zero, reset cpu_index back to 0 (' + str(x) + ')'
                    cpu_index = 0
                else:
                    cpu_index = cpu_index + 1
                    print 'WindowsDebugEngine: cpu_index = ' + str(cpu_index)
                time.sleep(0.25)
            print 'WindowsDebugEngine: cpu_index has eslapsed, terminate the debugger process now'

    def findProcess(self, name):
        pid = 0
        for proc in psutil.process_iter():
            if proc.name == name:
                pid = proc.pid

        return pid
