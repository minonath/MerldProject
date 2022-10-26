import io

from gu.libpng import read_png
from gu.opengl import *
from gu.system import icon
from gu.widget import _viewport


_width, _height, _, _data = read_png(io.BytesIO(icon))


class User:
    def __init__(self):
        self.program = 0
        self.vao = 0
        self.vbo = 0
        self.ibo = 0
        self.fbo = 0
        self.texture = 0


user = User()


def window_initial():
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    glDisable(GL_CULL_FACE)
    glEnable(GL_DEPTH_TEST)

    glClearColor(0, 0, 0, 0.5)

    _vertex = """#version 330
        in vec2 gu_position;
        in vec2 gu_frag_uv;
        out vec2 inner_uv;

        void main() {
            inner_uv = gu_frag_uv;
            gl_Position = vec4(gu_position, 0, 1);
        }
    """

    _fragment = """#version 330
        uniform sampler2D gu_texture;
        in vec2 inner_uv;
        out vec4 frag_color;

        void main() {
            frag_color = texture(gu_texture, inner_uv.st);
        }
    """

    _program = shader_program(
        GL_VERTEX_SHADER=_vertex, GL_FRAGMENT_SHADER=_fragment)

    _position = (Float * 16)(
        0, 1, 0, 0,
        0, 0, 0, 1,
        1, 0, 1, 1,
        1, 1, 1, 0
    )

    _element = (UInt * 6)(
        0, 1, 2, 0, 2, 3
    )

    _vao = UInt()
    glGenVertexArrays(1, _vao)
    glBindVertexArray(_vao)

    _vbo = UInt()
    glGenBuffers(1, _vbo)
    glBindBuffer(GL_ARRAY_BUFFER, _vbo)
    glBufferData(GL_ARRAY_BUFFER, 16 * 4, _position, GL_STATIC_DRAW)

    _gu_position = glGetAttribLocation(_program, b'gu_position')
    _gu_frag_uv = glGetAttribLocation(_program, b'gu_frag_uv')
    glEnableVertexAttribArray(_gu_position)
    glVertexAttribPointer(_gu_position, 2, GL_FLOAT, GL_FALSE, 4 * 4, 0)
    glEnableVertexAttribArray(_gu_frag_uv)
    glVertexAttribPointer(_gu_frag_uv, 2, GL_FLOAT, GL_FALSE, 4 * 4, 2 * 4)

    _ibo = UInt()
    glGenBuffers(1, _ibo)
    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, _ibo)
    glBufferData(GL_ELEMENT_ARRAY_BUFFER, 6 * 4, _element, GL_STATIC_DRAW)

    glBindVertexArray(0)
    glBindBuffer(GL_ARRAY_BUFFER, 0)
    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, 0)

    _inner_texture = UInt()
    glGenTextures(1, _inner_texture)
    glBindTexture(GL_TEXTURE_2D, _inner_texture)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, _width, _height, 0,
                 GL_RGBA, GL_UNSIGNED_BYTE, _data)

    _gu_texture = glGetUniformLocation(_program, b'gu_texture')
    glProgramUniform1ui(_program, _gu_texture, _inner_texture)

    _fbo = UInt()
    glGenFramebuffers(1, _fbo)
    _texture = UInt()
    glGenTextures(1, _texture)
    glBindTexture(GL_TEXTURE_2D, _texture)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)

    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, viewport[2], viewport[3], 0,
                 GL_RGBA, GL_UNSIGNED_BYTE, 0)

    glBindFramebuffer(GL_FRAMEBUFFER, _fbo)
    glFramebufferTexture2D(GL_FRAMEBUFFER, GL_COLOR_ATTACHMENT0,
                           GL_TEXTURE_2D, _texture, 0)

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glUseProgram(_program)
    glBindTexture(GL_TEXTURE_2D, _inner_texture)
    glBindVertexArray(_vao)
    glDrawElements(GL_TRIANGLES, 6, GL_UNSIGNED_INT, 0)
    glBindVertexArray(0)
    glBindTexture(GL_TEXTURE_2D, 0)
    glUseProgram(0)

    glBindFramebuffer(GL_FRAMEBUFFER, 0)
    glDeleteTextures(1, _inner_texture)

    glProgramUniform1ui(_program, _gu_texture, _texture)
    glClearColor(0.5, 0.4, 0.8, 1.0)

    # _position_frame = (ctypes.c_float * 16)(
    #     0, 1, 0, 1,
    #     0, 0, 0, 0,
    #     1, 0, 1, 0,
    #     1, 1, 1, 1
    # )
    #
    # glBindBuffer(GL_ARRAY_BUFFER, _vbo)
    # glBufferSubData(GL_ARRAY_BUFFER, 0, 16 * 4, _position_frame)

    user.program = _program
    user.vao = _vao
    user.vbo = _vbo
    user.ibo = _ibo
    user.fbo = _fbo
    user.texture = _texture


def window_render():
    glUseProgram(user.program)
    glBindTexture(GL_TEXTURE_2D, user.texture)
    glBindVertexArray(user.vao)
    glDrawElements(GL_TRIANGLES, 6, GL_UNSIGNED_INT, 0)
    glBindVertexArray(0)
    glBindTexture(GL_TEXTURE_2D, 0)
    glUseProgram(0)


def window_final():
    glDeleteProgram(user.program)
    glDeleteBuffers(1, user.vbo)
    glDeleteBuffers(1, user.ibo)
    glDeleteVertexArrays(1, user.vao)
    glDeleteFramebuffers(1, user.fbo)
    glDeleteTextures(1, user.texture)
