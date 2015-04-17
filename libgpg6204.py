
import os
import ctypes
import pyinterface

# ==========
# Structures
# ==========

# ==========
# Identifers
# ==========

# 1: Penc Open
# =============

# Penc Open : fulFlags
# ------------------
PENC_FLAG_NORMAL = 
PENC_FLAG_SHARE = 



# =========
# Functions
# =========

SO_DIR = '/usr/lib'
SO_NAME = 'libgpg7204.so'
SO_PATH = os.path.join(SO_DIR, SO_NAME)

try:
    lib = ctypes.cdll.LoadLibrary(SO_PATH)
except OSError:
    pass
else:
    pyinterface.so_available.append(SO_PATH)
    
    _int = ctypes.c_int
    _uint = ctypes.c_uint
    _ulong = ctypes.c_float




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

    # 5 int PencGetMode(int, int, int, int, int, int);
    # ----------------
    PencGetMode = lib.PencGetMode
    PencGetMode.restype = _uint
    PencGetMode.argtypes = (_int, _int, _int, _int, _int, _int) 

    # 6 int PencSetZMode(int, int, int);
    # ----------------   
    PencSetZMode = lib.PencSetZode
    PencSetZMode.restype = _uint
    PencSetZMode.argtypes = (_int, _int, _int)





















