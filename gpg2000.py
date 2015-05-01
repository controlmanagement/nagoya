
import sys
import time
import ctypes
import numpy

import pyinterface
import libgpg2000 as lib
pIE = pyinterface.IdentiferElement


# Identifer Wrapper
# =================

class BoardID(pyinterface.Identifer):
    id2724 = pIE('id2724', 2724)
    pass


# 3: DioInputPoint
# ------------------
class InputPoint(pyinterface.Identifer):
	size = 32
	bits = [pyinterface.BitIdentiferElement(i) for i in range(size)]
	del(i)
	bits[0].set_params('OUT1', 'ENABLED', 'DISABLED')
	bits[1].set_params('OUT2', 'ENABLED', 'DISABLED')
	bits[2].set_params('OUT3', 'ENABLED', 'DISABLED')
	bits[3].set_params('OUT4', 'ENABLED', 'DISABLED')
	bits[4].set_params('OUT5', 'ENABLED', 'DISABLED')
	bits[5].set_params('OUT6', 'ENABLED', 'DISABLED')
	bits[6].set_params('OUT7', 'ENABLED', 'DISABLED')
	bits[7].set_params('OUT8', 'ENABLED', 'DISABLED')
	bits[8].set_params('SIG1', 'ENABLED', 'DISABLED')
	bits[9].set_params('SIG2', 'ENABLED', 'DISABLED')
	bits[10].set_params('SIG3', 'ENABLED', 'DISABLED')
	bits[11].set_params('SIG4', 'ENABLED', 'DISABLED')
	bits[12].set_params('SIG5', 'ENABLED', 'DISABLED')
	bits[13].set_params('SIG6', 'ENABLED', 'DISABLED')
	bits[14].set_params('SIG7', 'ENABLED', 'DISABLED')
	bits[15].set_params('SIG8', 'ENABLED', 'DISABLED')
	bits[16].set_params('SIG1', 'ENABLED', 'DISABLED')
	bits[17].set_params('SIG2', 'ENABLED', 'DISABLED')
	bits[18].set_params('SIG3', 'ENABLED', 'DISABLED')
	bits[19].set_params('SIG4', 'ENABLED', 'DISABLED')
	bits[20].set_params('SIG5', 'ENABLED', 'DISABLED')
	bits[21].set_params('SIG6', 'ENABLED', 'DISABLED')
	bits[22].set_params('SIG7', 'ENABLED', 'DISABLED')
	bits[23].set_params('SIG8', 'ENABLED', 'DISABLED')
	bits[24].set_params('IN', 'ENABLED', 'DISABLED')
	pass

# 5: DioInputByte
# ------------------
class InputByteMode(pyinterface.Identifer):
	FBIDIO_IN1_8 = pIE('FBIDIO_IN1_8', lib.FBIDIO_IN1_8)
	FBIDIO_IN9_16 = pIE('FBIDIO_IN9_16', lib.FBIDIO_IN9_16)
	FBIDIO_IN17_24 = pIE('FBIDIO_IN17_24', lib.FBIDIO_IN17_24)
	FBIDIO_IN25_32 = pIE('FBIDIO_IN25_32', lib.FBIDIO_IN25_32)
	FBIDIO_IN33_40 = pIE('FBIDIO_IN33_40', lib.FBIDIO_IN33_40)
	FBIDIO_IN41_48 = pIE('FBIDIO_IN41_48', lib.FBIDIO_IN41_48)
	FBIDIO_IN49_56 = pIE('FBIDIO_IN49_56', lib.FBIDIO_IN49_56)
	FBIDIO_IN57_64 = pIE('FBIDIO_IN57_64', lib.FBIDIO_IN57_64)
	pass

# 6: DioInputWord
# ------------------
class InputWordMode(pyinterface.Identifer):
	FBIDIO_IN1_16 = pIE('FBIDIO_IN1_16', lib.FBIDIO_IN1_16)
	FBIDIO_IN17_32 = pIE('FBIDIO_IN17_32', lib.FBIDIO_IN17_32)
	FBIDIO_IN33_48 = pIE('FBIDIO_IN33_48', lib.FBIDIO_IN33_48)
	FBIDIO_IN49_64 = pIE('FBIDIO_IN49_64', lib.FBIDIO_IN49_64)
	pass

