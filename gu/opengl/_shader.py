import ctypes

from ._library import (
    glCreateShader, gl_get, OpenGLError, glShaderSource, glCompileShader,
    glGetShaderiv, GL_COMPILE_STATUS, GL_INFO_LOG_LENGTH, glGetShaderInfoLog,
    glDeleteShader, glAttachShader, glCreateProgram, glLinkProgram,
    glValidateProgram, glGetProgramiv, GL_LINK_STATUS, glGetProgramInfoLog,
    glDeleteProgram
)


def create_shader(program, target, source):
    """ 创建着色器管线 """

    _shader = glCreateShader(gl_get(target))

    if not _shader:
        raise OpenGLError('无法创建(Shader)着色器')

    _string = ctypes.create_string_buffer(source.encode())
    _char_pp = (ctypes.c_char_p * 1)(ctypes.cast(_string, ctypes.c_char_p))

    glShaderSource(_shader, 1, _char_pp, None)
    glCompileShader(_shader)

    _compiled = ctypes.c_int()
    glGetShaderiv(_shader, GL_COMPILE_STATUS, _compiled)
    if not _compiled:
        _length = ctypes.c_int()
        glGetShaderiv(_shader, GL_INFO_LOG_LENGTH, _length)
        _log = (ctypes.c_char * _length.value)()
        glGetShaderInfoLog(_shader, _length, _length, _log)
        glDeleteShader(_shader)
        raise OpenGLError(bytes(_log).decode())

    glAttachShader(program, _shader)

    return _shader


def shader_program(**shaders):
    """ 创建显卡渲染程序

    参数：
        - shaders 是一个字典，键值包含
        GL_VERTEX_SHADER, GL_TESS_EVALUATION_SHADER, GL_TESS_CONTROL_SHADER,
        GL_GEOMETRY_SHADER, GL_FRAGMENT_SHADER, GL_COMPUTE_SHADER
    返回一个渲染程序序列号
    """
    _program = glCreateProgram()

    if not _program:
        raise OpenGLError('无法创建(Program)渲染程序')

    _shaders = tuple(create_shader(_program, _target, _source)
                     for _target, _source in shaders.items())

    glLinkProgram(_program)

    for _shader in _shaders:
        glDeleteShader(_shader)

    glValidateProgram(_program)

    _linked = ctypes.c_int()
    glGetProgramiv(_program, GL_LINK_STATUS, _linked)
    if not _linked:
        _length = ctypes.c_int()
        glGetProgramiv(_program, GL_INFO_LOG_LENGTH, _length)
        _log = (ctypes.c_char * _length.value)()
        glGetProgramInfoLog(_program, _length, _length, _log)
        glDeleteProgram(_program)
        raise OpenGLError(bytes(_log).decode())

    return _program


__all__ = ['shader_program']
