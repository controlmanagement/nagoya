
import os
import ctypes
import pyinterface

#
# based on fbimtr.h (Version 1.01-01)
#

# ==========
# Structures
# ==========

# function pointer
# ----------------

PLPIMGCALLBACKEX = ctypes.CFUNCTYPE(IMGEVENTTABLEEX, ctypes.c_ulong)

# Original  
# ------------
class IMGCAPSTATUS(pyinterface.Structure):
    _fields_ = [('dwCapture', ctypes.c_ulong),
                ('dwFrameCnt', ctypes.c_ulong),
                ('dwTrigger', ctypes.c_ulong)]

class IMGCAPSTATUSEX(pyinterface.Structure):
    _fields_ = [('dwCapture', ctypes.c_ulong),
                ('dwFrameCntDMA', ctypes.c_ulong),
                ('dwFrameCntDRAM', ctypes.c_ulong),
                ('dwTrigger', ctypes.c_ulong)]

class IMGBUFFERINFO(pyinterface.Structure):
    _fields_ = [('pBufferAddress', ctypes.c_void_p),
                ('dwBufferSize', ctypes.c_ulong)]

class IMGBINCONFIG(pyinterface.Structure):
    _fields_ = [('dwColorIngredient', ctypes.c_ulong),
                ('dwMaxthreshould', ctypes.c_ulong),
                ('dwMinthreshould', ctypes.c_ulong),
                ('dwBinarizationMode', ctypes.c_ulong)]

class IMGTRGCONFIG(pyinterface.Structure):
    _fields_ = [('dwTriggerEnabled', ctypes.c_ulong),
                ('dwAreaMax', ctypes.c_ulong),
                ('dwAreaMin', ctypes.c_ulong),
                ('dwStartPointX', ctypes.c_ulong),
                ('dwStartPointY', ctypes.c_ulong),
                ('dwXLength', ctypes.c_ulong),
                ('dwYLength', ctypes.c_ulong),
                ('dwTriggerRangeMode', ctypes.c_ulong)]

class IMGEVENTTABLE(pyinterface.Structure):
    _fields_ = [('dwDI', ctypes.c_ulong),
                ('dwFrame', ctypes.c_ulong),
                ('dwTrigger', ctypes.c_ulong)]

class IMGEVENTTABLEEX(pyinterface.Structure):
    _fields_ = [('dwDI', ctypes.c_ulong),
                ('dwFrame', ctypes.c_ulong),
                ('dwTrigger', ctypes.c_ulong),
                ('dwFrameCntDMA', ctypes.c_ulong),
                ('dwFrameCntSDRAM', ctypes.c_ulong),
                ('dwXCoorddinates', ctypes.c_ulong),
                ('dwYCoorddinates', ctypes.c_ulong),
                ('dwPercentage', ctypes.c_ulong)]

class IMGEVENTTABLEEX(pyinterface.Structure):
    _fields_ = [('dwMode', ctypes.c_ulong),
                ('dwThinFrameCnt', ctypes.c_ulong),
                ('dwTimerCycle', ctypes.c_ulong),
                ('dwChFrameCnt', ctypes.c_ulong),
                ('dwChangePattern', ctypes.c_ulong)]

class IMGCAPCONFIG(pyinterface.Structure):
    _fields_ = [('dwMode', ctypes.c_ulong),
                ('dwThinFrameCnt', ctypes.c_ulong),
                ('dwTimerCycle', ctypes.c_ulong),
                ('dwChFrameCnt', ctypes.c_ulong),
                ('dwChangePattern[5]', ctypes.c_ulong)]

class IMGTNCONFIG(pyinterface.Structure):
    _fields_ = [('dwSDRAMId', ctypes.c_ulong),
                ('dwAutoRevision', ctypes.c_ulong),
                ('dwXCoorddinates', ctypes.c_ulong),
                ('dwYCoorddinates', ctypes.c_ulong),
                ('dwPercentage', ctypes.c_ulong),
                ('dwTriggerMode', ctypes.c_ulong)]

