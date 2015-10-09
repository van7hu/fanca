
#
# This file implements a callback COM object for the DbgEng.  It
# implements the IDebugEventCallbacks interface.
#
# This also removes the dependency on native event proxy code and
# works with the latest comtypes.
#
# Copyright (c) Michael Eddington (mike@phed.org)
#
# Change log:
# 05/03/2008 - Initial version written
# 10/08/2009 - Updated to work with comtypes >= 0.5
#

###########################################################
# wait for event defines
###########################################################
INFINITE = -1

###########################################################
# path defines
###########################################################
MAX_PATH = 1024

###########################################################
# status codes
###########################################################
STRSAFE_E_INSUFFICIENT_BUFFER = -2147024774

###########################################################
# unicode string
###########################################################
OBJECT_ATTRIBUTES_OFFSET_TO_ROOT_HANDLE = 4
OBJECT_ATTRIBUTES_OFFSET_TO_OBJECT_NAME = 8
SIZE_OF_OBJECT_ATTRIBUTES = 12

UNICODE_STRING_OFFSET_TO_LENGTH     = 0
UNICODE_STRING_OFFSET_TO_MAX_SIZE   = 2
UNICODE_STRING_OFFSET_TO_BUFFER_PTR = 4
SIZE_OF_UNICODE_STRING = 8

###########################################################
class DebuggerException(Exception):
    message = None
    
    ###########################################################
    def __init__(self, message):
        self.message = message
        
    ###########################################################
    def __str__(self):
        return self.message

##
##
##

#import logging
#LOG_FILENAME = '/DbgEngEvent.out.txt'
#logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG,)

import comtypes
from ctypes import *
import comtypes.server
import comtypes.server.connectionpoints
from comtypes import HRESULT, COMError
from comtypes.client import CreateObject, GetEvents, ShowEvents
from comtypes.hresult import S_OK
from comtypes.automation import IID
from comtypes.gen import DbgEng
import comtypes.gen.DbgEng
import comtypes.server.localserver

import sys
import struct

from comtypes import CoClass, GUID
from PyDbgEng import PyDbgEng

from comtypes.gen import DbgEng

