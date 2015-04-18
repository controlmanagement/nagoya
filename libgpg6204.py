
import os
import ctypes
import pyinterface

#
# 
#

# ==========
# Structures
# ==========

# function pointer
# ----------------
LPMTRCALLBACK = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_ulong, ctypes.c_ulong)

# ==========
# Identifers
# ==========

# 1: PencOpen
# =============

# PencOpen : fulFlags
# ------------------
PENC_FLAG_NORMAL = 
PENC_FLAG_SHARE = 


# 8: PencSetFilter
# =============

# PencSetFilter : nChannel
# ------------------
PENC_IN1_8 = 
PENC_IN9_16 = 


# 9: PencGetFilter
# =============

# PencGetFilter : nChannel
# ------------------
PENC_IN1_8 = 
PENC_IN9_16 = 


# 27: PencSetEventMask
# =============

# PencSetEventMask : nChannel
# ------------------
PENC_EVENT_BOARD = 
PENC_EVENT_DIO = 


# 28: PencGetEventMask
# =============

# PencGetEventMask : nChannel
# ------------------
PENC_EVENT_BOARD = 
PENC_EVENT_DIO = 

# =========
# Functions
# =========

SO_DIR = '/usr/lib'
SO_NAME = 'libgpg6204.so'
SO_PATH = os.path.join(SO_DIR, SO_NAME)

try:
    lib = ctypes.cdll.LoadLibrary(SO_PATH)
except OSError:
    pass