class IMGCLIPCONFIG(pyinterface.Structure):
    _fields_ = [('dwDataFormat', ctypes.c_ulong),
                ('dwXCoorddinates', ctypes.c_ulong),
                ('dwYCoorddinates', ctypes.c_ulong),
                ('dwXLength', ctypes.c_ulong),
                ('dwYLength', ctypes.c_ulong)]

class IMGMEASURE(pyinterface.Structure):
    _fields_ = [('dwArea', ctypes.c_ulong),
                ('dwXCoorddinates', ctypes.c_ulong),
                ('dwYCoorddinates', ctypes.c_ulong),
                ('dwFeretX1', ctypes.c_ulong),
                ('dwFeretX2', ctypes.c_ulong),
                ('dwFeretY1', ctypes.c_ulong),
                ('dwFeretY2', ctypes.c_ulong),
                ('dwFeretH', ctypes.c_ulong),
                ('dwFeretV', ctypes.c_ulong),
                ('dAngle', ctypes.c_float)]

class IMGFILTER(pyinterface.Structure):
    _fields_ = [('a', ctypes.c_int),
                ('b', ctypes.c_int),
                ('c', ctypes.c_int),
                ('d', ctypes.c_int),
                ('e', ctypes.c_int),
                ('f', ctypes.c_int),
                ('g', ctypes.c_int),
                ('h', ctypes.c_int),
                ('i', ctypes.c_int)]

class IMGDILATE_ERODE(pyinterface.Structure):
    _fields_ = [('dwStepCnt', ctypes.c_ulong),
                ('dwSelectDLID_E', ctypes.c_ulong),
                ('dwNeighborhood', ctypes.c_ulong)]

