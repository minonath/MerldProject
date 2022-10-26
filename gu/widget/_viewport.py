from ..math3d import Ints, Floats
from ..opengl import (
    glGetIntegerv, GL_VIEWPORT, glViewport, glScissor, GL_SCISSOR_TEST, Int,
    glEnable, glDisable, GL_SCISSOR_BOX, GL_DEPTH_TEST, glDepthMask,
    GL_COLOR_CLEAR_VALUE, glClearColor
)


class Viewport:
    def __init__(self):
        self._view_array = Ints(data_nums=4)
        self._view_scale = 0, 0
        self._view_ortho = Floats(data_nums=16)

        self._view_scissor_box = Ints(data_nums=4)
        self._view_scissor_test = Int()
        self._view_depth_test = Int()

    def view_initial(self, scale, width, height):
        glGetIntegerv(GL_VIEWPORT, self._view_array)
        self._view_scale = int(scale[0]), int(scale[1])
        self._view_ortho_update(width, height)

    def view_resize(self, width, height):
        _axis_x, _axis_y = self._view_scale
        glViewport(0, 0, width * _axis_x, height * _axis_y)
        glGetIntegerv(GL_VIEWPORT, self._view_array)
        glGetIntegerv(GL_SCISSOR_TEST, self._view_scissor_test)
        if self._view_scissor_test.value:
            glScissor(*self._view_array)

        self._view_ortho_update(width, height)

    def _view_ortho_update(self, width, height):
        self._view_ortho(2 / width, 0, 0, 0, 0, -2 / height, 0,
                         0, 0, 0, -1, 0, -1, 1, 0, 1)

    @property
    def view_width(self):
        return self._view_array[2]

    @property
    def view_height(self):
        return self._view_array[3]

    @property
    def view_ortho(self):
        return self._view_ortho

    def view_state_enable(self):
        glGetIntegerv(GL_SCISSOR_TEST, self._view_scissor_test)
        if self._view_scissor_test.value:
            glGetIntegerv(GL_SCISSOR_BOX, self._view_scissor_box)
        else:
            glEnable(GL_SCISSOR_TEST)
        glScissor(*self._view_array)

        glGetIntegerv(GL_DEPTH_TEST, self._view_depth_test)
        if self._view_depth_test.value:
            glDepthMask(False)

    def view_state_disable(self):
        if self._view_scissor_test.value:
            glScissor(*self._view_scissor_box)
        else:
            glDisable(GL_SCISSOR_TEST)

        if self._view_depth_test.value:
            glDepthMask(True)

    def view_scissor(self, left, top, right, bottom):
        _axis_x, _axis_y = self._view_scale
        glScissor(
            left * _axis_x, self._view_array[3] - bottom * _axis_y,
            (right - left) * _axis_x, (bottom - top) * _axis_y)

    def view_scissor_reset(self):
        glScissor(*self._view_array)

    def view_draft_area(self, relate, offset, size, anchor, border):
        """ 通过传入组件参数，来确定组件在窗口上的绘制区域

        参数：
            - relate 相对于窗口的位置，可计算出传动点
            - offset 相对于传动点的偏移
            - size 组件的尺寸
            - anchor 组件自身的锚点
            - border 组件的边框大小
        返回：
            返回组件的坐标，组件的绘制边框，组件的继承区域
        """

        _r_x, _r_y = relate
        _o_x, _o_y = offset
        _s_x, _s_y = size
        _a_x, _a_y = anchor

        _p_width, _p_height = (self._view_array[2] // self._view_scale[0],
                               self._view_array[3] // self._view_scale[1])

        _a0 = (_p_width * (1 + _r_x) - _s_x * (1 + _a_x)) // 2 + _o_x
        _a1 = (_p_height * (1 - _r_y) - _s_y * (1 - _a_y)) // 2 + _o_y

        _b0 = max(_a0, 0)
        _b1 = max(_a1, 0)
        _b2 = min(_a0 + _s_x, _p_width)
        _b3 = min(_a1 + _s_y, _p_height)

        _c_left, _c_top, _c_right, _c_bottom = border

        _c0 = _a0 + _c_left
        _c1 = _a1 + _c_top
        _c2 = _a0 + _s_x - _c_right
        _c3 = _a1 + _s_y - _c_bottom

        return (_a0, _a1), (_b0, _b1, _b2, _b3), (_c0, _c1, _c2, _c3)


view = Viewport()

__all__ = ['view']
