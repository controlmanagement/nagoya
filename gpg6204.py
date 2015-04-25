
import sys
import time
import ctypes
import numpy

import pyinterface
import libgpg6204 as lib
pIE = pyinterface.IdentiferElement


# Identifer Wrapper
# =================

class BoardID(pyinterface.Identifer):
    id6204 = pIE('id6204', 6204)
    pass

# 1: PencOpen
# ------------------
class PencOpen_fulFlags(pyinterface.Identifer):
	PENC_FLAG_NORMAL = pIE('PENC_FLAG_NORMAL', lib.PENC_FLAG_NORMAL)
	PENC_FLAG_SHARE = pIE('PENC_FLAG_SHARE', lib.PENC_FLAG_SHARE)
	pass

# 4: PencSetMode
# ------------------
class PencSetMode_nMode(pyinterface.BitIdentifer):
    size = 32
    bits = [pyinterface.BitIdentiferElement(i) for i in range(size)]
    del(i)
    bits[0].set_params('SEL0', 'OFF', 'ON')
    bits[1].set_params('SEL1', 'OFF', 'ON')
    bits[2].set_params('MD0', 'OFF', 'ON')
    bits[3].set_params('MD1', 'OFF', 'ON')
    pass

# 6: PencSetZMode
# ------------------
class PencSetZMode_nZMode(pyinterface.BitIdentifer):
    size = 32
    bits = [pyinterface.BitIdentiferElement(i) for i in range(size)]
    del(i)
    bits[0].set_params('CLS0', 'OFF', 'ON')
    bits[1].set_params('CLS1', 'OFF', 'ON')
    bits[2].set_params('LTS0', 'OFF', 'ON')
    bits[3].set_params('LTS1', 'OFF', 'ON')
    bits[4].set_params('ZP', 'OFF', 'ON')
    bits[5].set_params('LP', 'OFF', 'ON')
    pass

# 8: PencSetFilter
# ------------------
class PencSetFilter_nChannel(pyinterface.Identifer):
	PENC_IN1_8 = pIE('PENC_IN1_8', lib.PENC_IN1_8)
	PENC_IN9_16 = pIE('PENC_IN9_16', lib.PENC_IN9_16)
	pass

class PencSetFilter_ulFilter(pyinterface.BitIdentifer):
    size = 32
    bits = [pyinterface.BitIdentiferElement(i) for i in range(size)]
    del(i)
    bits[0].set_params('CNT0', 'OFF', 'ON')
    bits[1].set_params('CNT1', 'OFF', 'ON')
    bits[2].set_params('CNT2', 'OFF', 'ON')
    bits[3].set_params('CNT3', 'OFF', 'ON')
    bits[4].set_params('CNT4', 'OFF', 'ON')
    bits[5].set_params('', 'OFF', 'ON')
    bits[6].set_params('CLK0', 'OFF', 'ON')
    bits[7].set_params('CLK1', 'OFF', 'ON')
    bits[8].set_params('', 'OFF', 'ON')
    bits[9].set_params('', 'OFF', 'ON')
    bits[10].set_params('', 'OFF', 'ON')
    bits[11].set_params('', 'OFF', 'ON')
    bits[12].set_params('', 'OFF', 'ON'))
    bits[13].set_params('', 'OFF', 'ON')
    bits[14].set_params('', 'OFF', 'ON')
    bits[15].set_params('', 'OFF', 'ON')
    bits[16].set_params('', 'OFF', 'ON')
    bits[17].set_params('', 'OFF', 'ON')
    bits[18].set_params('', 'OFF', 'ON')
    bits[19].set_params('', 'OFF', 'ON')
    bits[20].set_params('', 'OFF', 'ON')
    bits[21].set_params('', 'OFF', 'ON')
    bits[22].set_params('', 'OFF', 'ON')
    bits[23].set_params('', 'OFF', 'ON')
    bits[24].set_params('', 'OFF', 'ON')
    bits[25].set_params('', 'OFF', 'ON')
    bits[26].set_params('', 'OFF', 'ON')
    bits[27].set_params('', 'OFF', 'ON')
    bits[28].set_params('', 'OFF', 'ON')
    bits[29].set_params('', 'OFF', 'ON')
    bits[30].set_params('', 'OFF', 'ON')
    bits[31].set_params('', 'OFF', 'ON')
    pass

