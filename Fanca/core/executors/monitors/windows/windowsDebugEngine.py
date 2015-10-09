import psutil, thread, time
from Fanca.core.executors.monitors.windows.debugger import Debugger
from Fanca.CONFIG import *
from Fanca.commons.jsonsocket import Server, Client

class WindowsDebugEngine:
    def __init__(self, server, configOptions):
        print 'WindowsDebugEngine: Start waitting for command'

        command = configOptions.command
        if configOptions.follow_fork == 'True':
            follow_fork = True
        else:
            follow_fork = False
        process_name = configOptions.process_name

        normal_data = {'fin': 'normal'}
        exception_data = {'fin': 'exception'}
        connection_counter = 0
        while True:
            server.accept()
            connection_counter = connection_counter + 1
            print str(connection_counter) + '. WindowsDebugEngine: Receiving connection'
            recv = server.recv()
            if recv['cmd'] == 'run':
                print 'WindowsDebugEngine: Got request to run the debugger'
                thread.start_new_thread(self.runCommand, (command, follow_fork))
                time.sleep(0.25)

                print "WindowsDebugEngine: Old thread checks for CPU usage by process '" + process_name + "', if it is zero, process will be killed"
                self.checkProcessCpuUsageAndKill(process_name)
                wdClient = Client()
                try:
                    wdClient.connect(MANAGEMENT_ENGINE_HOST, MANAGEMENT_ENGINE_PORT)
                    wdClient.send({'fin': 'normal'})
                except Exception, e:
                    print 'WindowsDebugEngine: ' + str(e)

    def runCommand(self, command, follow_fork):
        debugger = Debugger()
        print 'WindowsDebugEngine: Start new thread to run the debugger'
        print 'Command: '+command
        debugger.createDebugger(command, follow_fork)


    # some helper functions
    def checkProcessCpuUsageAndKill(self, process_name):
        pid = self.findProcess(process_name)

        cpu_index = 0
        if pid != 0:
            while cpu_index < DEBUG_ENGINE_CPU_COUNTER:
                x = psutil.Process(pid).get_cpu_percent(1)
                if x > 0:
                    print 'WindowsDebugEngine: CPU times is greater than zero, reset cpu_index back to 0 (' + str(x) + ')'
                    cpu_index = 0
                else:
                    cpu_index = cpu_index + 1
                    print 'WindowsDebugEngine: cpu_index = ' + str(cpu_index)
                time.sleep(0.25)
            print 'WindowsDebugEngine: cpu_index has eslapsed, kill process now'
            self.killProcess(pid)
    def findProcess(self, name):
        pid = 0
        for proc in psutil.process_iter():
            if proc.name == name:
                pid = proc.pid

        return pid

    def killProcess(self, pid):
        print 'WindowsDebugEngine: Trying to kill process'
        try:
            psutil.Process(pid).kill()
            print 'WindowsDebugEngine: Process killed'
        except:
            print 'WindowsDebugEngine: Could not kill process'
