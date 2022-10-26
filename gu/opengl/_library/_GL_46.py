from .._wrapper import *

GL_VERSION_4_6 = 1
GL_SHADER_BINARY_FORMAT_SPIR_V = 0x9551
GL_SPIR_V_BINARY = 0x9552
GL_PARAMETER_BUFFER = 0x80EE
GL_PARAMETER_BUFFER_BINDING = 0x80EF
GL_CONTEXT_FLAG_NO_ERROR_BIT = 0x00000008
GL_VERTICES_SUBMITTED = 0x82EE
GL_PRIMITIVES_SUBMITTED = 0x82EF
GL_VERTEX_SHADER_INVOCATIONS = 0x82F0
GL_TESS_CONTROL_SHADER_PATCHES = 0x82F1
GL_TESS_EVALUATION_SHADER_INVOCATIONS = 0x82F2
GL_GEOMETRY_SHADER_PRIMITIVES_EMITTED = 0x82F3
GL_FRAGMENT_SHADER_INVOCATIONS = 0x82F4
GL_COMPUTE_SHADER_INVOCATIONS = 0x82F5
GL_CLIPPING_INPUT_PRIMITIVES = 0x82F6
GL_CLIPPING_OUTPUT_PRIMITIVES = 0x82F7
GL_POLYGON_OFFSET_CLAMP = 0x8E1B
GL_SPIR_V_EXTENSIONS = 0x9553
GL_NUM_SPIR_V_EXTENSIONS = 0x9554
GL_TEXTURE_MAX_ANISOTROPY = 0x84FE
GL_MAX_TEXTURE_MAX_ANISOTROPY = 0x84FF
GL_TRANSFORM_FEEDBACK_OVERFLOW = 0x82EC
GL_TRANSFORM_FEEDBACK_STREAM_OVERFLOW = 0x82ED
PFNGLSPECIALIZESHADERPROC = C(None, UInt, CharP, UInt, P(UInt), P(UInt))
PFNGLMULTIDRAWARRAYSINDIRECTCOUNTPROC = C(None, UInt, VoidP, Size, Int, Int)
PFNGLMULTIDRAWELEMENTSINDIRECTCOUNTPROC = C(
    None, UInt, UInt, VoidP, Size, Int, Int
)
PFNGLPOLYGONOFFSETCLAMPPROC = C(None, Float, Float, Float)
glSpecializeShader = GL(
    'glSpecializeShader', None, UInt, CharP, UInt, P(UInt), P(UInt)
)
glMultiDrawArraysIndirectCount = GL(
    'glMultiDrawArraysIndirectCount', None, UInt, VoidP, Size, Int, Int
)
glMultiDrawElementsIndirectCount = GL(
    'glMultiDrawElementsIndirectCount', None, UInt, UInt, VoidP, Size, Int,
    Int
)
glPolygonOffsetClamp = GL('glPolygonOffsetClamp', None, Float, Float, Float)

__all__ = [
    'GL_VERSION_4_6', 'GL_SHADER_BINARY_FORMAT_SPIR_V', 'GL_SPIR_V_BINARY',
    'GL_PARAMETER_BUFFER', 'GL_PARAMETER_BUFFER_BINDING',
    'GL_CONTEXT_FLAG_NO_ERROR_BIT', 'GL_VERTICES_SUBMITTED',
    'GL_PRIMITIVES_SUBMITTED', 'GL_VERTEX_SHADER_INVOCATIONS',
    'GL_TESS_CONTROL_SHADER_PATCHES', 'GL_TESS_EVALUATION_SHADER_INVOCATIONS',
    'GL_GEOMETRY_SHADER_PRIMITIVES_EMITTED', 'GL_FRAGMENT_SHADER_INVOCATIONS',
    'GL_COMPUTE_SHADER_INVOCATIONS', 'GL_CLIPPING_INPUT_PRIMITIVES',
    'GL_CLIPPING_OUTPUT_PRIMITIVES', 'GL_POLYGON_OFFSET_CLAMP',
    'GL_SPIR_V_EXTENSIONS', 'GL_NUM_SPIR_V_EXTENSIONS',
    'GL_TEXTURE_MAX_ANISOTROPY', 'GL_MAX_TEXTURE_MAX_ANISOTROPY',
    'GL_TRANSFORM_FEEDBACK_OVERFLOW', 'GL_TRANSFORM_FEEDBACK_STREAM_OVERFLOW',
    'PFNGLSPECIALIZESHADERPROC', 'PFNGLMULTIDRAWARRAYSINDIRECTCOUNTPROC',
    'PFNGLMULTIDRAWELEMENTSINDIRECTCOUNTPROC', 'PFNGLPOLYGONOFFSETCLAMPPROC',
    'glSpecializeShader', 'glMultiDrawArraysIndirectCount',
    'glMultiDrawElementsIndirectCount', 'glPolygonOffsetClamp'
]