# 10: PencEnableCount
# ------------------
class PencEnableCount_nChSel(pyinterface.BitIdentifer):
    size = 32
    bits = [pyinterface.BitIdentiferElement(i) for i in range(size)]
    del(i)
    bits[0].set_params('CH1', 'OFF', 'ON')
    bits[1].set_params('CH2', 'OFF', 'ON')
    bits[2].set_params('CH3', 'OFF', 'ON')
    bits[3].set_params('CH4', 'OFF', 'ON')
    bits[4].set_params('CH5', 'OFF', 'ON')
    bits[5].set_params('CH6', 'OFF', 'ON')
    bits[6].set_params('CH7', 'OFF', 'ON')
    bits[7].set_params('CH8', 'OFF', 'ON')
    bits[8].set_params('', 'OFF', 'ON')
    bits[9].set_params('', 'OFF', 'ON')
    bits[10].set_params('', 'OFF', 'ON')
    bits[11].set_params('', 'OFF', 'ON')
    bits[12].set_params('', 'OFF', 'ON'))
    bits[13].set_params('', 'OFF', 'ON')
    bits[14].set_params('', 'OFF', 'ON')
    bits[15].set_params('', 'OFF', 'ON')
    bits[16].set_params('', 'OFF', 'ON')
    bits[17].set_params('', 'OFF', 'ON')
    bits[18].set_params('', 'OFF', 'ON')
    bits[19].set_params('', 'OFF', 'ON')
    bits[20].set_params('', 'OFF', 'ON')
    bits[21].set_params('', 'OFF', 'ON')
    bits[22].set_params('', 'OFF', 'ON')
    bits[23].set_params('', 'OFF', 'ON')
    bits[24].set_params('', 'OFF', 'ON')
    bits[25].set_params('', 'OFF', 'ON')
    bits[26].set_params('', 'OFF', 'ON')
    bits[27].set_params('', 'OFF', 'ON')
    bits[28].set_params('', 'OFF', 'ON')
    bits[29].set_params('', 'OFF', 'ON')
    bits[30].set_params('', 'OFF', 'ON')
    bits[31].set_params('', 'OFF', 'ON')
    pass

# 15: PencSetCounterEx
# ------------------
class PencSetCounterEx_nChSel(pyinterface.BitIdentifer):
    size = 32
    bits = [pyinterface.BitIdentiferElement(i) for i in range(size)]
    del(i)
    bits[0].set_params('CH1', 'OFF', 'ON')
    bits[1].set_params('CH2', 'OFF', 'ON')
    bits[2].set_params('CH3', 'OFF', 'ON')
    bits[3].set_params('CH4', 'OFF', 'ON')
    bits[4].set_params('CH5', 'OFF', 'ON')
    bits[5].set_params('CH6', 'OFF', 'ON')
    bits[6].set_params('CH7', 'OFF', 'ON')
    bits[7].set_params('CH8', 'OFF', 'ON')
    bits[8].set_params('', 'OFF', 'ON')
    bits[9].set_params('', 'OFF', 'ON')
    bits[10].set_params('', 'OFF', 'ON')
    bits[11].set_params('', 'OFF', 'ON')
    bits[12].set_params('', 'OFF', 'ON'))
    bits[13].set_params('', 'OFF', 'ON')
    bits[14].set_params('', 'OFF', 'ON')
    bits[15].set_params('', 'OFF', 'ON')
    bits[16].set_params('', 'OFF', 'ON')
    bits[17].set_params('', 'OFF', 'ON')
    bits[18].set_params('', 'OFF', 'ON')
    bits[19].set_params('', 'OFF', 'ON')
    bits[20].set_params('', 'OFF', 'ON')
    bits[21].set_params('', 'OFF', 'ON')
    bits[22].set_params('', 'OFF', 'ON')
    bits[23].set_params('', 'OFF', 'ON')
    bits[24].set_params('', 'OFF', 'ON')
    bits[25].set_params('', 'OFF', 'ON')
    bits[26].set_params('', 'OFF', 'ON')
    bits[27].set_params('', 'OFF', 'ON')
    bits[28].set_params('', 'OFF', 'ON')
    bits[29].set_params('', 'OFF', 'ON')
    bits[30].set_params('', 'OFF', 'ON')
    bits[31].set_params('', 'OFF', 'ON')
    pass

