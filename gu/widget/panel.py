import ctypes

from ._viewport import view
from ._taproot import Widget

from ..opengl import *


class ColoredPanel(Widget):
    _cp_program = 0
    _cp_camera = 0
    _cp_vao = 0
    _cp_vbo = 0
    _cp_ebo = 0

    @classmethod
    def widget_initial(cls):
        _vertex = """#version 330
            uniform mat4 gu_camera;
            in vec2 gu_position;
            in vec3 gu_color;
            out vec4 inner_color;
    
            void main() {
                inner_color = vec4(gu_color, 1);
                gl_Position = gu_camera * vec4(gu_position, 0, 1);
            }
        """
        _fragment = """#version 330
            in vec4 inner_color;
            out vec4 out_color;

            void main() {
                out_color = inner_color;
            }
        """
        _program = shader_program(
            GL_VERTEX_SHADER=_vertex, GL_FRAGMENT_SHADER=_fragment)

        _camera = glGetUniformLocation(_program, b'gu_camera')

        _vao = ctypes.c_uint()
        glGenVertexArrays(1, _vao)
        glBindVertexArray(_vao)

        _vbo = ctypes.c_uint()
        glGenBuffers(1, _vbo)
        glBindBuffer(GL_ARRAY_BUFFER, _vbo)
        glBufferData(GL_ARRAY_BUFFER, 20 * 4, 0, GL_STREAM_DRAW)

        _gu_position = glGetAttribLocation(_program, b'gu_position')
        glEnableVertexAttribArray(_gu_position)
        glVertexAttribPointer(_gu_position, 2, GL_FLOAT, GL_FALSE, 5 * 4, 0)

        _gu_color = glGetAttribLocation(_program, b'gu_color')
        glEnableVertexAttribArray(_gu_color)
        glVertexAttribPointer(_gu_color, 3, GL_FLOAT, GL_FALSE, 5 * 4, 2 * 4)

        _ebo = ctypes.c_uint()
        glGenBuffers(1, _ebo)
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, _ebo)
        _index = (ctypes.c_uint * 6)(0, 1, 2, 0, 2, 3)
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, 6 * 4, _index, GL_STATIC_DRAW)

        glBindVertexArray(0)
        glBindBuffer(GL_ARRAY_BUFFER, 0)
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, 0)

        cls._cp_program = _program
        cls._cp_camera = _camera
        cls._cp_vao = _vao
        cls._cp_vbo = _vbo
        cls._cp_ebo = _ebo

    @classmethod
    def widget_final(cls):
        glDeleteProgram(cls._cp_program)
        glDeleteVertexArrays(1, cls._cp_vao)
        glDeleteBuffers(1, cls._cp_vbo)
        glDeleteBuffers(1, cls._cp_ebo)

    @classmethod
    def widget_ortho(cls):
        glProgramUniformMatrix4fv(
            cls._cp_program, cls._cp_camera, 1, 0, view.view_ortho)

    def __init__(
            self, name=None, relate=(0, 0), offset=(0, 0), size=(128, 128),
            anchor=(0, 0), border=(0, 0, 0, 0), color=(0.5, 0.4, 0.8),
            visual=True):

        self._panel_color = color
        self._panel_buffer = 0

        Widget.__init__(
            self, name, relate, offset, size, anchor, border, visual)

    def widget_resize(self):
        super().widget_resize()

        _b0, _b1, _b2, _b3 = self._widget_outline
        _cr, _cg, _cb = self._panel_color

        self._panel_buffer = (ctypes.c_float * 20)(
            _b0, _b1, _cr, _cg, _cb,
            _b0, _b3, _cr, _cg, _cb,
            _b2, _b3, _cr, _cg, _cb,
            _b2, _b1, _cr, _cg, _cb,
        )

    def widget_update(self):
        glBindBuffer(GL_ARRAY_BUFFER, self._cp_vbo)
        glBufferSubData(GL_ARRAY_BUFFER, 0, 20 * 4, self._panel_buffer)
        glUseProgram(self._cp_program)
        glBindVertexArray(self._cp_vao)
        glDrawElements(GL_TRIANGLES, 6, GL_UNSIGNED_INT, 0)
        glBindVertexArray(0)
        glUseProgram(0)
