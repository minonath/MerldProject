"""
关于 FontData 的格式

'data' 部分记录图片数据，实际上是图片序列化信息数组，即 GL_TEXTURE_2D_ARRAY
'json' 部分记录字体信息
'json.ascent' 为字体基线上段的长度
'json.descent' 为字体基线下段的长度
'json.size' 为字体默认宽度
'json.boundary' 为 GL_TEXTURE_2D_ARRAY 的尺寸，长宽统一，为 2 的 n 次方
'json.level' 为 GL_TEXTURE_2D_ARRAY 的层数
'json.chunk' 图片序列化信息分段后压缩的体积是不一样长的，这里记录长度用于解压
'json.data' 为文字对应的 Unicode 信息，每个文字对应的信息如下：
'json.data.level' 文字贴图的层数 / 深度偏移
'json.data.offset.u' 文字贴图的横向偏移
'json.data.offset.v' 文字贴图的纵向偏移
'json.data.width' 文字宽度
"""
import os
import json
import zlib

from ..math3d import Array
from ..opengl import *
from ._viewport import view

font_directory = os.path.join(os.path.dirname(__file__), 'font')

try:
    import PIL.Image
    import PIL.ImageDraw
    import PIL.ImageFont
    import math

    def font_level(images, bound):
        _index = len(images)
        _image = PIL.Image.new('RGBA', (bound, bound), (255, 255, 255, 0))
        _draw = PIL.ImageDraw.Draw(_image)
        images.append(_image)
        return _draw, _index, 0


    def font_builder(name, size, bound=1024, space=-1, sampler=1, png=False):
        if space == -1:
            space = size // 4

        _images = []
        _record = []

        _absolute = os.path.join(font_directory, name)
        _font = PIL.ImageFont.FreeTypeFont(_absolute, size=size * sampler)

        _metric = _font.getmetrics()
        _height = sum(_metric)
        _height_i = _height + space

        _len = bound * sampler

        _draw, _index, _row = font_level(_images, _len)
        _column = 0

        for _i in range(65536):
            _char = chr(_i)
            _width = _font.getlength(_char)
            if _width:
                _width = math.ceil(_width)
                _width_i = _width + space
                if _column + _width_i > _len:
                    _row += _height_i
                    if _row + _height_i > _len:
                        _draw, _index, _row = font_level(_images, _len)
                    print('{:.3g}'.format(_i / 65536), end=' ')
                    _column = 0
                _draw.text((_column, _row), _char, font=_font)
            else:
                _width = size
                _width_i = _width + space
                if _column + _width_i > _len:
                    _row += _height_i
                    if _row + _height_i > _len:
                        _draw, _index, _row = font_level(_images, _len)
                    print('{:.3g}'.format(_i / 65536), end=' ')
                    _column = 0
            _record.append(
                (_index, _column / _len, _row / _len, _width // sampler))
            _column += _width_i

        _route = os.path.join(font_directory, name.rsplit('.')[0])

        _level = len(_images)
        _chunk = []

        with open('{}.{}.data'.format(_route, size), 'wb') as file:
            for _index in range(_level):
                _target = _images[_index].split()[-1]
                if sampler:
                    _target = _target.resize(
                        (bound, bound), PIL.Image.BICUBIC)
                if png:
                    _target.save('{}.{}.{}.png'.format(_route, size, _index))
                _compressed = zlib.compress(_target.tobytes())
                file.write(_compressed)
                _chunk.append(len(_compressed))

        _a, _d = PIL.ImageFont.FreeTypeFont(_absolute, size=size).getmetrics()

        _json = {'ascent': _a, 'descent': _d, 'size': size, 'bound': bound,
                 'level': _level, 'chunk': _chunk, 'data': _record}

        with open('{}.{}.json'.format(_route, size), 'w') as file:
            json.dump(_json, file)

except ModuleNotFoundError:
    font_builder = None


class ExtendFloats(Array):
    _EXTEND_STEP = 64

    def __init__(self):
        Array.__init__(self, self._EXTEND_STEP, Array.Float)

    def array_write(self, index, *elements):
        _test = index + len(elements)
        if _test >= self._array_nums:
            self.array_adjust(
                min(_test, self._array_nums + self._EXTEND_STEP))

        for _e in elements:
            self._array_data[index] = _e
            index += 1

        return index


class FontTypist:
    def __init__(self, name):
        _full_name = os.path.join(font_directory, name)

        with open(_full_name + '.json', 'r') as _stream:
            _json = json.load(_stream)

        self._font_ascent = _json['ascent']
        self._font_descent = _json['descent']
        self._font_metric = self._font_ascent + self._font_descent
        self._font_size = _json['size']
        self._font_bound = _json['bound']
        self._font_level = _json['level']
        self._font_chunk = _json['chunk']
        self._font_name = _full_name
        self._font_data = _json['data']
        self._font_axis = 1, 1

        self._font_program = 0
        self._font_camera = 0
        self._font_start = 0
        self._font_texture = 0
        self._font_vao = 0
        self._font_vbo = 0
        self._font_ibo = 0
        self._font_ebo = 0

        _coord_u = self._font_size / self._font_bound
        _coord_v = self._font_metric / self._font_bound

        self._font_buffer = (Float * 16)(
            0, - self._font_ascent, 0, 0,
            0, + self._font_descent, 0, _coord_v,
            self._font_size, self._font_descent, _coord_u, _coord_v,
            self._font_size, - self._font_ascent, _coord_u, 0)

        self._font_bytes = 0

    @property
    def font_height(self):
        return self._font_metric

    @property
    def font_width(self):
        return self._font_size

    def font_initial(self):
        _program = shader_program(
            GL_VERTEX_SHADER="""#version 330
                uniform mat4 gu_camera;
                uniform vec2 gu_start;
                in vec2 gu_position;
                in vec2 gu_uv;
                in vec3 gu_vertex;  // instance
                in vec3 gu_offset;  // instance
                in vec3 gu_color;  // instance
                out vec3 inner_uv;
                out vec4 inner_color;

                void main() {
                    float gu_ratio = gu_vertex.z;
                    gl_Position = gu_camera * vec4(
                        gu_vertex.x + gu_start.x + gu_position.x * gu_ratio,
                        gu_vertex.y + gu_start.y + gu_position.y,
                        0, 1);
                    inner_uv = vec3(
                        gu_offset.x + gu_uv.x * gu_ratio,
                        gu_offset.y + gu_uv.y,
                        gu_offset.z);
                    inner_color = vec4(gu_color, 1);
                }
            """,
            GL_FRAGMENT_SHADER="""#version 330
                uniform sampler2DArray gu_texture;
                in vec3 inner_uv;
                in vec4 inner_color;
                out vec4 out_color;

                void main() {
                    out_color = inner_color * texture(gu_texture, inner_uv);
                }
            """
        )

        _vao = UInt()
        glGenVertexArrays(1, _vao)
        glBindVertexArray(_vao)

        _vbo = UInt()
        glGenBuffers(1, _vbo)
        glBindBuffer(GL_ARRAY_BUFFER, _vbo)
        glBufferData(
            GL_ARRAY_BUFFER, 16 * 4, self._font_buffer, GL_STATIC_DRAW)

        _gu_position = glGetAttribLocation(_program, b'gu_position')
        glEnableVertexAttribArray(_gu_position)
        glVertexAttribPointer(_gu_position, 2, GL_FLOAT, GL_FALSE, 4 * 4, 0)

        _gu_uv = glGetAttribLocation(_program, b'gu_uv')
        glEnableVertexAttribArray(_gu_uv)
        glVertexAttribPointer(_gu_uv, 2, GL_FLOAT, GL_FALSE, 4 * 4, 2 * 4)

        _ibo = UInt()
        glGenBuffers(1, _ibo)
        glBindBuffer(GL_ARRAY_BUFFER, _ibo)

        _gu_vertex = glGetAttribLocation(_program, b'gu_vertex')
        glEnableVertexAttribArray(_gu_vertex)
        glVertexAttribPointer(_gu_vertex, 3, GL_FLOAT, GL_FALSE, 9 * 4, 0)
        glVertexAttribDivisor(_gu_vertex, 1)

        _gu_offset = glGetAttribLocation(_program, b'gu_offset')
        glEnableVertexAttribArray(_gu_offset)
        glVertexAttribPointer(_gu_offset, 3, GL_FLOAT, GL_FALSE, 9 * 4, 3 * 4)
        glVertexAttribDivisor(_gu_offset, 1)

        _gu_color = glGetAttribLocation(_program, b'gu_color')
        glEnableVertexAttribArray(_gu_color)
        glVertexAttribPointer(_gu_color, 3, GL_FLOAT, GL_FALSE, 9 * 4, 6 * 4)
        glVertexAttribDivisor(_gu_color, 1)

        _ebo = UInt()
        glGenBuffers(1, _ebo)
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, _ebo)
        _index = (UInt * 6)(0, 1, 2, 0, 2, 3)
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, 6 * 4, _index, GL_STATIC_DRAW)

        glBindVertexArray(0)
        glBindBuffer(GL_ARRAY_BUFFER, 0)
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, 0)

        _texture = UInt()
        glGenTextures(1, _texture)
        glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
        glBindTexture(GL_TEXTURE_2D_ARRAY, _texture)

        glTexParameteri(GL_TEXTURE_2D_ARRAY, GL_TEXTURE_SWIZZLE_R, GL_ONE)
        glTexParameteri(GL_TEXTURE_2D_ARRAY, GL_TEXTURE_SWIZZLE_G, GL_ONE)
        glTexParameteri(GL_TEXTURE_2D_ARRAY, GL_TEXTURE_SWIZZLE_B, GL_ONE)
        glTexParameteri(GL_TEXTURE_2D_ARRAY, GL_TEXTURE_SWIZZLE_A, GL_RED)
        glTexParameteri(
            GL_TEXTURE_2D_ARRAY, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        glTexParameteri(
            GL_TEXTURE_2D_ARRAY, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        glTexParameteri(GL_TEXTURE_2D_ARRAY, GL_TEXTURE_BASE_LEVEL, 0)
        glTexParameteri(
            GL_TEXTURE_2D_ARRAY, GL_TEXTURE_MAX_LEVEL, self._font_level - 1)

        glTexImage3D(GL_TEXTURE_2D_ARRAY, 0, GL_R8, self._font_bound,
                     self._font_bound, self._font_level, 0,
                     GL_RED, GL_UNSIGNED_BYTE, 0)

        with open(self._font_name + '.data', 'rb') as _stream:
            for _i in range(self._font_level):
                _image = zlib.decompress(_stream.read(self._font_chunk[_i]))
                glTexSubImage3D(
                    GL_TEXTURE_2D_ARRAY, 0, 0, 0, _i, self._font_bound,
                    self._font_bound, 1, GL_RED, GL_UNSIGNED_BYTE, _image)

        _gu_texture = glGetUniformLocation(_program, b'gu_texture')
        glProgramUniform1ui(_program, _gu_texture, _texture)
        glBindTexture(GL_TEXTURE_2D_ARRAY, 0)

        self._font_program = _program
        self._font_camera = glGetUniformLocation(_program, b'gu_camera')
        self._font_start = glGetUniformLocation(_program, b'gu_start')
        self._font_texture = _texture
        self._font_vao = _vao
        self._font_vbo = _vbo
        self._font_ibo = _ibo
        self._font_ebo = _ebo

    def font_final(self):
        glDeleteTextures(1, self._font_texture)

    def font_ortho(self):
        glProgramUniformMatrix4fv(
            self._font_program, self._font_camera, 1, 0, view.view_ortho)

    def font_change(self, name):
        pass

    def font_typeset(self, *text, size, spacing=(0, 0, 8), buffer=None):
        _width, _height = size
        _horizontal, _vertical, _paragraph = spacing
        _r, _g, _b = 0, 0, 0

        if not buffer:  # 扩展缓存容量
            buffer = ExtendFloats()

        _index = 0  # 开始排版，从上往下绘制，左上角为 0 0
        _offset_x = 0
        _offset_y = self._font_ascent
        for _segment in text:
            if isinstance(_segment, str):
                for _char in _segment:
                    _char = ord(_char)
                    _l, _u, _v, _w = self._font_data[_char]
                    if _offset_x + _w > _width:
                        _offset_x = 0
                        _offset_y += _vertical + self._font_metric
                        if _offset_y > _height:  # 越界的字体就不显示了
                            return buffer, _index // 9
                    _index = buffer.array_write(  # X Y S L U V R G B
                        _index,
                        _offset_x, _offset_y,  # 文字绘制的偏移量
                        _w / self._font_size,  # 文字宽度比例
                        _u, _v, _l, _r, _g, _b  # 贴图层级 UV 偏移量以及颜色
                    )
                    _offset_x += _w + _horizontal

            elif isinstance(_segment, tuple):
                _r, _g, _b = _segment

            elif _segment == 0:  # 换行
                _offset_x = 0
                _offset_y += _paragraph + self._font_metric

        return buffer, _index // 9

    def font_draw(self, buffer, count, offset, box):
        _off_x, _off_y = offset
        _left, _top, _right, _bottom = box
        view.view_scissor(_left, _top, _right, _bottom)

        glBindBuffer(GL_ARRAY_BUFFER, self._font_ibo)
        if self._font_bytes < buffer.array_size:
            self._font_bytes = buffer.array_size
            glBufferData(GL_ARRAY_BUFFER, self._font_bytes, 0, GL_STREAM_DRAW)
        glBufferSubData(GL_ARRAY_BUFFER, 0, buffer.array_size, buffer)

        glUseProgram(self._font_program)
        glUniform2f(self._font_start, _off_x + _left, _off_y + _top)

        glBindTexture(GL_TEXTURE_2D_ARRAY, self._font_texture)
        glBindVertexArray(self._font_vao)

        glDrawElementsInstanced(GL_TRIANGLES, 6, GL_UNSIGNED_INT, 0, count)

        glBindVertexArray(0)
        glBindTexture(GL_TEXTURE_2D_ARRAY, 0)
        glUseProgram(0)

        view.view_scissor_reset()

    def font_typeset_single_line(self, *text, spacing=0, buffer=None):
        _horizontal = spacing
        _r, _g, _b = 0, 0, 0

        if not buffer:  # 扩展缓存容量
            buffer = ExtendFloats()

        _index = 0  # 开始排版，从上往下绘制，左上角为 0 0
        _offset_x = 0
        _offset_y = self._font_ascent
        for _segment in text:
            if isinstance(_segment, str):
                for _char in _segment:
                    _char = ord(_char)
                    _l, _u, _v, _w = self._font_data[_char]
                    _index = buffer.array_write(  # X Y S L U V R G B
                        _index,
                        _offset_x, _offset_y,  # 文字绘制的偏移量
                        _w / self._font_size,  # 文字宽度比例
                        _u, _v, _l, _r, _g, _b  # 贴图层级 UV 偏移量以及颜色
                    )
                    _offset_x += _w + _horizontal

            elif isinstance(_segment, tuple):
                _r, _g, _b = _segment

        return buffer, _index // 9, _offset_x


typist = FontTypist('UniFont.16')

__all__ = ['typist', 'font_builder', 'font_directory']