# 19: PencGetStatus
# ------------------
class PencGetStatus_pnStatus(pyinterface.BitIdentifer):
    size = 32
    bits = [pyinterface.BitIdentiferElement(i) for i in range(size)]
    del(i)
    bits[0].set_params('A', 'High', 'Low')
    bits[1].set_params('B', 'High', 'Low')
    bits[2].set_params('Z', 'High', 'Low')
    bits[3].set_params('L1', 'High', 'Low')
    bits[4].set_params('L2', 'High', 'Low')
    bits[5].set_params('L3', 'High', 'Low')
    bits[8].set_params('CBF', 'OFF', 'ON')
    bits[9].set_params('EQ', 'disagreement', 'agreement')
    bits[10].set_params('EXLTS', 'OFF', 'ON')
    bits[11].set_params('EQF', 'disagreement', 'agreement')
    bits[12].set_params('PERR', 'OFF', 'ON')  
    pass

# 20: PencGetStatus
# ------------------
class PencGetStatusEx_nChSel(pyinterface.BitIdentifer):
    size = 32
    bits = [pyinterface.BitIdentiferElement(i) for i in range(size)]
    del(i)
    bits[0].set_params('CH1', 'OFF', 'ON')
    bits[1].set_params('CH2', 'OFF', 'ON')
    bits[2].set_params('CH3', 'OFF', 'ON')
    bits[3].set_params('CH4', 'OFF', 'ON')
    bits[4].set_params('CH5', 'OFF', 'ON')
    bits[5].set_params('CH6', 'OFF', 'ON')
    bits[6].set_params('CH7', 'OFF', 'ON')
    bits[7].set_params('CH8', 'OFF', 'ON')
    bits[8].set_params('', 'OFF', 'ON')
    bits[9].set_params('', 'OFF', 'ON')
    bits[10].set_params('', 'OFF', 'ON')
    bits[11].set_params('', 'OFF', 'ON')
    bits[12].set_params('', 'OFF', 'ON')
    bits[13].set_params('', 'OFF', 'ON')
    bits[14].set_params('', 'OFF', 'ON')
    bits[15].set_params('', 'OFF', 'ON')
    bits[16].set_params('', 'OFF', 'ON')
    bits[17].set_params('', 'OFF', 'ON')
    bits[18].set_params('', 'OFF', 'ON')
    bits[19].set_params('', 'OFF', 'ON')
    bits[20].set_params('', 'OFF', 'ON')
    bits[21].set_params('', 'OFF', 'ON')
    bits[22].set_params('', 'OFF', 'ON')
    bits[23].set_params('', 'OFF', 'ON')
    bits[24].set_params('', 'OFF', 'ON')
    bits[25].set_params('', 'OFF', 'ON')
    bits[26].set_params('', 'OFF', 'ON')
    bits[27].set_params('', 'OFF', 'ON')
    bits[28].set_params('', 'OFF', 'ON')
    bits[29].set_params('', 'OFF', 'ON')
    bits[30].set_params('', 'OFF', 'ON')
    bits[31].set_params('', 'OFF', 'ON')
    pass

class PencGetStatusEx_pulStatus(pyinterface.BitIdentifer):
    size = 32
    bits = [pyinterface.BitIdentiferElement(i) for i in range(size)]
    del(i)
    bits[0].set_params('A', 'High', 'Low')
    bits[1].set_params('B', 'High', 'Low')
    bits[2].set_params('Z', 'High', 'Low')
    bits[3].set_params('L1', 'High', 'Low')
    bits[4].set_params('L2', 'High', 'Low')
    bits[5].set_params('L3', 'High', 'Low')
    bits[8].set_params('CBF', 'OFF', 'ON')
    bits[9].set_params('EQ', 'disagreement', 'agreement')
    bits[10].set_params('EXLTS', 'OFF', 'ON')
    bits[11].set_params('EQF', 'disagreement', 'agreement')
    bits[12].set_params('PERR', 'OFF', 'ON')  
    pass

# 22: PencInputDI
# ------------------
class PencInputDI_pulValue(pyinterface.BitIdentifer):
    size = 32
    bits = [pyinterface.BitIdentiferElement(i) for i in range(size)]
    del(i)
    bits[0].set_params('IN1', 'High', 'Low')
    bits[1].set_params('IN2', 'High', 'Low')
    bits[2].set_params('IN3', 'High', 'Low')
    bits[3].set_params('IN4', 'High', 'Low')
    bits[4].set_params('IN5', 'High', 'Low')
    bits[5].set_params('IN6', 'High', 'Low')
    bits[6].set_params('IN7', 'High', 'Low')
    bits[7].set_params('IN8', 'High', 'Low')
    bits[8].set_params('IN9', 'High', 'Low')
    bits[9].set_params('IN10', 'High', 'Low')
    bits[10].set_params('IN11', 'High', 'Low')  
    bits[11].set_params('IN12', 'High', 'Low')
    bits[12].set_params('IN13', 'High', 'Low')
    bits[13].set_params('IN14', 'High', 'Low')
    bits[14].set_params('IN15', 'High', 'Low')
    bits[15].set_params('IN16', 'High', 'Low')  
    pass

