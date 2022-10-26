from .._wrapper import *

GL_AMD_framebuffer_multisample_advanced = 1
GL_RENDERBUFFER_STORAGE_SAMPLES_AMD = 0x91B2
GL_MAX_COLOR_FRAMEBUFFER_SAMPLES_AMD = 0x91B3
GL_MAX_COLOR_FRAMEBUFFER_STORAGE_SAMPLES_AMD = 0x91B4
GL_MAX_DEPTH_STENCIL_FRAMEBUFFER_SAMPLES_AMD = 0x91B5
GL_NUM_SUPPORTED_MULTISAMPLE_MODES_AMD = 0x91B6
GL_SUPPORTED_MULTISAMPLE_MODES_AMD = 0x91B7
PFNGLRENDERBUFFERSTORAGEMULTISAMPLEADVANCEDAMDPROC = C(
    None, UInt, Int, Int, UInt, Int, Int
)
PFNGLNAMEDRENDERBUFFERSTORAGEMULTISAMPLEADVANCEDAMDPROC = C(
    None, UInt, Int, Int, UInt, Int, Int
)
glRenderbufferStorageMultisampleAdvancedAMD = GL(
    'glRenderbufferStorageMultisampleAdvancedAMD', None, UInt, Int, Int, UInt,
    Int, Int
)
glNamedRenderbufferStorageMultisampleAdvancedAMD = GL(
    'glNamedRenderbufferStorageMultisampleAdvancedAMD', None, UInt, Int, Int,
    UInt, Int, Int
)
GL_AMD_performance_monitor = 1
GL_COUNTER_TYPE_AMD = 0x8BC0
GL_COUNTER_RANGE_AMD = 0x8BC1
GL_UNSIGNED_INT64_AMD = 0x8BC2
GL_PERCENTAGE_AMD = 0x8BC3
GL_PERFMON_RESULT_AVAILABLE_AMD = 0x8BC4
GL_PERFMON_RESULT_SIZE_AMD = 0x8BC5
GL_PERFMON_RESULT_AMD = 0x8BC6
PFNGLGETPERFMONITORGROUPSAMDPROC = C(None, P(Int), Int, P(UInt))
PFNGLGETPERFMONITORCOUNTERSAMDPROC = C(
    None, UInt, P(Int), P(Int), Int, P(UInt)
)
PFNGLGETPERFMONITORGROUPSTRINGAMDPROC = C(None, UInt, Int, P(Int), CharP)
PFNGLGETPERFMONITORCOUNTERSTRINGAMDPROC = C(
    None, UInt, UInt, Int, P(Int), CharP
)
PFNGLGETPERFMONITORCOUNTERINFOAMDPROC = C(None, UInt, UInt, UInt, VoidP)
PFNGLGENPERFMONITORSAMDPROC = C(None, Int, P(UInt))
PFNGLDELETEPERFMONITORSAMDPROC = C(None, Int, P(UInt))
PFNGLSELECTPERFMONITORCOUNTERSAMDPROC = C(
    None, UInt, UByte, UInt, Int, P(UInt)
)
PFNGLBEGINPERFMONITORAMDPROC = C(None, UInt)
PFNGLENDPERFMONITORAMDPROC = C(None, UInt)
PFNGLGETPERFMONITORCOUNTERDATAAMDPROC = C(
    None, UInt, UInt, Int, P(UInt), P(Int)
)
glGetPerfMonitorGroupsAMD = GL(
    'glGetPerfMonitorGroupsAMD', None, P(Int), Int, P(UInt)
)
glGetPerfMonitorCountersAMD = GL(
    'glGetPerfMonitorCountersAMD', None, UInt, P(Int), P(Int), Int, P(UInt)
)
glGetPerfMonitorGroupStringAMD = GL(
    'glGetPerfMonitorGroupStringAMD', None, UInt, Int, P(Int), CharP
)
glGetPerfMonitorCounterStringAMD = GL(
    'glGetPerfMonitorCounterStringAMD', None, UInt, UInt, Int, P(Int), CharP
)
glGetPerfMonitorCounterInfoAMD = GL(
    'glGetPerfMonitorCounterInfoAMD', None, UInt, UInt, UInt, VoidP
)
glGenPerfMonitorsAMD = GL('glGenPerfMonitorsAMD', None, Int, P(UInt))
glDeletePerfMonitorsAMD = GL('glDeletePerfMonitorsAMD', None, Int, P(UInt))
glSelectPerfMonitorCountersAMD = GL(
    'glSelectPerfMonitorCountersAMD', None, UInt, UByte, UInt, Int, P(UInt)
)
glBeginPerfMonitorAMD = GL('glBeginPerfMonitorAMD', None, UInt)
glEndPerfMonitorAMD = GL('glEndPerfMonitorAMD', None, UInt)
glGetPerfMonitorCounterDataAMD = GL(
    'glGetPerfMonitorCounterDataAMD', None, UInt, UInt, Int, P(UInt), P(Int)
)

