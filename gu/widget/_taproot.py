from ._viewport import view
from ._typist import typist

from ..opengl import *
from ..system import empty


class WidgetRoot:
    def __init__(self):
        self._root_plugin = []
        self._root_member = {}
        self._root_visual = []
        self._root_effect = False

        self.root_update = empty

        self._root_static_program = 0
        self._root_static_vao = 0
        self._root_static_vbo = 0
        self._root_static_ebo = 0
        self._root_static_fbo = 0
        self._root_static_texture = 0

        self._root_hovered = None  # 鼠标经过位置的组件

        self._root_selected = None  # 鼠标选取的组件

    # ---------------------------------------------------------------------
    # 打印输出

    def __repr__(self):
        return 'Root'

    def __str__(self):
        return 'Root({})'.format(
            ' '.join(str(_w) for _w in self._root_member.values()))

    # ---------------------------------------------------------------------
    # 查找创建的组件

    def __setitem__(self, key, value):
        self._root_member[key] = value

    def __getitem__(self, item):
        return self._root_member[item]

    def root_find(self, item):
        _route = item.split('.')
        _length = len(_route)
        _target = self
        if _length:
            for _i in range(_length):
                _target = _target[_route[_i]]
        return _target

    # ---------------------------------------------------------------------
    # 注册组件类型

    def root_register(self, widget_type):
        if self._root_effect:
            widget_type.widget_initial()
        self._root_plugin.append(widget_type)

    def root_meta(self, name, base, param):
        _widget_type = type(name, base, param)
        self.root_register(_widget_type)
        return _widget_type

    # ---------------------------------------------------------------------
    # 静态区域更新与绘制

    def _root_static_initial(self):
        _program = shader_program(
            GL_VERTEX_SHADER="""#version 330
                in vec2 gu_position;
                in vec2 gu_uv;
                out vec2 inner_uv;

                void main() {
                    inner_uv = gu_uv;
                    gl_Position = vec4(gu_position, 0, 1);
                }
            """,
            GL_FRAGMENT_SHADER="""#version 330
                uniform sampler2D gu_texture;
                in vec2 inner_uv;
                out vec4 frag_color;

                void main() {
                    frag_color = texture(gu_texture, inner_uv.st);

                    // 静态绘制因为离屏缘故，透明效果有偏差，故无法实现透明效果
                    if (frag_color.a > 0) frag_color.a = 1;
                }
            """)
        _position = (Float * 16)(
            -1, 1, 0, 1, -1, -1, 0, 0, 1, -1, 1, 0, 1, 1, 1, 1)
        _index = (UInt * 6)(0, 1, 2, 0, 2, 3)

        _vao = UInt()
        glGenVertexArrays(1, _vao)
        glBindVertexArray(_vao)

        _vbo = UInt()
        glGenBuffers(1, _vbo)
        glBindBuffer(GL_ARRAY_BUFFER, _vbo)
        glBufferData(GL_ARRAY_BUFFER, 16 * 4, _position, GL_STATIC_DRAW)

        _gu_position = glGetAttribLocation(_program, b'gu_position')
        _gu_uv = glGetAttribLocation(_program, b'gu_uv')
        glEnableVertexAttribArray(_gu_position)
        glVertexAttribPointer(_gu_position, 2, GL_FLOAT, GL_FALSE, 4 * 4, 0)
        glEnableVertexAttribArray(_gu_uv)
        glVertexAttribPointer(_gu_uv, 2, GL_FLOAT, GL_FALSE, 4 * 4, 2 * 4)

        _ebo = UInt()
        glGenBuffers(1, _ebo)
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, _ebo)
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, 6 * 4, _index, GL_STATIC_DRAW)

        glBindVertexArray(0)
        glBindBuffer(GL_ARRAY_BUFFER, 0)
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, 0)

        _fbo = UInt()
        glGenFramebuffers(1, _fbo)

        _texture = UInt()
        glGenTextures(1, _texture)
        glBindTexture(GL_TEXTURE_2D, _texture)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)

        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, view.view_width,
                     view.view_height, 0, GL_RGBA, GL_UNSIGNED_BYTE, 0)

        glBindFramebuffer(GL_FRAMEBUFFER, _fbo)
        glFramebufferTexture2D(GL_FRAMEBUFFER, GL_COLOR_ATTACHMENT0,
                               GL_TEXTURE_2D, _texture, 0)

        assert (GL_FRAMEBUFFER_COMPLETE ==
                glCheckFramebufferStatus(GL_DRAW_FRAMEBUFFER))

        _gu_texture = glGetUniformLocation(_program, b'gu_texture')
        glProgramUniform1ui(_program, _gu_texture, _texture)

        self._root_static_program = _program
        self._root_static_vao = _vao
        self._root_static_vbo = _vbo
        self._root_static_ebo = _ebo
        self._root_static_fbo = _fbo
        self._root_static_texture = _texture

    def _root_static_final(self):
        glDeleteProgram(self._root_static_program)
        glDeleteVertexArrays(1, self._root_static_vao)
        glDeleteBuffers(1, self._root_static_vbo)
        glDeleteBuffers(1, self._root_static_ebo)
        glDeleteFramebuffers(1, self._root_static_fbo)
        glDeleteTextures(1, self._root_static_texture)

    def _root_static_resize(self):
        glBindTexture(GL_TEXTURE_2D, self._root_static_texture)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, view.view_width,
                     view.view_height, 0, GL_RGBA, GL_UNSIGNED_BYTE, 0)
        self._root_static_update()

    def _root_static_update(self):
        # """ 这是调用组件绘制的函数，这里需要配置管线状态 """
        glBindFramebuffer(GL_FRAMEBUFFER, self._root_static_fbo)
        glClear(GL_COLOR_BUFFER_BIT)
        view.view_state_enable()
        for _widget in self._root_member.values():
            _widget.widget_update_iterator()
        view.view_state_disable()
        glBindFramebuffer(GL_FRAMEBUFFER, 0)

    def _root_static_render(self):
        glUseProgram(self._root_static_program)
        glBindTexture(GL_TEXTURE_2D, self._root_static_texture)
        glBindVertexArray(self._root_static_vao)

        glDrawElements(GL_TRIANGLES, 6, GL_UNSIGNED_INT, 0)

        glBindVertexArray(0)
        glBindTexture(GL_TEXTURE_2D, 0)
        glUseProgram(0)

    # ---------------------------------------------------------------------
    # 修改默认字体

    # def root_font(self, name):
    #     typist.font_change(name)
    #     self._widget_root_font_height = font_system.font_height
    #     if self.widget_root_update == self._widget_root_static_update:
    #         self._widget_root_static_resize()

    # ---------------------------------------------------------------------
    # 与窗口绑定的函数

    def root_initial(self):
        self._root_effect = True
        self.root_update = self._root_static_update

        for _type in self._root_plugin:
            _type.widget_initial()
            _type.widget_ortho()

        for _widget in self._root_member.values():
            _widget.widget_resize_iterator()

        typist.font_initial()
        typist.font_ortho()

        self._root_static_initial()
        self._root_static_update()

    def root_final(self):
        for _widget_type in self._root_plugin:
            _widget_type.widget_final()

        typist.font_final()
        self._root_effect = False
        self._root_static_final()
        self.root_update = empty

    def root_resize(self):
        typist.font_ortho()
        for _type in self._root_plugin:
            _type.widget_ortho()
        for _widget in self._root_member.values():
            _widget.widget_resize_iterator()
        self._root_static_resize()

    def root_render(self):
        # """ 这是调用组件绘制的函数，这里需要配置管线状态 """
        view.view_state_enable()
        self._root_static_render()
        for _widget in self._root_member.values():
            _widget.widget_render_iterator()
        view.view_state_disable()

    def root_hover(self, x_offset, y_offset):
        """ 鼠标悬停的位置，以悬停位置切换激活的组件 """

        for _child in self._root_visual:
            _hover = _child.widget_select_test(x_offset, y_offset)
            if _hover:
                if self._root_hovered != _hover:  # 前后组件不一样
                    if self._root_hovered:  # 脱离前组件
                        self._root_hovered.widget_hover_out()
                    _hover.widget_hover_in()  # 进入后组件
                    self._root_hovered = _hover
                return

        if self._root_hovered:
            self._root_hovered.widget_hover_out()
            self._root_hovered = None

    def root_pick_or_drop(self):
        """ 鼠标选取，或者释放 """

        if self._root_selected:
            pass