# 24: PencSetTimerConfig
# ------------------
class PencSetTimerConfig_ucTimerConfigValue(pyinterface.BitIdentifer):
    size = 32
    bits = [pyinterface.BitIdentiferElement(i) for i in range(size)]
    del(i)
    bits[0].set_params('CTL1', 'OFF', 'ON')
    bits[1].set_params('CTL2', 'OFF', 'ON')
    bits[2].set_params('CTL3', 'OFF', 'ON')
    bits[3].set_params('CTL4', 'OFF', 'ON')
    bits[4].set_params('CTL5', 'OFF', 'ON')
    bits[5].set_params('CTL6', 'OFF', 'ON')
    bits[6].set_params('CTL7', 'OFF', 'ON')
    pass

# 26: PencGetTimerCount
# ------------------
class PencGetTimerCount_pucTimerCount(pyinterface.BitIdentifer):
    size = 32
    bits = [pyinterface.BitIdentiferElement(i) for i in range(size)]
    del(i)
    bits[0].set_params('TD1', 'High', 'Low')
    bits[1].set_params('TD2', 'High', 'Low')
    bits[2].set_params('TD3', 'High', 'Low')
    bits[3].set_params('TD4', 'High', 'Low')
    pass

# 27: PencSetEventMask
# ------------------
class PencSetEventMask_nDevice(pyinterface.Identifer):
	PENC_EVENT_BOARD = pIE('PENC_EVENT_BOARD', lib.PENC_EVENT_BOARD)
	PENC_EVENT_DIO = pIE('PENC_EVENT_DIO', lib.PENC_EVENT_DIO)
	pass

class PencSetEventMask_nChannel(pyinterface.BitIdentifer):
    size = 32
    bits = [pyinterface.BitIdentiferElement(i) for i in range(size)]
    del(i)
    bits[0].set_params('SU_IN1', 'Mask', 'unMask')
    bits[1].set_params('SU_IN2', 'Mask', 'unMask')
    bits[2].set_params('SU_IN3', 'Mask', 'unMask')
    bits[3].set_params('SU_IN4', 'Mask', 'unMask')
    bits[4].set_params('SU_IN5', 'Mask', 'unMask')
    bits[5].set_params('SU_IN6', 'Mask', 'unMask')
    bits[6].set_params('SU_IN7', 'Mask', 'unMask')
    bits[7].set_params('SU_IN8', 'Mask', 'unMask')
    bits[8].set_params('SU_IN9', 'Mask', 'unMask')
    bits[9].set_params('SU_IN10', 'Mask', 'unMask')
    bits[10].set_params('SU_IN11', 'Mask', 'unMask')
    bits[11].set_params('SU_IN12', 'Mask', 'unMask')
    bits[12].set_params('SU_IN13', 'Mask', 'unMask')
    bits[13].set_params('SU_IN14', 'Mask', 'unMask')
    bits[14].set_params('SU_IN15', 'Mask', 'unMask')
    bits[15].set_params('SU_IN16', 'Mask', 'unMask')
    bits[16].set_params('SD_IN1', 'Mask', 'unMask')
    bits[17].set_params('SD_IN2', 'Mask', 'unMask')
    bits[18].set_params('SD_IN3', 'Mask', 'unMask')
    bits[19].set_params('SD_IN4', 'Mask', 'unMask')
    bits[20].set_params('SD_IN5', 'Mask', 'unMask')
    bits[21].set_params('SD_IN6', 'Mask', 'unMask')
    bits[22].set_params('SD_IN7', 'Mask', 'unMask')
    bits[23].set_params('SD_IN8', 'Mask', 'unMask')
    bits[24].set_params('SD_IN9', 'Mask', 'unMask')
    bits[25].set_params('SD_IN10', 'Mask', 'unMask')
    bits[26].set_params('SD_IN11', 'Mask', 'unMask')
    bits[27].set_params('SD_IN12', 'Mask', 'unMask')
    bits[28].set_params('SD_IN13', 'Mask', 'unMask')
    bits[29].set_params('SD_IN14', 'Mask', 'unMask')
    bits[30].set_params('SD_IN15', 'Mask', 'unMask')
    bits[31].set_params('SD_IN16', 'Mask', 'unMask')
    pass


