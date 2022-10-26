import ctypes
import os
import platform

from ..system import dynamic

uname = platform.uname()

system = {'Darwin': '.dylib', 'Windows': '.dll'}

machine = {
    'x86': '.x86', 'x86_64': '.x86_64', 'ARM64': '.arm64', 'AMD64': '.amd64'
}

glfw = dynamic(
    ctypes.cdll.LoadLibrary(
        os.path.join(
            os.path.dirname(__file__),
            'glfw_3' + system[uname.system] + machine[uname.machine]
        )
    )
)

Byte = ctypes.c_byte
UByte = ctypes.c_ubyte
Short = ctypes.c_short
UShort = ctypes.c_ushort
Int = ctypes.c_int
UInt = ctypes.c_uint
Long = ctypes.c_int64
ULong = ctypes.c_uint64
Float = ctypes.c_float
Double = ctypes.c_double
Size = ctypes.c_size_t
VoidP = ctypes.c_void_p
CharP = ctypes.c_char_p
P = ctypes.POINTER
C = ctypes.CFUNCTYPE
Structure = ctypes.Structure

GLFW_TRUE = 1
GLFW_FALSE = 0
GLFW_RELEASE = 0
GLFW_PRESS = 1
GLFW_REPEAT = 2
GLFW_HAT_CENTERED = 0
GLFW_HAT_UP = 1
GLFW_HAT_RIGHT = 2
GLFW_HAT_DOWN = 4
GLFW_HAT_LEFT = 8
GLFW_HAT_RIGHT_UP = (GLFW_HAT_RIGHT | GLFW_HAT_UP)
GLFW_HAT_RIGHT_DOWN = (GLFW_HAT_RIGHT | GLFW_HAT_DOWN)
GLFW_HAT_LEFT_UP = (GLFW_HAT_LEFT | GLFW_HAT_UP)
GLFW_HAT_LEFT_DOWN = (GLFW_HAT_LEFT | GLFW_HAT_DOWN)
GLFW_KEY_UNKNOWN = -1
GLFW_KEY_SPACE = 32
GLFW_KEY_APOSTROPHE = 39
GLFW_KEY_COMMA = 44
GLFW_KEY_MINUS = 45
GLFW_KEY_PERIOD = 46
GLFW_KEY_SLASH = 47
GLFW_KEY_0 = 48
GLFW_KEY_1 = 49
GLFW_KEY_2 = 50
GLFW_KEY_3 = 51
GLFW_KEY_4 = 52
GLFW_KEY_5 = 53
GLFW_KEY_6 = 54
GLFW_KEY_7 = 55
GLFW_KEY_8 = 56
GLFW_KEY_9 = 57
GLFW_KEY_SEMICOLON = 59
GLFW_KEY_EQUAL = 61
GLFW_KEY_A = 65
GLFW_KEY_B = 66
GLFW_KEY_C = 67
GLFW_KEY_D = 68
GLFW_KEY_E = 69
GLFW_KEY_F = 70
GLFW_KEY_G = 71
GLFW_KEY_H = 72
GLFW_KEY_I = 73
GLFW_KEY_J = 74
GLFW_KEY_K = 75
GLFW_KEY_L = 76
GLFW_KEY_M = 77
GLFW_KEY_N = 78
GLFW_KEY_O = 79
GLFW_KEY_P = 80
GLFW_KEY_Q = 81
GLFW_KEY_R = 82
GLFW_KEY_S = 83
GLFW_KEY_T = 84
GLFW_KEY_U = 85
GLFW_KEY_V = 86
GLFW_KEY_W = 87
GLFW_KEY_X = 88
GLFW_KEY_Y = 89
GLFW_KEY_Z = 90
GLFW_KEY_LEFT_BRACKET = 91
GLFW_KEY_BACKSLASH = 92
GLFW_KEY_RIGHT_BRACKET = 93
GLFW_KEY_GRAVE_ACCENT = 96
GLFW_KEY_WORLD_1 = 161
GLFW_KEY_WORLD_2 = 162
GLFW_KEY_ESCAPE = 256
GLFW_KEY_ENTER = 257
GLFW_KEY_TAB = 258
GLFW_KEY_BACKSPACE = 259
GLFW_KEY_INSERT = 260
GLFW_KEY_DELETE = 261
GLFW_KEY_RIGHT = 262
GLFW_KEY_LEFT = 263
GLFW_KEY_DOWN = 264
GLFW_KEY_UP = 265
GLFW_KEY_PAGE_UP = 266
GLFW_KEY_PAGE_DOWN = 267
GLFW_KEY_HOME = 268
GLFW_KEY_END = 269
GLFW_KEY_CAPS_LOCK = 280
GLFW_KEY_SCROLL_LOCK = 281
GLFW_KEY_NUM_LOCK = 282
GLFW_KEY_PRINT_SCREEN = 283
GLFW_KEY_PAUSE = 284
GLFW_KEY_F1 = 290
GLFW_KEY_F2 = 291
GLFW_KEY_F3 = 292
GLFW_KEY_F4 = 293
GLFW_KEY_F5 = 294
GLFW_KEY_F6 = 295
GLFW_KEY_F7 = 296
GLFW_KEY_F8 = 297
GLFW_KEY_F9 = 298
GLFW_KEY_F10 = 299
GLFW_KEY_F11 = 300
GLFW_KEY_F12 = 301
GLFW_KEY_F13 = 302
GLFW_KEY_F14 = 303
GLFW_KEY_F15 = 304
GLFW_KEY_F16 = 305
GLFW_KEY_F17 = 306
GLFW_KEY_F18 = 307
GLFW_KEY_F19 = 308
GLFW_KEY_F20 = 309
GLFW_KEY_F21 = 310
GLFW_KEY_F22 = 311
GLFW_KEY_F23 = 312
GLFW_KEY_F24 = 313
GLFW_KEY_F25 = 314
GLFW_KEY_KP_0 = 320
GLFW_KEY_KP_1 = 321
GLFW_KEY_KP_2 = 322
GLFW_KEY_KP_3 = 323
GLFW_KEY_KP_4 = 324
GLFW_KEY_KP_5 = 325
GLFW_KEY_KP_6 = 326
GLFW_KEY_KP_7 = 327
GLFW_KEY_KP_8 = 328
GLFW_KEY_KP_9 = 329
GLFW_KEY_KP_DECIMAL = 330
GLFW_KEY_KP_DIVIDE = 331
GLFW_KEY_KP_MULTIPLY = 332
GLFW_KEY_KP_SUBTRACT = 333
GLFW_KEY_KP_ADD = 334
GLFW_KEY_KP_ENTER = 335
GLFW_KEY_KP_EQUAL = 336
GLFW_KEY_LEFT_SHIFT = 340
GLFW_KEY_LEFT_CONTROL = 341
GLFW_KEY_LEFT_ALT = 342
GLFW_KEY_LEFT_SUPER = 343
GLFW_KEY_RIGHT_SHIFT = 344
GLFW_KEY_RIGHT_CONTROL = 345
GLFW_KEY_RIGHT_ALT = 346
GLFW_KEY_RIGHT_SUPER = 347
GLFW_KEY_MENU = 348
GLFW_KEY_LAST = GLFW_KEY_MENU
GLFW_MOD_SHIFT = 0x0001
GLFW_MOD_CONTROL = 0x0002
GLFW_MOD_ALT = 0x0004
GLFW_MOD_SUPER = 0x0008
GLFW_MOD_CAPS_LOCK = 0x0010
GLFW_MOD_NUM_LOCK = 0x0020
GLFW_MOUSE_BUTTON_1 = 0
GLFW_MOUSE_BUTTON_2 = 1
GLFW_MOUSE_BUTTON_3 = 2
GLFW_MOUSE_BUTTON_4 = 3
GLFW_MOUSE_BUTTON_5 = 4
GLFW_MOUSE_BUTTON_6 = 5
GLFW_MOUSE_BUTTON_7 = 6
GLFW_MOUSE_BUTTON_8 = 7
GLFW_MOUSE_BUTTON_LAST = GLFW_MOUSE_BUTTON_8
GLFW_MOUSE_BUTTON_LEFT = GLFW_MOUSE_BUTTON_1
GLFW_MOUSE_BUTTON_RIGHT = GLFW_MOUSE_BUTTON_2
GLFW_MOUSE_BUTTON_MIDDLE = GLFW_MOUSE_BUTTON_3
GLFW_JOYSTICK_1 = 0
GLFW_JOYSTICK_2 = 1
GLFW_JOYSTICK_3 = 2
GLFW_JOYSTICK_4 = 3
GLFW_JOYSTICK_5 = 4
GLFW_JOYSTICK_6 = 5
GLFW_JOYSTICK_7 = 6
GLFW_JOYSTICK_8 = 7
GLFW_JOYSTICK_9 = 8
GLFW_JOYSTICK_10 = 9
GLFW_JOYSTICK_11 = 10
GLFW_JOYSTICK_12 = 11
GLFW_JOYSTICK_13 = 12
GLFW_JOYSTICK_14 = 13
GLFW_JOYSTICK_15 = 14
GLFW_JOYSTICK_16 = 15
GLFW_JOYSTICK_LAST = GLFW_JOYSTICK_16
GLFW_GAMEPAD_BUTTON_A = 0
GLFW_GAMEPAD_BUTTON_B = 1
GLFW_GAMEPAD_BUTTON_X = 2
GLFW_GAMEPAD_BUTTON_Y = 3
GLFW_GAMEPAD_BUTTON_LEFT_BUMPER = 4
GLFW_GAMEPAD_BUTTON_RIGHT_BUMPER = 5
GLFW_GAMEPAD_BUTTON_BACK = 6
GLFW_GAMEPAD_BUTTON_START = 7
GLFW_GAMEPAD_BUTTON_GUIDE = 8
GLFW_GAMEPAD_BUTTON_LEFT_THUMB = 9
GLFW_GAMEPAD_BUTTON_RIGHT_THUMB = 10
GLFW_GAMEPAD_BUTTON_ANDROID_PAD_UP = 11
GLFW_GAMEPAD_BUTTON_ANDROID_PAD_RIGHT = 12
GLFW_GAMEPAD_BUTTON_ANDROID_PAD_DOWN = 13
GLFW_GAMEPAD_BUTTON_ANDROID_PAD_LEFT = 14
GLFW_GAMEPAD_BUTTON_LAST = GLFW_GAMEPAD_BUTTON_ANDROID_PAD_LEFT
GLFW_GAMEPAD_BUTTON_CROSS = GLFW_GAMEPAD_BUTTON_A
GLFW_GAMEPAD_BUTTON_CIRCLE = GLFW_GAMEPAD_BUTTON_B
GLFW_GAMEPAD_BUTTON_SQUARE = GLFW_GAMEPAD_BUTTON_X
GLFW_GAMEPAD_BUTTON_TRIANGLE = GLFW_GAMEPAD_BUTTON_Y
GLFW_GAMEPAD_AXIS_LEFT_X = 0
GLFW_GAMEPAD_AXIS_LEFT_Y = 1
GLFW_GAMEPAD_AXIS_RIGHT_X = 2
GLFW_GAMEPAD_AXIS_RIGHT_Y = 3
GLFW_GAMEPAD_AXIS_LEFT_TRIGGER = 4
GLFW_GAMEPAD_AXIS_RIGHT_TRIGGER = 5
GLFW_GAMEPAD_AXIS_LAST = GLFW_GAMEPAD_AXIS_RIGHT_TRIGGER
GLFW_NO_ERROR = 0
GLFW_NOT_INITIALIZED = 0x00010001
GLFW_NO_CURRENT_CONTEXT = 0x00010002
GLFW_INVALID_ENUM = 0x00010003
GLFW_INVALID_VALUE = 0x00010004
GLFW_OUT_OF_MEMORY = 0x00010005
GLFW_API_UNAVAILABLE = 0x00010006
GLFW_VERSION_UNAVAILABLE = 0x00010007
GLFW_PLATFORM_ERROR = 0x00010008
GLFW_FORMAT_UNAVAILABLE = 0x00010009
GLFW_NO_WINDOW_CONTEXT = 0x0001000A
GLFW_FOCUSED = 0x00020001
GLFW_ICONIFY = 0x00020002
GLFW_RESIZABLE = 0x00020003
GLFW_VISIBLE = 0x00020004
GLFW_DECORATED = 0x00020005
GLFW_AUTO_ICONIFY = 0x00020006
GLFW_FLOATING = 0x00020007
GLFW_MAXIMIZED = 0x00020008
GLFW_CENTER_CURSOR = 0x00020009
GLFW_TRANSPARENT_FRAME_BUFFER = 0x0002000A
GLFW_HOVERED = 0x0002000B
GLFW_FOCUS_ON_SHOW = 0x0002000C
GLFW_RED_BITS = 0x00021001
GLFW_GREEN_BITS = 0x00021002
GLFW_BLUE_BITS = 0x00021003
GLFW_ALPHA_BITS = 0x00021004
GLFW_DEPTH_BITS = 0x00021005
GLFW_STENCIL_BITS = 0x00021006
GLFW_ACCUMULATE_RED_BITS = 0x00021007
GLFW_ACCUMULATE_GREEN_BITS = 0x00021008
GLFW_ACCUMULATE_BLUE_BITS = 0x00021009
GLFW_ACCUMULATE_ALPHA_BITS = 0x0002100A
GLFW_AUX_BUFFERS = 0x0002100B
GLFW_STEREO = 0x0002100C
GLFW_SAMPLES = 0x0002100D
GLFW_S_RGB_CAPABLE = 0x0002100E
GLFW_REFRESH_RATE = 0x0002100F
GLFW_DOUBLE_BUFFER = 0x00021010
GLFW_CLIENT_API = 0x00022001
GLFW_CONTEXT_VERSION_MAJOR = 0x00022002
GLFW_CONTEXT_VERSION_MINOR = 0x00022003
GLFW_CONTEXT_REVISION = 0x00022004
GLFW_CONTEXT_ROBUSTNESS = 0x00022005
GLFW_OPENGL_FORWARD_COMPATIBLE = 0x00022006
GLFW_OPENGL_DEBUG_CONTEXT = 0x00022007
GLFW_OPENGL_PROFILE = 0x00022008
GLFW_CONTEXT_RELEASE_BEHAVIOR = 0x00022009
GLFW_CONTEXT_NO_ERROR = 0x0002200A
GLFW_CONTEXT_CREATION_API = 0x0002200B
GLFW_SCALE_TO_MONITOR = 0x0002200C
GLFW_COCOA_RETINA_FRAME_BUFFER = 0x00023001
GLFW_COCOA_FRAME_NAME = 0x00023002
GLFW_COCOA_GRAPHICS_SWITCHING = 0x00023003
GLFW_X11_CLASS_NAME = 0x00024001
GLFW_X11_INSTANCE_NAME = 0x00024002
GLFW_NO_API = 0
GLFW_OPENGL_API = 0x00030001
GLFW_OPENGL_ES_API = 0x00030002
GLFW_NO_ROBUSTNESS = 0
GLFW_NO_RESET_NOTIFICATION = 0x00031001
GLFW_LOSE_CONTEXT_ON_RESET = 0x00031002
GLFW_OPENGL_ANY_PROFILE = 0
GLFW_OPENGL_CORE_PROFILE = 0x00032001
GLFW_OPENGL_COMPATIBLE_PROFILE = 0x00032002
GLFW_CURSOR = 0x00033001
GLFW_STICKY_KEYS = 0x00033002
GLFW_STICKY_MOUSE_BUTTONS = 0x00033003
GLFW_LOCK_KEY_MODS = 0x00033004
GLFW_RAW_MOUSE_MOTION = 0x00033005
GLFW_CURSOR_NORMAL = 0x00034001
GLFW_CURSOR_HIDDEN = 0x00034002
GLFW_CURSOR_DISABLED = 0x00034003
GLFW_ANY_RELEASE_BEHAVIOR = 0
GLFW_RELEASE_BEHAVIOR_FLUSH = 0x00035001
GLFW_RELEASE_BEHAVIOR_NONE = 0x00035002
GLFW_NATIVE_CONTEXT_API = 0x00036001
GLFW_EGL_CONTEXT_API = 0x00036002
GLFW_OS_MESA_CONTEXT_API = 0x00036003
GLFW_ARROW_CURSOR = 0x00036001
GLFW_IBEAM_CURSOR = 0x00036002
GLFW_CROSSHAIR_CURSOR = 0x00036003
GLFW_HAND_CURSOR = 0x00036004
GLFW_HORIZON_RESIZE_CURSOR = 0x00036005
GLFW_VERTICAL_RESIZE_CURSOR = 0x00036006
GLFW_CONNECTED = 0x00040001
GLFW_DISCONNECTED = 0x00040002
GLFW_JOYSTICK_HAT_BUTTONS = 0x00050001
GLFW_COCOA_CHDIR_RESOURCES = 0x00051001
GLFW_COCOA_MENUBAR = 0x00051002
GLFW_DONT_CARE = -1


