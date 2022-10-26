from .system import empty, resource
from .widget import root
from .window import substitute, window


class Gu:
    def __init__(self):
        self.resource = resource
        self.window = window
        self.root = root

    def __repr__(self):
        return 'Gu'

    def __str__(self):
        return str(self.__dict__)

    def __call__(self, *args):
        resource.resource_load(*args)

        _global = {}
        try:
            exec(resource.resource_read('__main__.py'), _global)
        except Exception as _e:
            print(_e)

        for _func in substitute:
            setattr(self.window, _func, _global.get(_func, empty))

        if _global.get('gu') != self:
            _global['gu'] = self

        exec('gu.window._window_running()', _global)
        return self


gu = Gu()

__all__ = ['gu']