# 7: DioInputDword
# ------------------
class InputDwordMode(pyinterface.Identifer):
	FBIDIO_IN1_32 = pIE('FBIDIO_IN1_32', lib.FBIDIO_IN1_32)
	FBIDIO_IN32_64 = pIE('FBIDIO_IN32_64', lib.FBIDIO_IN32_64)
	pass

# 8: DioOutputByte
# ------------------
class OutputByteMode(pyinterface.Identifer):
	FBIDIO_OUT1_8 = pIE('FBIDIO_OUT1_8', lib.FBIDIO_OUT1_8)
	FBIDIO_OUT9_16 = pIE('FBIDIO_OUT9_16', lib.FBIDIO_OUT9_16)
	FBIDIO_OUT17_24 = pIE('FBIDIO_OUT17_24', lib.FBIDIO_OUT17_24)
	FBIDIO_OUT25_32 = pIE('FBIDIO_OUT25_32', lib.FBIDIO_OUT25_32)
	FBIDIO_OUT33_40 = pIE('FBIDIO_OUT33_40', lib.FBIDIO_OUT33_40)
	FBIDIO_OUT41_48 = pIE('FBIDIO_OUT41_48', lib.FBIDIO_OUT41_48)
	FBIDIO_OUT49_56 = pIE('FBIDIO_OUT49_56', lib.FBIDIO_OUT49_56)
	FBIDIO_OUT57_64 = pIE('FBIDIO_OUT57_64', lib.FBIDIO_OUT57_64)
	pass

# 9: DioOutputWord
# ------------------
class OutputWordMode(pyinterface.Identifer):
	FBIDIO_OUT1_16 = pIE('FBIDIO_OUT1_16', lib.FBIDIO_OUT1_16)
	FBIDIO_OUT17_32 = pIE('FBIDIO_OUT17_32', lib.FBIDIO_OUT17_32)
	FBIDIO_OUT33_48 = pIE('FBIDIO_OUT33_48', lib.FBIDIO_OUT33_48)
	FBIDIO_OUT49_64 = pIE('FBIDIO_OUT49_64', lib.FBIDIO_OUT49_64)
	pass

# 10: DioOutputDword
# ------------------
class OutputDwordMode(pyinterface.Identifer):
	FBIDIO_OUT1_32 = pIE('FBIDIO_OUT1_32', lib.FBIDIO_OUT1_32)
	FBIDIO_OUT33_64 = pIE('FBIDIO_OUT33_64', lib.FBIDIO_OUT33_64)
	pass

# 11: DioSetLatchStatus
# ------------------
class LatchStatus(pyinterface.Identifer):
	size = 8
	bits = [pyinterface.BitIdentiferElement(i) for i in range(size)]
	del(i)
	bits[0].set_params('PORT0', 'ENABLED', 'DISABLED')
	bits[1].set_params('PORT1', 'ENABLED', 'DISABLED')
	bits[2].set_params('PORT2', 'ENABLED', 'DISABLED')
	bits[3].set_params('PORT3', 'ENABLED', 'DISABLED')
	bits[4].set_params('PORT4', 'ENABLED', 'DISABLED')
	bits[5].set_params('PORT5', 'ENABLED', 'DISABLED')
	bits[6].set_params('PORT6', 'ENABLED', 'DISABLED')
	bits[7].set_params('PORT7', 'ENABLED', 'DISABLED')
	pass

# 13: DioGetAckStatus
# ------------------
class AckStatus(pyinterface.Identifer):
	size = 8
	bits = [pyinterface.BitIdentiferElement(i) for i in range(size)]
	del(i)
	bits[0].set_params('IR.IN2', 'HIGH', 'LOW')
	bits[5].set_params('STB2', 'HIGH', 'LOW')
	bits[6].set_params('ACKR2', 'HIGH', 'LOW')
	bits[7].set_params('ACK2', 'HIGH', 'LOW')
	pass

# 14: DioSetAckPulseCommand
# ------------------
class AckPulseCommand(pyinterface.Identifer):
	size = 8
	bits = [pyinterface.BitIdentiferElement(i) for i in range(size)]
	del(i)
	bits[3].set_params('P010', 'HIGH', 'DISABLED')
	bits[4].set_params('P011', 'LOW', 'DISABLESD')
	bits[5].set_params('P012', 'LOW_PULSE', 'DISABLED')
	bits[6].set_params('ACK10', 'HIGH', 'DISABLED')
	bits[7].set_params('ACK11', 'LOW', 'DISABLED')
	pass