class Monitor(Structure):
    _fields_ = [("dummy", Int)]


class Window(Structure):
    _fields_ = [("dummy", Int)]


class Cursor(Structure):
    _fields_ = [("dummy", Int)]


class VidMode(Structure):
    _fields_ = [("width", Int),
                ("height", Int),
                ("red_bits", Int),
                ("green_bits", Int),
                ("blue_bits", Int),
                ("refresh_rate", UInt)]


class GammaRamp(Structure):
    _fields_ = [("red", P(UShort)),
                ("green", P(UShort)),
                ("blue", P(UShort)),
                ("size", UInt)]


class Image(ctypes.Structure):
    _fields_ = [("width", Int),
                ("height", Int),
                ("pixels", P(UByte))]


class Gamepad(ctypes.Structure):
    _fields_ = [("buttons", (UByte * 15)),
                ("axes", (Float * 6))]


glfwInit = glfw('glfwInit', Int)
glfwTerminate = glfw('glfwTerminate', None)
glfwInitHint = glfw('glfwInitHint', None, Int, Int)
glfwGetVersion = glfw('glfwGetVersion', None, P(Int), P(Int), P(Int))
glfwGetVersionString = glfw('glfwGetVersionString', CharP)
glfwGetError = glfw('glfwGetError', Int, P(CharP))
glfwGetMonitors = glfw('glfwGetMonitors', P(P(Monitor)), P(Int))
glfwGetPrimaryMonitor = glfw('glfwGetPrimaryMonitor', P(Monitor))
glfwGetMonitorPos = glfw(
    'glfwGetMonitorPos', None, P(Monitor), P(Int), P(Int))
