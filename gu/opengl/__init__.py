from ._wrapper import (
    Byte, UByte, Short, UShort, Int, UInt, Long, ULong, Float, Double,
    VoidP, CharP, Size, Handle, GLSyncP
)

try:
    from ._library import *
except ModuleNotFoundError:
    from ._wrapper import wrapper
    wrapper()
    del wrapper
    from ._library import *

from ._shader import shader_program

del _library
del _wrapper
del _shader
