from .._wrapper import *

GL_VERSION_1_0 = 1
GL_DEPTH_BUFFER_BIT = 0x00000100
GL_STENCIL_BUFFER_BIT = 0x00000400
GL_COLOR_BUFFER_BIT = 0x00004000
GL_FALSE = 0
GL_TRUE = 1
GL_POINTS = 0x0000
GL_LINES = 0x0001
GL_LINE_LOOP = 0x0002
GL_LINE_STRIP = 0x0003
GL_TRIANGLES = 0x0004
GL_TRIANGLE_STRIP = 0x0005
GL_TRIANGLE_FAN = 0x0006
GL_QUADS = 0x0007
GL_NEVER = 0x0200
GL_LESS = 0x0201
GL_EQUAL = 0x0202
GL_LEQUAL = 0x0203
GL_GREATER = 0x0204
GL_NOTEQUAL = 0x0205
GL_GEQUAL = 0x0206
GL_ALWAYS = 0x0207
GL_ZERO = 0
GL_ONE = 1
GL_SRC_COLOR = 0x0300
GL_ONE_MINUS_SRC_COLOR = 0x0301
GL_SRC_ALPHA = 0x0302
GL_ONE_MINUS_SRC_ALPHA = 0x0303
GL_DST_ALPHA = 0x0304
GL_ONE_MINUS_DST_ALPHA = 0x0305
GL_DST_COLOR = 0x0306
GL_ONE_MINUS_DST_COLOR = 0x0307
GL_SRC_ALPHA_SATURATE = 0x0308
GL_NONE = 0
GL_FRONT_LEFT = 0x0400
GL_FRONT_RIGHT = 0x0401
GL_BACK_LEFT = 0x0402
GL_BACK_RIGHT = 0x0403
GL_FRONT = 0x0404
GL_BACK = 0x0405
GL_LEFT = 0x0406
GL_RIGHT = 0x0407
GL_FRONT_AND_BACK = 0x0408
GL_NO_ERROR = 0
GL_INVALID_ENUM = 0x0500
GL_INVALID_VALUE = 0x0501
GL_INVALID_OPERATION = 0x0502
GL_OUT_OF_MEMORY = 0x0505
GL_CW = 0x0900
GL_CCW = 0x0901
GL_POINT_SIZE = 0x0B11
GL_POINT_SIZE_RANGE = 0x0B12
GL_POINT_SIZE_GRANULARITY = 0x0B13
GL_LINE_SMOOTH = 0x0B20
GL_LINE_WIDTH = 0x0B21
GL_LINE_WIDTH_RANGE = 0x0B22
GL_LINE_WIDTH_GRANULARITY = 0x0B23
GL_POLYGON_MODE = 0x0B40
GL_POLYGON_SMOOTH = 0x0B41
GL_CULL_FACE = 0x0B44
GL_CULL_FACE_MODE = 0x0B45
GL_FRONT_FACE = 0x0B46
GL_DEPTH_RANGE = 0x0B70
GL_DEPTH_TEST = 0x0B71
GL_DEPTH_WRITEMASK = 0x0B72
GL_DEPTH_CLEAR_VALUE = 0x0B73
GL_DEPTH_FUNC = 0x0B74
GL_STENCIL_TEST = 0x0B90
GL_STENCIL_CLEAR_VALUE = 0x0B91
GL_STENCIL_FUNC = 0x0B92
GL_STENCIL_VALUE_MASK = 0x0B93
GL_STENCIL_FAIL = 0x0B94
GL_STENCIL_PASS_DEPTH_FAIL = 0x0B95
GL_STENCIL_PASS_DEPTH_PASS = 0x0B96
GL_STENCIL_REF = 0x0B97
GL_STENCIL_WRITEMASK = 0x0B98
GL_VIEWPORT = 0x0BA2
GL_DITHER = 0x0BD0
GL_BLEND_DST = 0x0BE0
GL_BLEND_SRC = 0x0BE1
GL_BLEND = 0x0BE2
GL_LOGIC_OP_MODE = 0x0BF0
GL_DRAW_BUFFER = 0x0C01
GL_READ_BUFFER = 0x0C02
GL_SCISSOR_BOX = 0x0C10
GL_SCISSOR_TEST = 0x0C11
GL_COLOR_CLEAR_VALUE = 0x0C22
GL_COLOR_WRITEMASK = 0x0C23
GL_DOUBLEBUFFER = 0x0C32
GL_STEREO = 0x0C33
GL_LINE_SMOOTH_HINT = 0x0C52
GL_POLYGON_SMOOTH_HINT = 0x0C53
GL_UNPACK_SWAP_BYTES = 0x0CF0
GL_UNPACK_LSB_FIRST = 0x0CF1
GL_UNPACK_ROW_LENGTH = 0x0CF2
GL_UNPACK_SKIP_ROWS = 0x0CF3
GL_UNPACK_SKIP_PIXELS = 0x0CF4
GL_UNPACK_ALIGNMENT = 0x0CF5
GL_PACK_SWAP_BYTES = 0x0D00
GL_PACK_LSB_FIRST = 0x0D01
GL_PACK_ROW_LENGTH = 0x0D02
GL_PACK_SKIP_ROWS = 0x0D03
GL_PACK_SKIP_PIXELS = 0x0D04
GL_PACK_ALIGNMENT = 0x0D05
GL_MAX_TEXTURE_SIZE = 0x0D33
GL_MAX_VIEWPORT_DIMS = 0x0D3A
GL_SUBPIXEL_BITS = 0x0D50
GL_TEXTURE_1D = 0x0DE0
GL_TEXTURE_2D = 0x0DE1
GL_TEXTURE_WIDTH = 0x1000
GL_TEXTURE_HEIGHT = 0x1001
GL_TEXTURE_BORDER_COLOR = 0x1004
GL_DONT_CARE = 0x1100
GL_FASTEST = 0x1101
GL_NICEST = 0x1102
GL_BYTE = 0x1400
GL_UNSIGNED_BYTE = 0x1401
GL_SHORT = 0x1402
GL_UNSIGNED_SHORT = 0x1403
GL_INT = 0x1404
GL_UNSIGNED_INT = 0x1405
GL_FLOAT = 0x1406
GL_STACK_OVERFLOW = 0x0503
GL_STACK_UNDERFLOW = 0x0504
GL_CLEAR = 0x1500
GL_AND = 0x1501
GL_AND_REVERSE = 0x1502
GL_COPY = 0x1503
GL_AND_INVERTED = 0x1504
GL_NOOP = 0x1505
GL_XOR = 0x1506
GL_OR = 0x1507
GL_NOR = 0x1508
GL_EQUIV = 0x1509
GL_INVERT = 0x150A
GL_OR_REVERSE = 0x150B
GL_COPY_INVERTED = 0x150C
GL_OR_INVERTED = 0x150D
GL_NAND = 0x150E
GL_SET = 0x150F
GL_TEXTURE = 0x1702
GL_COLOR = 0x1800
GL_DEPTH = 0x1801
GL_STENCIL = 0x1802
GL_STENCIL_INDEX = 0x1901
GL_DEPTH_COMPONENT = 0x1902
GL_RED = 0x1903
GL_GREEN = 0x1904
GL_BLUE = 0x1905
GL_ALPHA = 0x1906
GL_RGB = 0x1907
GL_RGBA = 0x1908
GL_POINT = 0x1B00
GL_LINE = 0x1B01
GL_FILL = 0x1B02
GL_KEEP = 0x1E00
GL_REPLACE = 0x1E01
GL_INCR = 0x1E02
GL_DECR = 0x1E03
GL_VENDOR = 0x1F00
GL_RENDERER = 0x1F01
GL_VERSION = 0x1F02
GL_EXTENSIONS = 0x1F03
GL_NEAREST = 0x2600
GL_LINEAR = 0x2601
GL_NEAREST_MIPMAP_NEAREST = 0x2700
GL_LINEAR_MIPMAP_NEAREST = 0x2701
GL_NEAREST_MIPMAP_LINEAR = 0x2702
GL_LINEAR_MIPMAP_LINEAR = 0x2703
GL_TEXTURE_MAG_FILTER = 0x2800
GL_TEXTURE_MIN_FILTER = 0x2801
GL_TEXTURE_WRAP_S = 0x2802
GL_TEXTURE_WRAP_T = 0x2803
GL_REPEAT = 0x2901
PFNGLCULLFACEPROC = C(None, UInt)
PFNGLFRONTFACEPROC = C(None, UInt)
PFNGLHINTPROC = C(None, UInt, UInt)
PFNGLLINEWIDTHPROC = C(None, Float)
PFNGLPOINTSIZEPROC = C(None, Float)
PFNGLPOLYGONMODEPROC = C(None, UInt, UInt)
PFNGLSCISSORPROC = C(None, Int, Int, Int, Int)
PFNGLTEXPARAMETERFPROC = C(None, UInt, UInt, Float)
PFNGLTEXPARAMETERFVPROC = C(None, UInt, UInt, P(Float))
PFNGLTEXPARAMETERIPROC = C(None, UInt, UInt, Int)
PFNGLTEXPARAMETERIVPROC = C(None, UInt, UInt, P(Int))
PFNGLTEXIMAGE1DPROC = C(None, UInt, Int, Int, Int, Int, UInt, UInt, VoidP)
PFNGLTEXIMAGE2DPROC = C(
    None, UInt, Int, Int, Int, Int, Int, UInt, UInt, VoidP
)
PFNGLDRAWBUFFERPROC = C(None, UInt)
PFNGLCLEARPROC = C(None, UInt)
PFNGLCLEARCOLORPROC = C(None, Float, Float, Float, Float)
PFNGLCLEARSTENCILPROC = C(None, Int)
PFNGLCLEARDEPTHPROC = C(None, Double)
PFNGLSTENCILMASKPROC = C(None, UInt)
PFNGLCOLORMASKPROC = C(None, UByte, UByte, UByte, UByte)
PFNGLDEPTHMASKPROC = C(None, UByte)
PFNGLDISABLEPROC = C(None, UInt)
PFNGLENABLEPROC = C(None, UInt)
PFNGLFINISHPROC = C(None)
PFNGLFLUSHPROC = C(None)
PFNGLBLENDFUNCPROC = C(None, UInt, UInt)
PFNGLLOGICOPPROC = C(None, UInt)
PFNGLSTENCILFUNCPROC = C(None, UInt, Int, UInt)
PFNGLSTENCILOPPROC = C(None, UInt, UInt, UInt)
PFNGLDEPTHFUNCPROC = C(None, UInt)
PFNGLPIXELSTOREFPROC = C(None, UInt, Float)
PFNGLPIXELSTOREIPROC = C(None, UInt, Int)
PFNGLREADBUFFERPROC = C(None, UInt)
PFNGLREADPIXELSPROC = C(None, Int, Int, Int, Int, UInt, UInt, VoidP)
PFNGLGETBOOLEANVPROC = C(None, UInt, P(UByte))
PFNGLGETDOUBLEVPROC = C(None, UInt, P(Double))
PFNGLGETERRORPROC = C(UInt)
PFNGLGETFLOATVPROC = C(None, UInt, P(Float))
PFNGLGETINTEGERVPROC = C(None, UInt, P(Int))
PFNGLGETSTRINGPROC = C(P(UByte), UInt)
PFNGLGETTEXIMAGEPROC = C(None, UInt, Int, UInt, UInt, VoidP)
PFNGLGETTEXPARAMETERFVPROC = C(None, UInt, UInt, P(Float))
PFNGLGETTEXPARAMETERIVPROC = C(None, UInt, UInt, P(Int))
PFNGLGETTEXLEVELPARAMETERFVPROC = C(None, UInt, Int, UInt, P(Float))
PFNGLGETTEXLEVELPARAMETERIVPROC = C(None, UInt, Int, UInt, P(Int))
PFNGLISENABLEDPROC = C(UByte, UInt)
PFNGLDEPTHRANGEPROC = C(None, Double, Double)
PFNGLVIEWPORTPROC = C(None, Int, Int, Int, Int)
glCullFace = GL('glCullFace', None, UInt)
glFrontFace = GL('glFrontFace', None, UInt)
glHint = GL('glHint', None, UInt, UInt)
glLineWidth = GL('glLineWidth', None, Float)
glPointSize = GL('glPointSize', None, Float)
glPolygonMode = GL('glPolygonMode', None, UInt, UInt)
glScissor = GL('glScissor', None, Int, Int, Int, Int)
glTexParameterf = GL('glTexParameterf', None, UInt, UInt, Float)
glTexParameterfv = GL('glTexParameterfv', None, UInt, UInt, P(Float))
glTexParameteri = GL('glTexParameteri', None, UInt, UInt, Int)
glTexParameteriv = GL('glTexParameteriv', None, UInt, UInt, P(Int))
glTexImage1D = GL(
    'glTexImage1D', None, UInt, Int, Int, Int, Int, UInt, UInt, VoidP
)
glTexImage2D = GL(
    'glTexImage2D', None, UInt, Int, Int, Int, Int, Int, UInt, UInt, VoidP
)
glDrawBuffer = GL('glDrawBuffer', None, UInt)
glClear = GL('glClear', None, UInt)
glClearColor = GL('glClearColor', None, Float, Float, Float, Float)
glClearStencil = GL('glClearStencil', None, Int)
glClearDepth = GL('glClearDepth', None, Double)
glStencilMask = GL('glStencilMask', None, UInt)
glColorMask = GL('glColorMask', None, UByte, UByte, UByte, UByte)
glDepthMask = GL('glDepthMask', None, UByte)
glDisable = GL('glDisable', None, UInt)
glEnable = GL('glEnable', None, UInt)
glFinish = GL('glFinish', None)
glFlush = GL('glFlush', None)
glBlendFunc = GL('glBlendFunc', None, UInt, UInt)
glLogicOp = GL('glLogicOp', None, UInt)
glStencilFunc = GL('glStencilFunc', None, UInt, Int, UInt)
glStencilOp = GL('glStencilOp', None, UInt, UInt, UInt)
glDepthFunc = GL('glDepthFunc', None, UInt)
glPixelStoref = GL('glPixelStoref', None, UInt, Float)
glPixelStorei = GL('glPixelStorei', None, UInt, Int)
glReadBuffer = GL('glReadBuffer', None, UInt)
glReadPixels = GL('glReadPixels', None, Int, Int, Int, Int, UInt, UInt, VoidP)
glGetBooleanv = GL('glGetBooleanv', None, UInt, P(UByte))
glGetDoublev = GL('glGetDoublev', None, UInt, P(Double))
glGetError = GL('glGetError', UInt)
glGetFloatv = GL('glGetFloatv', None, UInt, P(Float))
glGetIntegerv = GL('glGetIntegerv', None, UInt, P(Int))
glGetString = GL('glGetString', P(UByte), UInt)
glGetTexImage = GL('glGetTexImage', None, UInt, Int, UInt, UInt, VoidP)
glGetTexParameterfv = GL('glGetTexParameterfv', None, UInt, UInt, P(Float))
glGetTexParameteriv = GL('glGetTexParameteriv', None, UInt, UInt, P(Int))
glGetTexLevelParameterfv = GL(
    'glGetTexLevelParameterfv', None, UInt, Int, UInt, P(Float)
)
glGetTexLevelParameteriv = GL(
    'glGetTexLevelParameteriv', None, UInt, Int, UInt, P(Int)
)
glIsEnabled = GL('glIsEnabled', UByte, UInt)
glDepthRange = GL('glDepthRange', None, Double, Double)
glViewport = GL('glViewport', None, Int, Int, Int, Int)