glfwGetMonitorWorkArea = glfw(
    'glfwGetMonitorWork''area', None, P(Monitor), P(Int), P(Int), P(Int),
    P(Int))
glfwGetMonitorPhysicalSize = glfw(
    'glfwGetMonitorPhysicalSize', None, P(Monitor), P(Int), P(Int))
glfwGetMonitorContentScale = glfw(
    'glfwGetMonitorContentScale', None, P(Monitor), P(Float), P(Float))
glfwGetMonitorName = glfw('glfwGetMonitorName', CharP, P(Monitor))
glfwSetMonitorUserPointer = glfw(
    'glfwSetMonitorUserPointer', None, P(Monitor), VoidP)
glfwGetMonitorUserPointer = glfw(
    'glfwGetMonitorUserPointer', VoidP, P(Monitor))
glfwGetVideoModes = glfw(
    'glfwGetVideoModes', P(VidMode), P(Monitor), P(Int))
glfwGetVideoMode = glfw('glfwGetVideoMode', P(VidMode), P(Monitor))
glfwSetGamma = glfw('glfwSetGamma', None, P(Monitor), Float)
glfwGetGammaRamp = glfw('glfwGetGammaRamp', P(GammaRamp), P(Monitor))
glfwSetGammaRamp = glfw('glfwSetGammaRamp', None, P(Monitor), P(GammaRamp))
glfwDefaultWindowHints = glfw('glfwDefaultWindowHints', None)
glfwWindowHint = glfw('glfwWindowHint', None, Int, Int)
glfwWindowHintString = glfw('glfwWindowHintString', None, Int, CharP)
glfwCreateWindow = glfw(
    'glfwCreateWindow', P(Window), Int, Int, CharP, P(Monitor), P(Window))
