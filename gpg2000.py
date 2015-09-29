
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
    FBIDIO_IN33_64 = pIE('FBIDIO_IN32_64', lib.FBIDIO_IN33_64)
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

# 28: DioSetTimerConfig
# ------------------
class TimerConfig(pyinterface.Identifer):
    size = 8
    bits = [pyinterface.BitIdentiferElement(i) for i in range(size)]
    del(i)
    bits[0].set_params('BIT', 'ON', 'OFF')
    bits[1].set_params('BIT', 'ON', 'OFF')
    bits[2].set_params('BIT', 'ON', 'OFF')
    bits[3].set_params('BIT', 'ON', 'OFF')
    bits[4].set_params('BIT', 'ON', 'OFF')
    bits[5].set_params('BIT', 'ON', 'OFF')
    bits[6].set_params('BIT', 'ON', 'OFF')
    pass

# 30: DioGetTimerCount
# ------------------
class TimerCount(pyinterface.Identifer):
    size = 8
    bits = [pyinterface.BitIdentiferElement(i) for i in range(size)]
    del(i)
    bits[0].set_params('CTL1', 'ON', 'OFF')
    bits[1].set_params('CTL2', 'ON', 'OFF')
    bits[2].set_params('CTL3', 'ON', 'OFF')
    bits[3].set_params('CTL4', 'ON', 'OFF')
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
class IrqMaskEx(pyinterface.Identifer):
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

# 45: DioSetRstinMask
# ------------------
class RstinMask(pyinterface.Identifer):
    FBIDIO_RSTIN_MASK = pIE('FBIDIO_RSTIN_MASK', lib.FBIDIO_RSTIN_MASK)
    pass

# 47: CallBackProc
# ------------------
class CallBackProc(pyinterface.Identifer):
    size = 8
    bits = [pyinterface.BitIdentiferElement(i) for i in range(size)]
    del(i)
    bits[0].set_params('SIG1', 'CUTTING', 'NONE')
    bits[1].set_params('SIG2', 'CUTTING', 'NONE')
    bits[2].set_params('SIG3', 'CUTTING', 'NONE')
    bits[3].set_params('SIG4', 'CUTTING', 'NONE')
    bits[4].set_params('SIGT', 'CUTTING', 'NONE')
    bits[5].set_params('SIGR', 'CUTTING', 'NONE')
    pass

# 48: CallBackProcEx
# ------------------
class CallBackProcEx(pyinterface.Identifer):
    size = 32
    bits = [pyinterface.BitIdentiferElement(i) for i in range(size)]
    del(i)
    bits[0].set_params('IR1', 'EDGE_ON', 'EDGE_OFF')
    bits[1].set_params('IR2', 'EDGE_ON', 'EDGE_OFF')
    bits[2].set_params('IR3', 'EDGE_ON', 'EDGE_OFF')
    bits[3].set_params('IR4', 'EDGE_ON', 'EDGE_OFF')
    bits[4].set_params('IR5', 'EDGE_ON', 'EDGE_OFF')
    bits[5].set_params('IR6', 'EDGE_ON', 'EDGE_OFF')
    bits[6].set_params('IR7', 'EDGE_ON', 'EDGE_OFF')
    bits[7].set_params('IR8', 'EDGE_ON', 'EDGE_OFF')
    bits[8].set_params('IR9', 'EDGE_ON', 'EDGE_OFF')
    bits[9].set_params('IR10', 'EDGE_ON', 'EDGE_OFF')
    bits[10].set_params('IR11', 'EDGE_ON', 'EDGE_OFF')
    bits[11].set_params('IR12', 'EDGE_ON', 'EDGE_OFF')
    bits[12].set_params('IR13', 'EDGE_ON', 'EDGE_OFF')
    bits[13].set_params('IR14', 'EDGE_ON', 'EDGE_OFF')
    bits[14].set_params('IR15', 'EDGE_ON', 'EDGE_OFF')
    bits[15].set_params('IR16', 'EDGE_ON', 'EDGE_OFF')
    bits[16].set_params('IR17', 'EDGE_ON', 'EDGE_OFF')
    bits[17].set_params('IR18', 'EDGE_ON', 'EDGE_OFF')
    bits[18].set_params('IR19', 'EDGE_ON', 'EDGE_OFF')
    bits[19].set_params('IR20', 'EDGE_ON', 'EDGE_OFF')
    bits[20].set_params('IR21', 'EDGE_ON', 'EDGE_OFF')
    bits[21].set_params('IR22', 'EDGE_ON', 'EDGE_OFF')
    bits[22].set_params('IR23', 'EDGE_ON', 'EDGE_OFF')
    bits[23].set_params('IR24', 'EDGE_ON', 'EDGE_OFF')
    bits[24].set_params('IR25', 'EDGE_ON', 'EDGE_OFF')
    bits[25].set_params('IR26', 'EDGE_ON', 'EDGE_OFF')
    bits[26].set_params('IR27', 'EDGE_ON', 'EDGE_OFF')
    bits[27].set_params('IR28', 'EDGE_ON', 'EDGE_OFF')
    bits[28].set_params('IR29', 'EDGE_ON', 'EDGE_OFF')
    bits[29].set_params('IR30', 'EDGE_ON', 'EDGE_OFF')
    bits[30].set_params('IR31', 'EDGE_ON', 'EDGE_OFF')
    bits[31].set_params('IR32', 'EDGE_ON', 'EDGE_OFF')
    pass

