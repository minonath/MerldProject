from .._wrapper import *

GL_NV_bindless_multi_draw_indirect = 1
PFNGLMULTIDRAWARRAYSINDIRECTBINDLESSNVPROC = C(
    None, UInt, VoidP, Int, Int, Int
)
PFNGLMULTIDRAWELEMENTSINDIRECTBINDLESSNVPROC = C(
    None, UInt, UInt, VoidP, Int, Int, Int
)
glMultiDrawArraysIndirectBindlessNV = GL(
    'glMultiDrawArraysIndirectBindlessNV', None, UInt, VoidP, Int, Int, Int
)
glMultiDrawElementsIndirectBindlessNV = GL(
    'glMultiDrawElementsIndirectBindlessNV', None, UInt, UInt, VoidP, Int,
    Int, Int
)
GL_NV_bindless_multi_draw_indirect_count = 1
PFNGLMULTIDRAWARRAYSINDIRECTBINDLESSCOUNTNVPROC = C(
    None, UInt, VoidP, Int, Int, Int, Int
)
PFNGLMULTIDRAWELEMENTSINDIRECTBINDLESSCOUNTNVPROC = C(
    None, UInt, UInt, VoidP, Int, Int, Int, Int
)
glMultiDrawArraysIndirectBindlessCountNV = GL(
    'glMultiDrawArraysIndirectBindlessCountNV', None, UInt, VoidP, Int, Int,
    Int, Int
)
glMultiDrawElementsIndirectBindlessCountNV = GL(
    'glMultiDrawElementsIndirectBindlessCountNV', None, UInt, UInt, VoidP,
    Int, Int, Int, Int
)
GL_NV_bindless_texture = 1
PFNGLGETTEXTUREHANDLENVPROC = C(ULong, UInt)
PFNGLGETTEXTURESAMPLERHANDLENVPROC = C(ULong, UInt, UInt)
PFNGLMAKETEXTUREHANDLERESIDENTNVPROC = C(None, ULong)
PFNGLMAKETEXTUREHANDLENONRESIDENTNVPROC = C(None, ULong)
PFNGLGETIMAGEHANDLENVPROC = C(ULong, UInt, Int, UByte, Int, UInt)
PFNGLMAKEIMAGEHANDLERESIDENTNVPROC = C(None, ULong, UInt)
PFNGLMAKEIMAGEHANDLENONRESIDENTNVPROC = C(None, ULong)
PFNGLUNIFORMHANDLEUI64NVPROC = C(None, Int, ULong)
PFNGLUNIFORMHANDLEUI64VNVPROC = C(None, Int, Int, P(ULong))
PFNGLPROGRAMUNIFORMHANDLEUI64NVPROC = C(None, UInt, Int, ULong)
PFNGLPROGRAMUNIFORMHANDLEUI64VNVPROC = C(None, UInt, Int, Int, P(ULong))
PFNGLISTEXTUREHANDLERESIDENTNVPROC = C(UByte, ULong)
PFNGLISIMAGEHANDLERESIDENTNVPROC = C(UByte, ULong)
glGetTextureHandleNV = GL('glGetTextureHandleNV', ULong, UInt)
glGetTextureSamplerHandleNV = GL(
    'glGetTextureSamplerHandleNV', ULong, UInt, UInt
)
glMakeTextureHandleResidentNV = GL(
    'glMakeTextureHandleResidentNV', None, ULong
)
glMakeTextureHandleNonResidentNV = GL(
    'glMakeTextureHandleNonResidentNV', None, ULong
)
glGetImageHandleNV = GL(
    'glGetImageHandleNV', ULong, UInt, Int, UByte, Int, UInt
)
glMakeImageHandleResidentNV = GL(
    'glMakeImageHandleResidentNV', None, ULong, UInt
)
glMakeImageHandleNonResidentNV = GL(
    'glMakeImageHandleNonResidentNV', None, ULong
)
glUniformHandleui64NV = GL('glUniformHandleui64NV', None, Int, ULong)
glUniformHandleui64vNV = GL(
    'glUniformHandleui64vNV', None, Int, Int, P(ULong)
)
glProgramUniformHandleui64NV = GL(
    'glProgramUniformHandleui64NV', None, UInt, Int, ULong
)
glProgramUniformHandleui64vNV = GL(
    'glProgramUniformHandleui64vNV', None, UInt, Int, Int, P(ULong)
)
glIsTextureHandleResidentNV = GL('glIsTextureHandleResidentNV', UByte, ULong)
glIsImageHandleResidentNV = GL('glIsImageHandleResidentNV', UByte, ULong)
GL_NV_blend_equation_advanced = 1
GL_BLEND_OVERLAP_NV = 0x9281
GL_BLEND_PREMULTIPLIED_SRC_NV = 0x9280
GL_BLUE_NV = 0x1905
GL_COLORBURN_NV = 0x929A
GL_COLORDODGE_NV = 0x9299
GL_CONJOINT_NV = 0x9284
GL_CONTRAST_NV = 0x92A1
GL_DARKEN_NV = 0x9297
GL_DIFFERENCE_NV = 0x929E
GL_DISJOINT_NV = 0x9283
GL_DST_ATOP_NV = 0x928F
GL_DST_IN_NV = 0x928B
GL_DST_NV = 0x9287
GL_DST_OUT_NV = 0x928D
GL_DST_OVER_NV = 0x9289
GL_EXCLUSION_NV = 0x92A0
GL_GREEN_NV = 0x1904
GL_HARDLIGHT_NV = 0x929B
GL_HARDMIX_NV = 0x92A9
GL_HSL_COLOR_NV = 0x92AF
GL_HSL_HUE_NV = 0x92AD
GL_HSL_LUMINOSITY_NV = 0x92B0
GL_HSL_SATURATION_NV = 0x92AE
GL_INVERT_OVG_NV = 0x92B4
GL_INVERT_RGB_NV = 0x92A3
GL_LIGHTEN_NV = 0x9298
GL_LINEARBURN_NV = 0x92A5
GL_LINEARDODGE_NV = 0x92A4
GL_LINEARLIGHT_NV = 0x92A7
GL_MINUS_CLAMPED_NV = 0x92B3
GL_MINUS_NV = 0x929F
GL_MULTIPLY_NV = 0x9294
GL_OVERLAY_NV = 0x9296
GL_PINLIGHT_NV = 0x92A8
GL_PLUS_CLAMPED_ALPHA_NV = 0x92B2
GL_PLUS_CLAMPED_NV = 0x92B1
GL_PLUS_DARKER_NV = 0x9292
GL_PLUS_NV = 0x9291
GL_RED_NV = 0x1903
GL_SCREEN_NV = 0x9295
GL_SOFTLIGHT_NV = 0x929C
GL_SRC_ATOP_NV = 0x928E
GL_SRC_IN_NV = 0x928A
GL_SRC_NV = 0x9286
GL_SRC_OUT_NV = 0x928C
GL_SRC_OVER_NV = 0x9288
GL_UNCORRELATED_NV = 0x9282
GL_VIVIDLIGHT_NV = 0x92A6
GL_XOR_NV = 0x1506
PFNGLBLENDPARAMETERINVPROC = C(None, UInt, Int)
PFNGLBLENDBARRIERNVPROC = C(None)
glBlendParameteriNV = GL('glBlendParameteriNV', None, UInt, Int)
glBlendBarrierNV = GL('glBlendBarrierNV', None)
GL_NV_blend_equation_advanced_coherent = 1
GL_BLEND_ADVANCED_COHERENT_NV = 0x9285
GL_NV_blend_minmax_factor = 1
GL_FACTOR_MIN_AMD = 0x901C
GL_FACTOR_MAX_AMD = 0x901D
GL_NV_clip_space_w_scaling = 1
GL_VIEWPORT_POSITION_W_SCALE_NV = 0x937C
GL_VIEWPORT_POSITION_W_SCALE_X_COEFF_NV = 0x937D
GL_VIEWPORT_POSITION_W_SCALE_Y_COEFF_NV = 0x937E
PFNGLVIEWPORTPOSITIONWSCALENVPROC = C(None, UInt, Float, Float)
glViewportPositionWScaleNV = GL(
    'glViewportPositionWScaleNV', None, UInt, Float, Float
)
GL_NV_command_list = 1
GL_TERMINATE_SEQUENCE_COMMAND_NV = 0x0000
GL_NOP_COMMAND_NV = 0x0001
GL_DRAW_ELEMENTS_COMMAND_NV = 0x0002
GL_DRAW_ARRAYS_COMMAND_NV = 0x0003
GL_DRAW_ELEMENTS_STRIP_COMMAND_NV = 0x0004
GL_DRAW_ARRAYS_STRIP_COMMAND_NV = 0x0005
GL_DRAW_ELEMENTS_INSTANCED_COMMAND_NV = 0x0006
GL_DRAW_ARRAYS_INSTANCED_COMMAND_NV = 0x0007
GL_ELEMENT_ADDRESS_COMMAND_NV = 0x0008
GL_ATTRIBUTE_ADDRESS_COMMAND_NV = 0x0009
GL_UNIFORM_ADDRESS_COMMAND_NV = 0x000A
GL_BLEND_COLOR_COMMAND_NV = 0x000B
GL_STENCIL_REF_COMMAND_NV = 0x000C
GL_LINE_WIDTH_COMMAND_NV = 0x000D
GL_POLYGON_OFFSET_COMMAND_NV = 0x000E
GL_ALPHA_REF_COMMAND_NV = 0x000F
GL_VIEWPORT_COMMAND_NV = 0x0010
GL_SCISSOR_COMMAND_NV = 0x0011
GL_FRONT_FACE_COMMAND_NV = 0x0012
PFNGLCREATESTATESNVPROC = C(None, Int, P(UInt))
PFNGLDELETESTATESNVPROC = C(None, Int, P(UInt))
PFNGLISSTATENVPROC = C(UByte, UInt)
PFNGLSTATECAPTURENVPROC = C(None, UInt, UInt)
PFNGLGETCOMMANDHEADERNVPROC = C(UInt, UInt, UInt)
PFNGLGETSTAGEINDEXNVPROC = C(UShort, UInt)
PFNGLDRAWCOMMANDSNVPROC = C(None, UInt, UInt, P(Size), P(Int), UInt)
PFNGLDRAWCOMMANDSADDRESSNVPROC = C(None, UInt, P(ULong), P(Int), UInt)
PFNGLDRAWCOMMANDSSTATESNVPROC = C(
    None, UInt, P(Size), P(Int), P(UInt), P(UInt), UInt
)
PFNGLDRAWCOMMANDSSTATESADDRESSNVPROC = C(
    None, P(ULong), P(Int), P(UInt), P(UInt), UInt
)
PFNGLCREATECOMMANDLISTSNVPROC = C(None, Int, P(UInt))
PFNGLDELETECOMMANDLISTSNVPROC = C(None, Int, P(UInt))
PFNGLISCOMMANDLISTNVPROC = C(UByte, UInt)
PFNGLLISTDRAWCOMMANDSSTATESCLIENTNVPROC = C(
    None, UInt, UInt, P(VoidP), P(Int), P(UInt), P(UInt), UInt
)
PFNGLCOMMANDLISTSEGMENTSNVPROC = C(None, UInt, UInt)
PFNGLCOMPILECOMMANDLISTNVPROC = C(None, UInt)
PFNGLCALLCOMMANDLISTNVPROC = C(None, UInt)
glCreateStatesNV = GL('glCreateStatesNV', None, Int, P(UInt))
glDeleteStatesNV = GL('glDeleteStatesNV', None, Int, P(UInt))
glIsStateNV = GL('glIsStateNV', UByte, UInt)
glStateCaptureNV = GL('glStateCaptureNV', None, UInt, UInt)
glGetCommandHeaderNV = GL('glGetCommandHeaderNV', UInt, UInt, UInt)
glGetStageIndexNV = GL('glGetStageIndexNV', UShort, UInt)
glDrawCommandsNV = GL(
    'glDrawCommandsNV', None, UInt, UInt, P(Size), P(Int), UInt
)
glDrawCommandsAddressNV = GL(
    'glDrawCommandsAddressNV', None, UInt, P(ULong), P(Int), UInt
)
glDrawCommandsStatesNV = GL(
    'glDrawCommandsStatesNV', None, UInt, P(Size), P(Int), P(UInt), P(UInt),
    UInt
)
glDrawCommandsStatesAddressNV = GL(
    'glDrawCommandsStatesAddressNV', None, P(ULong), P(Int), P(UInt), P(UInt),
    UInt
)
glCreateCommandListsNV = GL('glCreateCommandListsNV', None, Int, P(UInt))
glDeleteCommandListsNV = GL('glDeleteCommandListsNV', None, Int, P(UInt))
glIsCommandListNV = GL('glIsCommandListNV', UByte, UInt)
glListDrawCommandsStatesClientNV = GL(
    'glListDrawCommandsStatesClientNV', None, UInt, UInt, P(VoidP), P(Int),
    P(UInt), P(UInt), UInt
)
glCommandListSegmentsNV = GL('glCommandListSegmentsNV', None, UInt, UInt)
glCompileCommandListNV = GL('glCompileCommandListNV', None, UInt)
glCallCommandListNV = GL('glCallCommandListNV', None, UInt)
GL_NV_compute_shader_derivatives = 1
GL_NV_conditional_render = 1
GL_QUERY_WAIT_NV = 0x8E13
GL_QUERY_NO_WAIT_NV = 0x8E14
GL_QUERY_BY_REGION_WAIT_NV = 0x8E15
GL_QUERY_BY_REGION_NO_WAIT_NV = 0x8E16
PFNGLBEGINCONDITIONALRENDERNVPROC = C(None, UInt, UInt)
PFNGLENDCONDITIONALRENDERNVPROC = C(None)
glBeginConditionalRenderNV = GL(
    'glBeginConditionalRenderNV', None, UInt, UInt
)
glEndConditionalRenderNV = GL('glEndConditionalRenderNV', None)
GL_NV_conservative_raster = 1
GL_CONSERVATIVE_RASTERIZATION_NV = 0x9346
GL_SUBPIXEL_PRECISION_BIAS_X_BITS_NV = 0x9347
GL_SUBPIXEL_PRECISION_BIAS_Y_BITS_NV = 0x9348
GL_MAX_SUBPIXEL_PRECISION_BIAS_BITS_NV = 0x9349
PFNGLSUBPIXELPRECISIONBIASNVPROC = C(None, UInt, UInt)
glSubpixelPrecisionBiasNV = GL('glSubpixelPrecisionBiasNV', None, UInt, UInt)
GL_NV_conservative_raster_dilate = 1
GL_CONSERVATIVE_RASTER_DILATE_NV = 0x9379
GL_CONSERVATIVE_RASTER_DILATE_RANGE_NV = 0x937A
GL_CONSERVATIVE_RASTER_DILATE_GRANULARITY_NV = 0x937B
PFNGLCONSERVATIVERASTERPARAMETERFNVPROC = C(None, UInt, Float)
glConservativeRasterParameterfNV = GL(
    'glConservativeRasterParameterfNV', None, UInt, Float
)
GL_NV_conservative_raster_pre_snap = 1
GL_CONSERVATIVE_RASTER_MODE_PRE_SNAP_NV = 0x9550
GL_NV_conservative_raster_pre_snap_triangles = 1
GL_CONSERVATIVE_RASTER_MODE_NV = 0x954D
GL_CONSERVATIVE_RASTER_MODE_POST_SNAP_NV = 0x954E
GL_CONSERVATIVE_RASTER_MODE_PRE_SNAP_TRIANGLES_NV = 0x954F
PFNGLCONSERVATIVERASTERPARAMETERINVPROC = C(None, UInt, Int)
glConservativeRasterParameteriNV = GL(
    'glConservativeRasterParameteriNV', None, UInt, Int
)
GL_NV_conservative_raster_underestimation = 1
GL_NV_depth_buffer_float = 1
GL_DEPTH_COMPONENT32F_NV = 0x8DAB
GL_DEPTH32F_STENCIL8_NV = 0x8DAC
GL_FLOAT_32_UNSIGNED_INT_24_8_REV_NV = 0x8DAD
GL_DEPTH_BUFFER_FLOAT_MODE_NV = 0x8DAF
PFNGLDEPTHRANGEDNVPROC = C(None, Double, Double)
PFNGLCLEARDEPTHDNVPROC = C(None, Double)
PFNGLDEPTHBOUNDSDNVPROC = C(None, Double, Double)
glDepthRangedNV = GL('glDepthRangedNV', None, Double, Double)
glClearDepthdNV = GL('glClearDepthdNV', None, Double)
glDepthBoundsdNV = GL('glDepthBoundsdNV', None, Double, Double)
GL_NV_draw_vulkan_image = 1
GLVULKANPROCNV = C(None)
PFNGLDRAWVKIMAGENVPROC = C(
    None, ULong, UInt, Float, Float, Float, Float, Float, Float, Float, Float,
    Float
)
PFNGLGETVKPROCADDRNVPROC = C(GLVULKANPROCNV, CharP)
PFNGLWAITVKSEMAPHORENVPROC = C(None, ULong)
PFNGLSIGNALVKSEMAPHORENVPROC = C(None, ULong)
PFNGLSIGNALVKFENCENVPROC = C(None, ULong)
glDrawVkImageNV = GL(
    'glDrawVkImageNV', None, ULong, UInt, Float, Float, Float, Float, Float,
    Float, Float, Float, Float
)
glGetVkProcAddrNV = GL('glGetVkProcAddrNV', GLVULKANPROCNV, CharP)
glWaitVkSemaphoreNV = GL('glWaitVkSemaphoreNV', None, ULong)
glSignalVkSemaphoreNV = GL('glSignalVkSemaphoreNV', None, ULong)
glSignalVkFenceNV = GL('glSignalVkFenceNV', None, ULong)
GL_NV_fill_rectangle = 1
GL_FILL_RECTANGLE_NV = 0x933C
GL_NV_fragment_coverage_to_color = 1
GL_FRAGMENT_COVERAGE_TO_COLOR_NV = 0x92DD
GL_FRAGMENT_COVERAGE_COLOR_NV = 0x92DE
PFNGLFRAGMENTCOVERAGECOLORNVPROC = C(None, UInt)
glFragmentCoverageColorNV = GL('glFragmentCoverageColorNV', None, UInt)
GL_NV_fragment_shader_barycentric = 1
GL_NV_fragment_shader_interlock = 1
GL_NV_framebuffer_mixed_samples = 1
GL_COVERAGE_MODULATION_TABLE_NV = 0x9331
GL_COLOR_SAMPLES_NV = 0x8E20
GL_DEPTH_SAMPLES_NV = 0x932D
GL_STENCIL_SAMPLES_NV = 0x932E
GL_MIXED_DEPTH_SAMPLES_SUPPORTED_NV = 0x932F
GL_MIXED_STENCIL_SAMPLES_SUPPORTED_NV = 0x9330
GL_COVERAGE_MODULATION_NV = 0x9332
GL_COVERAGE_MODULATION_TABLE_SIZE_NV = 0x9333
PFNGLCOVERAGEMODULATIONTABLENVPROC = C(None, Int, P(Float))
PFNGLGETCOVERAGEMODULATIONTABLENVPROC = C(None, Int, P(Float))
PFNGLCOVERAGEMODULATIONNVPROC = C(None, UInt)
glCoverageModulationTableNV = GL(
    'glCoverageModulationTableNV', None, Int, P(Float)
)
glGetCoverageModulationTableNV = GL(
    'glGetCoverageModulationTableNV', None, Int, P(Float)
)
glCoverageModulationNV = GL('glCoverageModulationNV', None, UInt)
GL_NV_framebuffer_multisample_coverage = 1
GL_RENDERBUFFER_COVERAGE_SAMPLES_NV = 0x8CAB
GL_RENDERBUFFER_COLOR_SAMPLES_NV = 0x8E10
GL_MAX_MULTISAMPLE_COVERAGE_MODES_NV = 0x8E11
GL_MULTISAMPLE_COVERAGE_MODES_NV = 0x8E12
PFNGLRENDERBUFFERSTORAGEMULTISAMPLECOVERAGENVPROC = C(
    None, UInt, Int, Int, UInt, Int, Int
)
glRenderbufferStorageMultisampleCoverageNV = GL(
    'glRenderbufferStorageMultisampleCoverageNV', None, UInt, Int, Int, UInt,
    Int, Int
)
GL_NV_geometry_shader_passthrough = 1
GL_NV_gpu_shader5 = 1
GL_INT64_NV = 0x140E
GL_UNSIGNED_INT64_NV = 0x140F
GL_INT8_NV = 0x8FE0
GL_INT8_VEC2_NV = 0x8FE1
GL_INT8_VEC3_NV = 0x8FE2
GL_INT8_VEC4_NV = 0x8FE3
GL_INT16_NV = 0x8FE4
GL_INT16_VEC2_NV = 0x8FE5
GL_INT16_VEC3_NV = 0x8FE6
GL_INT16_VEC4_NV = 0x8FE7
GL_INT64_VEC2_NV = 0x8FE9
GL_INT64_VEC3_NV = 0x8FEA
GL_INT64_VEC4_NV = 0x8FEB
GL_UNSIGNED_INT8_NV = 0x8FEC
GL_UNSIGNED_INT8_VEC2_NV = 0x8FED
GL_UNSIGNED_INT8_VEC3_NV = 0x8FEE
GL_UNSIGNED_INT8_VEC4_NV = 0x8FEF
GL_UNSIGNED_INT16_NV = 0x8FF0
GL_UNSIGNED_INT16_VEC2_NV = 0x8FF1
GL_UNSIGNED_INT16_VEC3_NV = 0x8FF2
GL_UNSIGNED_INT16_VEC4_NV = 0x8FF3
GL_UNSIGNED_INT64_VEC2_NV = 0x8FF5
GL_UNSIGNED_INT64_VEC3_NV = 0x8FF6
GL_UNSIGNED_INT64_VEC4_NV = 0x8FF7
GL_FLOAT16_NV = 0x8FF8
GL_FLOAT16_VEC2_NV = 0x8FF9
GL_FLOAT16_VEC3_NV = 0x8FFA
GL_FLOAT16_VEC4_NV = 0x8FFB
PFNGLUNIFORM1I64NVPROC = C(None, Int, Long)
PFNGLUNIFORM2I64NVPROC = C(None, Int, Long, Long)
PFNGLUNIFORM3I64NVPROC = C(None, Int, Long, Long, Long)
PFNGLUNIFORM4I64NVPROC = C(None, Int, Long, Long, Long, Long)
PFNGLUNIFORM1I64VNVPROC = C(None, Int, Int, P(Long))
PFNGLUNIFORM2I64VNVPROC = C(None, Int, Int, P(Long))
PFNGLUNIFORM3I64VNVPROC = C(None, Int, Int, P(Long))
PFNGLUNIFORM4I64VNVPROC = C(None, Int, Int, P(Long))
PFNGLUNIFORM1UI64NVPROC = C(None, Int, ULong)
PFNGLUNIFORM2UI64NVPROC = C(None, Int, ULong, ULong)
PFNGLUNIFORM3UI64NVPROC = C(None, Int, ULong, ULong, ULong)
PFNGLUNIFORM4UI64NVPROC = C(None, Int, ULong, ULong, ULong, ULong)
PFNGLUNIFORM1UI64VNVPROC = C(None, Int, Int, P(ULong))
PFNGLUNIFORM2UI64VNVPROC = C(None, Int, Int, P(ULong))
PFNGLUNIFORM3UI64VNVPROC = C(None, Int, Int, P(ULong))
PFNGLUNIFORM4UI64VNVPROC = C(None, Int, Int, P(ULong))
PFNGLGETUNIFORMI64VNVPROC = C(None, UInt, Int, P(Long))
PFNGLPROGRAMUNIFORM1I64NVPROC = C(None, UInt, Int, Long)
PFNGLPROGRAMUNIFORM2I64NVPROC = C(None, UInt, Int, Long, Long)
PFNGLPROGRAMUNIFORM3I64NVPROC = C(None, UInt, Int, Long, Long, Long)
PFNGLPROGRAMUNIFORM4I64NVPROC = C(None, UInt, Int, Long, Long, Long, Long)
PFNGLPROGRAMUNIFORM1I64VNVPROC = C(None, UInt, Int, Int, P(Long))
PFNGLPROGRAMUNIFORM2I64VNVPROC = C(None, UInt, Int, Int, P(Long))
PFNGLPROGRAMUNIFORM3I64VNVPROC = C(None, UInt, Int, Int, P(Long))
PFNGLPROGRAMUNIFORM4I64VNVPROC = C(None, UInt, Int, Int, P(Long))
PFNGLPROGRAMUNIFORM1UI64NVPROC = C(None, UInt, Int, ULong)
PFNGLPROGRAMUNIFORM2UI64NVPROC = C(None, UInt, Int, ULong, ULong)
PFNGLPROGRAMUNIFORM3UI64NVPROC = C(None, UInt, Int, ULong, ULong, ULong)
PFNGLPROGRAMUNIFORM4UI64NVPROC = C(
    None, UInt, Int, ULong, ULong, ULong, ULong
)
PFNGLPROGRAMUNIFORM1UI64VNVPROC = C(None, UInt, Int, Int, P(ULong))
PFNGLPROGRAMUNIFORM2UI64VNVPROC = C(None, UInt, Int, Int, P(ULong))
PFNGLPROGRAMUNIFORM3UI64VNVPROC = C(None, UInt, Int, Int, P(ULong))
PFNGLPROGRAMUNIFORM4UI64VNVPROC = C(None, UInt, Int, Int, P(ULong))
glUniform1i64NV = GL('glUniform1i64NV', None, Int, Long)
glUniform2i64NV = GL('glUniform2i64NV', None, Int, Long, Long)
glUniform3i64NV = GL('glUniform3i64NV', None, Int, Long, Long, Long)
glUniform4i64NV = GL('glUniform4i64NV', None, Int, Long, Long, Long, Long)
glUniform1i64vNV = GL('glUniform1i64vNV', None, Int, Int, P(Long))
glUniform2i64vNV = GL('glUniform2i64vNV', None, Int, Int, P(Long))
glUniform3i64vNV = GL('glUniform3i64vNV', None, Int, Int, P(Long))
glUniform4i64vNV = GL('glUniform4i64vNV', None, Int, Int, P(Long))
glUniform1ui64NV = GL('glUniform1ui64NV', None, Int, ULong)
glUniform2ui64NV = GL('glUniform2ui64NV', None, Int, ULong, ULong)
glUniform3ui64NV = GL('glUniform3ui64NV', None, Int, ULong, ULong, ULong)
glUniform4ui64NV = GL(
    'glUniform4ui64NV', None, Int, ULong, ULong, ULong, ULong
)
glUniform1ui64vNV = GL('glUniform1ui64vNV', None, Int, Int, P(ULong))
glUniform2ui64vNV = GL('glUniform2ui64vNV', None, Int, Int, P(ULong))
glUniform3ui64vNV = GL('glUniform3ui64vNV', None, Int, Int, P(ULong))
glUniform4ui64vNV = GL('glUniform4ui64vNV', None, Int, Int, P(ULong))
glGetUniformi64vNV = GL('glGetUniformi64vNV', None, UInt, Int, P(Long))
glProgramUniform1i64NV = GL('glProgramUniform1i64NV', None, UInt, Int, Long)
glProgramUniform2i64NV = GL(
    'glProgramUniform2i64NV', None, UInt, Int, Long, Long
)
glProgramUniform3i64NV = GL(
    'glProgramUniform3i64NV', None, UInt, Int, Long, Long, Long
)
glProgramUniform4i64NV = GL(
    'glProgramUniform4i64NV', None, UInt, Int, Long, Long, Long, Long
)
glProgramUniform1i64vNV = GL(
    'glProgramUniform1i64vNV', None, UInt, Int, Int, P(Long)
)
glProgramUniform2i64vNV = GL(
    'glProgramUniform2i64vNV', None, UInt, Int, Int, P(Long)
)
glProgramUniform3i64vNV = GL(
    'glProgramUniform3i64vNV', None, UInt, Int, Int, P(Long)
)
glProgramUniform4i64vNV = GL(
    'glProgramUniform4i64vNV', None, UInt, Int, Int, P(Long)
)
glProgramUniform1ui64NV = GL(
    'glProgramUniform1ui64NV', None, UInt, Int, ULong
)
glProgramUniform2ui64NV = GL(
    'glProgramUniform2ui64NV', None, UInt, Int, ULong, ULong
)
glProgramUniform3ui64NV = GL(
    'glProgramUniform3ui64NV', None, UInt, Int, ULong, ULong, ULong
)
glProgramUniform4ui64NV = GL(
    'glProgramUniform4ui64NV', None, UInt, Int, ULong, ULong, ULong, ULong
)
glProgramUniform1ui64vNV = GL(
    'glProgramUniform1ui64vNV', None, UInt, Int, Int, P(ULong)
)
glProgramUniform2ui64vNV = GL(
    'glProgramUniform2ui64vNV', None, UInt, Int, Int, P(ULong)
)
glProgramUniform3ui64vNV = GL(
    'glProgramUniform3ui64vNV', None, UInt, Int, Int, P(ULong)
)
glProgramUniform4ui64vNV = GL(
    'glProgramUniform4ui64vNV', None, UInt, Int, Int, P(ULong)
)
GL_NV_internalformat_sample_query = 1
GL_MULTISAMPLES_NV = 0x9371
GL_SUPERSAMPLE_SCALE_X_NV = 0x9372
GL_SUPERSAMPLE_SCALE_Y_NV = 0x9373
GL_CONFORMANT_NV = 0x9374
PFNGLGETINTERNALFORMATSAMPLEIVNVPROC = C(
    None, UInt, UInt, Int, UInt, Int, P(Int)
)
glGetInternalformatSampleivNV = GL(
    'glGetInternalformatSampleivNV', None, UInt, UInt, Int, UInt, Int, P(Int)
)
GL_NV_memory_attachment = 1
GL_ATTACHED_MEMORY_OBJECT_NV = 0x95A4
GL_ATTACHED_MEMORY_OFFSET_NV = 0x95A5
GL_MEMORY_ATTACHABLE_ALIGNMENT_NV = 0x95A6
GL_MEMORY_ATTACHABLE_SIZE_NV = 0x95A7
GL_MEMORY_ATTACHABLE_NV = 0x95A8
GL_DETACHED_MEMORY_INCARNATION_NV = 0x95A9
GL_DETACHED_TEXTURES_NV = 0x95AA
GL_DETACHED_BUFFERS_NV = 0x95AB
GL_MAX_DETACHED_TEXTURES_NV = 0x95AC
GL_MAX_DETACHED_BUFFERS_NV = 0x95AD
PFNGLGETMEMORYOBJECTDETACHEDRESOURCESUIVNVPROC = C(
    None, UInt, UInt, Int, Int, P(UInt)
)
PFNGLRESETMEMORYOBJECTPARAMETERNVPROC = C(None, UInt, UInt)
PFNGLTEXATTACHMEMORYNVPROC = C(None, UInt, UInt, ULong)
PFNGLBUFFERATTACHMEMORYNVPROC = C(None, UInt, UInt, ULong)
PFNGLTEXTUREATTACHMEMORYNVPROC = C(None, UInt, UInt, ULong)
PFNGLNAMEDBUFFERATTACHMEMORYNVPROC = C(None, UInt, UInt, ULong)
glGetMemoryObjectDetachedResourcesuivNV = GL(
    'glGetMemoryObjectDetachedResourcesuivNV', None, UInt, UInt, Int, Int,
    P(UInt)
)
glResetMemoryObjectParameterNV = GL(
    'glResetMemoryObjectParameterNV', None, UInt, UInt
)
glTexAttachMemoryNV = GL('glTexAttachMemoryNV', None, UInt, UInt, ULong)
glBufferAttachMemoryNV = GL('glBufferAttachMemoryNV', None, UInt, UInt, ULong)
glTextureAttachMemoryNV = GL(
    'glTextureAttachMemoryNV', None, UInt, UInt, ULong
)
glNamedBufferAttachMemoryNV = GL(
    'glNamedBufferAttachMemoryNV', None, UInt, UInt, ULong
)
GL_NV_memory_object_sparse = 1
PFNGLBUFFERPAGECOMMITMENTMEMNVPROC = C(
    None, UInt, Size, Size, UInt, ULong, UByte
)
PFNGLTEXPAGECOMMITMENTMEMNVPROC = C(
    None, UInt, Int, Int, Int, Int, Int, Int, Int, Int, UInt, ULong, UByte
)
PFNGLNAMEDBUFFERPAGECOMMITMENTMEMNVPROC = C(
    None, UInt, Size, Size, UInt, ULong, UByte
)
PFNGLTEXTUREPAGECOMMITMENTMEMNVPROC = C(
    None, UInt, Int, Int, Int, Int, Int, Int, Int, Int, UInt, ULong, UByte
)
glBufferPageCommitmentMemNV = GL(
    'glBufferPageCommitmentMemNV', None, UInt, Size, Size, UInt, ULong, UByte
)
glTexPageCommitmentMemNV = GL(
    'glTexPageCommitmentMemNV', None, UInt, Int, Int, Int, Int, Int, Int, Int,
    Int, UInt, ULong, UByte
)
glNamedBufferPageCommitmentMemNV = GL(
    'glNamedBufferPageCommitmentMemNV', None, UInt, Size, Size, UInt, ULong,
    UByte
)
glTexturePageCommitmentMemNV = GL(
    'glTexturePageCommitmentMemNV', None, UInt, Int, Int, Int, Int, Int, Int,
    Int, Int, UInt, ULong, UByte
)
GL_NV_mesh_shader = 1
GL_MESH_SHADER_NV = 0x9559
GL_TASK_SHADER_NV = 0x955A
GL_MAX_MESH_UNIFORM_BLOCKS_NV = 0x8E60
GL_MAX_MESH_TEXTURE_IMAGE_UNITS_NV = 0x8E61
GL_MAX_MESH_IMAGE_UNIFORMS_NV = 0x8E62
GL_MAX_MESH_UNIFORM_COMPONENTS_NV = 0x8E63
GL_MAX_MESH_ATOMIC_COUNTER_BUFFERS_NV = 0x8E64
GL_MAX_MESH_ATOMIC_COUNTERS_NV = 0x8E65
GL_MAX_MESH_SHADER_STORAGE_BLOCKS_NV = 0x8E66
GL_MAX_COMBINED_MESH_UNIFORM_COMPONENTS_NV = 0x8E67
GL_MAX_TASK_UNIFORM_BLOCKS_NV = 0x8E68
GL_MAX_TASK_TEXTURE_IMAGE_UNITS_NV = 0x8E69
GL_MAX_TASK_IMAGE_UNIFORMS_NV = 0x8E6A
GL_MAX_TASK_UNIFORM_COMPONENTS_NV = 0x8E6B
GL_MAX_TASK_ATOMIC_COUNTER_BUFFERS_NV = 0x8E6C
GL_MAX_TASK_ATOMIC_COUNTERS_NV = 0x8E6D
GL_MAX_TASK_SHADER_STORAGE_BLOCKS_NV = 0x8E6E
GL_MAX_COMBINED_TASK_UNIFORM_COMPONENTS_NV = 0x8E6F
GL_MAX_MESH_WORK_GROUP_INVOCATIONS_NV = 0x95A2
GL_MAX_TASK_WORK_GROUP_INVOCATIONS_NV = 0x95A3
GL_MAX_MESH_TOTAL_MEMORY_SIZE_NV = 0x9536
GL_MAX_TASK_TOTAL_MEMORY_SIZE_NV = 0x9537
GL_MAX_MESH_OUTPUT_VERTICES_NV = 0x9538
GL_MAX_MESH_OUTPUT_PRIMITIVES_NV = 0x9539
GL_MAX_TASK_OUTPUT_COUNT_NV = 0x953A
GL_MAX_DRAW_MESH_TASKS_COUNT_NV = 0x953D
GL_MAX_MESH_VIEWS_NV = 0x9557
GL_MESH_OUTPUT_PER_VERTEX_GRANULARITY_NV = 0x92DF
GL_MESH_OUTPUT_PER_PRIMITIVE_GRANULARITY_NV = 0x9543
GL_MAX_MESH_WORK_GROUP_SIZE_NV = 0x953B
GL_MAX_TASK_WORK_GROUP_SIZE_NV = 0x953C
GL_MESH_WORK_GROUP_SIZE_NV = 0x953E
GL_TASK_WORK_GROUP_SIZE_NV = 0x953F
GL_MESH_VERTICES_OUT_NV = 0x9579
GL_MESH_PRIMITIVES_OUT_NV = 0x957A
GL_MESH_OUTPUT_TYPE_NV = 0x957B
GL_UNIFORM_BLOCK_REFERENCED_BY_MESH_SHADER_NV = 0x959C
GL_UNIFORM_BLOCK_REFERENCED_BY_TASK_SHADER_NV = 0x959D
GL_REFERENCED_BY_MESH_SHADER_NV = 0x95A0
GL_REFERENCED_BY_TASK_SHADER_NV = 0x95A1
GL_MESH_SHADER_BIT_NV = 0x00000040
GL_TASK_SHADER_BIT_NV = 0x00000080
GL_MESH_SUBROUTINE_NV = 0x957C
GL_TASK_SUBROUTINE_NV = 0x957D
GL_MESH_SUBROUTINE_UNIFORM_NV = 0x957E
GL_TASK_SUBROUTINE_UNIFORM_NV = 0x957F
GL_ATOMIC_COUNTER_BUFFER_REFERENCED_BY_MESH_SHADER_NV = 0x959E
GL_ATOMIC_COUNTER_BUFFER_REFERENCED_BY_TASK_SHADER_NV = 0x959F
PFNGLDRAWMESHTASKSNVPROC = C(None, UInt, UInt)
PFNGLDRAWMESHTASKSINDIRECTNVPROC = C(None, Size)
PFNGLMULTIDRAWMESHTASKSINDIRECTNVPROC = C(None, Size, Int, Int)
PFNGLMULTIDRAWMESHTASKSINDIRECTCOUNTNVPROC = C(None, Size, Size, Int, Int)
glDrawMeshTasksNV = GL('glDrawMeshTasksNV', None, UInt, UInt)
glDrawMeshTasksIndirectNV = GL('glDrawMeshTasksIndirectNV', None, Size)
glMultiDrawMeshTasksIndirectNV = GL(
    'glMultiDrawMeshTasksIndirectNV', None, Size, Int, Int
)
glMultiDrawMeshTasksIndirectCountNV = GL(
    'glMultiDrawMeshTasksIndirectCountNV', None, Size, Size, Int, Int
)
GL_NV_path_rendering = 1
GL_PATH_FORMAT_SVG_NV = 0x9070
GL_PATH_FORMAT_PS_NV = 0x9071
GL_STANDARD_FONT_NAME_NV = 0x9072
GL_SYSTEM_FONT_NAME_NV = 0x9073
GL_FILE_NAME_NV = 0x9074
GL_PATH_STROKE_WIDTH_NV = 0x9075
GL_PATH_END_CAPS_NV = 0x9076
GL_PATH_INITIAL_END_CAP_NV = 0x9077
GL_PATH_TERMINAL_END_CAP_NV = 0x9078
GL_PATH_JOIN_STYLE_NV = 0x9079
GL_PATH_MITER_LIMIT_NV = 0x907A
GL_PATH_DASH_CAPS_NV = 0x907B
GL_PATH_INITIAL_DASH_CAP_NV = 0x907C
GL_PATH_TERMINAL_DASH_CAP_NV = 0x907D
GL_PATH_DASH_OFFSET_NV = 0x907E
GL_PATH_CLIENT_LENGTH_NV = 0x907F
GL_PATH_FILL_MODE_NV = 0x9080
GL_PATH_FILL_MASK_NV = 0x9081
GL_PATH_FILL_COVER_MODE_NV = 0x9082
GL_PATH_STROKE_COVER_MODE_NV = 0x9083
GL_PATH_STROKE_MASK_NV = 0x9084
GL_COUNT_UP_NV = 0x9088
GL_COUNT_DOWN_NV = 0x9089
GL_PATH_OBJECT_BOUNDING_BOX_NV = 0x908A
GL_CONVEX_HULL_NV = 0x908B
GL_BOUNDING_BOX_NV = 0x908D
GL_TRANSLATE_X_NV = 0x908E
GL_TRANSLATE_Y_NV = 0x908F
GL_TRANSLATE_2D_NV = 0x9090
GL_TRANSLATE_3D_NV = 0x9091
GL_AFFINE_2D_NV = 0x9092
GL_AFFINE_3D_NV = 0x9094
GL_TRANSPOSE_AFFINE_2D_NV = 0x9096
GL_TRANSPOSE_AFFINE_3D_NV = 0x9098
GL_UTF8_NV = 0x909A
GL_UTF16_NV = 0x909B
GL_BOUNDING_BOX_OF_BOUNDING_BOXES_NV = 0x909C
GL_PATH_COMMAND_COUNT_NV = 0x909D
GL_PATH_COORD_COUNT_NV = 0x909E
GL_PATH_DASH_ARRAY_COUNT_NV = 0x909F
GL_PATH_COMPUTED_LENGTH_NV = 0x90A0
GL_PATH_FILL_BOUNDING_BOX_NV = 0x90A1
GL_PATH_STROKE_BOUNDING_BOX_NV = 0x90A2
GL_SQUARE_NV = 0x90A3
GL_ROUND_NV = 0x90A4
GL_TRIANGULAR_NV = 0x90A5
GL_BEVEL_NV = 0x90A6
GL_MITER_REVERT_NV = 0x90A7
GL_MITER_TRUNCATE_NV = 0x90A8
GL_SKIP_MISSING_GLYPH_NV = 0x90A9
GL_USE_MISSING_GLYPH_NV = 0x90AA
GL_PATH_ERROR_POSITION_NV = 0x90AB
GL_ACCUM_ADJACENT_PAIRS_NV = 0x90AD
GL_ADJACENT_PAIRS_NV = 0x90AE
GL_FIRST_TO_REST_NV = 0x90AF
GL_PATH_GEN_MODE_NV = 0x90B0
GL_PATH_GEN_COEFF_NV = 0x90B1
GL_PATH_GEN_COMPONENTS_NV = 0x90B3
GL_PATH_STENCIL_FUNC_NV = 0x90B7
GL_PATH_STENCIL_REF_NV = 0x90B8
GL_PATH_STENCIL_VALUE_MASK_NV = 0x90B9
GL_PATH_STENCIL_DEPTH_OFFSET_FACTOR_NV = 0x90BD
GL_PATH_STENCIL_DEPTH_OFFSET_UNITS_NV = 0x90BE
GL_PATH_COVER_DEPTH_FUNC_NV = 0x90BF
GL_PATH_DASH_OFFSET_RESET_NV = 0x90B4
GL_MOVE_TO_RESETS_NV = 0x90B5
GL_MOVE_TO_CONTINUES_NV = 0x90B6
GL_CLOSE_PATH_NV = 0x00
GL_MOVE_TO_NV = 0x02
GL_RELATIVE_MOVE_TO_NV = 0x03
GL_LINE_TO_NV = 0x04
GL_RELATIVE_LINE_TO_NV = 0x05
GL_HORIZONTAL_LINE_TO_NV = 0x06
GL_RELATIVE_HORIZONTAL_LINE_TO_NV = 0x07
GL_VERTICAL_LINE_TO_NV = 0x08
GL_RELATIVE_VERTICAL_LINE_TO_NV = 0x09
GL_QUADRATIC_CURVE_TO_NV = 0x0A
GL_RELATIVE_QUADRATIC_CURVE_TO_NV = 0x0B
GL_CUBIC_CURVE_TO_NV = 0x0C
GL_RELATIVE_CUBIC_CURVE_TO_NV = 0x0D
GL_SMOOTH_QUADRATIC_CURVE_TO_NV = 0x0E
GL_RELATIVE_SMOOTH_QUADRATIC_CURVE_TO_NV = 0x0F
GL_SMOOTH_CUBIC_CURVE_TO_NV = 0x10
GL_RELATIVE_SMOOTH_CUBIC_CURVE_TO_NV = 0x11
GL_SMALL_CCW_ARC_TO_NV = 0x12
GL_RELATIVE_SMALL_CCW_ARC_TO_NV = 0x13
GL_SMALL_CW_ARC_TO_NV = 0x14
GL_RELATIVE_SMALL_CW_ARC_TO_NV = 0x15
GL_LARGE_CCW_ARC_TO_NV = 0x16
GL_RELATIVE_LARGE_CCW_ARC_TO_NV = 0x17
GL_LARGE_CW_ARC_TO_NV = 0x18
GL_RELATIVE_LARGE_CW_ARC_TO_NV = 0x19
GL_RESTART_PATH_NV = 0xF0
GL_DUP_FIRST_CUBIC_CURVE_TO_NV = 0xF2
GL_DUP_LAST_CUBIC_CURVE_TO_NV = 0xF4
GL_RECT_NV = 0xF6
GL_CIRCULAR_CCW_ARC_TO_NV = 0xF8
GL_CIRCULAR_CW_ARC_TO_NV = 0xFA
GL_CIRCULAR_TANGENT_ARC_TO_NV = 0xFC
GL_ARC_TO_NV = 0xFE
GL_RELATIVE_ARC_TO_NV = 0xFF
GL_BOLD_BIT_NV = 0x01
GL_ITALIC_BIT_NV = 0x02
GL_GLYPH_WIDTH_BIT_NV = 0x01
GL_GLYPH_HEIGHT_BIT_NV = 0x02
GL_GLYPH_HORIZONTAL_BEARING_X_BIT_NV = 0x04
GL_GLYPH_HORIZONTAL_BEARING_Y_BIT_NV = 0x08
GL_GLYPH_HORIZONTAL_BEARING_ADVANCE_BIT_NV = 0x10
GL_GLYPH_VERTICAL_BEARING_X_BIT_NV = 0x20
GL_GLYPH_VERTICAL_BEARING_Y_BIT_NV = 0x40
GL_GLYPH_VERTICAL_BEARING_ADVANCE_BIT_NV = 0x80
GL_GLYPH_HAS_KERNING_BIT_NV = 0x100
GL_FONT_X_MIN_BOUNDS_BIT_NV = 0x00010000
GL_FONT_Y_MIN_BOUNDS_BIT_NV = 0x00020000
GL_FONT_X_MAX_BOUNDS_BIT_NV = 0x00040000
GL_FONT_Y_MAX_BOUNDS_BIT_NV = 0x00080000
GL_FONT_UNITS_PER_EM_BIT_NV = 0x00100000
GL_FONT_ASCENDER_BIT_NV = 0x00200000
GL_FONT_DESCENDER_BIT_NV = 0x00400000
GL_FONT_HEIGHT_BIT_NV = 0x00800000
GL_FONT_MAX_ADVANCE_WIDTH_BIT_NV = 0x01000000
GL_FONT_MAX_ADVANCE_HEIGHT_BIT_NV = 0x02000000
GL_FONT_UNDERLINE_POSITION_BIT_NV = 0x04000000
GL_FONT_UNDERLINE_THICKNESS_BIT_NV = 0x08000000
GL_FONT_HAS_KERNING_BIT_NV = 0x10000000
GL_ROUNDED_RECT_NV = 0xE8
GL_RELATIVE_ROUNDED_RECT_NV = 0xE9
GL_ROUNDED_RECT2_NV = 0xEA
GL_RELATIVE_ROUNDED_RECT2_NV = 0xEB
GL_ROUNDED_RECT4_NV = 0xEC
GL_RELATIVE_ROUNDED_RECT4_NV = 0xED
GL_ROUNDED_RECT8_NV = 0xEE
GL_RELATIVE_ROUNDED_RECT8_NV = 0xEF
GL_RELATIVE_RECT_NV = 0xF7
GL_FONT_GLYPHS_AVAILABLE_NV = 0x9368
GL_FONT_TARGET_UNAVAILABLE_NV = 0x9369
GL_FONT_UNAVAILABLE_NV = 0x936A
GL_FONT_UNINTELLIGIBLE_NV = 0x936B
GL_CONIC_CURVE_TO_NV = 0x1A
GL_RELATIVE_CONIC_CURVE_TO_NV = 0x1B
GL_FONT_NUM_GLYPH_INDICES_BIT_NV = 0x20000000
GL_STANDARD_FONT_FORMAT_NV = 0x936C
GL_PATH_PROJECTION_NV = 0x1701
GL_PATH_MODELVIEW_NV = 0x1700
GL_PATH_MODELVIEW_STACK_DEPTH_NV = 0x0BA3
GL_PATH_MODELVIEW_MATRIX_NV = 0x0BA6
GL_PATH_MAX_MODELVIEW_STACK_DEPTH_NV = 0x0D36
GL_PATH_TRANSPOSE_MODELVIEW_MATRIX_NV = 0x84E3
GL_PATH_PROJECTION_STACK_DEPTH_NV = 0x0BA4
GL_PATH_PROJECTION_MATRIX_NV = 0x0BA7
GL_PATH_MAX_PROJECTION_STACK_DEPTH_NV = 0x0D38
GL_PATH_TRANSPOSE_PROJECTION_MATRIX_NV = 0x84E4
GL_FRAGMENT_INPUT_NV = 0x936D
PFNGLGENPATHSNVPROC = C(UInt, Int)
PFNGLDELETEPATHSNVPROC = C(None, UInt, Int)
PFNGLISPATHNVPROC = C(UByte, UInt)
PFNGLPATHCOMMANDSNVPROC = C(None, UInt, Int, P(UByte), Int, UInt, VoidP)
PFNGLPATHCOORDSNVPROC = C(None, UInt, Int, UInt, VoidP)
PFNGLPATHSUBCOMMANDSNVPROC = C(
    None, UInt, Int, Int, Int, P(UByte), Int, UInt, VoidP
)
PFNGLPATHSUBCOORDSNVPROC = C(None, UInt, Int, Int, UInt, VoidP)
PFNGLPATHSTRINGNVPROC = C(None, UInt, UInt, Int, VoidP)
PFNGLPATHGLYPHSNVPROC = C(
    None, UInt, UInt, VoidP, UInt, Int, UInt, VoidP, UInt, UInt, Float
)
PFNGLPATHGLYPHRANGENVPROC = C(
    None, UInt, UInt, VoidP, UInt, UInt, Int, UInt, UInt, Float
)
PFNGLWEIGHTPATHSNVPROC = C(None, UInt, Int, P(UInt), P(Float))
PFNGLCOPYPATHNVPROC = C(None, UInt, UInt)
PFNGLINTERPOLATEPATHSNVPROC = C(None, UInt, UInt, UInt, Float)
PFNGLTRANSFORMPATHNVPROC = C(None, UInt, UInt, UInt, P(Float))
PFNGLPATHPARAMETERIVNVPROC = C(None, UInt, UInt, P(Int))
PFNGLPATHPARAMETERINVPROC = C(None, UInt, UInt, Int)
PFNGLPATHPARAMETERFVNVPROC = C(None, UInt, UInt, P(Float))
PFNGLPATHPARAMETERFNVPROC = C(None, UInt, UInt, Float)
PFNGLPATHDASHARRAYNVPROC = C(None, UInt, Int, P(Float))
PFNGLPATHSTENCILFUNCNVPROC = C(None, UInt, Int, UInt)
PFNGLPATHSTENCILDEPTHOFFSETNVPROC = C(None, Float, Float)
PFNGLSTENCILFILLPATHNVPROC = C(None, UInt, UInt, UInt)
PFNGLSTENCILSTROKEPATHNVPROC = C(None, UInt, Int, UInt)
PFNGLSTENCILFILLPATHINSTANCEDNVPROC = C(
    None, Int, UInt, VoidP, UInt, UInt, UInt, UInt, P(Float)
)
PFNGLSTENCILSTROKEPATHINSTANCEDNVPROC = C(
    None, Int, UInt, VoidP, UInt, Int, UInt, UInt, P(Float)
)
PFNGLPATHCOVERDEPTHFUNCNVPROC = C(None, UInt)
PFNGLCOVERFILLPATHNVPROC = C(None, UInt, UInt)
PFNGLCOVERSTROKEPATHNVPROC = C(None, UInt, UInt)
PFNGLCOVERFILLPATHINSTANCEDNVPROC = C(
    None, Int, UInt, VoidP, UInt, UInt, UInt, P(Float)
)
PFNGLCOVERSTROKEPATHINSTANCEDNVPROC = C(
    None, Int, UInt, VoidP, UInt, UInt, UInt, P(Float)
)
PFNGLGETPATHPARAMETERIVNVPROC = C(None, UInt, UInt, P(Int))
PFNGLGETPATHPARAMETERFVNVPROC = C(None, UInt, UInt, P(Float))
PFNGLGETPATHCOMMANDSNVPROC = C(None, UInt, P(UByte))
PFNGLGETPATHCOORDSNVPROC = C(None, UInt, P(Float))
PFNGLGETPATHDASHARRAYNVPROC = C(None, UInt, P(Float))
PFNGLGETPATHMETRICSNVPROC = C(
    None, UInt, Int, UInt, VoidP, UInt, Int, P(Float)
)
PFNGLGETPATHMETRICRANGENVPROC = C(None, UInt, UInt, Int, Int, P(Float))
PFNGLGETPATHSPACINGNVPROC = C(
    None, UInt, Int, UInt, VoidP, UInt, Float, Float, UInt, P(Float)
)
PFNGLISPOINTINFILLPATHNVPROC = C(UByte, UInt, UInt, Float, Float)
PFNGLISPOINTINSTROKEPATHNVPROC = C(UByte, UInt, Float, Float)
PFNGLGETPATHLENGTHNVPROC = C(Float, UInt, Int, Int)
PFNGLPOINTALONGPATHNVPROC = C(
    UByte, UInt, Int, Int, Float, P(Float), P(Float), P(Float), P(Float)
)
PFNGLMATRIXLOAD3X2FNVPROC = C(None, UInt, P(Float))
PFNGLMATRIXLOAD3X3FNVPROC = C(None, UInt, P(Float))
PFNGLMATRIXLOADTRANSPOSE3X3FNVPROC = C(None, UInt, P(Float))
PFNGLMATRIXMULT3X2FNVPROC = C(None, UInt, P(Float))
PFNGLMATRIXMULT3X3FNVPROC = C(None, UInt, P(Float))
PFNGLMATRIXMULTTRANSPOSE3X3FNVPROC = C(None, UInt, P(Float))
PFNGLSTENCILTHENCOVERFILLPATHNVPROC = C(None, UInt, UInt, UInt, UInt)
PFNGLSTENCILTHENCOVERSTROKEPATHNVPROC = C(None, UInt, Int, UInt, UInt)
PFNGLSTENCILTHENCOVERFILLPATHINSTANCEDNVPROC = C(
    None, Int, UInt, VoidP, UInt, UInt, UInt, UInt, UInt, P(Float)
)
PFNGLSTENCILTHENCOVERSTROKEPATHINSTANCEDNVPROC = C(
    None, Int, UInt, VoidP, UInt, Int, UInt, UInt, UInt, P(Float)
)
PFNGLPATHGLYPHINDEXRANGENVPROC = C(
    UInt, UInt, VoidP, UInt, UInt, Float, P(UInt)
)
PFNGLPATHGLYPHINDEXARRAYNVPROC = C(
    UInt, UInt, UInt, VoidP, UInt, UInt, Int, UInt, Float
)
PFNGLPATHMEMORYGLYPHINDEXARRAYNVPROC = C(
    UInt, UInt, UInt, Size, VoidP, Int, UInt, Int, UInt, Float
)
PFNGLPROGRAMPATHFRAGMENTINPUTGENNVPROC = C(
    None, UInt, Int, UInt, Int, P(Float)
)
PFNGLGETPROGRAMRESOURCEFVNVPROC = C(
    None, UInt, UInt, UInt, Int, P(UInt), Int, P(Int), P(Float)
)
glGenPathsNV = GL('glGenPathsNV', UInt, Int)
glDeletePathsNV = GL('glDeletePathsNV', None, UInt, Int)
glIsPathNV = GL('glIsPathNV', UByte, UInt)
glPathCommandsNV = GL(
    'glPathCommandsNV', None, UInt, Int, P(UByte), Int, UInt, VoidP
)
glPathCoordsNV = GL('glPathCoordsNV', None, UInt, Int, UInt, VoidP)
glPathSubCommandsNV = GL(
    'glPathSubCommandsNV', None, UInt, Int, Int, Int, P(UByte), Int, UInt,
    VoidP
)
glPathSubCoordsNV = GL('glPathSubCoordsNV', None, UInt, Int, Int, UInt, VoidP)
glPathStringNV = GL('glPathStringNV', None, UInt, UInt, Int, VoidP)
glPathGlyphsNV = GL(
    'glPathGlyphsNV', None, UInt, UInt, VoidP, UInt, Int, UInt, VoidP, UInt,
    UInt, Float
)
glPathGlyphRangeNV = GL(
    'glPathGlyphRangeNV', None, UInt, UInt, VoidP, UInt, UInt, Int, UInt,
    UInt, Float
)
glWeightPathsNV = GL('glWeightPathsNV', None, UInt, Int, P(UInt), P(Float))
glCopyPathNV = GL('glCopyPathNV', None, UInt, UInt)
glInterpolatePathsNV = GL(
    'glInterpolatePathsNV', None, UInt, UInt, UInt, Float
)
glTransformPathNV = GL('glTransformPathNV', None, UInt, UInt, UInt, P(Float))
glPathParameterivNV = GL('glPathParameterivNV', None, UInt, UInt, P(Int))
glPathParameteriNV = GL('glPathParameteriNV', None, UInt, UInt, Int)
glPathParameterfvNV = GL('glPathParameterfvNV', None, UInt, UInt, P(Float))
glPathParameterfNV = GL('glPathParameterfNV', None, UInt, UInt, Float)
glPathDashArrayNV = GL('glPathDashArrayNV', None, UInt, Int, P(Float))
glPathStencilFuncNV = GL('glPathStencilFuncNV', None, UInt, Int, UInt)
glPathStencilDepthOffsetNV = GL(
    'glPathStencilDepthOffsetNV', None, Float, Float
)
glStencilFillPathNV = GL('glStencilFillPathNV', None, UInt, UInt, UInt)
glStencilStrokePathNV = GL('glStencilStrokePathNV', None, UInt, Int, UInt)
glStencilFillPathInstancedNV = GL(
    'glStencilFillPathInstancedNV', None, Int, UInt, VoidP, UInt, UInt, UInt,
    UInt, P(Float)
)
glStencilStrokePathInstancedNV = GL(
    'glStencilStrokePathInstancedNV', None, Int, UInt, VoidP, UInt, Int, UInt,
    UInt, P(Float)
)
glPathCoverDepthFuncNV = GL('glPathCoverDepthFuncNV', None, UInt)
glCoverFillPathNV = GL('glCoverFillPathNV', None, UInt, UInt)
glCoverStrokePathNV = GL('glCoverStrokePathNV', None, UInt, UInt)
glCoverFillPathInstancedNV = GL(
    'glCoverFillPathInstancedNV', None, Int, UInt, VoidP, UInt, UInt, UInt,
    P(Float)
)
glCoverStrokePathInstancedNV = GL(
    'glCoverStrokePathInstancedNV', None, Int, UInt, VoidP, UInt, UInt, UInt,
    P(Float)
)
glGetPathParameterivNV = GL(
    'glGetPathParameterivNV', None, UInt, UInt, P(Int)
)
glGetPathParameterfvNV = GL(
    'glGetPathParameterfvNV', None, UInt, UInt, P(Float)
)
glGetPathCommandsNV = GL('glGetPathCommandsNV', None, UInt, P(UByte))
glGetPathCoordsNV = GL('glGetPathCoordsNV', None, UInt, P(Float))
glGetPathDashArrayNV = GL('glGetPathDashArrayNV', None, UInt, P(Float))
glGetPathMetricsNV = GL(
    'glGetPathMetricsNV', None, UInt, Int, UInt, VoidP, UInt, Int, P(Float)
)
glGetPathMetricRangeNV = GL(
    'glGetPathMetricRangeNV', None, UInt, UInt, Int, Int, P(Float)
)
glGetPathSpacingNV = GL(
    'glGetPathSpacingNV', None, UInt, Int, UInt, VoidP, UInt, Float, Float,
    UInt, P(Float)
)
glIsPointInFillPathNV = GL(
    'glIsPointInFillPathNV', UByte, UInt, UInt, Float, Float
)
glIsPointInStrokePathNV = GL(
    'glIsPointInStrokePathNV', UByte, UInt, Float, Float
)
glGetPathLengthNV = GL('glGetPathLengthNV', Float, UInt, Int, Int)
glPointAlongPathNV = GL(
    'glPointAlongPathNV', UByte, UInt, Int, Int, Float, P(Float), P(Float),
    P(Float), P(Float)
)
glMatrixLoad3x2fNV = GL('glMatrixLoad3x2fNV', None, UInt, P(Float))
glMatrixLoad3x3fNV = GL('glMatrixLoad3x3fNV', None, UInt, P(Float))
glMatrixLoadTranspose3x3fNV = GL(
    'glMatrixLoadTranspose3x3fNV', None, UInt, P(Float)
)
glMatrixMult3x2fNV = GL('glMatrixMult3x2fNV', None, UInt, P(Float))
glMatrixMult3x3fNV = GL('glMatrixMult3x3fNV', None, UInt, P(Float))
glMatrixMultTranspose3x3fNV = GL(
    'glMatrixMultTranspose3x3fNV', None, UInt, P(Float)
)
glStencilThenCoverFillPathNV = GL(
    'glStencilThenCoverFillPathNV', None, UInt, UInt, UInt, UInt
)
glStencilThenCoverStrokePathNV = GL(
    'glStencilThenCoverStrokePathNV', None, UInt, Int, UInt, UInt
)
glStencilThenCoverFillPathInstancedNV = GL(
    'glStencilThenCoverFillPathInstancedNV', None, Int, UInt, VoidP, UInt,
    UInt, UInt, UInt, UInt, P(Float)
)
glStencilThenCoverStrokePathInstancedNV = GL(
    'glStencilThenCoverStrokePathInstancedNV', None, Int, UInt, VoidP, UInt,
    Int, UInt, UInt, UInt, P(Float)
)
glPathGlyphIndexRangeNV = GL(
    'glPathGlyphIndexRangeNV', UInt, UInt, VoidP, UInt, UInt, Float, P(UInt)
)
glPathGlyphIndexArrayNV = GL(
    'glPathGlyphIndexArrayNV', UInt, UInt, UInt, VoidP, UInt, UInt, Int, UInt,
    Float
)
glPathMemoryGlyphIndexArrayNV = GL(
    'glPathMemoryGlyphIndexArrayNV', UInt, UInt, UInt, Size, VoidP, Int, UInt,
    Int, UInt, Float
)
glProgramPathFragmentInputGenNV = GL(
    'glProgramPathFragmentInputGenNV', None, UInt, Int, UInt, Int, P(Float)
)
glGetProgramResourcefvNV = GL(
    'glGetProgramResourcefvNV', None, UInt, UInt, UInt, Int, P(UInt), Int,
    P(Int), P(Float)
)
GL_NV_path_rendering_shared_edge = 1
GL_SHARED_EDGE_NV = 0xC0
GL_NV_primitive_shading_rate = 1
GL_SHADING_RATE_IMAGE_PER_PRIMITIVE_NV = 0x95B1
GL_SHADING_RATE_IMAGE_PALETTE_COUNT_NV = 0x95B2
GL_NV_representative_fragment_test = 1
GL_REPRESENTATIVE_FRAGMENT_TEST_NV = 0x937F
GL_NV_sample_locations = 1
GL_SAMPLE_LOCATION_SUBPIXEL_BITS_NV = 0x933D
GL_SAMPLE_LOCATION_PIXEL_GRID_WIDTH_NV = 0x933E
GL_SAMPLE_LOCATION_PIXEL_GRID_HEIGHT_NV = 0x933F
GL_PROGRAMMABLE_SAMPLE_LOCATION_TABLE_SIZE_NV = 0x9340
GL_SAMPLE_LOCATION_NV = 0x8E50
GL_PROGRAMMABLE_SAMPLE_LOCATION_NV = 0x9341
GL_FRAMEBUFFER_PROGRAMMABLE_SAMPLE_LOCATIONS_NV = 0x9342
GL_FRAMEBUFFER_SAMPLE_LOCATION_PIXEL_GRID_NV = 0x9343
PFNGLFRAMEBUFFERSAMPLELOCATIONSFVNVPROC = C(None, UInt, UInt, Int, P(Float))
PFNGLNAMEDFRAMEBUFFERSAMPLELOCATIONSFVNVPROC = C(
    None, UInt, UInt, Int, P(Float)
)
PFNGLRESOLVEDEPTHVALUESNVPROC = C(None)
glFramebufferSampleLocationsfvNV = GL(
    'glFramebufferSampleLocationsfvNV', None, UInt, UInt, Int, P(Float)
)
glNamedFramebufferSampleLocationsfvNV = GL(
    'glNamedFramebufferSampleLocationsfvNV', None, UInt, UInt, Int, P(Float)
)
glResolveDepthValuesNV = GL('glResolveDepthValuesNV', None)
GL_NV_sample_mask_override_coverage = 1
GL_NV_scissor_exclusive = 1
GL_SCISSOR_TEST_EXCLUSIVE_NV = 0x9555
GL_SCISSOR_BOX_EXCLUSIVE_NV = 0x9556
PFNGLSCISSOREXCLUSIVENVPROC = C(None, Int, Int, Int, Int)
PFNGLSCISSOREXCLUSIVEARRAYVNVPROC = C(None, UInt, Int, P(Int))
glScissorExclusiveNV = GL('glScissorExclusiveNV', None, Int, Int, Int, Int)
glScissorExclusiveArrayvNV = GL(
    'glScissorExclusiveArrayvNV', None, UInt, Int, P(Int)
)
GL_NV_shader_atomic_counters = 1
GL_NV_shader_atomic_float = 1
GL_NV_shader_atomic_float64 = 1
GL_NV_shader_atomic_fp16_vector = 1
GL_NV_shader_atomic_int64 = 1
GL_NV_shader_buffer_load = 1
GL_BUFFER_GPU_ADDRESS_NV = 0x8F1D
GL_GPU_ADDRESS_NV = 0x8F34
GL_MAX_SHADER_BUFFER_ADDRESS_NV = 0x8F35
PFNGLMAKEBUFFERRESIDENTNVPROC = C(None, UInt, UInt)
PFNGLMAKEBUFFERNONRESIDENTNVPROC = C(None, UInt)
PFNGLISBUFFERRESIDENTNVPROC = C(UByte, UInt)
PFNGLMAKENAMEDBUFFERRESIDENTNVPROC = C(None, UInt, UInt)
PFNGLMAKENAMEDBUFFERNONRESIDENTNVPROC = C(None, UInt)
PFNGLISNAMEDBUFFERRESIDENTNVPROC = C(UByte, UInt)
PFNGLGETBUFFERPARAMETERUI64VNVPROC = C(None, UInt, UInt, P(ULong))
PFNGLGETNAMEDBUFFERPARAMETERUI64VNVPROC = C(None, UInt, UInt, P(ULong))
PFNGLGETINTEGERUI64VNVPROC = C(None, UInt, P(ULong))
PFNGLUNIFORMUI64NVPROC = C(None, Int, ULong)
PFNGLUNIFORMUI64VNVPROC = C(None, Int, Int, P(ULong))
PFNGLGETUNIFORMUI64VNVPROC = C(None, UInt, Int, P(ULong))
PFNGLPROGRAMUNIFORMUI64NVPROC = C(None, UInt, Int, ULong)
PFNGLPROGRAMUNIFORMUI64VNVPROC = C(None, UInt, Int, Int, P(ULong))
glMakeBufferResidentNV = GL('glMakeBufferResidentNV', None, UInt, UInt)
glMakeBufferNonResidentNV = GL('glMakeBufferNonResidentNV', None, UInt)
glIsBufferResidentNV = GL('glIsBufferResidentNV', UByte, UInt)
glMakeNamedBufferResidentNV = GL(
    'glMakeNamedBufferResidentNV', None, UInt, UInt
)
glMakeNamedBufferNonResidentNV = GL(
    'glMakeNamedBufferNonResidentNV', None, UInt
)
glIsNamedBufferResidentNV = GL('glIsNamedBufferResidentNV', UByte, UInt)
glGetBufferParameterui64vNV = GL(
    'glGetBufferParameterui64vNV', None, UInt, UInt, P(ULong)
)
glGetNamedBufferParameterui64vNV = GL(
    'glGetNamedBufferParameterui64vNV', None, UInt, UInt, P(ULong)
)
glGetIntegerui64vNV = GL('glGetIntegerui64vNV', None, UInt, P(ULong))
glUniformui64NV = GL('glUniformui64NV', None, Int, ULong)
glUniformui64vNV = GL('glUniformui64vNV', None, Int, Int, P(ULong))
glGetUniformui64vNV = GL('glGetUniformui64vNV', None, UInt, Int, P(ULong))
glProgramUniformui64NV = GL('glProgramUniformui64NV', None, UInt, Int, ULong)
glProgramUniformui64vNV = GL(
    'glProgramUniformui64vNV', None, UInt, Int, Int, P(ULong)
)
GL_NV_shader_buffer_store = 1
GL_SHADER_GLOBAL_ACCESS_BARRIER_BIT_NV = 0x00000010
GL_NV_shader_subgroup_partitioned = 1
GL_SUBGROUP_FEATURE_PARTITIONED_BIT_NV = 0x00000100
GL_NV_shader_texture_footprint = 1
GL_NV_shader_thread_group = 1
GL_WARP_SIZE_NV = 0x9339
GL_WARPS_PER_SM_NV = 0x933A
GL_SM_COUNT_NV = 0x933B
GL_NV_shader_thread_shuffle = 1
GL_NV_shading_rate_image = 1
GL_SHADING_RATE_IMAGE_NV = 0x9563
GL_SHADING_RATE_NO_INVOCATIONS_NV = 0x9564
GL_SHADING_RATE_1_INVOCATION_PER_PIXEL_NV = 0x9565
GL_SHADING_RATE_1_INVOCATION_PER_1X2_PIXELS_NV = 0x9566
GL_SHADING_RATE_1_INVOCATION_PER_2X1_PIXELS_NV = 0x9567
GL_SHADING_RATE_1_INVOCATION_PER_2X2_PIXELS_NV = 0x9568
GL_SHADING_RATE_1_INVOCATION_PER_2X4_PIXELS_NV = 0x9569
GL_SHADING_RATE_1_INVOCATION_PER_4X2_PIXELS_NV = 0x956A
GL_SHADING_RATE_1_INVOCATION_PER_4X4_PIXELS_NV = 0x956B
GL_SHADING_RATE_2_INVOCATIONS_PER_PIXEL_NV = 0x956C
GL_SHADING_RATE_4_INVOCATIONS_PER_PIXEL_NV = 0x956D
GL_SHADING_RATE_8_INVOCATIONS_PER_PIXEL_NV = 0x956E
GL_SHADING_RATE_16_INVOCATIONS_PER_PIXEL_NV = 0x956F
GL_SHADING_RATE_IMAGE_BINDING_NV = 0x955B
GL_SHADING_RATE_IMAGE_TEXEL_WIDTH_NV = 0x955C
GL_SHADING_RATE_IMAGE_TEXEL_HEIGHT_NV = 0x955D
GL_SHADING_RATE_IMAGE_PALETTE_SIZE_NV = 0x955E
GL_MAX_COARSE_FRAGMENT_SAMPLES_NV = 0x955F
GL_SHADING_RATE_SAMPLE_ORDER_DEFAULT_NV = 0x95AE
GL_SHADING_RATE_SAMPLE_ORDER_PIXEL_MAJOR_NV = 0x95AF
GL_SHADING_RATE_SAMPLE_ORDER_SAMPLE_MAJOR_NV = 0x95B0
PFNGLBINDSHADINGRATEIMAGENVPROC = C(None, UInt)
PFNGLGETSHADINGRATEIMAGEPALETTENVPROC = C(None, UInt, UInt, P(UInt))
PFNGLGETSHADINGRATESAMPLELOCATIONIVNVPROC = C(None, UInt, UInt, UInt, P(Int))
PFNGLSHADINGRATEIMAGEBARRIERNVPROC = C(None, UByte)
PFNGLSHADINGRATEIMAGEPALETTENVPROC = C(None, UInt, UInt, Int, P(UInt))
PFNGLSHADINGRATESAMPLEORDERNVPROC = C(None, UInt)
PFNGLSHADINGRATESAMPLEORDERCUSTOMNVPROC = C(None, UInt, UInt, P(Int))
glBindShadingRateImageNV = GL('glBindShadingRateImageNV', None, UInt)
glGetShadingRateImagePaletteNV = GL(
    'glGetShadingRateImagePaletteNV', None, UInt, UInt, P(UInt)
)
glGetShadingRateSampleLocationivNV = GL(
    'glGetShadingRateSampleLocationivNV', None, UInt, UInt, UInt, P(Int)
)
glShadingRateImageBarrierNV = GL('glShadingRateImageBarrierNV', None, UByte)
glShadingRateImagePaletteNV = GL(
    'glShadingRateImagePaletteNV', None, UInt, UInt, Int, P(UInt)
)
glShadingRateSampleOrderNV = GL('glShadingRateSampleOrderNV', None, UInt)
glShadingRateSampleOrderCustomNV = GL(
    'glShadingRateSampleOrderCustomNV', None, UInt, UInt, P(Int)
)
GL_NV_stereo_view_rendering = 1
GL_NV_texture_barrier = 1
PFNGLTEXTUREBARRIERNVPROC = C(None)
glTextureBarrierNV = GL('glTextureBarrierNV', None)
GL_NV_texture_rectangle_compressed = 1
GL_NV_uniform_buffer_unified_memory = 1
GL_UNIFORM_BUFFER_UNIFIED_NV = 0x936E
GL_UNIFORM_BUFFER_ADDRESS_NV = 0x936F
GL_UNIFORM_BUFFER_LENGTH_NV = 0x9370
GL_NV_vertex_attrib_integer_64bit = 1
PFNGLVERTEXATTRIBL1I64NVPROC = C(None, UInt, Long)
PFNGLVERTEXATTRIBL2I64NVPROC = C(None, UInt, Long, Long)
PFNGLVERTEXATTRIBL3I64NVPROC = C(None, UInt, Long, Long, Long)
PFNGLVERTEXATTRIBL4I64NVPROC = C(None, UInt, Long, Long, Long, Long)
PFNGLVERTEXATTRIBL1I64VNVPROC = C(None, UInt, P(Long))
PFNGLVERTEXATTRIBL2I64VNVPROC = C(None, UInt, P(Long))
PFNGLVERTEXATTRIBL3I64VNVPROC = C(None, UInt, P(Long))
PFNGLVERTEXATTRIBL4I64VNVPROC = C(None, UInt, P(Long))
PFNGLVERTEXATTRIBL1UI64NVPROC = C(None, UInt, ULong)
PFNGLVERTEXATTRIBL2UI64NVPROC = C(None, UInt, ULong, ULong)
PFNGLVERTEXATTRIBL3UI64NVPROC = C(None, UInt, ULong, ULong, ULong)
PFNGLVERTEXATTRIBL4UI64NVPROC = C(None, UInt, ULong, ULong, ULong, ULong)
PFNGLVERTEXATTRIBL1UI64VNVPROC = C(None, UInt, P(ULong))
PFNGLVERTEXATTRIBL2UI64VNVPROC = C(None, UInt, P(ULong))
PFNGLVERTEXATTRIBL3UI64VNVPROC = C(None, UInt, P(ULong))
PFNGLVERTEXATTRIBL4UI64VNVPROC = C(None, UInt, P(ULong))
PFNGLGETVERTEXATTRIBLI64VNVPROC = C(None, UInt, UInt, P(Long))
PFNGLGETVERTEXATTRIBLUI64VNVPROC = C(None, UInt, UInt, P(ULong))
PFNGLVERTEXATTRIBLFORMATNVPROC = C(None, UInt, Int, UInt, Int)
glVertexAttribL1i64NV = GL('glVertexAttribL1i64NV', None, UInt, Long)
glVertexAttribL2i64NV = GL('glVertexAttribL2i64NV', None, UInt, Long, Long)
glVertexAttribL3i64NV = GL(
    'glVertexAttribL3i64NV', None, UInt, Long, Long, Long
)
glVertexAttribL4i64NV = GL(
    'glVertexAttribL4i64NV', None, UInt, Long, Long, Long, Long
)
glVertexAttribL1i64vNV = GL('glVertexAttribL1i64vNV', None, UInt, P(Long))
glVertexAttribL2i64vNV = GL('glVertexAttribL2i64vNV', None, UInt, P(Long))
glVertexAttribL3i64vNV = GL('glVertexAttribL3i64vNV', None, UInt, P(Long))
glVertexAttribL4i64vNV = GL('glVertexAttribL4i64vNV', None, UInt, P(Long))
glVertexAttribL1ui64NV = GL('glVertexAttribL1ui64NV', None, UInt, ULong)
glVertexAttribL2ui64NV = GL(
    'glVertexAttribL2ui64NV', None, UInt, ULong, ULong
)
glVertexAttribL3ui64NV = GL(
    'glVertexAttribL3ui64NV', None, UInt, ULong, ULong, ULong
)
glVertexAttribL4ui64NV = GL(
    'glVertexAttribL4ui64NV', None, UInt, ULong, ULong, ULong, ULong
)
glVertexAttribL1ui64vNV = GL('glVertexAttribL1ui64vNV', None, UInt, P(ULong))
glVertexAttribL2ui64vNV = GL('glVertexAttribL2ui64vNV', None, UInt, P(ULong))
glVertexAttribL3ui64vNV = GL('glVertexAttribL3ui64vNV', None, UInt, P(ULong))
glVertexAttribL4ui64vNV = GL('glVertexAttribL4ui64vNV', None, UInt, P(ULong))
glGetVertexAttribLi64vNV = GL(
    'glGetVertexAttribLi64vNV', None, UInt, UInt, P(Long)
)
glGetVertexAttribLui64vNV = GL(
    'glGetVertexAttribLui64vNV', None, UInt, UInt, P(ULong)
)
glVertexAttribLFormatNV = GL(
    'glVertexAttribLFormatNV', None, UInt, Int, UInt, Int
)
GL_NV_vertex_buffer_unified_memory = 1
GL_VERTEX_ATTRIB_ARRAY_UNIFIED_NV = 0x8F1E
GL_ELEMENT_ARRAY_UNIFIED_NV = 0x8F1F
GL_VERTEX_ATTRIB_ARRAY_ADDRESS_NV = 0x8F20
GL_VERTEX_ARRAY_ADDRESS_NV = 0x8F21
GL_NORMAL_ARRAY_ADDRESS_NV = 0x8F22
GL_COLOR_ARRAY_ADDRESS_NV = 0x8F23
GL_INDEX_ARRAY_ADDRESS_NV = 0x8F24
GL_TEXTURE_COORD_ARRAY_ADDRESS_NV = 0x8F25
GL_EDGE_FLAG_ARRAY_ADDRESS_NV = 0x8F26
GL_SECONDARY_COLOR_ARRAY_ADDRESS_NV = 0x8F27
GL_FOG_COORD_ARRAY_ADDRESS_NV = 0x8F28
GL_ELEMENT_ARRAY_ADDRESS_NV = 0x8F29
GL_VERTEX_ATTRIB_ARRAY_LENGTH_NV = 0x8F2A
GL_VERTEX_ARRAY_LENGTH_NV = 0x8F2B
GL_NORMAL_ARRAY_LENGTH_NV = 0x8F2C
GL_COLOR_ARRAY_LENGTH_NV = 0x8F2D
GL_INDEX_ARRAY_LENGTH_NV = 0x8F2E
GL_TEXTURE_COORD_ARRAY_LENGTH_NV = 0x8F2F
GL_EDGE_FLAG_ARRAY_LENGTH_NV = 0x8F30
GL_SECONDARY_COLOR_ARRAY_LENGTH_NV = 0x8F31
GL_FOG_COORD_ARRAY_LENGTH_NV = 0x8F32
GL_ELEMENT_ARRAY_LENGTH_NV = 0x8F33
GL_DRAW_INDIRECT_UNIFIED_NV = 0x8F40
GL_DRAW_INDIRECT_ADDRESS_NV = 0x8F41
GL_DRAW_INDIRECT_LENGTH_NV = 0x8F42
PFNGLBUFFERADDRESSRANGENVPROC = C(None, UInt, UInt, ULong, Size)
PFNGLVERTEXFORMATNVPROC = C(None, Int, UInt, Int)
PFNGLNORMALFORMATNVPROC = C(None, UInt, Int)
PFNGLCOLORFORMATNVPROC = C(None, Int, UInt, Int)
PFNGLINDEXFORMATNVPROC = C(None, UInt, Int)
PFNGLTEXCOORDFORMATNVPROC = C(None, Int, UInt, Int)
PFNGLEDGEFLAGFORMATNVPROC = C(None, Int)
PFNGLSECONDARYCOLORFORMATNVPROC = C(None, Int, UInt, Int)
PFNGLFOGCOORDFORMATNVPROC = C(None, UInt, Int)
PFNGLVERTEXATTRIBFORMATNVPROC = C(None, UInt, Int, UInt, UByte, Int)
PFNGLVERTEXATTRIBIFORMATNVPROC = C(None, UInt, Int, UInt, Int)
PFNGLGETINTEGERUI64I_VNVPROC = C(None, UInt, UInt, P(ULong))
glBufferAddressRangeNV = GL(
    'glBufferAddressRangeNV', None, UInt, UInt, ULong, Size
)
glVertexFormatNV = GL('glVertexFormatNV', None, Int, UInt, Int)
glNormalFormatNV = GL('glNormalFormatNV', None, UInt, Int)
glColorFormatNV = GL('glColorFormatNV', None, Int, UInt, Int)
glIndexFormatNV = GL('glIndexFormatNV', None, UInt, Int)
glTexCoordFormatNV = GL('glTexCoordFormatNV', None, Int, UInt, Int)
glEdgeFlagFormatNV = GL('glEdgeFlagFormatNV', None, Int)
glSecondaryColorFormatNV = GL(
    'glSecondaryColorFormatNV', None, Int, UInt, Int
)
glFogCoordFormatNV = GL('glFogCoordFormatNV', None, UInt, Int)
glVertexAttribFormatNV = GL(
    'glVertexAttribFormatNV', None, UInt, Int, UInt, UByte, Int
)
glVertexAttribIFormatNV = GL(
    'glVertexAttribIFormatNV', None, UInt, Int, UInt, Int
)
glGetIntegerui64i_vNV = GL(
    'glGetIntegerui64i_vNV', None, UInt, UInt, P(ULong)
)
GL_NV_viewport_array2 = 1
GL_NV_viewport_swizzle = 1
GL_VIEWPORT_SWIZZLE_POSITIVE_X_NV = 0x9350
GL_VIEWPORT_SWIZZLE_NEGATIVE_X_NV = 0x9351
GL_VIEWPORT_SWIZZLE_POSITIVE_Y_NV = 0x9352
GL_VIEWPORT_SWIZZLE_NEGATIVE_Y_NV = 0x9353
GL_VIEWPORT_SWIZZLE_POSITIVE_Z_NV = 0x9354
GL_VIEWPORT_SWIZZLE_NEGATIVE_Z_NV = 0x9355
GL_VIEWPORT_SWIZZLE_POSITIVE_W_NV = 0x9356
GL_VIEWPORT_SWIZZLE_NEGATIVE_W_NV = 0x9357
GL_VIEWPORT_SWIZZLE_X_NV = 0x9358
GL_VIEWPORT_SWIZZLE_Y_NV = 0x9359
GL_VIEWPORT_SWIZZLE_Z_NV = 0x935A
GL_VIEWPORT_SWIZZLE_W_NV = 0x935B
PFNGLVIEWPORTSWIZZLENVPROC = C(None, UInt, UInt, UInt, UInt, UInt)
glViewportSwizzleNV = GL(
    'glViewportSwizzleNV', None, UInt, UInt, UInt, UInt, UInt
)