glfwDestroyWindow = glfw('glfwDestroyWindow', None, P(Window))
glfwWindowShouldClose = glfw('glfwWindowShouldClose', Int, P(Window))
glfwSetWindowShouldClose = glfw(
    'glfwSetWindowShouldClose', None, P(Window), Int)
glfwSetWindowTitle = glfw('glfwSetWindowTitle', None, P(Window), CharP)
glfwSetWindowIcon = glfw(
    'glfwSetWindowIcon', None, P(Window), Int, P(Image))
glfwGetWindowPos = glfw('glfwGetWindowPos', None, P(Window), P(Int), P(Int))
glfwSetWindowPos = glfw('glfwSetWindowPos', None, P(Window), Int, Int)
glfwGetWindowSize = glfw(
    'glfwGetWindowSize', None, P(Window), P(Int), P(Int))
glfwSetWindowSizeLimits = glfw(
    'glfwSetWindowSizeLimits', None, P(Window), Int, Int, Int, Int)
glfwSetWindowAspectRatio = glfw(
    'glfwSetWindowAspectRatio', None, P(Window), Int, Int)
glfwSetWindowSize = glfw('glfwSetWindowSize', None, P(Window), Int, Int)
glfwGetFrameBufferSize = glfw(
    'glfwGetFrame''bufferSize', None, P(Window), P(Int), P(Int))
glfwGetWindowFrameSize = glfw(
    'glfwGetWindowFrameSize',
    None, P(Window), P(Int), P(Int), P(Int), P(Int))
glfwGetWindowContentScale = glfw(
    'glfwGetWindowContentScale', None, P(Window), P(Float), P(Float))
glfwGetWindowOpacity = glfw('glfwGetWindowOpacity', Float, P(Window))
glfwSetWindowOpacity = glfw('glfwSetWindowOpacity', None, P(Window), Float)
glfwIconifyWindow = glfw('glfwIconifyWindow', None, P(Window))
glfwRestoreWindow = glfw('glfwRestoreWindow', None, P(Window))
glfwMaximizeWindow = glfw('glfwMaximizeWindow', None, P(Window))
glfwShowWindow = glfw('glfwShowWindow', None, P(Window))
glfwHideWindow = glfw('glfwHideWindow', None, P(Window))
glfwFocusWindow = glfw('glfwFocusWindow', None, P(Window))
glfwRequestWindowAttention = glfw(
    'glfwRequestWindowAttention', None, P(Window))
glfwGetWindowMonitor = glfw('glfwGetWindowMonitor', P(Monitor), P(Window))
glfwSetWindowMonitor = glfw(
    'glfwSetWindowMonitor',
    None, P(Window), P(Monitor), Int, Int, Int, Int, Int)
glfwGetWindowAttrib = glfw('glfwGetWindowAttrib', Int, P(Window), Int)
glfwSetWindowAttrib = glfw('glfwSetWindowAttrib', None, P(Window), Int, Int)
glfwSetWindowUserPointer = glfw(
    'glfwSetWindowUserPointer', None, P(Window), VoidP)
glfwGetWindowUserPointer = glfw('glfwGetWindowUserPointer', VoidP, P(Window))
glfwPollEvents = glfw('glfwPollEvents', None)
glfwWaitEvents = glfw('glfwWaitEvents', None)
glfwWaitEventsTimeout = glfw('glfwWaitEventsTimeout', None, Double)
glfwPostEmptyEvent = glfw('glfwPostEmptyEvent', None)
glfwGetInputMode = glfw('glfwGetInputMode', Int, P(Window), Int)
glfwSetInputMode = glfw('glfwSetInputMode', None, P(Window), Int, Int)
glfwRawMouseMotionSupported = glfw('glfwRawMouseMotionSupported', Int)
glfwGetKeyName = glfw('glfwGetKeyName', CharP, Int, Int)
glfwGetKeyScancode = glfw('glfwGetKeyScancode', Int, Int)
glfwGetKey = glfw('glfwGetKey', Int, P(Window), Int)
glfwGetMouseButton = glfw('glfwGetMouseButton', Int, P(Window), Int)
glfwGetCursorPos = glfw(
    'glfwGetCursorPos', None, P(Window), P(Double), P(Double))
glfwSetCursorPos = glfw('glfwSetCursorPos', None, P(Window), Double, Double)
glfwCreateCursor = glfw('glfwCreateCursor', P(Cursor), P(Image), Int, Int)
glfwCreateStandardCursor = glfw('glfwCreateStandardCursor', P(Cursor), Int)
glfwDestroyCursor = glfw('glfwDestroyCursor', None, P(Cursor))
glfwSetCursor = glfw('glfwSetCursor', None, P(Window), P(Cursor))
glfwJoystickPresent = glfw('glfwJoystickPresent', Int, Int)
glfwGetJoystickAxes = glfw('glfwGetJoystickAxes', P(Float), Int, P(Int))
glfwGetJoystickButtons = glfw(
    'glfwGetJoystickButtons', P(UByte), Int, P(Int))