# 15: DioGetStbStatus
# ------------------
class StbStatus(pyinterface.Identifer):
	size = 8
	bits = [pyinterface.BitIdentiferElement(i) for i in range(size)]
	del(i)
	bits[0].set_params('IR.IN1', 'HIGH', 'LOW')
	bits[4].set_params('LF', 'LATCH_ON', 'LATCH_OFF')
	bits[5].set_params('ACK1', 'HIGH', 'LOW')
	bits[6].set_params('STBR1', 'HIGH', 'LOW')
	bits[7].set_params('STB1', 'HIGH', 'LOW')
	pass

# 16: DioSetStbPulseCommand
# ------------------
class StbPulseStatus(pyinterface.Identifer):
	size = 8
	bits = [pyinterface.BitIdentiferElement(i) for i in range(size)]
	del(i)
	bits[3].set_params('P020', 'HIGH', 'DISABLED')
	bits[4].set_params('P021', 'LOW', 'DISABLED')
	bits[5].set_params('P022', 'LOW_PULSE', 'DISABLED')
	bits[6].set_params('STB20', 'HIGH', 'DISABLED')
	bits[7].set_params('STB21', 'LOW', 'DISABLED')
	pass


# 18: DioSetIrqMask
# ------------------
class IrqMask(pyinterface.Identifer):
	size = 8
	bits = [pyinterface.BitIdentiferElement(i) for i in range(size)]
	del(i)
	bits[0].set_params('SIG1', 'UNMASK', 'MASK')
	bits[1].set_params('SIG2', 'UNMASK', 'MASK')
	bits[2].set_params('SIG3', 'UNMASK', 'MASK')
	bits[3].set_params('SIG4', 'UNMASK', 'MASK')
	bits[4].set_params('SIGT', 'RSTIN_INTERRUPT', 'NONE')
	bits[5].set_params('SIGR', 'TIMER_INTERRUPT', 'NONE')
	pass

# 20: DioSetIrqConfig
# ------------------
class IrqConfig(pyinterface.Identifer):
	size = 8
	bits = [pyinterface.BitIdentiferElement(i) for i in range(size)]
	del(i)
	bits[0].set_params('SIG1', 'STB1', 'IN1')
	bits[1].set_params('SIG2', 'IR.IN1', 'IN2')
	bits[2].set_params('SIG3', 'ACK2', 'IN3')
	bits[3].set_params('SIG4', 'IR.IN2', 'IN4')
	bits[4].set_params('EDS1', 'HIGH', 'LOW')
	bits[5].set_params('EDS2', 'HIGH', 'LOW')
	bits[6].set_params('EDS3', 'HIGH', 'LOW')
	bits[7].set_params('EDS4', 'HIGH', 'LOW')
	pass

# 25: DioGetDeviceConfig
# ------------------
class DeviceConfig(pyinterface.Identifer):
	size = 32
	bits = [pyinterface.BitIdentiferElement(i) for i in range(size)]
	del(i)
	bits[0].set_params('IN1-8', 'ENABLED', 'DISABLED')
	bits[1].set_params('IN9-16', 'ENABLED', 'DISABLED')
	bits[2].set_params('IN17-24', 'ENABLED', 'DISABLED')
	bits[3].set_params('IN25-32', 'ENABLED', 'DISABLED')
	bits[4].set_params('IN33-40', 'ENABLED', 'DISABLED')
	bits[5].set_params('IN41-48', 'ENABLED', 'DISABLED')
	bits[6].set_params('IN49-56', 'ENABLED', 'DISABLED')
	bits[7].set_params('IN57-64', 'ENABLED', 'DISABLED')
	bits[8].set_params('OUT1-8', 'ENABLED', 'DISABLED')
	bits[9].set_params('OUT9-16', 'ENABLED', 'DISABLED')
	bits[10].set_params('OUT17-24', 'ENABLED', 'DISABLED')
	bits[11].set_params('OUT25-32', 'ENABLED', 'DISABLED')
	bits[12].set_params('OUT33-40', 'ENABLED', 'DISABLED')
	bits[13].set_params('OUT41-48', 'ENABLED', 'DISABLED')
	bits[14].set_params('OUT49-56', 'ENABLED', 'DISABLED')
	bits[15].set_params('OUT57-64', 'ENABLED', 'DISABLED')
	bits[16].set_params('STB1,ACK1', 'ENABLED', 'DISABLED')
	bits[17].set_params('STB2,ACK2', 'ENABLED', 'DISABLED')
	bits[18].set_params('IR.IN1', 'ENABLED', 'DISABLED')
	bits[19].set_params('IR.IN2', 'ENABLED', 'DISABLED')
	bits[20].set_params('PULSE.OUT1', 'ENABLED', 'DISABLED')
	bits[21].set_params('PULSE.OUT2', 'ENABLED', 'DISABLED')
	bits[22].set_params('DI1', 'ENABLED', 'DISABLED')
	bits[23].set_params('DI1-4', 'ENABLED', 'DISABLED')
	bits[24].set_params('DI5-8', 'ENABLED', 'DISABLED')
	bits[25].set_params('DO1', 'ENABLED', 'DISABLED')
	bits[26].set_params('DO1-4', 'ENABLED', 'DISABLED')
	bits[27].set_params('DO5-8', 'ENABLED', 'DISABLED')
	bits[28].set_params('PWR.IN1', 'ENABLED', 'DISABLED')
	bits[29].set_params('PWR.IN2', 'ENABLED', 'DISABLED')
	bits[30].set_params('INTER_TIMER', 'ENABLED', 'DISABLED')
	pass

