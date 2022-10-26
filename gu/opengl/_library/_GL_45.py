from .._wrapper import *

GL_VERSION_4_5 = 1
GL_CONTEXT_LOST = 0x0507
GL_NEGATIVE_ONE_TO_ONE = 0x935E
GL_ZERO_TO_ONE = 0x935F
GL_CLIP_ORIGIN = 0x935C
GL_CLIP_DEPTH_MODE = 0x935D
GL_QUERY_WAIT_INVERTED = 0x8E17
GL_QUERY_NO_WAIT_INVERTED = 0x8E18
GL_QUERY_BY_REGION_WAIT_INVERTED = 0x8E19
GL_QUERY_BY_REGION_NO_WAIT_INVERTED = 0x8E1A
GL_MAX_CULL_DISTANCES = 0x82F9
GL_MAX_COMBINED_CLIP_AND_CULL_DISTANCES = 0x82FA
GL_TEXTURE_TARGET = 0x1006
GL_QUERY_TARGET = 0x82EA
GL_GUILTY_CONTEXT_RESET = 0x8253
GL_INNOCENT_CONTEXT_RESET = 0x8254
GL_UNKNOWN_CONTEXT_RESET = 0x8255
GL_RESET_NOTIFICATION_STRATEGY = 0x8256
GL_LOSE_CONTEXT_ON_RESET = 0x8252
GL_NO_RESET_NOTIFICATION = 0x8261
GL_CONTEXT_FLAG_ROBUST_ACCESS_BIT = 0x00000004
GL_CONTEXT_RELEASE_BEHAVIOR = 0x82FB
GL_CONTEXT_RELEASE_BEHAVIOR_FLUSH = 0x82FC
PFNGLCLIPCONTROLPROC = C(None, UInt, UInt)
PFNGLCREATETRANSFORMFEEDBACKSPROC = C(None, Int, P(UInt))
PFNGLTRANSFORMFEEDBACKBUFFERBASEPROC = C(None, UInt, UInt, UInt)
PFNGLTRANSFORMFEEDBACKBUFFERRANGEPROC = C(None, UInt, UInt, UInt, Size, Size)
PFNGLGETTRANSFORMFEEDBACKIVPROC = C(None, UInt, UInt, P(Int))
PFNGLGETTRANSFORMFEEDBACKI_VPROC = C(None, UInt, UInt, UInt, P(Int))
PFNGLGETTRANSFORMFEEDBACKI64_VPROC = C(None, UInt, UInt, UInt, P(Long))
PFNGLCREATEBUFFERSPROC = C(None, Int, P(UInt))
PFNGLNAMEDBUFFERSTORAGEPROC = C(None, UInt, Size, VoidP, UInt)
PFNGLNAMEDBUFFERDATAPROC = C(None, UInt, Size, VoidP, UInt)
PFNGLNAMEDBUFFERSUBDATAPROC = C(None, UInt, Size, Size, VoidP)
PFNGLCOPYNAMEDBUFFERSUBDATAPROC = C(None, UInt, UInt, Size, Size, Size)
PFNGLCLEARNAMEDBUFFERDATAPROC = C(None, UInt, UInt, UInt, UInt, VoidP)
PFNGLCLEARNAMEDBUFFERSUBDATAPROC = C(
    None, UInt, UInt, Size, Size, UInt, UInt, VoidP
)
PFNGLMAPNAMEDBUFFERPROC = C(VoidP, UInt, UInt)
PFNGLMAPNAMEDBUFFERRANGEPROC = C(VoidP, UInt, Size, Size, UInt)
PFNGLUNMAPNAMEDBUFFERPROC = C(UByte, UInt)
PFNGLFLUSHMAPPEDNAMEDBUFFERRANGEPROC = C(None, UInt, Size, Size)
PFNGLGETNAMEDBUFFERPARAMETERIVPROC = C(None, UInt, UInt, P(Int))
PFNGLGETNAMEDBUFFERPARAMETERI64VPROC = C(None, UInt, UInt, P(Long))
PFNGLGETNAMEDBUFFERPOINTERVPROC = C(None, UInt, UInt, P(VoidP))
PFNGLGETNAMEDBUFFERSUBDATAPROC = C(None, UInt, Size, Size, VoidP)
PFNGLCREATEFRAMEBUFFERSPROC = C(None, Int, P(UInt))
PFNGLNAMEDFRAMEBUFFERRENDERBUFFERPROC = C(None, UInt, UInt, UInt, UInt)
PFNGLNAMEDFRAMEBUFFERPARAMETERIPROC = C(None, UInt, UInt, Int)
PFNGLNAMEDFRAMEBUFFERTEXTUREPROC = C(None, UInt, UInt, UInt, Int)
PFNGLNAMEDFRAMEBUFFERTEXTURELAYERPROC = C(None, UInt, UInt, UInt, Int, Int)
PFNGLNAMEDFRAMEBUFFERDRAWBUFFERPROC = C(None, UInt, UInt)
PFNGLNAMEDFRAMEBUFFERDRAWBUFFERSPROC = C(None, UInt, Int, P(UInt))
PFNGLNAMEDFRAMEBUFFERREADBUFFERPROC = C(None, UInt, UInt)
PFNGLINVALIDATENAMEDFRAMEBUFFERDATAPROC = C(None, UInt, Int, P(UInt))
PFNGLINVALIDATENAMEDFRAMEBUFFERSUBDATAPROC = C(
    None, UInt, Int, P(UInt), Int, Int, Int, Int
)
PFNGLCLEARNAMEDFRAMEBUFFERIVPROC = C(None, UInt, UInt, Int, P(Int))
PFNGLCLEARNAMEDFRAMEBUFFERUIVPROC = C(None, UInt, UInt, Int, P(UInt))
PFNGLCLEARNAMEDFRAMEBUFFERFVPROC = C(None, UInt, UInt, Int, P(Float))
PFNGLCLEARNAMEDFRAMEBUFFERFIPROC = C(None, UInt, UInt, Int, Float, Int)
PFNGLBLITNAMEDFRAMEBUFFERPROC = C(
    None, UInt, UInt, Int, Int, Int, Int, Int, Int, Int, Int, UInt, UInt
)
PFNGLCHECKNAMEDFRAMEBUFFERSTATUSPROC = C(UInt, UInt, UInt)
PFNGLGETNAMEDFRAMEBUFFERPARAMETERIVPROC = C(None, UInt, UInt, P(Int))
PFNGLGETNAMEDFRAMEBUFFERATTACHMENTPARAMETERIVPROC = C(
    None, UInt, UInt, UInt, P(Int)
)
PFNGLCREATERENDERBUFFERSPROC = C(None, Int, P(UInt))
PFNGLNAMEDRENDERBUFFERSTORAGEPROC = C(None, UInt, UInt, Int, Int)
PFNGLNAMEDRENDERBUFFERSTORAGEMULTISAMPLEPROC = C(
    None, UInt, Int, UInt, Int, Int
)
PFNGLGETNAMEDRENDERBUFFERPARAMETERIVPROC = C(None, UInt, UInt, P(Int))
PFNGLCREATETEXTURESPROC = C(None, UInt, Int, P(UInt))
PFNGLTEXTUREBUFFERPROC = C(None, UInt, UInt, UInt)
PFNGLTEXTUREBUFFERRANGEPROC = C(None, UInt, UInt, UInt, Size, Size)
PFNGLTEXTURESTORAGE1DPROC = C(None, UInt, Int, UInt, Int)
PFNGLTEXTURESTORAGE2DPROC = C(None, UInt, Int, UInt, Int, Int)
PFNGLTEXTURESTORAGE3DPROC = C(None, UInt, Int, UInt, Int, Int, Int)
PFNGLTEXTURESTORAGE2DMULTISAMPLEPROC = C(
    None, UInt, Int, UInt, Int, Int, UByte
)
PFNGLTEXTURESTORAGE3DMULTISAMPLEPROC = C(
    None, UInt, Int, UInt, Int, Int, Int, UByte
)
PFNGLTEXTURESUBIMAGE1DPROC = C(None, UInt, Int, Int, Int, UInt, UInt, VoidP)
PFNGLTEXTURESUBIMAGE2DPROC = C(
    None, UInt, Int, Int, Int, Int, Int, UInt, UInt, VoidP
)
PFNGLTEXTURESUBIMAGE3DPROC = C(
    None, UInt, Int, Int, Int, Int, Int, Int, Int, UInt, UInt, VoidP
)
PFNGLCOMPRESSEDTEXTURESUBIMAGE1DPROC = C(
    None, UInt, Int, Int, Int, UInt, Int, VoidP
)
PFNGLCOMPRESSEDTEXTURESUBIMAGE2DPROC = C(
    None, UInt, Int, Int, Int, Int, Int, UInt, Int, VoidP
)
PFNGLCOMPRESSEDTEXTURESUBIMAGE3DPROC = C(
    None, UInt, Int, Int, Int, Int, Int, Int, Int, UInt, Int, VoidP
)
PFNGLCOPYTEXTURESUBIMAGE1DPROC = C(None, UInt, Int, Int, Int, Int, Int)
PFNGLCOPYTEXTURESUBIMAGE2DPROC = C(
    None, UInt, Int, Int, Int, Int, Int, Int, Int
)
PFNGLCOPYTEXTURESUBIMAGE3DPROC = C(
    None, UInt, Int, Int, Int, Int, Int, Int, Int, Int
)
PFNGLTEXTUREPARAMETERFPROC = C(None, UInt, UInt, Float)
PFNGLTEXTUREPARAMETERFVPROC = C(None, UInt, UInt, P(Float))
PFNGLTEXTUREPARAMETERIPROC = C(None, UInt, UInt, Int)
PFNGLTEXTUREPARAMETERIIVPROC = C(None, UInt, UInt, P(Int))
PFNGLTEXTUREPARAMETERIUIVPROC = C(None, UInt, UInt, P(UInt))
PFNGLTEXTUREPARAMETERIVPROC = C(None, UInt, UInt, P(Int))
PFNGLGENERATETEXTUREMIPMAPPROC = C(None, UInt)
PFNGLBINDTEXTUREUNITPROC = C(None, UInt, UInt)
PFNGLGETTEXTUREIMAGEPROC = C(None, UInt, Int, UInt, UInt, Int, VoidP)
PFNGLGETCOMPRESSEDTEXTUREIMAGEPROC = C(None, UInt, Int, Int, VoidP)
PFNGLGETTEXTURELEVELPARAMETERFVPROC = C(None, UInt, Int, UInt, P(Float))
PFNGLGETTEXTURELEVELPARAMETERIVPROC = C(None, UInt, Int, UInt, P(Int))
PFNGLGETTEXTUREPARAMETERFVPROC = C(None, UInt, UInt, P(Float))
PFNGLGETTEXTUREPARAMETERIIVPROC = C(None, UInt, UInt, P(Int))
PFNGLGETTEXTUREPARAMETERIUIVPROC = C(None, UInt, UInt, P(UInt))
PFNGLGETTEXTUREPARAMETERIVPROC = C(None, UInt, UInt, P(Int))
PFNGLCREATEVERTEXARRAYSPROC = C(None, Int, P(UInt))
PFNGLDISABLEVERTEXARRAYATTRIBPROC = C(None, UInt, UInt)
PFNGLENABLEVERTEXARRAYATTRIBPROC = C(None, UInt, UInt)
PFNGLVERTEXARRAYELEMENTBUFFERPROC = C(None, UInt, UInt)
PFNGLVERTEXARRAYVERTEXBUFFERPROC = C(None, UInt, UInt, UInt, Size, Int)
PFNGLVERTEXARRAYVERTEXBUFFERSPROC = C(
    None, UInt, UInt, Int, P(UInt), P(Size), P(Int)
)
PFNGLVERTEXARRAYATTRIBBINDINGPROC = C(None, UInt, UInt, UInt)
PFNGLVERTEXARRAYATTRIBFORMATPROC = C(None, UInt, UInt, Int, UInt, UByte, UInt)
PFNGLVERTEXARRAYATTRIBIFORMATPROC = C(None, UInt, UInt, Int, UInt, UInt)
PFNGLVERTEXARRAYATTRIBLFORMATPROC = C(None, UInt, UInt, Int, UInt, UInt)
PFNGLVERTEXARRAYBINDINGDIVISORPROC = C(None, UInt, UInt, UInt)
PFNGLGETVERTEXARRAYIVPROC = C(None, UInt, UInt, P(Int))
PFNGLGETVERTEXARRAYINDEXEDIVPROC = C(None, UInt, UInt, UInt, P(Int))
PFNGLGETVERTEXARRAYINDEXED64IVPROC = C(None, UInt, UInt, UInt, P(Long))
PFNGLCREATESAMPLERSPROC = C(None, Int, P(UInt))
PFNGLCREATEPROGRAMPIPELINESPROC = C(None, Int, P(UInt))
PFNGLCREATEQUERIESPROC = C(None, UInt, Int, P(UInt))
PFNGLGETQUERYBUFFEROBJECTI64VPROC = C(None, UInt, UInt, UInt, Size)
PFNGLGETQUERYBUFFEROBJECTIVPROC = C(None, UInt, UInt, UInt, Size)
PFNGLGETQUERYBUFFEROBJECTUI64VPROC = C(None, UInt, UInt, UInt, Size)
PFNGLGETQUERYBUFFEROBJECTUIVPROC = C(None, UInt, UInt, UInt, Size)
PFNGLMEMORYBARRIERBYREGIONPROC = C(None, UInt)
PFNGLGETTEXTURESUBIMAGEPROC = C(
    None, UInt, Int, Int, Int, Int, Int, Int, Int, UInt, UInt, Int, VoidP
)
PFNGLGETCOMPRESSEDTEXTURESUBIMAGEPROC = C(
    None, UInt, Int, Int, Int, Int, Int, Int, Int, Int, VoidP
)
PFNGLGETGRAPHICSRESETSTATUSPROC = C(UInt)
PFNGLGETNCOMPRESSEDTEXIMAGEPROC = C(None, UInt, Int, Int, VoidP)
PFNGLGETNTEXIMAGEPROC = C(None, UInt, Int, UInt, UInt, Int, VoidP)
PFNGLGETNUNIFORMDVPROC = C(None, UInt, Int, Int, P(Double))
PFNGLGETNUNIFORMFVPROC = C(None, UInt, Int, Int, P(Float))
PFNGLGETNUNIFORMIVPROC = C(None, UInt, Int, Int, P(Int))
PFNGLGETNUNIFORMUIVPROC = C(None, UInt, Int, Int, P(UInt))
PFNGLREADNPIXELSPROC = C(None, Int, Int, Int, Int, UInt, UInt, Int, VoidP)
PFNGLTEXTUREBARRIERPROC = C(None)
glClipControl = GL('glClipControl', None, UInt, UInt)
glCreateTransformFeedbacks = GL(
    'glCreateTransformFeedbacks', None, Int, P(UInt)
)
glTransformFeedbackBufferBase = GL(
    'glTransformFeedbackBufferBase', None, UInt, UInt, UInt
)
glTransformFeedbackBufferRange = GL(
    'glTransformFeedbackBufferRange', None, UInt, UInt, UInt, Size, Size
)
glGetTransformFeedbackiv = GL(
    'glGetTransformFeedbackiv', None, UInt, UInt, P(Int)
)
glGetTransformFeedbacki_v = GL(
    'glGetTransformFeedbacki_v', None, UInt, UInt, UInt, P(Int)
)
glGetTransformFeedbacki64_v = GL(
    'glGetTransformFeedbacki64_v', None, UInt, UInt, UInt, P(Long)
)
glCreateBuffers = GL('glCreateBuffers', None, Int, P(UInt))
glNamedBufferStorage = GL(
    'glNamedBufferStorage', None, UInt, Size, VoidP, UInt
)
glNamedBufferData = GL('glNamedBufferData', None, UInt, Size, VoidP, UInt)
glNamedBufferSubData = GL(
    'glNamedBufferSubData', None, UInt, Size, Size, VoidP
)
glCopyNamedBufferSubData = GL(
    'glCopyNamedBufferSubData', None, UInt, UInt, Size, Size, Size
)
glClearNamedBufferData = GL(
    'glClearNamedBufferData', None, UInt, UInt, UInt, UInt, VoidP
)
glClearNamedBufferSubData = GL(
    'glClearNamedBufferSubData', None, UInt, UInt, Size, Size, UInt, UInt,
    VoidP
)
glMapNamedBuffer = GL('glMapNamedBuffer', VoidP, UInt, UInt)
glMapNamedBufferRange = GL(
    'glMapNamedBufferRange', VoidP, UInt, Size, Size, UInt
)
glUnmapNamedBuffer = GL('glUnmapNamedBuffer', UByte, UInt)
glFlushMappedNamedBufferRange = GL(
    'glFlushMappedNamedBufferRange', None, UInt, Size, Size
)
glGetNamedBufferParameteriv = GL(
    'glGetNamedBufferParameteriv', None, UInt, UInt, P(Int)
)
glGetNamedBufferParameteri64v = GL(
    'glGetNamedBufferParameteri64v', None, UInt, UInt, P(Long)
)
glGetNamedBufferPointerv = GL(
    'glGetNamedBufferPointerv', None, UInt, UInt, P(VoidP)
)
glGetNamedBufferSubData = GL(
    'glGetNamedBufferSubData', None, UInt, Size, Size, VoidP
)
glCreateFramebuffers = GL('glCreateFramebuffers', None, Int, P(UInt))
glNamedFramebufferRenderbuffer = GL(
    'glNamedFramebufferRenderbuffer', None, UInt, UInt, UInt, UInt
)
glNamedFramebufferParameteri = GL(
    'glNamedFramebufferParameteri', None, UInt, UInt, Int
)
glNamedFramebufferTexture = GL(
    'glNamedFramebufferTexture', None, UInt, UInt, UInt, Int
)
glNamedFramebufferTextureLayer = GL(
    'glNamedFramebufferTextureLayer', None, UInt, UInt, UInt, Int, Int
)
glNamedFramebufferDrawBuffer = GL(
    'glNamedFramebufferDrawBuffer', None, UInt, UInt
)
glNamedFramebufferDrawBuffers = GL(
    'glNamedFramebufferDrawBuffers', None, UInt, Int, P(UInt)
)
glNamedFramebufferReadBuffer = GL(
    'glNamedFramebufferReadBuffer', None, UInt, UInt
)
glInvalidateNamedFramebufferData = GL(
    'glInvalidateNamedFramebufferData', None, UInt, Int, P(UInt)
)
glInvalidateNamedFramebufferSubData = GL(
    'glInvalidateNamedFramebufferSubData', None, UInt, Int, P(UInt), Int, Int,
    Int, Int
)
glClearNamedFramebufferiv = GL(
    'glClearNamedFramebufferiv', None, UInt, UInt, Int, P(Int)
)
glClearNamedFramebufferuiv = GL(
    'glClearNamedFramebufferuiv', None, UInt, UInt, Int, P(UInt)
)
glClearNamedFramebufferfv = GL(
    'glClearNamedFramebufferfv', None, UInt, UInt, Int, P(Float)
)
glClearNamedFramebufferfi = GL(
    'glClearNamedFramebufferfi', None, UInt, UInt, Int, Float, Int
)
glBlitNamedFramebuffer = GL(
    'glBlitNamedFramebuffer', None, UInt, UInt, Int, Int, Int, Int, Int, Int,
    Int, Int, UInt, UInt
)
glCheckNamedFramebufferStatus = GL(
    'glCheckNamedFramebufferStatus', UInt, UInt, UInt
)
glGetNamedFramebufferParameteriv = GL(
    'glGetNamedFramebufferParameteriv', None, UInt, UInt, P(Int)
)
glGetNamedFramebufferAttachmentParameteriv = GL(
    'glGetNamedFramebufferAttachmentParameteriv', None, UInt, UInt, UInt,
    P(Int)
)
glCreateRenderbuffers = GL('glCreateRenderbuffers', None, Int, P(UInt))
glNamedRenderbufferStorage = GL(
    'glNamedRenderbufferStorage', None, UInt, UInt, Int, Int
)
glNamedRenderbufferStorageMultisample = GL(
    'glNamedRenderbufferStorageMultisample', None, UInt, Int, UInt, Int, Int
)
glGetNamedRenderbufferParameteriv = GL(
    'glGetNamedRenderbufferParameteriv', None, UInt, UInt, P(Int)
)
glCreateTextures = GL('glCreateTextures', None, UInt, Int, P(UInt))
glTextureBuffer = GL('glTextureBuffer', None, UInt, UInt, UInt)
glTextureBufferRange = GL(
    'glTextureBufferRange', None, UInt, UInt, UInt, Size, Size
)
glTextureStorage1D = GL('glTextureStorage1D', None, UInt, Int, UInt, Int)
glTextureStorage2D = GL('glTextureStorage2D', None, UInt, Int, UInt, Int, Int)
glTextureStorage3D = GL(
    'glTextureStorage3D', None, UInt, Int, UInt, Int, Int, Int
)
glTextureStorage2DMultisample = GL(
    'glTextureStorage2DMultisample', None, UInt, Int, UInt, Int, Int, UByte
)
glTextureStorage3DMultisample = GL(
    'glTextureStorage3DMultisample', None, UInt, Int, UInt, Int, Int, Int,
    UByte
)
glTextureSubImage1D = GL(
    'glTextureSubImage1D', None, UInt, Int, Int, Int, UInt, UInt, VoidP
)
glTextureSubImage2D = GL(
    'glTextureSubImage2D', None, UInt, Int, Int, Int, Int, Int, UInt, UInt,
    VoidP
)
glTextureSubImage3D = GL(
    'glTextureSubImage3D', None, UInt, Int, Int, Int, Int, Int, Int, Int,
    UInt, UInt, VoidP
)
glCompressedTextureSubImage1D = GL(
    'glCompressedTextureSubImage1D', None, UInt, Int, Int, Int, UInt, Int,
    VoidP
)
glCompressedTextureSubImage2D = GL(
    'glCompressedTextureSubImage2D', None, UInt, Int, Int, Int, Int, Int,
    UInt, Int, VoidP
)
glCompressedTextureSubImage3D = GL(
    'glCompressedTextureSubImage3D', None, UInt, Int, Int, Int, Int, Int, Int,
    Int, UInt, Int, VoidP
)
glCopyTextureSubImage1D = GL(
    'glCopyTextureSubImage1D', None, UInt, Int, Int, Int, Int, Int
)
glCopyTextureSubImage2D = GL(
    'glCopyTextureSubImage2D', None, UInt, Int, Int, Int, Int, Int, Int, Int
)
glCopyTextureSubImage3D = GL(
    'glCopyTextureSubImage3D', None, UInt, Int, Int, Int, Int, Int, Int, Int,
    Int
)
glTextureParameterf = GL('glTextureParameterf', None, UInt, UInt, Float)
glTextureParameterfv = GL('glTextureParameterfv', None, UInt, UInt, P(Float))
glTextureParameteri = GL('glTextureParameteri', None, UInt, UInt, Int)
glTextureParameterIiv = GL('glTextureParameterIiv', None, UInt, UInt, P(Int))
glTextureParameterIuiv = GL(
    'glTextureParameterIuiv', None, UInt, UInt, P(UInt)
)
glTextureParameteriv = GL('glTextureParameteriv', None, UInt, UInt, P(Int))
glGenerateTextureMipmap = GL('glGenerateTextureMipmap', None, UInt)
glBindTextureUnit = GL('glBindTextureUnit', None, UInt, UInt)
glGetTextureImage = GL(
    'glGetTextureImage', None, UInt, Int, UInt, UInt, Int, VoidP
)
glGetCompressedTextureImage = GL(
    'glGetCompressedTextureImage', None, UInt, Int, Int, VoidP
)
glGetTextureLevelParameterfv = GL(
    'glGetTextureLevelParameterfv', None, UInt, Int, UInt, P(Float)
)
glGetTextureLevelParameteriv = GL(
    'glGetTextureLevelParameteriv', None, UInt, Int, UInt, P(Int)
)
glGetTextureParameterfv = GL(
    'glGetTextureParameterfv', None, UInt, UInt, P(Float)
)
glGetTextureParameterIiv = GL(
    'glGetTextureParameterIiv', None, UInt, UInt, P(Int)
)
glGetTextureParameterIuiv = GL(
    'glGetTextureParameterIuiv', None, UInt, UInt, P(UInt)
)
glGetTextureParameteriv = GL(
    'glGetTextureParameteriv', None, UInt, UInt, P(Int)
)
glCreateVertexArrays = GL('glCreateVertexArrays', None, Int, P(UInt))
glDisableVertexArrayAttrib = GL(
    'glDisableVertexArrayAttrib', None, UInt, UInt
)
glEnableVertexArrayAttrib = GL('glEnableVertexArrayAttrib', None, UInt, UInt)
glVertexArrayElementBuffer = GL(
    'glVertexArrayElementBuffer', None, UInt, UInt
)
glVertexArrayVertexBuffer = GL(
    'glVertexArrayVertexBuffer', None, UInt, UInt, UInt, Size, Int
)
glVertexArrayVertexBuffers = GL(
    'glVertexArrayVertexBuffers', None, UInt, UInt, Int, P(UInt), P(Size),
    P(Int)
)
glVertexArrayAttribBinding = GL(
    'glVertexArrayAttribBinding', None, UInt, UInt, UInt
)
glVertexArrayAttribFormat = GL(
    'glVertexArrayAttribFormat', None, UInt, UInt, Int, UInt, UByte, UInt
)
glVertexArrayAttribIFormat = GL(
    'glVertexArrayAttribIFormat', None, UInt, UInt, Int, UInt, UInt
)
glVertexArrayAttribLFormat = GL(
    'glVertexArrayAttribLFormat', None, UInt, UInt, Int, UInt, UInt
)
glVertexArrayBindingDivisor = GL(
    'glVertexArrayBindingDivisor', None, UInt, UInt, UInt
)
glGetVertexArrayiv = GL('glGetVertexArrayiv', None, UInt, UInt, P(Int))
glGetVertexArrayIndexediv = GL(
    'glGetVertexArrayIndexediv', None, UInt, UInt, UInt, P(Int)
)
glGetVertexArrayIndexed64iv = GL(
    'glGetVertexArrayIndexed64iv', None, UInt, UInt, UInt, P(Long)
)
glCreateSamplers = GL('glCreateSamplers', None, Int, P(UInt))
glCreateProgramPipelines = GL('glCreateProgramPipelines', None, Int, P(UInt))
glCreateQueries = GL('glCreateQueries', None, UInt, Int, P(UInt))
glGetQueryBufferObjecti64v = GL(
    'glGetQueryBufferObjecti64v', None, UInt, UInt, UInt, Size
)
glGetQueryBufferObjectiv = GL(
    'glGetQueryBufferObjectiv', None, UInt, UInt, UInt, Size
)
glGetQueryBufferObjectui64v = GL(
    'glGetQueryBufferObjectui64v', None, UInt, UInt, UInt, Size
)
glGetQueryBufferObjectuiv = GL(
    'glGetQueryBufferObjectuiv', None, UInt, UInt, UInt, Size
)
glMemoryBarrierByRegion = GL('glMemoryBarrierByRegion', None, UInt)
glGetTextureSubImage = GL(
    'glGetTextureSubImage', None, UInt, Int, Int, Int, Int, Int, Int, Int,
    UInt, UInt, Int, VoidP
)
glGetCompressedTextureSubImage = GL(
    'glGetCompressedTextureSubImage', None, UInt, Int, Int, Int, Int, Int,
    Int, Int, Int, VoidP
)
glGetGraphicsResetStatus = GL('glGetGraphicsResetStatus', UInt)
glGetnCompressedTexImage = GL(
    'glGetnCompressedTexImage', None, UInt, Int, Int, VoidP
)
glGetnTexImage = GL('glGetnTexImage', None, UInt, Int, UInt, UInt, Int, VoidP)
glGetnUniformdv = GL('glGetnUniformdv', None, UInt, Int, Int, P(Double))
glGetnUniformfv = GL('glGetnUniformfv', None, UInt, Int, Int, P(Float))
glGetnUniformiv = GL('glGetnUniformiv', None, UInt, Int, Int, P(Int))
glGetnUniformuiv = GL('glGetnUniformuiv', None, UInt, Int, Int, P(UInt))
glReadnPixels = GL(
    'glReadnPixels', None, Int, Int, Int, Int, UInt, UInt, Int, VoidP
)
glTextureBarrier = GL('glTextureBarrier', None)

