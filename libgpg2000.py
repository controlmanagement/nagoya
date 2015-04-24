
import os
import ctypes
import pyinterface




# ==========
# Structures
# ==========






# ==========
# Identifers
# ==========

FBIDIO_FLAG_SHARE = 1

# 5:DioInputByte
#===============

#nNo : 
#---------------
FBIDIO_IN1_8 = 0x00000001
FBIDIO_IN9_16 = 0x00000002
FBIDIO_IN17_24 = 0x00000004
FBIDIO_IN25_32 = 0x00000008
FBIDIO_IN33_40 = 0x00000010
FBIDIO_IN41_48 = 0x00000020
FBIDIO_IN49_56 = 0x00000040
FBIDIO_IN57_64 = 0x00000080


# 6: DioInputWord
#===============

#nNo : 
#---------------
FBIDIO_IN1_16 = 0x00000003
FBIDIO_IN17_32 = 0x0000000c
FBIDIO_IN33_48 = 0x00000030
FBIDIO_IN49_64 = 0x000000c0


# 7: DioInputDword
#===============

#nNo : 
#---------------
FBIDIO_IN1_32 = 0x0000000f
FBIDIO_IN33_64 = 0x000000f0


# 8: DioOutputByte
#===============

#nNo : 
#---------------
FBIDIO_OUT1_8 = 0x00000100
FBIDIO_OUT9_16 = 0x00000200
FBIDIO_OUT17_24 = 0x00000400
FBIDIO_OUT25_32 = 0x00000800
FBIDIO_OUT33_40 = 0x00001000
FBIDIO_OUT41_48 = 0x00002000
FBIDIO_OUT49_56 = 0x00004000
FBIDIO_OUT57_64 = 0x00008000


# 9: DioOutputWord
#===============

#nNo : 
#---------------
FBIDIO_OUT1_16 = 0x00000300
FBIDIO_OUT17_32 = 0x00000c00
FBIDIO_OUT33_48 = 0x00003000
FBIDIO_OUT49_64 = 0x0000c000


# 10: DioOutputDword
#===============

#nNo : 
#---------------
FBIDIO_OUT1_32 = 0x00000f00
FBIDIO_OUT33_64 = 0x0000f000


# 43: DioEintSetFilterConfig
#===============

#nNo : 
#---------------
FBIDIO_IRIN1_2_STB1 0x0000ffff


# 45: DioSetRstinMask
#===============

#ulRstinMask : 
#---------------
FBIDIO_RSTIN_MASK = 1

# 51: DioOutputSync
#===============

#Line : 
#---------------
FBIDIO_SYNC1 = 0
FBIDIO_SYNC2 = 1


# RETURN VALUE
# ============ 
FBIDIO_ERROR_SUCCESS = 0x00000000
FBIDIO_ERROR_NOT_DEVICE = 0xC0000001
FBIDIO_ERROR_NOT_OPEN = 0xC0000002
FBIDIO_ERROR_INVALID_DEVICE_NUMBER  = 0xC0000003
FBIDIO_ERROR_ALREADY_OPEN = 0xC0000004
FBIDIO_ERROR_NOT_SUPPORTED = 0xC0000009
FBIDIO_ERROR_PARAMETER = 0xC0001021
FBIDIO_ERROR_INVALID_CALL = 0xC0001002
FBIDIO_ERROR_USBIO_FAILED = 0xC0001085
FBIDIO_ERROR_USBIO_TIMEOUT = 0xC0001086
FBIDIO_ERROR_USBLIB_LOAD_FAILED = 0xC0001087
FBIDIO_ERROR_DEVICE_HANDLE = 0xFFFFFFFF


#================
#Function
#================

SO_DIR = '/usr/lib'
SO_NAME = 'libgpg2000.so'
SO_PATH = os.path.jpin(SO_DIR,SO_NAME)

try:
	lib = ctypes.cdll.LoadLibrary(SO_PATH)
except OSError:
	pass