# 26: DioGetDeviceConfigEx
# ------------------
class DeviceConfigEx(pyinterface.Identifer):
	size = 32
	bits = [pyinterface.BitIdentiferElement(i) for i in range(size)]
	del(i)
	bits[0].set_params('IN1-8_EDGE', 'ENABLED', 'DISABLED')
	bits[1].set_params('IN9-16_EDGE', 'ENABLED', 'DISABLED')
	bits[2].set_params('IN17-24_EDGE', 'ENABLED', 'DISABLED')
	bits[3].set_params('IN25-32_EDGE', 'ENABLED', 'DISABLED')
	bits[4].set_params('IN33-40_EDGE', 'ENABLED', 'DISABLED')
	bits[5].set_params('IN41-48_EDGE', 'ENABLED', 'DISABLED')
	bits[6].set_params('IN49-56_EDGE', 'ENABLED', 'DISABLED')
	bits[7].set_params('IN57-64_EDGE', 'ENABLED', 'DISABLED')
	bits[24].set_params('DGFILTER', 'ENABLED', 'DISABLED')
	bits[25].set_params('RSTIN_MASK', 'ENABLED', 'DISABLED')
	bits[26].set_params('DGFILTER', 'ENABLED', 'DISABLED')
	pass

# 28: DioSetTimerConfig  ???????????????????????????????????????????????????????
# ------------------
class TimerConfig(pyinterface.Identifer):
	size = 8
	bits = [pyinterface.BitIdentiferElement(i) for i in range(size)]
	del(i)
	bits[0].set_params('CYCLE', '', '')
	bits[1].set_params('CYCLE', '', '')
	bits[2].set_params('CYCLE', '', '')
	bits[3].set_params('CYCLE', '', '')
	bits[4].set_params('BASE_CYCLE', '', '')
	bits[5].set_params('BASE_CYCLE', '', '')
	bits[6].set_params('BASE_CYCLE', '', '')
	pass

# 30: DioGetTimerCount   ????????????????????????????
# ------------------
class TimerCount(pyinterface.Identifer):
	size = 8
	bits = [pyinterface.BitIdentiferElement(i) for i in range(size)]
	del(i)
	bits[0].set_params('CYCLE', '', '')
	bits[1].set_params('CYCLE', '', '')
	bits[2].set_params('CYCLE', '', '')
	bits[3].set_params('CYCLE', '', '')
	pass