else:
    pyinterface.so_available.append(SO_PATH)
    
    _P = ctypes.POINTER
    _int = ctypes.c_int
    _int_p = _P(ctypes.c_int)
    _uint = ctypes.c_uint
    _ulong = ctypes.c_float
    _ulong_p = _P(ctypes.c_ulong)
    _ubyte = ctypes.c_ubyte
    _ubyte_p = _P(ctypes.c_ubyte)
    _void = 

    # 1 int PencOpen(int, unsigned long);
    # -------------------
    PencOpen = lib.PencOpen
    PencOpen.restype = _uint
    PencOpen.argtypes = (_int,　_ulong)

    # 2 int PencClose(int);
    # ----------------
    PencClose = lib.PencClose
    PencClose.restype = _uint
    PencClose.argtypes = (_int,)

    # 3 int PencReset(int, int);
    # ------------------
    PencReset = lib.PencReset
    PencReset.restype = _uint
    PencReset.argtypes = (_int, _int)

    # 4 int PencSetMode(int, int, int, int, int, int);
    # ------------------
    PencSetMode = lib.PencSetMode
    PencSetMode.restype = _uint
    PencSetMode.argtypes = (_int, _int, _int, _int, _int, _int) 

    # 5 int PencGetMode(int, int, int*, int*, int*, int*);
    # ----------------
    PencGetMode = lib.PencGetMode
    PencGetMode.restype = _uint
    PencGetMode.argtypes = (_int, _int, _int_p, _int_p, _int_p, _int_p) 

    # 6 int PencSetZMode(int, int, int);
    # ----------------   
    PencSetZMode = lib.PencSetZMode
    PencSetZMode.restype = _uint
    PencSetZMode.argtypes = (_int, _int, _int)

    # 7 int PencGetZMode(int, int, int*);
    # ----------------   
    PencGetZMode = lib.PencGetZMode
    PencGetZMode.restype = _uint
    PencGetZMode.argtypes = (_int, _int, _int_p)

    # 8 int PencSetFilter(int, int, unsigned long);
    # ----------------   
    PencSetFilter = lib.PencSetFilter
    PencSetFilter.restype = _uint
    PencSetFilter.argtypes = (_int, _int, _ulong)        

    # 9 int PencGetFilter(int, int, unsigned long*);
    # ----------------   
    PencGetFilter = lib.PencGetFilter
    PencGetFilter.restype = _uint
    PencGetFilter.argtypes = (_int, _int, _ulong_p) 

    # 10 int PencEnableCount(int, unsigned int, int);
    # ----------------   
    PencEnableCount = lib.PencEnableCount
    PencEnableCount.restype = _uint
    PencEnableCount.argtypes = (_int, _uint, _int)

    # 11 int PencSetResetInMask(int, unsigned char);
    # ----------------   
    PencSetResetInMask = lib.PencSetResetInMask
    PencSetResetInMask.restype = _uint
    PencSetResetInMask.argtypes = (_int, _ubyte)

    # 12 int PencGetResetInMask(int, unsigned char*);
    # ----------------   
    PencGetResetInMask = lib.PencGetResetInMask
    PencGetResetInMask.restype = _uint
    PencGetResetInMask.argtypes = (_int, _ubyte_p)

    # 13 int PencSetCounter(int, int, unsigned long);
    # ----------------   
    PencSetCounter = lib.PencSetCounter
    PencSetCounter.restype = _uint
    PencSetCounter.argtypes = (_int, _int, _ulong)

    # 14 int PencGetCounter(int, int, unsigned long*);
    # ----------------   
    PencGetCounter = lib.PencGetCounter
    PencGetCounter.restype = _uint
    PencGetCounter.argtypes = (_int, _int, _ulong_p)

    # 15 int PencSetCounterEx(int, unsigned int, unsigned long*);
    # ----------------   
    PencSetCounterEx = lib.PencSetCounterEx
    PencSetCounterEx.restype = _uint
    PencSetCounterEx.argtypes = (_int, _uint, _ulong_p)

    # 16 int PencGetCounterEx(int, unsigned int, unsigned long*);
    # ----------------   
    PencGetCounterEx = lib.PencSetCounterEx
    PencGetCounterEx.restype = _uint
    PencGetCounterEx.argtypes = (_int, _uint, _ulong_p)

    # 17 int PencSetComparator(int, int, unsigned long);
    # ----------------   
    PencSetComparator = lib.PencSetComparator
    PencSetComparator.restype = _uint
    PencSetComparator.argtypes = (_int, _int, _ulong)

    # 18 int PencGetComparator(int, int, unsigned long*);
    # ----------------   
    PencGetComparator = lib.PencGetComparator
    PencGetComparator.restype = _uint
    PencGetComparator.argtypes = (_int, _int, _ulong_p)

    # 19 int PencGetStatus(int, int, int*);
    # ----------------   
    PencGetStatus = lib.PencGetStatus
    PencGetStatus.restype = _uint
    PencGetStatus.argtypes = (_int, _int, _int_p)

    # 20 int PencGetStatusEx(int, unsigned int, unsigned long*, unsigned long*);
    # ----------------   
    PencGetStatusEx = lib.PencGetStatusEx
    PencGetStatusEx.restype = _uint
    PencGetStatusEx.argtypes = (_int, _uint, _ulong_p, _ulong_p)

    # 21 int PencGetResetInStatus(int, unsigned char*);
    # ----------------   
    PencGetResetInStatus = lib.PencGetResetInStatus
    PencGetResetInStatus.restype = _uint
    PencGetResetInStatus.argtypes = (_int, _ubyte_p)

    # 22 int PencInputDI(int, unsigned long*);
    # ----------------   
    PencInputDI = lib.PencInputDI
    PencInputDI.restype = _uint
    PencInputDI.argtypes = (_int, _ulong_p)

    # 23 int PencOutputDO(int, unsigned long);
    # ----------------   
    PencOutputDO = lib.PencOutputDO
    PencOutputDO.restype = _uint
    PencOutputDO.argtypes = (_int, _ulong)

    # 24 int PencSetTimerConfig(int, unsigned char);
    # ----------------   
    PencSetTimerConfig = lib.PencSetTimerConfig
    PencSetTimerConfig.restype = _uint
    PencSetTimerConfig.argtypes = (_int, _ubyte)

    # 25 int PencGetTimerConfig(int, unsigned char*);
    # ----------------   
    PencGetTimerConfig = lib.PencGetTimerConfig
    PencGetTimerConfig.restype = _uint
    PencGetTimerConfig.argtypes = (_int, _ubyte_p)

    # 26 int PencGetTimerCount(int, unsigned char*);
    # ----------------   
    PencGetTimerCount = lib.PencGetTimerCount
    PencGetTimerCount.restype = _uint
    PencGetTimerCount.argtypes = (_int, _ubyte_p)

    # 27 int PencSetEventMask(int, int, int, int);
    # ----------------   
    PencSetEventMask = lib.PencSetEventMask
    PencSetEventMask.restype = _uint
    PencSetEventMask.argtypes = (_int, _int, _int, _int)

    # 28 int PencGetEventMask(int, int, int*, int*);
    # ----------------   
    PencGetEventMask = lib.PencGetEventMask
    PencGetEventMask.restype = _uint
    PencGetEventMask.argtypes = (_int, _int, _int_p, _int_p)

    # 29 int PencSetEventEx(int, LPPENCCALLBACKEX, unsigned long);
    # ----------------   
    PencSetEventEx = lib.PencSetEventEx
    PencSetEventEx.restype = _uint
    PencSetEventEx.argtypes = (_int, _P(LPPENCCALLBACKEX), _ulong)

    # 30 int PencKillEvent(int);
    # ----------------   
    PencKillEvent = lib.PencKillEvent
    PencKillEvent.restype = _uint
    PencKillEvent.argtypes = (_int,)    

    # 31 void lpEventProcEx(int, unsigned long, unsigned long);
    # ----------------   
    lpEventProcEx = lib.lpEventProcEx
    lpEventProcEx.restype = _
    PencSetEventEx.argtypes = (_int, _ulong, _ulong)