__all__ = [
    'GL_AMD_framebuffer_multisample_advanced',
    'GL_RENDERBUFFER_STORAGE_SAMPLES_AMD',
    'GL_MAX_COLOR_FRAMEBUFFER_SAMPLES_AMD',
    'GL_MAX_COLOR_FRAMEBUFFER_STORAGE_SAMPLES_AMD',
    'GL_MAX_DEPTH_STENCIL_FRAMEBUFFER_SAMPLES_AMD',
    'GL_NUM_SUPPORTED_MULTISAMPLE_MODES_AMD',
    'GL_SUPPORTED_MULTISAMPLE_MODES_AMD',
    'PFNGLRENDERBUFFERSTORAGEMULTISAMPLEADVANCEDAMDPROC',
    'PFNGLNAMEDRENDERBUFFERSTORAGEMULTISAMPLEADVANCEDAMDPROC',
    'glRenderbufferStorageMultisampleAdvancedAMD',
    'glNamedRenderbufferStorageMultisampleAdvancedAMD',
    'GL_AMD_performance_monitor', 'GL_COUNTER_TYPE_AMD',
    'GL_COUNTER_RANGE_AMD', 'GL_UNSIGNED_INT64_AMD', 'GL_PERCENTAGE_AMD',
    'GL_PERFMON_RESULT_AVAILABLE_AMD', 'GL_PERFMON_RESULT_SIZE_AMD',
    'GL_PERFMON_RESULT_AMD', 'PFNGLGETPERFMONITORGROUPSAMDPROC',
    'PFNGLGETPERFMONITORCOUNTERSAMDPROC',
    'PFNGLGETPERFMONITORGROUPSTRINGAMDPROC',
    'PFNGLGETPERFMONITORCOUNTERSTRINGAMDPROC',
    'PFNGLGETPERFMONITORCOUNTERINFOAMDPROC', 'PFNGLGENPERFMONITORSAMDPROC',
    'PFNGLDELETEPERFMONITORSAMDPROC', 'PFNGLSELECTPERFMONITORCOUNTERSAMDPROC',
    'PFNGLBEGINPERFMONITORAMDPROC', 'PFNGLENDPERFMONITORAMDPROC',
    'PFNGLGETPERFMONITORCOUNTERDATAAMDPROC', 'glGetPerfMonitorGroupsAMD',
    'glGetPerfMonitorCountersAMD', 'glGetPerfMonitorGroupStringAMD',
    'glGetPerfMonitorCounterStringAMD', 'glGetPerfMonitorCounterInfoAMD',
    'glGenPerfMonitorsAMD', 'glDeletePerfMonitorsAMD',
    'glSelectPerfMonitorCountersAMD', 'glBeginPerfMonitorAMD',
    'glEndPerfMonitorAMD', 'glGetPerfMonitorCounterDataAMD'
]