# 31: DioEintSetIrqMask
# ------------------
class EintIrqMask(pyinterface.Identifer):
	size = 32
	bits = [pyinterface.BitIdentiferElement(i) for i in range(size)]
	del(i)
	bits[0].set_params('IR1', 'UNMASK', 'MASK')
	bits[1].set_params('IR2', 'UNMASK', 'MASK')
	bits[2].set_params('IR3', 'UNMASK', 'MASK')
	bits[3].set_params('IR4', 'UNMASK', 'MASK')
	bits[4].set_params('IR5', 'UNMASK', 'MASK')
	bits[5].set_params('IR6', 'UNMASK', 'MASK')
	bits[6].set_params('IR7', 'UNMASK', 'MASK')
	bits[7].set_params('IR8', 'UNMASK', 'MASK')
	bits[8].set_params('IR9', 'UNMASK', 'MASK')
	bits[9].set_params('IR10', 'UNMASK', 'MASK')
	bits[10].set_params('IR11', 'UNMASK', 'MASK')
	bits[11].set_params('IR12', 'UNMASK', 'MASK')
	bits[12].set_params('IR13', 'UNMASK', 'MASK')
	bits[13].set_params('IR14', 'UNMASK', 'MASK')
	bits[14].set_params('IR15', 'UNMASK', 'MASK')
	bits[15].set_params('IR16', 'UNMASK', 'MASK')
	bits[16].set_params('IR17', 'UNMASK', 'MASK')
	bits[17].set_params('IR18', 'UNMASK', 'MASK')
	bits[18].set_params('IR19', 'UNMASK', 'MASK')
	bits[19].set_params('IR20', 'UNMASK', 'MASK')
	bits[20].set_params('IR21', 'UNMASK', 'MASK')
	bits[21].set_params('IR22', 'UNMASK', 'MASK')
	bits[22].set_params('IR23', 'UNMASK', 'MASK')
	bits[23].set_params('IR24', 'UNMASK', 'MASK')
	bits[24].set_params('IR25', 'UNMASK', 'MASK')
	bits[25].set_params('IR26', 'UNMASK', 'MASK')
	bits[26].set_params('IR27', 'UNMASK', 'MASK')
	bits[27].set_params('IR28', 'UNMASK', 'MASK')
	bits[28].set_params('IR29', 'UNMASK', 'MASK')
	bits[29].set_params('IR30', 'UNMASK', 'MASK')
	bits[30].set_params('IR31', 'UNMASK', 'MASK')
	bits[31].set_params('IR32', 'UNMASK', 'MASK')
	pass

# 33: DioEintSetEdgeConfig
# ------------------
class EintEdgeConfig(pyinterface.Identifer):
	size = 32
	bits = [pyinterface.BitIdentiferElement(i) for i in range(size)]
	del(i)
	bits[0].set_params('IR1', 'ENABLED', 'UNABLED')
	bits[1].set_params('IR2', 'ENABLED', 'UNABLED')
	bits[2].set_params('IR3', 'ENABLED', 'UNABLED')
	bits[3].set_params('IR4', 'ENABLED', 'UNABLED')
	bits[4].set_params('IR5', 'ENABLED', 'UNABLED')
	bits[5].set_params('IR6', 'ENABLED', 'UNABLED')
	bits[6].set_params('IR7', 'ENABLED', 'UNABLED')
	bits[7].set_params('IR8', 'ENABLED', 'UNABLED')
	bits[8].set_params('IR9', 'ENABLED', 'UNABLED')
	bits[9].set_params('IR10', 'ENABLED', 'UNABLED')
	bits[10].set_params('IR11', 'ENABLED', 'UNABLED')
	bits[11].set_params('IR12', 'ENABLED', 'UNABLED')
	bits[12].set_params('IR13', 'ENABLED', 'UNABLED')
	bits[13].set_params('IR14', 'ENABLED', 'UNABLED')
	bits[14].set_params('IR15', 'ENABLED', 'UNABLED')
	bits[15].set_params('IR16', 'ENABLED', 'UNABLED')
	bits[16].set_params('IR17', 'ENABLED', 'UNABLED')
	bits[17].set_params('IR18', 'ENABLED', 'UNABLED')
	bits[18].set_params('IR19', 'ENABLED', 'UNABLED')
	bits[19].set_params('IR20', 'ENABLED', 'UNABLED')
	bits[20].set_params('IR21', 'ENABLED', 'UNABLED')
	bits[21].set_params('IR22', 'ENABLED', 'UNABLED')
	bits[22].set_params('IR23', 'ENABLED', 'UNABLED')
	bits[23].set_params('IR24', 'ENABLED', 'UNABLED')
	bits[24].set_params('IR25', 'ENABLED', 'UNABLED')
	bits[25].set_params('IR26', 'ENABLED', 'UNABLED')
	bits[26].set_params('IR27', 'ENABLED', 'UNABLED')
	bits[27].set_params('IR28', 'ENABLED', 'UNABLED')
	bits[28].set_params('IR29', 'ENABLED', 'UNABLED')
	bits[29].set_params('IR30', 'ENABLED', 'UNABLED')
	bits[30].set_params('IR31', 'ENABLED', 'UNABLED')
	bits[31].set_params('IR32', 'ENABLED', 'UNABLED')
	pass