__all__ = [
    'GL_NV_bindless_multi_draw_indirect',
    'PFNGLMULTIDRAWARRAYSINDIRECTBINDLESSNVPROC',
    'PFNGLMULTIDRAWELEMENTSINDIRECTBINDLESSNVPROC',
    'glMultiDrawArraysIndirectBindlessNV',
    'glMultiDrawElementsIndirectBindlessNV',
    'GL_NV_bindless_multi_draw_indirect_count',
    'PFNGLMULTIDRAWARRAYSINDIRECTBINDLESSCOUNTNVPROC',
    'PFNGLMULTIDRAWELEMENTSINDIRECTBINDLESSCOUNTNVPROC',
    'glMultiDrawArraysIndirectBindlessCountNV',
    'glMultiDrawElementsIndirectBindlessCountNV', 'GL_NV_bindless_texture',
    'PFNGLGETTEXTUREHANDLENVPROC', 'PFNGLGETTEXTURESAMPLERHANDLENVPROC',
    'PFNGLMAKETEXTUREHANDLERESIDENTNVPROC',
    'PFNGLMAKETEXTUREHANDLENONRESIDENTNVPROC', 'PFNGLGETIMAGEHANDLENVPROC',
    'PFNGLMAKEIMAGEHANDLERESIDENTNVPROC',
    'PFNGLMAKEIMAGEHANDLENONRESIDENTNVPROC', 'PFNGLUNIFORMHANDLEUI64NVPROC',
    'PFNGLUNIFORMHANDLEUI64VNVPROC', 'PFNGLPROGRAMUNIFORMHANDLEUI64NVPROC',
    'PFNGLPROGRAMUNIFORMHANDLEUI64VNVPROC',
    'PFNGLISTEXTUREHANDLERESIDENTNVPROC', 'PFNGLISIMAGEHANDLERESIDENTNVPROC',
    'glGetTextureHandleNV', 'glGetTextureSamplerHandleNV',
    'glMakeTextureHandleResidentNV', 'glMakeTextureHandleNonResidentNV',
    'glGetImageHandleNV', 'glMakeImageHandleResidentNV',
    'glMakeImageHandleNonResidentNV', 'glUniformHandleui64NV',
    'glUniformHandleui64vNV', 'glProgramUniformHandleui64NV',
    'glProgramUniformHandleui64vNV', 'glIsTextureHandleResidentNV',
    'glIsImageHandleResidentNV', 'GL_NV_blend_equation_advanced',
    'GL_BLEND_OVERLAP_NV', 'GL_BLEND_PREMULTIPLIED_SRC_NV', 'GL_BLUE_NV',
    'GL_COLORBURN_NV', 'GL_COLORDODGE_NV', 'GL_CONJOINT_NV', 'GL_CONTRAST_NV',
    'GL_DARKEN_NV', 'GL_DIFFERENCE_NV', 'GL_DISJOINT_NV', 'GL_DST_ATOP_NV',
    'GL_DST_IN_NV', 'GL_DST_NV', 'GL_DST_OUT_NV', 'GL_DST_OVER_NV',
    'GL_EXCLUSION_NV', 'GL_GREEN_NV', 'GL_HARDLIGHT_NV', 'GL_HARDMIX_NV',
    'GL_HSL_COLOR_NV', 'GL_HSL_HUE_NV', 'GL_HSL_LUMINOSITY_NV',
    'GL_HSL_SATURATION_NV', 'GL_INVERT_OVG_NV', 'GL_INVERT_RGB_NV',
    'GL_LIGHTEN_NV', 'GL_LINEARBURN_NV', 'GL_LINEARDODGE_NV',
    'GL_LINEARLIGHT_NV', 'GL_MINUS_CLAMPED_NV', 'GL_MINUS_NV',
    'GL_MULTIPLY_NV', 'GL_OVERLAY_NV', 'GL_PINLIGHT_NV',
    'GL_PLUS_CLAMPED_ALPHA_NV', 'GL_PLUS_CLAMPED_NV', 'GL_PLUS_DARKER_NV',
    'GL_PLUS_NV', 'GL_RED_NV', 'GL_SCREEN_NV', 'GL_SOFTLIGHT_NV',
    'GL_SRC_ATOP_NV', 'GL_SRC_IN_NV', 'GL_SRC_NV', 'GL_SRC_OUT_NV',
    'GL_SRC_OVER_NV', 'GL_UNCORRELATED_NV', 'GL_VIVIDLIGHT_NV', 'GL_XOR_NV',
    'PFNGLBLENDPARAMETERINVPROC', 'PFNGLBLENDBARRIERNVPROC',
    'glBlendParameteriNV', 'glBlendBarrierNV',
    'GL_NV_blend_equation_advanced_coherent', 'GL_BLEND_ADVANCED_COHERENT_NV',
    'GL_NV_blend_minmax_factor', 'GL_FACTOR_MIN_AMD', 'GL_FACTOR_MAX_AMD',
    'GL_NV_clip_space_w_scaling', 'GL_VIEWPORT_POSITION_W_SCALE_NV',
    'GL_VIEWPORT_POSITION_W_SCALE_X_COEFF_NV',
    'GL_VIEWPORT_POSITION_W_SCALE_Y_COEFF_NV',
    'PFNGLVIEWPORTPOSITIONWSCALENVPROC', 'glViewportPositionWScaleNV',
    'GL_NV_command_list', 'GL_TERMINATE_SEQUENCE_COMMAND_NV',
    'GL_NOP_COMMAND_NV', 'GL_DRAW_ELEMENTS_COMMAND_NV',
    'GL_DRAW_ARRAYS_COMMAND_NV', 'GL_DRAW_ELEMENTS_STRIP_COMMAND_NV',
    'GL_DRAW_ARRAYS_STRIP_COMMAND_NV',
    'GL_DRAW_ELEMENTS_INSTANCED_COMMAND_NV',
    'GL_DRAW_ARRAYS_INSTANCED_COMMAND_NV', 'GL_ELEMENT_ADDRESS_COMMAND_NV',
    'GL_ATTRIBUTE_ADDRESS_COMMAND_NV', 'GL_UNIFORM_ADDRESS_COMMAND_NV',
    'GL_BLEND_COLOR_COMMAND_NV', 'GL_STENCIL_REF_COMMAND_NV',
    'GL_LINE_WIDTH_COMMAND_NV', 'GL_POLYGON_OFFSET_COMMAND_NV',
    'GL_ALPHA_REF_COMMAND_NV', 'GL_VIEWPORT_COMMAND_NV',
    'GL_SCISSOR_COMMAND_NV', 'GL_FRONT_FACE_COMMAND_NV',
    'PFNGLCREATESTATESNVPROC', 'PFNGLDELETESTATESNVPROC',
    'PFNGLISSTATENVPROC', 'PFNGLSTATECAPTURENVPROC',
    'PFNGLGETCOMMANDHEADERNVPROC', 'PFNGLGETSTAGEINDEXNVPROC',
    'PFNGLDRAWCOMMANDSNVPROC', 'PFNGLDRAWCOMMANDSADDRESSNVPROC',
    'PFNGLDRAWCOMMANDSSTATESNVPROC', 'PFNGLDRAWCOMMANDSSTATESADDRESSNVPROC',
    'PFNGLCREATECOMMANDLISTSNVPROC', 'PFNGLDELETECOMMANDLISTSNVPROC',
    'PFNGLISCOMMANDLISTNVPROC', 'PFNGLLISTDRAWCOMMANDSSTATESCLIENTNVPROC',
    'PFNGLCOMMANDLISTSEGMENTSNVPROC', 'PFNGLCOMPILECOMMANDLISTNVPROC',
    'PFNGLCALLCOMMANDLISTNVPROC', 'glCreateStatesNV', 'glDeleteStatesNV',
    'glIsStateNV', 'glStateCaptureNV', 'glGetCommandHeaderNV',
    'glGetStageIndexNV', 'glDrawCommandsNV', 'glDrawCommandsAddressNV',
    'glDrawCommandsStatesNV', 'glDrawCommandsStatesAddressNV',
    'glCreateCommandListsNV', 'glDeleteCommandListsNV', 'glIsCommandListNV',
    'glListDrawCommandsStatesClientNV', 'glCommandListSegmentsNV',
    'glCompileCommandListNV', 'glCallCommandListNV',
    'GL_NV_compute_shader_derivatives', 'GL_NV_conditional_render',
    'GL_QUERY_WAIT_NV', 'GL_QUERY_NO_WAIT_NV', 'GL_QUERY_BY_REGION_WAIT_NV',
    'GL_QUERY_BY_REGION_NO_WAIT_NV', 'PFNGLBEGINCONDITIONALRENDERNVPROC',
    'PFNGLENDCONDITIONALRENDERNVPROC', 'glBeginConditionalRenderNV',
    'glEndConditionalRenderNV', 'GL_NV_conservative_raster',
    'GL_CONSERVATIVE_RASTERIZATION_NV',
    'GL_SUBPIXEL_PRECISION_BIAS_X_BITS_NV',
    'GL_SUBPIXEL_PRECISION_BIAS_Y_BITS_NV',
    'GL_MAX_SUBPIXEL_PRECISION_BIAS_BITS_NV',
    'PFNGLSUBPIXELPRECISIONBIASNVPROC', 'glSubpixelPrecisionBiasNV',
    'GL_NV_conservative_raster_dilate', 'GL_CONSERVATIVE_RASTER_DILATE_NV',
    'GL_CONSERVATIVE_RASTER_DILATE_RANGE_NV',
    'GL_CONSERVATIVE_RASTER_DILATE_GRANULARITY_NV',
    'PFNGLCONSERVATIVERASTERPARAMETERFNVPROC',
    'glConservativeRasterParameterfNV', 'GL_NV_conservative_raster_pre_snap',
    'GL_CONSERVATIVE_RASTER_MODE_PRE_SNAP_NV',
    'GL_NV_conservative_raster_pre_snap_triangles',
    'GL_CONSERVATIVE_RASTER_MODE_NV',
    'GL_CONSERVATIVE_RASTER_MODE_POST_SNAP_NV',
    'GL_CONSERVATIVE_RASTER_MODE_PRE_SNAP_TRIANGLES_NV',
    'PFNGLCONSERVATIVERASTERPARAMETERINVPROC',
    'glConservativeRasterParameteriNV',
    'GL_NV_conservative_raster_underestimation', 'GL_NV_depth_buffer_float',
    'GL_DEPTH_COMPONENT32F_NV', 'GL_DEPTH32F_STENCIL8_NV',
    'GL_FLOAT_32_UNSIGNED_INT_24_8_REV_NV', 'GL_DEPTH_BUFFER_FLOAT_MODE_NV',
    'PFNGLDEPTHRANGEDNVPROC', 'PFNGLCLEARDEPTHDNVPROC',
    'PFNGLDEPTHBOUNDSDNVPROC', 'glDepthRangedNV', 'glClearDepthdNV',
    'glDepthBoundsdNV', 'GL_NV_draw_vulkan_image', 'GLVULKANPROCNV',
    'PFNGLDRAWVKIMAGENVPROC', 'PFNGLGETVKPROCADDRNVPROC',
    'PFNGLWAITVKSEMAPHORENVPROC', 'PFNGLSIGNALVKSEMAPHORENVPROC',
    'PFNGLSIGNALVKFENCENVPROC', 'glDrawVkImageNV', 'glGetVkProcAddrNV',
    'glWaitVkSemaphoreNV', 'glSignalVkSemaphoreNV', 'glSignalVkFenceNV',
    'GL_NV_fill_rectangle', 'GL_FILL_RECTANGLE_NV',
    'GL_NV_fragment_coverage_to_color', 'GL_FRAGMENT_COVERAGE_TO_COLOR_NV',
    'GL_FRAGMENT_COVERAGE_COLOR_NV', 'PFNGLFRAGMENTCOVERAGECOLORNVPROC',
    'glFragmentCoverageColorNV', 'GL_NV_fragment_shader_barycentric',
    'GL_NV_fragment_shader_interlock', 'GL_NV_framebuffer_mixed_samples',
    'GL_COVERAGE_MODULATION_TABLE_NV', 'GL_COLOR_SAMPLES_NV',
    'GL_DEPTH_SAMPLES_NV', 'GL_STENCIL_SAMPLES_NV',
    'GL_MIXED_DEPTH_SAMPLES_SUPPORTED_NV',
    'GL_MIXED_STENCIL_SAMPLES_SUPPORTED_NV', 'GL_COVERAGE_MODULATION_NV',
    'GL_COVERAGE_MODULATION_TABLE_SIZE_NV',
    'PFNGLCOVERAGEMODULATIONTABLENVPROC',
    'PFNGLGETCOVERAGEMODULATIONTABLENVPROC', 'PFNGLCOVERAGEMODULATIONNVPROC',
    'glCoverageModulationTableNV', 'glGetCoverageModulationTableNV',
    'glCoverageModulationNV', 'GL_NV_framebuffer_multisample_coverage',
    'GL_RENDERBUFFER_COVERAGE_SAMPLES_NV', 'GL_RENDERBUFFER_COLOR_SAMPLES_NV',
    'GL_MAX_MULTISAMPLE_COVERAGE_MODES_NV',
    'GL_MULTISAMPLE_COVERAGE_MODES_NV',
    'PFNGLRENDERBUFFERSTORAGEMULTISAMPLECOVERAGENVPROC',
    'glRenderbufferStorageMultisampleCoverageNV',
    'GL_NV_geometry_shader_passthrough', 'GL_NV_gpu_shader5', 'GL_INT64_NV',
    'GL_UNSIGNED_INT64_NV', 'GL_INT8_NV', 'GL_INT8_VEC2_NV',
    'GL_INT8_VEC3_NV', 'GL_INT8_VEC4_NV', 'GL_INT16_NV', 'GL_INT16_VEC2_NV',
    'GL_INT16_VEC3_NV', 'GL_INT16_VEC4_NV', 'GL_INT64_VEC2_NV',
    'GL_INT64_VEC3_NV', 'GL_INT64_VEC4_NV', 'GL_UNSIGNED_INT8_NV',
    'GL_UNSIGNED_INT8_VEC2_NV', 'GL_UNSIGNED_INT8_VEC3_NV',
    'GL_UNSIGNED_INT8_VEC4_NV', 'GL_UNSIGNED_INT16_NV',
    'GL_UNSIGNED_INT16_VEC2_NV', 'GL_UNSIGNED_INT16_VEC3_NV',
    'GL_UNSIGNED_INT16_VEC4_NV', 'GL_UNSIGNED_INT64_VEC2_NV',
    'GL_UNSIGNED_INT64_VEC3_NV', 'GL_UNSIGNED_INT64_VEC4_NV', 'GL_FLOAT16_NV',
    'GL_FLOAT16_VEC2_NV', 'GL_FLOAT16_VEC3_NV', 'GL_FLOAT16_VEC4_NV',
    'PFNGLUNIFORM1I64NVPROC', 'PFNGLUNIFORM2I64NVPROC',
    'PFNGLUNIFORM3I64NVPROC', 'PFNGLUNIFORM4I64NVPROC',
    'PFNGLUNIFORM1I64VNVPROC', 'PFNGLUNIFORM2I64VNVPROC',
    'PFNGLUNIFORM3I64VNVPROC', 'PFNGLUNIFORM4I64VNVPROC',
    'PFNGLUNIFORM1UI64NVPROC', 'PFNGLUNIFORM2UI64NVPROC',
    'PFNGLUNIFORM3UI64NVPROC', 'PFNGLUNIFORM4UI64NVPROC',
    'PFNGLUNIFORM1UI64VNVPROC', 'PFNGLUNIFORM2UI64VNVPROC',
    'PFNGLUNIFORM3UI64VNVPROC', 'PFNGLUNIFORM4UI64VNVPROC',
    'PFNGLGETUNIFORMI64VNVPROC', 'PFNGLPROGRAMUNIFORM1I64NVPROC',
    'PFNGLPROGRAMUNIFORM2I64NVPROC', 'PFNGLPROGRAMUNIFORM3I64NVPROC',
    'PFNGLPROGRAMUNIFORM4I64NVPROC', 'PFNGLPROGRAMUNIFORM1I64VNVPROC',
    'PFNGLPROGRAMUNIFORM2I64VNVPROC', 'PFNGLPROGRAMUNIFORM3I64VNVPROC',
    'PFNGLPROGRAMUNIFORM4I64VNVPROC', 'PFNGLPROGRAMUNIFORM1UI64NVPROC',
    'PFNGLPROGRAMUNIFORM2UI64NVPROC', 'PFNGLPROGRAMUNIFORM3UI64NVPROC',
    'PFNGLPROGRAMUNIFORM4UI64NVPROC', 'PFNGLPROGRAMUNIFORM1UI64VNVPROC',
    'PFNGLPROGRAMUNIFORM2UI64VNVPROC', 'PFNGLPROGRAMUNIFORM3UI64VNVPROC',
    'PFNGLPROGRAMUNIFORM4UI64VNVPROC', 'glUniform1i64NV', 'glUniform2i64NV',
    'glUniform3i64NV', 'glUniform4i64NV', 'glUniform1i64vNV',
    'glUniform2i64vNV', 'glUniform3i64vNV', 'glUniform4i64vNV',
    'glUniform1ui64NV', 'glUniform2ui64NV', 'glUniform3ui64NV',
    'glUniform4ui64NV', 'glUniform1ui64vNV', 'glUniform2ui64vNV',
    'glUniform3ui64vNV', 'glUniform4ui64vNV', 'glGetUniformi64vNV',
    'glProgramUniform1i64NV', 'glProgramUniform2i64NV',
    'glProgramUniform3i64NV', 'glProgramUniform4i64NV',
    'glProgramUniform1i64vNV', 'glProgramUniform2i64vNV',
    'glProgramUniform3i64vNV', 'glProgramUniform4i64vNV',
    'glProgramUniform1ui64NV', 'glProgramUniform2ui64NV',
    'glProgramUniform3ui64NV', 'glProgramUniform4ui64NV',
    'glProgramUniform1ui64vNV', 'glProgramUniform2ui64vNV',
    'glProgramUniform3ui64vNV', 'glProgramUniform4ui64vNV',
    'GL_NV_internalformat_sample_query', 'GL_MULTISAMPLES_NV',
    'GL_SUPERSAMPLE_SCALE_X_NV', 'GL_SUPERSAMPLE_SCALE_Y_NV',
    'GL_CONFORMANT_NV', 'PFNGLGETINTERNALFORMATSAMPLEIVNVPROC',
    'glGetInternalformatSampleivNV', 'GL_NV_memory_attachment',
    'GL_ATTACHED_MEMORY_OBJECT_NV', 'GL_ATTACHED_MEMORY_OFFSET_NV',
    'GL_MEMORY_ATTACHABLE_ALIGNMENT_NV', 'GL_MEMORY_ATTACHABLE_SIZE_NV',
    'GL_MEMORY_ATTACHABLE_NV', 'GL_DETACHED_MEMORY_INCARNATION_NV',
    'GL_DETACHED_TEXTURES_NV', 'GL_DETACHED_BUFFERS_NV',
    'GL_MAX_DETACHED_TEXTURES_NV', 'GL_MAX_DETACHED_BUFFERS_NV',
    'PFNGLGETMEMORYOBJECTDETACHEDRESOURCESUIVNVPROC',
    'PFNGLRESETMEMORYOBJECTPARAMETERNVPROC', 'PFNGLTEXATTACHMEMORYNVPROC',
    'PFNGLBUFFERATTACHMEMORYNVPROC', 'PFNGLTEXTUREATTACHMEMORYNVPROC',
    'PFNGLNAMEDBUFFERATTACHMEMORYNVPROC',
    'glGetMemoryObjectDetachedResourcesuivNV',
    'glResetMemoryObjectParameterNV', 'glTexAttachMemoryNV',
    'glBufferAttachMemoryNV', 'glTextureAttachMemoryNV',
    'glNamedBufferAttachMemoryNV', 'GL_NV_memory_object_sparse',
    'PFNGLBUFFERPAGECOMMITMENTMEMNVPROC', 'PFNGLTEXPAGECOMMITMENTMEMNVPROC',
    'PFNGLNAMEDBUFFERPAGECOMMITMENTMEMNVPROC',
    'PFNGLTEXTUREPAGECOMMITMENTMEMNVPROC', 'glBufferPageCommitmentMemNV',
    'glTexPageCommitmentMemNV', 'glNamedBufferPageCommitmentMemNV',
    'glTexturePageCommitmentMemNV', 'GL_NV_mesh_shader', 'GL_MESH_SHADER_NV',
    'GL_TASK_SHADER_NV', 'GL_MAX_MESH_UNIFORM_BLOCKS_NV',
    'GL_MAX_MESH_TEXTURE_IMAGE_UNITS_NV', 'GL_MAX_MESH_IMAGE_UNIFORMS_NV',
    'GL_MAX_MESH_UNIFORM_COMPONENTS_NV',
    'GL_MAX_MESH_ATOMIC_COUNTER_BUFFERS_NV', 'GL_MAX_MESH_ATOMIC_COUNTERS_NV',
    'GL_MAX_MESH_SHADER_STORAGE_BLOCKS_NV',
    'GL_MAX_COMBINED_MESH_UNIFORM_COMPONENTS_NV',
    'GL_MAX_TASK_UNIFORM_BLOCKS_NV', 'GL_MAX_TASK_TEXTURE_IMAGE_UNITS_NV',
    'GL_MAX_TASK_IMAGE_UNIFORMS_NV', 'GL_MAX_TASK_UNIFORM_COMPONENTS_NV',
    'GL_MAX_TASK_ATOMIC_COUNTER_BUFFERS_NV', 'GL_MAX_TASK_ATOMIC_COUNTERS_NV',
    'GL_MAX_TASK_SHADER_STORAGE_BLOCKS_NV',
    'GL_MAX_COMBINED_TASK_UNIFORM_COMPONENTS_NV',
    'GL_MAX_MESH_WORK_GROUP_INVOCATIONS_NV',
    'GL_MAX_TASK_WORK_GROUP_INVOCATIONS_NV',
    'GL_MAX_MESH_TOTAL_MEMORY_SIZE_NV', 'GL_MAX_TASK_TOTAL_MEMORY_SIZE_NV',
    'GL_MAX_MESH_OUTPUT_VERTICES_NV', 'GL_MAX_MESH_OUTPUT_PRIMITIVES_NV',
    'GL_MAX_TASK_OUTPUT_COUNT_NV', 'GL_MAX_DRAW_MESH_TASKS_COUNT_NV',
    'GL_MAX_MESH_VIEWS_NV', 'GL_MESH_OUTPUT_PER_VERTEX_GRANULARITY_NV',
    'GL_MESH_OUTPUT_PER_PRIMITIVE_GRANULARITY_NV',
    'GL_MAX_MESH_WORK_GROUP_SIZE_NV', 'GL_MAX_TASK_WORK_GROUP_SIZE_NV',
    'GL_MESH_WORK_GROUP_SIZE_NV', 'GL_TASK_WORK_GROUP_SIZE_NV',
    'GL_MESH_VERTICES_OUT_NV', 'GL_MESH_PRIMITIVES_OUT_NV',
    'GL_MESH_OUTPUT_TYPE_NV', 'GL_UNIFORM_BLOCK_REFERENCED_BY_MESH_SHADER_NV',
    'GL_UNIFORM_BLOCK_REFERENCED_BY_TASK_SHADER_NV',
    'GL_REFERENCED_BY_MESH_SHADER_NV', 'GL_REFERENCED_BY_TASK_SHADER_NV',
    'GL_MESH_SHADER_BIT_NV', 'GL_TASK_SHADER_BIT_NV', 'GL_MESH_SUBROUTINE_NV',
    'GL_TASK_SUBROUTINE_NV', 'GL_MESH_SUBROUTINE_UNIFORM_NV',
    'GL_TASK_SUBROUTINE_UNIFORM_NV',
    'GL_ATOMIC_COUNTER_BUFFER_REFERENCED_BY_MESH_SHADER_NV',
    'GL_ATOMIC_COUNTER_BUFFER_REFERENCED_BY_TASK_SHADER_NV',
    'PFNGLDRAWMESHTASKSNVPROC', 'PFNGLDRAWMESHTASKSINDIRECTNVPROC',
    'PFNGLMULTIDRAWMESHTASKSINDIRECTNVPROC',
    'PFNGLMULTIDRAWMESHTASKSINDIRECTCOUNTNVPROC', 'glDrawMeshTasksNV',
    'glDrawMeshTasksIndirectNV', 'glMultiDrawMeshTasksIndirectNV',
    'glMultiDrawMeshTasksIndirectCountNV', 'GL_NV_path_rendering',
    'GL_PATH_FORMAT_SVG_NV', 'GL_PATH_FORMAT_PS_NV',
    'GL_STANDARD_FONT_NAME_NV', 'GL_SYSTEM_FONT_NAME_NV', 'GL_FILE_NAME_NV',
    'GL_PATH_STROKE_WIDTH_NV', 'GL_PATH_END_CAPS_NV',
    'GL_PATH_INITIAL_END_CAP_NV', 'GL_PATH_TERMINAL_END_CAP_NV',
    'GL_PATH_JOIN_STYLE_NV', 'GL_PATH_MITER_LIMIT_NV', 'GL_PATH_DASH_CAPS_NV',
    'GL_PATH_INITIAL_DASH_CAP_NV', 'GL_PATH_TERMINAL_DASH_CAP_NV',
    'GL_PATH_DASH_OFFSET_NV', 'GL_PATH_CLIENT_LENGTH_NV',
    'GL_PATH_FILL_MODE_NV', 'GL_PATH_FILL_MASK_NV',
    'GL_PATH_FILL_COVER_MODE_NV', 'GL_PATH_STROKE_COVER_MODE_NV',
    'GL_PATH_STROKE_MASK_NV', 'GL_COUNT_UP_NV', 'GL_COUNT_DOWN_NV',
    'GL_PATH_OBJECT_BOUNDING_BOX_NV', 'GL_CONVEX_HULL_NV',
    'GL_BOUNDING_BOX_NV', 'GL_TRANSLATE_X_NV', 'GL_TRANSLATE_Y_NV',
    'GL_TRANSLATE_2D_NV', 'GL_TRANSLATE_3D_NV', 'GL_AFFINE_2D_NV',
    'GL_AFFINE_3D_NV', 'GL_TRANSPOSE_AFFINE_2D_NV',
    'GL_TRANSPOSE_AFFINE_3D_NV', 'GL_UTF8_NV', 'GL_UTF16_NV',
    'GL_BOUNDING_BOX_OF_BOUNDING_BOXES_NV', 'GL_PATH_COMMAND_COUNT_NV',
    'GL_PATH_COORD_COUNT_NV', 'GL_PATH_DASH_ARRAY_COUNT_NV',
    'GL_PATH_COMPUTED_LENGTH_NV', 'GL_PATH_FILL_BOUNDING_BOX_NV',
    'GL_PATH_STROKE_BOUNDING_BOX_NV', 'GL_SQUARE_NV', 'GL_ROUND_NV',
    'GL_TRIANGULAR_NV', 'GL_BEVEL_NV', 'GL_MITER_REVERT_NV',
    'GL_MITER_TRUNCATE_NV', 'GL_SKIP_MISSING_GLYPH_NV',
    'GL_USE_MISSING_GLYPH_NV', 'GL_PATH_ERROR_POSITION_NV',
    'GL_ACCUM_ADJACENT_PAIRS_NV', 'GL_ADJACENT_PAIRS_NV',
    'GL_FIRST_TO_REST_NV', 'GL_PATH_GEN_MODE_NV', 'GL_PATH_GEN_COEFF_NV',
    'GL_PATH_GEN_COMPONENTS_NV', 'GL_PATH_STENCIL_FUNC_NV',
    'GL_PATH_STENCIL_REF_NV', 'GL_PATH_STENCIL_VALUE_MASK_NV',
    'GL_PATH_STENCIL_DEPTH_OFFSET_FACTOR_NV',
    'GL_PATH_STENCIL_DEPTH_OFFSET_UNITS_NV', 'GL_PATH_COVER_DEPTH_FUNC_NV',
    'GL_PATH_DASH_OFFSET_RESET_NV', 'GL_MOVE_TO_RESETS_NV',
    'GL_MOVE_TO_CONTINUES_NV', 'GL_CLOSE_PATH_NV', 'GL_MOVE_TO_NV',
    'GL_RELATIVE_MOVE_TO_NV', 'GL_LINE_TO_NV', 'GL_RELATIVE_LINE_TO_NV',
    'GL_HORIZONTAL_LINE_TO_NV', 'GL_RELATIVE_HORIZONTAL_LINE_TO_NV',
    'GL_VERTICAL_LINE_TO_NV', 'GL_RELATIVE_VERTICAL_LINE_TO_NV',
    'GL_QUADRATIC_CURVE_TO_NV', 'GL_RELATIVE_QUADRATIC_CURVE_TO_NV',
    'GL_CUBIC_CURVE_TO_NV', 'GL_RELATIVE_CUBIC_CURVE_TO_NV',
    'GL_SMOOTH_QUADRATIC_CURVE_TO_NV',
    'GL_RELATIVE_SMOOTH_QUADRATIC_CURVE_TO_NV', 'GL_SMOOTH_CUBIC_CURVE_TO_NV',
    'GL_RELATIVE_SMOOTH_CUBIC_CURVE_TO_NV', 'GL_SMALL_CCW_ARC_TO_NV',
    'GL_RELATIVE_SMALL_CCW_ARC_TO_NV', 'GL_SMALL_CW_ARC_TO_NV',
    'GL_RELATIVE_SMALL_CW_ARC_TO_NV', 'GL_LARGE_CCW_ARC_TO_NV',
    'GL_RELATIVE_LARGE_CCW_ARC_TO_NV', 'GL_LARGE_CW_ARC_TO_NV',
    'GL_RELATIVE_LARGE_CW_ARC_TO_NV', 'GL_RESTART_PATH_NV',
    'GL_DUP_FIRST_CUBIC_CURVE_TO_NV', 'GL_DUP_LAST_CUBIC_CURVE_TO_NV',
    'GL_RECT_NV', 'GL_CIRCULAR_CCW_ARC_TO_NV', 'GL_CIRCULAR_CW_ARC_TO_NV',
    'GL_CIRCULAR_TANGENT_ARC_TO_NV', 'GL_ARC_TO_NV', 'GL_RELATIVE_ARC_TO_NV',
    'GL_BOLD_BIT_NV', 'GL_ITALIC_BIT_NV', 'GL_GLYPH_WIDTH_BIT_NV',
    'GL_GLYPH_HEIGHT_BIT_NV', 'GL_GLYPH_HORIZONTAL_BEARING_X_BIT_NV',
    'GL_GLYPH_HORIZONTAL_BEARING_Y_BIT_NV',
    'GL_GLYPH_HORIZONTAL_BEARING_ADVANCE_BIT_NV',
    'GL_GLYPH_VERTICAL_BEARING_X_BIT_NV',
    'GL_GLYPH_VERTICAL_BEARING_Y_BIT_NV',
    'GL_GLYPH_VERTICAL_BEARING_ADVANCE_BIT_NV', 'GL_GLYPH_HAS_KERNING_BIT_NV',
    'GL_FONT_X_MIN_BOUNDS_BIT_NV', 'GL_FONT_Y_MIN_BOUNDS_BIT_NV',
    'GL_FONT_X_MAX_BOUNDS_BIT_NV', 'GL_FONT_Y_MAX_BOUNDS_BIT_NV',
    'GL_FONT_UNITS_PER_EM_BIT_NV', 'GL_FONT_ASCENDER_BIT_NV',
    'GL_FONT_DESCENDER_BIT_NV', 'GL_FONT_HEIGHT_BIT_NV',
    'GL_FONT_MAX_ADVANCE_WIDTH_BIT_NV', 'GL_FONT_MAX_ADVANCE_HEIGHT_BIT_NV',
    'GL_FONT_UNDERLINE_POSITION_BIT_NV', 'GL_FONT_UNDERLINE_THICKNESS_BIT_NV',
    'GL_FONT_HAS_KERNING_BIT_NV', 'GL_ROUNDED_RECT_NV',
    'GL_RELATIVE_ROUNDED_RECT_NV', 'GL_ROUNDED_RECT2_NV',
    'GL_RELATIVE_ROUNDED_RECT2_NV', 'GL_ROUNDED_RECT4_NV',
    'GL_RELATIVE_ROUNDED_RECT4_NV', 'GL_ROUNDED_RECT8_NV',
    'GL_RELATIVE_ROUNDED_RECT8_NV', 'GL_RELATIVE_RECT_NV',
    'GL_FONT_GLYPHS_AVAILABLE_NV', 'GL_FONT_TARGET_UNAVAILABLE_NV',
    'GL_FONT_UNAVAILABLE_NV', 'GL_FONT_UNINTELLIGIBLE_NV',
    'GL_CONIC_CURVE_TO_NV', 'GL_RELATIVE_CONIC_CURVE_TO_NV',
    'GL_FONT_NUM_GLYPH_INDICES_BIT_NV', 'GL_STANDARD_FONT_FORMAT_NV',
    'GL_PATH_PROJECTION_NV', 'GL_PATH_MODELVIEW_NV',
    'GL_PATH_MODELVIEW_STACK_DEPTH_NV', 'GL_PATH_MODELVIEW_MATRIX_NV',
    'GL_PATH_MAX_MODELVIEW_STACK_DEPTH_NV',
    'GL_PATH_TRANSPOSE_MODELVIEW_MATRIX_NV',
    'GL_PATH_PROJECTION_STACK_DEPTH_NV', 'GL_PATH_PROJECTION_MATRIX_NV',
    'GL_PATH_MAX_PROJECTION_STACK_DEPTH_NV',
    'GL_PATH_TRANSPOSE_PROJECTION_MATRIX_NV', 'GL_FRAGMENT_INPUT_NV',
    'PFNGLGENPATHSNVPROC', 'PFNGLDELETEPATHSNVPROC', 'PFNGLISPATHNVPROC',
    'PFNGLPATHCOMMANDSNVPROC', 'PFNGLPATHCOORDSNVPROC',
    'PFNGLPATHSUBCOMMANDSNVPROC', 'PFNGLPATHSUBCOORDSNVPROC',
    'PFNGLPATHSTRINGNVPROC', 'PFNGLPATHGLYPHSNVPROC',
    'PFNGLPATHGLYPHRANGENVPROC', 'PFNGLWEIGHTPATHSNVPROC',
    'PFNGLCOPYPATHNVPROC', 'PFNGLINTERPOLATEPATHSNVPROC',
    'PFNGLTRANSFORMPATHNVPROC', 'PFNGLPATHPARAMETERIVNVPROC',
    'PFNGLPATHPARAMETERINVPROC', 'PFNGLPATHPARAMETERFVNVPROC',
    'PFNGLPATHPARAMETERFNVPROC', 'PFNGLPATHDASHARRAYNVPROC',
    'PFNGLPATHSTENCILFUNCNVPROC', 'PFNGLPATHSTENCILDEPTHOFFSETNVPROC',
    'PFNGLSTENCILFILLPATHNVPROC', 'PFNGLSTENCILSTROKEPATHNVPROC',
    'PFNGLSTENCILFILLPATHINSTANCEDNVPROC',
    'PFNGLSTENCILSTROKEPATHINSTANCEDNVPROC', 'PFNGLPATHCOVERDEPTHFUNCNVPROC',
    'PFNGLCOVERFILLPATHNVPROC', 'PFNGLCOVERSTROKEPATHNVPROC',
    'PFNGLCOVERFILLPATHINSTANCEDNVPROC',
    'PFNGLCOVERSTROKEPATHINSTANCEDNVPROC', 'PFNGLGETPATHPARAMETERIVNVPROC',
    'PFNGLGETPATHPARAMETERFVNVPROC', 'PFNGLGETPATHCOMMANDSNVPROC',
    'PFNGLGETPATHCOORDSNVPROC', 'PFNGLGETPATHDASHARRAYNVPROC',
    'PFNGLGETPATHMETRICSNVPROC', 'PFNGLGETPATHMETRICRANGENVPROC',
    'PFNGLGETPATHSPACINGNVPROC', 'PFNGLISPOINTINFILLPATHNVPROC',
    'PFNGLISPOINTINSTROKEPATHNVPROC', 'PFNGLGETPATHLENGTHNVPROC',
    'PFNGLPOINTALONGPATHNVPROC', 'PFNGLMATRIXLOAD3X2FNVPROC',
    'PFNGLMATRIXLOAD3X3FNVPROC', 'PFNGLMATRIXLOADTRANSPOSE3X3FNVPROC',
    'PFNGLMATRIXMULT3X2FNVPROC', 'PFNGLMATRIXMULT3X3FNVPROC',
    'PFNGLMATRIXMULTTRANSPOSE3X3FNVPROC',
    'PFNGLSTENCILTHENCOVERFILLPATHNVPROC',
    'PFNGLSTENCILTHENCOVERSTROKEPATHNVPROC',
    'PFNGLSTENCILTHENCOVERFILLPATHINSTANCEDNVPROC',
    'PFNGLSTENCILTHENCOVERSTROKEPATHINSTANCEDNVPROC',
    'PFNGLPATHGLYPHINDEXRANGENVPROC', 'PFNGLPATHGLYPHINDEXARRAYNVPROC',
    'PFNGLPATHMEMORYGLYPHINDEXARRAYNVPROC',
    'PFNGLPROGRAMPATHFRAGMENTINPUTGENNVPROC',
    'PFNGLGETPROGRAMRESOURCEFVNVPROC', 'glGenPathsNV', 'glDeletePathsNV',
    'glIsPathNV', 'glPathCommandsNV', 'glPathCoordsNV', 'glPathSubCommandsNV',
    'glPathSubCoordsNV', 'glPathStringNV', 'glPathGlyphsNV',
    'glPathGlyphRangeNV', 'glWeightPathsNV', 'glCopyPathNV',
    'glInterpolatePathsNV', 'glTransformPathNV', 'glPathParameterivNV',
    'glPathParameteriNV', 'glPathParameterfvNV', 'glPathParameterfNV',
    'glPathDashArrayNV', 'glPathStencilFuncNV', 'glPathStencilDepthOffsetNV',
    'glStencilFillPathNV', 'glStencilStrokePathNV',
    'glStencilFillPathInstancedNV', 'glStencilStrokePathInstancedNV',
    'glPathCoverDepthFuncNV', 'glCoverFillPathNV', 'glCoverStrokePathNV',
    'glCoverFillPathInstancedNV', 'glCoverStrokePathInstancedNV',
    'glGetPathParameterivNV', 'glGetPathParameterfvNV', 'glGetPathCommandsNV',
    'glGetPathCoordsNV', 'glGetPathDashArrayNV', 'glGetPathMetricsNV',
    'glGetPathMetricRangeNV', 'glGetPathSpacingNV', 'glIsPointInFillPathNV',
    'glIsPointInStrokePathNV', 'glGetPathLengthNV', 'glPointAlongPathNV',
    'glMatrixLoad3x2fNV', 'glMatrixLoad3x3fNV', 'glMatrixLoadTranspose3x3fNV',
    'glMatrixMult3x2fNV', 'glMatrixMult3x3fNV', 'glMatrixMultTranspose3x3fNV',
    'glStencilThenCoverFillPathNV', 'glStencilThenCoverStrokePathNV',
    'glStencilThenCoverFillPathInstancedNV',
    'glStencilThenCoverStrokePathInstancedNV', 'glPathGlyphIndexRangeNV',
    'glPathGlyphIndexArrayNV', 'glPathMemoryGlyphIndexArrayNV',
    'glProgramPathFragmentInputGenNV', 'glGetProgramResourcefvNV',
    'GL_NV_path_rendering_shared_edge', 'GL_SHARED_EDGE_NV',
    'GL_NV_primitive_shading_rate', 'GL_SHADING_RATE_IMAGE_PER_PRIMITIVE_NV',
    'GL_SHADING_RATE_IMAGE_PALETTE_COUNT_NV',
    'GL_NV_representative_fragment_test',
    'GL_REPRESENTATIVE_FRAGMENT_TEST_NV', 'GL_NV_sample_locations',
    'GL_SAMPLE_LOCATION_SUBPIXEL_BITS_NV',
    'GL_SAMPLE_LOCATION_PIXEL_GRID_WIDTH_NV',
    'GL_SAMPLE_LOCATION_PIXEL_GRID_HEIGHT_NV',
    'GL_PROGRAMMABLE_SAMPLE_LOCATION_TABLE_SIZE_NV', 'GL_SAMPLE_LOCATION_NV',
    'GL_PROGRAMMABLE_SAMPLE_LOCATION_NV',
    'GL_FRAMEBUFFER_PROGRAMMABLE_SAMPLE_LOCATIONS_NV',
    'GL_FRAMEBUFFER_SAMPLE_LOCATION_PIXEL_GRID_NV',
    'PFNGLFRAMEBUFFERSAMPLELOCATIONSFVNVPROC',
    'PFNGLNAMEDFRAMEBUFFERSAMPLELOCATIONSFVNVPROC',
    'PFNGLRESOLVEDEPTHVALUESNVPROC', 'glFramebufferSampleLocationsfvNV',
    'glNamedFramebufferSampleLocationsfvNV', 'glResolveDepthValuesNV',
    'GL_NV_sample_mask_override_coverage', 'GL_NV_scissor_exclusive',
    'GL_SCISSOR_TEST_EXCLUSIVE_NV', 'GL_SCISSOR_BOX_EXCLUSIVE_NV',
    'PFNGLSCISSOREXCLUSIVENVPROC', 'PFNGLSCISSOREXCLUSIVEARRAYVNVPROC',
    'glScissorExclusiveNV', 'glScissorExclusiveArrayvNV',
    'GL_NV_shader_atomic_counters', 'GL_NV_shader_atomic_float',
    'GL_NV_shader_atomic_float64', 'GL_NV_shader_atomic_fp16_vector',
    'GL_NV_shader_atomic_int64', 'GL_NV_shader_buffer_load',
    'GL_BUFFER_GPU_ADDRESS_NV', 'GL_GPU_ADDRESS_NV',
    'GL_MAX_SHADER_BUFFER_ADDRESS_NV', 'PFNGLMAKEBUFFERRESIDENTNVPROC',
    'PFNGLMAKEBUFFERNONRESIDENTNVPROC', 'PFNGLISBUFFERRESIDENTNVPROC',
    'PFNGLMAKENAMEDBUFFERRESIDENTNVPROC',
    'PFNGLMAKENAMEDBUFFERNONRESIDENTNVPROC',
    'PFNGLISNAMEDBUFFERRESIDENTNVPROC', 'PFNGLGETBUFFERPARAMETERUI64VNVPROC',
    'PFNGLGETNAMEDBUFFERPARAMETERUI64VNVPROC', 'PFNGLGETINTEGERUI64VNVPROC',
    'PFNGLUNIFORMUI64NVPROC', 'PFNGLUNIFORMUI64VNVPROC',
    'PFNGLGETUNIFORMUI64VNVPROC', 'PFNGLPROGRAMUNIFORMUI64NVPROC',
    'PFNGLPROGRAMUNIFORMUI64VNVPROC', 'glMakeBufferResidentNV',
    'glMakeBufferNonResidentNV', 'glIsBufferResidentNV',
    'glMakeNamedBufferResidentNV', 'glMakeNamedBufferNonResidentNV',
    'glIsNamedBufferResidentNV', 'glGetBufferParameterui64vNV',
    'glGetNamedBufferParameterui64vNV', 'glGetIntegerui64vNV',
    'glUniformui64NV', 'glUniformui64vNV', 'glGetUniformui64vNV',
    'glProgramUniformui64NV', 'glProgramUniformui64vNV',
    'GL_NV_shader_buffer_store', 'GL_SHADER_GLOBAL_ACCESS_BARRIER_BIT_NV',
    'GL_NV_shader_subgroup_partitioned',
    'GL_SUBGROUP_FEATURE_PARTITIONED_BIT_NV',
    'GL_NV_shader_texture_footprint', 'GL_NV_shader_thread_group',
    'GL_WARP_SIZE_NV', 'GL_WARPS_PER_SM_NV', 'GL_SM_COUNT_NV',
    'GL_NV_shader_thread_shuffle', 'GL_NV_shading_rate_image',
    'GL_SHADING_RATE_IMAGE_NV', 'GL_SHADING_RATE_NO_INVOCATIONS_NV',
    'GL_SHADING_RATE_1_INVOCATION_PER_PIXEL_NV',
    'GL_SHADING_RATE_1_INVOCATION_PER_1X2_PIXELS_NV',
    'GL_SHADING_RATE_1_INVOCATION_PER_2X1_PIXELS_NV',
    'GL_SHADING_RATE_1_INVOCATION_PER_2X2_PIXELS_NV',
    'GL_SHADING_RATE_1_INVOCATION_PER_2X4_PIXELS_NV',
    'GL_SHADING_RATE_1_INVOCATION_PER_4X2_PIXELS_NV',
    'GL_SHADING_RATE_1_INVOCATION_PER_4X4_PIXELS_NV',
    'GL_SHADING_RATE_2_INVOCATIONS_PER_PIXEL_NV',
    'GL_SHADING_RATE_4_INVOCATIONS_PER_PIXEL_NV',
    'GL_SHADING_RATE_8_INVOCATIONS_PER_PIXEL_NV',
    'GL_SHADING_RATE_16_INVOCATIONS_PER_PIXEL_NV',
    'GL_SHADING_RATE_IMAGE_BINDING_NV',
    'GL_SHADING_RATE_IMAGE_TEXEL_WIDTH_NV',
    'GL_SHADING_RATE_IMAGE_TEXEL_HEIGHT_NV',
    'GL_SHADING_RATE_IMAGE_PALETTE_SIZE_NV',
    'GL_MAX_COARSE_FRAGMENT_SAMPLES_NV',
    'GL_SHADING_RATE_SAMPLE_ORDER_DEFAULT_NV',
    'GL_SHADING_RATE_SAMPLE_ORDER_PIXEL_MAJOR_NV',
    'GL_SHADING_RATE_SAMPLE_ORDER_SAMPLE_MAJOR_NV',
    'PFNGLBINDSHADINGRATEIMAGENVPROC',
    'PFNGLGETSHADINGRATEIMAGEPALETTENVPROC',
    'PFNGLGETSHADINGRATESAMPLELOCATIONIVNVPROC',
    'PFNGLSHADINGRATEIMAGEBARRIERNVPROC',
    'PFNGLSHADINGRATEIMAGEPALETTENVPROC', 'PFNGLSHADINGRATESAMPLEORDERNVPROC',
    'PFNGLSHADINGRATESAMPLEORDERCUSTOMNVPROC', 'glBindShadingRateImageNV',
    'glGetShadingRateImagePaletteNV', 'glGetShadingRateSampleLocationivNV',
    'glShadingRateImageBarrierNV', 'glShadingRateImagePaletteNV',
    'glShadingRateSampleOrderNV', 'glShadingRateSampleOrderCustomNV',
    'GL_NV_stereo_view_rendering', 'GL_NV_texture_barrier',
    'PFNGLTEXTUREBARRIERNVPROC', 'glTextureBarrierNV',
    'GL_NV_texture_rectangle_compressed',
    'GL_NV_uniform_buffer_unified_memory', 'GL_UNIFORM_BUFFER_UNIFIED_NV',
    'GL_UNIFORM_BUFFER_ADDRESS_NV', 'GL_UNIFORM_BUFFER_LENGTH_NV',
    'GL_NV_vertex_attrib_integer_64bit', 'PFNGLVERTEXATTRIBL1I64NVPROC',
    'PFNGLVERTEXATTRIBL2I64NVPROC', 'PFNGLVERTEXATTRIBL3I64NVPROC',
    'PFNGLVERTEXATTRIBL4I64NVPROC', 'PFNGLVERTEXATTRIBL1I64VNVPROC',
    'PFNGLVERTEXATTRIBL2I64VNVPROC', 'PFNGLVERTEXATTRIBL3I64VNVPROC',
    'PFNGLVERTEXATTRIBL4I64VNVPROC', 'PFNGLVERTEXATTRIBL1UI64NVPROC',
    'PFNGLVERTEXATTRIBL2UI64NVPROC', 'PFNGLVERTEXATTRIBL3UI64NVPROC',
    'PFNGLVERTEXATTRIBL4UI64NVPROC', 'PFNGLVERTEXATTRIBL1UI64VNVPROC',
    'PFNGLVERTEXATTRIBL2UI64VNVPROC', 'PFNGLVERTEXATTRIBL3UI64VNVPROC',
    'PFNGLVERTEXATTRIBL4UI64VNVPROC', 'PFNGLGETVERTEXATTRIBLI64VNVPROC',
    'PFNGLGETVERTEXATTRIBLUI64VNVPROC', 'PFNGLVERTEXATTRIBLFORMATNVPROC',
    'glVertexAttribL1i64NV', 'glVertexAttribL2i64NV', 'glVertexAttribL3i64NV',
    'glVertexAttribL4i64NV', 'glVertexAttribL1i64vNV',
    'glVertexAttribL2i64vNV', 'glVertexAttribL3i64vNV',
    'glVertexAttribL4i64vNV', 'glVertexAttribL1ui64NV',
    'glVertexAttribL2ui64NV', 'glVertexAttribL3ui64NV',
    'glVertexAttribL4ui64NV', 'glVertexAttribL1ui64vNV',
    'glVertexAttribL2ui64vNV', 'glVertexAttribL3ui64vNV',
    'glVertexAttribL4ui64vNV', 'glGetVertexAttribLi64vNV',
    'glGetVertexAttribLui64vNV', 'glVertexAttribLFormatNV',
    'GL_NV_vertex_buffer_unified_memory', 'GL_VERTEX_ATTRIB_ARRAY_UNIFIED_NV',
    'GL_ELEMENT_ARRAY_UNIFIED_NV', 'GL_VERTEX_ATTRIB_ARRAY_ADDRESS_NV',
    'GL_VERTEX_ARRAY_ADDRESS_NV', 'GL_NORMAL_ARRAY_ADDRESS_NV',
    'GL_COLOR_ARRAY_ADDRESS_NV', 'GL_INDEX_ARRAY_ADDRESS_NV',
    'GL_TEXTURE_COORD_ARRAY_ADDRESS_NV', 'GL_EDGE_FLAG_ARRAY_ADDRESS_NV',
    'GL_SECONDARY_COLOR_ARRAY_ADDRESS_NV', 'GL_FOG_COORD_ARRAY_ADDRESS_NV',
    'GL_ELEMENT_ARRAY_ADDRESS_NV', 'GL_VERTEX_ATTRIB_ARRAY_LENGTH_NV',
    'GL_VERTEX_ARRAY_LENGTH_NV', 'GL_NORMAL_ARRAY_LENGTH_NV',
    'GL_COLOR_ARRAY_LENGTH_NV', 'GL_INDEX_ARRAY_LENGTH_NV',
    'GL_TEXTURE_COORD_ARRAY_LENGTH_NV', 'GL_EDGE_FLAG_ARRAY_LENGTH_NV',
    'GL_SECONDARY_COLOR_ARRAY_LENGTH_NV', 'GL_FOG_COORD_ARRAY_LENGTH_NV',
    'GL_ELEMENT_ARRAY_LENGTH_NV', 'GL_DRAW_INDIRECT_UNIFIED_NV',
    'GL_DRAW_INDIRECT_ADDRESS_NV', 'GL_DRAW_INDIRECT_LENGTH_NV',
    'PFNGLBUFFERADDRESSRANGENVPROC', 'PFNGLVERTEXFORMATNVPROC',
    'PFNGLNORMALFORMATNVPROC', 'PFNGLCOLORFORMATNVPROC',
    'PFNGLINDEXFORMATNVPROC', 'PFNGLTEXCOORDFORMATNVPROC',
    'PFNGLEDGEFLAGFORMATNVPROC', 'PFNGLSECONDARYCOLORFORMATNVPROC',
    'PFNGLFOGCOORDFORMATNVPROC', 'PFNGLVERTEXATTRIBFORMATNVPROC',
    'PFNGLVERTEXATTRIBIFORMATNVPROC', 'PFNGLGETINTEGERUI64I_VNVPROC',
    'glBufferAddressRangeNV', 'glVertexFormatNV', 'glNormalFormatNV',
    'glColorFormatNV', 'glIndexFormatNV', 'glTexCoordFormatNV',
    'glEdgeFlagFormatNV', 'glSecondaryColorFormatNV', 'glFogCoordFormatNV',
    'glVertexAttribFormatNV', 'glVertexAttribIFormatNV',
    'glGetIntegerui64i_vNV', 'GL_NV_viewport_array2',
    'GL_NV_viewport_swizzle', 'GL_VIEWPORT_SWIZZLE_POSITIVE_X_NV',
    'GL_VIEWPORT_SWIZZLE_NEGATIVE_X_NV', 'GL_VIEWPORT_SWIZZLE_POSITIVE_Y_NV',
    'GL_VIEWPORT_SWIZZLE_NEGATIVE_Y_NV', 'GL_VIEWPORT_SWIZZLE_POSITIVE_Z_NV',
    'GL_VIEWPORT_SWIZZLE_NEGATIVE_Z_NV', 'GL_VIEWPORT_SWIZZLE_POSITIVE_W_NV',
    'GL_VIEWPORT_SWIZZLE_NEGATIVE_W_NV', 'GL_VIEWPORT_SWIZZLE_X_NV',
    'GL_VIEWPORT_SWIZZLE_Y_NV', 'GL_VIEWPORT_SWIZZLE_Z_NV',
    'GL_VIEWPORT_SWIZZLE_W_NV', 'PFNGLVIEWPORTSWIZZLENVPROC',
    'glViewportSwizzleNV'
]
