from gu import gu

from gu.window import rate, window
from gu.widget import root, Widget, typist, font_builder
from gu.widget.panel import ColoredPanel
from gu.widget.label import StaticLabel, DynamicLabel
from gu.opengl import *


window(fps=30)


class Palette(Widget, metaclass=root.root_meta):
    pass


root.root_register(ColoredPanel)


ColoredPanel('test', size=(400, 400), border=(40, 40, 10, 40))
ColoredPanel('test.close', relate=(1, 1), anchor=(-1, -1), size=(24, 24), color=(1, 1, 1))


for x in range(0, 350, 10):
    for y in range(0, 350, 10):
        ColoredPanel('test.'+str(x)+str(y), offset=(x, y),
                     relate=(-1, 1), anchor=(-1, 1), size=(9, 9), color=(x / 360, y/ 360, 1))

StaticLabel('test.other',
            text=('请问i饿不放弃俄两份轻薄', (1, 0, 0), '多', (0, 0, 0), '长',
            '12345'), relate=(-1, -1), anchor=(-1, -1), width=100)

DynamicLabel('other',
            text=('测试一下这个有', (1, 0, 0), '多', (0, 0, 0), '长',
            '12345'),
            relate=(-1, -1), anchor=(-1, -1), width=400)

StaticLabel('mi',
            text=('测试一下这个有', (1, 0, 0), '多', (0, 0, 0), '长',
            '12345'),
            relate=(-1, -1), offset=(0, -27), anchor=(-1, -1), width=400)


m = DynamicLabel('test.fps', relate=(-1, 0), anchor=(-1, -1), width=300)


def window_initial():
    glClearColor(0.85, 0.85, 0.85, 0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)


def window_render():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    m.label_text(rate.rate_average_fps + '  ' + str(rate.rate_pressure()))


# font_builder('SourceHan.otf', 16, sampler=4)
# font_builder('UniFont.ttf', 16)
