from .._wrapper import *

GL_VERSION_3_3 = 1
GL_VERTEX_ATTRIB_ARRAY_DIVISOR = 0x88FE
GL_SRC1_COLOR = 0x88F9
GL_ONE_MINUS_SRC1_COLOR = 0x88FA
GL_ONE_MINUS_SRC1_ALPHA = 0x88FB
GL_MAX_DUAL_SOURCE_DRAW_BUFFERS = 0x88FC
GL_ANY_SAMPLES_PASSED = 0x8C2F
GL_SAMPLER_BINDING = 0x8919
GL_RGB10_A2UI = 0x906F
GL_TEXTURE_SWIZZLE_R = 0x8E42
GL_TEXTURE_SWIZZLE_G = 0x8E43
GL_TEXTURE_SWIZZLE_B = 0x8E44
GL_TEXTURE_SWIZZLE_A = 0x8E45
GL_TEXTURE_SWIZZLE_RGBA = 0x8E46
GL_TIME_ELAPSED = 0x88BF
GL_TIMESTAMP = 0x8E28
GL_INT_2_10_10_10_REV = 0x8D9F
PFNGLBINDFRAGDATALOCATIONINDEXEDPROC = C(None, UInt, UInt, UInt, CharP)
PFNGLGETFRAGDATAINDEXPROC = C(Int, UInt, CharP)
PFNGLGENSAMPLERSPROC = C(None, Int, P(UInt))
PFNGLDELETESAMPLERSPROC = C(None, Int, P(UInt))
PFNGLISSAMPLERPROC = C(UByte, UInt)
PFNGLBINDSAMPLERPROC = C(None, UInt, UInt)
PFNGLSAMPLERPARAMETERIPROC = C(None, UInt, UInt, Int)
PFNGLSAMPLERPARAMETERIVPROC = C(None, UInt, UInt, P(Int))
PFNGLSAMPLERPARAMETERFPROC = C(None, UInt, UInt, Float)
PFNGLSAMPLERPARAMETERFVPROC = C(None, UInt, UInt, P(Float))
PFNGLSAMPLERPARAMETERIIVPROC = C(None, UInt, UInt, P(Int))
PFNGLSAMPLERPARAMETERIUIVPROC = C(None, UInt, UInt, P(UInt))
PFNGLGETSAMPLERPARAMETERIVPROC = C(None, UInt, UInt, P(Int))
PFNGLGETSAMPLERPARAMETERIIVPROC = C(None, UInt, UInt, P(Int))
PFNGLGETSAMPLERPARAMETERFVPROC = C(None, UInt, UInt, P(Float))
PFNGLGETSAMPLERPARAMETERIUIVPROC = C(None, UInt, UInt, P(UInt))
PFNGLQUERYCOUNTERPROC = C(None, UInt, UInt)
PFNGLGETQUERYOBJECTI64VPROC = C(None, UInt, UInt, P(Long))
PFNGLGETQUERYOBJECTUI64VPROC = C(None, UInt, UInt, P(ULong))
PFNGLVERTEXATTRIBDIVISORPROC = C(None, UInt, UInt)
PFNGLVERTEXATTRIBP1UIPROC = C(None, UInt, UInt, UByte, UInt)
PFNGLVERTEXATTRIBP1UIVPROC = C(None, UInt, UInt, UByte, P(UInt))
PFNGLVERTEXATTRIBP2UIPROC = C(None, UInt, UInt, UByte, UInt)
PFNGLVERTEXATTRIBP2UIVPROC = C(None, UInt, UInt, UByte, P(UInt))
PFNGLVERTEXATTRIBP3UIPROC = C(None, UInt, UInt, UByte, UInt)
PFNGLVERTEXATTRIBP3UIVPROC = C(None, UInt, UInt, UByte, P(UInt))
PFNGLVERTEXATTRIBP4UIPROC = C(None, UInt, UInt, UByte, UInt)
PFNGLVERTEXATTRIBP4UIVPROC = C(None, UInt, UInt, UByte, P(UInt))
glBindFragDataLocationIndexed = GL(
    'glBindFragDataLocationIndexed', None, UInt, UInt, UInt, CharP
)
glGetFragDataIndex = GL('glGetFragDataIndex', Int, UInt, CharP)
glGenSamplers = GL('glGenSamplers', None, Int, P(UInt))
glDeleteSamplers = GL('glDeleteSamplers', None, Int, P(UInt))
glIsSampler = GL('glIsSampler', UByte, UInt)
glBindSampler = GL('glBindSampler', None, UInt, UInt)
glSamplerParameteri = GL('glSamplerParameteri', None, UInt, UInt, Int)
glSamplerParameteriv = GL('glSamplerParameteriv', None, UInt, UInt, P(Int))
glSamplerParameterf = GL('glSamplerParameterf', None, UInt, UInt, Float)
glSamplerParameterfv = GL('glSamplerParameterfv', None, UInt, UInt, P(Float))
glSamplerParameterIiv = GL('glSamplerParameterIiv', None, UInt, UInt, P(Int))
glSamplerParameterIuiv = GL(
    'glSamplerParameterIuiv', None, UInt, UInt, P(UInt)
)
glGetSamplerParameteriv = GL(
    'glGetSamplerParameteriv', None, UInt, UInt, P(Int)
)
glGetSamplerParameterIiv = GL(
    'glGetSamplerParameterIiv', None, UInt, UInt, P(Int)
)
glGetSamplerParameterfv = GL(
    'glGetSamplerParameterfv', None, UInt, UInt, P(Float)
)
glGetSamplerParameterIuiv = GL(
    'glGetSamplerParameterIuiv', None, UInt, UInt, P(UInt)
)
glQueryCounter = GL('glQueryCounter', None, UInt, UInt)
glGetQueryObjecti64v = GL('glGetQueryObjecti64v', None, UInt, UInt, P(Long))
glGetQueryObjectui64v = GL(
    'glGetQueryObjectui64v', None, UInt, UInt, P(ULong)
)
glVertexAttribDivisor = GL('glVertexAttribDivisor', None, UInt, UInt)
glVertexAttribP1ui = GL('glVertexAttribP1ui', None, UInt, UInt, UByte, UInt)
glVertexAttribP1uiv = GL(
    'glVertexAttribP1uiv', None, UInt, UInt, UByte, P(UInt)
)
glVertexAttribP2ui = GL('glVertexAttribP2ui', None, UInt, UInt, UByte, UInt)
glVertexAttribP2uiv = GL(
    'glVertexAttribP2uiv', None, UInt, UInt, UByte, P(UInt)
)
glVertexAttribP3ui = GL('glVertexAttribP3ui', None, UInt, UInt, UByte, UInt)
glVertexAttribP3uiv = GL(
    'glVertexAttribP3uiv', None, UInt, UInt, UByte, P(UInt)
)
glVertexAttribP4ui = GL('glVertexAttribP4ui', None, UInt, UInt, UByte, UInt)
glVertexAttribP4uiv = GL(
    'glVertexAttribP4uiv', None, UInt, UInt, UByte, P(UInt)
)