__all__ = [
    'GL_VERSION_1_0', 'GL_DEPTH_BUFFER_BIT', 'GL_STENCIL_BUFFER_BIT',
    'GL_COLOR_BUFFER_BIT', 'GL_FALSE', 'GL_TRUE', 'GL_POINTS', 'GL_LINES',
    'GL_LINE_LOOP', 'GL_LINE_STRIP', 'GL_TRIANGLES', 'GL_TRIANGLE_STRIP',
    'GL_TRIANGLE_FAN', 'GL_QUADS', 'GL_NEVER', 'GL_LESS', 'GL_EQUAL',
    'GL_LEQUAL', 'GL_GREATER', 'GL_NOTEQUAL', 'GL_GEQUAL', 'GL_ALWAYS',
    'GL_ZERO', 'GL_ONE', 'GL_SRC_COLOR', 'GL_ONE_MINUS_SRC_COLOR',
    'GL_SRC_ALPHA', 'GL_ONE_MINUS_SRC_ALPHA', 'GL_DST_ALPHA',
    'GL_ONE_MINUS_DST_ALPHA', 'GL_DST_COLOR', 'GL_ONE_MINUS_DST_COLOR',
    'GL_SRC_ALPHA_SATURATE', 'GL_NONE', 'GL_FRONT_LEFT', 'GL_FRONT_RIGHT',
    'GL_BACK_LEFT', 'GL_BACK_RIGHT', 'GL_FRONT', 'GL_BACK', 'GL_LEFT',
    'GL_RIGHT', 'GL_FRONT_AND_BACK', 'GL_NO_ERROR', 'GL_INVALID_ENUM',
    'GL_INVALID_VALUE', 'GL_INVALID_OPERATION', 'GL_OUT_OF_MEMORY', 'GL_CW',
    'GL_CCW', 'GL_POINT_SIZE', 'GL_POINT_SIZE_RANGE',
    'GL_POINT_SIZE_GRANULARITY', 'GL_LINE_SMOOTH', 'GL_LINE_WIDTH',
    'GL_LINE_WIDTH_RANGE', 'GL_LINE_WIDTH_GRANULARITY', 'GL_POLYGON_MODE',
    'GL_POLYGON_SMOOTH', 'GL_CULL_FACE', 'GL_CULL_FACE_MODE', 'GL_FRONT_FACE',
    'GL_DEPTH_RANGE', 'GL_DEPTH_TEST', 'GL_DEPTH_WRITEMASK',
    'GL_DEPTH_CLEAR_VALUE', 'GL_DEPTH_FUNC', 'GL_STENCIL_TEST',
    'GL_STENCIL_CLEAR_VALUE', 'GL_STENCIL_FUNC', 'GL_STENCIL_VALUE_MASK',
    'GL_STENCIL_FAIL', 'GL_STENCIL_PASS_DEPTH_FAIL',
    'GL_STENCIL_PASS_DEPTH_PASS', 'GL_STENCIL_REF', 'GL_STENCIL_WRITEMASK',
    'GL_VIEWPORT', 'GL_DITHER', 'GL_BLEND_DST', 'GL_BLEND_SRC', 'GL_BLEND',
    'GL_LOGIC_OP_MODE', 'GL_DRAW_BUFFER', 'GL_READ_BUFFER', 'GL_SCISSOR_BOX',
    'GL_SCISSOR_TEST', 'GL_COLOR_CLEAR_VALUE', 'GL_COLOR_WRITEMASK',
    'GL_DOUBLEBUFFER', 'GL_STEREO', 'GL_LINE_SMOOTH_HINT',
    'GL_POLYGON_SMOOTH_HINT', 'GL_UNPACK_SWAP_BYTES', 'GL_UNPACK_LSB_FIRST',
    'GL_UNPACK_ROW_LENGTH', 'GL_UNPACK_SKIP_ROWS', 'GL_UNPACK_SKIP_PIXELS',
    'GL_UNPACK_ALIGNMENT', 'GL_PACK_SWAP_BYTES', 'GL_PACK_LSB_FIRST',
    'GL_PACK_ROW_LENGTH', 'GL_PACK_SKIP_ROWS', 'GL_PACK_SKIP_PIXELS',
    'GL_PACK_ALIGNMENT', 'GL_MAX_TEXTURE_SIZE', 'GL_MAX_VIEWPORT_DIMS',
    'GL_SUBPIXEL_BITS', 'GL_TEXTURE_1D', 'GL_TEXTURE_2D', 'GL_TEXTURE_WIDTH',
    'GL_TEXTURE_HEIGHT', 'GL_TEXTURE_BORDER_COLOR', 'GL_DONT_CARE',
    'GL_FASTEST', 'GL_NICEST', 'GL_BYTE', 'GL_UNSIGNED_BYTE', 'GL_SHORT',
    'GL_UNSIGNED_SHORT', 'GL_INT', 'GL_UNSIGNED_INT', 'GL_FLOAT',
    'GL_STACK_OVERFLOW', 'GL_STACK_UNDERFLOW', 'GL_CLEAR', 'GL_AND',
    'GL_AND_REVERSE', 'GL_COPY', 'GL_AND_INVERTED', 'GL_NOOP', 'GL_XOR',
    'GL_OR', 'GL_NOR', 'GL_EQUIV', 'GL_INVERT', 'GL_OR_REVERSE',
    'GL_COPY_INVERTED', 'GL_OR_INVERTED', 'GL_NAND', 'GL_SET', 'GL_TEXTURE',
    'GL_COLOR', 'GL_DEPTH', 'GL_STENCIL', 'GL_STENCIL_INDEX',
    'GL_DEPTH_COMPONENT', 'GL_RED', 'GL_GREEN', 'GL_BLUE', 'GL_ALPHA',
    'GL_RGB', 'GL_RGBA', 'GL_POINT', 'GL_LINE', 'GL_FILL', 'GL_KEEP',
    'GL_REPLACE', 'GL_INCR', 'GL_DECR', 'GL_VENDOR', 'GL_RENDERER',
    'GL_VERSION', 'GL_EXTENSIONS', 'GL_NEAREST', 'GL_LINEAR',
    'GL_NEAREST_MIPMAP_NEAREST', 'GL_LINEAR_MIPMAP_NEAREST',
    'GL_NEAREST_MIPMAP_LINEAR', 'GL_LINEAR_MIPMAP_LINEAR',
    'GL_TEXTURE_MAG_FILTER', 'GL_TEXTURE_MIN_FILTER', 'GL_TEXTURE_WRAP_S',
    'GL_TEXTURE_WRAP_T', 'GL_REPEAT', 'PFNGLCULLFACEPROC',
    'PFNGLFRONTFACEPROC', 'PFNGLHINTPROC', 'PFNGLLINEWIDTHPROC',
    'PFNGLPOINTSIZEPROC', 'PFNGLPOLYGONMODEPROC', 'PFNGLSCISSORPROC',
    'PFNGLTEXPARAMETERFPROC', 'PFNGLTEXPARAMETERFVPROC',
    'PFNGLTEXPARAMETERIPROC', 'PFNGLTEXPARAMETERIVPROC',
    'PFNGLTEXIMAGE1DPROC', 'PFNGLTEXIMAGE2DPROC', 'PFNGLDRAWBUFFERPROC',
    'PFNGLCLEARPROC', 'PFNGLCLEARCOLORPROC', 'PFNGLCLEARSTENCILPROC',
    'PFNGLCLEARDEPTHPROC', 'PFNGLSTENCILMASKPROC', 'PFNGLCOLORMASKPROC',
    'PFNGLDEPTHMASKPROC', 'PFNGLDISABLEPROC', 'PFNGLENABLEPROC',
    'PFNGLFINISHPROC', 'PFNGLFLUSHPROC', 'PFNGLBLENDFUNCPROC',
    'PFNGLLOGICOPPROC', 'PFNGLSTENCILFUNCPROC', 'PFNGLSTENCILOPPROC',
    'PFNGLDEPTHFUNCPROC', 'PFNGLPIXELSTOREFPROC', 'PFNGLPIXELSTOREIPROC',
    'PFNGLREADBUFFERPROC', 'PFNGLREADPIXELSPROC', 'PFNGLGETBOOLEANVPROC',
    'PFNGLGETDOUBLEVPROC', 'PFNGLGETERRORPROC', 'PFNGLGETFLOATVPROC',
    'PFNGLGETINTEGERVPROC', 'PFNGLGETSTRINGPROC', 'PFNGLGETTEXIMAGEPROC',
    'PFNGLGETTEXPARAMETERFVPROC', 'PFNGLGETTEXPARAMETERIVPROC',
    'PFNGLGETTEXLEVELPARAMETERFVPROC', 'PFNGLGETTEXLEVELPARAMETERIVPROC',
    'PFNGLISENABLEDPROC', 'PFNGLDEPTHRANGEPROC', 'PFNGLVIEWPORTPROC',
    'glCullFace', 'glFrontFace', 'glHint', 'glLineWidth', 'glPointSize',
    'glPolygonMode', 'glScissor', 'glTexParameterf', 'glTexParameterfv',
    'glTexParameteri', 'glTexParameteriv', 'glTexImage1D', 'glTexImage2D',
    'glDrawBuffer', 'glClear', 'glClearColor', 'glClearStencil',
    'glClearDepth', 'glStencilMask', 'glColorMask', 'glDepthMask',
    'glDisable', 'glEnable', 'glFinish', 'glFlush', 'glBlendFunc',
    'glLogicOp', 'glStencilFunc', 'glStencilOp', 'glDepthFunc',
    'glPixelStoref', 'glPixelStorei', 'glReadBuffer', 'glReadPixels',
    'glGetBooleanv', 'glGetDoublev', 'glGetError', 'glGetFloatv',
    'glGetIntegerv', 'glGetString', 'glGetTexImage', 'glGetTexParameterfv',
    'glGetTexParameteriv', 'glGetTexLevelParameterfv',
    'glGetTexLevelParameteriv', 'glIsEnabled', 'glDepthRange', 'glViewport'
]
