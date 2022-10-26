from .._wrapper import *

GL_ARB_ES2_compatibility = 1
GL_ARB_ES3_1_compatibility = 1
GL_ARB_ES3_2_compatibility = 1
GL_PRIMITIVE_BOUNDING_BOX_ARB = 0x92BE
GL_MULTISAMPLE_LINE_WIDTH_RANGE_ARB = 0x9381
GL_MULTISAMPLE_LINE_WIDTH_GRANULARITY_ARB = 0x9382
PFNGLPRIMITIVEBOUNDINGBOXARBPROC = C(
    None, Float, Float, Float, Float, Float, Float, Float, Float
)
glPrimitiveBoundingBoxARB = GL(
    'glPrimitiveBoundingBoxARB', None, Float, Float, Float, Float, Float,
    Float, Float, Float
)
GL_ARB_ES3_compatibility = 1
GL_ARB_arrays_of_arrays = 1
GL_ARB_base_instance = 1
GL_ARB_bindless_texture = 1
GL_UNSIGNED_INT64_ARB = 0x140F
PFNGLGETTEXTUREHANDLEARBPROC = C(ULong, UInt)
PFNGLGETTEXTURESAMPLERHANDLEARBPROC = C(ULong, UInt, UInt)
PFNGLMAKETEXTUREHANDLERESIDENTARBPROC = C(None, ULong)
PFNGLMAKETEXTUREHANDLENONRESIDENTARBPROC = C(None, ULong)
PFNGLGETIMAGEHANDLEARBPROC = C(ULong, UInt, Int, UByte, Int, UInt)
PFNGLMAKEIMAGEHANDLERESIDENTARBPROC = C(None, ULong, UInt)
PFNGLMAKEIMAGEHANDLENONRESIDENTARBPROC = C(None, ULong)
PFNGLUNIFORMHANDLEUI64ARBPROC = C(None, Int, ULong)
PFNGLUNIFORMHANDLEUI64VARBPROC = C(None, Int, Int, P(ULong))
PFNGLPROGRAMUNIFORMHANDLEUI64ARBPROC = C(None, UInt, Int, ULong)
PFNGLPROGRAMUNIFORMHANDLEUI64VARBPROC = C(None, UInt, Int, Int, P(ULong))
PFNGLISTEXTUREHANDLERESIDENTARBPROC = C(UByte, ULong)
PFNGLISIMAGEHANDLERESIDENTARBPROC = C(UByte, ULong)
PFNGLVERTEXATTRIBL1UI64ARBPROC = C(None, UInt, ULong)
PFNGLVERTEXATTRIBL1UI64VARBPROC = C(None, UInt, P(ULong))
PFNGLGETVERTEXATTRIBLUI64VARBPROC = C(None, UInt, UInt, P(ULong))
glGetTextureHandleARB = GL('glGetTextureHandleARB', ULong, UInt)
glGetTextureSamplerHandleARB = GL(
    'glGetTextureSamplerHandleARB', ULong, UInt, UInt
)
glMakeTextureHandleResidentARB = GL(
    'glMakeTextureHandleResidentARB', None, ULong
)
glMakeTextureHandleNonResidentARB = GL(
    'glMakeTextureHandleNonResidentARB', None, ULong
)
glGetImageHandleARB = GL(
    'glGetImageHandleARB', ULong, UInt, Int, UByte, Int, UInt
)
glMakeImageHandleResidentARB = GL(
    'glMakeImageHandleResidentARB', None, ULong, UInt
)
glMakeImageHandleNonResidentARB = GL(
    'glMakeImageHandleNonResidentARB', None, ULong
)
glUniformHandleui64ARB = GL('glUniformHandleui64ARB', None, Int, ULong)
glUniformHandleui64vARB = GL(
    'glUniformHandleui64vARB', None, Int, Int, P(ULong)
)
glProgramUniformHandleui64ARB = GL(
    'glProgramUniformHandleui64ARB', None, UInt, Int, ULong
)
glProgramUniformHandleui64vARB = GL(
    'glProgramUniformHandleui64vARB', None, UInt, Int, Int, P(ULong)
)
glIsTextureHandleResidentARB = GL(
    'glIsTextureHandleResidentARB', UByte, ULong
)
glIsImageHandleResidentARB = GL('glIsImageHandleResidentARB', UByte, ULong)
glVertexAttribL1ui64ARB = GL('glVertexAttribL1ui64ARB', None, UInt, ULong)
glVertexAttribL1ui64vARB = GL(
    'glVertexAttribL1ui64vARB', None, UInt, P(ULong)
)
glGetVertexAttribLui64vARB = GL(
    'glGetVertexAttribLui64vARB', None, UInt, UInt, P(ULong)
)
GL_ARB_blend_func_extended = 1
GL_ARB_buffer_storage = 1
GL_ARB_cl_event = 1
GL_SYNC_CL_EVENT_ARB = 0x8240
GL_SYNC_CL_EVENT_COMPLETE_ARB = 0x8241
PFNGLCREATESYNCFROMCLEVENTARBPROC = C(GLSyncP, VoidP, VoidP, UInt)
glCreateSyncFromCLeventARB = GL(
    'glCreateSyncFromCLeventARB', GLSyncP, VoidP, VoidP, UInt
)
GL_ARB_clear_buffer_object = 1
GL_ARB_clear_texture = 1
GL_ARB_clip_control = 1
GL_ARB_compressed_texture_pixel_storage = 1
GL_ARB_compute_shader = 1
GL_ARB_compute_variable_group_size = 1
GL_MAX_COMPUTE_VARIABLE_GROUP_INVOCATIONS_ARB = 0x9344
GL_MAX_COMPUTE_FIXED_GROUP_INVOCATIONS_ARB = 0x90EB
GL_MAX_COMPUTE_VARIABLE_GROUP_SIZE_ARB = 0x9345
GL_MAX_COMPUTE_FIXED_GROUP_SIZE_ARB = 0x91BF
PFNGLDISPATCHCOMPUTEGROUPSIZEARBPROC = C(
    None, UInt, UInt, UInt, UInt, UInt, UInt
)
glDispatchComputeGroupSizeARB = GL(
    'glDispatchComputeGroupSizeARB', None, UInt, UInt, UInt, UInt, UInt, UInt
)
GL_ARB_conditional_render_inverted = 1
GL_ARB_conservative_depth = 1
GL_ARB_copy_buffer = 1
GL_ARB_copy_image = 1
GL_ARB_cull_distance = 1
GL_ARB_debug_output = 1
GLDEBUGPROCARB = C(None, UInt, UInt, UInt, UInt, Int, CharP, VoidP)
GL_DEBUG_OUTPUT_SYNCHRONOUS_ARB = 0x8242
GL_DEBUG_NEXT_LOGGED_MESSAGE_LENGTH_ARB = 0x8243
GL_DEBUG_CALLBACK_FUNCTION_ARB = 0x8244
GL_DEBUG_CALLBACK_USER_PARAM_ARB = 0x8245
GL_DEBUG_SOURCE_API_ARB = 0x8246
GL_DEBUG_SOURCE_WINDOW_SYSTEM_ARB = 0x8247
GL_DEBUG_SOURCE_SHADER_COMPILER_ARB = 0x8248
GL_DEBUG_SOURCE_THIRD_PARTY_ARB = 0x8249
GL_DEBUG_SOURCE_APPLICATION_ARB = 0x824A
GL_DEBUG_SOURCE_OTHER_ARB = 0x824B
GL_DEBUG_TYPE_ERROR_ARB = 0x824C
GL_DEBUG_TYPE_DEPRECATED_BEHAVIOR_ARB = 0x824D
GL_DEBUG_TYPE_UNDEFINED_BEHAVIOR_ARB = 0x824E
GL_DEBUG_TYPE_PORTABILITY_ARB = 0x824F
GL_DEBUG_TYPE_PERFORMANCE_ARB = 0x8250
GL_DEBUG_TYPE_OTHER_ARB = 0x8251
GL_MAX_DEBUG_MESSAGE_LENGTH_ARB = 0x9143
GL_MAX_DEBUG_LOGGED_MESSAGES_ARB = 0x9144
GL_DEBUG_LOGGED_MESSAGES_ARB = 0x9145
GL_DEBUG_SEVERITY_HIGH_ARB = 0x9146
GL_DEBUG_SEVERITY_MEDIUM_ARB = 0x9147
GL_DEBUG_SEVERITY_LOW_ARB = 0x9148
PFNGLDEBUGMESSAGECONTROLARBPROC = C(
    None, UInt, UInt, UInt, Int, P(UInt), UByte
)
PFNGLDEBUGMESSAGEINSERTARBPROC = C(None, UInt, UInt, UInt, UInt, Int, CharP)
PFNGLDEBUGMESSAGECALLBACKARBPROC = C(None, GLDEBUGPROCARB, VoidP)
PFNGLGETDEBUGMESSAGELOGARBPROC = C(
    UInt, UInt, Int, P(UInt), P(UInt), P(UInt), P(UInt), P(Int), CharP
)
glDebugMessageControlARB = GL(
    'glDebugMessageControlARB', None, UInt, UInt, UInt, Int, P(UInt), UByte
)
glDebugMessageInsertARB = GL(
    'glDebugMessageInsertARB', None, UInt, UInt, UInt, UInt, Int, CharP
)
glDebugMessageCallbackARB = GL(
    'glDebugMessageCallbackARB', None, GLDEBUGPROCARB, VoidP
)
glGetDebugMessageLogARB = GL(
    'glGetDebugMessageLogARB', UInt, UInt, Int, P(UInt), P(UInt), P(UInt),
    P(UInt), P(Int), CharP
)
GL_ARB_depth_buffer_float = 1
GL_ARB_depth_clamp = 1
GL_ARB_derivative_control = 1
GL_ARB_direct_state_access = 1
GL_ARB_draw_buffers_blend = 1
PFNGLBLENDEQUATIONIARBPROC = C(None, UInt, UInt)
PFNGLBLENDEQUATIONSEPARATEIARBPROC = C(None, UInt, UInt, UInt)
PFNGLBLENDFUNCIARBPROC = C(None, UInt, UInt, UInt)
PFNGLBLENDFUNCSEPARATEIARBPROC = C(None, UInt, UInt, UInt, UInt, UInt)
glBlendEquationiARB = GL('glBlendEquationiARB', None, UInt, UInt)
glBlendEquationSeparateiARB = GL(
    'glBlendEquationSeparateiARB', None, UInt, UInt, UInt
)
glBlendFunciARB = GL('glBlendFunciARB', None, UInt, UInt, UInt)
glBlendFuncSeparateiARB = GL(
    'glBlendFuncSeparateiARB', None, UInt, UInt, UInt, UInt, UInt
)
GL_ARB_draw_elements_base_vertex = 1
GL_ARB_draw_indirect = 1
GL_ARB_draw_instanced = 1
PFNGLDRAWARRAYSINSTANCEDARBPROC = C(None, UInt, Int, Int, Int)
PFNGLDRAWELEMENTSINSTANCEDARBPROC = C(None, UInt, Int, UInt, VoidP, Int)
glDrawArraysInstancedARB = GL(
    'glDrawArraysInstancedARB', None, UInt, Int, Int, Int
)
glDrawElementsInstancedARB = GL(
    'glDrawElementsInstancedARB', None, UInt, Int, UInt, VoidP, Int
)
GL_ARB_enhanced_layouts = 1
GL_ARB_explicit_attrib_location = 1
GL_ARB_explicit_uniform_location = 1
GL_ARB_fragment_coord_conventions = 1
GL_ARB_fragment_layer_viewport = 1
GL_ARB_fragment_shader_interlock = 1
GL_ARB_framebuffer_no_attachments = 1
GL_ARB_framebuffer_object = 1
GL_ARB_framebuffer_sRGB = 1
GL_ARB_geometry_shader4 = 1
GL_LINES_ADJACENCY_ARB = 0x000A
GL_LINE_STRIP_ADJACENCY_ARB = 0x000B
GL_TRIANGLES_ADJACENCY_ARB = 0x000C
GL_TRIANGLE_STRIP_ADJACENCY_ARB = 0x000D
GL_PROGRAM_POINT_SIZE_ARB = 0x8642
GL_MAX_GEOMETRY_TEXTURE_IMAGE_UNITS_ARB = 0x8C29
GL_FRAMEBUFFER_ATTACHMENT_LAYERED_ARB = 0x8DA7
GL_FRAMEBUFFER_INCOMPLETE_LAYER_TARGETS_ARB = 0x8DA8
GL_FRAMEBUFFER_INCOMPLETE_LAYER_COUNT_ARB = 0x8DA9
GL_GEOMETRY_SHADER_ARB = 0x8DD9
GL_GEOMETRY_VERTICES_OUT_ARB = 0x8DDA
GL_GEOMETRY_INPUT_TYPE_ARB = 0x8DDB
GL_GEOMETRY_OUTPUT_TYPE_ARB = 0x8DDC
GL_MAX_GEOMETRY_VARYING_COMPONENTS_ARB = 0x8DDD
GL_MAX_VERTEX_VARYING_COMPONENTS_ARB = 0x8DDE
GL_MAX_GEOMETRY_UNIFORM_COMPONENTS_ARB = 0x8DDF
GL_MAX_GEOMETRY_OUTPUT_VERTICES_ARB = 0x8DE0
GL_MAX_GEOMETRY_TOTAL_OUTPUT_COMPONENTS_ARB = 0x8DE1
PFNGLPROGRAMPARAMETERIARBPROC = C(None, UInt, UInt, Int)
PFNGLFRAMEBUFFERTEXTUREARBPROC = C(None, UInt, UInt, UInt, Int)
PFNGLFRAMEBUFFERTEXTURELAYERARBPROC = C(None, UInt, UInt, UInt, Int, Int)
PFNGLFRAMEBUFFERTEXTUREFACEARBPROC = C(None, UInt, UInt, UInt, Int, UInt)
glProgramParameteriARB = GL('glProgramParameteriARB', None, UInt, UInt, Int)
glFramebufferTextureARB = GL(
    'glFramebufferTextureARB', None, UInt, UInt, UInt, Int
)
glFramebufferTextureLayerARB = GL(
    'glFramebufferTextureLayerARB', None, UInt, UInt, UInt, Int, Int
)
glFramebufferTextureFaceARB = GL(
    'glFramebufferTextureFaceARB', None, UInt, UInt, UInt, Int, UInt
)
GL_ARB_get_program_binary = 1
GL_ARB_get_texture_sub_image = 1
GL_ARB_gl_spirv = 1
GL_SHADER_BINARY_FORMAT_SPIR_V_ARB = 0x9551
GL_SPIR_V_BINARY_ARB = 0x9552
PFNGLSPECIALIZESHADERARBPROC = C(None, UInt, CharP, UInt, P(UInt), P(UInt))
glSpecializeShaderARB = GL(
    'glSpecializeShaderARB', None, UInt, CharP, UInt, P(UInt), P(UInt)
)
GL_ARB_gpu_shader5 = 1
GL_ARB_gpu_shader_fp64 = 1
GL_ARB_gpu_shader_int64 = 1
GL_INT64_ARB = 0x140E
GL_INT64_VEC2_ARB = 0x8FE9
GL_INT64_VEC3_ARB = 0x8FEA
GL_INT64_VEC4_ARB = 0x8FEB
GL_UNSIGNED_INT64_VEC2_ARB = 0x8FF5
GL_UNSIGNED_INT64_VEC3_ARB = 0x8FF6
GL_UNSIGNED_INT64_VEC4_ARB = 0x8FF7
PFNGLUNIFORM1I64ARBPROC = C(None, Int, Long)
PFNGLUNIFORM2I64ARBPROC = C(None, Int, Long, Long)
PFNGLUNIFORM3I64ARBPROC = C(None, Int, Long, Long, Long)
PFNGLUNIFORM4I64ARBPROC = C(None, Int, Long, Long, Long, Long)
PFNGLUNIFORM1I64VARBPROC = C(None, Int, Int, P(Long))
PFNGLUNIFORM2I64VARBPROC = C(None, Int, Int, P(Long))
PFNGLUNIFORM3I64VARBPROC = C(None, Int, Int, P(Long))
PFNGLUNIFORM4I64VARBPROC = C(None, Int, Int, P(Long))
PFNGLUNIFORM1UI64ARBPROC = C(None, Int, ULong)
PFNGLUNIFORM2UI64ARBPROC = C(None, Int, ULong, ULong)
PFNGLUNIFORM3UI64ARBPROC = C(None, Int, ULong, ULong, ULong)
PFNGLUNIFORM4UI64ARBPROC = C(None, Int, ULong, ULong, ULong, ULong)
PFNGLUNIFORM1UI64VARBPROC = C(None, Int, Int, P(ULong))
PFNGLUNIFORM2UI64VARBPROC = C(None, Int, Int, P(ULong))
PFNGLUNIFORM3UI64VARBPROC = C(None, Int, Int, P(ULong))
PFNGLUNIFORM4UI64VARBPROC = C(None, Int, Int, P(ULong))
PFNGLGETUNIFORMI64VARBPROC = C(None, UInt, Int, P(Long))
PFNGLGETUNIFORMUI64VARBPROC = C(None, UInt, Int, P(ULong))
PFNGLGETNUNIFORMI64VARBPROC = C(None, UInt, Int, Int, P(Long))
PFNGLGETNUNIFORMUI64VARBPROC = C(None, UInt, Int, Int, P(ULong))
PFNGLPROGRAMUNIFORM1I64ARBPROC = C(None, UInt, Int, Long)
PFNGLPROGRAMUNIFORM2I64ARBPROC = C(None, UInt, Int, Long, Long)
PFNGLPROGRAMUNIFORM3I64ARBPROC = C(None, UInt, Int, Long, Long, Long)
PFNGLPROGRAMUNIFORM4I64ARBPROC = C(None, UInt, Int, Long, Long, Long, Long)
PFNGLPROGRAMUNIFORM1I64VARBPROC = C(None, UInt, Int, Int, P(Long))
PFNGLPROGRAMUNIFORM2I64VARBPROC = C(None, UInt, Int, Int, P(Long))
PFNGLPROGRAMUNIFORM3I64VARBPROC = C(None, UInt, Int, Int, P(Long))
PFNGLPROGRAMUNIFORM4I64VARBPROC = C(None, UInt, Int, Int, P(Long))
PFNGLPROGRAMUNIFORM1UI64ARBPROC = C(None, UInt, Int, ULong)
PFNGLPROGRAMUNIFORM2UI64ARBPROC = C(None, UInt, Int, ULong, ULong)
PFNGLPROGRAMUNIFORM3UI64ARBPROC = C(None, UInt, Int, ULong, ULong, ULong)
PFNGLPROGRAMUNIFORM4UI64ARBPROC = C(
    None, UInt, Int, ULong, ULong, ULong, ULong
)
PFNGLPROGRAMUNIFORM1UI64VARBPROC = C(None, UInt, Int, Int, P(ULong))
PFNGLPROGRAMUNIFORM2UI64VARBPROC = C(None, UInt, Int, Int, P(ULong))
PFNGLPROGRAMUNIFORM3UI64VARBPROC = C(None, UInt, Int, Int, P(ULong))
PFNGLPROGRAMUNIFORM4UI64VARBPROC = C(None, UInt, Int, Int, P(ULong))
glUniform1i64ARB = GL('glUniform1i64ARB', None, Int, Long)
glUniform2i64ARB = GL('glUniform2i64ARB', None, Int, Long, Long)
glUniform3i64ARB = GL('glUniform3i64ARB', None, Int, Long, Long, Long)
glUniform4i64ARB = GL('glUniform4i64ARB', None, Int, Long, Long, Long, Long)
glUniform1i64vARB = GL('glUniform1i64vARB', None, Int, Int, P(Long))
glUniform2i64vARB = GL('glUniform2i64vARB', None, Int, Int, P(Long))
glUniform3i64vARB = GL('glUniform3i64vARB', None, Int, Int, P(Long))
glUniform4i64vARB = GL('glUniform4i64vARB', None, Int, Int, P(Long))
glUniform1ui64ARB = GL('glUniform1ui64ARB', None, Int, ULong)
glUniform2ui64ARB = GL('glUniform2ui64ARB', None, Int, ULong, ULong)
glUniform3ui64ARB = GL('glUniform3ui64ARB', None, Int, ULong, ULong, ULong)
glUniform4ui64ARB = GL(
    'glUniform4ui64ARB', None, Int, ULong, ULong, ULong, ULong
)
glUniform1ui64vARB = GL('glUniform1ui64vARB', None, Int, Int, P(ULong))
glUniform2ui64vARB = GL('glUniform2ui64vARB', None, Int, Int, P(ULong))
glUniform3ui64vARB = GL('glUniform3ui64vARB', None, Int, Int, P(ULong))
glUniform4ui64vARB = GL('glUniform4ui64vARB', None, Int, Int, P(ULong))
glGetUniformi64vARB = GL('glGetUniformi64vARB', None, UInt, Int, P(Long))
glGetUniformui64vARB = GL('glGetUniformui64vARB', None, UInt, Int, P(ULong))
glGetnUniformi64vARB = GL(
    'glGetnUniformi64vARB', None, UInt, Int, Int, P(Long)
)
glGetnUniformui64vARB = GL(
    'glGetnUniformui64vARB', None, UInt, Int, Int, P(ULong)
)
glProgramUniform1i64ARB = GL('glProgramUniform1i64ARB', None, UInt, Int, Long)
glProgramUniform2i64ARB = GL(
    'glProgramUniform2i64ARB', None, UInt, Int, Long, Long
)
glProgramUniform3i64ARB = GL(
    'glProgramUniform3i64ARB', None, UInt, Int, Long, Long, Long
)
glProgramUniform4i64ARB = GL(
    'glProgramUniform4i64ARB', None, UInt, Int, Long, Long, Long, Long
)
glProgramUniform1i64vARB = GL(
    'glProgramUniform1i64vARB', None, UInt, Int, Int, P(Long)
)
glProgramUniform2i64vARB = GL(
    'glProgramUniform2i64vARB', None, UInt, Int, Int, P(Long)
)
glProgramUniform3i64vARB = GL(
    'glProgramUniform3i64vARB', None, UInt, Int, Int, P(Long)
)
glProgramUniform4i64vARB = GL(
    'glProgramUniform4i64vARB', None, UInt, Int, Int, P(Long)
)
glProgramUniform1ui64ARB = GL(
    'glProgramUniform1ui64ARB', None, UInt, Int, ULong
)
glProgramUniform2ui64ARB = GL(
    'glProgramUniform2ui64ARB', None, UInt, Int, ULong, ULong
)
glProgramUniform3ui64ARB = GL(
    'glProgramUniform3ui64ARB', None, UInt, Int, ULong, ULong, ULong
)
glProgramUniform4ui64ARB = GL(
    'glProgramUniform4ui64ARB', None, UInt, Int, ULong, ULong, ULong, ULong
)
glProgramUniform1ui64vARB = GL(
    'glProgramUniform1ui64vARB', None, UInt, Int, Int, P(ULong)
)
glProgramUniform2ui64vARB = GL(
    'glProgramUniform2ui64vARB', None, UInt, Int, Int, P(ULong)
)
glProgramUniform3ui64vARB = GL(
    'glProgramUniform3ui64vARB', None, UInt, Int, Int, P(ULong)
)
glProgramUniform4ui64vARB = GL(
    'glProgramUniform4ui64vARB', None, UInt, Int, Int, P(ULong)
)
GL_ARB_half_float_vertex = 1
GL_ARB_imaging = 1
GL_ARB_indirect_parameters = 1
GL_PARAMETER_BUFFER_ARB = 0x80EE
GL_PARAMETER_BUFFER_BINDING_ARB = 0x80EF
PFNGLMULTIDRAWARRAYSINDIRECTCOUNTARBPROC = C(
    None, UInt, VoidP, Size, Int, Int
)
PFNGLMULTIDRAWELEMENTSINDIRECTCOUNTARBPROC = C(
    None, UInt, UInt, VoidP, Size, Int, Int
)
glMultiDrawArraysIndirectCountARB = GL(
    'glMultiDrawArraysIndirectCountARB', None, UInt, VoidP, Size, Int, Int
)
glMultiDrawElementsIndirectCountARB = GL(
    'glMultiDrawElementsIndirectCountARB', None, UInt, UInt, VoidP, Size, Int,
    Int
)
GL_ARB_instanced_arrays = 1
GL_VERTEX_ATTRIB_ARRAY_DIVISOR_ARB = 0x88FE
PFNGLVERTEXATTRIBDIVISORARBPROC = C(None, UInt, UInt)
glVertexAttribDivisorARB = GL('glVertexAttribDivisorARB', None, UInt, UInt)
GL_ARB_internalformat_query = 1
GL_ARB_internalformat_query2 = 1
GL_SRGB_DECODE_ARB = 0x8299
GL_VIEW_CLASS_EAC_R11 = 0x9383
GL_VIEW_CLASS_EAC_RG11 = 0x9384
GL_VIEW_CLASS_ETC2_RGB = 0x9385
GL_VIEW_CLASS_ETC2_RGBA = 0x9386
GL_VIEW_CLASS_ETC2_EAC_RGBA = 0x9387
GL_VIEW_CLASS_ASTC_4x4_RGBA = 0x9388
GL_VIEW_CLASS_ASTC_5x4_RGBA = 0x9389
GL_VIEW_CLASS_ASTC_5x5_RGBA = 0x938A
GL_VIEW_CLASS_ASTC_6x5_RGBA = 0x938B
GL_VIEW_CLASS_ASTC_6x6_RGBA = 0x938C
GL_VIEW_CLASS_ASTC_8x5_RGBA = 0x938D
GL_VIEW_CLASS_ASTC_8x6_RGBA = 0x938E
GL_VIEW_CLASS_ASTC_8x8_RGBA = 0x938F
GL_VIEW_CLASS_ASTC_10x5_RGBA = 0x9390
GL_VIEW_CLASS_ASTC_10x6_RGBA = 0x9391
GL_VIEW_CLASS_ASTC_10x8_RGBA = 0x9392
GL_VIEW_CLASS_ASTC_10x10_RGBA = 0x9393
GL_VIEW_CLASS_ASTC_12x10_RGBA = 0x9394
GL_VIEW_CLASS_ASTC_12x12_RGBA = 0x9395
GL_ARB_invalidate_subdata = 1
GL_ARB_map_buffer_alignment = 1
GL_ARB_map_buffer_range = 1
GL_ARB_multi_bind = 1
GL_ARB_multi_draw_indirect = 1
GL_ARB_occlusion_query2 = 1
GL_ARB_parallel_shader_compile = 1
GL_MAX_SHADER_COMPILER_THREADS_ARB = 0x91B0
GL_COMPLETION_STATUS_ARB = 0x91B1
PFNGLMAXSHADERCOMPILERTHREADSARBPROC = C(None, UInt)
glMaxShaderCompilerThreadsARB = GL(
    'glMaxShaderCompilerThreadsARB', None, UInt
)
GL_ARB_pipeline_statistics_query = 1
GL_VERTICES_SUBMITTED_ARB = 0x82EE
GL_PRIMITIVES_SUBMITTED_ARB = 0x82EF
GL_VERTEX_SHADER_INVOCATIONS_ARB = 0x82F0
GL_TESS_CONTROL_SHADER_PATCHES_ARB = 0x82F1
GL_TESS_EVALUATION_SHADER_INVOCATIONS_ARB = 0x82F2
GL_GEOMETRY_SHADER_PRIMITIVES_EMITTED_ARB = 0x82F3
GL_FRAGMENT_SHADER_INVOCATIONS_ARB = 0x82F4
GL_COMPUTE_SHADER_INVOCATIONS_ARB = 0x82F5
GL_CLIPPING_INPUT_PRIMITIVES_ARB = 0x82F6
GL_CLIPPING_OUTPUT_PRIMITIVES_ARB = 0x82F7
GL_ARB_pixel_buffer_object = 1
GL_PIXEL_PACK_BUFFER_ARB = 0x88EB
GL_PIXEL_UNPACK_BUFFER_ARB = 0x88EC
GL_PIXEL_PACK_BUFFER_BINDING_ARB = 0x88ED
GL_PIXEL_UNPACK_BUFFER_BINDING_ARB = 0x88EF
GL_ARB_polygon_offset_clamp = 1
GL_ARB_post_depth_coverage = 1
GL_ARB_program_interface_query = 1
GL_ARB_provoking_vertex = 1
GL_ARB_query_buffer_object = 1
GL_ARB_robust_buffer_access_behavior = 1
GL_ARB_robustness = 1
GL_CONTEXT_FLAG_ROBUST_ACCESS_BIT_ARB = 0x00000004
GL_LOSE_CONTEXT_ON_RESET_ARB = 0x8252
GL_GUILTY_CONTEXT_RESET_ARB = 0x8253
GL_INNOCENT_CONTEXT_RESET_ARB = 0x8254
GL_UNKNOWN_CONTEXT_RESET_ARB = 0x8255
GL_RESET_NOTIFICATION_STRATEGY_ARB = 0x8256
GL_NO_RESET_NOTIFICATION_ARB = 0x8261
PFNGLGETGRAPHICSRESETSTATUSARBPROC = C(UInt)
PFNGLGETNTEXIMAGEARBPROC = C(None, UInt, Int, UInt, UInt, Int, VoidP)
PFNGLREADNPIXELSARBPROC = C(None, Int, Int, Int, Int, UInt, UInt, Int, VoidP)
PFNGLGETNCOMPRESSEDTEXIMAGEARBPROC = C(None, UInt, Int, Int, VoidP)
PFNGLGETNUNIFORMFVARBPROC = C(None, UInt, Int, Int, P(Float))
PFNGLGETNUNIFORMIVARBPROC = C(None, UInt, Int, Int, P(Int))
PFNGLGETNUNIFORMUIVARBPROC = C(None, UInt, Int, Int, P(UInt))
PFNGLGETNUNIFORMDVARBPROC = C(None, UInt, Int, Int, P(Double))
glGetGraphicsResetStatusARB = GL('glGetGraphicsResetStatusARB', UInt)
glGetnTexImageARB = GL(
    'glGetnTexImageARB', None, UInt, Int, UInt, UInt, Int, VoidP
)
glReadnPixelsARB = GL(
    'glReadnPixelsARB', None, Int, Int, Int, Int, UInt, UInt, Int, VoidP
)
glGetnCompressedTexImageARB = GL(
    'glGetnCompressedTexImageARB', None, UInt, Int, Int, VoidP
)
glGetnUniformfvARB = GL('glGetnUniformfvARB', None, UInt, Int, Int, P(Float))
glGetnUniformivARB = GL('glGetnUniformivARB', None, UInt, Int, Int, P(Int))
glGetnUniformuivARB = GL('glGetnUniformuivARB', None, UInt, Int, Int, P(UInt))
glGetnUniformdvARB = GL('glGetnUniformdvARB', None, UInt, Int, Int, P(Double))
GL_ARB_robustness_isolation = 1
GL_ARB_sample_locations = 1
GL_SAMPLE_LOCATION_SUBPIXEL_BITS_ARB = 0x933D
GL_SAMPLE_LOCATION_PIXEL_GRID_WIDTH_ARB = 0x933E
GL_SAMPLE_LOCATION_PIXEL_GRID_HEIGHT_ARB = 0x933F
GL_PROGRAMMABLE_SAMPLE_LOCATION_TABLE_SIZE_ARB = 0x9340
GL_SAMPLE_LOCATION_ARB = 0x8E50
GL_PROGRAMMABLE_SAMPLE_LOCATION_ARB = 0x9341
GL_FRAMEBUFFER_PROGRAMMABLE_SAMPLE_LOCATIONS_ARB = 0x9342
GL_FRAMEBUFFER_SAMPLE_LOCATION_PIXEL_GRID_ARB = 0x9343
PFNGLFRAMEBUFFERSAMPLELOCATIONSFVARBPROC = C(None, UInt, UInt, Int, P(Float))
PFNGLNAMEDFRAMEBUFFERSAMPLELOCATIONSFVARBPROC = C(
    None, UInt, UInt, Int, P(Float)
)
PFNGLEVALUATEDEPTHVALUESARBPROC = C(None)
glFramebufferSampleLocationsfvARB = GL(
    'glFramebufferSampleLocationsfvARB', None, UInt, UInt, Int, P(Float)
)
glNamedFramebufferSampleLocationsfvARB = GL(
    'glNamedFramebufferSampleLocationsfvARB', None, UInt, UInt, Int, P(Float)
)
glEvaluateDepthValuesARB = GL('glEvaluateDepthValuesARB', None)
GL_ARB_sample_shading = 1
GL_SAMPLE_SHADING_ARB = 0x8C36
GL_MIN_SAMPLE_SHADING_VALUE_ARB = 0x8C37
PFNGLMINSAMPLESHADINGARBPROC = C(None, Float)
glMinSampleShadingARB = GL('glMinSampleShadingARB', None, Float)
GL_ARB_sampler_objects = 1
GL_ARB_seamless_cube_map = 1
GL_ARB_seamless_cubemap_per_texture = 1
GL_ARB_separate_shader_objects = 1
GL_ARB_shader_atomic_counter_ops = 1
GL_ARB_shader_atomic_counters = 1
GL_ARB_shader_ballot = 1
GL_ARB_shader_bit_encoding = 1
GL_ARB_shader_clock = 1
GL_ARB_shader_draw_parameters = 1
GL_ARB_shader_group_vote = 1
GL_ARB_shader_image_load_store = 1
GL_ARB_shader_image_size = 1
GL_ARB_shader_precision = 1
GL_ARB_shader_stencil_export = 1
GL_ARB_shader_storage_buffer_object = 1
GL_ARB_shader_subroutine = 1
GL_ARB_shader_texture_image_samples = 1
GL_ARB_shader_viewport_layer_array = 1
GL_ARB_shading_language_420pack = 1
GL_ARB_shading_language_include = 1
GL_SHADER_INCLUDE_ARB = 0x8DAE
GL_NAMED_STRING_LENGTH_ARB = 0x8DE9
GL_NAMED_STRING_TYPE_ARB = 0x8DEA
PFNGLNAMEDSTRINGARBPROC = C(None, UInt, Int, CharP, Int, CharP)
PFNGLDELETENAMEDSTRINGARBPROC = C(None, Int, CharP)
PFNGLCOMPILESHADERINCLUDEARBPROC = C(None, UInt, Int, P(CharP), P(Int))
PFNGLISNAMEDSTRINGARBPROC = C(UByte, Int, CharP)
PFNGLGETNAMEDSTRINGARBPROC = C(None, Int, CharP, Int, P(Int), CharP)
PFNGLGETNAMEDSTRINGIVARBPROC = C(None, Int, CharP, UInt, P(Int))
glNamedStringARB = GL('glNamedStringARB', None, UInt, Int, CharP, Int, CharP)
glDeleteNamedStringARB = GL('glDeleteNamedStringARB', None, Int, CharP)
glCompileShaderIncludeARB = GL(
    'glCompileShaderIncludeARB', None, UInt, Int, P(CharP), P(Int)
)
glIsNamedStringARB = GL('glIsNamedStringARB', UByte, Int, CharP)
glGetNamedStringARB = GL(
    'glGetNamedStringARB', None, Int, CharP, Int, P(Int), CharP
)
glGetNamedStringivARB = GL(
    'glGetNamedStringivARB', None, Int, CharP, UInt, P(Int)
)
GL_ARB_shading_language_packing = 1
GL_ARB_sparse_buffer = 1
GL_SPARSE_STORAGE_BIT_ARB = 0x0400
GL_SPARSE_BUFFER_PAGE_SIZE_ARB = 0x82F8
PFNGLBUFFERPAGECOMMITMENTARBPROC = C(None, UInt, Size, Size, UByte)
PFNGLNAMEDBUFFERPAGECOMMITMENTEXTPROC = C(None, UInt, Size, Size, UByte)
PFNGLNAMEDBUFFERPAGECOMMITMENTARBPROC = C(None, UInt, Size, Size, UByte)
glBufferPageCommitmentARB = GL(
    'glBufferPageCommitmentARB', None, UInt, Size, Size, UByte
)
glNamedBufferPageCommitmentEXT = GL(
    'glNamedBufferPageCommitmentEXT', None, UInt, Size, Size, UByte
)
glNamedBufferPageCommitmentARB = GL(
    'glNamedBufferPageCommitmentARB', None, UInt, Size, Size, UByte
)
GL_ARB_sparse_texture = 1
GL_TEXTURE_SPARSE_ARB = 0x91A6
GL_VIRTUAL_PAGE_SIZE_INDEX_ARB = 0x91A7
GL_NUM_SPARSE_LEVELS_ARB = 0x91AA
GL_NUM_VIRTUAL_PAGE_SIZES_ARB = 0x91A8
GL_VIRTUAL_PAGE_SIZE_X_ARB = 0x9195
GL_VIRTUAL_PAGE_SIZE_Y_ARB = 0x9196
GL_VIRTUAL_PAGE_SIZE_Z_ARB = 0x9197
GL_MAX_SPARSE_TEXTURE_SIZE_ARB = 0x9198
GL_MAX_SPARSE_3D_TEXTURE_SIZE_ARB = 0x9199
GL_MAX_SPARSE_ARRAY_TEXTURE_LAYERS_ARB = 0x919A
GL_SPARSE_TEXTURE_FULL_ARRAY_CUBE_MIPMAPS_ARB = 0x91A9
PFNGLTEXPAGECOMMITMENTARBPROC = C(
    None, UInt, Int, Int, Int, Int, Int, Int, Int, UByte
)
glTexPageCommitmentARB = GL(
    'glTexPageCommitmentARB', None, UInt, Int, Int, Int, Int, Int, Int, Int,
    UByte
)
GL_ARB_sparse_texture2 = 1
GL_ARB_sparse_texture_clamp = 1
GL_ARB_spirv_extensions = 1
GL_ARB_stencil_texturing = 1
GL_ARB_sync = 1
GL_ARB_tessellation_shader = 1
GL_ARB_texture_barrier = 1
GL_ARB_texture_border_clamp = 1
GL_CLAMP_TO_BORDER_ARB = 0x812D
GL_ARB_texture_buffer_object = 1
GL_TEXTURE_BUFFER_ARB = 0x8C2A
GL_MAX_TEXTURE_BUFFER_SIZE_ARB = 0x8C2B
GL_TEXTURE_BINDING_BUFFER_ARB = 0x8C2C
GL_TEXTURE_BUFFER_DATA_STORE_BINDING_ARB = 0x8C2D
GL_TEXTURE_BUFFER_FORMAT_ARB = 0x8C2E
PFNGLTEXBUFFERARBPROC = C(None, UInt, UInt, UInt)
glTexBufferARB = GL('glTexBufferARB', None, UInt, UInt, UInt)
GL_ARB_texture_buffer_object_rgb32 = 1
GL_ARB_texture_buffer_range = 1
GL_ARB_texture_compression_bptc = 1
GL_COMPRESSED_RGBA_BPTC_UNORM_ARB = 0x8E8C
GL_COMPRESSED_SRGB_ALPHA_BPTC_UNORM_ARB = 0x8E8D
GL_COMPRESSED_RGB_BPTC_SIGNED_FLOAT_ARB = 0x8E8E
GL_COMPRESSED_RGB_BPTC_UNSIGNED_FLOAT_ARB = 0x8E8F
GL_ARB_texture_compression_rgtc = 1
GL_ARB_texture_cube_map_array = 1
GL_TEXTURE_CUBE_MAP_ARRAY_ARB = 0x9009
GL_TEXTURE_BINDING_CUBE_MAP_ARRAY_ARB = 0x900A
GL_PROXY_TEXTURE_CUBE_MAP_ARRAY_ARB = 0x900B
GL_SAMPLER_CUBE_MAP_ARRAY_ARB = 0x900C
GL_SAMPLER_CUBE_MAP_ARRAY_SHADOW_ARB = 0x900D
GL_INT_SAMPLER_CUBE_MAP_ARRAY_ARB = 0x900E
GL_UNSIGNED_INT_SAMPLER_CUBE_MAP_ARRAY_ARB = 0x900F
GL_ARB_texture_filter_anisotropic = 1
GL_ARB_texture_filter_minmax = 1
GL_TEXTURE_REDUCTION_MODE_ARB = 0x9366
GL_WEIGHTED_AVERAGE_ARB = 0x9367
GL_ARB_texture_gather = 1
GL_MIN_PROGRAM_TEXTURE_GATHER_OFFSET_ARB = 0x8E5E
GL_MAX_PROGRAM_TEXTURE_GATHER_OFFSET_ARB = 0x8E5F
GL_MAX_PROGRAM_TEXTURE_GATHER_COMPONENTS_ARB = 0x8F9F
GL_ARB_texture_mirror_clamp_to_edge = 1
GL_ARB_texture_mirrored_repeat = 1
GL_MIRRORED_REPEAT_ARB = 0x8370
GL_ARB_texture_multisample = 1
GL_ARB_texture_non_power_of_two = 1
GL_ARB_texture_query_levels = 1
GL_ARB_texture_query_lod = 1
GL_ARB_texture_rg = 1
GL_ARB_texture_rgb10_a2ui = 1
GL_ARB_texture_stencil8 = 1
GL_ARB_texture_storage = 1
GL_ARB_texture_storage_multisample = 1
GL_ARB_texture_swizzle = 1
GL_ARB_texture_view = 1
GL_ARB_timer_query = 1
GL_ARB_transform_feedback2 = 1
GL_ARB_transform_feedback3 = 1
GL_ARB_transform_feedback_instanced = 1
GL_ARB_transform_feedback_overflow_query = 1
GL_TRANSFORM_FEEDBACK_OVERFLOW_ARB = 0x82EC
GL_TRANSFORM_FEEDBACK_STREAM_OVERFLOW_ARB = 0x82ED
GL_ARB_uniform_buffer_object = 1
GL_ARB_vertex_array_bgra = 1
GL_ARB_vertex_array_object = 1
GL_ARB_vertex_attrib_64bit = 1
GL_ARB_vertex_attrib_binding = 1
GL_ARB_vertex_type_10f_11f_11f_rev = 1
GL_ARB_vertex_type_2_10_10_10_rev = 1
GL_ARB_viewport_array = 1
PFNGLDEPTHRANGEARRAYDVNVPROC = C(None, UInt, Int, P(Double))
PFNGLDEPTHRANGEINDEXEDDNVPROC = C(None, UInt, Double, Double)
glDepthRangeArraydvNV = GL(
    'glDepthRangeArraydvNV', None, UInt, Int, P(Double)
)
glDepthRangeIndexeddNV = GL(
    'glDepthRangeIndexeddNV', None, UInt, Double, Double
)

