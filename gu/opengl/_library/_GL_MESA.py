from .._wrapper import *

GL_MESA_framebuffer_flip_x = 1
GL_FRAMEBUFFER_FLIP_X_MESA = 0x8BBC
GL_MESA_framebuffer_flip_y = 1
GL_FRAMEBUFFER_FLIP_Y_MESA = 0x8BBB
PFNGLFRAMEBUFFERPARAMETERIMESAPROC = C(None, UInt, UInt, Int)
PFNGLGETFRAMEBUFFERPARAMETERIVMESAPROC = C(None, UInt, UInt, P(Int))
glFramebufferParameteriMESA = GL(
    'glFramebufferParameteriMESA', None, UInt, UInt, Int
)
glGetFramebufferParameterivMESA = GL(
    'glGetFramebufferParameterivMESA', None, UInt, UInt, P(Int)
)
GL_MESA_framebuffer_swap_xy = 1
GL_FRAMEBUFFER_SWAP_XY_MESA = 0x8BBD

__all__ = [
    'GL_MESA_framebuffer_flip_x', 'GL_FRAMEBUFFER_FLIP_X_MESA',
    'GL_MESA_framebuffer_flip_y', 'GL_FRAMEBUFFER_FLIP_Y_MESA',
    'PFNGLFRAMEBUFFERPARAMETERIMESAPROC',
    'PFNGLGETFRAMEBUFFERPARAMETERIVMESAPROC', 'glFramebufferParameteriMESA',
    'glGetFramebufferParameterivMESA', 'GL_MESA_framebuffer_swap_xy',
    'GL_FRAMEBUFFER_SWAP_XY_MESA'
]
