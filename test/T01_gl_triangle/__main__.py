import ctypes

from gu.opengl import *


class User:
    def __init__(self):
        self.program = 0
        self.vao = 0
        self.vbo = 0

    def __repr__(self):
        return 'User'

    def __str__(self):
        return str(self.__dict__)


user = User()


def window_initial():
    _vertex = """#version 330
        in vec4 gu_position;
        void main() {
            gl_Position = gu_position;
        }
    """

    _fragment = """#version 330
        out vec4 frag_color;
        void main() {
            frag_color = vec4(0.5, 0.4, 0.8, 1.0);
        }
    """

    _program = shader_program(
        GL_VERTEX_SHADER=_vertex, GL_FRAGMENT_SHADER=_fragment)

    _position = (ctypes.c_float * 12)(
        -0.5, 0.3, 0, 1,
        0.3, 0.3, 0, 1,
        0.3, -0.5, 0, 1
    )

    _vao = ctypes.c_uint()
    glGenVertexArrays(1, _vao)
    glBindVertexArray(_vao)

    _vbo = ctypes.c_uint()
    glGenBuffers(1, _vbo)
    glBindBuffer(GL_ARRAY_BUFFER, _vbo)
    glBufferData(GL_ARRAY_BUFFER, 12 * 4, _position, GL_STATIC_DRAW)

    _gu_position = glGetAttribLocation(_program, b'gu_position')
    glEnableVertexAttribArray(_gu_position)
    glVertexAttribPointer(_gu_position, 4, GL_FLOAT, GL_FALSE, 4 * 4, 0)

    glBindBuffer(GL_ARRAY_BUFFER, 0)
    glBindVertexArray(0)

    user.program = _program
    user.vao = _vao
    user.vbo = _vbo


def window_render():
    glUseProgram(user.program)

    glBindVertexArray(user.vao)
    glDrawArrays(GL_TRIANGLES, 0, 3)

    glBindVertexArray(0)
    glUseProgram(0)


def window_final():
    glDeleteProgram(user.program)
    glDeleteBuffers(1, user.vbo)
    glDeleteVertexArrays(1, user.vao)
