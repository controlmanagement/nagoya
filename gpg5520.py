
import sys
import time
import ctypes
import numpy

import pyinterface
import libgpg5520 as lib
pIE = pyinterface.IdentiferElement


# Identifer Wrapper
# =================

class BoardID(pyinterface.Identifer):
    id5521 = pIE('id5521', 5521)
    id5522 = pIE('id5522', 5522)
    pass

# 5: ImgSetBuffer
# 26: ImgAllocateSDRAM
# 43: ImgSaveBitMapFile
# structure 10: IMGCLIPCONFIG
# ------------------
class ImgSetBuffer_BufferFormat(pyinterface.Identifer):
	IFIMG_COLOR_RGB32 = pIE('IFIMG_COLOR_RGB32', lib.IFIMG_COLOR_RGB32)
	IFIMG_COLOR_RGB24 = pIE('IFIMG_COLOR_RGB24', lib.IFIMG_COLOR_RGB24)
	IFIMG_COLOR_RGB15 = pIE('IFIMG_COLOR_RGB15', lib.IFIMG_COLOR_RGB15)
	IFIMG_COLOR_GRAY8 = pIE('IFIMG_COLOR_GRAY8', lib.IFIMG_COLOR_GRAY8)
	IFIMG_COLOR_RED8 = pIE('IFIMG_COLOR_RED8', lib.IFIMG_COLOR_RED8)
	IFIMG_COLOR_GREEN8 = pIE('IFIMG_COLOR_GREEN8', lib.IFIMG_COLOR_GREEN8)
	IFIMG_COLOR_BLUE8 = pIE('IFIMG_COLOR_BLUE8', lib.IFIMG_COLOR_BLUE8)
	IFIMG_COLOR_BIN8 = pIE('IFIMG_COLOR_BIN8', lib.IFIMG_COLOR_BIN8)
	IFIMG_COLOR_RGB16 = pIE('IFIMG_COLOR_RGB16', lib.IFIMG_COLOR_RGB16)
	IFIMG_COLOR_FIL8 = pIE('IFIMG_COLOR_FIL8', lib.IFIMG_COLOR_FIL8)
	IFIMG_COLOR_LABEL8 = pIE('IFIMG_COLOR_LABEL8', lib.IFIMG_COLOR_LABEL8)
	IFIMG_COLOR_CMP8 = pIE('IFIMG_COLOR_CMP8', lib.IFIMG_COLOR_CMP8)
	
	IFIMG_RESOLUTION_320_240 = pIE('IFIMG_RESOLUTION_320_240', lib.IFIMG_RESOLUTION_320_240)
	IFIMG_RESOLUTION_160_120 = pIE('IFIMG_RESOLUTION_160_120', lib.IFIMG_RESOLUTION_160_120)

	IFIMG_MEASUREMENT_HSIT = pIE('IFIMG_MEASUREMENT_HSIT', lib.IFIMG_MEASUREMENT_HSIT)
	IFIMG_MEASUREMENT_PRO = pIE('IFIMG_MEASUREMENT_PRO', lib.IFIMG_MEASUREMENT_PRO)
	IFIMG_MEASUREMENT_LBLCNT = pIE('IFIMG_MEASUREMENT_LBLCNT', lib.IFIMG_MEASUREMENT_LBLCNT)
	IFIMG_MEASUREMENT_AREA = pIE('IFIMG_MEASUREMENT_AREA', lib.IFIMG_MEASUREMENT_AREA)
	IFIMG_MEASUREMENT_GRV = pIE('IFIMG_MEASUREMENT_GRV', lib.IFIMG_MEASUREMENT_GRV)
	IFIMG_MEASUREMENT_FERE = pIE('IFIMG_MEASUREMENT_FERE', lib.IFIMG_MEASUREMENT_FERE)
	IFIMG_MEASUREMENT_ELLIPSE = pIE('IFIMG_MEASUREMENT_ELLIPSE', lib.IFIMG_MEASUREMENT_ELLIPSE)
	IFIMG_PIXEL_RGB = pIE('IFIMG_PIXEL_RGB', lib.IFIMG_PIXEL_RGB)
	IFIMG_PIXEL_BGR = pIE('IFIMG_PIXEL_BGR', lib.IFIMG_PIXEL_BGR)
	pass

