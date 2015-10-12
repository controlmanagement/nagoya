
import os
import ctypes
import pyinterface

#
# based on fbimtr.h (Version 1.01-01)
#

# ==========
# Structures
# ==========

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

class IMGCAPCONFIG(pyinterface.Structure):
    _fields_ = [('dwMode', ctypes.c_ulong),
                ('dwThinFrameCnt', ctypes.c_ulong),
                ('dwTimerCycle', ctypes.c_ulong),
                ('dwChFrameCnt', ctypes.c_ulong),
                ('dwChangePattern[5]', ctypes.c_ulong)]

class IMGPTNCONFIG(pyinterface.Structure):
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

class IMGLUTINFO(pyinterface.Structure):
    _fields_ = [('rgbBlue[256]', ctypes.c_ubyte),
                ('rgbGreen[256]', ctypes.c_ubyte),
                ('rgbRed[256]', ctypes.c_ubyte)
                ]

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
    _fields_ = [('sec', ctypes.c_int),
                ('min', ctypes.c_int),
                ('hour', ctypes.c_int)]

class IFIMGDATE(pyinterface.Structure):
    _fields_ = [('mday', ctypes.c_int),
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

# function pointer
# ----------------

PLPIMGCALLBACK = ctypes.CFUNCTYPE(IMGEVENTTABLE, ctypes.c_ulong, ctypes.c_ulong)
PLPIMGCALLBACKEX = ctypes.CFUNCTYPE(IMGEVENTTABLEEX, ctypes.c_ulong)


# ==========
# Identiferse
# ==========

# 5: ImgSetBuffer
# 26: ImgAllocateSDRAM
# 43: ImgSaveBitMapFile
# structure 10: IMGCLIPCONFIG
# =============
# ImgSetBuffer : BufferFormat
# ImgAllocateSDRAM : DataFormat
# ImgSaveBitMapFile : BufferFormat
# IMGCLIPCONFIG : dwDataFormat
# ------------------
IFIMG_COLOR_RGB32 = 0xc0000001
IFIMG_COLOR_RGB24 = 0xc0000002
IFIMG_COLOR_RGB15 = 0xc0000003
IFIMG_COLOR_GRAY8 = 0xc0000004
IFIMG_COLOR_RED8 = 0xc0000005
IFIMG_COLOR_GREEN8 = 0xc0000006
IFIMG_COLOR_BLUE8 = 0xc0000007
IFIMG_COLOR_BIN8 = 0xc0000008
IFIMG_COLOR_CMP8 = 0xc000000A
IFIMG_COLOR_RGB16 = 0xc000000B
IFIMG_COLOR_FIL8 = 0xc000000C
IFIMG_COLOR_LABEL8 = 0xc000000D
IFIMG_COLOR_RGB30 = 0xc000000E

IFIMG_RESOLUTION_640_480 = 0x00000000L
IFIMG_RESOLUTION_320_240 = 0x80000000L
IFIMG_RESOLUTION_160_120 = 0x40000000L

IFIMG_MEASUREMENT_HSIT = 0x00000200
IFIMG_MEASUREMENT_PRO = 0x00000700
IFIMG_MEASUREMENT_LBLCNT = 0x00000800
IFIMG_MEASUREMENT_AREA = 0x00001000
IFIMG_MEASUREMENT_GRV = 0x00002000
IFIMG_MEASUREMENT_FERE = 0x00004000
IFIMG_MEASUREMENT_ELLIPSE = 0x00008000
IFIMG_PIXEL_RGB = 0x00000000L
IFIMG_PIXEL_BGR = 0x01000000L

# 7: ImgStartCapture
# =============
# ImgStartCapture : StartMode
# ------------------
IFIMG_DMACAPTURE_START = 0x01
IFIMG_SDRAMCAPTURE_START = 0x02

# 8: ImgStopCapture
# =============
# ImgStopCapture : StopMode
# ------------------
IFIMG_FRAME_STOP = 0x01
IFIMG_IMMEDIATE_STOP = 0x02
IFIMG_SDRAM_FRAME_STOP = 0x04
IFIMG_SDRAM_IMMEDIATE_STOP = 0x08

# 10: ImgSetOutputMode
# =============
# ImgSetOutputMode : Mode
# ------------------
IFIMG_OUTMODE_THROUGH = 0x01
IFIMG_OUTMODE_COLORBAR = 0x02
IFIMG_OUTMODE_STILL_PICTURE = 0x03

# 24: ImgSetChannel
# structure 8: IMGCAPCONFIG
# =============
# ImgSetChannel : ChannelNum
# IMGCAPCONFIG : dwChangePattern
# ------------------
IFIMG_CHANNEL_CN1 = 0x01
IFIMG_CHANNEL_CN4 = 0x04
IFIMG_CHANNEL_CN5 = 0x05
IFIMG_CHANNEL_CN6 = 0x06
IFIMG_CHANNEL_CN7 = 0x07

# 30: ImgBmCaptureData
# =============
# ImgBmCaptureData : Position
# ------------------
IFIMG_BUFF_HEAD = 0x00
IFIMG_BUFF_CONTINUATION = 0x01

# 35: ImgSetColorIngredient
# structure 4: IMGBINCONFIG
# =============
# ImgSetColorIngredient : Ingredient
# IMGBINCONFIG : dwColorIngredient
# ------------------
IFIMG_INGREDIENT_RED = 0x01
IFIMG_INGREDIENT_GREEN = 0x02
IFIMG_INGREDIENT_BLUE = 0x03
IFIMG_INGREDIENT_GRAY = 0x04

# 39: ImgSetFilter
# =============
# ImgSetFilter : FilterSelect
# ------------------
IFIMG_SPATIAL_FILTER = 0x00000001
IFIMG_EDGE_FILTER = 0x00000002

# 41: ImgSetLabelingConfig
# =============
# ImgSetLabelingConfig : Connection
# ------------------
IFIMG_FOUR_CONNECTION = 0x00000000
IFIMG_EIGHT_CONNECTION = 0x00000001

# 48: ImgSetSyncErrorDetection
# =============
# ImgSetSyncErrorDetection : Mode
# ------------------
IFIMG_ERR_DETECTION_MODE1 = 0x00000001
IFIMG_ERR_DETECTION_MODE2 = 0x00000002
IFIMG_ERR_DETECTION_MODE3 = 0x00000003
IFIMG_ERR_DETECTION_MODE4 = 0x00000004
IFIMG_ERR_DETECTION_MODE5 = 0x00000005
IFIMG_ERR_DETECTION_MODE6 = 0x00000006
IFIMG_ERR_DETECTION_MODE7 = 0x00000007
IFIMG_ERR_DETECTION_MODE8 = 0x00000008

# 49: ImgGetCameraConnectionStatus
# =============
# ImgGetCameraConnectionStatus : Status
# ------------------
IFIMG_CAMERA_NOTSUPPORTED = 0x00000000
IFIMG_CAMERA_CONNECTION = 0x00000001
IFIMG_CAMERA_UNCONNECTION = 0x00000002

# 50: ImgSetImposeImage
# =============
# ImgSetImposeImage : SetMode
# ImgSetImposeImage : ImposeNum
# ------------------
IFIMG_SET_IMPOSE = 0x00000000
IFIMG_SELECT_IMPOSE = 0x00000001
IFIMG_NON_IMPOSE = 0x00000002
IFIMG_CHECK_SETINPOSE = 0x00000003
IFIMG_CHECK_SETINPOSE_STOP = 0x00000004

# ImgSetImposeImage : ImposeOperation
# ------------------
IFIMG_IMPOSE_REPLACE = 0x00000001
IFIMG_IMPOSE_ADD = 0x00000002
IFIMG_IMPOSE_SUB = 0x00000003
IFIMG_IMPOSE_XOR = 0x00000004
IFIMG_IMPOSE_OVERWRITE = 0x00000008
IFIMG_IMPOSE_PERMEATION_3_1 = 0x00000009
IFIMG_IMPOSE_PERMEATION = 0x0000000A
IFIMG_IMPOSE_PERMEATION_1_3 = 0x0000000B

# 52: ImgSetImposeDateTimeInfo
# =============
# ImgSetImposeDateTimeInfo : SetMode
# ------------------
IFIMG_IMPOSE_NONE_DATETIME = 0x00000000
IFIMG_IMPOSE_SET_DATE = 0x00000001
IFIMG_IMPOSE_SET_TIME = 0x00000002
IFIMG_IMPOSE_STRING_OUTLINE =0x00000003

# structure 4: IMGBINCONFIG
# =============
# IMGBINCONFIG : dwBinarzationMode
# ------------------
IFIMG_BINMODE_NORMAL = 0x01
IFIMG_BINMODE_REVERSAL = 0x02

# structure 8: IMGCAPCONFIG
# =============
# IMGCAPCONFIG : dwMode
# ------------------
IFIMG_CAPTURE_NORMAL = 0x01
IFIMG_CAPTURE_THINOUT = 0x02
IFIMG_CAPTURE_TIMER = 0x03
IFIMG_CAPTURE_CH_FRAME = 0x04
IFIMG_CAPTURE_CH_TIMER = 0x05

# structure 9: IMGPTNCONFIG
# =============
# IMGPTNCONFIG : dwAutoRevision
# ------------------
IFIMG_AUTO_ENABLE = 0x01
IFIMG_AUTO_DISABLE = 0x02

# IMGPTNCONFIG : dwTriggerMode
# ------------------
IFIMG_PTNMATCH_NORMAL = 0x01
IFIMG_PTNMATCH_REVERSAL = 0x02
IFIMG_PTNMATCH_NONE = 0x03


# ==========
# RETURN VALUE
# ========== 
IFIMG_ERROR_SUCCESS = 0
IFIMG_ERROR_NOT_DEVICE = 0xC0000001
IFIMG_ERROR_NOT_OPEN = 0xC0000002
IFIMG_ERROR_INVALID_DEVICE_NUMBER = 0xC0000003
IFIMG_ERROR_ALREADY_OPEN = 0xC0000004
IFIMG_ERROR_IO_PENDING = 0xC0000008
IFIMG_ERROR_INSUFFICIENT_BUFFER = 0xC0000007
IFIMG_ERROR_NOT_SUPPORTED = 0xC0000009
IFIMG_ERROR_INVALID_PARAMETER = 0xC0000010
IFIMG_ERROR_NOT_ALLOCATE_MEMORY = 0xC0000021
IFIMG_ERROR_NOW_CAPTURING = 0xC0001000
IFIMG_ERROR_NOW_STOP = 0xC0001001
IFIMG_ERROR_NULL_POINTER = 0xC0001002
IFIMG_ERROR_WRITE_FAILED = 0xC0001003
IFIMG_ERROR_READ_FAILED = 0xC0001004
IFIMG_ERROR_NOBUFFER = 0xC0001005
IFIMG_ERROR_INVALID_OFFSET = 0xC0001006
IFIMG_ERROR_SDRAM_NOW_CAPTURING = 0xC0001007
IFIMG_ERROR_SDRAM_NOW_STOP = 0xC0001008
IFIMG_ERROR_NOT_SET_COMPDATA = 0xC0001009
IFIMG_ERROR_SDRAM_NOTSET_CAPDATA = 0xC000100A
IFIMG_ERROR_NOT_COMPDATA = 0xC000100B
IFIMG_ERROR_INVALID_SDRAM_ID = 0xC000100C
IFIMG_ERROR_SDRAM_NOT_CAPDATA = 0xC000100D
IFIMG_ERROR_SDRAM_NOMEMORY = 0xC000100E
IFIMG_ERROR_INVALID_FORMAT = 0xC000100F
IFIMG_EROOR_NOW_SDRAM_BM = 0xC0001010
IFIMG_ERROR_NOW_IMPOSEDATA_WRITE = 0xC000101

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

    # 5 int ImgSetBuffer(int, PIMGBUFFERINFO unsigned long);
    # -------------------
    ImgSetBuffer = lib.ImgSetBuffer
    ImgSetBuffer.restype = _int
    ImgSetBuffer.argtypes = (_int, _P(IMGBUFFERINFO), _ulong)

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

    # 15 int ImgGetMeasurementValue(int, unsigned long*, unsigned long*, unsigned long*, unsigned long*,);
    # -------------------
    ImgGetMeasurementValue = lib.ImgGetMeasurementValue
    ImgGetMeasurementValue.restype = _int
    ImgGetMeasurementValue.argtypes = (_int, _ulong_p, _ulong_p, _ulong_p, _ulong_p,)

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
    ImgSetEvent.argtypes = (_int, PLPIMGCALLBACK, _ulong,)

    # 22 int ImgSetEventEx(int, PLPIMGCALLBACK, unsigned long);
    # -------------------
    ImgSetEventEx = lib.ImgSetEventEx
    ImgSetEventEx.restype = _int
    ImgSetEventEx.argtypes = (_int, PLPIMGCALLBACK, _ulong,)

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
    ImgGetMeasurementValueEx.argtypes = (_int, _P(IMGMEASURE), _ulong_p,)

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

    # 43 int ImgSaveBitmapFile(char*, void*, unsigned long, long, long);
    # -------------------
    ImgSaveBitmapFile = lib.ImgSaveBitmapFile
    ImgSaveBitmapFile.restype = _int
    ImgSaveBitmapFile.argtypes = (_char_p, _void_p, _ulong, _long, _long,)

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

    # 51 int ImgSetImposeDateTime(int, PIFIMGDATE, PIFIMGTIME);
    # -------------------
    ImgSetImposeDateTime = lib.ImgSetImposeDateTime
    ImgSetImposeDateTime.restype = _int
    ImgSetImposeDateTime.argtypes = (_int, _P(IFIMGDATE), _P(IFIMGTIME),)

    # 52 int ImgSetImposeDateTimeInfo(int, PIFIMGDATE, PIFIMGTIME, unsigned long, unsigned long*, unsigned long);
    # -------------------
    ImgSetImposeDateTimeInfo = lib.ImgSetImposeDateTimeInfo
    ImgSetImposeDateTimeInfo.restype = _int
    ImgSetImposeDateTimeInfo.argtypes = (_int, _P(IFIMGDATE), _P(IFIMGTIME), _ulong, _ulong_p, _ulong,)
