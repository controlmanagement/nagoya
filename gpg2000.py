
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














# Error Wrapper
#===================









# ==========================
# GPG-2000 Python
# ==========================










# ==========================
# GPG-2000 Python Controller
# ==========================