# 7: ImgStartCapture
# ------------------
class ImgStartCapture_StartMode(pyinterface.Identifer):
	IFIMG_DMACAPTURE_START = pIE('IFIMG_DMACAPTURE_START', lib.IFIMG_DMACAPTURE_START)
	IFIMG_SDRAMCAPTURE_START = pIE('IFIMG_SDRAMCAPTURE_START', lib.IFIMG_SDRAMCAPTURE_START)
	pass

# 8: ImgStopCapture
# ------------------
class ImgStopCapture_StopMode(pyinterface.Identifer):
	IFIMG_FRAME_STOP = pIE('IFIMG_FRAME_STOP', lib.IFIMG_FRAME_STOP)
	IFIMG_IMMEDIATE_STOP = pIE('IFIMG_IMMEDIATE_STOP', lib.IFIMG_IMMEDIATE_STOP)
	IFIMG_SDRAM_FRAME_STOP = pIE('IFIMG_SDRAM_FRAME_STOP', lib.IFIMG_SDRAM_FRAME_STOP)
	IFIMG_SDRAM_IMMEDIATE_STOP = pIE('IFIMG_SDRAM_IMMEDIATE_STOP', lib.IFIMG_SDRAM_IMMEDIATE_STOP)
	pass

# 10: ImgSetOutputMode
# ------------------
class ImgSetOutputMode_Mode(pyinterface.Identifer):
	IFIMG_OUTMODE_THROUGH = pIE('IFIMG_OUTMODE_THROUGH', lib.IFIMG_OUTMODE_THROUGH)
	IFIMG_OUTMODE_COLORBAR = pIE('IFIMG_OUTMODE_COLORBAR', lib.IFIMG_OUTMODE_COLORBAR)
	IFIMG_OUTMODE_PICTURE = pIE('IFIMG_OUTMODE_PICTURE', lib.IFIMG_OUTMODE_PICTURE)
	pass

# 17: ImgInputDI
# ------------------
class ImgInputDI_DI(pyinterface.BitIdentifer):
    size = 16
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
    pass

# 18: ImgOutputDO
# ------------------
class ImgOutputDO_DO(pyinterface.BitIdentifer):
    size = 16
    bits = [pyinterface.BitIdentiferElement(i) for i in range(size)]
    del(i)
    bits[0].set_params('OUT1', 'High', 'Low')
    bits[1].set_params('OUT2', 'High', 'Low')
    bits[2].set_params('OUT3', 'High', 'Low')
    bits[3].set_params('OUT4', 'High', 'Low')
    bits[4].set_params('OUT5', 'High', 'Low')
    bits[5].set_params('OUT6', 'High', 'Low')
    bits[6].set_params('OUT7', 'High', 'Low')
    bits[7].set_params('OUT8', 'High', 'Low')
    pass

# 24: ImgSetChannel
# structure 8: IMGCAPCONFIG
# ------------------
class ImgSetChannel_ChannelNum(pyinterface.Identifer):
#class IMGCAPCONFIG_dwChangePattern(pyinterface.Identifer):
	IFIMG_CHANNEL_CN1 = pIE('IFIMG_CHANNEL_CN1', lib.IFIMG_CHANNEL_CN1)
	IFIMG_CHANNEL_CN4 = pIE('IFIMG_CHANNEL_CN4', lib.IFIMG_CHANNEL_CN4)
	IFIMG_CHANNEL_CN5 = pIE('IFIMG_CHANNEL_CN5', lib.IFIMG_CHANNEL_CN5)
	IFIMG_CHANNEL_CN6 = pIE('IFIMG_CHANNEL_CN6', lib.IFIMG_CHANNEL_CN6)
	IFIMG_CHANNEL_CN7 = pIE('IFIMG_CHANNEL_CN7', lib.IFIMG_CHANNEL_CN7)
	pass

# 30: ImgBmCaptureData
# ------------------
class ImgBmCaptureData_Position(pyinterface.Identifer):
	IFIMG_BUFF_HEAD = pIE('IFIMG_BUFF_HEAD', lib.IFIMG_BUFF_HEAD)
	IFIMG_BUFF_CONTINUATION = pIE('IFIMG_BUFF_CONTINUATION', lib.IFIMG_BUFF_CONTINUATION)
	pass