# 35: DioEintSetIrqMaskEx
# ------------------
class IrqMaskEx(pyinterface.Identifer):            ????????????????????????
	size = 32
	bits = [pyinterface.BitIdentiferElement(i) for i in range(size)]
	del(i)
	bits[0].set_params('IR1', 'UNMASK', 'MASK')
	bits[1].set_params('IR2', 'UNMASK', 'MASK')
	bits[2].set_params('IR3', 'UNMASK', 'MASK')
	bits[3].set_params('IR4', 'UNMASK', 'MASK')
	bits[4].set_params('IR5', 'UNMASK', 'MASK')
	bits[5].set_params('IR6', 'UNMASK', 'MASK')
	bits[6].set_params('IR7', 'UNMASK', 'MASK')
	bits[7].set_params('IR8', 'UNMASK', 'MASK')
	bits[8].set_params('IR9', 'UNMASK', 'MASK')
	bits[9].set_params('IR10', 'UNMASK', 'MASK')
	bits[10].set_params('IR11', 'UNMASK', 'MASK')
	bits[11].set_params('IR12', 'UNMASK', 'MASK')
	bits[12].set_params('IR13', 'UNMASK', 'MASK')
	bits[13].set_params('IR14', 'UNMASK', 'MASK')
	bits[14].set_params('IR15', 'UNMASK', 'MASK')
	bits[15].set_params('IR16', 'UNMASK', 'MASK')
	bits[16].set_params('IR17', 'UNMASK', 'MASK')
	bits[17].set_params('IR18', 'UNMASK', 'MASK')
	bits[18].set_params('IR19', 'UNMASK', 'MASK')
	bits[19].set_params('IR20', 'UNMASK', 'MASK')
	bits[20].set_params('IR21', 'UNMASK', 'MASK')
	bits[21].set_params('IR22', 'UNMASK', 'MASK')
	bits[22].set_params('IR23', 'UNMASK', 'MASK')
	bits[23].set_params('IR24', 'UNMASK', 'MASK')
	bits[24].set_params('IR25', 'UNMASK', 'MASK')
	bits[25].set_params('IR26', 'UNMASK', 'MASK')
	bits[26].set_params('IR27', 'UNMASK', 'MASK')
	bits[27].set_params('IR28', 'UNMASK', 'MASK')
	bits[28].set_params('IR29', 'UNMASK', 'MASK')
	bits[29].set_params('IR30', 'UNMASK', 'MASK')
	bits[30].set_params('IR31', 'UNMASK', 'MASK')
	bits[31].set_params('IR32', 'UNMASK', 'MASK')
	pass

# 39: DioEintInputPoint   ???????????????????????
# ------------------
class IrqMaskEx(pyinterface.Identifer): 
	size = 32
	bits = [pyinterface.BitIdentiferElement(i) for i in range(size)]
	del(i)





# 43: DioEintSetFilterConfig
# ------------------
class EintFilterConfig(pyinterface.Identifer):
	FBIDIO_IRIN1_2_STB1 = pIE('FBIDIO_IRIN1_2_STB1', lib.FBIDIO_IRIN1_2_STB1)
	pass

class EintFilterConfig(pyinterface.Identifer): ???????????????????????????????????????????????
	size = 8
	bits = [pyinterface.BitIdentiferElement(i) for i in range(size)]
	del(i)
	bits[0].set_params('', '', '')
	bits[1].set_params('', '', '')
	bits[2].set_params('', '', '')
	bits[3].set_params('', '', '')
	bits[4].set_params('', '', '')
	bits[5].set_params('', '', '')
	bits[6].set_params('', '', '')
	bits[7].set_params('', '', '')

# 45: DioSetRstinMask
# ------------------
class RstinMask(pyinterface.Identifer):
	FBIDIO_RSTIN_MASK = pIE('FBIDIO_RSTIN_MASK', lib.FBIDIO_RSTIN_MASK)
	pass

# 51: DioOutputSync
# ------------------
class RstinMask(pyinterface.Identifer):
	FBIDIO_SYNC1 = pIE('FBIDIO_SYNC1', lib.FBIDIO_SYNC1)
	FBIDIO_SYNC2 = pIE('FBIDIO_SYNC2', lib.FBIDIO_SYNC2)
	pass