class IFIMGTIME(pyinterface.Structure):
    _fields_ = [('sec', ctypes.c_int,
                ('min', ctypes.c_int),
                ('hour', ctypes.c_int)]

class IFIMGDATE(pyinterface.Structure):
    _fields_ = [('mday', ctypes.c_int,
                ('mon', ctypes.c_int),
                ('year', ctypes.c_int)]

class IFIMGTIMEINFO(pyinterface.Structure):
    _fields_ = [('Time', IFIMGTIME),
                ('XCoorddinates', ctypes.c_int),
                ('YCoorddinates', ctypes.c_int)]

class IFIMGDATEINFO(pyinterface.Structure):
    _fields_ = [('Date', IFIMGDATE),
                ('XCoorddinates', ctypes.c_int),
                ('YCoorddinates', ctypes.c_int)]


# ==========
# Identiferse
# ==========

# 5: ImgSetBuffer
# 26: ImgAllocateSDRAM
# 43: ImgSaveBitMapFile
# =============
# ImgSetBuffer : BufferFormat
# ImgAllocateSDRAM : DataFormat
# ImgSaveBitMapFile : BufferFormat
# ------------------
IFIMG_COLOR_RGB32 = 
IFIMG_COLOR_RGB24 = 
IFIMG_COLOR_RGB15 = 
IFIMG_COLOR_GRAY8 = 
IFIMG_COLOR_RED8 = 
IFIMG_COLOR_GREEN8 = 
IFIMG_COLOR_BLUE8 = 
IFIMG_COLOR_BIN8 = 
IFIMG_COLOR_RGB16 = 
IFIMG_COLOR_FIL8 = 
IFIMG_COLOR_LABEL8 = 
IFIMG_COLOR_CMP8 = 

IFIMG_RESOLUTION_320_240 =
IFIMG_RESOLUTION_160_120 =

IFIMG_MEASUREMENT_HSIT =
IFIMG_MEASUREMENT_PRO =
IFIMG_MEASUREMENT_LBLCNT =
IFIMG_MEASUREMENT_AREA =
IFIMG_MEASUREMENT_GRV = 
IFIMG_MEASUREMENT_FERE = 
IFIMG_PIXEL_RGB =
IFIMG_PIXEL_BGR = 

# 7: ImgStartCapture
# =============
# ImgStartCapture : StartMode
# ------------------
IFIMG_DMACAPTURE_START = 
IFIMG_SDRAMCAPTURE_START = 

# 8: ImgStopCapture
# =============
# ImgStopCapture : StopMode
# ------------------
IFIMG_FRAME_STOP =
IFIMG_IMMEDIATE_STOP = 
IFIMG_SDRAM_FRAME_STOP =
IFIMG_SDRAM_IMMEDIATE_STOP =

# 10: ImgSetOutputMode
# =============
# ImgSetOutputMode : Mode
# ------------------
IFIMG_OUTMODE_THROUGH = 
IFIMG_OUTMODE_COLORBAR =
IFIMG_OUTMODE_PICTURE =

# 24: ImgSetChannel
# =============
# ImgSetChannel : ChannelNum
# ------------------
IFIMG_CHANNEL_CN1 =
IFIMG_CHANNEL_CN4 =
IFIMG_CHANNEL_CN5 =
IFIMG_CHANNEL_CN6 =
IFIMG_CHANNEL_CN7 =

# 30: ImgBmCaptureData
# =============
# ImgBmCaptureData : Position
# ------------------
IFIMG_BUFF_HEAD =
IFIMG_BUFF_CONTINUATION =

# 35: ImgSetColorIngredient
# =============
# ImgSetColorIngredient : Ingredient
# ------------------
IFIMG_INGREDIENT_RED =
IFIMG_INGREDIENT_GREEN =
IFIMG_INGREDIENT_BLUE =
IFIMG_INGREDIENT_GRAY =

# 39: ImgSetFilter
# =============
# ImgSetFilter : FilterSelect
# ------------------
IFIMG_SPATIAL_FILTER =
IFIMG_EDGE_FILTER = 

# 41: ImgSetLabelingConfig
# =============
# ImgSetLabelingConfig : Connection
# ------------------
IFIMG_FOUR_CONNECTION = 
IFIMG_EIGHT_CONNECTION = 

# 48: ImgSetSyncErrorDetection
# =============
# ImgSetSyncErrorDetection : Mode
# ------------------
IFIMG_ERR_DETECTION_MODE1 = 
IFIMG_ERR_DETECTION_MODE2 = 
IFIMG_ERR_DETECTION_MODE3 = 
IFIMG_ERR_DETECTION_MODE4 = 
IFIMG_ERR_DETECTION_MODE5 = 
IFIMG_ERR_DETECTION_MODE6 = 
IFIMG_ERR_DETECTION_MODE7 = 
IFIMG_ERR_DETECTION_MODE8 = 

# 49: ImgGetCameraConnectionStatus
# =============
# ImgGetCameraConnectionStatus : Status
# ------------------
IFIMG_CAMERA_NOTSUPPORTED =
IFIMG_CAMERA_CONNECTION =
IFIMG_CAMERA_UNCONNECTION =

# 50: ImgSetImposeImage
# =============
# ImgSetImposeImage : SetMode
# ImgSetImposeImage : ImposeNum
# ------------------
IFIMG_SET_IMPOSE = 
IFIMG_SELECT_IMPOSE =
IFIMG_NON_IMPOSE =
IFIMG_CHECK_SETINPOSE =

# ImgSetImposeImage : ImposeOperation
# ------------------
IFIMG_IMPOSE_REPLACE =
IFIMG_IMPOSE_ADD =
IFIMG_IMPOSE_SUB =
IFIMG_IMPOSE_XOR =
IFIMG_IMPOSE_PERMEATION_3_1 =
IFIMG_IMPOSE_PERMEATION =
IFIMG_IMPOSE_PERMEATION_1_3 =

# 51: ImgSetImposeDateTimeInfo
# =============
# ImgSetImposeDateTimeInfo : SetMode
# ------------------
IFIMG_IMPOSE_NONE_DATETIME = 
IFIMG_IMPOSE_SET_DATE =
IFIMG_IMPOSE_SET_TIME = 
IFIMG_IMPOSE_STRING_OUTLINE =


# ==========
# RETURN VALUE
# ========== 
IFIMG_ERROR_SUCCESS = 0
IFIMG_ERROR_NOT_DEVICE = 0xc0000001
IFIMG_ERROR_NOT_OPEN = 0xc0000002
IFIMG_ERROR_INVALID_DEVICE_NUMBER =　0xc0000003
IFIMG_ERROR_ALREADY_OPEN = 0xc0000004
IFIMG_ERROR_NOT_SUPPORTED = 0xc0000009
IFIMG_ERROR_INVALID_PARAMETER = 0xc0000010
IFIMG_ERROR_NOT_ALLOCATE_MEMO = 0xc0000021
IFIMG_ERROR_NOT_ALLOCATE_MEMONOW_CAPTURING = 0xc0001000
IFIMG_ERROR_NOW_STOP = 0xc0001001
IFIMG_ERROR_NULL_POINTER = 0xc0001002
IFIMG_ERROR_WRITE_FAILED = 0xc0001003
IFIMG_ERROR_READ_FAILED = 0xc0001004
IFIMG_ERROR_NOBUFFER = 0xc0001005
IFIMG_ERROR_INVALID_OFFSET = 0xc0001006
IFIMG_ERROR_SDRAM_NOW_CAPTURING = 0xc0001007
IFIMG_ERROR_SDRAM_NOW_STOP = 0xc0001008
IFIMG_ERROR_NOT_SET_COMPDATA = 0xc0001009
IFIMG_ERROR_SDRAM_NOTSET_CAPDATA = 0xc000100a
IFIMG_ERROR_NOT_COMPDATA = 0xc000100b
IFIMG_ERROR_INVALID_SDRAM_ID = 0xc000100c
IFIMG_ERROR_SDRAM_NOT_CAPDATA = 0xc000100d
IFIMG_ERROR_SDRAM_NOMEMORY = 0xc000100e
IFIMG_ERROR_INVALID_FORMAT = 0xc000100f
IFIMG_EROOR_NOW_SDRAM_BM = 0xc0001010
IFIMG_ERROR_NOW_IMPOSEDATA_WRITE = 0xc000101d

# =========
# Functions
# =========

SO_DIR = '/usr/lib'
SO_NAME = 'libgpg5520.so'
SO_PATH = os.path.join(SO_DIR, SO_NAME)

try:
    lib = ctypes.cdll.LoadLibrary(SO_PATH)
except OSError:
    pass
else:
    pyinterface.so_available.append(SO_PATH)
    
    _int = ctypes.c_int
    _P = ctypes.POINTER
    _void_p = ctypes.c_void_p
    _ushort = ctypes.c_ushort
    _ulong_p = _P(ctypes.c_ulong)
    _ushort_p = _P(ctypes.c_ushort)
    _ulong = ctypes.c_ulong
    _char_p = ctypes.c_char_p
    _long = ctypes.c_long
    

    # 1 int ImgOpen(int);
    # -------------------
    ImgOpen = lib.ImgOpen
    ImgOpen.restype = _int
    ImgOpen.argtypes = (_int,)
    
    # 2 int ImgClose(int);
    # -------------------
    ImgClose = lib.ImgClose
    ImgClose.restype = _int
    ImgClose.argtypes = (_int,)
    
    # 3 int ImgGetCaptureStatus(int, PIMGCAPSTATUS);
    # -------------------
    ImgGetCaptureStatus = lib.ImgGetCaptureStatus
    ImgGetCaptureStatus.restype = _int
    ImgGetCaptureStatus.argtypes = (_int, _P(IMGCAPSTATUS))
    
    # 4 int ImgGetCaptureStatusEx(int, PIMGCAPSTATUSEX);
    # -------------------
    ImgGetCaptureStatusEx = lib.ImgGetCaptureStatusEx
    ImgGetCaptureStatusEx.restype = _int
    ImgGetCaptureStatusEx.argtypes = (_int, _P(IMGCAPSTATUSEX))

    # 5 int ImgSetBuffer(int, PIMGBUFFERINFO);
    # -------------------
    ImgSetBuffer = lib.ImgSetBuffer
    ImgSetBuffer.restype = _int
    ImgSetBuffer.argtypes = (_int, _P(IMGBUFFERINFO))

    # 6 int ImgGetMemPtrValue(int, void*);
    # -------------------
    ImgGetMemPtrValue = lib.ImgGetMemPtrValue
    ImgGetMemPtrValue.restype = _int
    ImgGetMemPtrValue.argtypes = (_void_p,)

    # 7 int ImgStartCapture(int, unsigned long, unsigned long);
    # -------------------
    ImgStartCapture = lib.ImgStartCapture
    ImgStartCapture.restype = _int
    ImgStartCapture.argtypes = (_int, _ulong, _ulong,)

    # 8 int ImgStopCapture(int, unsigned long);
    # -------------------
    ImgStopCapture = lib.ImgStopCapture
    ImgStopCapture.restype = _int
    ImgStopCapture.argtypes = (_int, _ulong,)

    # 9 int ImgSetPosition(int, int, int,);
    # -------------------
    ImgSetPosition = lib.ImgSetPosition
    ImgSetPosition.restype = _int
    ImgSetPosition.argtypes = (_int, _int, _int,)

    # 10 int ImgSetOutputMode(int, unsigned short);
    # -------------------
    ImgSetOutputMode = lib.ImgSetOutputMode
    ImgSetOutputMode.restype = _int
    ImgSetOutputMode.argtypes = (_int, _ushort,)

    # 11 int ImgSetStillPictureData(int, void*);
    # -------------------
    ImgSetStillPictureData = lib.ImgSetStillPictureData
    ImgSetStillPictureData.restype = _int
    ImgSetStillPictureData.argtypes = (_int, _void_p,)

    # 12 int ImgGetStillPictureData(int, void*);
    # -------------------
    ImgGetStillPictureData = lib.ImgGetStillPictureData
    ImgGetStillPictureData.restype = _int
    ImgGetStillPictureData.argtypes = (_int, _void_p,)

    # 13 int ImgSetBinarizationConfig(int, PIMGBINCONFIG);
    # -------------------
    ImgSetBinarizationConfig = lib.ImgSetBinarizationConfig
    ImgSetBinarizationConfig.restype = _int
    ImgSetBinarizationConfig.argtypes = (_int, _P(IMGBINCONFIG),)

    # 14 int ImgSetMeasurementRange(int, unsigned long, unsigned long, unsigned long, unsigned long,);
    # -------------------
    ImgSetBinarizationConfig = lib.ImgSetBinarizationConfig
    ImgSetBinarizationConfig.restype = _int
    ImgSetBinarizationConfig.argtypes = (_int, _ulong, _ulong, _ulong, _ulong,)

    # 15 int ImgGetMeasurementValuel(int, unsigned long*, unsigned long*, unsigned long*, unsigned long*,);
    # -------------------
    ImgGetMeasurementValuel = lib.ImgGetMeasurementValuel
    ImgGetMeasurementValuel.restype = _int
    ImgGetMeasurementValuel.argtypes = (_int, _ulong_p, _ulong_p, _ulong_p, _ulong_p,)

    # 16 int ImgSetTriggerConfig(int, PIMGTRGCONFIG);
    # -------------------
    ImgSetTriggerConfig = lib.ImgSetTriggerConfig
    ImgSetTriggerConfig.restype = _int
    ImgSetTriggerConfig.argtypes = (_int, _P(IMGTRGCONFIG),)

    # 17 int ImgInputDI(int, unsigned short*);
    # -------------------
    ImgSetTriggerConfig = lib.ImgSetTriggerConfig
    ImgSetTriggerConfig.restype = _int
    ImgSetTriggerConfig.argtypes = (_int, _ushort_p,)

    # 18 int ImgOutputDO(int, unsigned short);
    # -------------------
    ImgOutputDO = lib.ImgOutputDO
    ImgOutputDO.restype = _int
    ImgOutputDO.argtypes = (_int, _ushort,)

    # 19 int ImgSetEventMask(int, PIMGEVENTTABLE);
    # -------------------
    ImgSetEventMask = lib.ImgSetEventMask
    ImgSetEventMask.restype = _int
    ImgSetEventMask.argtypes = (_int, _P(IMGEVENTTABLE),)

    # 20 int ImgGetEventMask(int, PIMGEVENTTABLE);
    # -------------------
    ImgGetEventMask = lib.ImgGetEventMask
    ImgGetEventMask.restype = _int
    ImgGetEventMask.argtypes = (_int, _P(IMGEVENTTABLE),)

    # 21 int ImgSetEvent(int, PLPIMGCALLBACK, unsigned long);
    # -------------------
    ImgSetEvent = lib.ImgSetEvent
    ImgSetEvent.restype = _int
    ImgSetEvent.argtypes = (_int, _P(LPIMGCALLBACK), _ulong,)

    # 22 int ImgSetEventEx(int, PLPIMGCALLBACK, unsigned long);
    # -------------------
    ImgSetEventEx = lib.ImgSetEventEx
    ImgSetEventEx.restype = _int
    ImgSetEventEx.argtypes = (_int, _P(LPIMGCALLBACK), _ulong,)

    # 23 int ImgKillEvent(int);
    # -------------------
    ImgSetEventEx = lib.ImgSetEventEx
    ImgSetEventEx.restype = _int
    ImgSetEventEx.argtypes = (_int,)

    # 24 int ImgSetChannel(int, unsigned long);
    # -------------------
    ImgSetChannel = lib.ImgSetChannel
    ImgSetChannel.restype = _int
    ImgSetChannel.argtypes = (_int, _ulong,)

    # 25 int ImgSetCaptureConfig(int, PIMGCAPCONFIG);
    # -------------------
    ImgSetCaptureConfig = lib.ImgSetCaptureConfig
    ImgSetCaptureConfig.restype = _int
    ImgSetCaptureConfig.argtypes = (_int, _P(IMGCAPCONFIG),)

    # 26 int ImgAllocateSDRAM(int, unsigned long, unsigned long, unsigned long, unsigned long, unsigned long*);
    # -------------------
    ImgAllocateSDRAM = lib.ImgAllocateSDRAM
    ImgAllocateSDRAM.restype = _int
    ImgAllocateSDRAM.argtypes = (_int, _ulong, _ulong, _ulong, _ulong, _ulong_p,)

    # 27 int ImgFreeSDRAM(int, unsigned long);
    # -------------------
    ImgFreeSDRAM = lib.ImgFreeSDRAM
    ImgFreeSDRAM.restype = _int
    ImgFreeSDRAM.argtypes = (_int, _ulong,)

    # 28 int ImgSetSDRAM(int, unsigned long);
    # -------------------
    ImgSetSDRAM = lib.ImgSetSDRAM
    ImgSetSDRAM.restype = _int
    ImgSetSDRAM.argtypes = (_int, _ulong,)

    # 29 int ImgReadCaptureData(int, unsigned long, unsigned long, unsigned long, void*, unsigned long);
    # -------------------
    ImgReadCaptureData = lib.ImgReadCaptureData
    ImgReadCaptureData.restype = _int
    ImgReadCaptureData.argtypes = (_int, _ulong, _ulong, _ulong, _void_p, _ulong,)

    # 30 int ImgBmCaptureData(int, unsigned long, unsigned long, unsigned long, unsigned long);
    # -------------------
    ImgBmCaptureData = lib.ImgReadCaptureData
    ImgBmCaptureData.restype = _int
    ImgBmCaptureData.argtypes = (_int, _ulong, _ulong, _ulong, _ulong,)

    # 31 int ImgWriteComparisonData(int, unsigned long, void*, unsigned long);
    # -------------------
    ImgWriteComparisonData = lib.ImgWriteComparisonData
    ImgWriteComparisonData.restype = _int
    ImgWriteComparisonData.argtypes = (_int, _ulong, _void_p, _ulong,)

    # 32 int ImgSetComparisonConfig(int, PIMGPTNCOFIG);
    # -------------------
    ImgSetComparisonConfig = lib.ImgSetComparisonConfig
    ImgSetComparisonConfig.restype = _int
    ImgSetComparisonConfig.argtypes = (_int, _P(IMGPTNCONFIG),)

    # 33 int ImgGetMachingLevel(int, unsigned long*, unsigned long*);
    # -------------------
    ImgGetMachingLevel = lib.ImgGetMachingLevel
    ImgGetMachingLevel.restype = _int
    ImgGetMachingLevel.argtypes = (_int, _ulong_p, _ulong_p,)

    # 34 int ImgClipData(void*, void*, unsigned long, PIMGCLIPCONFIG);
    # -------------------
    ImgGetMachingLevel = lib.ImgGetMachingLevel
    ImgGetMachingLevel.restype = _int
    ImgGetMachingLevel.argtypes = (_void_p, _void_p, _P(IMGCLIPCONFIG),)

    # 35 int ImgSetColorIngredient(int, unsigned long);
    # -------------------
    ImgSetColorIngredient = lib.ImgSetColorIngredient
    ImgSetColorIngredient.restype = _int
    ImgSetColorIngredient.argtypes = (_int, _ulong,)

    # 36 int ImgGetMeasurementValueEx(int, PIMGMEASURE, unsigned long*);
    # -------------------
    ImgGetMeasurementValueEx = lib.ImgGetMeasurementValueEx
    ImgGetMeasurementValueEx.restype = _int
    ImgGetMeasurementValueEx.argtypes = (_int, _P(IMGMEASURE), _unlong*,)

    # 37 int ImgSetConversionConfig(int, unsigned long);
    # -------------------
    ImgSetConversionConfig = lib.ImgSetConversionConfig
    ImgSetConversionConfig.restype = _int
    ImgSetConversionConfig.argtypes = (_int, _ulong,)

    # 38 int ImgSetLUT(int, PIMGLUTINFO);
    # -------------------
    ImgSetLUT = lib.ImgSetLUT
    ImgSetLUT.restype = _int
    ImgSetLUT.argtypes = (_int, _P(IMGLUTINFO),)

    # 39 int ImgSetFilter(int, unsigned long, PIMGFILTER);
    # -------------------
    ImgSetFilter = lib.ImgSetFilter
    ImgSetFilter.restype = _int
    ImgSetFilter.argtypes = (_int, _ulong, _P(IMGFILTER),)

    # 40 int ImgSetDil_Er(int, PIMGDILATE_ERODE);
    # -------------------
    ImgSetDil_Er = lib.ImgSetDil_Er
    ImgSetDil_Er.restype = _int
    ImgSetDil_Er.argtypes = (_int, _P(IMGDILATE_ERODE),)

    # 41 int ImgSetLabelingConfig(int, unsigned long);
    # -------------------
    ImgSetLabelingConfig = lib.ImgSetLabelingConfig
    ImgSetLabelingConfig.restype = _int
    ImgSetLabelingConfig.argtypes = (_int, _ulong,)

    # 42 int ImgGetMeasurementValueLBL(int, void*, unsigned long, unsigned long*, PIMGMEASURE);
    # -------------------
    ImgGetMeasurementValueLBL = lib.ImgGetMeasurementValueLBL
    ImgGetMeasurementValueLBL.restype = _int
    ImgGetMeasurementValueLBL.argtypes = (_int, _void_p, _ulong, _ulong_p, _P(IMGMEASURE),)

    # 43 int ImgSaveBitMapFile(char*, void*, unsigned long, long, long);
    # -------------------
    ImgSaveBitMapFile = lib.ImgSaveBitMapFile
    ImgSaveBitMapFile.restype = _int
    ImgSaveBitMapFile.argtypes = (_char_p, _void_p, _ulong, _long, _long,)

    # 44 int ImgSetDecoderConfig(int, unsigned long, unsigned long);
    # -------------------
    ImgSetDecoderConfig = lib.ImgSetDecoderConfig
    ImgSetDecoderConfig.restype = _int
    ImgSetDecoderConfig.argtypes = (_int, _ulong, _ulong,)

    # 45 int ImgSetEncoderConfig(int, unsigned short, unsigned short);
    # -------------------
    ImgSetEncoderConfig = lib.ImgSetEncoderConfig
    ImgSetEncoderConfig.restype = _int
    ImgSetEncoderConfig.argtypes = (_int, _ushort, _ushort,)

    # 46 int ImgSetGainControl(int, int);
    # -------------------
    ImgSetGainControl = lib.ImgSetGainControl
    ImgSetGainControl.restype = _int
    ImgSetGainControl.argtypes = (_int, _int,)

    # 47 int ImgSetBlankingLevel(int, int);
    # -------------------
    ImgSetBlankingLevel = lib.ImgSetBlankingLevel
    ImgSetBlankingLevel.restype = _int
    ImgSetBlankingLevel.argtypes = (_int, _int,)

    # 48 int ImgSetSyncErrorDetection(int, unsigned long);
    # -------------------
    ImgSetSyncErrorDetection = lib.ImgSetSyncErrorDetection
    ImgSetSyncErrorDetection.restype = _int
    ImgSetSyncErrorDetection.argtypes = (_int, _ulong,)

    # 49 int ImgGetCameraConnectionStatus(int, unsigned long*);
    # -------------------
    ImgGetCameraConnectionStatus = lib.ImgGetCameraConnectionStatus
    ImgGetCameraConnectionStatus.restype = _int
    ImgGetCameraConnectionStatus.argtypes = (_int, _ulong_p,)

    # 50 int ImgSetImposeImage(int, unsigned long, unsigned long, unsigned long, void*, unsigned long);
    # -------------------
    ImgSetImposeImage = lib.ImgSetImposeImage
    ImgSetImposeImage.restype = _int
    ImgSetImposeImage.argtypes = (_int, _ulong, _ulong, _ulong, _void_p, _ulong,)

    # 52 int ImgSetImposeDateTime(int, PIFIMGDATE, PIFIMGTIME);
    # -------------------
    ImgSetImposeDateTime = lib.ImgSetImposeDateTime
    ImgSetImposeDateTime.restype = _int
    ImgSetImposeDateTime.argtypes = (_int, _P(IFIMGDATE), _P(IFIMGTIME),)

    # 52 int ImgSetImposeDateTimeInfo(int, PIFIMGDATE, PIFIMGTIME, unsigned long, unsigned long*, unsigned long);
    # -------------------
    ImgSetImposeDateTimeInfo = lib.ImgSetImposeDateTimeInfo
    ImgSetImposeDateTimeInfo.restype = _int
    ImgSetImposeDateTimeInfo.argtypes = (_int, _P(IFIMGDATE), _P(IFIMGTIME), _ulong, _ulong*, _ulong,)
