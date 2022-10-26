from .._wrapper import *

GL_EXT_EGL_image_storage = 1
PFNGLEGLIMAGETARGETTEXSTORAGEEXTPROC = C(None, UInt, VoidP, P(Int))
PFNGLEGLIMAGETARGETTEXTURESTORAGEEXTPROC = C(None, UInt, VoidP, P(Int))
glEGLImageTargetTexStorageEXT = GL(
    'glEGLImageTargetTexStorageEXT', None, UInt, VoidP, P(Int)
)
glEGLImageTargetTextureStorageEXT = GL(
    'glEGLImageTargetTextureStorageEXT', None, UInt, VoidP, P(Int)
)
GL_EXT_EGL_sync = 1
GL_EXT_debug_label = 1
GL_PROGRAM_PIPELINE_OBJECT_EXT = 0x8A4F
GL_PROGRAM_OBJECT_EXT = 0x8B40
GL_SHADER_OBJECT_EXT = 0x8B48
GL_BUFFER_OBJECT_EXT = 0x9151
GL_QUERY_OBJECT_EXT = 0x9153
GL_VERTEX_ARRAY_OBJECT_EXT = 0x9154
PFNGLLABELOBJECTEXTPROC = C(None, UInt, UInt, Int, CharP)
PFNGLGETOBJECTLABELEXTPROC = C(None, UInt, UInt, Int, P(Int), CharP)
glLabelObjectEXT = GL('glLabelObjectEXT', None, UInt, UInt, Int, CharP)
glGetObjectLabelEXT = GL(
    'glGetObjectLabelEXT', None, UInt, UInt, Int, P(Int), CharP
)
GL_EXT_debug_marker = 1
PFNGLINSERTEVENTMARKEREXTPROC = C(None, Int, CharP)
PFNGLPUSHGROUPMARKEREXTPROC = C(None, Int, CharP)
PFNGLPOPGROUPMARKEREXTPROC = C(None)
glInsertEventMarkerEXT = GL('glInsertEventMarkerEXT', None, Int, CharP)
glPushGroupMarkerEXT = GL('glPushGroupMarkerEXT', None, Int, CharP)
glPopGroupMarkerEXT = GL('glPopGroupMarkerEXT', None)
GL_EXT_direct_state_access = 1
GL_PROGRAM_MATRIX_EXT = 0x8E2D
GL_TRANSPOSE_PROGRAM_MATRIX_EXT = 0x8E2E
GL_PROGRAM_MATRIX_STACK_DEPTH_EXT = 0x8E2F
PFNGLMATRIXLOADFEXTPROC = C(None, UInt, P(Float))
PFNGLMATRIXLOADDEXTPROC = C(None, UInt, P(Double))
PFNGLMATRIXMULTFEXTPROC = C(None, UInt, P(Float))
PFNGLMATRIXMULTDEXTPROC = C(None, UInt, P(Double))
PFNGLMATRIXLOADIDENTITYEXTPROC = C(None, UInt)
PFNGLMATRIXROTATEFEXTPROC = C(None, UInt, Float, Float, Float, Float)
PFNGLMATRIXROTATEDEXTPROC = C(None, UInt, Double, Double, Double, Double)
PFNGLMATRIXSCALEFEXTPROC = C(None, UInt, Float, Float, Float)
PFNGLMATRIXSCALEDEXTPROC = C(None, UInt, Double, Double, Double)
PFNGLMATRIXTRANSLATEFEXTPROC = C(None, UInt, Float, Float, Float)
PFNGLMATRIXTRANSLATEDEXTPROC = C(None, UInt, Double, Double, Double)
PFNGLMATRIXFRUSTUMEXTPROC = C(
    None, UInt, Double, Double, Double, Double, Double, Double
)
PFNGLMATRIXORTHOEXTPROC = C(
    None, UInt, Double, Double, Double, Double, Double, Double
)
PFNGLMATRIXPOPEXTPROC = C(None, UInt)
PFNGLMATRIXPUSHEXTPROC = C(None, UInt)
PFNGLCLIENTATTRIBDEFAULTEXTPROC = C(None, UInt)
PFNGLPUSHCLIENTATTRIBDEFAULTEXTPROC = C(None, UInt)
PFNGLTEXTUREPARAMETERFEXTPROC = C(None, UInt, UInt, UInt, Float)
PFNGLTEXTUREPARAMETERFVEXTPROC = C(None, UInt, UInt, UInt, P(Float))
PFNGLTEXTUREPARAMETERIEXTPROC = C(None, UInt, UInt, UInt, Int)
PFNGLTEXTUREPARAMETERIVEXTPROC = C(None, UInt, UInt, UInt, P(Int))
PFNGLTEXTUREIMAGE1DEXTPROC = C(
    None, UInt, UInt, Int, Int, Int, Int, UInt, UInt, VoidP
)
PFNGLTEXTUREIMAGE2DEXTPROC = C(
    None, UInt, UInt, Int, Int, Int, Int, Int, UInt, UInt, VoidP
)
PFNGLTEXTURESUBIMAGE1DEXTPROC = C(
    None, UInt, UInt, Int, Int, Int, UInt, UInt, VoidP
)
PFNGLTEXTURESUBIMAGE2DEXTPROC = C(
    None, UInt, UInt, Int, Int, Int, Int, Int, UInt, UInt, VoidP
)
PFNGLCOPYTEXTUREIMAGE1DEXTPROC = C(
    None, UInt, UInt, Int, UInt, Int, Int, Int, Int
)
PFNGLCOPYTEXTUREIMAGE2DEXTPROC = C(
    None, UInt, UInt, Int, UInt, Int, Int, Int, Int, Int
)
PFNGLCOPYTEXTURESUBIMAGE1DEXTPROC = C(
    None, UInt, UInt, Int, Int, Int, Int, Int
)
PFNGLCOPYTEXTURESUBIMAGE2DEXTPROC = C(
    None, UInt, UInt, Int, Int, Int, Int, Int, Int, Int
)
PFNGLGETTEXTUREIMAGEEXTPROC = C(None, UInt, UInt, Int, UInt, UInt, VoidP)
PFNGLGETTEXTUREPARAMETERFVEXTPROC = C(None, UInt, UInt, UInt, P(Float))
PFNGLGETTEXTUREPARAMETERIVEXTPROC = C(None, UInt, UInt, UInt, P(Int))
PFNGLGETTEXTURELEVELPARAMETERFVEXTPROC = C(
    None, UInt, UInt, Int, UInt, P(Float)
)
PFNGLGETTEXTURELEVELPARAMETERIVEXTPROC = C(
    None, UInt, UInt, Int, UInt, P(Int)
)
PFNGLTEXTUREIMAGE3DEXTPROC = C(
    None, UInt, UInt, Int, Int, Int, Int, Int, Int, UInt, UInt, VoidP
)
PFNGLTEXTURESUBIMAGE3DEXTPROC = C(
    None, UInt, UInt, Int, Int, Int, Int, Int, Int, Int, UInt, UInt, VoidP
)
PFNGLCOPYTEXTURESUBIMAGE3DEXTPROC = C(
    None, UInt, UInt, Int, Int, Int, Int, Int, Int, Int, Int
)
PFNGLBINDMULTITEXTUREEXTPROC = C(None, UInt, UInt, UInt)
PFNGLMULTITEXCOORDPOINTEREXTPROC = C(None, UInt, Int, UInt, Int, VoidP)
PFNGLMULTITEXENVFEXTPROC = C(None, UInt, UInt, UInt, Float)
PFNGLMULTITEXENVFVEXTPROC = C(None, UInt, UInt, UInt, P(Float))
PFNGLMULTITEXENVIEXTPROC = C(None, UInt, UInt, UInt, Int)
PFNGLMULTITEXENVIVEXTPROC = C(None, UInt, UInt, UInt, P(Int))
PFNGLMULTITEXGENDEXTPROC = C(None, UInt, UInt, UInt, Double)
PFNGLMULTITEXGENDVEXTPROC = C(None, UInt, UInt, UInt, P(Double))
PFNGLMULTITEXGENFEXTPROC = C(None, UInt, UInt, UInt, Float)
PFNGLMULTITEXGENFVEXTPROC = C(None, UInt, UInt, UInt, P(Float))
PFNGLMULTITEXGENIEXTPROC = C(None, UInt, UInt, UInt, Int)
PFNGLMULTITEXGENIVEXTPROC = C(None, UInt, UInt, UInt, P(Int))
PFNGLGETMULTITEXENVFVEXTPROC = C(None, UInt, UInt, UInt, P(Float))
PFNGLGETMULTITEXENVIVEXTPROC = C(None, UInt, UInt, UInt, P(Int))
PFNGLGETMULTITEXGENDVEXTPROC = C(None, UInt, UInt, UInt, P(Double))
PFNGLGETMULTITEXGENFVEXTPROC = C(None, UInt, UInt, UInt, P(Float))
PFNGLGETMULTITEXGENIVEXTPROC = C(None, UInt, UInt, UInt, P(Int))
PFNGLMULTITEXPARAMETERIEXTPROC = C(None, UInt, UInt, UInt, Int)
PFNGLMULTITEXPARAMETERIVEXTPROC = C(None, UInt, UInt, UInt, P(Int))
PFNGLMULTITEXPARAMETERFEXTPROC = C(None, UInt, UInt, UInt, Float)
PFNGLMULTITEXPARAMETERFVEXTPROC = C(None, UInt, UInt, UInt, P(Float))
PFNGLMULTITEXIMAGE1DEXTPROC = C(
    None, UInt, UInt, Int, Int, Int, Int, UInt, UInt, VoidP
)
PFNGLMULTITEXIMAGE2DEXTPROC = C(
    None, UInt, UInt, Int, Int, Int, Int, Int, UInt, UInt, VoidP
)
PFNGLMULTITEXSUBIMAGE1DEXTPROC = C(
    None, UInt, UInt, Int, Int, Int, UInt, UInt, VoidP
)
PFNGLMULTITEXSUBIMAGE2DEXTPROC = C(
    None, UInt, UInt, Int, Int, Int, Int, Int, UInt, UInt, VoidP
)
PFNGLCOPYMULTITEXIMAGE1DEXTPROC = C(
    None, UInt, UInt, Int, UInt, Int, Int, Int, Int
)
PFNGLCOPYMULTITEXIMAGE2DEXTPROC = C(
    None, UInt, UInt, Int, UInt, Int, Int, Int, Int, Int
)
PFNGLCOPYMULTITEXSUBIMAGE1DEXTPROC = C(
    None, UInt, UInt, Int, Int, Int, Int, Int
)
PFNGLCOPYMULTITEXSUBIMAGE2DEXTPROC = C(
    None, UInt, UInt, Int, Int, Int, Int, Int, Int, Int
)
PFNGLGETMULTITEXIMAGEEXTPROC = C(None, UInt, UInt, Int, UInt, UInt, VoidP)
PFNGLGETMULTITEXPARAMETERFVEXTPROC = C(None, UInt, UInt, UInt, P(Float))
PFNGLGETMULTITEXPARAMETERIVEXTPROC = C(None, UInt, UInt, UInt, P(Int))
PFNGLGETMULTITEXLEVELPARAMETERFVEXTPROC = C(
    None, UInt, UInt, Int, UInt, P(Float)
)
PFNGLGETMULTITEXLEVELPARAMETERIVEXTPROC = C(
    None, UInt, UInt, Int, UInt, P(Int)
)
PFNGLMULTITEXIMAGE3DEXTPROC = C(
    None, UInt, UInt, Int, Int, Int, Int, Int, Int, UInt, UInt, VoidP
)
PFNGLMULTITEXSUBIMAGE3DEXTPROC = C(
    None, UInt, UInt, Int, Int, Int, Int, Int, Int, Int, UInt, UInt, VoidP
)
PFNGLCOPYMULTITEXSUBIMAGE3DEXTPROC = C(
    None, UInt, UInt, Int, Int, Int, Int, Int, Int, Int, Int
)
PFNGLENABLECLIENTSTATEINDEXEDEXTPROC = C(None, UInt, UInt)
PFNGLDISABLECLIENTSTATEINDEXEDEXTPROC = C(None, UInt, UInt)
PFNGLGETFLOATINDEXEDVEXTPROC = C(None, UInt, UInt, P(Float))
PFNGLGETDOUBLEINDEXEDVEXTPROC = C(None, UInt, UInt, P(Double))
PFNGLGETPOINTERINDEXEDVEXTPROC = C(None, UInt, UInt, P(VoidP))
PFNGLENABLEINDEXEDEXTPROC = C(None, UInt, UInt)
PFNGLDISABLEINDEXEDEXTPROC = C(None, UInt, UInt)
PFNGLISENABLEDINDEXEDEXTPROC = C(UByte, UInt, UInt)
PFNGLGETINTEGERINDEXEDVEXTPROC = C(None, UInt, UInt, P(Int))
PFNGLGETBOOLEANINDEXEDVEXTPROC = C(None, UInt, UInt, P(UByte))
PFNGLCOMPRESSEDTEXTUREIMAGE3DEXTPROC = C(
    None, UInt, UInt, Int, UInt, Int, Int, Int, Int, Int, VoidP
)
PFNGLCOMPRESSEDTEXTUREIMAGE2DEXTPROC = C(
    None, UInt, UInt, Int, UInt, Int, Int, Int, Int, VoidP
)
PFNGLCOMPRESSEDTEXTUREIMAGE1DEXTPROC = C(
    None, UInt, UInt, Int, UInt, Int, Int, Int, VoidP
)
PFNGLCOMPRESSEDTEXTURESUBIMAGE3DEXTPROC = C(
    None, UInt, UInt, Int, Int, Int, Int, Int, Int, Int, UInt, Int, VoidP
)
PFNGLCOMPRESSEDTEXTURESUBIMAGE2DEXTPROC = C(
    None, UInt, UInt, Int, Int, Int, Int, Int, UInt, Int, VoidP
)
PFNGLCOMPRESSEDTEXTURESUBIMAGE1DEXTPROC = C(
    None, UInt, UInt, Int, Int, Int, UInt, Int, VoidP
)
PFNGLGETCOMPRESSEDTEXTUREIMAGEEXTPROC = C(None, UInt, UInt, Int, VoidP)
PFNGLCOMPRESSEDMULTITEXIMAGE3DEXTPROC = C(
    None, UInt, UInt, Int, UInt, Int, Int, Int, Int, Int, VoidP
)
PFNGLCOMPRESSEDMULTITEXIMAGE2DEXTPROC = C(
    None, UInt, UInt, Int, UInt, Int, Int, Int, Int, VoidP
)
PFNGLCOMPRESSEDMULTITEXIMAGE1DEXTPROC = C(
    None, UInt, UInt, Int, UInt, Int, Int, Int, VoidP
)
PFNGLCOMPRESSEDMULTITEXSUBIMAGE3DEXTPROC = C(
    None, UInt, UInt, Int, Int, Int, Int, Int, Int, Int, UInt, Int, VoidP
)
PFNGLCOMPRESSEDMULTITEXSUBIMAGE2DEXTPROC = C(
    None, UInt, UInt, Int, Int, Int, Int, Int, UInt, Int, VoidP
)
PFNGLCOMPRESSEDMULTITEXSUBIMAGE1DEXTPROC = C(
    None, UInt, UInt, Int, Int, Int, UInt, Int, VoidP
)
PFNGLGETCOMPRESSEDMULTITEXIMAGEEXTPROC = C(None, UInt, UInt, Int, VoidP)
PFNGLMATRIXLOADTRANSPOSEFEXTPROC = C(None, UInt, P(Float))
PFNGLMATRIXLOADTRANSPOSEDEXTPROC = C(None, UInt, P(Double))
PFNGLMATRIXMULTTRANSPOSEFEXTPROC = C(None, UInt, P(Float))
PFNGLMATRIXMULTTRANSPOSEDEXTPROC = C(None, UInt, P(Double))
PFNGLNAMEDBUFFERDATAEXTPROC = C(None, UInt, Size, VoidP, UInt)
PFNGLNAMEDBUFFERSUBDATAEXTPROC = C(None, UInt, Size, Size, VoidP)
PFNGLMAPNAMEDBUFFEREXTPROC = C(VoidP, UInt, UInt)
PFNGLUNMAPNAMEDBUFFEREXTPROC = C(UByte, UInt)
PFNGLGETNAMEDBUFFERPARAMETERIVEXTPROC = C(None, UInt, UInt, P(Int))
PFNGLGETNAMEDBUFFERPOINTERVEXTPROC = C(None, UInt, UInt, P(VoidP))
PFNGLGETNAMEDBUFFERSUBDATAEXTPROC = C(None, UInt, Size, Size, VoidP)
PFNGLPROGRAMUNIFORM1FEXTPROC = C(None, UInt, Int, Float)
PFNGLPROGRAMUNIFORM2FEXTPROC = C(None, UInt, Int, Float, Float)
PFNGLPROGRAMUNIFORM3FEXTPROC = C(None, UInt, Int, Float, Float, Float)
PFNGLPROGRAMUNIFORM4FEXTPROC = C(None, UInt, Int, Float, Float, Float, Float)
PFNGLPROGRAMUNIFORM1IEXTPROC = C(None, UInt, Int, Int)
PFNGLPROGRAMUNIFORM2IEXTPROC = C(None, UInt, Int, Int, Int)
PFNGLPROGRAMUNIFORM3IEXTPROC = C(None, UInt, Int, Int, Int, Int)
PFNGLPROGRAMUNIFORM4IEXTPROC = C(None, UInt, Int, Int, Int, Int, Int)
PFNGLPROGRAMUNIFORM1FVEXTPROC = C(None, UInt, Int, Int, P(Float))
PFNGLPROGRAMUNIFORM2FVEXTPROC = C(None, UInt, Int, Int, P(Float))
PFNGLPROGRAMUNIFORM3FVEXTPROC = C(None, UInt, Int, Int, P(Float))
PFNGLPROGRAMUNIFORM4FVEXTPROC = C(None, UInt, Int, Int, P(Float))
PFNGLPROGRAMUNIFORM1IVEXTPROC = C(None, UInt, Int, Int, P(Int))
PFNGLPROGRAMUNIFORM2IVEXTPROC = C(None, UInt, Int, Int, P(Int))
PFNGLPROGRAMUNIFORM3IVEXTPROC = C(None, UInt, Int, Int, P(Int))
PFNGLPROGRAMUNIFORM4IVEXTPROC = C(None, UInt, Int, Int, P(Int))
PFNGLPROGRAMUNIFORMMATRIX2FVEXTPROC = C(None, UInt, Int, Int, UByte, P(Float))
PFNGLPROGRAMUNIFORMMATRIX3FVEXTPROC = C(None, UInt, Int, Int, UByte, P(Float))
PFNGLPROGRAMUNIFORMMATRIX4FVEXTPROC = C(None, UInt, Int, Int, UByte, P(Float))
PFNGLPROGRAMUNIFORMMATRIX2X3FVEXTPROC = C(
    None, UInt, Int, Int, UByte, P(Float)
)
PFNGLPROGRAMUNIFORMMATRIX3X2FVEXTPROC = C(
    None, UInt, Int, Int, UByte, P(Float)
)
PFNGLPROGRAMUNIFORMMATRIX2X4FVEXTPROC = C(
    None, UInt, Int, Int, UByte, P(Float)
)
PFNGLPROGRAMUNIFORMMATRIX4X2FVEXTPROC = C(
    None, UInt, Int, Int, UByte, P(Float)
)
PFNGLPROGRAMUNIFORMMATRIX3X4FVEXTPROC = C(
    None, UInt, Int, Int, UByte, P(Float)
)
PFNGLPROGRAMUNIFORMMATRIX4X3FVEXTPROC = C(
    None, UInt, Int, Int, UByte, P(Float)
)
PFNGLTEXTUREBUFFEREXTPROC = C(None, UInt, UInt, UInt, UInt)
PFNGLMULTITEXBUFFEREXTPROC = C(None, UInt, UInt, UInt, UInt)
PFNGLTEXTUREPARAMETERIIVEXTPROC = C(None, UInt, UInt, UInt, P(Int))
PFNGLTEXTUREPARAMETERIUIVEXTPROC = C(None, UInt, UInt, UInt, P(UInt))
PFNGLGETTEXTUREPARAMETERIIVEXTPROC = C(None, UInt, UInt, UInt, P(Int))
PFNGLGETTEXTUREPARAMETERIUIVEXTPROC = C(None, UInt, UInt, UInt, P(UInt))
PFNGLMULTITEXPARAMETERIIVEXTPROC = C(None, UInt, UInt, UInt, P(Int))
PFNGLMULTITEXPARAMETERIUIVEXTPROC = C(None, UInt, UInt, UInt, P(UInt))
PFNGLGETMULTITEXPARAMETERIIVEXTPROC = C(None, UInt, UInt, UInt, P(Int))
PFNGLGETMULTITEXPARAMETERIUIVEXTPROC = C(None, UInt, UInt, UInt, P(UInt))
PFNGLPROGRAMUNIFORM1UIEXTPROC = C(None, UInt, Int, UInt)
PFNGLPROGRAMUNIFORM2UIEXTPROC = C(None, UInt, Int, UInt, UInt)
PFNGLPROGRAMUNIFORM3UIEXTPROC = C(None, UInt, Int, UInt, UInt, UInt)
PFNGLPROGRAMUNIFORM4UIEXTPROC = C(None, UInt, Int, UInt, UInt, UInt, UInt)
PFNGLPROGRAMUNIFORM1UIVEXTPROC = C(None, UInt, Int, Int, P(UInt))
PFNGLPROGRAMUNIFORM2UIVEXTPROC = C(None, UInt, Int, Int, P(UInt))
PFNGLPROGRAMUNIFORM3UIVEXTPROC = C(None, UInt, Int, Int, P(UInt))
PFNGLPROGRAMUNIFORM4UIVEXTPROC = C(None, UInt, Int, Int, P(UInt))
PFNGLNAMEDPROGRAMLOCALPARAMETERS4FVEXTPROC = C(
    None, UInt, UInt, UInt, Int, P(Float)
)
PFNGLNAMEDPROGRAMLOCALPARAMETERI4IEXTPROC = C(
    None, UInt, UInt, UInt, Int, Int, Int, Int
)
PFNGLNAMEDPROGRAMLOCALPARAMETERI4IVEXTPROC = C(None, UInt, UInt, UInt, P(Int))
PFNGLNAMEDPROGRAMLOCALPARAMETERSI4IVEXTPROC = C(
    None, UInt, UInt, UInt, Int, P(Int)
)
PFNGLNAMEDPROGRAMLOCALPARAMETERI4UIEXTPROC = C(
    None, UInt, UInt, UInt, UInt, UInt, UInt, UInt
)
PFNGLNAMEDPROGRAMLOCALPARAMETERI4UIVEXTPROC = C(
    None, UInt, UInt, UInt, P(UInt)
)
PFNGLNAMEDPROGRAMLOCALPARAMETERSI4UIVEXTPROC = C(
    None, UInt, UInt, UInt, Int, P(UInt)
)
PFNGLGETNAMEDPROGRAMLOCALPARAMETERIIVEXTPROC = C(
    None, UInt, UInt, UInt, P(Int)
)
PFNGLGETNAMEDPROGRAMLOCALPARAMETERIUIVEXTPROC = C(
    None, UInt, UInt, UInt, P(UInt)
)
PFNGLENABLECLIENTSTATEIEXTPROC = C(None, UInt, UInt)
PFNGLDISABLECLIENTSTATEIEXTPROC = C(None, UInt, UInt)
PFNGLGETFLOATI_VEXTPROC = C(None, UInt, UInt, P(Float))
PFNGLGETDOUBLEI_VEXTPROC = C(None, UInt, UInt, P(Double))
PFNGLGETPOINTERI_VEXTPROC = C(None, UInt, UInt, P(VoidP))
PFNGLNAMEDPROGRAMSTRINGEXTPROC = C(None, UInt, UInt, UInt, Int, VoidP)
PFNGLNAMEDPROGRAMLOCALPARAMETER4DEXTPROC = C(
    None, UInt, UInt, UInt, Double, Double, Double, Double
)
PFNGLNAMEDPROGRAMLOCALPARAMETER4DVEXTPROC = C(
    None, UInt, UInt, UInt, P(Double)
)
PFNGLNAMEDPROGRAMLOCALPARAMETER4FEXTPROC = C(
    None, UInt, UInt, UInt, Float, Float, Float, Float
)
PFNGLNAMEDPROGRAMLOCALPARAMETER4FVEXTPROC = C(
    None, UInt, UInt, UInt, P(Float)
)
PFNGLGETNAMEDPROGRAMLOCALPARAMETERDVEXTPROC = C(
    None, UInt, UInt, UInt, P(Double)
)
PFNGLGETNAMEDPROGRAMLOCALPARAMETERFVEXTPROC = C(
    None, UInt, UInt, UInt, P(Float)
)
PFNGLGETNAMEDPROGRAMIVEXTPROC = C(None, UInt, UInt, UInt, P(Int))
PFNGLGETNAMEDPROGRAMSTRINGEXTPROC = C(None, UInt, UInt, UInt, VoidP)
PFNGLNAMEDRENDERBUFFERSTORAGEEXTPROC = C(None, UInt, UInt, Int, Int)
PFNGLGETNAMEDRENDERBUFFERPARAMETERIVEXTPROC = C(None, UInt, UInt, P(Int))
PFNGLNAMEDRENDERBUFFERSTORAGEMULTISAMPLEEXTPROC = C(
    None, UInt, Int, UInt, Int, Int
)
PFNGLNAMEDRENDERBUFFERSTORAGEMULTISAMPLECOVERAGEEXTPROC = C(
    None, UInt, Int, Int, UInt, Int, Int
)
PFNGLCHECKNAMEDFRAMEBUFFERSTATUSEXTPROC = C(UInt, UInt, UInt)
PFNGLNAMEDFRAMEBUFFERTEXTURE1DEXTPROC = C(None, UInt, UInt, UInt, UInt, Int)
PFNGLNAMEDFRAMEBUFFERTEXTURE2DEXTPROC = C(None, UInt, UInt, UInt, UInt, Int)
PFNGLNAMEDFRAMEBUFFERTEXTURE3DEXTPROC = C(
    None, UInt, UInt, UInt, UInt, Int, Int
)
PFNGLNAMEDFRAMEBUFFERRENDERBUFFEREXTPROC = C(None, UInt, UInt, UInt, UInt)
PFNGLGETNAMEDFRAMEBUFFERATTACHMENTPARAMETERIVEXTPROC = C(
    None, UInt, UInt, UInt, P(Int)
)
PFNGLGENERATETEXTUREMIPMAPEXTPROC = C(None, UInt, UInt)
PFNGLGENERATEMULTITEXMIPMAPEXTPROC = C(None, UInt, UInt)
PFNGLFRAMEBUFFERDRAWBUFFEREXTPROC = C(None, UInt, UInt)
PFNGLFRAMEBUFFERDRAWBUFFERSEXTPROC = C(None, UInt, Int, P(UInt))
PFNGLFRAMEBUFFERREADBUFFEREXTPROC = C(None, UInt, UInt)
PFNGLGETFRAMEBUFFERPARAMETERIVEXTPROC = C(None, UInt, UInt, P(Int))
PFNGLNAMEDCOPYBUFFERSUBDATAEXTPROC = C(None, UInt, UInt, Size, Size, Size)
PFNGLNAMEDFRAMEBUFFERTEXTUREEXTPROC = C(None, UInt, UInt, UInt, Int)
PFNGLNAMEDFRAMEBUFFERTEXTURELAYEREXTPROC = C(None, UInt, UInt, UInt, Int, Int)
PFNGLNAMEDFRAMEBUFFERTEXTUREFACEEXTPROC = C(None, UInt, UInt, UInt, Int, UInt)
PFNGLTEXTURERENDERBUFFEREXTPROC = C(None, UInt, UInt, UInt)
PFNGLMULTITEXRENDERBUFFEREXTPROC = C(None, UInt, UInt, UInt)
PFNGLVERTEXARRAYVERTEXOFFSETEXTPROC = C(
    None, UInt, UInt, Int, UInt, Int, Size
)
PFNGLVERTEXARRAYCOLOROFFSETEXTPROC = C(None, UInt, UInt, Int, UInt, Int, Size)
PFNGLVERTEXARRAYEDGEFLAGOFFSETEXTPROC = C(None, UInt, UInt, Int, Size)
PFNGLVERTEXARRAYINDEXOFFSETEXTPROC = C(None, UInt, UInt, UInt, Int, Size)
PFNGLVERTEXARRAYNORMALOFFSETEXTPROC = C(None, UInt, UInt, UInt, Int, Size)
PFNGLVERTEXARRAYTEXCOORDOFFSETEXTPROC = C(
    None, UInt, UInt, Int, UInt, Int, Size
)
PFNGLVERTEXARRAYMULTITEXCOORDOFFSETEXTPROC = C(
    None, UInt, UInt, UInt, Int, UInt, Int, Size
)
PFNGLVERTEXARRAYFOGCOORDOFFSETEXTPROC = C(None, UInt, UInt, UInt, Int, Size)
PFNGLVERTEXARRAYSECONDARYCOLOROFFSETEXTPROC = C(
    None, UInt, UInt, Int, UInt, Int, Size
)
PFNGLVERTEXARRAYVERTEXATTRIBOFFSETEXTPROC = C(
    None, UInt, UInt, UInt, Int, UInt, UByte, Int, Size
)
PFNGLVERTEXARRAYVERTEXATTRIBIOFFSETEXTPROC = C(
    None, UInt, UInt, UInt, Int, UInt, Int, Size
)
PFNGLENABLEVERTEXARRAYEXTPROC = C(None, UInt, UInt)
PFNGLDISABLEVERTEXARRAYEXTPROC = C(None, UInt, UInt)
PFNGLENABLEVERTEXARRAYATTRIBEXTPROC = C(None, UInt, UInt)
PFNGLDISABLEVERTEXARRAYATTRIBEXTPROC = C(None, UInt, UInt)
PFNGLGETVERTEXARRAYINTEGERVEXTPROC = C(None, UInt, UInt, P(Int))
PFNGLGETVERTEXARRAYPOINTERVEXTPROC = C(None, UInt, UInt, P(VoidP))
PFNGLGETVERTEXARRAYINTEGERI_VEXTPROC = C(None, UInt, UInt, UInt, P(Int))
PFNGLGETVERTEXARRAYPOINTERI_VEXTPROC = C(None, UInt, UInt, UInt, P(VoidP))
PFNGLMAPNAMEDBUFFERRANGEEXTPROC = C(VoidP, UInt, Size, Size, UInt)
PFNGLFLUSHMAPPEDNAMEDBUFFERRANGEEXTPROC = C(None, UInt, Size, Size)
PFNGLNAMEDBUFFERSTORAGEEXTPROC = C(None, UInt, Size, VoidP, UInt)
PFNGLCLEARNAMEDBUFFERDATAEXTPROC = C(None, UInt, UInt, UInt, UInt, VoidP)
PFNGLCLEARNAMEDBUFFERSUBDATAEXTPROC = C(
    None, UInt, UInt, Size, Size, UInt, UInt, VoidP
)
PFNGLNAMEDFRAMEBUFFERPARAMETERIEXTPROC = C(None, UInt, UInt, Int)
PFNGLGETNAMEDFRAMEBUFFERPARAMETERIVEXTPROC = C(None, UInt, UInt, P(Int))
PFNGLPROGRAMUNIFORM1DEXTPROC = C(None, UInt, Int, Double)
PFNGLPROGRAMUNIFORM2DEXTPROC = C(None, UInt, Int, Double, Double)
PFNGLPROGRAMUNIFORM3DEXTPROC = C(None, UInt, Int, Double, Double, Double)
PFNGLPROGRAMUNIFORM4DEXTPROC = C(
    None, UInt, Int, Double, Double, Double, Double
)
PFNGLPROGRAMUNIFORM1DVEXTPROC = C(None, UInt, Int, Int, P(Double))
PFNGLPROGRAMUNIFORM2DVEXTPROC = C(None, UInt, Int, Int, P(Double))
PFNGLPROGRAMUNIFORM3DVEXTPROC = C(None, UInt, Int, Int, P(Double))
PFNGLPROGRAMUNIFORM4DVEXTPROC = C(None, UInt, Int, Int, P(Double))
PFNGLPROGRAMUNIFORMMATRIX2DVEXTPROC = C(
    None, UInt, Int, Int, UByte, P(Double)
)
PFNGLPROGRAMUNIFORMMATRIX3DVEXTPROC = C(
    None, UInt, Int, Int, UByte, P(Double)
)
PFNGLPROGRAMUNIFORMMATRIX4DVEXTPROC = C(
    None, UInt, Int, Int, UByte, P(Double)
)
PFNGLPROGRAMUNIFORMMATRIX2X3DVEXTPROC = C(
    None, UInt, Int, Int, UByte, P(Double)
)
PFNGLPROGRAMUNIFORMMATRIX2X4DVEXTPROC = C(
    None, UInt, Int, Int, UByte, P(Double)
)
PFNGLPROGRAMUNIFORMMATRIX3X2DVEXTPROC = C(
    None, UInt, Int, Int, UByte, P(Double)
)
PFNGLPROGRAMUNIFORMMATRIX3X4DVEXTPROC = C(
    None, UInt, Int, Int, UByte, P(Double)
)
PFNGLPROGRAMUNIFORMMATRIX4X2DVEXTPROC = C(
    None, UInt, Int, Int, UByte, P(Double)
)
PFNGLPROGRAMUNIFORMMATRIX4X3DVEXTPROC = C(
    None, UInt, Int, Int, UByte, P(Double)
)
PFNGLTEXTUREBUFFERRANGEEXTPROC = C(None, UInt, UInt, UInt, UInt, Size, Size)
PFNGLTEXTURESTORAGE1DEXTPROC = C(None, UInt, UInt, Int, UInt, Int)
PFNGLTEXTURESTORAGE2DEXTPROC = C(None, UInt, UInt, Int, UInt, Int, Int)
PFNGLTEXTURESTORAGE3DEXTPROC = C(None, UInt, UInt, Int, UInt, Int, Int, Int)
PFNGLTEXTURESTORAGE2DMULTISAMPLEEXTPROC = C(
    None, UInt, UInt, Int, UInt, Int, Int, UByte
)
PFNGLTEXTURESTORAGE3DMULTISAMPLEEXTPROC = C(
    None, UInt, UInt, Int, UInt, Int, Int, Int, UByte
)
PFNGLVERTEXARRAYBINDVERTEXBUFFEREXTPROC = C(None, UInt, UInt, UInt, Size, Int)
PFNGLVERTEXARRAYVERTEXATTRIBFORMATEXTPROC = C(
    None, UInt, UInt, Int, UInt, UByte, UInt
)
PFNGLVERTEXARRAYVERTEXATTRIBIFORMATEXTPROC = C(
    None, UInt, UInt, Int, UInt, UInt
)
PFNGLVERTEXARRAYVERTEXATTRIBLFORMATEXTPROC = C(
    None, UInt, UInt, Int, UInt, UInt
)
PFNGLVERTEXARRAYVERTEXATTRIBBINDINGEXTPROC = C(None, UInt, UInt, UInt)
PFNGLVERTEXARRAYVERTEXBINDINGDIVISOREXTPROC = C(None, UInt, UInt, UInt)
PFNGLVERTEXARRAYVERTEXATTRIBLOFFSETEXTPROC = C(
    None, UInt, UInt, UInt, Int, UInt, Int, Size
)
PFNGLTEXTUREPAGECOMMITMENTEXTPROC = C(
    None, UInt, Int, Int, Int, Int, Int, Int, Int, UByte
)
PFNGLVERTEXARRAYVERTEXATTRIBDIVISOREXTPROC = C(None, UInt, UInt, UInt)
glMatrixLoadfEXT = GL('glMatrixLoadfEXT', None, UInt, P(Float))
glMatrixLoaddEXT = GL('glMatrixLoaddEXT', None, UInt, P(Double))
glMatrixMultfEXT = GL('glMatrixMultfEXT', None, UInt, P(Float))
glMatrixMultdEXT = GL('glMatrixMultdEXT', None, UInt, P(Double))
glMatrixLoadIdentityEXT = GL('glMatrixLoadIdentityEXT', None, UInt)
glMatrixRotatefEXT = GL(
    'glMatrixRotatefEXT', None, UInt, Float, Float, Float, Float
)
glMatrixRotatedEXT = GL(
    'glMatrixRotatedEXT', None, UInt, Double, Double, Double, Double
)
glMatrixScalefEXT = GL('glMatrixScalefEXT', None, UInt, Float, Float, Float)
glMatrixScaledEXT = GL(
    'glMatrixScaledEXT', None, UInt, Double, Double, Double
)
glMatrixTranslatefEXT = GL(
    'glMatrixTranslatefEXT', None, UInt, Float, Float, Float
)
glMatrixTranslatedEXT = GL(
    'glMatrixTranslatedEXT', None, UInt, Double, Double, Double
)
glMatrixFrustumEXT = GL(
    'glMatrixFrustumEXT', None, UInt, Double, Double, Double, Double, Double,
    Double
)
glMatrixOrthoEXT = GL(
    'glMatrixOrthoEXT', None, UInt, Double, Double, Double, Double, Double,
    Double
)
glMatrixPopEXT = GL('glMatrixPopEXT', None, UInt)
glMatrixPushEXT = GL('glMatrixPushEXT', None, UInt)
glClientAttribDefaultEXT = GL('glClientAttribDefaultEXT', None, UInt)
glPushClientAttribDefaultEXT = GL('glPushClientAttribDefaultEXT', None, UInt)
glTextureParameterfEXT = GL(
    'glTextureParameterfEXT', None, UInt, UInt, UInt, Float
)
glTextureParameterfvEXT = GL(
    'glTextureParameterfvEXT', None, UInt, UInt, UInt, P(Float)
)
glTextureParameteriEXT = GL(
    'glTextureParameteriEXT', None, UInt, UInt, UInt, Int
)
glTextureParameterivEXT = GL(
    'glTextureParameterivEXT', None, UInt, UInt, UInt, P(Int)
)
glTextureImage1DEXT = GL(
    'glTextureImage1DEXT', None, UInt, UInt, Int, Int, Int, Int, UInt, UInt,
    VoidP
)
glTextureImage2DEXT = GL(
    'glTextureImage2DEXT', None, UInt, UInt, Int, Int, Int, Int, Int, UInt,
    UInt, VoidP
)
glTextureSubImage1DEXT = GL(
    'glTextureSubImage1DEXT', None, UInt, UInt, Int, Int, Int, UInt, UInt,
    VoidP
)
glTextureSubImage2DEXT = GL(
    'glTextureSubImage2DEXT', None, UInt, UInt, Int, Int, Int, Int, Int, UInt,
    UInt, VoidP
)
glCopyTextureImage1DEXT = GL(
    'glCopyTextureImage1DEXT', None, UInt, UInt, Int, UInt, Int, Int, Int, Int
)
glCopyTextureImage2DEXT = GL(
    'glCopyTextureImage2DEXT', None, UInt, UInt, Int, UInt, Int, Int, Int,
    Int, Int
)
glCopyTextureSubImage1DEXT = GL(
    'glCopyTextureSubImage1DEXT', None, UInt, UInt, Int, Int, Int, Int, Int
)
glCopyTextureSubImage2DEXT = GL(
    'glCopyTextureSubImage2DEXT', None, UInt, UInt, Int, Int, Int, Int, Int,
    Int, Int
)
glGetTextureImageEXT = GL(
    'glGetTextureImageEXT', None, UInt, UInt, Int, UInt, UInt, VoidP
)
glGetTextureParameterfvEXT = GL(
    'glGetTextureParameterfvEXT', None, UInt, UInt, UInt, P(Float)
)
glGetTextureParameterivEXT = GL(
    'glGetTextureParameterivEXT', None, UInt, UInt, UInt, P(Int)
)
glGetTextureLevelParameterfvEXT = GL(
    'glGetTextureLevelParameterfvEXT', None, UInt, UInt, Int, UInt, P(Float)
)
glGetTextureLevelParameterivEXT = GL(
    'glGetTextureLevelParameterivEXT', None, UInt, UInt, Int, UInt, P(Int)
)
glTextureImage3DEXT = GL(
    'glTextureImage3DEXT', None, UInt, UInt, Int, Int, Int, Int, Int, Int,
    UInt, UInt, VoidP
)
glTextureSubImage3DEXT = GL(
    'glTextureSubImage3DEXT', None, UInt, UInt, Int, Int, Int, Int, Int, Int,
    Int, UInt, UInt, VoidP
)
glCopyTextureSubImage3DEXT = GL(
    'glCopyTextureSubImage3DEXT', None, UInt, UInt, Int, Int, Int, Int, Int,
    Int, Int, Int
)
glBindMultiTextureEXT = GL('glBindMultiTextureEXT', None, UInt, UInt, UInt)
glMultiTexCoordPointerEXT = GL(
    'glMultiTexCoordPointerEXT', None, UInt, Int, UInt, Int, VoidP
)
glMultiTexEnvfEXT = GL('glMultiTexEnvfEXT', None, UInt, UInt, UInt, Float)
glMultiTexEnvfvEXT = GL(
    'glMultiTexEnvfvEXT', None, UInt, UInt, UInt, P(Float)
)
glMultiTexEnviEXT = GL('glMultiTexEnviEXT', None, UInt, UInt, UInt, Int)
glMultiTexEnvivEXT = GL('glMultiTexEnvivEXT', None, UInt, UInt, UInt, P(Int))
glMultiTexGendEXT = GL('glMultiTexGendEXT', None, UInt, UInt, UInt, Double)
glMultiTexGendvEXT = GL(
    'glMultiTexGendvEXT', None, UInt, UInt, UInt, P(Double)
)
glMultiTexGenfEXT = GL('glMultiTexGenfEXT', None, UInt, UInt, UInt, Float)
glMultiTexGenfvEXT = GL(
    'glMultiTexGenfvEXT', None, UInt, UInt, UInt, P(Float)
)
glMultiTexGeniEXT = GL('glMultiTexGeniEXT', None, UInt, UInt, UInt, Int)
glMultiTexGenivEXT = GL('glMultiTexGenivEXT', None, UInt, UInt, UInt, P(Int))
glGetMultiTexEnvfvEXT = GL(
    'glGetMultiTexEnvfvEXT', None, UInt, UInt, UInt, P(Float)
)
glGetMultiTexEnvivEXT = GL(
    'glGetMultiTexEnvivEXT', None, UInt, UInt, UInt, P(Int)
)
glGetMultiTexGendvEXT = GL(
    'glGetMultiTexGendvEXT', None, UInt, UInt, UInt, P(Double)
)
glGetMultiTexGenfvEXT = GL(
    'glGetMultiTexGenfvEXT', None, UInt, UInt, UInt, P(Float)
)
glGetMultiTexGenivEXT = GL(
    'glGetMultiTexGenivEXT', None, UInt, UInt, UInt, P(Int)
)
glMultiTexParameteriEXT = GL(
    'glMultiTexParameteriEXT', None, UInt, UInt, UInt, Int
)
glMultiTexParameterivEXT = GL(
    'glMultiTexParameterivEXT', None, UInt, UInt, UInt, P(Int)
)
glMultiTexParameterfEXT = GL(
    'glMultiTexParameterfEXT', None, UInt, UInt, UInt, Float
)
glMultiTexParameterfvEXT = GL(
    'glMultiTexParameterfvEXT', None, UInt, UInt, UInt, P(Float)
)
glMultiTexImage1DEXT = GL(
    'glMultiTexImage1DEXT', None, UInt, UInt, Int, Int, Int, Int, UInt, UInt,
    VoidP
)
glMultiTexImage2DEXT = GL(
    'glMultiTexImage2DEXT', None, UInt, UInt, Int, Int, Int, Int, Int, UInt,
    UInt, VoidP
)
glMultiTexSubImage1DEXT = GL(
    'glMultiTexSubImage1DEXT', None, UInt, UInt, Int, Int, Int, UInt, UInt,
    VoidP
)
glMultiTexSubImage2DEXT = GL(
    'glMultiTexSubImage2DEXT', None, UInt, UInt, Int, Int, Int, Int, Int,
    UInt, UInt, VoidP
)
glCopyMultiTexImage1DEXT = GL(
    'glCopyMultiTexImage1DEXT', None, UInt, UInt, Int, UInt, Int, Int, Int,
    Int
)
glCopyMultiTexImage2DEXT = GL(
    'glCopyMultiTexImage2DEXT', None, UInt, UInt, Int, UInt, Int, Int, Int,
    Int, Int
)
glCopyMultiTexSubImage1DEXT = GL(
    'glCopyMultiTexSubImage1DEXT', None, UInt, UInt, Int, Int, Int, Int, Int
)
glCopyMultiTexSubImage2DEXT = GL(
    'glCopyMultiTexSubImage2DEXT', None, UInt, UInt, Int, Int, Int, Int, Int,
    Int, Int
)
glGetMultiTexImageEXT = GL(
    'glGetMultiTexImageEXT', None, UInt, UInt, Int, UInt, UInt, VoidP
)
glGetMultiTexParameterfvEXT = GL(
    'glGetMultiTexParameterfvEXT', None, UInt, UInt, UInt, P(Float)
)
glGetMultiTexParameterivEXT = GL(
    'glGetMultiTexParameterivEXT', None, UInt, UInt, UInt, P(Int)
)
glGetMultiTexLevelParameterfvEXT = GL(
    'glGetMultiTexLevelParameterfvEXT', None, UInt, UInt, Int, UInt, P(Float)
)
glGetMultiTexLevelParameterivEXT = GL(
    'glGetMultiTexLevelParameterivEXT', None, UInt, UInt, Int, UInt, P(Int)
)
glMultiTexImage3DEXT = GL(
    'glMultiTexImage3DEXT', None, UInt, UInt, Int, Int, Int, Int, Int, Int,
    UInt, UInt, VoidP
)
glMultiTexSubImage3DEXT = GL(
    'glMultiTexSubImage3DEXT', None, UInt, UInt, Int, Int, Int, Int, Int, Int,
    Int, UInt, UInt, VoidP
)
glCopyMultiTexSubImage3DEXT = GL(
    'glCopyMultiTexSubImage3DEXT', None, UInt, UInt, Int, Int, Int, Int, Int,
    Int, Int, Int
)
glEnableClientStateIndexedEXT = GL(
    'glEnableClientStateIndexedEXT', None, UInt, UInt
)
glDisableClientStateIndexedEXT = GL(
    'glDisableClientStateIndexedEXT', None, UInt, UInt
)
glGetFloatIndexedvEXT = GL(
    'glGetFloatIndexedvEXT', None, UInt, UInt, P(Float)
)
glGetDoubleIndexedvEXT = GL(
    'glGetDoubleIndexedvEXT', None, UInt, UInt, P(Double)
)
glGetPointerIndexedvEXT = GL(
    'glGetPointerIndexedvEXT', None, UInt, UInt, P(VoidP)
)
glEnableIndexedEXT = GL('glEnableIndexedEXT', None, UInt, UInt)
glDisableIndexedEXT = GL('glDisableIndexedEXT', None, UInt, UInt)
glIsEnabledIndexedEXT = GL('glIsEnabledIndexedEXT', UByte, UInt, UInt)
glGetIntegerIndexedvEXT = GL(
    'glGetIntegerIndexedvEXT', None, UInt, UInt, P(Int)
)
glGetBooleanIndexedvEXT = GL(
    'glGetBooleanIndexedvEXT', None, UInt, UInt, P(UByte)
)
glCompressedTextureImage3DEXT = GL(
    'glCompressedTextureImage3DEXT', None, UInt, UInt, Int, UInt, Int, Int,
    Int, Int, Int, VoidP
)
glCompressedTextureImage2DEXT = GL(
    'glCompressedTextureImage2DEXT', None, UInt, UInt, Int, UInt, Int, Int,
    Int, Int, VoidP
)
glCompressedTextureImage1DEXT = GL(
    'glCompressedTextureImage1DEXT', None, UInt, UInt, Int, UInt, Int, Int,
    Int, VoidP
)
glCompressedTextureSubImage3DEXT = GL(
    'glCompressedTextureSubImage3DEXT', None, UInt, UInt, Int, Int, Int, Int,
    Int, Int, Int, UInt, Int, VoidP
)
glCompressedTextureSubImage2DEXT = GL(
    'glCompressedTextureSubImage2DEXT', None, UInt, UInt, Int, Int, Int, Int,
    Int, UInt, Int, VoidP
)
glCompressedTextureSubImage1DEXT = GL(
    'glCompressedTextureSubImage1DEXT', None, UInt, UInt, Int, Int, Int, UInt,
    Int, VoidP
)
glGetCompressedTextureImageEXT = GL(
    'glGetCompressedTextureImageEXT', None, UInt, UInt, Int, VoidP
)
glCompressedMultiTexImage3DEXT = GL(
    'glCompressedMultiTexImage3DEXT', None, UInt, UInt, Int, UInt, Int, Int,
    Int, Int, Int, VoidP
)
glCompressedMultiTexImage2DEXT = GL(
    'glCompressedMultiTexImage2DEXT', None, UInt, UInt, Int, UInt, Int, Int,
    Int, Int, VoidP
)
glCompressedMultiTexImage1DEXT = GL(
    'glCompressedMultiTexImage1DEXT', None, UInt, UInt, Int, UInt, Int, Int,
    Int, VoidP
)
glCompressedMultiTexSubImage3DEXT = GL(
    'glCompressedMultiTexSubImage3DEXT', None, UInt, UInt, Int, Int, Int, Int,
    Int, Int, Int, UInt, Int, VoidP
)
glCompressedMultiTexSubImage2DEXT = GL(
    'glCompressedMultiTexSubImage2DEXT', None, UInt, UInt, Int, Int, Int, Int,
    Int, UInt, Int, VoidP
)
glCompressedMultiTexSubImage1DEXT = GL(
    'glCompressedMultiTexSubImage1DEXT', None, UInt, UInt, Int, Int, Int,
    UInt, Int, VoidP
)
glGetCompressedMultiTexImageEXT = GL(
    'glGetCompressedMultiTexImageEXT', None, UInt, UInt, Int, VoidP
)
glMatrixLoadTransposefEXT = GL(
    'glMatrixLoadTransposefEXT', None, UInt, P(Float)
)
glMatrixLoadTransposedEXT = GL(
    'glMatrixLoadTransposedEXT', None, UInt, P(Double)
)
glMatrixMultTransposefEXT = GL(
    'glMatrixMultTransposefEXT', None, UInt, P(Float)
)
glMatrixMultTransposedEXT = GL(
    'glMatrixMultTransposedEXT', None, UInt, P(Double)
)
glNamedBufferDataEXT = GL(
    'glNamedBufferDataEXT', None, UInt, Size, VoidP, UInt
)
glNamedBufferSubDataEXT = GL(
    'glNamedBufferSubDataEXT', None, UInt, Size, Size, VoidP
)
glMapNamedBufferEXT = GL('glMapNamedBufferEXT', VoidP, UInt, UInt)
glUnmapNamedBufferEXT = GL('glUnmapNamedBufferEXT', UByte, UInt)
glGetNamedBufferParameterivEXT = GL(
    'glGetNamedBufferParameterivEXT', None, UInt, UInt, P(Int)
)
glGetNamedBufferPointervEXT = GL(
    'glGetNamedBufferPointervEXT', None, UInt, UInt, P(VoidP)
)
glGetNamedBufferSubDataEXT = GL(
    'glGetNamedBufferSubDataEXT', None, UInt, Size, Size, VoidP
)
glProgramUniform1fEXT = GL('glProgramUniform1fEXT', None, UInt, Int, Float)
glProgramUniform2fEXT = GL(
    'glProgramUniform2fEXT', None, UInt, Int, Float, Float
)
glProgramUniform3fEXT = GL(
    'glProgramUniform3fEXT', None, UInt, Int, Float, Float, Float
)
glProgramUniform4fEXT = GL(
    'glProgramUniform4fEXT', None, UInt, Int, Float, Float, Float, Float
)
glProgramUniform1iEXT = GL('glProgramUniform1iEXT', None, UInt, Int, Int)
glProgramUniform2iEXT = GL('glProgramUniform2iEXT', None, UInt, Int, Int, Int)
glProgramUniform3iEXT = GL(
    'glProgramUniform3iEXT', None, UInt, Int, Int, Int, Int
)
glProgramUniform4iEXT = GL(
    'glProgramUniform4iEXT', None, UInt, Int, Int, Int, Int, Int
)
glProgramUniform1fvEXT = GL(
    'glProgramUniform1fvEXT', None, UInt, Int, Int, P(Float)
)
glProgramUniform2fvEXT = GL(
    'glProgramUniform2fvEXT', None, UInt, Int, Int, P(Float)
)
glProgramUniform3fvEXT = GL(
    'glProgramUniform3fvEXT', None, UInt, Int, Int, P(Float)
)
glProgramUniform4fvEXT = GL(
    'glProgramUniform4fvEXT', None, UInt, Int, Int, P(Float)
)
glProgramUniform1ivEXT = GL(
    'glProgramUniform1ivEXT', None, UInt, Int, Int, P(Int)
)
glProgramUniform2ivEXT = GL(
    'glProgramUniform2ivEXT', None, UInt, Int, Int, P(Int)
)
glProgramUniform3ivEXT = GL(
    'glProgramUniform3ivEXT', None, UInt, Int, Int, P(Int)
)
glProgramUniform4ivEXT = GL(
    'glProgramUniform4ivEXT', None, UInt, Int, Int, P(Int)
)
glProgramUniformMatrix2fvEXT = GL(
    'glProgramUniformMatrix2fvEXT', None, UInt, Int, Int, UByte, P(Float)
)
glProgramUniformMatrix3fvEXT = GL(
    'glProgramUniformMatrix3fvEXT', None, UInt, Int, Int, UByte, P(Float)
)
glProgramUniformMatrix4fvEXT = GL(
    'glProgramUniformMatrix4fvEXT', None, UInt, Int, Int, UByte, P(Float)
)
glProgramUniformMatrix2x3fvEXT = GL(
    'glProgramUniformMatrix2x3fvEXT', None, UInt, Int, Int, UByte, P(Float)
)
glProgramUniformMatrix3x2fvEXT = GL(
    'glProgramUniformMatrix3x2fvEXT', None, UInt, Int, Int, UByte, P(Float)
)
glProgramUniformMatrix2x4fvEXT = GL(
    'glProgramUniformMatrix2x4fvEXT', None, UInt, Int, Int, UByte, P(Float)
)
glProgramUniformMatrix4x2fvEXT = GL(
    'glProgramUniformMatrix4x2fvEXT', None, UInt, Int, Int, UByte, P(Float)
)
glProgramUniformMatrix3x4fvEXT = GL(
    'glProgramUniformMatrix3x4fvEXT', None, UInt, Int, Int, UByte, P(Float)
)
glProgramUniformMatrix4x3fvEXT = GL(
    'glProgramUniformMatrix4x3fvEXT', None, UInt, Int, Int, UByte, P(Float)
)
glTextureBufferEXT = GL('glTextureBufferEXT', None, UInt, UInt, UInt, UInt)
glMultiTexBufferEXT = GL('glMultiTexBufferEXT', None, UInt, UInt, UInt, UInt)
glTextureParameterIivEXT = GL(
    'glTextureParameterIivEXT', None, UInt, UInt, UInt, P(Int)
)
glTextureParameterIuivEXT = GL(
    'glTextureParameterIuivEXT', None, UInt, UInt, UInt, P(UInt)
)
glGetTextureParameterIivEXT = GL(
    'glGetTextureParameterIivEXT', None, UInt, UInt, UInt, P(Int)
)
glGetTextureParameterIuivEXT = GL(
    'glGetTextureParameterIuivEXT', None, UInt, UInt, UInt, P(UInt)
)
glMultiTexParameterIivEXT = GL(
    'glMultiTexParameterIivEXT', None, UInt, UInt, UInt, P(Int)
)
glMultiTexParameterIuivEXT = GL(
    'glMultiTexParameterIuivEXT', None, UInt, UInt, UInt, P(UInt)
)
glGetMultiTexParameterIivEXT = GL(
    'glGetMultiTexParameterIivEXT', None, UInt, UInt, UInt, P(Int)
)
glGetMultiTexParameterIuivEXT = GL(
    'glGetMultiTexParameterIuivEXT', None, UInt, UInt, UInt, P(UInt)
)
glProgramUniform1uiEXT = GL('glProgramUniform1uiEXT', None, UInt, Int, UInt)
glProgramUniform2uiEXT = GL(
    'glProgramUniform2uiEXT', None, UInt, Int, UInt, UInt
)
glProgramUniform3uiEXT = GL(
    'glProgramUniform3uiEXT', None, UInt, Int, UInt, UInt, UInt
)
glProgramUniform4uiEXT = GL(
    'glProgramUniform4uiEXT', None, UInt, Int, UInt, UInt, UInt, UInt
)
glProgramUniform1uivEXT = GL(
    'glProgramUniform1uivEXT', None, UInt, Int, Int, P(UInt)
)
glProgramUniform2uivEXT = GL(
    'glProgramUniform2uivEXT', None, UInt, Int, Int, P(UInt)
)
glProgramUniform3uivEXT = GL(
    'glProgramUniform3uivEXT', None, UInt, Int, Int, P(UInt)
)
glProgramUniform4uivEXT = GL(
    'glProgramUniform4uivEXT', None, UInt, Int, Int, P(UInt)
)
glNamedProgramLocalParameters4fvEXT = GL(
    'glNamedProgramLocalParameters4fvEXT', None, UInt, UInt, UInt, Int,
    P(Float)
)
glNamedProgramLocalParameterI4iEXT = GL(
    'glNamedProgramLocalParameterI4iEXT', None, UInt, UInt, UInt, Int, Int,
    Int, Int
)
glNamedProgramLocalParameterI4ivEXT = GL(
    'glNamedProgramLocalParameterI4ivEXT', None, UInt, UInt, UInt, P(Int)
)
glNamedProgramLocalParametersI4ivEXT = GL(
    'glNamedProgramLocalParametersI4ivEXT', None, UInt, UInt, UInt, Int,
    P(Int)
)
glNamedProgramLocalParameterI4uiEXT = GL(
    'glNamedProgramLocalParameterI4uiEXT', None, UInt, UInt, UInt, UInt, UInt,
    UInt, UInt
)
glNamedProgramLocalParameterI4uivEXT = GL(
    'glNamedProgramLocalParameterI4uivEXT', None, UInt, UInt, UInt, P(UInt)
)
glNamedProgramLocalParametersI4uivEXT = GL(
    'glNamedProgramLocalParametersI4uivEXT', None, UInt, UInt, UInt, Int,
    P(UInt)
)
glGetNamedProgramLocalParameterIivEXT = GL(
    'glGetNamedProgramLocalParameterIivEXT', None, UInt, UInt, UInt, P(Int)
)
glGetNamedProgramLocalParameterIuivEXT = GL(
    'glGetNamedProgramLocalParameterIuivEXT', None, UInt, UInt, UInt, P(UInt)
)
glEnableClientStateiEXT = GL('glEnableClientStateiEXT', None, UInt, UInt)
glDisableClientStateiEXT = GL('glDisableClientStateiEXT', None, UInt, UInt)
glGetFloati_vEXT = GL('glGetFloati_vEXT', None, UInt, UInt, P(Float))
glGetDoublei_vEXT = GL('glGetDoublei_vEXT', None, UInt, UInt, P(Double))
glGetPointeri_vEXT = GL('glGetPointeri_vEXT', None, UInt, UInt, P(VoidP))
glNamedProgramStringEXT = GL(
    'glNamedProgramStringEXT', None, UInt, UInt, UInt, Int, VoidP
)
glNamedProgramLocalParameter4dEXT = GL(
    'glNamedProgramLocalParameter4dEXT', None, UInt, UInt, UInt, Double,
    Double, Double, Double
)
glNamedProgramLocalParameter4dvEXT = GL(
    'glNamedProgramLocalParameter4dvEXT', None, UInt, UInt, UInt, P(Double)
)
glNamedProgramLocalParameter4fEXT = GL(
    'glNamedProgramLocalParameter4fEXT', None, UInt, UInt, UInt, Float, Float,
    Float, Float
)
glNamedProgramLocalParameter4fvEXT = GL(
    'glNamedProgramLocalParameter4fvEXT', None, UInt, UInt, UInt, P(Float)
)
glGetNamedProgramLocalParameterdvEXT = GL(
    'glGetNamedProgramLocalParameterdvEXT', None, UInt, UInt, UInt, P(Double)
)
glGetNamedProgramLocalParameterfvEXT = GL(
    'glGetNamedProgramLocalParameterfvEXT', None, UInt, UInt, UInt, P(Float)
)
glGetNamedProgramivEXT = GL(
    'glGetNamedProgramivEXT', None, UInt, UInt, UInt, P(Int)
)
glGetNamedProgramStringEXT = GL(
    'glGetNamedProgramStringEXT', None, UInt, UInt, UInt, VoidP
)
glNamedRenderbufferStorageEXT = GL(
    'glNamedRenderbufferStorageEXT', None, UInt, UInt, Int, Int
)
glGetNamedRenderbufferParameterivEXT = GL(
    'glGetNamedRenderbufferParameterivEXT', None, UInt, UInt, P(Int)
)
glNamedRenderbufferStorageMultisampleEXT = GL(
    'glNamedRenderbufferStorageMultisampleEXT', None, UInt, Int, UInt, Int,
    Int
)
glNamedRenderbufferStorageMultisampleCoverageEXT = GL(
    'glNamedRenderbufferStorageMultisampleCoverageEXT', None, UInt, Int, Int,
    UInt, Int, Int
)
glCheckNamedFramebufferStatusEXT = GL(
    'glCheckNamedFramebufferStatusEXT', UInt, UInt, UInt
)
glNamedFramebufferTexture1DEXT = GL(
    'glNamedFramebufferTexture1DEXT', None, UInt, UInt, UInt, UInt, Int
)
glNamedFramebufferTexture2DEXT = GL(
    'glNamedFramebufferTexture2DEXT', None, UInt, UInt, UInt, UInt, Int
)
glNamedFramebufferTexture3DEXT = GL(
    'glNamedFramebufferTexture3DEXT', None, UInt, UInt, UInt, UInt, Int, Int
)
glNamedFramebufferRenderbufferEXT = GL(
    'glNamedFramebufferRenderbufferEXT', None, UInt, UInt, UInt, UInt
)
glGetNamedFramebufferAttachmentParameterivEXT = GL(
    'glGetNamedFramebufferAttachmentParameterivEXT', None, UInt, UInt, UInt,
    P(Int)
)
glGenerateTextureMipmapEXT = GL(
    'glGenerateTextureMipmapEXT', None, UInt, UInt
)
glGenerateMultiTexMipmapEXT = GL(
    'glGenerateMultiTexMipmapEXT', None, UInt, UInt
)
glFramebufferDrawBufferEXT = GL(
    'glFramebufferDrawBufferEXT', None, UInt, UInt
)
glFramebufferDrawBuffersEXT = GL(
    'glFramebufferDrawBuffersEXT', None, UInt, Int, P(UInt)
)
glFramebufferReadBufferEXT = GL(
    'glFramebufferReadBufferEXT', None, UInt, UInt
)
glGetFramebufferParameterivEXT = GL(
    'glGetFramebufferParameterivEXT', None, UInt, UInt, P(Int)
)
glNamedCopyBufferSubDataEXT = GL(
    'glNamedCopyBufferSubDataEXT', None, UInt, UInt, Size, Size, Size
)
glNamedFramebufferTextureEXT = GL(
    'glNamedFramebufferTextureEXT', None, UInt, UInt, UInt, Int
)
glNamedFramebufferTextureLayerEXT = GL(
    'glNamedFramebufferTextureLayerEXT', None, UInt, UInt, UInt, Int, Int
)
glNamedFramebufferTextureFaceEXT = GL(
    'glNamedFramebufferTextureFaceEXT', None, UInt, UInt, UInt, Int, UInt
)
glTextureRenderbufferEXT = GL(
    'glTextureRenderbufferEXT', None, UInt, UInt, UInt
)
glMultiTexRenderbufferEXT = GL(
    'glMultiTexRenderbufferEXT', None, UInt, UInt, UInt
)
glVertexArrayVertexOffsetEXT = GL(
    'glVertexArrayVertexOffsetEXT', None, UInt, UInt, Int, UInt, Int, Size
)
glVertexArrayColorOffsetEXT = GL(
    'glVertexArrayColorOffsetEXT', None, UInt, UInt, Int, UInt, Int, Size
)
glVertexArrayEdgeFlagOffsetEXT = GL(
    'glVertexArrayEdgeFlagOffsetEXT', None, UInt, UInt, Int, Size
)
glVertexArrayIndexOffsetEXT = GL(
    'glVertexArrayIndexOffsetEXT', None, UInt, UInt, UInt, Int, Size
)
glVertexArrayNormalOffsetEXT = GL(
    'glVertexArrayNormalOffsetEXT', None, UInt, UInt, UInt, Int, Size
)
glVertexArrayTexCoordOffsetEXT = GL(
    'glVertexArrayTexCoordOffsetEXT', None, UInt, UInt, Int, UInt, Int, Size
)
glVertexArrayMultiTexCoordOffsetEXT = GL(
    'glVertexArrayMultiTexCoordOffsetEXT', None, UInt, UInt, UInt, Int, UInt,
    Int, Size
)
glVertexArrayFogCoordOffsetEXT = GL(
    'glVertexArrayFogCoordOffsetEXT', None, UInt, UInt, UInt, Int, Size
)
glVertexArraySecondaryColorOffsetEXT = GL(
    'glVertexArraySecondaryColorOffsetEXT', None, UInt, UInt, Int, UInt, Int,
    Size
)
glVertexArrayVertexAttribOffsetEXT = GL(
    'glVertexArrayVertexAttribOffsetEXT', None, UInt, UInt, UInt, Int, UInt,
    UByte, Int, Size
)
glVertexArrayVertexAttribIOffsetEXT = GL(
    'glVertexArrayVertexAttribIOffsetEXT', None, UInt, UInt, UInt, Int, UInt,
    Int, Size
)
glEnableVertexArrayEXT = GL('glEnableVertexArrayEXT', None, UInt, UInt)
glDisableVertexArrayEXT = GL('glDisableVertexArrayEXT', None, UInt, UInt)
glEnableVertexArrayAttribEXT = GL(
    'glEnableVertexArrayAttribEXT', None, UInt, UInt
)
glDisableVertexArrayAttribEXT = GL(
    'glDisableVertexArrayAttribEXT', None, UInt, UInt
)
glGetVertexArrayIntegervEXT = GL(
    'glGetVertexArrayIntegervEXT', None, UInt, UInt, P(Int)
)
glGetVertexArrayPointervEXT = GL(
    'glGetVertexArrayPointervEXT', None, UInt, UInt, P(VoidP)
)
glGetVertexArrayIntegeri_vEXT = GL(
    'glGetVertexArrayIntegeri_vEXT', None, UInt, UInt, UInt, P(Int)
)
glGetVertexArrayPointeri_vEXT = GL(
    'glGetVertexArrayPointeri_vEXT', None, UInt, UInt, UInt, P(VoidP)
)
glMapNamedBufferRangeEXT = GL(
    'glMapNamedBufferRangeEXT', VoidP, UInt, Size, Size, UInt
)
glFlushMappedNamedBufferRangeEXT = GL(
    'glFlushMappedNamedBufferRangeEXT', None, UInt, Size, Size
)
glNamedBufferStorageEXT = GL(
    'glNamedBufferStorageEXT', None, UInt, Size, VoidP, UInt
)
glClearNamedBufferDataEXT = GL(
    'glClearNamedBufferDataEXT', None, UInt, UInt, UInt, UInt, VoidP
)
glClearNamedBufferSubDataEXT = GL(
    'glClearNamedBufferSubDataEXT', None, UInt, UInt, Size, Size, UInt, UInt,
    VoidP
)
glNamedFramebufferParameteriEXT = GL(
    'glNamedFramebufferParameteriEXT', None, UInt, UInt, Int
)
glGetNamedFramebufferParameterivEXT = GL(
    'glGetNamedFramebufferParameterivEXT', None, UInt, UInt, P(Int)
)
glProgramUniform1dEXT = GL('glProgramUniform1dEXT', None, UInt, Int, Double)
glProgramUniform2dEXT = GL(
    'glProgramUniform2dEXT', None, UInt, Int, Double, Double
)
glProgramUniform3dEXT = GL(
    'glProgramUniform3dEXT', None, UInt, Int, Double, Double, Double
)
glProgramUniform4dEXT = GL(
    'glProgramUniform4dEXT', None, UInt, Int, Double, Double, Double, Double
)
glProgramUniform1dvEXT = GL(
    'glProgramUniform1dvEXT', None, UInt, Int, Int, P(Double)
)
glProgramUniform2dvEXT = GL(
    'glProgramUniform2dvEXT', None, UInt, Int, Int, P(Double)
)
glProgramUniform3dvEXT = GL(
    'glProgramUniform3dvEXT', None, UInt, Int, Int, P(Double)
)
glProgramUniform4dvEXT = GL(
    'glProgramUniform4dvEXT', None, UInt, Int, Int, P(Double)
)
glProgramUniformMatrix2dvEXT = GL(
    'glProgramUniformMatrix2dvEXT', None, UInt, Int, Int, UByte, P(Double)
)
glProgramUniformMatrix3dvEXT = GL(
    'glProgramUniformMatrix3dvEXT', None, UInt, Int, Int, UByte, P(Double)
)
glProgramUniformMatrix4dvEXT = GL(
    'glProgramUniformMatrix4dvEXT', None, UInt, Int, Int, UByte, P(Double)
)
glProgramUniformMatrix2x3dvEXT = GL(
    'glProgramUniformMatrix2x3dvEXT', None, UInt, Int, Int, UByte, P(Double)
)
glProgramUniformMatrix2x4dvEXT = GL(
    'glProgramUniformMatrix2x4dvEXT', None, UInt, Int, Int, UByte, P(Double)
)
glProgramUniformMatrix3x2dvEXT = GL(
    'glProgramUniformMatrix3x2dvEXT', None, UInt, Int, Int, UByte, P(Double)
)
glProgramUniformMatrix3x4dvEXT = GL(
    'glProgramUniformMatrix3x4dvEXT', None, UInt, Int, Int, UByte, P(Double)
)
glProgramUniformMatrix4x2dvEXT = GL(
    'glProgramUniformMatrix4x2dvEXT', None, UInt, Int, Int, UByte, P(Double)
)
glProgramUniformMatrix4x3dvEXT = GL(
    'glProgramUniformMatrix4x3dvEXT', None, UInt, Int, Int, UByte, P(Double)
)
glTextureBufferRangeEXT = GL(
    'glTextureBufferRangeEXT', None, UInt, UInt, UInt, UInt, Size, Size
)
glTextureStorage1DEXT = GL(
    'glTextureStorage1DEXT', None, UInt, UInt, Int, UInt, Int
)
glTextureStorage2DEXT = GL(
    'glTextureStorage2DEXT', None, UInt, UInt, Int, UInt, Int, Int
)
glTextureStorage3DEXT = GL(
    'glTextureStorage3DEXT', None, UInt, UInt, Int, UInt, Int, Int, Int
)
glTextureStorage2DMultisampleEXT = GL(
    'glTextureStorage2DMultisampleEXT', None, UInt, UInt, Int, UInt, Int, Int,
    UByte
)
glTextureStorage3DMultisampleEXT = GL(
    'glTextureStorage3DMultisampleEXT', None, UInt, UInt, Int, UInt, Int, Int,
    Int, UByte
)
glVertexArrayBindVertexBufferEXT = GL(
    'glVertexArrayBindVertexBufferEXT', None, UInt, UInt, UInt, Size, Int
)
glVertexArrayVertexAttribFormatEXT = GL(
    'glVertexArrayVertexAttribFormatEXT', None, UInt, UInt, Int, UInt, UByte,
    UInt
)
glVertexArrayVertexAttribIFormatEXT = GL(
    'glVertexArrayVertexAttribIFormatEXT', None, UInt, UInt, Int, UInt, UInt
)
glVertexArrayVertexAttribLFormatEXT = GL(
    'glVertexArrayVertexAttribLFormatEXT', None, UInt, UInt, Int, UInt, UInt
)
glVertexArrayVertexAttribBindingEXT = GL(
    'glVertexArrayVertexAttribBindingEXT', None, UInt, UInt, UInt
)
glVertexArrayVertexBindingDivisorEXT = GL(
    'glVertexArrayVertexBindingDivisorEXT', None, UInt, UInt, UInt
)
glVertexArrayVertexAttribLOffsetEXT = GL(
    'glVertexArrayVertexAttribLOffsetEXT', None, UInt, UInt, UInt, Int, UInt,
    Int, Size
)
glTexturePageCommitmentEXT = GL(
    'glTexturePageCommitmentEXT', None, UInt, Int, Int, Int, Int, Int, Int,
    Int, UByte
)
glVertexArrayVertexAttribDivisorEXT = GL(
    'glVertexArrayVertexAttribDivisorEXT', None, UInt, UInt, UInt
)
GL_EXT_draw_instanced = 1
PFNGLDRAWARRAYSINSTANCEDEXTPROC = C(None, UInt, Int, Int, Int)
PFNGLDRAWELEMENTSINSTANCEDEXTPROC = C(None, UInt, Int, UInt, VoidP, Int)
glDrawArraysInstancedEXT = GL(
    'glDrawArraysInstancedEXT', None, UInt, Int, Int, Int
)
glDrawElementsInstancedEXT = GL(
    'glDrawElementsInstancedEXT', None, UInt, Int, UInt, VoidP, Int
)
GL_EXT_multiview_tessellation_geometry_shader = 1
GL_EXT_multiview_texture_multisample = 1
GL_EXT_multiview_timer_query = 1
GL_EXT_polygon_offset_clamp = 1
GL_POLYGON_OFFSET_CLAMP_EXT = 0x8E1B
PFNGLPOLYGONOFFSETCLAMPEXTPROC = C(None, Float, Float, Float)
glPolygonOffsetClampEXT = GL(
    'glPolygonOffsetClampEXT', None, Float, Float, Float
)
GL_EXT_post_depth_coverage = 1
GL_EXT_raster_multisample = 1
GL_RASTER_MULTISAMPLE_EXT = 0x9327
GL_RASTER_SAMPLES_EXT = 0x9328
GL_MAX_RASTER_SAMPLES_EXT = 0x9329
GL_RASTER_FIXED_SAMPLE_LOCATIONS_EXT = 0x932A
GL_MULTISAMPLE_RASTERIZATION_ALLOWED_EXT = 0x932B
GL_EFFECTIVE_RASTER_SAMPLES_EXT = 0x932C
PFNGLRASTERSAMPLESEXTPROC = C(None, UInt, UByte)
glRasterSamplesEXT = GL('glRasterSamplesEXT', None, UInt, UByte)
GL_EXT_separate_shader_objects = 1
GL_ACTIVE_PROGRAM_EXT = 0x8B8D
PFNGLUSESHADERPROGRAMEXTPROC = C(None, UInt, UInt)
PFNGLACTIVEPROGRAMEXTPROC = C(None, UInt)
PFNGLCREATESHADERPROGRAMEXTPROC = C(UInt, UInt, CharP)
glUseShaderProgramEXT = GL('glUseShaderProgramEXT', None, UInt, UInt)
glActiveProgramEXT = GL('glActiveProgramEXT', None, UInt)
glCreateShaderProgramEXT = GL('glCreateShaderProgramEXT', UInt, UInt, CharP)
GL_EXT_shader_framebuffer_fetch = 1
GL_FRAGMENT_SHADER_DISCARDS_SAMPLES_EXT = 0x8A52
GL_EXT_shader_framebuffer_fetch_non_coherent = 1
PFNGLFRAMEBUFFERFETCHBARRIEREXTPROC = C(None)
glFramebufferFetchBarrierEXT = GL('glFramebufferFetchBarrierEXT', None)
GL_EXT_shader_integer_mix = 1
GL_EXT_texture_compression_s3tc = 1
GL_COMPRESSED_RGB_S3TC_DXT1_EXT = 0x83F0
GL_COMPRESSED_RGBA_S3TC_DXT1_EXT = 0x83F1
GL_COMPRESSED_RGBA_S3TC_DXT3_EXT = 0x83F2
GL_COMPRESSED_RGBA_S3TC_DXT5_EXT = 0x83F3
GL_EXT_texture_filter_minmax = 1
GL_TEXTURE_REDUCTION_MODE_EXT = 0x9366
GL_WEIGHTED_AVERAGE_EXT = 0x9367
GL_EXT_texture_sRGB_R8 = 1
GL_SR8_EXT = 0x8FBD
GL_EXT_texture_sRGB_RG8 = 1
GL_SRG8_EXT = 0x8FBE
GL_EXT_texture_sRGB_decode = 1
GL_TEXTURE_SRGB_DECODE_EXT = 0x8A48
GL_DECODE_EXT = 0x8A49
GL_SKIP_DECODE_EXT = 0x8A4A
GL_EXT_texture_shadow_lod = 1
GL_EXT_texture_storage = 1
GL_TEXTURE_IMMUTABLE_FORMAT_EXT = 0x912F
GL_ALPHA8_EXT = 0x803C
GL_LUMINANCE8_EXT = 0x8040
GL_LUMINANCE8_ALPHA8_EXT = 0x8045
GL_RGBA32F_EXT = 0x8814
GL_RGB32F_EXT = 0x8815
GL_ALPHA32F_EXT = 0x8816
GL_LUMINANCE32F_EXT = 0x8818
GL_LUMINANCE_ALPHA32F_EXT = 0x8819
GL_RGBA16F_EXT = 0x881A
GL_RGB16F_EXT = 0x881B
GL_ALPHA16F_EXT = 0x881C
GL_LUMINANCE16F_EXT = 0x881E
GL_LUMINANCE_ALPHA16F_EXT = 0x881F
GL_RGB10_A2_EXT = 0x8059
GL_RGB10_EXT = 0x8052
GL_BGRA8_EXT = 0x93A1
GL_R8_EXT = 0x8229
GL_RG8_EXT = 0x822B
GL_R32F_EXT = 0x822E
GL_RG32F_EXT = 0x8230
GL_R16F_EXT = 0x822D
GL_RG16F_EXT = 0x822F
PFNGLTEXSTORAGE1DEXTPROC = C(None, UInt, Int, UInt, Int)
PFNGLTEXSTORAGE2DEXTPROC = C(None, UInt, Int, UInt, Int, Int)
PFNGLTEXSTORAGE3DEXTPROC = C(None, UInt, Int, UInt, Int, Int, Int)
glTexStorage1DEXT = GL('glTexStorage1DEXT', None, UInt, Int, UInt, Int)
glTexStorage2DEXT = GL('glTexStorage2DEXT', None, UInt, Int, UInt, Int, Int)
glTexStorage3DEXT = GL(
    'glTexStorage3DEXT', None, UInt, Int, UInt, Int, Int, Int
)
GL_EXT_window_rectangles = 1
GL_INCLUSIVE_EXT = 0x8F10
GL_EXCLUSIVE_EXT = 0x8F11
GL_WINDOW_RECTANGLE_EXT = 0x8F12
GL_WINDOW_RECTANGLE_MODE_EXT = 0x8F13
GL_MAX_WINDOW_RECTANGLES_EXT = 0x8F14
GL_NUM_WINDOW_RECTANGLES_EXT = 0x8F15
PFNGLWINDOWRECTANGLESEXTPROC = C(None, UInt, Int, P(Int))
glWindowRectanglesEXT = GL('glWindowRectanglesEXT', None, UInt, Int, P(Int))

