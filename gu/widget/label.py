from ._taproot import root, Widget
from ._typist import typist


class StaticLabel(Widget, metaclass=root.root_meta):
    """ 一个静态文本 """

    def __init__(
            self, name=None, text='', text_anchor=0, text_spacing=0,
            relate=(0, 0), offset=(0, 0), width=128, anchor=(0, 0),
            border=(0, 0, 0, 0), visual=True):

        self._label_width = width
        self._label_spacing = 0, 0, 8
        (self._label_buffer, self._label_count, _label_length
         ) = typist.font_typeset_single_line(*text, spacing=text_spacing)

        Widget.__init__(
            self, name, relate, offset,
            (width + border[0] + border[1],
             typist.font_height + border[2] + border[3]),
            anchor, border, visual)

        self._label_start = (
            (width - _label_length) * (1 + text_anchor) // 2, 0)

    def widget_update(self):
        typist.font_draw(self._label_buffer, self._label_count,
                         self._label_start, self._widget_box)


class DynamicLabel(Widget, metaclass=root.root_meta):
    def __init__(
            self, name=None, text='', text_anchor=0, text_spacing=0,
            relate=(0, 0), offset=(0, 0), width=128, anchor=(0, 0),
            border=(0, 0, 0, 0), visual=True):

        self._label_width = width
        self._label_anchor = text_anchor
        self._label_spacing = text_spacing
        (self._label_buffer, self._label_count, _label_length
         ) = typist.font_typeset_single_line(*text, spacing=text_spacing)

        Widget.__init__(
            self, name, relate, offset,
            (width + border[0] + border[1],
             typist.font_height + border[2] + border[3]),
            anchor, border, visual)

        self._label_start = (
            (width - _label_length) * (1 + text_anchor) // 2, 0)

    def widget_render(self):
        typist.font_draw(self._label_buffer, self._label_count,
                         self._label_start, self._widget_box)

    def label_text(self, *text, anchor=None, spacing=None):
        if anchor is not None:
            self._label_anchor = anchor

        if spacing is not None:
            self._label_spacing = spacing

        (self._label_buffer, self._label_count, _label_length
         ) = typist.font_typeset_single_line(
            *text, spacing=self._label_spacing)

        self._label_start = (
            (self._label_width - _label_length) *
            (1 + self._label_anchor) // 2, 0)