__all__ = [
    'GL_VERSION_3_3', 'GL_VERTEX_ATTRIB_ARRAY_DIVISOR', 'GL_SRC1_COLOR',
    'GL_ONE_MINUS_SRC1_COLOR', 'GL_ONE_MINUS_SRC1_ALPHA',
    'GL_MAX_DUAL_SOURCE_DRAW_BUFFERS', 'GL_ANY_SAMPLES_PASSED',
    'GL_SAMPLER_BINDING', 'GL_RGB10_A2UI', 'GL_TEXTURE_SWIZZLE_R',
    'GL_TEXTURE_SWIZZLE_G', 'GL_TEXTURE_SWIZZLE_B', 'GL_TEXTURE_SWIZZLE_A',
    'GL_TEXTURE_SWIZZLE_RGBA', 'GL_TIME_ELAPSED', 'GL_TIMESTAMP',
    'GL_INT_2_10_10_10_REV', 'PFNGLBINDFRAGDATALOCATIONINDEXEDPROC',
    'PFNGLGETFRAGDATAINDEXPROC', 'PFNGLGENSAMPLERSPROC',
    'PFNGLDELETESAMPLERSPROC', 'PFNGLISSAMPLERPROC', 'PFNGLBINDSAMPLERPROC',
    'PFNGLSAMPLERPARAMETERIPROC', 'PFNGLSAMPLERPARAMETERIVPROC',
    'PFNGLSAMPLERPARAMETERFPROC', 'PFNGLSAMPLERPARAMETERFVPROC',
    'PFNGLSAMPLERPARAMETERIIVPROC', 'PFNGLSAMPLERPARAMETERIUIVPROC',
    'PFNGLGETSAMPLERPARAMETERIVPROC', 'PFNGLGETSAMPLERPARAMETERIIVPROC',
    'PFNGLGETSAMPLERPARAMETERFVPROC', 'PFNGLGETSAMPLERPARAMETERIUIVPROC',
    'PFNGLQUERYCOUNTERPROC', 'PFNGLGETQUERYOBJECTI64VPROC',
    'PFNGLGETQUERYOBJECTUI64VPROC', 'PFNGLVERTEXATTRIBDIVISORPROC',
    'PFNGLVERTEXATTRIBP1UIPROC', 'PFNGLVERTEXATTRIBP1UIVPROC',
    'PFNGLVERTEXATTRIBP2UIPROC', 'PFNGLVERTEXATTRIBP2UIVPROC',
    'PFNGLVERTEXATTRIBP3UIPROC', 'PFNGLVERTEXATTRIBP3UIVPROC',
    'PFNGLVERTEXATTRIBP4UIPROC', 'PFNGLVERTEXATTRIBP4UIVPROC',
    'glBindFragDataLocationIndexed', 'glGetFragDataIndex', 'glGenSamplers',
    'glDeleteSamplers', 'glIsSampler', 'glBindSampler', 'glSamplerParameteri',
    'glSamplerParameteriv', 'glSamplerParameterf', 'glSamplerParameterfv',
    'glSamplerParameterIiv', 'glSamplerParameterIuiv',
    'glGetSamplerParameteriv', 'glGetSamplerParameterIiv',
    'glGetSamplerParameterfv', 'glGetSamplerParameterIuiv', 'glQueryCounter',
    'glGetQueryObjecti64v', 'glGetQueryObjectui64v', 'glVertexAttribDivisor',
    'glVertexAttribP1ui', 'glVertexAttribP1uiv', 'glVertexAttribP2ui',
    'glVertexAttribP2uiv', 'glVertexAttribP3ui', 'glVertexAttribP3uiv',
    'glVertexAttribP4ui', 'glVertexAttribP4uiv'
]