# 35: ImgSetColorIngredient
# structure 4: IMGBINCONFIG
# ------------------
class ImgSetColorIngredient_Ingredient(pyinterface.Identifer):
#class IMGBINCONFIG_dwColorIngredient(pyinterface.Identifer):
	IFIMG_INGREDIENT_RED = pIE('IFIMG_INGREDIENT_RED', lib.IFIMG_INGREDIENT_RED)
	IFIMG_INGREDIENT_GREEN = pIE('IFIMG_INGREDIENT_GREEN', lib.IFIMG_INGREDIENT_GREEN)
	IFIMG_INGREDIENT_BLUE = pIE('IFIMG_INGREDIENT_BLUE', lib.IFIMG_INGREDIENT_BLUE)
	IFIMG_INGREDIENT_GRAY = pIE('IFIMG_INGREDIENT_GRAY', lib.IFIMG_INGREDIENT_GRAY)
	pass

# 37: ImgSetConversionConfig
# ------------------
class ImgSetConversionConfig_CnvEnabled(pyinterface.BitIdentifer):
    size = 32
    bits = [pyinterface.BitIdentiferElement(i) for i in range(size)]
    del(i)
    bits[0].set_params('CH1', 'OFF', 'ON')
    bits[1].set_params('CH2', 'OFF', 'ON')
    bits[2].set_params('CH3', 'OFF', 'ON')
    pass

# 39: ImgSetFilter
# ------------------
class ImgSetFilter_FilterSelect(pyinterface.Identifer):
	IFIMG_SPATIAL_FILTER = pIE('IFIMG_SPATIAL_FILTER', lib.IFIMG_SPATIAL_FILTER)
	IFIMG_EDGE_FILTER = pIE('IFIMG_EDGE_FILTER', lib.IFIMG_EDGE_FILTER)
	pass

# 41: ImgSetLabelingConfig
# ------------------
class ImgSetLabelingConfig_Connection(pyinterface.Identifer):
	IFIMG_FOUR_CONNECTION = pIE('IFIMG_FOUR_CONNECTION', lib.IFIMG_FOUR_CONNECTION)
	IFIMG_EIGHT_CONNECTION = pIE('IFIMG_EIGHT_CONNECTION', lib.IFIMG_EIGHT_CONNECTION)
	pass

# 48: ImgSetSyncErrorDetection
# ------------------
class ImgSetSyncErrorDetection_Mode(pyinterface.Identifer):
	IFIMG_ERR_DETECTION_MODE1 = pIE('IFIMG_ERR_DETECTION_MODE1', lib.IFIMG_ERR_DETECTION_MODE1)
	IFIMG_ERR_DETECTION_MODE2 = pIE('IFIMG_ERR_DETECTION_MODE2', lib.IFIMG_ERR_DETECTION_MODE2)
	IFIMG_ERR_DETECTION_MODE3 = pIE('IFIMG_ERR_DETECTION_MODE3', lib.IFIMG_ERR_DETECTION_MODE3)
	IFIMG_ERR_DETECTION_MODE4 = pIE('IFIMG_ERR_DETECTION_MODE4', lib.IFIMG_ERR_DETECTION_MODE4)
	IFIMG_ERR_DETECTION_MODE5 = pIE('IFIMG_ERR_DETECTION_MODE5', lib.IFIMG_ERR_DETECTION_MODE5)
	IFIMG_ERR_DETECTION_MODE6 = pIE('IFIMG_ERR_DETECTION_MODE6', lib.IFIMG_ERR_DETECTION_MODE6)
	IFIMG_ERR_DETECTION_MODE7 = pIE('IFIMG_ERR_DETECTION_MODE7', lib.IFIMG_ERR_DETECTION_MODE7)
	IFIMG_ERR_DETECTION_MODE8 = pIE('IFIMG_ERR_DETECTION_MODE8', lib.IFIMG_ERR_DETECTION_MODE8)
	pass

# 49: ImgGetCameraConnectionStatus
# ------------------
class ImgGetCameraConnectionStatus_Status(pyinterface.Identifer):
	IFIMG_CAMERA_NOTSUPPORTED = pIE('IFIMG_CAMERA_NOTSUPPORTED', lib.IFIMG_CAMERA_NOTSUPPORTED)
	IFIMG_CAMERA_CONNECTION = pIE('IFIMG_CAMERA_CONNECTION', lib.IFIMG_CAMERA_CONNECTION)
	IFIMG_CAMERA_UNCONNECTION = pIE('IFIMG_CAMERA_UNCONNECTION', lib.IFIMG_CAMERA_UNCONNECTION)
	pass

