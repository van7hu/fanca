import PyDbgEng
from comtypes.gen import DbgEng
import threading

class DbgEventHandler(PyDbgEng.IDebugOutputCallbacksSink, PyDbgEng.IDebugEventCallbacksSink):
	def GetInterestMask(self):
		return PyDbgEng.DbgEng.DEBUG_EVENT_EXCEPTION | PyDbgEng.DbgEng.DEBUG_FILTER_INITIAL_BREAKPOINT | \
			PyDbgEng.DbgEng.DEBUG_EVENT_EXIT_PROCESS | PyDbgEng.DbgEng.DEBUG_EVENT_LOAD_MODULE
	def Output(self, this, Mask, Text):
		self.buff += Text
		#print self.buff
	def ExitProcess(self, dbg, ExitCode):
		print 'Debugger: Target application has exitted'
		return DEBUG_STATUS_NO_CHANGE
	def Exception(self, dbg, ExceptionCode, ExceptionFlags, ExceptionRecord,
		ExceptionAddress, NumberParameters, ExceptionInformation0, ExceptionInformation1,
		ExceptionInformation2, ExceptionInformation3, ExceptionInformation4,
		ExceptionInformation5, ExceptionInformation6, ExceptionInformation7,
		ExceptionInformation8, ExceptionInformation9, ExceptionInformation10,
		ExceptionInformation11, ExceptionInformation12, ExceptionInformation13,
		ExceptionInformation14, FirstChance):
		
		print 'DbgEventHandler.Exception: We got an exception, let us see it'
		if FirstChance:
			if ExceptionCode == 0xC0000005:
				print 'We should have something good, Exception code is 0xc0000005'
			else:
				print 'Exception code: ' + format(ExceptionCode, '08x')
		pass
class Debugger(object):
	def createDebugger(self, command, follow_fork):
		event_handler = DbgEventHandler()
		dbg = PyDbgEng.ProcessCreator(command, follow_fork, event_handler, event_handler, "SRV*http://msdl.microsoft.com/download/symbols")
		quit_event = threading.Event()
		dbg.event_loop_with_quit_event(quit_event)