root = WidgetRoot()


class Widget:
    def __repr__(self):
        if self._widget_children:
            return '{}({})'.format(self._widget_name, ' '.join(
                str(_w) for _w in self._widget_children.values()))
        else:
            return '{}'.format(self._widget_name)

    def __init__(self, name, relate, offset, size, anchor, border, visual):
        if not name and name in root:
            raise NameError

        _route = name.split('.')
        _length = len(_route) - 1
        _parent = root
        if _length:
            for _i in range(_length):
                _parent = _parent[_route[_i]]
            self._widget_parent = _parent
            name = _route[-1]
            _parent[name] = self

        else:
            self._widget_parent = None
            root[name] = self

        self._widget_children = {}
        self._widget_visual = []

        self._widget_relate = relate
        self._widget_offset = offset
        self._widget_size = size
        self._widget_anchor = anchor
        self._widget_border = border

        self._widget_position = 0, 0
        self._widget_outline = 0, 0, 0, 0
        self._widget_box = 0, 0, 0, 0

        self._widget_name = name

        visual and self.widget_switch()

    def __setitem__(self, key, value):
        self._widget_children[key] = value

    def __getitem__(self, item):
        return self._widget_children[item]

    @classmethod
    def widget_initial(cls):
        """ 绑定显存 """

    @classmethod
    def widget_final(cls):
        """ 回收显存 """

    @classmethod
    def widget_ortho(cls):
        """ 改变窗口 """

    def widget_resize(self):
        """ 更新属性 """

        if self._widget_parent:
            _f = self._widget_parent.widget_draft
        else:
            _f = view.view_draft_area
        (self._widget_position, self._widget_outline, self._widget_box) = _f(
            self._widget_relate, self._widget_offset, self._widget_size,
            self._widget_anchor, self._widget_border)

    def widget_update(self):
        """ 静态绘制 """

    def widget_render(self):
        """ 动态绘制 """

    def widget_resize_iterator(self):
        self.widget_resize()
        for _child in self._widget_children.values():
            _child.widget_resize_iterator()

    def widget_update_iterator(self):
        self.widget_update()
        for _child in self._widget_children.values():
            _child.widget_update_iterator()

    def widget_render_iterator(self):
        self.widget_render()
        for _child in self._widget_children.values():
            _child.widget_render_iterator()

    def widget_switch(self):
        if self._widget_parent:
            _target = self._widget_parent._widget_visual
        else:
            _target = root._root_visual

        if self in _target:
            _target.remove(self)
        else:
            _target.append(self)

        root.root_update()

    def widget_draft(self, relate, offset, size, anchor, border):
        """ 通过输入下级 widget 属性，来产生该 widget 的区域属性 """
        _r_x, _r_y = relate
        _o_x, _o_y = offset
        _s_x, _s_y = size
        _a_x, _a_y = anchor

        _p_left, _p_top, _p_right, _p_bottom = self._widget_box

        _a0 = ((_p_right - _p_left) * (1 + _r_x) -
               _s_x * (1 + _a_x)) // 2 + _p_left + _o_x
        _a1 = ((_p_bottom - _p_top) * (1 - _r_y) -
               _s_y * (1 - _a_y)) // 2 + _p_top + _o_y

        _b_left, _b_top, _b_right, _b_bottom = self._widget_outline

        _b0 = max(_a0, _b_left)
        _b1 = max(_a1, _b_top)
        _b2 = min(_a0 + _s_x, _b_right)
        _b3 = min(_a1 + _s_y, _b_bottom)

        _c_left, _c_top, _c_right, _c_bottom = border

        _c0 = _a0 + _c_left
        _c1 = _a1 + _c_top
        _c2 = _a0 + _s_x - _c_right
        _c3 = _a1 + _s_y - _c_bottom

        return (_a0, _a1), (_b0, _b1, _b2, _b3),  (_c0, _c1, _c2, _c3)

    def widget_select_test(self, x, y):
        _x0, _y0, _x1, _y1 = self._widget_outline
        if _x0 > x or x > _x1 or _y0 > y or y > _y1:
            return None

        for _child in self._widget_visual:
            _result = _child.widget_select_test(x, y)
            if _result:
                return _result

        return self

    def widget_hover_in(self):
        """ 鼠标进入 """
        print(self)

    def widget_hover_out(self):
        """ 鼠标移出 """
        print(self)


__all__ = ['root', 'Widget']