# 50: ImgSetImposeImage
# ------------------
class ImgSetImposeImage_SetMode(pyinterface.Identifer):
#class ImgSetImposeImage_ImposeNum(pyinterface.Identifer):
	IFIMG_SET_IMPOSE = pIE('IFIMG_SET_IMPOSE', lib.IFIMG_SET_IMPOSE)
	IFIMG_SELECT_IMPOSE = pIE('IFIMG_SELECT_IMPOSE', lib.IFIMG_SELECT_IMPOSE)
	IFIMG_NON_IMPOSE = pIE('IFIMG_NON_IMPOSE', lib.IFIMG_NON_IMPOSE)
	IFIMG_CHECK_SETINPOSE = pIE('IFIMG_CHECK_SETINPOSE', lib.IFIMG_CHECK_SETINPOSE)
	pass

class ImgSetImposeImage_ImposeOperation(pyinterface.Identifer):
	IFIMG_IMPOSE_REPLACE = pIE('IFIMG_IMPOSE_REPLACE', lib.IFIMG_IMPOSE_REPLACE)
	IFIMG_IMPOSE_ADD = pIE('IFIMG_IMPOSE_ADD', lib.IFIMG_IMPOSE_ADD)
	IFIMG_IMPOSE_SUB = pIE('IFIMG_IMPOSE_SUB', lib.IFIMG_IMPOSE_SUB)
	IFIMG_IMPOSE_XOR = pIE('IFIMG_IMPOSE_XOR', lib.IFIMG_IMPOSE_XOR)
	IFIMG_IMPOSE_PERMEATION_3_1 = pIE('IFIMG_IMPOSE_PERMEATION_3_1', lib.IFIMG_IMPOSE_PERMEATION_3_1)
	IFIMG_IMPOSE_PERMEATION = pIE('IFIMG_IMPOSE_PERMEATION', lib.IFIMG_IMPOSE_PERMEATION)
	IFIMG_IMPOSE_PERMEATION_1_3 = pIE('IFIMG_IMPOSE_PERMEATION_1_3', lib.IFIMG_IMPOSE_PERMEATION_1_3)
	pass

# 52: ImgSetImposeDateTimeInfo
# ------------------
class ImgSetImposeDateTimeInfo_SetMode(pyinterface.Identifer):
	IFIMG_IMPOSE_NONE_DATETIME = pIE('IFIMG_IMPOSE_NONE_DATETIME', lib.IFIMG_IMPOSE_NONE_DATETIME)
	IFIMG_IMPOSE_SET_DATE = pIE('IFIMG_IMPOSE_SET_DATE', lib.IFIMG_IMPOSE_SET_DATE)
	IFIMG_IMPOSE_SET_TIME = pIE('IFIMG_IMPOSE_SET_TIME', lib.IFIMG_IMPOSE_SET_TIME)
	IFIMG_IMPOSE_STRING_OUTLINE = pIE('IFIMG_IMPOSE_STRING_OUTLINE', lib.IFIMG_IMPOSE_STRING_OUTLINE)
	pass

# structure 1: IMGCAPSTATUS
# ------------------
class IMGCAPSTATUS_dwCapture(pyinterface.BitIdentifer):
    size = 32
    bits = [pyinterface.BitIdentiferElement(i) for i in range(size)]
    del(i)
    bits[0].set_params('CH1', 'OFF', 'ON')
    bits[1].set_params('CH2', 'OFF', 'ON')
    bits[2].set_params('CH3', 'OFF', 'ON')
    bits[3].set_params('CH4', 'OFF', 'ON')
    bits[8].set_params('CH5', 'OFF', 'ON')
    bits[9].set_params('CH6', 'OFF', 'ON')
    bits[10].set_params('CH7', 'OFF', 'ON')
    pass