else:
	pyinterface.so_available.append(SO_PATH)
	
	_P = ctypes.POINTER
	_char_p = ctypes.c_char_p
	_uchar = ctypes.c_ubyte
	_uchar_p = _P(ctypes.c_ubyte)
	_ushort = ctypes.c_ushort
	_ushort_p = _P(ctypes.c_ushort)
	_int = ctypes.c_int
	_int_p = _P(ctypes.c_int)
	_uint = ctypes.c_uint
	_long = ctypes.c_long
	_long_p = _P(ctypes.c_long)
	_ulong = ctypes.c_ulong
	_ulong_p = _P(ctypes.c_ulong)
	_float = ctypes.c_float
	_float_p = _P(ctypes.c_float)
	_void_p = ctypes.c_void_p

	#int DioOpen(int, unsigned long);
	#--------------------------------
	DioOpen = lib.DioOpen
	DioOpen.restype = _unit
	DioOpen.argtypes = (_int, _ulong)
	
	#int DioClose(int);
	#--------------------------------
	DioClose = lib.DioClose
	DioClose.restype = _unit
	DioClose.argtypes = (_int)
	
	#int DioInputPoint(int, int*, unsigned long, unsigned long);
	#---------------------------------
	DioInputPoint = lib.DioInputPoint
	DioInputPoint.restype = _unit
	DioInputPoint.argtypes = (_int, _int_p, _ulong, _ulong)
	
	#int DioOutputPoint(int, int*, unsigned long, unsigned long);
	#---------------------------------
	DioOutputPoint = lib.DioOutputPoint
	DioOutputPoint.restype = _unit
	DioOutputPoint.argtypes = (_int, _int, _ulong, _ulong)
	
	#int DioInputByte(int, int, unsigned char*);
	#---------------------------------
	DioInputByte = lib.DioInputByte
	DioInputByte.restype = _uint
	DioInputByte.argtypes = (_int, _int, _uchar_p)
	
	#int DioInputWord(int, int, unsigned short*);
	#----------------------------------
	DioInputWord = lib.DioInputWord
	DioInputWord.restype = _uint
	DioInputWord.argtypes = (_int, _int, _ushort_p)
	
	#int DioInputDword(int, int, unsigned long*);
	#----------------------------------
	DioInputDword =lib.DioInputDword
	DioInputDword.restype = _uint
	DioInputDword.argtypes = (_int, _int, _ulong_p)
	
	#int DioOutputByte(int, int, unsigned char);
	#----------------------------------
	DioOutputByte = lib.DioOutputByte
	DioOutputByte.restype = _uint
	DioOutputByte.argtypes = (_int, _int, _uchar)
	
	#int DioOutputWord(int, int, unsigned short);
	#----------------------------------
	DioOutputWord = lib.DioOutputWord
	DioOutputWord.restype = _uint
	DioOutputWord.argtypes = (_int, _int, _ushort)
	
	#int DioOutputDword(int, int, unsigned long);
	#----------------------------------
	DioOutputDword = lib.DioOutputDword
	DioOutputDword.restype = _unit
	DioOutputDword.argtypes = (_int, _int, _ulong)
	
	#int DioSetLatchStatus(int, unsigned char);
	#----------------------------------
	DioSetLatchStatus = lib.DioSetLatchStatus
	DioSetLatchStatus.restype = _uint
	DioSetLatchStatus.argtypes = (_int, _uchar)
	
	#int DioGetLatchStatus(int, unsigned char*);
	#----------------------------------
	DioGetLatchStatus = lib.DioGetLatchStatus
	DioGetLatchStatus.restype = _uint
	DioGetLatchStatus.argtypes = (_int, _uchar_p)
	
	#int DioGetAckStatus(int, unsigned char*);
	#----------------------------------
	DioGetAckStatus = lib.DioGetAckStatus
	DioGetAckStatus.restype = _uint
	DioGetACkStatus.argtypes = (_int, _uchar_p)
	
	#int DioSetAckPulseCommand(int, unsigned char);
	#----------------------------------
	DioSetAckPulseCommand = lib.DioSetACkPulseCommand
	DioSetAckPulseCommand.restype = _uint
	DioSetAckPulseCommand.argtypes = (_int, _uchar)
	
	#int DioGetStbStatus(int, unsigned char*);
	#----------------------------------
	DioGetStbStatus = lib.DioGetStbStatus
	DioGetStbStatus.restype = _uint
	DioGetStbStatus.argtype = (_int, _uchar_p)
	
	#int DioSetStbPulseCommand(int, unsigned char);
	#----------------------------------
	DioSetStbPulseCommand = lib.DioSetStbPulseCommand
	DioSetStbPulseCommand.restype = _uint
	DioSetStbPulseCommand.argtypes = (_int, _uchar)
	
	#int DioGetResetInStatus(int, unsigned char*);
	#----------------------------------
	DioGetResetInStatus = lib.DioGetResetInStatus
	DioGetResetInStatus.restype = _uint
	DioGetResetInStatus.argtypes = (_int, _uchar_p)
	
	#int DioSetIrqMask(int, unsigned char);
	#----------------------------------
	DioSetIrqMask = lib.DioSetIrqMask
	DioSetIrqMask.restype = _uint
	DioSetIrqMask.argtypes = (_int, _uchar)
	
	#int DioGetIrqMask(int, unsigned char*);
	#----------------------------------
	DioGetIrqMask = lib.DioGetIrqMask
	DioGetIrqMask.restype = _uint
	DioGetIrqMask.argtypes = (_int, _uchar_p)
	
	#int DioSetIrqConfig(int, unsigned char);
	#----------------------------------
	DioSetIrqConfig = lib.DioSetIrqConfig
	DioSetIrqConfig.restype = _uint
	DiosetIrqConfig.argtypes = (_int, _uchar)
	
	#int DioGetIrqConfig(int, unsigned char*);
	#----------------------------------
	DioGetIrqConfig = lib.DioGetIrqConfig
	DioGetIrqConfig.restype = _uint
	DioGetIrqConfig.argtypes = (_int, _uchar_p)
	
	#int DioRegistIsr(int, unsigned long, PDIOCALLBACK);
	#----------------------------------
	DioRegistIrq = lib.DioRegistIrq
	DioRegistIrq.restype = _uint
	DioRegistIrq.argtypes = (_int, _ulong, _P(PDIOCALLBACK))
	
	#int DioRegistIsrEx(int, unsigned long, PDIOCALLBACKEX);
	#----------------------------------
	DioRegistIsrEx = lib.DioRegistIsrEx
	DioRegistIsrEx.restype = _uint
	DioRegistIsrEx.argtypes = (_int, _ulong, _P(PDIOCALLBACKEX))
	
	#int DioEintRegistIsr(int, unsigned long, PDIOEINTCALLBACK);
	#----------------------------------
	DioEintRegistIsr = lib.DioEintRegistIsr
	DioEintRegistIsr.restype = _uint
	DioEintRegistIsr.argtypes = (_int, _ulong, _P(DIOEINTCALLBACK))
	
	#int DioGetDeviceConfig(int, unsigned long*);
	#----------------------------------
	DioGetDeviceConfig = lib.DioGetDeviceConfig
	DioGetDeviceConfig.restype = _uint
	DioGetDeviceConfig.argtypes = (_int, _ulong_p)
	
	#int DioGetDevieceConfigEx(int, unsigned long*, unsigned long*);
	#----------------------------------
	DioGetDeviceConfigEx = lib.DioGetDeviceConfigEx
	DioGetDeviceConfigEx.restype = _uint
	DioGetDeviceConfigEx.argtypes = (_int, _ulong_p, _ulong_p)
	
	#int DioCommonGetPciDeviceInfo(int, unsigned short*, unsigned short*, unsigned long*, unsigned char*, unsigned long*, unsigned long*, unsigned long*, unsigned long*, unsigned long*, unsigned long*, unsigned short*, unsigned short*, unsigned char*, unsigned long*)
	#----------------------------------
	DioCommonGetPciDeviceInfo = lib.DioCommonGetDeviceInfo
	DioCommonGetPciDeviceInfo.restype = _uint
	DioCommonGetPCiDeviceInfo.argtypes = (_int, _ushort_p, _ushort_p, _ulong_p, _uchar_p, _ulong_p, _ulong_p, _ulong_p, _ulong_p, _ulong_p, _ulong_p, _ushort_p, _ushort_p, _uchar_p, _ulong_p)
	
	#int DioSetTimerConfig(int, unsigned char);
	#----------------------------------
	DioSetTimerConfig = lib.DioSetTimerConfig
	DioSetTimerConfig.restype = _uint
	DioSetTimerConfig.argtypes = (_int, _uchar)
	
	#int DioGetTimerConfig(int, unsigned char*);
	#----------------------------------
	DiogetTimerConfig = lib.DioGetTimerConfig
	DioGEtTimerConfig.restype = _uint
	DioGetTimerConfig.argtypes = (_int, _uchar_p)
	
	#int DioGetTimerCount(int, unsigned char*);
	#----------------------------------
	DioGetTimerCount = lib.DioGetTimerCount
	DioGetTimetCount.restype = _uint
	DioGetTimerCount.argtypes = (_int, _uchar_p)
	
	#int DioEintSetIrqMask(int, unsigned long);
	#----------------------------------
	DioEintSetIrqMask = lib.DioEintSetIrqMask
	DioEintSetIrqMask.restype = _uint
	DioEintSetIrqMask.argtypes = (_int, _ulong)
	
	#int DioEintGetIrqMask(int, unsigned long*);
	#----------------------------------
	DioEintGetIrqMask = lib.DioEintSetIrqMask
	DioEintGetIrqMask.restype = _uint
	DioEintGetIrqMask.argtypes = (_int, _ulong)
	
	#int DioEintSetEdgeConfig(int, unsigned long, unsigned long);
	#----------------------------------
	DioEintSetEdgeConfig = lib.DioEintSetEdgeConfig
	DioEintSetEdgeConfig.restype = _uint
	DioEintSetEdgeConfig.argtypes = (_int, _ulong, _ulong)
	
	#int DioEintGetEdgeConfig(int, unsigned long*, unsigned long*);
	#----------------------------------
	DioEintGetEdgeConfig = lib.DioEintGetEdgeConfig
	DioEintGetEdgeConfig.restype = _uint
	DioEintGetEDgeConfig.argtypes = (_int, _ulong_p, _ulong_p)
	
	#int DioEintSetIrqMaskEx(int, int, unsigned long);
	#----------------------------------
	DioEintSetIrqMaskEx = lib.DioEintSetIrqMaskEx
	DioEintSetIrqMaskEx.restype = _uint
	DioEintSetIrqMaskEx.argtypes = (_int, _int, _ulong)
	
	#int DioEintGetIrqMaskEx(int, int, unsigned long*);
	#----------------------------------
	DioEintGetIrqMaskEx = lib.DioEintGetIrqMaskEx
	DioEintGetIrqMaskEx.restype = _uint
	DioEintGetIrqMaskEx.argtypes = (_int, _int, _ulong_p)
	
	#int DioEintSetEdgeConfigEx(int, int, unsigned long, unsigned long);
	#----------------------------------
	DioEintSetEdgeConfigEx = lib.DioEintSetEdgeConfigEx
	DioEintSetEdgeConfigEx.restype = _uint
	DioEintSetEdgeConfigEx.argtypes = (_int, _int, _ulong, _ulong)
	
	#int DioEintGetEdgeConfigEx(int, int, unsigned long*, unsigned long*);
	#----------------------------------
	DioEintGetEdgeConfigEx = lib.DioEintGetEdgeConfigEx
	DioEintGetEdgeConfigEx.restype = _uint
	DioEintGetEdgeConfigEx.argtypes = (_int, _int, _ulong_p, _ulong_p)
	
	#int DioEintInputPoint(int, int*, unsigned long, unsigned long);
	#----------------------------------
	DioEintInputPoint = lib.DioEintInputPoint
	DioEintInputPoint.restype = _uint
	DioEintInputPoint.argtypes = (_int, _int_p, _ulong, _ulong)
	
	#int DioEintInputByte(int, int, unsigned char*, unsigned char*);
	#----------------------------------
	DioEintInputByte = lib.DioEintInputByte
	DioEintInputByte.restype = _uint
	DioEintInputByte,argtypes = (_int, _int, _uchar_p, _uchar_p)
	
	#int DioEintInputWord(int, int, unsigned short*, unsigned short*);
	#----------------------------------
	DioEintInputWord = lib.DioEintInputWord
	DioEintInputWord.restype = _uint
	DioEintInputWord.argtypes = (_int, _int, _ushort_p, _ushort_p)
	
	#int DioEintInputDword(int, int, unsigned long*, unsigned long*);
	#----------------------------------
	DioEintInputDword = lib.DioEintInputDword
	DioEintInputDword.restype = _uint
	DioEintInputDword.argtypes = (_int, _int, _ulong_p, _ulong_p)
	
	#int DioEintSetFilterConfig(int, int, int);
	#----------------------------------
	DioEintSetFilterConfig = lib.DioEintSetFilterConfig
	DioEintSetFilterConfig.restype = _uint
	DioEintSetFilterConfig.argtypes = (_int, _int, _int)
	
	#int DioEintGetFilterConfig(int, int, int*);
	#----------------------------------
	DioEintGetFilterConfig = lib.DioEintGetFilterConfig
	DioEintGetFilterConfig.restype = _uint
	DioEintGetFilterConfig.argtypes = (_int, _int, _int_p)
	
	#int DioSetRstinMask(int, unsigned long);
	#----------------------------------
	DioSetRstinMask = lib.DioSetRstinMask
	DioSetRstinMask.restype = _uint
	DioSetRstinMask.argtypes = (_int, _ulong)
	
	#int DioGetRstinMask(int, unsigned long*);
	#----------------------------------
	DioGetRstinMask = lib.DioGetRstinMask
	DioGetRstinMask.restype = _uint
	DioGetRstinMask.argtypes = (_int, _ulong_p)
	
	#void CallBackProc(unsigned long, unsigned char, int);
	#----------------------------------
	CallBackProc = lib.CalBackProc
	CallBackProc.restype = _uint
	CallBackProc.argtypes = (_ulong, _uchar, _int)
	
	#void CallBackProcEx(unsigned long, unsigned char, unsigned long, unsigned long, int);
	#----------------------------------
	CallBackProcEx = lib.CallBackProcEx
	CallBackProcEx.restype = _uint
	CallBackProcEx.argtypes = (_ulong, _uchar, _ulong, _ulong, _int)
	
	#void EintCallBackProc(unsigned long, unsigned long*, int);
	#----------------------------------
	EintCallBackProc = lib.EintCallBackProc
	EintCallBaclProc.restype = _uint
	EintCallBackProc.argtypes = (_ulong, _ulong_p, _int)
	
	#void BGCallBackProc(unsigned short);
	#----------------------------------
	BGCallBackProc = lib.BGCallBackProc
	BGCallBackProc = _uint
	BGCallBackProc = (_uchar)
	
	#int DioOutputSync(int, int, unsigned long, unsigned long);
	#----------------------------------
	DioOutputSync = lib.DioOutputSync
	DioOutputSync.restype = _uint
	DioOutputSync.argtypes = (_int, _int, _ulong, _ulong)
	
	#int DioGetBackGroundUseTimer(int, int*);
	#----------------------------------
	DioGetBackGroundUseTimer = lib.DioGetBackGroundUseTimer
	DioGetBackGroundUseTimer.restype = _uint
	DioGetBackGroundUseTimer.argtypes = (_int, _int_p)
	
	#int DioSetBackGroundUseTimer(int, int);
	#----------------------------------
	DioSetBackGroundUseTimer = lib.DioSetBackGroundUseTimer
	DioSetBackGroundUseTimer.restype = _uint
	DioSetBackGroundUseTimer.argtypes = (_int, _int)
	
	#void DioSetBackGround(int, unsigned long, unsigned long, unsigned long, unsigned long, unsigned long, unsigned long);
	#----------------------------------
	DioSetBackGround = lib.DioSetBackGround
	DioSetBackGround.restype = _uint
	DioSetBackGround.argtypes = (_int, _ulong, _ulong, _ulong, _ulong, _ulong, _ulong)
	
	#int DioFreeBackGround(int, void*);
	#----------------------------------
	DioFreeBackGround = lib.DioFreeBackGround
	DioFreeBackGround.restype = _uint
	DioFreeBackGround,argtypes = (_int, _void_p)
	
	#int DioStopBackGround(int, void*);
	#----------------------------------
	DioStopBackGround = lib.DioStopBackGround
	DioStopBackGround.restype = _uint
	DioStopBackGround.argtypes = (_int, _void_p)
	
	#int DioGetBackGroundStatus(int, void*, unsigned long*, unsigned long*, unsigned long*, unsigned long*, unsigned long*, unsigned long*, unsigned long*, unsigned long*, unsigned long*, int*);
	#----------------------------------
	DioGetBackGroundStatus = lib.DioGetBackGroundStatus
	DioGetBackGroundStatus.restype = _unit
	DioGetBackGroundStatus.argtypes = (_int, _void_p, _ulong_p, _ulong_p, _ulong_p, _ulong_p, _ulong_p, _ulong_p, _ulong_p, _ulong_p, _ulong_p, _int_p)
	
	#int DioInputPointBack(int, void*, int*, unsigned long, LPDIOBGCALLBACK);
	#----------------------------------
	DioInputPointBack = lib.DioInputPointBack
	DioInputPointBack.restype = _uint
	DioInputPointBack.argtypes = (_int, _void_p, _int_p, _ulong_p, _P(LPDIOBGCALLBACK))
	
	#int DioOutputPointBack(int, void*, int*, unsigned long, LPDIOBGCALLBACK);
	#----------------------------------
	DioOutputPointBack = lib.DioOutputPointBack
	DioOutputPointBack.restype = _uint
	DioOutputPointBack.argtypes = (_int, _void_p, _int_p, _ulong, _P(LPDIOBGCALLBACK))
	