glfwGetJoystickHats = glfw('glfwGetJoystickHats', P(UByte), Int, P(Int))
glfwGetJoystickName = glfw('glfwGetJoystickName', CharP, Int)
glfwGetJoystickGUID = glfw('glfwGetJoystickGUID', CharP, Int)
glfwGetJoystickUserPointer = glfw('glfwGetJoystickUserPointer', VoidP, Int)
glfwSetJoystickUserPointer = glfw(
    'glfwSetJoystickUserPointer', None, Int, VoidP)
glfwJoystickIsGamepad = glfw('glfwJoystickIsGamepad', Int, Int)
glfwUpdateGamepadMappings = glfw('glfwUpdateGamepadMappings', Int, CharP)
glfwGetGamepadName = glfw('glfwGetGamepadName', CharP, Int)
glfwGetGamepadState = glfw('glfwGetGamepadState', Int, Int, P(Gamepad))
glfwGetClipboardString = glfw('glfwGetClipboardString', CharP, P(Window))
glfwSetClipboardString = glfw(
    'glfwSetClipboardString', None, P(Window), CharP)
glfwGetTime = glfw('glfwGetTime', Double)
glfwSetTime = glfw('glfwSetTime', None, Double)
glfwGetTimerValue = glfw('glfwGetTimerValue', ULong)
glfwGetTimerFrequency = glfw('glfwGetTimerFrequency', ULong)
glfwMakeContextCurrent = glfw('glfwMakeContextCurrent', None, P(Window))
glfwGetCurrentContext = glfw('glfwGetCurrentContext', P(Window))
glfwSwapBuffers = glfw('glfwSwapBuffers', None, P(Window))
glfwSwapInterval = glfw('glfwSwapInterval', None, Int)

GLFWErrorFun = C(None, Int, CharP)
GLFWWindowPosFun = C(None, P(Window), Int, Int)
GLFWWindowSizeFun = C(None, P(Window), Int, Int)
GLFWWindowCloseFun = C(None, P(Window))
GLFWWindowRefreshFun = C(None, P(Window))
GLFWWindowFocusFun = C(None, P(Window), Int)
GLFWWindowIconifyFun = C(None, P(Window), Int)
GLFWWindowMaximizeFun = C(None, P(Window), Int)
GLFWFrameBufferSizeFun = C(None, P(Window), Int, Int)
GLFWWindowContentScaleFun = C(None, P(Window), Float, Float)
GLFWMouseButtonFun = C(None, P(Window), Int, Int, Int)
GLFWCursorPosFun = C(None, P(Window), Double, Double)
GLFWCursorEnterFun = C(None, P(Window), Int)
GLFWScrollFun = C(None, P(Window), Double, Double)
GLFWKeyFun = C(None, P(Window), Int, Int, Int, Int)
GLFWCharFun = C(None, P(Window), UInt)
GLFWCharModsFun = C(None, P(Window), UInt, Int)
GLFWDropFun = C(None, P(Window), Int, P(CharP))
GLFWMonitorFun = C(None, P(Window), Int)
GLFWJoystickFun = C(None, Int, Int)

glfwSetErrorCallback = glfw(
    'glfwSetErrorCallback', GLFWErrorFun, GLFWErrorFun)
glfwSetMonitorCallback = glfw(
    'glfwSetMonitorCallback', GLFWMonitorFun, GLFWMonitorFun)
glfwSetWindowPosCallback = glfw(
    'glfwSetWindowPosCallback',
    GLFWWindowPosFun, P(Window), GLFWWindowPosFun)
glfwSetWindowSizeCallback = glfw(
    'glfwSetWindowSizeCallback',
    GLFWWindowSizeFun, P(Window), GLFWWindowSizeFun)
glfwSetWindowCloseCallback = glfw(
    'glfwSetWindowCloseCallback',
    GLFWWindowCloseFun, P(Window), GLFWWindowCloseFun)
glfwSetWindowRefreshCallback = glfw(
    'glfwSetWindowRefreshCallback',
    GLFWWindowRefreshFun, P(Window), GLFWWindowRefreshFun)
glfwSetWindowFocusCallback = glfw(
    'glfwSetWindowFocusCallback',
    GLFWWindowFocusFun, P(Window), GLFWWindowFocusFun)
glfwSetWindowIconifyCallback = glfw(
    'glfwSetWindowIconifyCallback',
    GLFWWindowIconifyFun, P(Window), GLFWWindowIconifyFun)
glfwSetWindowMaximizeCallback = glfw(
    'glfwSetWindowMaximizeCallback',
    GLFWWindowMaximizeFun, P(Window), GLFWWindowMaximizeFun)
glfwSetFrameBufferSizeCallback = glfw(
    'glfwSetFrame''bufferSizeCallback',
    GLFWFrameBufferSizeFun, P(Window), GLFWFrameBufferSizeFun)
glfwSetWindowContentScaleCallback = glfw(
    'glfwSetWindowContentScaleCallback',
    GLFWWindowContentScaleFun, P(Window), GLFWWindowContentScaleFun)
glfwSetKeyCallback = glfw(
    'glfwSetKeyCallback', GLFWKeyFun, P(Window), GLFWKeyFun)
glfwSetCharCallback = glfw(
    'glfwSetCharCallback', GLFWCharFun, P(Window), GLFWCharFun)
glfwSetCharModsCallback = glfw(
    'glfwSetCharModsCallback', GLFWCharModsFun, P(Window), GLFWCharModsFun)
glfwSetMouseButtonCallback = glfw(
    'glfwSetMouseButtonCallback',
    GLFWMouseButtonFun, P(Window), GLFWMouseButtonFun)
glfwSetCursorPosCallback = glfw(
    'glfwSetCursorPosCallback',
    GLFWCursorPosFun, P(Window), GLFWCursorPosFun)
glfwSetCursorEnterCallback = glfw(
    'glfwSetCursorEnterCallback',
    GLFWCursorEnterFun, P(Window), GLFWCursorEnterFun)
glfwSetScrollCallback = glfw(
    'glfwSetScrollCallback', GLFWScrollFun, P(Window), GLFWScrollFun)
glfwSetDropCallback = glfw(
    'glfwSetDropCallback', GLFWDropFun, P(Window), GLFWDropFun)
glfwSetJoystickCallback = glfw(
    'glfwSetJoystickCallback', GLFWJoystickFun, GLFWJoystickFun)

ProcAddress = C(None)