# Error Wrapper
# =============
class ErrorGPG7204(pyinterface.ErrorCode):
	PENC_ERROR_SUCCESS = pIE('PENC_ERROR_SUCCESS', lib.PENC_ERROR_SUCCESS)
	PENC_ERROR_NOT_DEVICE = pIE('PENC_ERROR_NOT_DEVICE', lib.PENC_ERROR_NOT_DEVICE)
    PENC_ERROR_NOT_OPEN = pIE('PENC_ERROR_NOT_OPEN',lib.PENC_ERROR_NOT_OPEN)
    PENC_ERROR_INVALID_DEVICE_NUMBER = pIE('PENC_ERROR_INVALID_DEVICE_NUMBER',lib.PENC_ERROR_INVALID_DEVICE_NUMBER)
    PENC_ERROR_ALREADY_OPEN = pIE('PENC_ERROR_ALREADY_OPEN',lib.PENC_ERROR_ALREADY_OPEN)
    PENC_ERROR_NOT_SUPPORTED = pIE('PENC_ERROR_NOT_SUPPORTED',lib.PENC_ERROR_NOT_SUPPORTED)
    PENC_ERROR_INITIALIZE_IRQ = pIE('PENC_ERROR_INITIALIZE_IRQ',lib.PENC_ERROR_INITIALIZE_IRQ)
    PENC_ERROR_INVALID_CHANNEL = pIE('PENC_ERROR_INVALID_CHANNEL',lib.PENC_ERROR_INVALID_CHANNEL)
    PENC_ERROR_INVALID_MODE = pIE('PENC_ERROR_INVALID_MODE',lib.PENC_ERROR_INVALID_MODE)
    PENC_ERROR_INVALID_DIRECT = pIE('PENC_ERROR_INVALID_DIRECT',lib.PENC_ERROR_INVALID_DIRECT)
    PENC_ERROR_INVALID_EQUALS = pIE('PENC_ERROR_INVALID_EQUALS',lib.PENC_ERROR_INVALID_EQUALS)
    PENC_ERROR_INVALID_LATCH = pIE('PENC_ERROR_INVALID_LATCH', lib.PENC_ERROR_INVALID_LATCH)
    PENC_ERROR_INVALID_COUNTER = pIE('PENC_ERROR_INVALID_COUNTER', lib.PENC_ERROR_INVALID_COUNTER)
    PENC_ERROR_INVALID_COMPARATOR = pIE('PENC_ERROR_INVALID_COMPARATOR',lib.PENC_ERROR_INVALID_COMPARATOR)
    PENC_ERROR_PENC_ERROR_INVALID_ZMODE = pIE('PENC_ERROR_INVALID_ZMODE',lib.PENC_ERROR_INVALID_ZMODE)
    PENC_ERROR_INVALID_MASK = pIE('PENC_ERROR_INVALID_MASK',lib.PENC_ERROR_INVALID_MASK)
    PENC_ERROR_INVALID_ITIMER = pIE('PENC_ERROR_INVALID_ITIMER',lib.PENC_ERROR_INVALID_ITIMER)
    PENC_ERROR_ALREADY_REGISTRATION = pIE('PENC_ERROR_ALREADY_REGISTRATION',lib.PENC_ERROR_ALREADY_REGISTRATION)
    PENC_ERROR_ALREADY_DELETE = pIE('PENC_ERROR_ALREADY_DELETE',lib.PENC_ERROR_ALREADY_DELETE)
    PENC_ERROR_MEMORY_NOTALLOCATED = pIE('PENC_ERROR_MEMORY_NOTALLOCATED',lib.PENC_ERROR_MEMORY_NOTALLOCATED)
    PENC_ERROR_DRVCAL = pIE('PENC_ERROR_DRVCAL',lib.PENC_ERROR_DRVCAL)
    PENC_ERROR_NULL_POINTER = pIE('PENC_ERROR_NULL_POINTER',lib.PENC_ERROR_NULL_POINTER)
    PENC_ERROR_PARAMETER = pIE('PENC_ERROR_PARAMETER',lib.PENC_ERROR_PARAMETER)
    PENC_ERROR_INVALID_FILTER = pIE('PENC_ERROR_INVALID_FILTER',lib.PENC_ERROR_INVALID_FILTER)
    PENC_ERROR_INVALID_DO = pIE('PENC_ERROR_INVALID_DO',lib.PENC_ERROR_INVALID_DO)
    PENC_ERROR_INVALID_RSTINMASK = pIE('PENC_ERROR_INVALID_RSTINMASK',lib.PENC_ERROR_INVALID_RSTINMASK)

    _success = PENC_ERROR_SUCCESS
    pass

    