class IMGCAPSTATUS_dwTrigger(pyinterface.BitIdentifer):
    size = 32
    bits = [pyinterface.BitIdentiferElement(i) for i in range(size)]
    del(i)
    bits[0].set_params('CH1', 'OFF', 'ON')
    bits[1].set_params('CH2', 'OFF', 'ON')
    bits[2].set_params('CH3', 'OFF', 'ON')
    pass

# structure 2: IMGCAPSTATUSEX
# ------------------
class IMGCAPSTATUSEX_dwCapture(pyinterface.BitIdentifer):
    size = 32
    bits = [pyinterface.BitIdentiferElement(i) for i in range(size)]
    del(i)
    bits[0].set_params('CH1', 'OFF', 'ON')
    bits[1].set_params('CH2', 'OFF', 'ON')
    bits[2].set_params('CH3', 'OFF', 'ON')
    bits[3].set_params('CH4', 'OFF', 'ON')
    bits[4].set_params('CH5', 'OFF', 'ON')
    bits[5].set_params('CH6', 'OFF', 'ON')
    bits[8].set_params('CH7', 'OFF', 'ON')
    bits[9].set_params('CH8', 'OFF', 'ON')
    bits[10].set_params('CH9', 'OFF', 'ON')
    pass

class IMGCAPSTATUSEX_dwTrigger(pyinterface.BitIdentifer):
    size = 32
    bits = [pyinterface.BitIdentiferElement(i) for i in range(size)]
    del(i)
    bits[0].set_params('CH1', 'OFF', 'ON')
    bits[1].set_params('CH2', 'OFF', 'ON')
    bits[2].set_params('CH3', 'OFF', 'ON')
    bits[4].set_params('CH4', 'OFF', 'ON')
    pass

# structure 5: IMGTRGCONFIG
# ------------------
class IMGTRGCONFIG_dwTriggerEnabled(pyinterface.BitIdentifer):
    size = 32
    bits = [pyinterface.BitIdentiferElement(i) for i in range(size)]
    del(i)
    bits[0].set_params('CH1', 'OFF', 'ON')
    bits[1].set_params('CH2', 'OFF', 'ON')
    bits[2].set_params('CH3', 'OFF', 'ON')
    pass

class IMGTRGCONFIG_dwTriggerRangeMode(pyinterface.BitIdentifer):
    size = 32
    bits = [pyinterface.BitIdentiferElement(i) for i in range(size)]
    del(i)
    bits[0].set_params('CH1', 'OFF', 'ON')
    bits[1].set_params('CH2', 'OFF', 'ON')
    pass

# structure 6: IMGEVENTTABLE
# ------------------
class IMGEVENTTABLE_dwDI(pyinterface.BitIdentifer):
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

class IMGEVENTTABLE_dwFrame(pyinterface.BitIdentifer):
    size = 32
    bits = [pyinterface.BitIdentiferElement(i) for i in range(size)]
    del(i)
    bits[0].set_params('CH1', 'OFF', 'ON')
    bits[1].set_params('CH2', 'OFF', 'ON')
    bits[2].set_params('CH3', 'OFF', 'ON')
    bits[3].set_params('CH4', 'OFF', 'ON')
    pass

class IMGEVENTTABLE_dwTrigger(pyinterface.BitIdentifer):
    size = 32
    bits = [pyinterface.BitIdentiferElement(i) for i in range(size)]
    del(i)
    bits[0].set_params('CH1', 'OFF', 'ON')
    bits[1].set_params('CH2', 'OFF', 'ON')
    bits[2].set_params('CH3', 'OFF', 'ON')
    bits[3].set_params('CH4', 'OFF', 'ON')
    bits[4].set_params('CH5', 'OFF', 'ON')
    bits[16].set_params('CH6', 'OFF', 'ON')
    pass

# structure 7: IMGEVENTTABLEEX
# ------------------
class IMGEVENTTABLEEX_dwDI(pyinterface.BitIdentifer):
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

class IMGEVENTTABLEEX_dwFrame(pyinterface.BitIdentifer):
    size = 32
    bits = [pyinterface.BitIdentiferElement(i) for i in range(size)]
    del(i)
    bits[0].set_params('CH1', 'OFF', 'ON')
    bits[1].set_params('CH2', 'OFF', 'ON')
    bits[2].set_params('CH3', 'OFF', 'ON')
    bits[3].set_params('CH4', 'OFF', 'ON')
    pass