# Error Wrapper
#===================
class ErrorGPG2000(pyinterface.ErrorCode):
	FBIDIO_ERROR_SUCCESS = pIE('FBIDIO_ERROR_SUCCESS', lib.FBIDIO_ERROR_SUCCESS)
	FBIDIO_ERROR_NOT_DEVICE = pIE('FBIDIO_ERROR_NOT_DEVICE', lib.FBIDIO_ERROR_NOT_DEVICE)
	FBIDIO_ERROR_NOT_OPEN = pIE('FBIDIO_ERROR_NOT_OPEN', lib.FBIDIO_ERROR_NOT_OPEN)
	FBIDIO_ERROR_INVALID_DEVICE_NUMBER = pIE('FBIDIO_ERROR_INVALID_DEVICE_NUMBER', lib.FBIDIO_ERROR_INVALID_DEVICE_NUMBER)
	FBIDIO_ERROR_ALREADY_OPEN = pIE('FBIDIO_ERROR_ALREADY_OPEN', lib.FBIDIO_ERROR_ALREADY_OPEN)
	FBIDIO_ERROR_NOT_SUPPORTED = pIE('FBIDIO_ERROR_NOT_SUPPORTED', lib.FBIDIO_ERROR_NOT_SUPPORTED)
	FBIDIO_ERROR_PARAMETER = pIE('FBIDIO_ERROR_PARAMETER', lib.FBIDIO_ERROR_PARAMETER)
	FBIDIO_ERROR_INVALID_CALL = pIE('FBIDIO_ERROR_INVALID_CALL', lib.FBIDIO_ERROR_INVALID_CALL)
	FBIDIO_ERROR_USBIO_FAILED = pIE('FBIDIO_ERROR_USBIO_FAILED', lib.FBIDIO_ERROR_USBIO_FAILED)
	FBIDIO_ERROR_USBIO_TIMEOUT = pIE('FBIDIO_ERROR_USBIO_TIMEOUT', lib.FBIDIO_ERROR_USBIO_TIMEOUT)
	FBIDIO_ERROR_USBLIB_LOAD_FAILED = pIE('FBIDIO_ERROR_USBLIB_LOAD_FAILED', lib.FBIDIO_ERROR_USBLIB_LOAD_FAILED)
	FBIDIO_ERROR_DEVICE_HANDLE = pIE('FBIDIO_ERROR_DEVICE_HANDLE', lib.FBIDIO_ERROR_DEVICE_HANDLE)
	
    _success = FBIDIO_ERROR_SUCCESS
    pass



# ==========================
# GPG-2000 Python
# ==========================
class gpg2000(object):