__all__ = [
    'GL_VERSION_4_5', 'GL_CONTEXT_LOST', 'GL_NEGATIVE_ONE_TO_ONE',
    'GL_ZERO_TO_ONE', 'GL_CLIP_ORIGIN', 'GL_CLIP_DEPTH_MODE',
    'GL_QUERY_WAIT_INVERTED', 'GL_QUERY_NO_WAIT_INVERTED',
    'GL_QUERY_BY_REGION_WAIT_INVERTED', 'GL_QUERY_BY_REGION_NO_WAIT_INVERTED',
    'GL_MAX_CULL_DISTANCES', 'GL_MAX_COMBINED_CLIP_AND_CULL_DISTANCES',
    'GL_TEXTURE_TARGET', 'GL_QUERY_TARGET', 'GL_GUILTY_CONTEXT_RESET',
    'GL_INNOCENT_CONTEXT_RESET', 'GL_UNKNOWN_CONTEXT_RESET',
    'GL_RESET_NOTIFICATION_STRATEGY', 'GL_LOSE_CONTEXT_ON_RESET',
    'GL_NO_RESET_NOTIFICATION', 'GL_CONTEXT_FLAG_ROBUST_ACCESS_BIT',
    'GL_CONTEXT_RELEASE_BEHAVIOR', 'GL_CONTEXT_RELEASE_BEHAVIOR_FLUSH',
    'PFNGLCLIPCONTROLPROC', 'PFNGLCREATETRANSFORMFEEDBACKSPROC',
    'PFNGLTRANSFORMFEEDBACKBUFFERBASEPROC',
    'PFNGLTRANSFORMFEEDBACKBUFFERRANGEPROC',
    'PFNGLGETTRANSFORMFEEDBACKIVPROC', 'PFNGLGETTRANSFORMFEEDBACKI_VPROC',
    'PFNGLGETTRANSFORMFEEDBACKI64_VPROC', 'PFNGLCREATEBUFFERSPROC',
    'PFNGLNAMEDBUFFERSTORAGEPROC', 'PFNGLNAMEDBUFFERDATAPROC',
    'PFNGLNAMEDBUFFERSUBDATAPROC', 'PFNGLCOPYNAMEDBUFFERSUBDATAPROC',
    'PFNGLCLEARNAMEDBUFFERDATAPROC', 'PFNGLCLEARNAMEDBUFFERSUBDATAPROC',
    'PFNGLMAPNAMEDBUFFERPROC', 'PFNGLMAPNAMEDBUFFERRANGEPROC',
    'PFNGLUNMAPNAMEDBUFFERPROC', 'PFNGLFLUSHMAPPEDNAMEDBUFFERRANGEPROC',
    'PFNGLGETNAMEDBUFFERPARAMETERIVPROC',
    'PFNGLGETNAMEDBUFFERPARAMETERI64VPROC', 'PFNGLGETNAMEDBUFFERPOINTERVPROC',
    'PFNGLGETNAMEDBUFFERSUBDATAPROC', 'PFNGLCREATEFRAMEBUFFERSPROC',
    'PFNGLNAMEDFRAMEBUFFERRENDERBUFFERPROC',
    'PFNGLNAMEDFRAMEBUFFERPARAMETERIPROC', 'PFNGLNAMEDFRAMEBUFFERTEXTUREPROC',
    'PFNGLNAMEDFRAMEBUFFERTEXTURELAYERPROC',
    'PFNGLNAMEDFRAMEBUFFERDRAWBUFFERPROC',
    'PFNGLNAMEDFRAMEBUFFERDRAWBUFFERSPROC',
    'PFNGLNAMEDFRAMEBUFFERREADBUFFERPROC',
    'PFNGLINVALIDATENAMEDFRAMEBUFFERDATAPROC',
    'PFNGLINVALIDATENAMEDFRAMEBUFFERSUBDATAPROC',
    'PFNGLCLEARNAMEDFRAMEBUFFERIVPROC', 'PFNGLCLEARNAMEDFRAMEBUFFERUIVPROC',
    'PFNGLCLEARNAMEDFRAMEBUFFERFVPROC', 'PFNGLCLEARNAMEDFRAMEBUFFERFIPROC',
    'PFNGLBLITNAMEDFRAMEBUFFERPROC', 'PFNGLCHECKNAMEDFRAMEBUFFERSTATUSPROC',
    'PFNGLGETNAMEDFRAMEBUFFERPARAMETERIVPROC',
    'PFNGLGETNAMEDFRAMEBUFFERATTACHMENTPARAMETERIVPROC',
    'PFNGLCREATERENDERBUFFERSPROC', 'PFNGLNAMEDRENDERBUFFERSTORAGEPROC',
    'PFNGLNAMEDRENDERBUFFERSTORAGEMULTISAMPLEPROC',
    'PFNGLGETNAMEDRENDERBUFFERPARAMETERIVPROC', 'PFNGLCREATETEXTURESPROC',
    'PFNGLTEXTUREBUFFERPROC', 'PFNGLTEXTUREBUFFERRANGEPROC',
    'PFNGLTEXTURESTORAGE1DPROC', 'PFNGLTEXTURESTORAGE2DPROC',
    'PFNGLTEXTURESTORAGE3DPROC', 'PFNGLTEXTURESTORAGE2DMULTISAMPLEPROC',
    'PFNGLTEXTURESTORAGE3DMULTISAMPLEPROC', 'PFNGLTEXTURESUBIMAGE1DPROC',
    'PFNGLTEXTURESUBIMAGE2DPROC', 'PFNGLTEXTURESUBIMAGE3DPROC',
    'PFNGLCOMPRESSEDTEXTURESUBIMAGE1DPROC',
    'PFNGLCOMPRESSEDTEXTURESUBIMAGE2DPROC',
    'PFNGLCOMPRESSEDTEXTURESUBIMAGE3DPROC', 'PFNGLCOPYTEXTURESUBIMAGE1DPROC',
    'PFNGLCOPYTEXTURESUBIMAGE2DPROC', 'PFNGLCOPYTEXTURESUBIMAGE3DPROC',
    'PFNGLTEXTUREPARAMETERFPROC', 'PFNGLTEXTUREPARAMETERFVPROC',
    'PFNGLTEXTUREPARAMETERIPROC', 'PFNGLTEXTUREPARAMETERIIVPROC',
    'PFNGLTEXTUREPARAMETERIUIVPROC', 'PFNGLTEXTUREPARAMETERIVPROC',
    'PFNGLGENERATETEXTUREMIPMAPPROC', 'PFNGLBINDTEXTUREUNITPROC',
    'PFNGLGETTEXTUREIMAGEPROC', 'PFNGLGETCOMPRESSEDTEXTUREIMAGEPROC',
    'PFNGLGETTEXTURELEVELPARAMETERFVPROC',
    'PFNGLGETTEXTURELEVELPARAMETERIVPROC', 'PFNGLGETTEXTUREPARAMETERFVPROC',
    'PFNGLGETTEXTUREPARAMETERIIVPROC', 'PFNGLGETTEXTUREPARAMETERIUIVPROC',
    'PFNGLGETTEXTUREPARAMETERIVPROC', 'PFNGLCREATEVERTEXARRAYSPROC',
    'PFNGLDISABLEVERTEXARRAYATTRIBPROC', 'PFNGLENABLEVERTEXARRAYATTRIBPROC',
    'PFNGLVERTEXARRAYELEMENTBUFFERPROC', 'PFNGLVERTEXARRAYVERTEXBUFFERPROC',
    'PFNGLVERTEXARRAYVERTEXBUFFERSPROC', 'PFNGLVERTEXARRAYATTRIBBINDINGPROC',
    'PFNGLVERTEXARRAYATTRIBFORMATPROC', 'PFNGLVERTEXARRAYATTRIBIFORMATPROC',
    'PFNGLVERTEXARRAYATTRIBLFORMATPROC', 'PFNGLVERTEXARRAYBINDINGDIVISORPROC',
    'PFNGLGETVERTEXARRAYIVPROC', 'PFNGLGETVERTEXARRAYINDEXEDIVPROC',
    'PFNGLGETVERTEXARRAYINDEXED64IVPROC', 'PFNGLCREATESAMPLERSPROC',
    'PFNGLCREATEPROGRAMPIPELINESPROC', 'PFNGLCREATEQUERIESPROC',
    'PFNGLGETQUERYBUFFEROBJECTI64VPROC', 'PFNGLGETQUERYBUFFEROBJECTIVPROC',
    'PFNGLGETQUERYBUFFEROBJECTUI64VPROC', 'PFNGLGETQUERYBUFFEROBJECTUIVPROC',
    'PFNGLMEMORYBARRIERBYREGIONPROC', 'PFNGLGETTEXTURESUBIMAGEPROC',
    'PFNGLGETCOMPRESSEDTEXTURESUBIMAGEPROC',
    'PFNGLGETGRAPHICSRESETSTATUSPROC', 'PFNGLGETNCOMPRESSEDTEXIMAGEPROC',
    'PFNGLGETNTEXIMAGEPROC', 'PFNGLGETNUNIFORMDVPROC',
    'PFNGLGETNUNIFORMFVPROC', 'PFNGLGETNUNIFORMIVPROC',
    'PFNGLGETNUNIFORMUIVPROC', 'PFNGLREADNPIXELSPROC',
    'PFNGLTEXTUREBARRIERPROC', 'glClipControl', 'glCreateTransformFeedbacks',
    'glTransformFeedbackBufferBase', 'glTransformFeedbackBufferRange',
    'glGetTransformFeedbackiv', 'glGetTransformFeedbacki_v',
    'glGetTransformFeedbacki64_v', 'glCreateBuffers', 'glNamedBufferStorage',
    'glNamedBufferData', 'glNamedBufferSubData', 'glCopyNamedBufferSubData',
    'glClearNamedBufferData', 'glClearNamedBufferSubData', 'glMapNamedBuffer',
    'glMapNamedBufferRange', 'glUnmapNamedBuffer',
    'glFlushMappedNamedBufferRange', 'glGetNamedBufferParameteriv',
    'glGetNamedBufferParameteri64v', 'glGetNamedBufferPointerv',
    'glGetNamedBufferSubData', 'glCreateFramebuffers',
    'glNamedFramebufferRenderbuffer', 'glNamedFramebufferParameteri',
    'glNamedFramebufferTexture', 'glNamedFramebufferTextureLayer',
    'glNamedFramebufferDrawBuffer', 'glNamedFramebufferDrawBuffers',
    'glNamedFramebufferReadBuffer', 'glInvalidateNamedFramebufferData',
    'glInvalidateNamedFramebufferSubData', 'glClearNamedFramebufferiv',
    'glClearNamedFramebufferuiv', 'glClearNamedFramebufferfv',
    'glClearNamedFramebufferfi', 'glBlitNamedFramebuffer',
    'glCheckNamedFramebufferStatus', 'glGetNamedFramebufferParameteriv',
    'glGetNamedFramebufferAttachmentParameteriv', 'glCreateRenderbuffers',
    'glNamedRenderbufferStorage', 'glNamedRenderbufferStorageMultisample',
    'glGetNamedRenderbufferParameteriv', 'glCreateTextures',
    'glTextureBuffer', 'glTextureBufferRange', 'glTextureStorage1D',
    'glTextureStorage2D', 'glTextureStorage3D',
    'glTextureStorage2DMultisample', 'glTextureStorage3DMultisample',
    'glTextureSubImage1D', 'glTextureSubImage2D', 'glTextureSubImage3D',
    'glCompressedTextureSubImage1D', 'glCompressedTextureSubImage2D',
    'glCompressedTextureSubImage3D', 'glCopyTextureSubImage1D',
    'glCopyTextureSubImage2D', 'glCopyTextureSubImage3D',
    'glTextureParameterf', 'glTextureParameterfv', 'glTextureParameteri',
    'glTextureParameterIiv', 'glTextureParameterIuiv', 'glTextureParameteriv',
    'glGenerateTextureMipmap', 'glBindTextureUnit', 'glGetTextureImage',
    'glGetCompressedTextureImage', 'glGetTextureLevelParameterfv',
    'glGetTextureLevelParameteriv', 'glGetTextureParameterfv',
    'glGetTextureParameterIiv', 'glGetTextureParameterIuiv',
    'glGetTextureParameteriv', 'glCreateVertexArrays',
    'glDisableVertexArrayAttrib', 'glEnableVertexArrayAttrib',
    'glVertexArrayElementBuffer', 'glVertexArrayVertexBuffer',
    'glVertexArrayVertexBuffers', 'glVertexArrayAttribBinding',
    'glVertexArrayAttribFormat', 'glVertexArrayAttribIFormat',
    'glVertexArrayAttribLFormat', 'glVertexArrayBindingDivisor',
    'glGetVertexArrayiv', 'glGetVertexArrayIndexediv',
    'glGetVertexArrayIndexed64iv', 'glCreateSamplers',
    'glCreateProgramPipelines', 'glCreateQueries',
    'glGetQueryBufferObjecti64v', 'glGetQueryBufferObjectiv',
    'glGetQueryBufferObjectui64v', 'glGetQueryBufferObjectuiv',
    'glMemoryBarrierByRegion', 'glGetTextureSubImage',
    'glGetCompressedTextureSubImage', 'glGetGraphicsResetStatus',
    'glGetnCompressedTexImage', 'glGetnTexImage', 'glGetnUniformdv',
    'glGetnUniformfv', 'glGetnUniformiv', 'glGetnUniformuiv', 'glReadnPixels',
    'glTextureBarrier'
]