class IMGEVENTTABLEEX_dwTrigger(pyinterface.BitIdentifer):
    size = 32
    bits = [pyinterface.BitIdentiferElement(i) for i in range(size)]
    del(i)
    bits[0].set_params('CH1', 'OFF', 'ON')
    bits[1].set_params('CH2', 'OFF', 'ON')
    bits[2].set_params('CH3', 'OFF', 'ON')
    bits[3].set_params('CH4', 'OFF', 'ON')
    bits[4].set_params('CH5', 'OFF', 'ON')
    pass

# structure 8: IMGCAPCONFIG
# ------------------
class IMGCAPCONFIG_dwMode(pyinterface.Identifer):
	IFIMG_CAPTURE_NORMAL = pIE('IFIMG_CAPTURE_NORMAL', lib.IFIMG_CAPTURE_NORMAL)
	IFIMG_CAPTURE_THINOUT = pIE('IFIMG_CAPTURE_THINOUT', lib.IFIMG_CAPTURE_THINOUT)
	IFIMG_CAPTURE_TIMER = pIE('IFIMG_CAPTURE_TIMER', lib.IFIMG_CAPTURE_TIMER)
	IFIMG_CAPTURE_CH_FRAME = pIE('IFIMG_CAPTURE_CH_FRAME', lib.IFIMG_CAPTURE_CH_FRAME)
	IFIMG_CAPTURE_CH_TIMER = pIE('IFIMG_CAPTURE_CH_TIMER', lib.IFIMG_CAPTURE_CH_TIMER)
	pass

# structure 9: IMGPTNCONFIG
# ------------------
class IMGPTNCONFIG_dwAutoRevision(pyinterface.Identifer):
	IFIMG_AUTO_ENABLE = pIE('IFIMG_AUTO_ENABLE', lib.IFIMG_AUTO_ENABLE)
	IFIMG_AUTO_DISABLE = pIE('IFIMG_AUTO_DISABLE', lib.IFIMG_AUTO_DISABLE)
	pass

class IMGPTNCONFIG_dwTriggerMode(pyinterface.Identifer):
	IFIMG_PTNMATCH_NORMAL = pIE('IFIMG_PTNMATCH_NORMAL', lib.IFIMG_PTNMATCH_NORMAL)
	IFIMG_PTNMATCH_REVERSAL = pIE('IFIMG_PTNMATCH_REVERSAL', lib.IFIMG_PTNMATCH_REVERSAL)
	IFIMG_PTNMATCH_NONE = pIE('IFIMG_PTNMATCH_NONE', lib.IFIMG_PTNMATCH_NONE)
	pass

# structure 14: IMGDILATE_ERODE
# ------------------
class IMGDILATE_ERODE_dwSelectD_E(pyinterface.BitIdentifer):
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

class IMGDILATE_ERODE_dwNeighborhood(pyinterface.BitIdentifer):
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