# ==========================
# GPG-2000 Python Controller
# ==========================
class gpg2000_controller(object):
	ndev = int()
	boardid = ''
	print_log = True

	def __init__(self, ndev=1, boardid=2000, initialize=True):
		"""
		boardid = 2000
		"""
		self.ndev = ndev
		self.boardid = BoardID.verify(boardid)
		if initialize: self.initialize()
		return

	def _log(self, msg):
		if self.print_log:
			print('Interface GPG2000(%d): %s'%(self.ndev, msg))
			pass
		return
        
	def _error_check(self, error_no):
		ErrorGPG2000.check(error_no)
		return

	def initialize(self):
		self.open()
		return




	def open(self):
		"""
		1. DioOpen
		"""
		self._log('open')
		ret = lib.DioOpen(self.ndev)
		self._error_check(ret)
		return

	def close(self):
		"""
		2. DioClose
		"""
		self._log('close')
		ret = lib.DioClose(self.ndev)
		self._error_check(ret)
		return

	def in_point(self, startnum, num):
		"""
		3. DioInputPoint
		"""
		self._log('in_point')
		buffer = ctypes.c_int(0)
		num = InputPoint(num)
		ret = lib.DioInputPoint(self.ndev, buffer, startnum, num)
		self._error_check(ret)
		return buffer

	def out_point(self, startnum, num):
		"""
		4. DioOutputPoint
		"""
		self._log('out_point')
		buffer = ctypes.c_int(0)
		num = InputPoint(num)
		ret = lib.DioOutputPoint(self.ndev, buffer, startnum, num)
		self._error_check(ret)
		return buffer

	def in_byte(self, no):
		"""
		5. DioInputByte
		"""
		self._log('in_byte')
		no = InputByteMode.verify(no)
		value = ctypes.c_char_p(0)
		ret = lib.DioInputByte(self.ndev, no, value)
		self._error_check(ret)
		return value

	def in_word(self, no):
		"""
		6. DioInputWord
		"""
		self._log('in_word')
		no = InputWordMode.verify(no)
		value = ctypes.c_ushort_p(0)
		ret = lib.DioInputWord(self.ndev, no, value)
		self._error_check(ret)
		return value

	def in_dword(self, no):
		"""
		7. DioInputDword
		"""
		self._log('in_dword')
		no = InputDwordMode.verify(no)
		value = ctypes.c_ulong_p(0)
		ret = lib.DioInputDword(self.ndev, no, value)
		self._error_check(ret)
		return value

	def out_byte(self, no):
		"""
		8. DioOutputByte
		"""
		self._log('out_byte')
		no = OutputByteMode.verify(no)
		value = ctypes.c_char_p(0)
		ret = lib.DioOutputByte(self.ndev, no, value)
		self._error_check(ret)
		return value

	def out_word(self, no):
		"""
		9. DioOutputWord
		"""
		self._log('out_word')
		no = OutputWordMode.verify(no)
		value = ctypes.c_ushort_p(0)
		ret = lib.DioOutputWord(self.ndev, no, value)
		self._error_check(ret)
		return value

	def out_dword(self, no):
		"""
		10. DioOutputDword
		"""
		self._log('out_dword')
		no = OutputDwordMode.verify(no)
		value = ctypes.c_ulong_p(0)
		ret = lib.DioOutputDword(self.ndev, no, value)
		self._error_check(ret)
		return value

	def set_latch(self, status):
		"""
		11. DioSetLatchStatus
		"""
		self._log('set_latch')
		status = LatchStatus(status)
		ret = lib.DioSetLatchStatus(self.ndev, status)
		self._error_check(ret)
		return

	def get_latch(self):
		"""
		12. DioGetLatchStatus
		"""
		self._log('set_latch')
		status = ctypes.c_char_p(0)
		status = LatchStatus(status.value)
		ret = lib.DioGetLatchStatus(self.ndev, status)
		self._error_check(ret)
		return status

	def get_ack(self):
		"""
		13. DioGetAckStatus
		"""
		self._log('get_ack')
		status = ctypes.c_uchar_p(0)
		status = AckStatus(status.value)
		ret = lib.DioGetAckStatus(self.ndev, status)
		self._error_check(ret)
		return status

	def set_ack(self, commamd):
		"""
		14. DioSetAckPulseCommand
		"""
		self._log('set_ack')
		command = AckPulseCommand(command)
		ret = lib.DioSetAckPulseCommand(self.ndev, status)
		self._error_check(ret)
		return

	def get_stb(self):
		"""
		15. DioGetStbStatus
		"""
		self._log('get_stb_status')
		status = ctypes.c_uchar_p(0)
		status = StbStatus(status.value)
		ret = lib.DioGetStbStatus(self.ndev, status)
		self._error_check(ret)
		return status

	def set_stb(self, command):
		"""
		16. DioSetStbPulseCommand
		"""
		self._log('set_stb')
		command = StbPulseStatus(command)
		ret = lib.DioSetStbPulseCommand(self.ndev, command)
		self._error_check(ret)
		return

	def get_reset(self):
		"""
		17. DioGetResetInStatus
		"""
		self._log('get_reset')
		status = ctypes.c_uchar_p(0)
		ret = lib.DioGetResetStatus(self.ndev, status)
		self._error_check(ret)
		return status.value

	def set_irq():
		"""
		18. DioSetIrqMask
		"""






	def ():
		"""
		19. DioGetIrqMask
		"""







	def ():
		"""
		20. DioSetIrqConfig
		"""







	def ():
		"""
		21. DioGetIrqConfig
		"""







	def ():
		"""
		22. DioRegistIsr
		"""







	def ():
		"""
		23. DioRegistIsrEx
		"""







	def ():
		"""
		24. DioEintRegistIsr
		"""








	def ():
		"""
		25. DioGetDeviceConfig
		"""








	def ():
		"""
		26. DioGetDeviceConfigEx
		"""








	def ():
		"""
		27. DioCommonGetPciDeviceInfo
		"""







	def ():
		"""
		28. DioSetTimerConfig
		"""









	def ():
		"""
		29. DioGetTimerConfig
		"""