class DbgEngEventCallbacks(CoClass):
	
	_reg_clsid_ = GUID('{EAC5ACAA-7BD0-4f1f-8DEB-DF2862A7E85B}')
	_reg_threading_ = "Both"
	_reg_progid_ = "PyDbgEngLib.DbgEngEventCallbacks.1"
	_reg_novers_progid_ = "PyDbgEngLib.DbgEngEventCallbacks"
	_reg_desc_ = "Callback class!"
	_reg_clsctx_ = comtypes.CLSCTX_INPROC_SERVER
	
	_com_interfaces_ = [DbgEng.IDebugEventCallbacks, DbgEng.IDebugOutputCallbacks,
						comtypes.typeinfo.IProvideClassInfo2,
						comtypes.errorinfo.ISupportErrorInfo,
						comtypes.connectionpoints.IConnectionPointContainer]
	
	def IDebugOutputCallbacks_Output(self, arg1, arg2, arg3 = None):
		
		# >= v0.5.1
		if arg3 == None:
			unknown = None
			mask = arg1
			text = arg2
		# <= 0.4.2
		else:
			unknown = arg1
			mask = arg2
			text = arg3
		
		self._pyDbgEng = PyDbgEng.fuzzyWuzzy
		self._pyDbgEng.output_callbacks_sink.Output(unknown, mask, text)
		return S_OK
	
	def IDebugEventCallbacks_Breakpoint(self, unknown, bp = None):
		
		# >= v0.5.1
		if bp == None:
			bp = unknown
			unknown = None
		
		return self._pyDbgEng.Breakpoint(unknown, bp)
	
	def IDebugEventCallbacks_ChangeDebuggeeState(self, unknown, flags, arg = None):
		# >= v0.5.1
		if arg == None:
			arg = flags
			flags = unknown
			unknown = None
		
		return self._pyDbgEng.ChangeDebuggeeState(unknown, flags, arg)
	
	def IDebugEventCallbacks_ChangeEngineState(self, unknown, flags, arg = None):
		# >= v0.5.1
		if arg == None:
			arg = flags
			flags = unknown
			unknown = None
		
		return self._pyDbgEng.ChangeEngineState(unknown, flags, arg)
	
	def IDebugEventCallbacks_Exception(self, unknown, exception, firstChance = None):
		# >= v0.5.1:
		if firstChance == None:
			firstChance = exception
			exception = unknown
			unknown = None
		
		return self._pyDbgEng.Exception(unknown, exception, firstChance)
	
	def IDebugEventCallbacks_GetInterestMask(self, unknown = None, mask = None):
		# Superhack!
		self._pyDbgEng = PyDbgEng.fuzzyWuzzy
		
		# For v0.5.1 and on
		if unknown == None and mask == None:
			return self._pyDbgEng.GetInterestMask()
		
		# For v0.4 and lower
		mask[0] = self._pyDbgEng.GetInterestMask()
		return S_OK
	
	def IDebugEventCallbacks_LoadModule(self, unknown, imageFileHandle, baseOffset, moduleSize, moduleName, imageName, checkSum, timeDateStamp = None):
		# >= v0.5.1
		if timeDateStamp == None:
			timeDateStamp = checkSum
			checkSum = imageName
			imageName = moduleName
			moduleName = moduleSize
			moduleSize = baseOffset
			baseOffset = imageFileHandle
			imageFileHandle = unknown
			unknown = None
		
		return self._pyDbgEng.LoadModule(unknown, imageFileHandle, baseOffset, moduleSize, moduleName, imageName, checkSum, timeDateStamp)
	
	def IDebugEventCallbacks_UnloadModule(self, unknown, imageBaseName, baseOffset = None):
		# >= 0.5.1
		if baseOffset == None:
			baseOffset = imageBaseName
			imageBaseName = unknown
			unknown = None
		
		return self._pyDbgEng.UnloadModule(unknown, imageBaseName, baseOffset)
	
	def IDebugEventCallbacks_CreateProcess(self, unknown, imageFileHandle, handle, baseOffset, moduleSize,
										   moduleName, imageName, checkSum, timeDateStamp,
										   initialThreadHandle, threadDataOffset, startOffset = None):
		# >= 0.5.1
		if startOffset == None:
			startOffset = threadDataOffset
			threadDataOffset = initialThreadHandle
			initialThreadHandle = timeDateStamp
			timeDataStamp = checkSum
			checkSum = imageName
			imageName = moduleName
			moduleName = moduleSize
			moduleSize = baseOffset
			baseOffset = handle
			handle = imageFileHandle
			imageFileHandle = unknown
			unknown = None
			
		return self._pyDbgEng.CreateProcess(unknown, imageFileHandle, handle, baseOffset, moduleSize, moduleName, imageName, checkSum, timeDateStamp,
										   initialThreadHandle, threadDataOffset, startOffset)
	
	def IDebugEventCallbacks_ExitProcess(self, unknown, exitCode = None):
		# >= 0.5.1
		if exitCode == None:
			exitCode = unknown
			unknown = None
			
		return self._pyDbgEng.ExitProcess(unknown, exitCode)
	
	def IDebugEventCallbacks_SessionStatus(self, unknown, status = None):
		# >= 0.5.1
		if status == None:
			status = unknown
			unknown = None
			
		return self._pyDbgEng.SessionStatus(unknown, status)
	
	def IDebugEventCallbacks_ChangeSymbolState(self, unknown, flags, arg = None):
		# >= 0.5.1
		if arg == None:
			arg = flags
			flags = unknown
			unknown = None
		
		return self._pyDbgEng.ChangeSymbolState(unknown, flags, arg)
	
	def IDebugEventCallbacks_SystemError(self, unknown, error, level = None):
		# >= 0.5.1
		if level == None:
			level = error
			error = unknown
			unknown = None
			
		return self._pyDbgEng.SystemError(unknown, error, level)
	
	def IDebugEventCallbacks_CreateThread(self, unknown, handle, dataOffset, startOffset = None):
		# >= 0.5.1
		if startOffset == None:
			startOffset = dataOffset
			dataOffset = handle
			handle = unknown
			unknown = None
			
		return self._pyDbgEng.CreateThread(handle, unknown, dataOffset, startOffset)
	
	def IDebugEventCallbacks_ExitThread(self, unknown, exitCode = None):
		# >= 0.5.1
		if exitCode == None:
			exitCode = unknown
			unknown = None
			
		return self._pyDbgEng.ExitThread(unknown, exitCode)

if __name__ == "__main__":
    try:
        from comtypes.server.register import UseCommandLine
        UseCommandLine(DbgEngEventCallbacks)
    except Exception:
        import traceback
        traceback.print_exc()
        raw_input()

# end