glfwExtensionSupported = glfw('glfwExtensionSupported', Int, CharP)
glfwGetProcAddress = glfw('glfwGetProcAddress', ProcAddress, CharP)
glfwVulkanSupported = glfw('glfwVulkanSupported', Int)
glfwGetRequiredInstanceExtensions = glfw(
    'glfwGetRequiredInstanceExtensions', P(CharP), P(UInt))


__all__ = [
    'GLFW_TRUE', 'GLFW_FALSE', 'GLFW_RELEASE', 'GLFW_PRESS', 'GLFW_REPEAT',
    'GLFW_HAT_CENTERED', 'GLFW_HAT_UP', 'GLFW_HAT_RIGHT', 'GLFW_HAT_DOWN',
    'GLFW_HAT_LEFT', 'GLFW_HAT_RIGHT_UP', 'GLFW_HAT_RIGHT_DOWN',
    'GLFW_HAT_LEFT_UP', 'GLFW_HAT_LEFT_DOWN', 'GLFW_KEY_UNKNOWN',
    'GLFW_KEY_SPACE', 'GLFW_KEY_APOSTROPHE', 'GLFW_KEY_COMMA',
    'GLFW_KEY_MINUS', 'GLFW_KEY_PERIOD', 'GLFW_KEY_SLASH', 'GLFW_KEY_0',
    'GLFW_KEY_1', 'GLFW_KEY_2', 'GLFW_KEY_3', 'GLFW_KEY_4', 'GLFW_KEY_5',
    'GLFW_KEY_6', 'GLFW_KEY_7', 'GLFW_KEY_8', 'GLFW_KEY_9',
    'GLFW_KEY_SEMICOLON', 'GLFW_KEY_EQUAL', 'GLFW_KEY_A', 'GLFW_KEY_B',
    'GLFW_KEY_C', 'GLFW_KEY_D', 'GLFW_KEY_E', 'GLFW_KEY_F', 'GLFW_KEY_G',
    'GLFW_KEY_H', 'GLFW_KEY_I', 'GLFW_KEY_J', 'GLFW_KEY_K', 'GLFW_KEY_L',
    'GLFW_KEY_M', 'GLFW_KEY_N', 'GLFW_KEY_O', 'GLFW_KEY_P', 'GLFW_KEY_Q',
    'GLFW_KEY_R', 'GLFW_KEY_S', 'GLFW_KEY_T', 'GLFW_KEY_U', 'GLFW_KEY_V',
    'GLFW_KEY_W', 'GLFW_KEY_X', 'GLFW_KEY_Y', 'GLFW_KEY_Z',
    'GLFW_KEY_LEFT_BRACKET', 'GLFW_KEY_BACKSLASH', 'GLFW_KEY_RIGHT_BRACKET',
    'GLFW_KEY_GRAVE_ACCENT', 'GLFW_KEY_WORLD_1', 'GLFW_KEY_WORLD_2',
    'GLFW_KEY_ESCAPE', 'GLFW_KEY_ENTER', 'GLFW_KEY_TAB', 'GLFW_KEY_BACKSPACE',
    'GLFW_KEY_INSERT', 'GLFW_KEY_DELETE', 'GLFW_KEY_RIGHT', 'GLFW_KEY_LEFT',
    'GLFW_KEY_DOWN', 'GLFW_KEY_UP', 'GLFW_KEY_PAGE_UP', 'GLFW_KEY_PAGE_DOWN',
    'GLFW_KEY_HOME', 'GLFW_KEY_END', 'GLFW_KEY_CAPS_LOCK',
    'GLFW_KEY_SCROLL_LOCK', 'GLFW_KEY_NUM_LOCK', 'GLFW_KEY_PRINT_SCREEN',
    'GLFW_KEY_PAUSE', 'GLFW_KEY_F1', 'GLFW_KEY_F2', 'GLFW_KEY_F3',
    'GLFW_KEY_F4', 'GLFW_KEY_F5', 'GLFW_KEY_F6', 'GLFW_KEY_F7', 'GLFW_KEY_F8',
    'GLFW_KEY_F9', 'GLFW_KEY_F10', 'GLFW_KEY_F11', 'GLFW_KEY_F12',
    'GLFW_KEY_F13', 'GLFW_KEY_F14', 'GLFW_KEY_F15', 'GLFW_KEY_F16',
    'GLFW_KEY_F17', 'GLFW_KEY_F18', 'GLFW_KEY_F19', 'GLFW_KEY_F20',
    'GLFW_KEY_F21', 'GLFW_KEY_F22', 'GLFW_KEY_F23', 'GLFW_KEY_F24',
    'GLFW_KEY_F25', 'GLFW_KEY_KP_0', 'GLFW_KEY_KP_1', 'GLFW_KEY_KP_2',
    'GLFW_KEY_KP_3', 'GLFW_KEY_KP_4', 'GLFW_KEY_KP_5', 'GLFW_KEY_KP_6',
    'GLFW_KEY_KP_7', 'GLFW_KEY_KP_8', 'GLFW_KEY_KP_9', 'GLFW_KEY_KP_DECIMAL',
    'GLFW_KEY_KP_DIVIDE', 'GLFW_KEY_KP_MULTIPLY', 'GLFW_KEY_KP_SUBTRACT',
    'GLFW_KEY_KP_ADD', 'GLFW_KEY_KP_ENTER', 'GLFW_KEY_KP_EQUAL',
    'GLFW_KEY_LEFT_SHIFT', 'GLFW_KEY_LEFT_CONTROL', 'GLFW_KEY_LEFT_ALT',
    'GLFW_KEY_LEFT_SUPER', 'GLFW_KEY_RIGHT_SHIFT', 'GLFW_KEY_RIGHT_CONTROL',
    'GLFW_KEY_RIGHT_ALT', 'GLFW_KEY_RIGHT_SUPER', 'GLFW_KEY_MENU',
    'GLFW_KEY_LAST', 'GLFW_MOD_SHIFT', 'GLFW_MOD_CONTROL', 'GLFW_MOD_ALT',
    'GLFW_MOD_SUPER', 'GLFW_MOD_CAPS_LOCK', 'GLFW_MOD_NUM_LOCK',
    'GLFW_MOUSE_BUTTON_1', 'GLFW_MOUSE_BUTTON_2', 'GLFW_MOUSE_BUTTON_3',
    'GLFW_MOUSE_BUTTON_4', 'GLFW_MOUSE_BUTTON_5', 'GLFW_MOUSE_BUTTON_6',
    'GLFW_MOUSE_BUTTON_7', 'GLFW_MOUSE_BUTTON_8', 'GLFW_MOUSE_BUTTON_LAST',
    'GLFW_MOUSE_BUTTON_LEFT', 'GLFW_MOUSE_BUTTON_RIGHT',
    'GLFW_MOUSE_BUTTON_MIDDLE', 'GLFW_JOYSTICK_1', 'GLFW_JOYSTICK_2',
    'GLFW_JOYSTICK_3', 'GLFW_JOYSTICK_4', 'GLFW_JOYSTICK_5',
    'GLFW_JOYSTICK_6', 'GLFW_JOYSTICK_7', 'GLFW_JOYSTICK_8',
    'GLFW_JOYSTICK_9', 'GLFW_JOYSTICK_10', 'GLFW_JOYSTICK_11',
    'GLFW_JOYSTICK_12', 'GLFW_JOYSTICK_13', 'GLFW_JOYSTICK_14',
    'GLFW_JOYSTICK_15', 'GLFW_JOYSTICK_16', 'GLFW_JOYSTICK_LAST',
    'GLFW_GAMEPAD_BUTTON_A', 'GLFW_GAMEPAD_BUTTON_B', 'GLFW_GAMEPAD_BUTTON_X',
    'GLFW_GAMEPAD_BUTTON_Y', 'GLFW_GAMEPAD_BUTTON_LEFT_BUMPER',
    'GLFW_GAMEPAD_BUTTON_RIGHT_BUMPER', 'GLFW_GAMEPAD_BUTTON_BACK',
    'GLFW_GAMEPAD_BUTTON_START', 'GLFW_GAMEPAD_BUTTON_GUIDE',
    'GLFW_GAMEPAD_BUTTON_LEFT_THUMB', 'GLFW_GAMEPAD_BUTTON_RIGHT_THUMB',
    'GLFW_GAMEPAD_BUTTON_ANDROID_PAD_UP',
    'GLFW_GAMEPAD_BUTTON_ANDROID_PAD_RIGHT',
    'GLFW_GAMEPAD_BUTTON_ANDROID_PAD_DOWN',
    'GLFW_GAMEPAD_BUTTON_ANDROID_PAD_LEFT', 'GLFW_GAMEPAD_BUTTON_LAST',
    'GLFW_GAMEPAD_BUTTON_CROSS', 'GLFW_GAMEPAD_BUTTON_CIRCLE',
    'GLFW_GAMEPAD_BUTTON_SQUARE', 'GLFW_GAMEPAD_BUTTON_TRIANGLE',
    'GLFW_GAMEPAD_AXIS_LEFT_X', 'GLFW_GAMEPAD_AXIS_LEFT_Y',
    'GLFW_GAMEPAD_AXIS_RIGHT_X', 'GLFW_GAMEPAD_AXIS_RIGHT_Y',
    'GLFW_GAMEPAD_AXIS_LEFT_TRIGGER', 'GLFW_GAMEPAD_AXIS_RIGHT_TRIGGER',
    'GLFW_GAMEPAD_AXIS_LAST', 'GLFW_NO_ERROR', 'GLFW_NOT_INITIALIZED',
    'GLFW_NO_CURRENT_CONTEXT', 'GLFW_INVALID_ENUM', 'GLFW_INVALID_VALUE',
    'GLFW_OUT_OF_MEMORY', 'GLFW_API_UNAVAILABLE', 'GLFW_VERSION_UNAVAILABLE',
    'GLFW_PLATFORM_ERROR', 'GLFW_FORMAT_UNAVAILABLE',
    'GLFW_NO_WINDOW_CONTEXT', 'GLFW_FOCUSED', 'GLFW_ICONIFY',
    'GLFW_RESIZABLE', 'GLFW_VISIBLE', 'GLFW_DECORATED', 'GLFW_AUTO_ICONIFY',
    'GLFW_FLOATING', 'GLFW_MAXIMIZED', 'GLFW_CENTER_CURSOR',
    'GLFW_TRANSPARENT_FRAME_BUFFER', 'GLFW_HOVERED', 'GLFW_FOCUS_ON_SHOW',
    'GLFW_RED_BITS', 'GLFW_GREEN_BITS', 'GLFW_BLUE_BITS', 'GLFW_ALPHA_BITS',
    'GLFW_DEPTH_BITS', 'GLFW_STENCIL_BITS', 'GLFW_ACCUMULATE_RED_BITS',
    'GLFW_ACCUMULATE_GREEN_BITS', 'GLFW_ACCUMULATE_BLUE_BITS',
    'GLFW_ACCUMULATE_ALPHA_BITS', 'GLFW_AUX_BUFFERS', 'GLFW_STEREO',
    'GLFW_SAMPLES', 'GLFW_S_RGB_CAPABLE', 'GLFW_REFRESH_RATE',
    'GLFW_DOUBLE_BUFFER', 'GLFW_CLIENT_API', 'GLFW_CONTEXT_VERSION_MAJOR',
    'GLFW_CONTEXT_VERSION_MINOR', 'GLFW_CONTEXT_REVISION',
    'GLFW_CONTEXT_ROBUSTNESS', 'GLFW_OPENGL_FORWARD_COMPATIBLE',
    'GLFW_OPENGL_DEBUG_CONTEXT', 'GLFW_OPENGL_PROFILE',
    'GLFW_CONTEXT_RELEASE_BEHAVIOR', 'GLFW_CONTEXT_NO_ERROR',
    'GLFW_CONTEXT_CREATION_API', 'GLFW_SCALE_TO_MONITOR',
    'GLFW_COCOA_RETINA_FRAME_BUFFER', 'GLFW_COCOA_FRAME_NAME',
    'GLFW_COCOA_GRAPHICS_SWITCHING', 'GLFW_X11_CLASS_NAME',
    'GLFW_X11_INSTANCE_NAME', 'GLFW_NO_API', 'GLFW_OPENGL_API',
    'GLFW_OPENGL_ES_API', 'GLFW_NO_ROBUSTNESS', 'GLFW_NO_RESET_NOTIFICATION',
    'GLFW_LOSE_CONTEXT_ON_RESET', 'GLFW_OPENGL_ANY_PROFILE',
    'GLFW_OPENGL_CORE_PROFILE', 'GLFW_OPENGL_COMPATIBLE_PROFILE',
    'GLFW_CURSOR', 'GLFW_STICKY_KEYS', 'GLFW_STICKY_MOUSE_BUTTONS',
    'GLFW_LOCK_KEY_MODS', 'GLFW_RAW_MOUSE_MOTION', 'GLFW_CURSOR_NORMAL',
    'GLFW_CURSOR_HIDDEN', 'GLFW_CURSOR_DISABLED', 'GLFW_ANY_RELEASE_BEHAVIOR',
    'GLFW_RELEASE_BEHAVIOR_FLUSH', 'GLFW_RELEASE_BEHAVIOR_NONE',
    'GLFW_NATIVE_CONTEXT_API', 'GLFW_EGL_CONTEXT_API',
    'GLFW_OS_MESA_CONTEXT_API', 'GLFW_ARROW_CURSOR', 'GLFW_IBEAM_CURSOR',
    'GLFW_CROSSHAIR_CURSOR', 'GLFW_HAND_CURSOR', 'GLFW_HORIZON_RESIZE_CURSOR',
    'GLFW_VERTICAL_RESIZE_CURSOR', 'GLFW_CONNECTED', 'GLFW_DISCONNECTED',
    'GLFW_JOYSTICK_HAT_BUTTONS', 'GLFW_COCOA_CHDIR_RESOURCES',
    'GLFW_COCOA_MENUBAR', 'GLFW_DONT_CARE', 'Monitor', 'Window', 'Cursor',
    'VidMode', 'GammaRamp', 'Image', 'Gamepad', 'glfwInit', 'glfwTerminate',
    'glfwInitHint', 'glfwGetVersion', 'glfwGetVersionString', 'glfwGetError',
    'glfwGetMonitors', 'glfwGetPrimaryMonitor', 'glfwGetMonitorPos',
    'glfwGetMonitorWorkArea', 'glfwGetMonitorPhysicalSize',
    'glfwGetMonitorContentScale', 'glfwGetMonitorName',
    'glfwSetMonitorUserPointer', 'glfwGetMonitorUserPointer',
    'glfwGetVideoModes', 'glfwGetVideoMode', 'glfwSetGamma',
    'glfwGetGammaRamp', 'glfwSetGammaRamp', 'glfwDefaultWindowHints',
    'glfwWindowHint', 'glfwWindowHintString', 'glfwCreateWindow',
    'glfwDestroyWindow', 'glfwWindowShouldClose', 'glfwSetWindowShouldClose',
    'glfwSetWindowTitle', 'glfwSetWindowIcon', 'glfwGetWindowPos',
    'glfwSetWindowPos', 'glfwGetWindowSize', 'glfwSetWindowSizeLimits',
    'glfwSetWindowAspectRatio', 'glfwSetWindowSize', 'glfwGetFrameBufferSize',
    'glfwGetWindowFrameSize', 'glfwGetWindowContentScale',
    'glfwGetWindowOpacity', 'glfwSetWindowOpacity', 'glfwIconifyWindow',
    'glfwRestoreWindow', 'glfwMaximizeWindow', 'glfwShowWindow',
    'glfwHideWindow', 'glfwFocusWindow', 'glfwRequestWindowAttention',
    'glfwGetWindowMonitor', 'glfwSetWindowMonitor', 'glfwGetWindowAttrib',
    'glfwSetWindowAttrib', 'glfwSetWindowUserPointer',
    'glfwGetWindowUserPointer', 'glfwPollEvents', 'glfwWaitEvents',
    'glfwWaitEventsTimeout', 'glfwPostEmptyEvent', 'glfwGetInputMode',
    'glfwSetInputMode', 'glfwRawMouseMotionSupported', 'glfwGetKeyName',
    'glfwGetKeyScancode', 'glfwGetKey', 'glfwGetMouseButton',
    'glfwGetCursorPos', 'glfwSetCursorPos', 'glfwCreateCursor',
    'glfwCreateStandardCursor', 'glfwDestroyCursor', 'glfwSetCursor',
    'glfwJoystickPresent', 'glfwGetJoystickAxes', 'glfwGetJoystickButtons',
    'glfwGetJoystickHats', 'glfwGetJoystickName', 'glfwGetJoystickGUID',
    'glfwGetJoystickUserPointer', 'glfwSetJoystickUserPointer',
    'glfwJoystickIsGamepad', 'glfwUpdateGamepadMappings',
    'glfwGetGamepadName', 'glfwGetGamepadState', 'glfwGetClipboardString',
    'glfwSetClipboardString', 'glfwGetTime', 'glfwSetTime',
    'glfwGetTimerValue', 'glfwGetTimerFrequency', 'glfwMakeContextCurrent',
    'glfwGetCurrentContext', 'glfwSwapBuffers', 'glfwSwapInterval',
    'GLFWErrorFun', 'GLFWWindowPosFun', 'GLFWWindowSizeFun',
    'GLFWWindowCloseFun', 'GLFWWindowRefreshFun', 'GLFWWindowFocusFun',
    'GLFWWindowIconifyFun', 'GLFWWindowMaximizeFun', 'GLFWFrameBufferSizeFun',
    'GLFWWindowContentScaleFun', 'GLFWMouseButtonFun', 'GLFWCursorPosFun',
    'GLFWCursorEnterFun', 'GLFWScrollFun', 'GLFWKeyFun', 'GLFWCharFun',
    'GLFWCharModsFun', 'GLFWDropFun', 'GLFWMonitorFun', 'GLFWJoystickFun',
    'glfwSetErrorCallback', 'glfwSetMonitorCallback',
    'glfwSetWindowPosCallback', 'glfwSetWindowSizeCallback',
    'glfwSetWindowCloseCallback', 'glfwSetWindowRefreshCallback',
    'glfwSetWindowFocusCallback', 'glfwSetWindowIconifyCallback',
    'glfwSetWindowMaximizeCallback', 'glfwSetFrameBufferSizeCallback',
    'glfwSetWindowContentScaleCallback', 'glfwSetKeyCallback',
    'glfwSetCharCallback', 'glfwSetCharModsCallback',
    'glfwSetMouseButtonCallback', 'glfwSetCursorPosCallback',
    'glfwSetCursorEnterCallback', 'glfwSetScrollCallback',
    'glfwSetDropCallback', 'glfwSetJoystickCallback',
    'glfwExtensionSupported', 'glfwGetProcAddress', 'glfwVulkanSupported',
    'glfwGetRequiredInstanceExtensions'
]