__all__ = [
    'GL_ARB_ES2_compatibility', 'GL_ARB_ES3_1_compatibility',
    'GL_ARB_ES3_2_compatibility', 'GL_PRIMITIVE_BOUNDING_BOX_ARB',
    'GL_MULTISAMPLE_LINE_WIDTH_RANGE_ARB',
    'GL_MULTISAMPLE_LINE_WIDTH_GRANULARITY_ARB',
    'PFNGLPRIMITIVEBOUNDINGBOXARBPROC', 'glPrimitiveBoundingBoxARB',
    'GL_ARB_ES3_compatibility', 'GL_ARB_arrays_of_arrays',
    'GL_ARB_base_instance', 'GL_ARB_bindless_texture',
    'GL_UNSIGNED_INT64_ARB', 'PFNGLGETTEXTUREHANDLEARBPROC',
    'PFNGLGETTEXTURESAMPLERHANDLEARBPROC',
    'PFNGLMAKETEXTUREHANDLERESIDENTARBPROC',
    'PFNGLMAKETEXTUREHANDLENONRESIDENTARBPROC', 'PFNGLGETIMAGEHANDLEARBPROC',
    'PFNGLMAKEIMAGEHANDLERESIDENTARBPROC',
    'PFNGLMAKEIMAGEHANDLENONRESIDENTARBPROC', 'PFNGLUNIFORMHANDLEUI64ARBPROC',
    'PFNGLUNIFORMHANDLEUI64VARBPROC', 'PFNGLPROGRAMUNIFORMHANDLEUI64ARBPROC',
    'PFNGLPROGRAMUNIFORMHANDLEUI64VARBPROC',
    'PFNGLISTEXTUREHANDLERESIDENTARBPROC',
    'PFNGLISIMAGEHANDLERESIDENTARBPROC', 'PFNGLVERTEXATTRIBL1UI64ARBPROC',
    'PFNGLVERTEXATTRIBL1UI64VARBPROC', 'PFNGLGETVERTEXATTRIBLUI64VARBPROC',
    'glGetTextureHandleARB', 'glGetTextureSamplerHandleARB',
    'glMakeTextureHandleResidentARB', 'glMakeTextureHandleNonResidentARB',
    'glGetImageHandleARB', 'glMakeImageHandleResidentARB',
    'glMakeImageHandleNonResidentARB', 'glUniformHandleui64ARB',
    'glUniformHandleui64vARB', 'glProgramUniformHandleui64ARB',
    'glProgramUniformHandleui64vARB', 'glIsTextureHandleResidentARB',
    'glIsImageHandleResidentARB', 'glVertexAttribL1ui64ARB',
    'glVertexAttribL1ui64vARB', 'glGetVertexAttribLui64vARB',
    'GL_ARB_blend_func_extended', 'GL_ARB_buffer_storage', 'GL_ARB_cl_event',
    'GL_SYNC_CL_EVENT_ARB', 'GL_SYNC_CL_EVENT_COMPLETE_ARB',
    'PFNGLCREATESYNCFROMCLEVENTARBPROC', 'glCreateSyncFromCLeventARB',
    'GL_ARB_clear_buffer_object', 'GL_ARB_clear_texture',
    'GL_ARB_clip_control', 'GL_ARB_compressed_texture_pixel_storage',
    'GL_ARB_compute_shader', 'GL_ARB_compute_variable_group_size',
    'GL_MAX_COMPUTE_VARIABLE_GROUP_INVOCATIONS_ARB',
    'GL_MAX_COMPUTE_FIXED_GROUP_INVOCATIONS_ARB',
    'GL_MAX_COMPUTE_VARIABLE_GROUP_SIZE_ARB',
    'GL_MAX_COMPUTE_FIXED_GROUP_SIZE_ARB',
    'PFNGLDISPATCHCOMPUTEGROUPSIZEARBPROC', 'glDispatchComputeGroupSizeARB',
    'GL_ARB_conditional_render_inverted', 'GL_ARB_conservative_depth',
    'GL_ARB_copy_buffer', 'GL_ARB_copy_image', 'GL_ARB_cull_distance',
    'GL_ARB_debug_output', 'GLDEBUGPROCARB',
    'GL_DEBUG_OUTPUT_SYNCHRONOUS_ARB',
    'GL_DEBUG_NEXT_LOGGED_MESSAGE_LENGTH_ARB',
    'GL_DEBUG_CALLBACK_FUNCTION_ARB', 'GL_DEBUG_CALLBACK_USER_PARAM_ARB',
    'GL_DEBUG_SOURCE_API_ARB', 'GL_DEBUG_SOURCE_WINDOW_SYSTEM_ARB',
    'GL_DEBUG_SOURCE_SHADER_COMPILER_ARB', 'GL_DEBUG_SOURCE_THIRD_PARTY_ARB',
    'GL_DEBUG_SOURCE_APPLICATION_ARB', 'GL_DEBUG_SOURCE_OTHER_ARB',
    'GL_DEBUG_TYPE_ERROR_ARB', 'GL_DEBUG_TYPE_DEPRECATED_BEHAVIOR_ARB',
    'GL_DEBUG_TYPE_UNDEFINED_BEHAVIOR_ARB', 'GL_DEBUG_TYPE_PORTABILITY_ARB',
    'GL_DEBUG_TYPE_PERFORMANCE_ARB', 'GL_DEBUG_TYPE_OTHER_ARB',
    'GL_MAX_DEBUG_MESSAGE_LENGTH_ARB', 'GL_MAX_DEBUG_LOGGED_MESSAGES_ARB',
    'GL_DEBUG_LOGGED_MESSAGES_ARB', 'GL_DEBUG_SEVERITY_HIGH_ARB',
    'GL_DEBUG_SEVERITY_MEDIUM_ARB', 'GL_DEBUG_SEVERITY_LOW_ARB',
    'PFNGLDEBUGMESSAGECONTROLARBPROC', 'PFNGLDEBUGMESSAGEINSERTARBPROC',
    'PFNGLDEBUGMESSAGECALLBACKARBPROC', 'PFNGLGETDEBUGMESSAGELOGARBPROC',
    'glDebugMessageControlARB', 'glDebugMessageInsertARB',
    'glDebugMessageCallbackARB', 'glGetDebugMessageLogARB',
    'GL_ARB_depth_buffer_float', 'GL_ARB_depth_clamp',
    'GL_ARB_derivative_control', 'GL_ARB_direct_state_access',
    'GL_ARB_draw_buffers_blend', 'PFNGLBLENDEQUATIONIARBPROC',
    'PFNGLBLENDEQUATIONSEPARATEIARBPROC', 'PFNGLBLENDFUNCIARBPROC',
    'PFNGLBLENDFUNCSEPARATEIARBPROC', 'glBlendEquationiARB',
    'glBlendEquationSeparateiARB', 'glBlendFunciARB',
    'glBlendFuncSeparateiARB', 'GL_ARB_draw_elements_base_vertex',
    'GL_ARB_draw_indirect', 'GL_ARB_draw_instanced',
    'PFNGLDRAWARRAYSINSTANCEDARBPROC', 'PFNGLDRAWELEMENTSINSTANCEDARBPROC',
    'glDrawArraysInstancedARB', 'glDrawElementsInstancedARB',
    'GL_ARB_enhanced_layouts', 'GL_ARB_explicit_attrib_location',
    'GL_ARB_explicit_uniform_location', 'GL_ARB_fragment_coord_conventions',
    'GL_ARB_fragment_layer_viewport', 'GL_ARB_fragment_shader_interlock',
    'GL_ARB_framebuffer_no_attachments', 'GL_ARB_framebuffer_object',
    'GL_ARB_framebuffer_sRGB', 'GL_ARB_geometry_shader4',
    'GL_LINES_ADJACENCY_ARB', 'GL_LINE_STRIP_ADJACENCY_ARB',
    'GL_TRIANGLES_ADJACENCY_ARB', 'GL_TRIANGLE_STRIP_ADJACENCY_ARB',
    'GL_PROGRAM_POINT_SIZE_ARB', 'GL_MAX_GEOMETRY_TEXTURE_IMAGE_UNITS_ARB',
    'GL_FRAMEBUFFER_ATTACHMENT_LAYERED_ARB',
    'GL_FRAMEBUFFER_INCOMPLETE_LAYER_TARGETS_ARB',
    'GL_FRAMEBUFFER_INCOMPLETE_LAYER_COUNT_ARB', 'GL_GEOMETRY_SHADER_ARB',
    'GL_GEOMETRY_VERTICES_OUT_ARB', 'GL_GEOMETRY_INPUT_TYPE_ARB',
    'GL_GEOMETRY_OUTPUT_TYPE_ARB', 'GL_MAX_GEOMETRY_VARYING_COMPONENTS_ARB',
    'GL_MAX_VERTEX_VARYING_COMPONENTS_ARB',
    'GL_MAX_GEOMETRY_UNIFORM_COMPONENTS_ARB',
    'GL_MAX_GEOMETRY_OUTPUT_VERTICES_ARB',
    'GL_MAX_GEOMETRY_TOTAL_OUTPUT_COMPONENTS_ARB',
    'PFNGLPROGRAMPARAMETERIARBPROC', 'PFNGLFRAMEBUFFERTEXTUREARBPROC',
    'PFNGLFRAMEBUFFERTEXTURELAYERARBPROC',
    'PFNGLFRAMEBUFFERTEXTUREFACEARBPROC', 'glProgramParameteriARB',
    'glFramebufferTextureARB', 'glFramebufferTextureLayerARB',
    'glFramebufferTextureFaceARB', 'GL_ARB_get_program_binary',
    'GL_ARB_get_texture_sub_image', 'GL_ARB_gl_spirv',
    'GL_SHADER_BINARY_FORMAT_SPIR_V_ARB', 'GL_SPIR_V_BINARY_ARB',
    'PFNGLSPECIALIZESHADERARBPROC', 'glSpecializeShaderARB',
    'GL_ARB_gpu_shader5', 'GL_ARB_gpu_shader_fp64', 'GL_ARB_gpu_shader_int64',
    'GL_INT64_ARB', 'GL_INT64_VEC2_ARB', 'GL_INT64_VEC3_ARB',
    'GL_INT64_VEC4_ARB', 'GL_UNSIGNED_INT64_VEC2_ARB',
    'GL_UNSIGNED_INT64_VEC3_ARB', 'GL_UNSIGNED_INT64_VEC4_ARB',
    'PFNGLUNIFORM1I64ARBPROC', 'PFNGLUNIFORM2I64ARBPROC',
    'PFNGLUNIFORM3I64ARBPROC', 'PFNGLUNIFORM4I64ARBPROC',
    'PFNGLUNIFORM1I64VARBPROC', 'PFNGLUNIFORM2I64VARBPROC',
    'PFNGLUNIFORM3I64VARBPROC', 'PFNGLUNIFORM4I64VARBPROC',
    'PFNGLUNIFORM1UI64ARBPROC', 'PFNGLUNIFORM2UI64ARBPROC',
    'PFNGLUNIFORM3UI64ARBPROC', 'PFNGLUNIFORM4UI64ARBPROC',
    'PFNGLUNIFORM1UI64VARBPROC', 'PFNGLUNIFORM2UI64VARBPROC',
    'PFNGLUNIFORM3UI64VARBPROC', 'PFNGLUNIFORM4UI64VARBPROC',
    'PFNGLGETUNIFORMI64VARBPROC', 'PFNGLGETUNIFORMUI64VARBPROC',
    'PFNGLGETNUNIFORMI64VARBPROC', 'PFNGLGETNUNIFORMUI64VARBPROC',
    'PFNGLPROGRAMUNIFORM1I64ARBPROC', 'PFNGLPROGRAMUNIFORM2I64ARBPROC',
    'PFNGLPROGRAMUNIFORM3I64ARBPROC', 'PFNGLPROGRAMUNIFORM4I64ARBPROC',
    'PFNGLPROGRAMUNIFORM1I64VARBPROC', 'PFNGLPROGRAMUNIFORM2I64VARBPROC',
    'PFNGLPROGRAMUNIFORM3I64VARBPROC', 'PFNGLPROGRAMUNIFORM4I64VARBPROC',
    'PFNGLPROGRAMUNIFORM1UI64ARBPROC', 'PFNGLPROGRAMUNIFORM2UI64ARBPROC',
    'PFNGLPROGRAMUNIFORM3UI64ARBPROC', 'PFNGLPROGRAMUNIFORM4UI64ARBPROC',
    'PFNGLPROGRAMUNIFORM1UI64VARBPROC', 'PFNGLPROGRAMUNIFORM2UI64VARBPROC',
    'PFNGLPROGRAMUNIFORM3UI64VARBPROC', 'PFNGLPROGRAMUNIFORM4UI64VARBPROC',
    'glUniform1i64ARB', 'glUniform2i64ARB', 'glUniform3i64ARB',
    'glUniform4i64ARB', 'glUniform1i64vARB', 'glUniform2i64vARB',
    'glUniform3i64vARB', 'glUniform4i64vARB', 'glUniform1ui64ARB',
    'glUniform2ui64ARB', 'glUniform3ui64ARB', 'glUniform4ui64ARB',
    'glUniform1ui64vARB', 'glUniform2ui64vARB', 'glUniform3ui64vARB',
    'glUniform4ui64vARB', 'glGetUniformi64vARB', 'glGetUniformui64vARB',
    'glGetnUniformi64vARB', 'glGetnUniformui64vARB',
    'glProgramUniform1i64ARB', 'glProgramUniform2i64ARB',
    'glProgramUniform3i64ARB', 'glProgramUniform4i64ARB',
    'glProgramUniform1i64vARB', 'glProgramUniform2i64vARB',
    'glProgramUniform3i64vARB', 'glProgramUniform4i64vARB',
    'glProgramUniform1ui64ARB', 'glProgramUniform2ui64ARB',
    'glProgramUniform3ui64ARB', 'glProgramUniform4ui64ARB',
    'glProgramUniform1ui64vARB', 'glProgramUniform2ui64vARB',
    'glProgramUniform3ui64vARB', 'glProgramUniform4ui64vARB',
    'GL_ARB_half_float_vertex', 'GL_ARB_imaging',
    'GL_ARB_indirect_parameters', 'GL_PARAMETER_BUFFER_ARB',
    'GL_PARAMETER_BUFFER_BINDING_ARB',
    'PFNGLMULTIDRAWARRAYSINDIRECTCOUNTARBPROC',
    'PFNGLMULTIDRAWELEMENTSINDIRECTCOUNTARBPROC',
    'glMultiDrawArraysIndirectCountARB',
    'glMultiDrawElementsIndirectCountARB', 'GL_ARB_instanced_arrays',
    'GL_VERTEX_ATTRIB_ARRAY_DIVISOR_ARB', 'PFNGLVERTEXATTRIBDIVISORARBPROC',
    'glVertexAttribDivisorARB', 'GL_ARB_internalformat_query',
    'GL_ARB_internalformat_query2', 'GL_SRGB_DECODE_ARB',
    'GL_VIEW_CLASS_EAC_R11', 'GL_VIEW_CLASS_EAC_RG11',
    'GL_VIEW_CLASS_ETC2_RGB', 'GL_VIEW_CLASS_ETC2_RGBA',
    'GL_VIEW_CLASS_ETC2_EAC_RGBA', 'GL_VIEW_CLASS_ASTC_4x4_RGBA',
    'GL_VIEW_CLASS_ASTC_5x4_RGBA', 'GL_VIEW_CLASS_ASTC_5x5_RGBA',
    'GL_VIEW_CLASS_ASTC_6x5_RGBA', 'GL_VIEW_CLASS_ASTC_6x6_RGBA',
    'GL_VIEW_CLASS_ASTC_8x5_RGBA', 'GL_VIEW_CLASS_ASTC_8x6_RGBA',
    'GL_VIEW_CLASS_ASTC_8x8_RGBA', 'GL_VIEW_CLASS_ASTC_10x5_RGBA',
    'GL_VIEW_CLASS_ASTC_10x6_RGBA', 'GL_VIEW_CLASS_ASTC_10x8_RGBA',
    'GL_VIEW_CLASS_ASTC_10x10_RGBA', 'GL_VIEW_CLASS_ASTC_12x10_RGBA',
    'GL_VIEW_CLASS_ASTC_12x12_RGBA', 'GL_ARB_invalidate_subdata',
    'GL_ARB_map_buffer_alignment', 'GL_ARB_map_buffer_range',
    'GL_ARB_multi_bind', 'GL_ARB_multi_draw_indirect',
    'GL_ARB_occlusion_query2', 'GL_ARB_parallel_shader_compile',
    'GL_MAX_SHADER_COMPILER_THREADS_ARB', 'GL_COMPLETION_STATUS_ARB',
    'PFNGLMAXSHADERCOMPILERTHREADSARBPROC', 'glMaxShaderCompilerThreadsARB',
    'GL_ARB_pipeline_statistics_query', 'GL_VERTICES_SUBMITTED_ARB',
    'GL_PRIMITIVES_SUBMITTED_ARB', 'GL_VERTEX_SHADER_INVOCATIONS_ARB',
    'GL_TESS_CONTROL_SHADER_PATCHES_ARB',
    'GL_TESS_EVALUATION_SHADER_INVOCATIONS_ARB',
    'GL_GEOMETRY_SHADER_PRIMITIVES_EMITTED_ARB',
    'GL_FRAGMENT_SHADER_INVOCATIONS_ARB', 'GL_COMPUTE_SHADER_INVOCATIONS_ARB',
    'GL_CLIPPING_INPUT_PRIMITIVES_ARB', 'GL_CLIPPING_OUTPUT_PRIMITIVES_ARB',
    'GL_ARB_pixel_buffer_object', 'GL_PIXEL_PACK_BUFFER_ARB',
    'GL_PIXEL_UNPACK_BUFFER_ARB', 'GL_PIXEL_PACK_BUFFER_BINDING_ARB',
    'GL_PIXEL_UNPACK_BUFFER_BINDING_ARB', 'GL_ARB_polygon_offset_clamp',
    'GL_ARB_post_depth_coverage', 'GL_ARB_program_interface_query',
    'GL_ARB_provoking_vertex', 'GL_ARB_query_buffer_object',
    'GL_ARB_robust_buffer_access_behavior', 'GL_ARB_robustness',
    'GL_CONTEXT_FLAG_ROBUST_ACCESS_BIT_ARB', 'GL_LOSE_CONTEXT_ON_RESET_ARB',
    'GL_GUILTY_CONTEXT_RESET_ARB', 'GL_INNOCENT_CONTEXT_RESET_ARB',
    'GL_UNKNOWN_CONTEXT_RESET_ARB', 'GL_RESET_NOTIFICATION_STRATEGY_ARB',
    'GL_NO_RESET_NOTIFICATION_ARB', 'PFNGLGETGRAPHICSRESETSTATUSARBPROC',
    'PFNGLGETNTEXIMAGEARBPROC', 'PFNGLREADNPIXELSARBPROC',
    'PFNGLGETNCOMPRESSEDTEXIMAGEARBPROC', 'PFNGLGETNUNIFORMFVARBPROC',
    'PFNGLGETNUNIFORMIVARBPROC', 'PFNGLGETNUNIFORMUIVARBPROC',
    'PFNGLGETNUNIFORMDVARBPROC', 'glGetGraphicsResetStatusARB',
    'glGetnTexImageARB', 'glReadnPixelsARB', 'glGetnCompressedTexImageARB',
    'glGetnUniformfvARB', 'glGetnUniformivARB', 'glGetnUniformuivARB',
    'glGetnUniformdvARB', 'GL_ARB_robustness_isolation',
    'GL_ARB_sample_locations', 'GL_SAMPLE_LOCATION_SUBPIXEL_BITS_ARB',
    'GL_SAMPLE_LOCATION_PIXEL_GRID_WIDTH_ARB',
    'GL_SAMPLE_LOCATION_PIXEL_GRID_HEIGHT_ARB',
    'GL_PROGRAMMABLE_SAMPLE_LOCATION_TABLE_SIZE_ARB',
    'GL_SAMPLE_LOCATION_ARB', 'GL_PROGRAMMABLE_SAMPLE_LOCATION_ARB',
    'GL_FRAMEBUFFER_PROGRAMMABLE_SAMPLE_LOCATIONS_ARB',
    'GL_FRAMEBUFFER_SAMPLE_LOCATION_PIXEL_GRID_ARB',
    'PFNGLFRAMEBUFFERSAMPLELOCATIONSFVARBPROC',
    'PFNGLNAMEDFRAMEBUFFERSAMPLELOCATIONSFVARBPROC',
    'PFNGLEVALUATEDEPTHVALUESARBPROC', 'glFramebufferSampleLocationsfvARB',
    'glNamedFramebufferSampleLocationsfvARB', 'glEvaluateDepthValuesARB',
    'GL_ARB_sample_shading', 'GL_SAMPLE_SHADING_ARB',
    'GL_MIN_SAMPLE_SHADING_VALUE_ARB', 'PFNGLMINSAMPLESHADINGARBPROC',
    'glMinSampleShadingARB', 'GL_ARB_sampler_objects',
    'GL_ARB_seamless_cube_map', 'GL_ARB_seamless_cubemap_per_texture',
    'GL_ARB_separate_shader_objects', 'GL_ARB_shader_atomic_counter_ops',
    'GL_ARB_shader_atomic_counters', 'GL_ARB_shader_ballot',
    'GL_ARB_shader_bit_encoding', 'GL_ARB_shader_clock',
    'GL_ARB_shader_draw_parameters', 'GL_ARB_shader_group_vote',
    'GL_ARB_shader_image_load_store', 'GL_ARB_shader_image_size',
    'GL_ARB_shader_precision', 'GL_ARB_shader_stencil_export',
    'GL_ARB_shader_storage_buffer_object', 'GL_ARB_shader_subroutine',
    'GL_ARB_shader_texture_image_samples',
    'GL_ARB_shader_viewport_layer_array', 'GL_ARB_shading_language_420pack',
    'GL_ARB_shading_language_include', 'GL_SHADER_INCLUDE_ARB',
    'GL_NAMED_STRING_LENGTH_ARB', 'GL_NAMED_STRING_TYPE_ARB',
    'PFNGLNAMEDSTRINGARBPROC', 'PFNGLDELETENAMEDSTRINGARBPROC',
    'PFNGLCOMPILESHADERINCLUDEARBPROC', 'PFNGLISNAMEDSTRINGARBPROC',
    'PFNGLGETNAMEDSTRINGARBPROC', 'PFNGLGETNAMEDSTRINGIVARBPROC',
    'glNamedStringARB', 'glDeleteNamedStringARB', 'glCompileShaderIncludeARB',
    'glIsNamedStringARB', 'glGetNamedStringARB', 'glGetNamedStringivARB',
    'GL_ARB_shading_language_packing', 'GL_ARB_sparse_buffer',
    'GL_SPARSE_STORAGE_BIT_ARB', 'GL_SPARSE_BUFFER_PAGE_SIZE_ARB',
    'PFNGLBUFFERPAGECOMMITMENTARBPROC',
    'PFNGLNAMEDBUFFERPAGECOMMITMENTEXTPROC',
    'PFNGLNAMEDBUFFERPAGECOMMITMENTARBPROC', 'glBufferPageCommitmentARB',
    'glNamedBufferPageCommitmentEXT', 'glNamedBufferPageCommitmentARB',
    'GL_ARB_sparse_texture', 'GL_TEXTURE_SPARSE_ARB',
    'GL_VIRTUAL_PAGE_SIZE_INDEX_ARB', 'GL_NUM_SPARSE_LEVELS_ARB',
    'GL_NUM_VIRTUAL_PAGE_SIZES_ARB', 'GL_VIRTUAL_PAGE_SIZE_X_ARB',
    'GL_VIRTUAL_PAGE_SIZE_Y_ARB', 'GL_VIRTUAL_PAGE_SIZE_Z_ARB',
    'GL_MAX_SPARSE_TEXTURE_SIZE_ARB', 'GL_MAX_SPARSE_3D_TEXTURE_SIZE_ARB',
    'GL_MAX_SPARSE_ARRAY_TEXTURE_LAYERS_ARB',
    'GL_SPARSE_TEXTURE_FULL_ARRAY_CUBE_MIPMAPS_ARB',
    'PFNGLTEXPAGECOMMITMENTARBPROC', 'glTexPageCommitmentARB',
    'GL_ARB_sparse_texture2', 'GL_ARB_sparse_texture_clamp',
    'GL_ARB_spirv_extensions', 'GL_ARB_stencil_texturing', 'GL_ARB_sync',
    'GL_ARB_tessellation_shader', 'GL_ARB_texture_barrier',
    'GL_ARB_texture_border_clamp', 'GL_CLAMP_TO_BORDER_ARB',
    'GL_ARB_texture_buffer_object', 'GL_TEXTURE_BUFFER_ARB',
    'GL_MAX_TEXTURE_BUFFER_SIZE_ARB', 'GL_TEXTURE_BINDING_BUFFER_ARB',
    'GL_TEXTURE_BUFFER_DATA_STORE_BINDING_ARB',
    'GL_TEXTURE_BUFFER_FORMAT_ARB', 'PFNGLTEXBUFFERARBPROC', 'glTexBufferARB',
    'GL_ARB_texture_buffer_object_rgb32', 'GL_ARB_texture_buffer_range',
    'GL_ARB_texture_compression_bptc', 'GL_COMPRESSED_RGBA_BPTC_UNORM_ARB',
    'GL_COMPRESSED_SRGB_ALPHA_BPTC_UNORM_ARB',
    'GL_COMPRESSED_RGB_BPTC_SIGNED_FLOAT_ARB',
    'GL_COMPRESSED_RGB_BPTC_UNSIGNED_FLOAT_ARB',
    'GL_ARB_texture_compression_rgtc', 'GL_ARB_texture_cube_map_array',
    'GL_TEXTURE_CUBE_MAP_ARRAY_ARB', 'GL_TEXTURE_BINDING_CUBE_MAP_ARRAY_ARB',
    'GL_PROXY_TEXTURE_CUBE_MAP_ARRAY_ARB', 'GL_SAMPLER_CUBE_MAP_ARRAY_ARB',
    'GL_SAMPLER_CUBE_MAP_ARRAY_SHADOW_ARB',
    'GL_INT_SAMPLER_CUBE_MAP_ARRAY_ARB',
    'GL_UNSIGNED_INT_SAMPLER_CUBE_MAP_ARRAY_ARB',
    'GL_ARB_texture_filter_anisotropic', 'GL_ARB_texture_filter_minmax',
    'GL_TEXTURE_REDUCTION_MODE_ARB', 'GL_WEIGHTED_AVERAGE_ARB',
    'GL_ARB_texture_gather', 'GL_MIN_PROGRAM_TEXTURE_GATHER_OFFSET_ARB',
    'GL_MAX_PROGRAM_TEXTURE_GATHER_OFFSET_ARB',
    'GL_MAX_PROGRAM_TEXTURE_GATHER_COMPONENTS_ARB',
    'GL_ARB_texture_mirror_clamp_to_edge', 'GL_ARB_texture_mirrored_repeat',
    'GL_MIRRORED_REPEAT_ARB', 'GL_ARB_texture_multisample',
    'GL_ARB_texture_non_power_of_two', 'GL_ARB_texture_query_levels',
    'GL_ARB_texture_query_lod', 'GL_ARB_texture_rg',
    'GL_ARB_texture_rgb10_a2ui', 'GL_ARB_texture_stencil8',
    'GL_ARB_texture_storage', 'GL_ARB_texture_storage_multisample',
    'GL_ARB_texture_swizzle', 'GL_ARB_texture_view', 'GL_ARB_timer_query',
    'GL_ARB_transform_feedback2', 'GL_ARB_transform_feedback3',
    'GL_ARB_transform_feedback_instanced',
    'GL_ARB_transform_feedback_overflow_query',
    'GL_TRANSFORM_FEEDBACK_OVERFLOW_ARB',
    'GL_TRANSFORM_FEEDBACK_STREAM_OVERFLOW_ARB',
    'GL_ARB_uniform_buffer_object', 'GL_ARB_vertex_array_bgra',
    'GL_ARB_vertex_array_object', 'GL_ARB_vertex_attrib_64bit',
    'GL_ARB_vertex_attrib_binding', 'GL_ARB_vertex_type_10f_11f_11f_rev',
    'GL_ARB_vertex_type_2_10_10_10_rev', 'GL_ARB_viewport_array',
    'PFNGLDEPTHRANGEARRAYDVNVPROC', 'PFNGLDEPTHRANGEINDEXEDDNVPROC',
    'glDepthRangeArraydvNV', 'glDepthRangeIndexeddNV'
]
