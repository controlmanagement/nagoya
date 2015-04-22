
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
class PencGetStatus_pnStatus*(pyinterface.BitIdentifer):
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




# 27: PencSetEventMask
# ------------------
class PencSetEventMask(pyinterface.Identifer):
	PENC_EVENT_BOARD = pIE('PENC_EVENT_BOARD', lib.PENC_EVENT_BOARD)
	PENC_EVENT_DIO = pIE('PENC_EVENT_DIO', lib.PENC_EVENT_DIO)
	pass

