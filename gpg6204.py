
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
