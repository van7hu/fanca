import psutil, time
from multiprocessing import Process

from Fanca.core.executors.monitors.windows.debugger import Debugger
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

        debuggerProcess = Process(target=self.runCommand, args=(command, follow_fork))
        replyProcess = Process(target=self.replyServer, args=(executorQueue,))
        print 'WindowsDebugEngine: Start 2 processes for debugger'
        debuggerProcess.start()
        replyProcess.start()

        print "WindowsDebugEngine: Old thread checks for CPU usage by process '" + process_name + "', if it is zero, debugger will be killed"
        time.sleep(1)

        self.checkProcessCpuUsage(process_name)
        debuggerProcess.terminate()
        replyProcess.terminate()

        if executorQueue.empty():
            print 'We have an empry'
            executorQueue.put(normal_data)            
        else:
            print 'Noooooooooooo'
            exception_data = executorQueue.get_nowait()
            executorQueue.put(exception_data)

    def runCommand(self, command, follow_fork):      
        debugger = Debugger()
        print 'WindowsDebugEngine, runCommand(): Start new Process to run the debugger'
        print 'Command: '+command
        debugger.createDebugger(command, follow_fork)

    def replyServer(self, executorQueue):
        print 'WindowsDebugEngine, replyServer():Waitting for reply from debugger'
        server = Server(REPLY_HOST, REPLY_PORT)
        server.accept()
        print 'WindowsDebugEngine, replyServer():got reply from debugger'
        executorQueue.put(server.recv())

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