# Error Wrapper
# =============
class ErrorGPG7204(pyinterface.ErrorCode):
    IFIMG_ERROR_SUCCESS = pIE('IFIMG_ERROR_SUCCESS', lib.IFIMG_ERROR_SUCCESS)
    IFIMG_ERROR_NOT_DEVICE = pIE('IFIMG_ERROR_NOT_DEVICE', lib.IFIMG_ERROR_NOT_DEVICE)
    IFIMG_ERROR_NOT_OPEN = pIE('IFIMG_ERROR_NOT_OPEN', lib.IFIMG_ERROR_NOT_OPEN)
    IFIMG_ERROR_INVALID_DEVICE_NUMBER = pIE('IFIMG_ERROR_INVALID_DEVICE_NUMBER',lib.IFIMG_ERROR_INVALID_DEVICE_NUMBER)
    IFIMG_ERROR_ALREADY_OPEN = pIE('IFIMG_ERROR_ALREADY_OPEN',lib.IFIMG_ERROR_ALREADY_OPEN)
    IFIMG_ERROR_NOT_SUPPORTED = pIE('IFIMG_ERROR_NOT_SUPPORTED',lib.IFIMG_ERROR_NOT_SUPPORTED)
    IFIMG_ERROR_INVALID_PARAMETER = pIE('IFIMG_ERROR_INVALID_PARAMETER',lib.IFIMG_ERROR_INVALID_PARAMETER)
    IFIMG_ERROR_NOT_ALLOCATE_MEMO = pIE('IFIMG_ERROR_NOT_ALLOCATE_MEMO',lib.IFIMG_ERROR_NOT_ALLOCATE_MEMO)
    IFIMG_ERROR_NOT_ALLOCATE_MEMONOW_CAPTURING = pIE('IFIMG_ERROR_NOT_ALLOCATE_MEMONOW_CAPTURING',lib.IFIMG_ERROR_NOT_ALLOCATE_MEMONOW_CAPTURING)
    IFIMG_ERROR_NOW_STOP = pIE('IFIMG_ERROR_NOW_STOP',lib.IFIMG_ERROR_NOW_STOP)
    IFIMG_ERROR_NULL_POINTER = pIE('IFIMG_ERROR_NULL_POINTER',lib.IFIMG_ERROR_NULL_POINTER)
    IFIMG_ERROR_WRITE_FAILED = pIE('IFIMG_ERROR_WRITE_FAILED', lib.IFIMG_ERROR_WRITE_FAILED)
    IFIMG_ERROR_READ_FAILED = pIE('IFIMG_ERROR_READ_FAILED', lib.IFIMG_ERROR_READ_FAILED)
    IFIMG_ERROR_NOBUFFER = pIE('IFIMG_ERROR_NOBUFFER',lib.IFIMG_ERROR_NOBUFFER)
    IFIMG_ERROR_INVALID_OFFSET = pIE('IFIMG_ERROR_INVALID_OFFSET',lib.IFIMG_ERROR_INVALID_OFFSET)
    IFIMG_ERROR_SDRAM_NOW_CAPTURING = pIE('IFIMG_ERROR_SDRAM_NOW_CAPTURING',lib.IFIMG_ERROR_SDRAM_NOW_CAPTURING)
    IFIMG_ERROR_SDRAM_NOW_STOP = pIE('IFIMG_ERROR_SDRAM_NOW_STOP',lib.IFIMG_ERROR_SDRAM_NOW_STOP)
    IFIMG_ERROR_NOT_SET_COMPDATA = pIE('IFIMG_ERROR_NOT_SET_COMPDATA',lib.IFIMG_ERROR_NOT_SET_COMPDATA)
    IFIMG_ERROR_SDRAM_NOTSET_CAPDATA = pIE('IFIMG_ERROR_SDRAM_NOTSET_CAPDATA',lib.IFIMG_ERROR_SDRAM_NOTSET_CAPDATA)
    IFIMG_ERROR_NOT_COMPDATA = pIE('IFIMG_ERROR_NOT_COMPDATA',lib.IFIMG_ERROR_NOT_COMPDATA)
    IFIMG_ERROR_INVALID_SDRAM_ID = pIE('IFIMG_ERROR_INVALID_SDRAM_ID',lib.IFIMG_ERROR_INVALID_SDRAM_ID)
    IFIMG_ERROR_SDRAM_NOT_CAPDATA = pIE('IFIMG_ERROR_SDRAM_NOT_CAPDATA',lib.IFIMG_ERROR_SDRAM_NOT_CAPDATA)
    IFIMG_ERROR_SDRAM_NOMEMORY = pIE('IFIMG_ERROR_SDRAM_NOMEMORY',lib.IFIMG_ERROR_SDRAM_NOMEMORY)
    IFIMG_ERROR_INVALID_FORMAT = pIE('IFIMG_ERROR_INVALID_FORMAT',lib.IFIMG_ERROR_INVALID_FORMAT)
    IFIMG_EROOR_NOW_SDRAM_BM = pIE('IFIMG_EROOR_NOW_SDRAM_BM',lib.IFIMG_EROOR_NOW_SDRAM_BM)
    IFIMG_ERROR_NOW_IMPOSEDATA_WRITE = pIE('IFIMG_ERROR_NOW_IMPOSEDATA_WRITE',lib.IFIMG_ERROR_NOW_IMPOSEDATA_WRITE)

    _success = IFIMG_ERROR_SUCCESS
    pass


# ==========================
# GPG-5520 Python 
# ==========================



# ==========================
# GPG-5520 Python Controller
# ==========================

