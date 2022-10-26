import collections
import os
import time

from .glfw_3 import *

from ..math3d import Ints, Floats
from ..opengl import *
from ..system import empty
from ..widget import view, root


class RateController:
    """ 用于控制帧刷新频率的类

    调用 rate_record 记录每帧的时间；
    可以自动计算间隔时间，并按照多次采样计算帧率；
    调用 rate_sleep 会按照设定好的帧率进行休眠调整。
    """

    def __init__(self):
        self._rate_record_size = 0
        self._rate_record_limit = 60
        self._rate_record_data = collections.deque()
        self._rate_time_current = 0  # 当前帧时间
        self._rate_time_interval = 0  # 间隔
        self._rate_swap_interval = 0
        self._rate_swap_compensate = 0

        self.rate_sleep = self._rate_sleep_pass
        self.rate_record = self._rate_record_expand

        self._rate_pressure_data = collections.deque()  # 压力统计
        self._rate_pressure_size = 0
        self._rate_pressure_limit = 5  # 默认 60 秒的统计
        self._rate_pressure_sampler = []  # 每秒的采样
        self._rate_pressure_analyse = self._rate_pressure_expand

    def _rate_record_expand(self):
        _current = time.perf_counter()
        _interval = _current - self._rate_time_current
        if int(_current) - int(self._rate_time_current):
            self._rate_pressure_analyse()
        self._rate_time_current = _current
        self._rate_time_interval = _interval

        self._rate_record_data.append(_interval)
        self._rate_record_size += 1
        if self._rate_record_size >= self._rate_record_limit:
            self.rate_record = self._rate_record_normal

    def _rate_record_normal(self):
        _current = time.perf_counter()
        _interval = _current - self._rate_time_current
        if int(_current) - int(self._rate_time_current):
            self._rate_pressure_analyse()
        self._rate_time_current = _current
        self._rate_time_interval = _interval

        self._rate_record_data.popleft()
        self._rate_record_data.append(_interval)

    @property
    def rate_sampler(self):
        """ 帧速率采样限制

        多次采样减少单帧的速度浮动，这里用于采样上限的确定
        """
        return self._rate_record_limit

    @rate_sampler.setter
    def rate_sampler(self, limit):
        if self._rate_record_size > limit:
            for _ in range(self._rate_record_size - limit):
                self._rate_record_data.popleft()
            self._rate_record_size = limit
            self.rate_record = self._rate_record_normal
        elif self._rate_record_limit < limit:
            self.rate_record = self._rate_record_expand

        self._rate_record_limit = limit

    @property
    def rate_average_fps(self):
        if self._rate_record_size:
            return str(round(
                self._rate_record_size / sum(self._rate_record_data)))
        elif self._rate_swap_interval:
            return str(round(1 // self._rate_swap_interval))
        else:
            return '0'

    @rate_average_fps.setter
    def rate_average_fps(self, fps):
        self._rate_swap_interval = 1 / fps
        self.rate_sleep = self._rate_sleep_active
        self.rate_sampler = fps  # 用 1 秒的时间进行重新采样

    def rate_frame_sync(self):
        """ 设置为帧同步 """

        self._rate_swap_interval = 0
        self.rate_sleep = self._rate_sleep_pass

    def _rate_sleep_active(self):
        # 用于测算需要沉睡的时间
        # 由于 python 的 sleep 唤醒并不准确，会误差 0.001 秒
        _wanted = (self._rate_swap_interval + self._rate_time_current -
                   self._rate_swap_compensate - 0.001)
        _sleep = _wanted - time.perf_counter()

        if _sleep > 0:
            time.sleep(_sleep)

        # 检测真实沉睡时间，并进行矫正
        _offset = time.perf_counter() - _wanted
        self._rate_pressure_per_frame(_sleep + _offset)
        self._rate_swap_compensate = _offset if _offset > 0 else 0

    def _rate_sleep_pass(self):
        # 因为无法完整测算时间间隔，所以采用上一次的间隔进行计算
        self._rate_pressure_per_frame(
            self._rate_time_interval + self._rate_time_current -
            time.perf_counter())

    @property
    def rate_last_interval(self):
        return self._rate_time_interval

    def _rate_pressure_per_frame(self, spare_time):
        self._rate_pressure_sampler.append(spare_time)

    def _rate_pressure_expand(self):
        if self._rate_pressure_sampler:
            _second_pressure = 100 - int(
                100 * sum(self._rate_pressure_sampler))
            if _second_pressure < 0:
                _second_pressure = 0
            self._rate_pressure_sampler.clear()
        else:
            _second_pressure = 0

        self._rate_pressure_data.append(_second_pressure)
        self._rate_pressure_size += 1
        if self._rate_pressure_size >= self._rate_pressure_limit:
            self._rate_pressure_analyse = self._rate_pressure_normal

    def _rate_pressure_normal(self):
        if self._rate_pressure_sampler:
            _second_pressure = 100 - int(
                100 * sum(self._rate_pressure_sampler))
            if _second_pressure < 0:
                _second_pressure = 0
            self._rate_pressure_sampler.clear()
        else:
            _second_pressure = 0

        self._rate_pressure_data.popleft()
        self._rate_pressure_data.append(_second_pressure)

    def rate_pressure(self):
        return self._rate_pressure_data

    @property
    def rate_pressure_duration(self):
        return self._rate_pressure_limit

    @rate_pressure_duration.setter
    def rate_pressure_duration(self, duration):
        if self._rate_pressure_size > duration:
            for _ in range(self._rate_pressure_size - duration):
                self._rate_pressure_data.popleft()
            self._rate_pressure_size = duration
            self._rate_pressure_analyse = self._rate_pressure_normal
        elif self._rate_pressure_limit < duration:
            self._rate_pressure_analyse = self._rate_pressure_expand

        self._rate_pressure_limit = duration


rate = RateController()


class WindowPrototype:
    def __init__(self, width=640, height=480, name='Gu'):
        self._window_size = width, height  # 窗口尺寸
        self._window_name = name.encode()  # 窗口名称
        self._window_sync = collections.deque()  # 同步序列
        self._window_glfw = None  # 窗口指针
        self._window_axis = 1, 1  # 窗口轴向放缩
        self._window_swap = 1  # 帧同步交换

    def __repr__(self):
        return 'Window'

    def __call__(self, *, width=None, height=None, name=None, fps=None):
        """ 一些窗口参数的调整 """

        if width:
            if height:
                self._window_size = width, height
            else:
                self._window_size = width, self._window_size[1]
            if self._window_glfw:
                glfwSetWindowSize(self._window_glfw, *self._window_size)
        elif height:
            self._window_size = self._window_size[0], height
            if self._window_glfw:
                glfwSetWindowSize(self._window_glfw, *self._window_size)

        if name:
            self._window_name = name.encode()
            if self._window_glfw:
                glfwSetWindowTitle(self._window_glfw, self._window_name)

        if fps is not None:
            if fps:
                rate.rate_average_fps = fps
                self._window_swap = 0
                if self._window_glfw:
                    glfwMakeContextCurrent(self._window_glfw)
                    glfwSwapInterval(0)
            else:
                rate.rate_frame_sync()
                self._window_swap = 1
                if self._window_glfw:
                    glfwMakeContextCurrent(self._window_glfw)
                    glfwSwapInterval(1)

    def _window_update(self):
        """ 窗口运行时进行的同步运算 """

        _size = len(self._window_sync)
        while _size:
            _size -= 1
            _func, *_args = self._window_sync.popleft()
            try:
                # 事件 WindowSize WindowPos ContentScale 存在阻塞延迟
                # 延迟会导致 _resize_inner 函数多次调用，只有最后一次才是有效操作
                # 因此 这里进行一次帧内筛除，尽量减少 _resize_inner 重复调用
                if _size and _func.__name__ == self._WINDOW_RESIZE_MASK:
                    _r_func, _r_args = _func, _args
                    while _size:
                        _size -= 1
                        _func, *_args = self._window_sync.popleft()
                        if _func.__name__ == self._WINDOW_RESIZE_MASK:
                            if _size:
                                _r_func, _r_args = _func, _args
                                continue
                            else:
                                _func(*_args)
                        else:
                            _r_func(*_r_args)
                            _func(*_args)
                else:
                    _func(*_args)

            except Exception as _e:
                print(_e)

    def _window_running(self):
        """ 窗口启动，隐藏以防止误调用 """

        # 需要持有到窗口运行结束避免被局部回收，回收会导致 glfw 回调空值
        _bind_function = self._window_function_wrap()

        _directory = os.getcwd()

        if glfwInit():
            os.chdir(_directory)  # glfwInit 会改变程序运行空间，这里改回来

            glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 3)
            glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 3)
            glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE)
            glfwWindowHint(GLFW_OPENGL_FORWARD_COMPATIBLE, GLFW_TRUE)
            glfwWindowHint(GLFW_SAMPLES, 1)

            self._window_glfw = _window = glfwCreateWindow(
                *self._window_size, self._window_name, None, None)

            if _window:
                for _bind, _function in _bind_function:  # 绑定回调函数
                    _bind(_window, _function)

                _size = Ints(data_nums=2)  # 重新测定窗口尺寸
                glfwGetWindowSize(_window, _size, _size.array_offset(1))
                _width, _height = self._window_size = tuple(_size)

                # 获取窗口与显卡缓存之间的放缩规则
                _scale = Floats(data_nums=2)
                glfwGetWindowContentScale(
                    _window, _scale, _scale.array_offset(1))

                _area = Ints(data_nums=4)  # 窗口居中
                glfwGetMonitorWorkArea(
                    glfwGetPrimaryMonitor(), _area, _area.array_offset(1),
                    _area.array_offset(2), _area.array_offset(3))
                _x_offset = _area[0] + (_area[2] - _width) // 2
                _y_offset = _area[1] + (_area[3] - _height) // 2
                glfwSetWindowPos(_window, _x_offset, _y_offset)

                glfwMakeContextCurrent(_window)  # 需要 make current 才生效
                view.view_initial(_scale, _width, _height)
                self._window_initial()
                glfwSwapInterval(self._window_swap)

                while not glfwWindowShouldClose(_window):
                    rate.rate_record()
                    glfwPollEvents()
                    glfwMakeContextCurrent(_window)
                    self._window_update()
                    self._window_render()
                    rate.rate_sleep()
                    glfwSwapBuffers(_window)

                self._window_final()

            glfwTerminate()

    def _window_initial(self):
        """ 绑定显存 """

        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

        self.window_initial()
        root.root_initial()

    def _window_render(self):
        """ 显存渲染 """

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        self.window_render()
        root.root_render()

    def _window_final(self):
        """ 回收显存 """

        self.window_final()
        root.root_final()

    def _window_resize_sync(self, width, height):
        self._window_size = width, height
        glfwMakeContextCurrent(self._window_glfw)
        view.view_resize(width, height)
        root.root_resize()
        self.window_resize(width, height)

    _WINDOW_RESIZE_MASK = _window_resize_sync.__name__

    # 提供给用户修改的函数
    window_initial = empty  # 初始化 ()
    window_render = empty  # 帧渲染 (interval)
    window_final = empty  # 回收销毁 ()
    window_key = empty  # 键盘输入 (key, scancode, action, mods)
    window_mouse = empty  # 鼠标移动 (x_offset, y_offset)
    window_button = empty  # 鼠标按钮 (index, press, mods)
    window_resize = empty  # 窗口尺寸 (width, height)
    window_char = empty  # 字符输入 (char)
    window_scroll = empty  # 鼠标滚动 (x_offset, y_offset)

    def _window_function_wrap(self):
        """ 绑定窗口与 glfw 之间的回调，应该尽量实现 """

        def _key_wrap(_, key, scancode, press, mods):
            # glfwMakeContextCurrent(glfw_window)
            self.window_key(key, scancode, press, mods)

        def _mouse_wrap(_, x_offset, y_offset):
            # glfwMakeContextCurrent(glfw_window)
            root.root_hover(x_offset, y_offset)
            self.window_mouse(x_offset, y_offset)

        def _resize_wrap(_, width, height):
            # glfwMakeContextCurrent(glfw_window)
            self._window_sync.append(
                (self._window_resize_sync, width, height))

        def _button_wrap(_, index, press, mods):
            # glfwMakeContextCurrent(glfw_window)
            self.window_button(index, press, mods)

        def _char_wrap(_, char):
            # glfwMakeContextCurrent(glfw_window)
            self.window_char(char)

        def _scroll_wrap(_, x_offset, y_offset):
            # glfwMakeContextCurrent(glfw_window)
            self.window_scroll(x_offset, y_offset)

        def _max_wrap(_, mask):
            print(self._window_size)
            # glfwGetWindowFrameSize()

        return (
            (glfwSetKeyCallback, GLFWKeyFun(_key_wrap)),
            (glfwSetCursorPosCallback, GLFWCursorPosFun(_mouse_wrap)),
            (glfwSetWindowSizeCallback, GLFWWindowSizeFun(_resize_wrap)),
            (glfwSetMouseButtonCallback, GLFWMouseButtonFun(_button_wrap)),
            (glfwSetCharCallback, GLFWCharFun(_char_wrap)),
            (glfwSetScrollCallback, GLFWScrollFun(_scroll_wrap)),
            (glfwSetWindowMaximizeCallback, GLFWWindowMaximizeFun(_max_wrap)),
        )


substitute = (
    'window_initial', 'window_render', 'window_final', 'window_key',
    'window_mouse', 'window_button', 'window_resize', 'window_char',
    'window_scroll')

window = WindowPrototype()

__all__ = ['rate', 'substitute', 'window']