# 51: DioOutputSync
# ------------------
class RstinMask(pyinterface.Identifer):
    FBIDIO_SYNC1 = pIE('FBIDIO_SYNC1', lib.FBIDIO_SYNC1)
    FBIDIO_SYNC2 = pIE('FBIDIO_SYNC2', lib.FBIDIO_SYNC2)
    pass

class OutputSync(pyinterface.Identifer):
    size = 8
    bits = [pyinterface.BitIdentiferElement(i) for i in range(size)]
    del(i)
    bits[0].set_params('DI1', 'ENABLE', 'DISABLE')
    bits[1].set_params('DI2', 'ENABLE', 'DISABLE')
    bits[2].set_params('DI3', 'ENABLE', 'DISABLE')
    bits[3].set_params('DI4', 'ENABLE', 'DISABLE')
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
    def __init__(self, ndev=1, remote=False):
        initialize = not remote
        self.ctrl = gpg2000_controller(ndev, initialize=initialize)
        pass

    def di_check(self, start_num, num):
        ret = self.ctrl.in_point(start_num, num)
        return ret

    def do_output(self, buffer, startnum, num):
        self.ctrl.out_point(buffer, startnum, num)
        return



# ==========================
# GPG-2000 Python Controller
# ==========================
class gpg2000_controller(object):
    ndev = int()
    boardid = ''
    print_log = True

    def __init__(self, ndev=1, boardid=2724, initialize=True):
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
        ret = lib.DioOpen(self.ndev, 0)
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
        buffer = ctypes.c_int*64
        buffer = buffer(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                        0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)
        ret = lib.DioInputPoint(self.ndev, buffer, startnum, num)
        self._error_check(ret)
        return buffer

    def out_point(self, buffer, startnum, num):
        """
        4. DioOutputPoint
        """
        self._log('out_point')
        c_buff = ctypes.c_int*64
        c_buff = c_buff(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                        0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)
        c_buff[0:num-1] = buffer[0:num-1]
        ret = lib.DioOutputPoint(self.ndev, c_buff, startnum, num)
        self._error_check(ret)
        return

    def in_byte(self, no):
        """
        5. DioInputByte
        """
        self._log('in_byte')
        no = InputByteMode.verify(no)
        value = ctypes.c_ubyte(0)
        ret = lib.DioInputByte(self.ndev, no, value)
        self._error_check(ret)
        value = int(value.value)
        return value

    def in_word(self, no):
        """
        6. DioInputWord
        """
        self._log('in_word')
        no = InputWordMode.verify(no)
        value = ctypes.c_ushort(0)
        ret = lib.DioInputWord(self.ndev, no, value)
        self._error_check(ret)
        value = int(value.value)
        return value

    def in_dword(self, no):
        """
        7. DioInputDword
        """
        self._log('in_dword')
        no = InputDwordMode.verify(no)
        value = ctypes.c_ulong(0)
        ret = lib.DioInputDword(self.ndev, no, value)
        self._error_check(ret)
        value = int(value.value)
        return value

    def out_byte(self, no, value):
        """
        8. DioOutputByte
        """
        self._log('out_byte')
        no = OutputByteMode.verify(no)
        value = ctypes.c_ubyte(value)
        ret = lib.DioOutputByte(self.ndev, no, value)
        self._error_check(ret)
        return

    def out_word(self, no, value):
        """
        9. DioOutputWord
        """
        self._log('out_word')
        no = OutputWordMode.verify(no)
        value = ctypes.c_ushort(value)
        ret = lib.DioOutputWord(self.ndev, no, value)
        self._error_check(ret)
        return

    def out_dword(self, no, value):
        """
        10. DioOutputDword
        """
        self._log('out_dword')
        no = OutputDwordMode.verify(no)
        value = ctypes.c_ulong(value)
        ret = lib.DioOutputDword(self.ndev, no, value)
        self._error_check(ret)
        return

    def set_latch(self, status):
        """
        11. DioSetLatchStatus
        """
        self._log('set_latch')
        ret = lib.DioSetLatchStatus(self.ndev, status)
        self._error_check(ret)
        return

    def get_latch(self):
        """
        12. DioGetLatchStatus
        """
        self._log('set_latch')
        status = ctypes.c_ubyte(0)
        ret = lib.DioGetLatchStatus(self.ndev, status)
        status = LatchStatus(status.value)
        self._error_check(ret)
        return status

    def get_ack(self):
        """
        13. DioGetAckStatus
        """
        self._log('get_ack')
        status = ctypes.c_ubyte(0)
        ret = lib.DioGetAckStatus(self.ndev, status)
        status = AckStatus(status.value)
        self._error_check(ret)
        return status

    def set_ack(self, commamd):
        """
        14. DioSetAckPulseCommand
        """
        self._log('set_ack')
        ret = lib.DioSetAckPulseCommand(self.ndev, status)
        self._error_check(ret)
        return

    def get_stb(self):
        """
        15. DioGetStbStatus
        """
        self._log('get_stb_status')
        status = ctypes.c_ubyte(0)
        ret = lib.DioGetStbStatus(self.ndev, status)
        status = StbStatus(status.value)
        self._error_check(ret)
        return status

    def set_stb(self, command):
        """
        16. DioSetStbPulseCommand
        """
        self._log('set_stb')
        ret = lib.DioSetStbPulseCommand(self.ndev, command)
        self._error_check(ret)
        return

    def get_reset(self):
        """
        17. DioGetResetInStatus
        """
        self._log('get_reset')
        status = ctypes.c_ubyte(0)
        ret = lib.DioGetResetStatus(self.ndev, status)
        self._error_check(ret)
        status = int(status.value)
        return status

    def set_irq_mask(self, mask):
        """
        18. DioSetIrqMask
        """
        self._log('set_irq_mask')
        ret = lib.DioSetIrqMask(self.ndev, mask)
        self._error_check(ret)
        return

    def get_irq_mask(self):
        """
        19. DioGetIrqMask
        """
        self._log('get_irq_mask')
        mask = ctypes.c_ubyte(0)
        ret = lib.DioGetIrqMask(self.ndev, mask)
        mask = IrqMask(mask.value)
        self._error_check(ret)
        return mask

    def set_irq_config(self, cofig):
        """
        20. DioSetIrqConfig
        """
        self._log('set_irq_config')
        ret = lib.DioSetIrqConfig(self.ndev, config)
        self._error_check(ret)
        return

    def get_irq_config(self):
        """
        21. DioGetIrqConfig
        """
        self._log('get_irq_config')
        config = ctypes.c_ubyte(0)
        ret = lib.DioGetIrqConfig(self.ndev, config)
        config = IrqConfig(config.value)
        self._error_check(ret)
        return config

    def regist_isr(self, callbackproc, userdata=None):
        """
        22. DioRegistIsr
        """
        self._log('regist_isr')
        ret = lib.DioRegistIsr(self.ndev, userdata, callbackproc)
        return

    def regist_isr_ex(self, userdata, callbackprocex):
        """
        23. DioRegistIsrEx
        """
        self._log('regist_isr_ex')
        ret = lib.DioRegistIsrEx(self.ndev, userdata, callbackprocex)
        return

    def eint_regist_isr(self, userdata, eintcallbackproc):
        """
        24. DioEintRegistIsr
        """
        self._log('eint_regist_isr')
        ret = lib.DioEintRegistIsr(self.ndev, userdata, eintcallbackproc)
        return

    def get_device_config(self):
        """
        25. DioGetDeviceConfig
        """
        self._log('get_device_config')
        device_config = ctypes.c_ulong(0)
        ret = lib.DioGetDeviceConfig(self.ndev, device_config)
        device_config = DeviceConfig(device_config.value)
        return device_config

    def get_device_config_ex(self):
        """
        26. DioGetDeviceConfigEx
        """
        self._log('get_device_config_ex')
        device_config = ctypes.c_ulong(0)
        device_config_ex = ctypes.c_ulong(0)
        ret = lib.DioGetDeviceConfigEx(self.ndev, device_config, device_config_ex)
        device_config = DeviceConfig(device_config.value)
        device_config_ex = DeviceConfigEx(device_config_ex.value)
        return [device_config, device_config_ex]

    def get_device_info(self):
        """
        27. DioCommonGetPciDeviceInfo
        """
        self._log('get_device_info')
        device_id = ctypes.c_ushort(0)
        vendor_id = ctypes.c_ushort(0)
        class_code = ctypes.c_ulong(0)
        revision_id = ctypes.c_ubyte(0)
        base_iddress0 = ctypes.c_ulong(0)
        base_iddress1 = ctypes.c_ulong(0)
        base_iddress2 = ctypes.c_ulong(0)
        base_iddress3 = ctypes.c_ulong(0)
        base_iddress4 = ctypes.c_ulong(0)
        base_iddress5 = ctypes.c_ulong(0)
        system_id = ctypes.c_ushort(0)
        system_vendor_id = ctypes.c_ushort(0)
        interrput_line = ctypes.c_ubyte(0)
        board_id = ctypes.c_ulong(0)
        ret = lib.DioCommonGetPciDeviceInfo(self.ndev, device_id, vendor_id, class_code, revision_id, base_iddress0, base_iddress1, base_iddress2, base_iddress3, base_iddress4, base_iddres5, system_id, system_vendor_id, interrput_id, board_id)
        return [device_id, vendor_id, class_code, revision_id, base_iddress0, base_iddress1, base_iddress2, base_iddress3, base_iddress4, base_iddres5, system_id, system_vendor_id, interrput_id, board_id]

    def set_timer_config(self, timer_config):
        """
        28. DioSetTimerConfig
        """
        self._log('set_timer_config')
        ret = lib.DioSetTimerConfig(self.ndev, timer_config)
        return

    def get_timer_config(self):
        """
        29. DioGetTimerConfig
        """
        self._log('get_timer_config')
        timer_config = ctypes.c_ubyte(0)
        ret = lib.DioGetTimerConfig(self.ndev, timer_config)
        timer_config = TimerConfig(timer_config.value)
        return timer_config

    def get_timer_count(self):
        """
        30. DioGetTimerCount
        """
        self._log('get_timer_count')
        timer_count = ctypes.c_ubyte(0)
        ret = lib.DioGetTimerCount(self.ndev, timer_count)
        timer_count = TimerCount(timer_count.value)
        return timer_count

    def eint_set_irq_mask(self, irqmask):
        """
        31. DioEintSetIrqMask
        """
        self._log('eint_set_irq_mask')
        ret = lib.DioEintSetIrqMask(self.ndev, irqmask)
        return

    def eint_get_irq_mask(self):
        """
        32. DioEintGetIrqMask
        """
        self._log('eint_get_irq_mask')
        irqmask = ctypes.c_ulong(0)
        ret = lib.DioEintGetIrqMadk(self.ndev, irqmask)
        irqmask = EintIrqMask(irqmask.value)
        return irqmask

    def set_edge_config(self, fall_config, rise_config):
        """
        33. DioEintSetEdgeConfig
        """
        self._log('set_edge_config')
        ret = lib.DioEintSetEdgeConfig(self.ndev, fall_config, rise_config)
        return

    def get_edge_config(self):
        """
        34. DioEintGetEdgeConfig
        """
        self._log('get_edge_config')
        fall_config = ctypes.c_ulong(0)
        rise_config = ctypes.c_ulong(0)
        ret = lib.DioEintGetEdgeConfig(self.ndev, fall_config, rise_config)
        fall_config = EintEdgeConfig(fall_config.value)
        rise_config = EintEdgeConfig(rise_config.value)
        return [fall_config, rise_config]

    def set_irq_mask_ex(self, no, irqmask):
        """
        35. DioEintSetIrqMaskEx
        """
        self._log('set_irq_mask_ex')
        no = InputDwordMode(no)
        irqmask = IrqMaskEx(irqmask)
        ret = lib.DioEintSetIrqMask(self.ndev, no, irqmask)
        return

    def get_irq_mask_ex(self, no):
        """
        36. DioEintGetIrqMaskEx
        """
        self._log('get_irq_mask_ex')
        no = InputDwordMode(no)
        irqmask = ctypes.c_ulong(0)
        ret = lib.DioEintGetIrqMaskEx(self.ndev, no, irqmask)
        irqmask = IrqMaskEx(irqmask.value)
        return irqmask

    def set_edge_config_ex(self, no, fall_config, rise_config):
        """
        37. DioEintSetEdgeConfigEx
        """
        self._log('set_edge_config_ex')
        no = InputDwordMode(no)
        fall_config = EintEdgeConfig(fall_config)
        rise_config = EintEdgeConfig(rise_config)
        ret = lib.DioEintSetEdgeConfigEx(self.ndev, no, fall_config, rise_config)
        return

    def get_edge_config_ex(self, no):
        """
        38. DioEintGetEdgeConfigEx
        """
        self._log('get_edge_config_ex')
        no = InputDwordMode(no)
        fall_config = ctypes.c_ulong(0)
        rise_config = ctypes.c_ulong(0)
        ret = lib.DioEintSetEdgeConfigEx(self.ndev, no, fall_config, rise_config)
        fall_config = EintEdgeConfig(fall_config.value)
        rise_config = EintEdgeConfig(rise_config.value)
        return [fall_config, rise_config]

    def eint_in_point(self, startnum, num):
        """
        39. DioEintInputPoint
        """
        self._log('eint_in_point')
        buffer = ctypes.c_int(0)
        ret = lib.DioEintInputPoint(self.ndev, buffer, startnum, num)
        return buffer

    def eint_in_byte(self, no):
        """
        40. DioEintInputByte
        """
        self._log('eint_in_byte')
        no = InputByteMode(no)
        fall_value = ctypes.c_ubyte(0)
        rise_value = ctypes.c_ubyte(0)
        ret = lib.DioEintInputByte(self.ndev, no, fall_value, rise_value)
        return [fall_value, rise_value]

    def eint_in_word(self, no):
        """
        41. DioEintInputWord
        """
        self._log('eint_in_word')
        no = InputWordMode(no)
        fall_value = ctypes.c_ushort(0)
        rise_value = ctypes.c_ushort(0)
        ret = lib.DioEintInputWord(self.ndev, no, fall_value, rise_value)
        return [fall_value, rise_value]

    def eint_in_dword(self, no):
        """
        42. DioEintInputDword
        """
        self._log('eint_in_dword')
        no = InputDwordMode(no)
        fall_value = ctypes.c_ulong(0)
        rise_value = ctypes.c_ulong(0)
        ret = lib.DioEintInputDword(self.ndev, no, fall_value, rise_value)
        return [fall_value, rise_value]

    def get_filter(self, no):
        """
        44. DioEintGetFilterConfig
        """
        self._log('get_filter')
        no = EintFilterNo(no)
        config = ctypes.c_int(0)
        ret = lib.DioEintGetFilterConfig(self.ndev, no, config)
        config = EintFilterConfig(config.value)
        return config

    def set_rstin_mask(self, mask):
        """
        45. DioSetRstinMask
        """
        self._log('set_rstin_mask')
        mask = RstinMask(mask)
        ret = lib.DioSetRstinMask(self.ndev, mask)
        return

    def get_rstin_mask(self):
        """
        46. DioGetRstinMask
        """
        self._log('get_rstin')
        mask = ctypes.c_ulong(0)
        ret = lib.DioGetRstinMask(self.ndev, mask)
        mask = RstinMask(mask.value)
        return mask

    def out_put_sync(self, line, up_edge, down_edge):
        """
        51. DioOutputSync
        """
        self._log('out_put_sync')
        line = RstinMask(line)
        up_edge = OutputSync(up_edge)
        down_edge = OutputSync(down_edge)
        ret = lib.DioOutputSync(self.ndev, line, up_edge, down_edge)
        return