__all__ = [
    'GL_EXT_EGL_image_storage', 'PFNGLEGLIMAGETARGETTEXSTORAGEEXTPROC',
    'PFNGLEGLIMAGETARGETTEXTURESTORAGEEXTPROC',
    'glEGLImageTargetTexStorageEXT', 'glEGLImageTargetTextureStorageEXT',
    'GL_EXT_EGL_sync', 'GL_EXT_debug_label', 'GL_PROGRAM_PIPELINE_OBJECT_EXT',
    'GL_PROGRAM_OBJECT_EXT', 'GL_SHADER_OBJECT_EXT', 'GL_BUFFER_OBJECT_EXT',
    'GL_QUERY_OBJECT_EXT', 'GL_VERTEX_ARRAY_OBJECT_EXT',
    'PFNGLLABELOBJECTEXTPROC', 'PFNGLGETOBJECTLABELEXTPROC',
    'glLabelObjectEXT', 'glGetObjectLabelEXT', 'GL_EXT_debug_marker',
    'PFNGLINSERTEVENTMARKEREXTPROC', 'PFNGLPUSHGROUPMARKEREXTPROC',
    'PFNGLPOPGROUPMARKEREXTPROC', 'glInsertEventMarkerEXT',
    'glPushGroupMarkerEXT', 'glPopGroupMarkerEXT',
    'GL_EXT_direct_state_access', 'GL_PROGRAM_MATRIX_EXT',
    'GL_TRANSPOSE_PROGRAM_MATRIX_EXT', 'GL_PROGRAM_MATRIX_STACK_DEPTH_EXT',
    'PFNGLMATRIXLOADFEXTPROC', 'PFNGLMATRIXLOADDEXTPROC',
    'PFNGLMATRIXMULTFEXTPROC', 'PFNGLMATRIXMULTDEXTPROC',
    'PFNGLMATRIXLOADIDENTITYEXTPROC', 'PFNGLMATRIXROTATEFEXTPROC',
    'PFNGLMATRIXROTATEDEXTPROC', 'PFNGLMATRIXSCALEFEXTPROC',
    'PFNGLMATRIXSCALEDEXTPROC', 'PFNGLMATRIXTRANSLATEFEXTPROC',
    'PFNGLMATRIXTRANSLATEDEXTPROC', 'PFNGLMATRIXFRUSTUMEXTPROC',
    'PFNGLMATRIXORTHOEXTPROC', 'PFNGLMATRIXPOPEXTPROC',
    'PFNGLMATRIXPUSHEXTPROC', 'PFNGLCLIENTATTRIBDEFAULTEXTPROC',
    'PFNGLPUSHCLIENTATTRIBDEFAULTEXTPROC', 'PFNGLTEXTUREPARAMETERFEXTPROC',
    'PFNGLTEXTUREPARAMETERFVEXTPROC', 'PFNGLTEXTUREPARAMETERIEXTPROC',
    'PFNGLTEXTUREPARAMETERIVEXTPROC', 'PFNGLTEXTUREIMAGE1DEXTPROC',
    'PFNGLTEXTUREIMAGE2DEXTPROC', 'PFNGLTEXTURESUBIMAGE1DEXTPROC',
    'PFNGLTEXTURESUBIMAGE2DEXTPROC', 'PFNGLCOPYTEXTUREIMAGE1DEXTPROC',
    'PFNGLCOPYTEXTUREIMAGE2DEXTPROC', 'PFNGLCOPYTEXTURESUBIMAGE1DEXTPROC',
    'PFNGLCOPYTEXTURESUBIMAGE2DEXTPROC', 'PFNGLGETTEXTUREIMAGEEXTPROC',
    'PFNGLGETTEXTUREPARAMETERFVEXTPROC', 'PFNGLGETTEXTUREPARAMETERIVEXTPROC',
    'PFNGLGETTEXTURELEVELPARAMETERFVEXTPROC',
    'PFNGLGETTEXTURELEVELPARAMETERIVEXTPROC', 'PFNGLTEXTUREIMAGE3DEXTPROC',
    'PFNGLTEXTURESUBIMAGE3DEXTPROC', 'PFNGLCOPYTEXTURESUBIMAGE3DEXTPROC',
    'PFNGLBINDMULTITEXTUREEXTPROC', 'PFNGLMULTITEXCOORDPOINTEREXTPROC',
    'PFNGLMULTITEXENVFEXTPROC', 'PFNGLMULTITEXENVFVEXTPROC',
    'PFNGLMULTITEXENVIEXTPROC', 'PFNGLMULTITEXENVIVEXTPROC',
    'PFNGLMULTITEXGENDEXTPROC', 'PFNGLMULTITEXGENDVEXTPROC',
    'PFNGLMULTITEXGENFEXTPROC', 'PFNGLMULTITEXGENFVEXTPROC',
    'PFNGLMULTITEXGENIEXTPROC', 'PFNGLMULTITEXGENIVEXTPROC',
    'PFNGLGETMULTITEXENVFVEXTPROC', 'PFNGLGETMULTITEXENVIVEXTPROC',
    'PFNGLGETMULTITEXGENDVEXTPROC', 'PFNGLGETMULTITEXGENFVEXTPROC',
    'PFNGLGETMULTITEXGENIVEXTPROC', 'PFNGLMULTITEXPARAMETERIEXTPROC',
    'PFNGLMULTITEXPARAMETERIVEXTPROC', 'PFNGLMULTITEXPARAMETERFEXTPROC',
    'PFNGLMULTITEXPARAMETERFVEXTPROC', 'PFNGLMULTITEXIMAGE1DEXTPROC',
    'PFNGLMULTITEXIMAGE2DEXTPROC', 'PFNGLMULTITEXSUBIMAGE1DEXTPROC',
    'PFNGLMULTITEXSUBIMAGE2DEXTPROC', 'PFNGLCOPYMULTITEXIMAGE1DEXTPROC',
    'PFNGLCOPYMULTITEXIMAGE2DEXTPROC', 'PFNGLCOPYMULTITEXSUBIMAGE1DEXTPROC',
    'PFNGLCOPYMULTITEXSUBIMAGE2DEXTPROC', 'PFNGLGETMULTITEXIMAGEEXTPROC',
    'PFNGLGETMULTITEXPARAMETERFVEXTPROC',
    'PFNGLGETMULTITEXPARAMETERIVEXTPROC',
    'PFNGLGETMULTITEXLEVELPARAMETERFVEXTPROC',
    'PFNGLGETMULTITEXLEVELPARAMETERIVEXTPROC', 'PFNGLMULTITEXIMAGE3DEXTPROC',
    'PFNGLMULTITEXSUBIMAGE3DEXTPROC', 'PFNGLCOPYMULTITEXSUBIMAGE3DEXTPROC',
    'PFNGLENABLECLIENTSTATEINDEXEDEXTPROC',
    'PFNGLDISABLECLIENTSTATEINDEXEDEXTPROC', 'PFNGLGETFLOATINDEXEDVEXTPROC',
    'PFNGLGETDOUBLEINDEXEDVEXTPROC', 'PFNGLGETPOINTERINDEXEDVEXTPROC',
    'PFNGLENABLEINDEXEDEXTPROC', 'PFNGLDISABLEINDEXEDEXTPROC',
    'PFNGLISENABLEDINDEXEDEXTPROC', 'PFNGLGETINTEGERINDEXEDVEXTPROC',
    'PFNGLGETBOOLEANINDEXEDVEXTPROC', 'PFNGLCOMPRESSEDTEXTUREIMAGE3DEXTPROC',
    'PFNGLCOMPRESSEDTEXTUREIMAGE2DEXTPROC',
    'PFNGLCOMPRESSEDTEXTUREIMAGE1DEXTPROC',
    'PFNGLCOMPRESSEDTEXTURESUBIMAGE3DEXTPROC',
    'PFNGLCOMPRESSEDTEXTURESUBIMAGE2DEXTPROC',
    'PFNGLCOMPRESSEDTEXTURESUBIMAGE1DEXTPROC',
    'PFNGLGETCOMPRESSEDTEXTUREIMAGEEXTPROC',
    'PFNGLCOMPRESSEDMULTITEXIMAGE3DEXTPROC',
    'PFNGLCOMPRESSEDMULTITEXIMAGE2DEXTPROC',
    'PFNGLCOMPRESSEDMULTITEXIMAGE1DEXTPROC',
    'PFNGLCOMPRESSEDMULTITEXSUBIMAGE3DEXTPROC',
    'PFNGLCOMPRESSEDMULTITEXSUBIMAGE2DEXTPROC',
    'PFNGLCOMPRESSEDMULTITEXSUBIMAGE1DEXTPROC',
    'PFNGLGETCOMPRESSEDMULTITEXIMAGEEXTPROC',
    'PFNGLMATRIXLOADTRANSPOSEFEXTPROC', 'PFNGLMATRIXLOADTRANSPOSEDEXTPROC',
    'PFNGLMATRIXMULTTRANSPOSEFEXTPROC', 'PFNGLMATRIXMULTTRANSPOSEDEXTPROC',
    'PFNGLNAMEDBUFFERDATAEXTPROC', 'PFNGLNAMEDBUFFERSUBDATAEXTPROC',
    'PFNGLMAPNAMEDBUFFEREXTPROC', 'PFNGLUNMAPNAMEDBUFFEREXTPROC',
    'PFNGLGETNAMEDBUFFERPARAMETERIVEXTPROC',
    'PFNGLGETNAMEDBUFFERPOINTERVEXTPROC', 'PFNGLGETNAMEDBUFFERSUBDATAEXTPROC',
    'PFNGLPROGRAMUNIFORM1FEXTPROC', 'PFNGLPROGRAMUNIFORM2FEXTPROC',
    'PFNGLPROGRAMUNIFORM3FEXTPROC', 'PFNGLPROGRAMUNIFORM4FEXTPROC',
    'PFNGLPROGRAMUNIFORM1IEXTPROC', 'PFNGLPROGRAMUNIFORM2IEXTPROC',
    'PFNGLPROGRAMUNIFORM3IEXTPROC', 'PFNGLPROGRAMUNIFORM4IEXTPROC',
    'PFNGLPROGRAMUNIFORM1FVEXTPROC', 'PFNGLPROGRAMUNIFORM2FVEXTPROC',
    'PFNGLPROGRAMUNIFORM3FVEXTPROC', 'PFNGLPROGRAMUNIFORM4FVEXTPROC',
    'PFNGLPROGRAMUNIFORM1IVEXTPROC', 'PFNGLPROGRAMUNIFORM2IVEXTPROC',
    'PFNGLPROGRAMUNIFORM3IVEXTPROC', 'PFNGLPROGRAMUNIFORM4IVEXTPROC',
    'PFNGLPROGRAMUNIFORMMATRIX2FVEXTPROC',
    'PFNGLPROGRAMUNIFORMMATRIX3FVEXTPROC',
    'PFNGLPROGRAMUNIFORMMATRIX4FVEXTPROC',
    'PFNGLPROGRAMUNIFORMMATRIX2X3FVEXTPROC',
    'PFNGLPROGRAMUNIFORMMATRIX3X2FVEXTPROC',
    'PFNGLPROGRAMUNIFORMMATRIX2X4FVEXTPROC',
    'PFNGLPROGRAMUNIFORMMATRIX4X2FVEXTPROC',
    'PFNGLPROGRAMUNIFORMMATRIX3X4FVEXTPROC',
    'PFNGLPROGRAMUNIFORMMATRIX4X3FVEXTPROC', 'PFNGLTEXTUREBUFFEREXTPROC',
    'PFNGLMULTITEXBUFFEREXTPROC', 'PFNGLTEXTUREPARAMETERIIVEXTPROC',
    'PFNGLTEXTUREPARAMETERIUIVEXTPROC', 'PFNGLGETTEXTUREPARAMETERIIVEXTPROC',
    'PFNGLGETTEXTUREPARAMETERIUIVEXTPROC', 'PFNGLMULTITEXPARAMETERIIVEXTPROC',
    'PFNGLMULTITEXPARAMETERIUIVEXTPROC',
    'PFNGLGETMULTITEXPARAMETERIIVEXTPROC',
    'PFNGLGETMULTITEXPARAMETERIUIVEXTPROC', 'PFNGLPROGRAMUNIFORM1UIEXTPROC',
    'PFNGLPROGRAMUNIFORM2UIEXTPROC', 'PFNGLPROGRAMUNIFORM3UIEXTPROC',
    'PFNGLPROGRAMUNIFORM4UIEXTPROC', 'PFNGLPROGRAMUNIFORM1UIVEXTPROC',
    'PFNGLPROGRAMUNIFORM2UIVEXTPROC', 'PFNGLPROGRAMUNIFORM3UIVEXTPROC',
    'PFNGLPROGRAMUNIFORM4UIVEXTPROC',
    'PFNGLNAMEDPROGRAMLOCALPARAMETERS4FVEXTPROC',
    'PFNGLNAMEDPROGRAMLOCALPARAMETERI4IEXTPROC',
    'PFNGLNAMEDPROGRAMLOCALPARAMETERI4IVEXTPROC',
    'PFNGLNAMEDPROGRAMLOCALPARAMETERSI4IVEXTPROC',
    'PFNGLNAMEDPROGRAMLOCALPARAMETERI4UIEXTPROC',
    'PFNGLNAMEDPROGRAMLOCALPARAMETERI4UIVEXTPROC',
    'PFNGLNAMEDPROGRAMLOCALPARAMETERSI4UIVEXTPROC',
    'PFNGLGETNAMEDPROGRAMLOCALPARAMETERIIVEXTPROC',
    'PFNGLGETNAMEDPROGRAMLOCALPARAMETERIUIVEXTPROC',
    'PFNGLENABLECLIENTSTATEIEXTPROC', 'PFNGLDISABLECLIENTSTATEIEXTPROC',
    'PFNGLGETFLOATI_VEXTPROC', 'PFNGLGETDOUBLEI_VEXTPROC',
    'PFNGLGETPOINTERI_VEXTPROC', 'PFNGLNAMEDPROGRAMSTRINGEXTPROC',
    'PFNGLNAMEDPROGRAMLOCALPARAMETER4DEXTPROC',
    'PFNGLNAMEDPROGRAMLOCALPARAMETER4DVEXTPROC',
    'PFNGLNAMEDPROGRAMLOCALPARAMETER4FEXTPROC',
    'PFNGLNAMEDPROGRAMLOCALPARAMETER4FVEXTPROC',
    'PFNGLGETNAMEDPROGRAMLOCALPARAMETERDVEXTPROC',
    'PFNGLGETNAMEDPROGRAMLOCALPARAMETERFVEXTPROC',
    'PFNGLGETNAMEDPROGRAMIVEXTPROC', 'PFNGLGETNAMEDPROGRAMSTRINGEXTPROC',
    'PFNGLNAMEDRENDERBUFFERSTORAGEEXTPROC',
    'PFNGLGETNAMEDRENDERBUFFERPARAMETERIVEXTPROC',
    'PFNGLNAMEDRENDERBUFFERSTORAGEMULTISAMPLEEXTPROC',
    'PFNGLNAMEDRENDERBUFFERSTORAGEMULTISAMPLECOVERAGEEXTPROC',
    'PFNGLCHECKNAMEDFRAMEBUFFERSTATUSEXTPROC',
    'PFNGLNAMEDFRAMEBUFFERTEXTURE1DEXTPROC',
    'PFNGLNAMEDFRAMEBUFFERTEXTURE2DEXTPROC',
    'PFNGLNAMEDFRAMEBUFFERTEXTURE3DEXTPROC',
    'PFNGLNAMEDFRAMEBUFFERRENDERBUFFEREXTPROC',
    'PFNGLGETNAMEDFRAMEBUFFERATTACHMENTPARAMETERIVEXTPROC',
    'PFNGLGENERATETEXTUREMIPMAPEXTPROC', 'PFNGLGENERATEMULTITEXMIPMAPEXTPROC',
    'PFNGLFRAMEBUFFERDRAWBUFFEREXTPROC', 'PFNGLFRAMEBUFFERDRAWBUFFERSEXTPROC',
    'PFNGLFRAMEBUFFERREADBUFFEREXTPROC',
    'PFNGLGETFRAMEBUFFERPARAMETERIVEXTPROC',
    'PFNGLNAMEDCOPYBUFFERSUBDATAEXTPROC',
    'PFNGLNAMEDFRAMEBUFFERTEXTUREEXTPROC',
    'PFNGLNAMEDFRAMEBUFFERTEXTURELAYEREXTPROC',
    'PFNGLNAMEDFRAMEBUFFERTEXTUREFACEEXTPROC',
    'PFNGLTEXTURERENDERBUFFEREXTPROC', 'PFNGLMULTITEXRENDERBUFFEREXTPROC',
    'PFNGLVERTEXARRAYVERTEXOFFSETEXTPROC',
    'PFNGLVERTEXARRAYCOLOROFFSETEXTPROC',
    'PFNGLVERTEXARRAYEDGEFLAGOFFSETEXTPROC',
    'PFNGLVERTEXARRAYINDEXOFFSETEXTPROC',
    'PFNGLVERTEXARRAYNORMALOFFSETEXTPROC',
    'PFNGLVERTEXARRAYTEXCOORDOFFSETEXTPROC',
    'PFNGLVERTEXARRAYMULTITEXCOORDOFFSETEXTPROC',
    'PFNGLVERTEXARRAYFOGCOORDOFFSETEXTPROC',
    'PFNGLVERTEXARRAYSECONDARYCOLOROFFSETEXTPROC',
    'PFNGLVERTEXARRAYVERTEXATTRIBOFFSETEXTPROC',
    'PFNGLVERTEXARRAYVERTEXATTRIBIOFFSETEXTPROC',
    'PFNGLENABLEVERTEXARRAYEXTPROC', 'PFNGLDISABLEVERTEXARRAYEXTPROC',
    'PFNGLENABLEVERTEXARRAYATTRIBEXTPROC',
    'PFNGLDISABLEVERTEXARRAYATTRIBEXTPROC',
    'PFNGLGETVERTEXARRAYINTEGERVEXTPROC',
    'PFNGLGETVERTEXARRAYPOINTERVEXTPROC',
    'PFNGLGETVERTEXARRAYINTEGERI_VEXTPROC',
    'PFNGLGETVERTEXARRAYPOINTERI_VEXTPROC', 'PFNGLMAPNAMEDBUFFERRANGEEXTPROC',
    'PFNGLFLUSHMAPPEDNAMEDBUFFERRANGEEXTPROC',
    'PFNGLNAMEDBUFFERSTORAGEEXTPROC', 'PFNGLCLEARNAMEDBUFFERDATAEXTPROC',
    'PFNGLCLEARNAMEDBUFFERSUBDATAEXTPROC',
    'PFNGLNAMEDFRAMEBUFFERPARAMETERIEXTPROC',
    'PFNGLGETNAMEDFRAMEBUFFERPARAMETERIVEXTPROC',
    'PFNGLPROGRAMUNIFORM1DEXTPROC', 'PFNGLPROGRAMUNIFORM2DEXTPROC',
    'PFNGLPROGRAMUNIFORM3DEXTPROC', 'PFNGLPROGRAMUNIFORM4DEXTPROC',
    'PFNGLPROGRAMUNIFORM1DVEXTPROC', 'PFNGLPROGRAMUNIFORM2DVEXTPROC',
    'PFNGLPROGRAMUNIFORM3DVEXTPROC', 'PFNGLPROGRAMUNIFORM4DVEXTPROC',
    'PFNGLPROGRAMUNIFORMMATRIX2DVEXTPROC',
    'PFNGLPROGRAMUNIFORMMATRIX3DVEXTPROC',
    'PFNGLPROGRAMUNIFORMMATRIX4DVEXTPROC',
    'PFNGLPROGRAMUNIFORMMATRIX2X3DVEXTPROC',
    'PFNGLPROGRAMUNIFORMMATRIX2X4DVEXTPROC',
    'PFNGLPROGRAMUNIFORMMATRIX3X2DVEXTPROC',
    'PFNGLPROGRAMUNIFORMMATRIX3X4DVEXTPROC',
    'PFNGLPROGRAMUNIFORMMATRIX4X2DVEXTPROC',
    'PFNGLPROGRAMUNIFORMMATRIX4X3DVEXTPROC', 'PFNGLTEXTUREBUFFERRANGEEXTPROC',
    'PFNGLTEXTURESTORAGE1DEXTPROC', 'PFNGLTEXTURESTORAGE2DEXTPROC',
    'PFNGLTEXTURESTORAGE3DEXTPROC', 'PFNGLTEXTURESTORAGE2DMULTISAMPLEEXTPROC',
    'PFNGLTEXTURESTORAGE3DMULTISAMPLEEXTPROC',
    'PFNGLVERTEXARRAYBINDVERTEXBUFFEREXTPROC',
    'PFNGLVERTEXARRAYVERTEXATTRIBFORMATEXTPROC',
    'PFNGLVERTEXARRAYVERTEXATTRIBIFORMATEXTPROC',
    'PFNGLVERTEXARRAYVERTEXATTRIBLFORMATEXTPROC',
    'PFNGLVERTEXARRAYVERTEXATTRIBBINDINGEXTPROC',
    'PFNGLVERTEXARRAYVERTEXBINDINGDIVISOREXTPROC',
    'PFNGLVERTEXARRAYVERTEXATTRIBLOFFSETEXTPROC',
    'PFNGLTEXTUREPAGECOMMITMENTEXTPROC',
    'PFNGLVERTEXARRAYVERTEXATTRIBDIVISOREXTPROC', 'glMatrixLoadfEXT',
    'glMatrixLoaddEXT', 'glMatrixMultfEXT', 'glMatrixMultdEXT',
    'glMatrixLoadIdentityEXT', 'glMatrixRotatefEXT', 'glMatrixRotatedEXT',
    'glMatrixScalefEXT', 'glMatrixScaledEXT', 'glMatrixTranslatefEXT',
    'glMatrixTranslatedEXT', 'glMatrixFrustumEXT', 'glMatrixOrthoEXT',
    'glMatrixPopEXT', 'glMatrixPushEXT', 'glClientAttribDefaultEXT',
    'glPushClientAttribDefaultEXT', 'glTextureParameterfEXT',
    'glTextureParameterfvEXT', 'glTextureParameteriEXT',
    'glTextureParameterivEXT', 'glTextureImage1DEXT', 'glTextureImage2DEXT',
    'glTextureSubImage1DEXT', 'glTextureSubImage2DEXT',
    'glCopyTextureImage1DEXT', 'glCopyTextureImage2DEXT',
    'glCopyTextureSubImage1DEXT', 'glCopyTextureSubImage2DEXT',
    'glGetTextureImageEXT', 'glGetTextureParameterfvEXT',
    'glGetTextureParameterivEXT', 'glGetTextureLevelParameterfvEXT',
    'glGetTextureLevelParameterivEXT', 'glTextureImage3DEXT',
    'glTextureSubImage3DEXT', 'glCopyTextureSubImage3DEXT',
    'glBindMultiTextureEXT', 'glMultiTexCoordPointerEXT', 'glMultiTexEnvfEXT',
    'glMultiTexEnvfvEXT', 'glMultiTexEnviEXT', 'glMultiTexEnvivEXT',
    'glMultiTexGendEXT', 'glMultiTexGendvEXT', 'glMultiTexGenfEXT',
    'glMultiTexGenfvEXT', 'glMultiTexGeniEXT', 'glMultiTexGenivEXT',
    'glGetMultiTexEnvfvEXT', 'glGetMultiTexEnvivEXT', 'glGetMultiTexGendvEXT',
    'glGetMultiTexGenfvEXT', 'glGetMultiTexGenivEXT',
    'glMultiTexParameteriEXT', 'glMultiTexParameterivEXT',
    'glMultiTexParameterfEXT', 'glMultiTexParameterfvEXT',
    'glMultiTexImage1DEXT', 'glMultiTexImage2DEXT', 'glMultiTexSubImage1DEXT',
    'glMultiTexSubImage2DEXT', 'glCopyMultiTexImage1DEXT',
    'glCopyMultiTexImage2DEXT', 'glCopyMultiTexSubImage1DEXT',
    'glCopyMultiTexSubImage2DEXT', 'glGetMultiTexImageEXT',
    'glGetMultiTexParameterfvEXT', 'glGetMultiTexParameterivEXT',
    'glGetMultiTexLevelParameterfvEXT', 'glGetMultiTexLevelParameterivEXT',
    'glMultiTexImage3DEXT', 'glMultiTexSubImage3DEXT',
    'glCopyMultiTexSubImage3DEXT', 'glEnableClientStateIndexedEXT',
    'glDisableClientStateIndexedEXT', 'glGetFloatIndexedvEXT',
    'glGetDoubleIndexedvEXT', 'glGetPointerIndexedvEXT', 'glEnableIndexedEXT',
    'glDisableIndexedEXT', 'glIsEnabledIndexedEXT', 'glGetIntegerIndexedvEXT',
    'glGetBooleanIndexedvEXT', 'glCompressedTextureImage3DEXT',
    'glCompressedTextureImage2DEXT', 'glCompressedTextureImage1DEXT',
    'glCompressedTextureSubImage3DEXT', 'glCompressedTextureSubImage2DEXT',
    'glCompressedTextureSubImage1DEXT', 'glGetCompressedTextureImageEXT',
    'glCompressedMultiTexImage3DEXT', 'glCompressedMultiTexImage2DEXT',
    'glCompressedMultiTexImage1DEXT', 'glCompressedMultiTexSubImage3DEXT',
    'glCompressedMultiTexSubImage2DEXT', 'glCompressedMultiTexSubImage1DEXT',
    'glGetCompressedMultiTexImageEXT', 'glMatrixLoadTransposefEXT',
    'glMatrixLoadTransposedEXT', 'glMatrixMultTransposefEXT',
    'glMatrixMultTransposedEXT', 'glNamedBufferDataEXT',
    'glNamedBufferSubDataEXT', 'glMapNamedBufferEXT', 'glUnmapNamedBufferEXT',
    'glGetNamedBufferParameterivEXT', 'glGetNamedBufferPointervEXT',
    'glGetNamedBufferSubDataEXT', 'glProgramUniform1fEXT',
    'glProgramUniform2fEXT', 'glProgramUniform3fEXT', 'glProgramUniform4fEXT',
    'glProgramUniform1iEXT', 'glProgramUniform2iEXT', 'glProgramUniform3iEXT',
    'glProgramUniform4iEXT', 'glProgramUniform1fvEXT',
    'glProgramUniform2fvEXT', 'glProgramUniform3fvEXT',
    'glProgramUniform4fvEXT', 'glProgramUniform1ivEXT',
    'glProgramUniform2ivEXT', 'glProgramUniform3ivEXT',
    'glProgramUniform4ivEXT', 'glProgramUniformMatrix2fvEXT',
    'glProgramUniformMatrix3fvEXT', 'glProgramUniformMatrix4fvEXT',
    'glProgramUniformMatrix2x3fvEXT', 'glProgramUniformMatrix3x2fvEXT',
    'glProgramUniformMatrix2x4fvEXT', 'glProgramUniformMatrix4x2fvEXT',
    'glProgramUniformMatrix3x4fvEXT', 'glProgramUniformMatrix4x3fvEXT',
    'glTextureBufferEXT', 'glMultiTexBufferEXT', 'glTextureParameterIivEXT',
    'glTextureParameterIuivEXT', 'glGetTextureParameterIivEXT',
    'glGetTextureParameterIuivEXT', 'glMultiTexParameterIivEXT',
    'glMultiTexParameterIuivEXT', 'glGetMultiTexParameterIivEXT',
    'glGetMultiTexParameterIuivEXT', 'glProgramUniform1uiEXT',
    'glProgramUniform2uiEXT', 'glProgramUniform3uiEXT',
    'glProgramUniform4uiEXT', 'glProgramUniform1uivEXT',
    'glProgramUniform2uivEXT', 'glProgramUniform3uivEXT',
    'glProgramUniform4uivEXT', 'glNamedProgramLocalParameters4fvEXT',
    'glNamedProgramLocalParameterI4iEXT',
    'glNamedProgramLocalParameterI4ivEXT',
    'glNamedProgramLocalParametersI4ivEXT',
    'glNamedProgramLocalParameterI4uiEXT',
    'glNamedProgramLocalParameterI4uivEXT',
    'glNamedProgramLocalParametersI4uivEXT',
    'glGetNamedProgramLocalParameterIivEXT',
    'glGetNamedProgramLocalParameterIuivEXT', 'glEnableClientStateiEXT',
    'glDisableClientStateiEXT', 'glGetFloati_vEXT', 'glGetDoublei_vEXT',
    'glGetPointeri_vEXT', 'glNamedProgramStringEXT',
    'glNamedProgramLocalParameter4dEXT', 'glNamedProgramLocalParameter4dvEXT',
    'glNamedProgramLocalParameter4fEXT', 'glNamedProgramLocalParameter4fvEXT',
    'glGetNamedProgramLocalParameterdvEXT',
    'glGetNamedProgramLocalParameterfvEXT', 'glGetNamedProgramivEXT',
    'glGetNamedProgramStringEXT', 'glNamedRenderbufferStorageEXT',
    'glGetNamedRenderbufferParameterivEXT',
    'glNamedRenderbufferStorageMultisampleEXT',
    'glNamedRenderbufferStorageMultisampleCoverageEXT',
    'glCheckNamedFramebufferStatusEXT', 'glNamedFramebufferTexture1DEXT',
    'glNamedFramebufferTexture2DEXT', 'glNamedFramebufferTexture3DEXT',
    'glNamedFramebufferRenderbufferEXT',
    'glGetNamedFramebufferAttachmentParameterivEXT',
    'glGenerateTextureMipmapEXT', 'glGenerateMultiTexMipmapEXT',
    'glFramebufferDrawBufferEXT', 'glFramebufferDrawBuffersEXT',
    'glFramebufferReadBufferEXT', 'glGetFramebufferParameterivEXT',
    'glNamedCopyBufferSubDataEXT', 'glNamedFramebufferTextureEXT',
    'glNamedFramebufferTextureLayerEXT', 'glNamedFramebufferTextureFaceEXT',
    'glTextureRenderbufferEXT', 'glMultiTexRenderbufferEXT',
    'glVertexArrayVertexOffsetEXT', 'glVertexArrayColorOffsetEXT',
    'glVertexArrayEdgeFlagOffsetEXT', 'glVertexArrayIndexOffsetEXT',
    'glVertexArrayNormalOffsetEXT', 'glVertexArrayTexCoordOffsetEXT',
    'glVertexArrayMultiTexCoordOffsetEXT', 'glVertexArrayFogCoordOffsetEXT',
    'glVertexArraySecondaryColorOffsetEXT',
    'glVertexArrayVertexAttribOffsetEXT',
    'glVertexArrayVertexAttribIOffsetEXT', 'glEnableVertexArrayEXT',
    'glDisableVertexArrayEXT', 'glEnableVertexArrayAttribEXT',
    'glDisableVertexArrayAttribEXT', 'glGetVertexArrayIntegervEXT',
    'glGetVertexArrayPointervEXT', 'glGetVertexArrayIntegeri_vEXT',
    'glGetVertexArrayPointeri_vEXT', 'glMapNamedBufferRangeEXT',
    'glFlushMappedNamedBufferRangeEXT', 'glNamedBufferStorageEXT',
    'glClearNamedBufferDataEXT', 'glClearNamedBufferSubDataEXT',
    'glNamedFramebufferParameteriEXT', 'glGetNamedFramebufferParameterivEXT',
    'glProgramUniform1dEXT', 'glProgramUniform2dEXT', 'glProgramUniform3dEXT',
    'glProgramUniform4dEXT', 'glProgramUniform1dvEXT',
    'glProgramUniform2dvEXT', 'glProgramUniform3dvEXT',
    'glProgramUniform4dvEXT', 'glProgramUniformMatrix2dvEXT',
    'glProgramUniformMatrix3dvEXT', 'glProgramUniformMatrix4dvEXT',
    'glProgramUniformMatrix2x3dvEXT', 'glProgramUniformMatrix2x4dvEXT',
    'glProgramUniformMatrix3x2dvEXT', 'glProgramUniformMatrix3x4dvEXT',
    'glProgramUniformMatrix4x2dvEXT', 'glProgramUniformMatrix4x3dvEXT',
    'glTextureBufferRangeEXT', 'glTextureStorage1DEXT',
    'glTextureStorage2DEXT', 'glTextureStorage3DEXT',
    'glTextureStorage2DMultisampleEXT', 'glTextureStorage3DMultisampleEXT',
    'glVertexArrayBindVertexBufferEXT', 'glVertexArrayVertexAttribFormatEXT',
    'glVertexArrayVertexAttribIFormatEXT',
    'glVertexArrayVertexAttribLFormatEXT',
    'glVertexArrayVertexAttribBindingEXT',
    'glVertexArrayVertexBindingDivisorEXT',
    'glVertexArrayVertexAttribLOffsetEXT', 'glTexturePageCommitmentEXT',
    'glVertexArrayVertexAttribDivisorEXT', 'GL_EXT_draw_instanced',
    'PFNGLDRAWARRAYSINSTANCEDEXTPROC', 'PFNGLDRAWELEMENTSINSTANCEDEXTPROC',
    'glDrawArraysInstancedEXT', 'glDrawElementsInstancedEXT',
    'GL_EXT_multiview_tessellation_geometry_shader',
    'GL_EXT_multiview_texture_multisample', 'GL_EXT_multiview_timer_query',
    'GL_EXT_polygon_offset_clamp', 'GL_POLYGON_OFFSET_CLAMP_EXT',
    'PFNGLPOLYGONOFFSETCLAMPEXTPROC', 'glPolygonOffsetClampEXT',
    'GL_EXT_post_depth_coverage', 'GL_EXT_raster_multisample',
    'GL_RASTER_MULTISAMPLE_EXT', 'GL_RASTER_SAMPLES_EXT',
    'GL_MAX_RASTER_SAMPLES_EXT', 'GL_RASTER_FIXED_SAMPLE_LOCATIONS_EXT',
    'GL_MULTISAMPLE_RASTERIZATION_ALLOWED_EXT',
    'GL_EFFECTIVE_RASTER_SAMPLES_EXT', 'PFNGLRASTERSAMPLESEXTPROC',
    'glRasterSamplesEXT', 'GL_EXT_separate_shader_objects',
    'GL_ACTIVE_PROGRAM_EXT', 'PFNGLUSESHADERPROGRAMEXTPROC',
    'PFNGLACTIVEPROGRAMEXTPROC', 'PFNGLCREATESHADERPROGRAMEXTPROC',
    'glUseShaderProgramEXT', 'glActiveProgramEXT', 'glCreateShaderProgramEXT',
    'GL_EXT_shader_framebuffer_fetch',
    'GL_FRAGMENT_SHADER_DISCARDS_SAMPLES_EXT',
    'GL_EXT_shader_framebuffer_fetch_non_coherent',
    'PFNGLFRAMEBUFFERFETCHBARRIEREXTPROC', 'glFramebufferFetchBarrierEXT',
    'GL_EXT_shader_integer_mix', 'GL_EXT_texture_compression_s3tc',
    'GL_COMPRESSED_RGB_S3TC_DXT1_EXT', 'GL_COMPRESSED_RGBA_S3TC_DXT1_EXT',
    'GL_COMPRESSED_RGBA_S3TC_DXT3_EXT', 'GL_COMPRESSED_RGBA_S3TC_DXT5_EXT',
    'GL_EXT_texture_filter_minmax', 'GL_TEXTURE_REDUCTION_MODE_EXT',
    'GL_WEIGHTED_AVERAGE_EXT', 'GL_EXT_texture_sRGB_R8', 'GL_SR8_EXT',
    'GL_EXT_texture_sRGB_RG8', 'GL_SRG8_EXT', 'GL_EXT_texture_sRGB_decode',
    'GL_TEXTURE_SRGB_DECODE_EXT', 'GL_DECODE_EXT', 'GL_SKIP_DECODE_EXT',
    'GL_EXT_texture_shadow_lod', 'GL_EXT_texture_storage',
    'GL_TEXTURE_IMMUTABLE_FORMAT_EXT', 'GL_ALPHA8_EXT', 'GL_LUMINANCE8_EXT',
    'GL_LUMINANCE8_ALPHA8_EXT', 'GL_RGBA32F_EXT', 'GL_RGB32F_EXT',
    'GL_ALPHA32F_EXT', 'GL_LUMINANCE32F_EXT', 'GL_LUMINANCE_ALPHA32F_EXT',
    'GL_RGBA16F_EXT', 'GL_RGB16F_EXT', 'GL_ALPHA16F_EXT',
    'GL_LUMINANCE16F_EXT', 'GL_LUMINANCE_ALPHA16F_EXT', 'GL_RGB10_A2_EXT',
    'GL_RGB10_EXT', 'GL_BGRA8_EXT', 'GL_R8_EXT', 'GL_RG8_EXT', 'GL_R32F_EXT',
    'GL_RG32F_EXT', 'GL_R16F_EXT', 'GL_RG16F_EXT', 'PFNGLTEXSTORAGE1DEXTPROC',
    'PFNGLTEXSTORAGE2DEXTPROC', 'PFNGLTEXSTORAGE3DEXTPROC',
    'glTexStorage1DEXT', 'glTexStorage2DEXT', 'glTexStorage3DEXT',
    'GL_EXT_window_rectangles', 'GL_INCLUSIVE_EXT', 'GL_EXCLUSIVE_EXT',
    'GL_WINDOW_RECTANGLE_EXT', 'GL_WINDOW_RECTANGLE_MODE_EXT',
    'GL_MAX_WINDOW_RECTANGLES_EXT', 'GL_NUM_WINDOW_RECTANGLES_EXT',
    'PFNGLWINDOWRECTANGLESEXTPROC', 'glWindowRectanglesEXT'
]
