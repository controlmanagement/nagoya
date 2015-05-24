
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

# 3: PencReset
# ------------------
class PencReset_nChannel(pyinterface.Identifer):
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
    bits[6].set_params('CLK0', 'OFF', 'ON')
    bits[7].set_params('CLK1', 'OFF', 'ON')
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

# ==========================
# GPG-6204 Python 
# ==========================

class gpg7204(object):
    def __init__(self, ndev=1, remote=False):
        initialize = not remote
        self.ctrl = gpg6204_controller(ndev, initialize=initialize)
        pass

    def start












# ==========================
# GPG-6204 Python Controller
# ==========================

class gpg6204_controller(object):
    ndev = int()

    boardid = ''
    print_log = True
    
    def __init__(self, ndev=1, boardid=6204, initialize=True):
        """
        boardid = 6204
        """
        self.ndev = ndev
        self.boardid = BoardID.verify(boardid)
        if initialize: self.initialize()
        return

    def _log(self, msg):
        if self.print_log:
            print('Interface GPG6204(%d): %s'%(self.ndev, msg))
            pass
        return
    
    def _error_check(self, error_no):
        ErrorGPG6204.check(error_no)
        return
     
    def initialize(self):
        self.open()
        return
    
    def open(self, fulFlags):
        """
        1. PencOpen
        """
        self._log('open')
        fulFlags = PencOpen_fulFlags.verify(fulFlags)
        ret = lib.PencOpen(self.ndev, fulFlags)
        self._error_check(ret)
        return

    def close(self):
    	"""
        2. PencClose
        """
        self._log('close')
        ret = lib.PencClose(self.ndev)
        self._error_check(ret)
        return

    def reset(self, nChannel):
    	"""
        3. PencReset
        """
        self._log('reset')
        nChannel = PencReset_nChannel.verify(nChannel)
        ret = lib.PencReset(self.ndev, nChannel)
        self._error_check(ret)
        return

    def set_mode(self, nChannel, nMode, nDirection, nEqual, nLatch):
    	"""
        4. PencSetMode
        """
        self._log('set_mode')
        nChannel = PencSetMode_nChannel.verify(nChannel)
        nMode = PencSetMode_nMode.verify(nMode)
        nDirection = PencSetMode_nDirection.verify(nDirection)
        nEqual = PencSetMode_nEqual.verify(nEqual)
        nLatch = PencSetMode_nLatch.verify(nLatch)
        ret = lib.PencSetMode(self.ndev, nChannel, nMode, nDirection, nEqual, nLatch)
        self._error_check(ret)
        return

    def get_mode(self, nChannel):
    	"""
        5. PencGetMode
        """
        self._log('get_mode')
        nChannel = PencSetMode_nChannel.verify(nChannel)
        pnMode = ctypes.c_int(0)
        pnDirection = ctypes.c_int(0)
        pnEqual = ctypes.c_int(0)
        pnLatch = ctypes.c_int(0)
        ret = lib.PencGetMode(self.ndev, nChannel, nMode, nDirection, nEqual, nLatch)
        self._error_check(ret)
        pnMode = PencGetMode_nMode.verify(nMode)
        pnDirection = PencGetMode_nDirection.verify(nDirection)
        pnEqual = PencGetMode_nEqual.verify(nEqual)
        pnLatch = PencGetMode_nLatch.verify(nLatch)
        return [pnMode, pnDirection, pnEqual, pnLatch]
        
    def set_zmode(self, nChannel, nZMode):
    	"""
        6. PencSetZMode
        """
        self._log('set_zmode')
        nChannel = PencSetMode_nChannel.verify(nChannel)
        nZMode = PencSetZMode_nZMode.verify(nZMode)
        ret = lib.PencSetZMode(self.ndev, nChannel, nZMode)
        self._error_check(ret)
        return

    def get_zmode(self, nChannel):
    	"""
        7. PencGetZMode
        """
        self._log('get_zmode')
        nChannel = PencSetMode_nChannel.verify(nChannel)
        pnZMode = ctypes.c_int(0)
        ret = lib.PencGetZMode(self.ndev, nChannel, pnZMode)
        self._error_check(ret)
        pnZMode = PencGetZMode_pnMode.verify(pnZMode)
        return pnZMode

    def set_filter(self, nChannel, ulFilter):
    	"""
        8. PencSetFilter
        """
        self._log('set_filter')
        nChannel = PencSetMode_nChannel.verify(nChannel)
        ulFilter = PencSetFilter_ulFilter.verify(ulFilter)
        ret = lib.PenSetFilter(self.ndev, nChannel, ulFilter)
        self._error_check(ret)
        return

    def get_filter(self, nChannel):
    	"""
        9. PencGetFilter
        """  
        self._log('get_filter')
        nChannel = PencSetMode_nChannel.verify(nChannel)
        pulFilter = ctypes.c_int(0)
        ret = lib.PenGetFilter(self.ndev, nChannel, pulFilter)
        self._error_check(ret)
        pulFilter = PencGetFilter_pulFilter.verify(pulFilter)
        return pulFilter

    def enable_count(self, uChSel, nEnable):
    	"""
        10. PencEnableCount
        """
        self._log('enable_count')
        uChSel = PencEnableCount_uChSel.verify(uChSel)
        uEnable = PencEnableCount_uEnable.verify(uEnable)
        ret = lib.PencEnableCount(self.ndev, uChSel, uEnable)
        self._error_check(ret)
        return
    
    def set_reset_in_mask(self, bResetInMask):
    	"""
        11. PencSetResetInMask
        """
        self._log('set_reset_in_mask')
        bResetInMask = PencSetResetInMask_bResetInMask.verify(bResetInMask)
        ret = lib.PencSetResetInMask(self.ndev, bResetInMask)
        self._error_check(ret)
        return
    
    def get_reset_in_mask(self):
    	"""
        12. PencGetResetInMask
        """
        self._log('get_reset_in_mask')
        pbResetInMask = ctypes.c_ulong(0)
        ret = lib.PencGetResetInMask(self.ndev, pbResetInMask)
        self._error_check(ret)    
        pbResetInMask = PencGetResetInMask_pbResetInMask.verify(pbResetInMask)
        return pbResetInMask
    
    def set_counter(self, nChannel, ulCounter):
    	"""
        13. PencSetCounter
        """
        self._log('set_counter')
        nChannel = PencSetMode_nChannel.verify(nChannel)
        ulCounter = PencSetCounter_ulCounter.verify(ulCounter)
        ret = lib.PencSetCounter(self.ndev, nChannel, ulCounter)
        self._error_check(ret)
        return
    
    def get_counter(self, nChannel):
    	"""
        14. PencGetCounter
        """
        self._log('get_counter')
        nChannel = PencSetMode_nChannel.verify(nChannel)
        pulCounter = ctypes.c_ulong(0)
        ret = lib.PencGetCounter(self.ndev, nChannel, pulCounter)
        self._error_check(ret)
        pulCounter = PencGetCounter_pulCounter.verify(pulCounter)
        return pulCounter
        
    def set_counter_ex(self, nChSel, pulCounter):
    	"""
        15. PencSetCounterEx
        """
        self._log('set_counter_ex')
        pulCounter = PencSetCounterEx_pulCounter.verify(pulCounter)
        ret = lib.PencSetCounterEx(self.ndev, nChSel, pulCounter)
        self._error_check(ret)
        return
    
    def get_counter_ex(self, nChSel):
    	"""
        16. PencGetCounterEx
        """
        self._log('get_counter_ex')
        nChSel = PencGetCounterEx_nChSel.verify(nChSel)
        pulCounter = ctypes.c_ulong(0)
        ret = lib.PencGetCounterEx(self.ndev, nChSel, pulCounter)
        self._error_check(ret)
        pulCounter = PencGetCounterEx_pulCounter.verify(pulCounter)
        return pulCounter

    def set_comparator(self, nChannel, ulComparator):
    	"""
        17. PencSetComaparator
        """
        self._log('set_comparator')
        nChannel = PencSetMode_nChannel.verify(nChannel)
        ulComparator = PencSetComparator_ulComparator.verify(ulComparator)
        ret = lib.PencSetComaparator(self.ndev, nChannel, ulComparator)
        self._error_check(ret)
        return

    def get_comparator(self, nChannel):
    	"""
        18. PencGetComparator
        """
        self._log('get_comparator')
        nChannel = PencSetMode_nChannel.verify(nChannel)
        pulComparator = ctypes.c_ulong(0)
        ret = lib.PencGetComparator(self.ndev, nChannel, pulComparator)
        self._error_check(ret)
        pulComparator = PencGetComparator_pulComparator.verify(pulComparator)
        return pulComparator
       
    def get_status(self, nChannel):
    	"""
        19. PencGetStatus
        """
        self._log('get_status')
        nChannel = PencSetMode_nChannel.verify(nChannel)
        pnStatus = ctypes.c_int(0)
        ret = lib.PencGetStatus(self.ndev, nChannel, pnStatus)
        self._error_check(ret)
        pnStatus = PencGetStatus_pnStatus.verify(pnStatus)
        return pnStatus
       
    def get_status_ex(self, nChSel, pulCounter, pulStatus):
    	"""
        20. PencGetStatusEx
        """
        self._log('get_status_ex')
        nChSel = PencGetStatusEx_nChSel.verify(nChSel)
        pulCounter = ctypes.c_ulong(0)
        pulStatus = ctypes.c_ulong(0)
        ret = lib.PencGetStatusEx(self.ndev, nChSel, pulCounter, pulStatus)
        self._error_check(ret)
        pulCounter = PencGetStatusEx_pulCounter.verify(pulCounter)
        pulStatus = PencGetStatusEx_pulStatus.verify(pulStatus)
        return [pulCounter, pulStatus]
     
    def get_reset_in_status(self):
    	"""
        21. PencGetResetInStatus
        """
        self._log('get_reset_in_status')
        pbResetInStatus = ctypes.c_ubyte(0)
        ret = lib.PencGetResetInStatus(self.ndev, pbResetInStatus)
        self._error_check(ret)
        pbResetInStatus = PencGetResetInStatus_pbResetInStatus.verify(pbResetInStatus)
        return pbResetInStatus
    
    def input_di(self):
    	"""
        22. PencInputDI
        """
        self._log('input_di')
        pulValue = ctypes.c_ulong(0)
        ret = lib.PencInputDI(self.ndev, pulValue)
        self._error_check(ret)
        pulValue = PencInputDI_pulValue.verify(pulValue)
        return pulValue
    
    def output_do(self, ulValue):
    	"""
        23. PencOutputDO
        """
        self._log('output_do')
        ulValue = PencOutputDO_ulvalue.verify(ulValue)
        ret = lib.PencOutputDO(self.ndev, ulValue)
        self._error_check(ret)
        return
    
    def set_timer_config(self, ucTimerConfigValue):
    	"""
        24. PencSetTimerConfig
        """
        self._log('set_timer_config')
        ucTimerConfigValue = PencSetTimerConfig_ucTimerConfigValue.verify(ucTimerConfigValue)
        ret = lib.PencSetTimerConfig(self.ndev, ucTimerConfigValue)
        self._error_check(ret)
        return
    
    def get_timer_config(self):
    	"""
        25. PencGetTimerConfig
        """
        self._log('get_timer_config')
        pucTimerConfigValue = ctypes.c_ubyte(0)
        ret = lib.PencGetTimerConfig(self.ndev, pucTimerConfigValue)
        self._error_check(ret)
        pucTimerConfigValue = PencGetTimerConfig_pucTimerConfigValue.verify(pucTimerConfigValue)
        return　pucTimerConfigValue
    
    def get_timer_count(self):
    	"""
        26. PencGetTimerCount
        """
        self._log('get_timer_count')
        pucTimerCount = ctypes.c_ubyte(0)
        ret = lib.PencGetTimerCount(self.ndev, pucTimerCount)
        self._error_check(ret)
        pucTimerCount = PencGetTimerCount_pucTimerCount.verify(pucTimerCount)
        return pucTimerCount
    
    def set_event_mask(self, nChannel, nEventMask, nTimerMask):
    	"""
        27. PencSetEventMask
        """
        self._log('set_event_mask')
        nChannel = PencSetMode_nChannel.verify(nChannel)
        nEventMask = PencSetEventMask_nEventMask.verify(nEventMask)
        nTimerMask = PencSetEventMask_nTimerMask.verify(nTimerMask)
        ret = lib.PencSetEventMask(self.ndev, nChannel, nEventMask, nTimerMask)
        self._error_check(ret)
        return

    def get_event_mask(self, nChannel):
    	"""
        28. PencGetEventMask
        """
        self._log('get_event_mask')
        nChannel = PencSetMode_nChannel.verify(nChannel)
        pnEventMask = ctypes.c_int(0)
        pucTimerMask = ctypes.c_int(0)
        ret = lib.PencGetEventMask(self.ndev, nChannel, pnEventMask, pnTimerMask)
        self._error_check(ret)
        pnEventMask = PencGetEventMask_pnEventMask.verify(pnEventMask)
        pnTimerMask = PencGetEventMask_pnTimerMask.verify(pnTimerMask)
        return [pnEventMask, pnTimerMask]
    
    def set_event_ex(self, ipEventProEx, ulUser):
    	"""
        29. PencSetEventEx
        """
        self._log('set_event_ex')
        ipEventProEx = PencSetEventEx_ipEventProEx.verify(ipEventProEx)
        ulUser = PencSetEventEx_ulUser.verify(ulUser)
        ret = lib.PencSetEventEx(self.ndev, ipEventProEx, ulUser)
        self._error_check(ret)
        return

    def kill_event(self):
    	"""
        30. PencKillEvent
        """
        self._log('kill_event')
        ret = lib.PencKillEvent(self.ndev)
        self._error_check(ret)
        return

    def lp_event_proc_ex(self, ulEvent, ulUser):
    	"""
        31. lpEventProcEx
        """
        self._log('lp_event_proc_ex')
        ulEvent = lpEventProcEx_ulEvent.verify(ulEvent)
        ulUser = lpEventProcEx_ulUser.verify(ulUser)
        ret = lib.lpEventProcEx(self.nChannel, ulEvent, ulUser)
        self._error_check(ret)
        return

    