class gpg5520_controller(object):
    ndev = int()

    boardid = ''
    print_log = True
    
    def __init__(self, ndev=1, boardid=5520, initialize=True):
        """
        boardid = 5520
        """
        self.ndev = ndev
        self.boardid = BoardID.verify(boardid)
        if initialize: self.initialize()
        return

    def _log(self, msg):
        if self.print_log:
            print('Interface GPG5520(%d): %s'%(self.ndev, msg))
            pass
        return
    
    def _error_check(self, error_no):
        ErrorGPG5520.check(error_no)
        return

    def initialize(self):
        self.open()
        return
    
    def open(self):
        """
        1. ImgOpen
        """
        self._log('open')
        ret = lib.ImgOpen(self.ndev)
        self._error_check(ret)
        return

    def close(self):
        """
        2. ImgClose
        """
        self._log('close')
        ret = lib.ImgClose(self.ndev)
        self._error_check(ret)
        return

    def get_capture_status(self):
        """
        3. ImgGetCaptureStatus
        """
        self._log('get_capture_status')
        config = lib.IMGCAPSTATUS()
        config.dwCapture = ctypes.c_ulong(0)
        config.dwFrameCnt = ctypes.c_ulong(0)
        config.dwTrigger = ctypes.c_ulong(0)
        ret = lib.ImgGetCaptureStatus(self.ndev, config)
        self._error_check(ret)
        config.dwCapture = IMGCAPSTATUS_dwCapture(config.value)
        config.dwTrigger = IMGCAPSTATUS_dwTrigger(config.value)
        return config

    def get_capture_status_ex(self):
        """
        4. ImgGetCaptureStatusEx
        """
        self._log('get_capture_status_ex')
        config = lib.IMGCAPSTATUSEX()
        config.dwCapture = ctypes.c_ulong(0)
        config.dwFrameCntDMA = ctypes.c_ulong(0)
        config.dwFrameCntDRAM = ctypes.c_ulong(0)
        config.dwTrigger = ctypes.c_ulong(0)
        ret = lib.ImgGetCaptureStatusEx(self.ndev, config)
        self._error_check(ret)
        config.dwCapture = IMGCAPSTATUSEX_dwCapture(config.value)
        config.dwTrigger = IMGCAPSTATUSEX_dwTrigger(config.value)
        return config

    def set_buffer(self, BufferFormat = 'IFIMG_COLOR_RGB24', Address, Size):
        """
        5. ImgSetBuffer
        """
        self._log('set_buffer')
        BufferFormat = ImgSetBuffer_BufferFormat.verify(BufferFormat)
        config = lib.IMGBUFFERINFO()
        config.pBufferAddress = Address
        config.dwBufferSize = Size
        ret = lib.ImgSetBuffer(self.ndev, config, BufferFormat)
        self._error_check(ret)
        return


    def start_capture(self, FrameCnt , StartMode = 'IFIMG_DMACAPTURE_START'):
        """
        7. ImgStartCapture
        """
        self._log('start_capture')
        StartMode = ImgStartCapture_StartMode.verify(StartMode)
        ret = lib.ImgStartCapture(self.ndev, FrameCnt, StartMode)
        self._error_check(ret)
        return


    def clip_data(dest, src, FrameNum, dwDataFormat = 'IFIMG_COLOR_RGB24', dwXcoodinates = 0, dwYcoodinates = 0, dwXLength = 640, dwXLength = 480):
        """
        34. ImgClipData
        """
        self._log('clip_data')
        dwDataFormat = ImgSetBuffer_BufferFormat.verify(dwDataFormat)
        config = lib.IMGCLIPCONFIG()
        config.dwDataFormat = dwDataFormat
        config.dwXcoodinates = dwXcoodinates
        config.dwYcoodinates = dwYcoodinates
        config.dwXLength= dwXLength
        config.dwYLength = dwYLength
        ret = lib.ImgClipData(dest, src, FrameNum, config)
        self._error_check(ret)
        return


    def save_bit_map_file(PathName, BufferPointer, BufferFormat = 'IFIMG_COLOR_RGB24', Width, Height):
        """
        43. ImgSaveBitMapFile
        """
        self._log('save_bit_map_file')
        BufferFormat = ImgSetBuffer_BufferFormat.verify(BufferFormat)
        ret = lib.ImgSaveBitMapFile(PathName, BufferPointer, BufferFormat, Width,Height)
        self._error_check(ret)
        return























