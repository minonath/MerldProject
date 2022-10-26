"""
Gu OpenGL Wrap 2021-05-04

从官网下载头文件并进行 python 绑定
https://github.com/KhronosGroup/OpenGL-Registry
https://github.com/KhronosGroup/OpenGL-Registry/raw/master/api/GL/glcorearb.h
"""
import ctypes
import os
import platform
import re
import ssl
import urllib.error
import urllib.request

from ..system import dynamic

system = platform.system()

dir_name, base_name = os.path.split(__file__)

library = os.path.join(dir_name, '_library')

download = os.path.join(dir_name, '_gl_core_arb.h')  # 根据下载文件来改变

git_url = 'https://github.com/KhronosGroup/OpenGL-Registry/' \
          'raw/master/api/GL/gl''core''arb.h'

mirror_url = 'https://gitee.com/mirrors_KhronosGroup/OpenGL-Registry/' \
             'raw/master/api/GL/gl''core''arb.h'


def wrapper():
    """ 绑定头文件 """

    _name = _file = None

    if not os.path.exists(library):
        os.mkdir(library)

    for _line in wrapper_data().splitlines():
        if _line.startswith('#ifndef GL_'):  # 分割文件
            _name, _file = wrapper_create_file(_line, _name, _file)

        elif _line.startswith('#define GL_'):  # 常数
            _sign, _line = wrapper_constant(_line)
            _file.write(_line)
            ext_name.append(_sign)

        elif _line.startswith('typedef'):  # 自定义类型以及回调函数
            if _line.endswith(')'):
                _sign, _line = wrapper_callback(_line)
                _file.write(wrapper_pep8(_line))
                ext_name.append(_sign)

        elif _line.startswith('GL''API'):  # 接口函数
            _sign, _line = wrapper_external(_line)
            _file.write(wrapper_pep8(_line))
            ext_name.append(_sign)

    if ext_name:
        _file.write('\n')
        _file.write(wrapper_pep8(
            "__all__ = ['%s']" % ("', '".join(ext_name))))
        _file.close()

    if _file:
        _file.close()

    wrapper_init()


def wrapper_data():
    """ 从目标文件中获取需要的代码，如果目标不存在，则从网络上下载；再进行一些处理 """

    if os.path.exists(download):
        with open(download, 'r') as _download:
            _data = _download.read()
    else:
        _context = ssl.create_default_context()
        _context.check_hostname = False
        _context.verify_mode = ssl.CERT_NONE

        try:
            _raw = urllib.request.urlopen(git_url, context=_context)

        except urllib.error.URLError:  # 尝试下载，国内网络不怎么行，用镜像吧
            _raw = urllib.request.urlopen(mirror_url, context=_context)

        _data = _raw.read().decode()

        with open(download, 'w') as _download:
            _download.write(_data)

    _data = re.sub(r'/\*[\s\S]*?\*/', '', _data)  # 删除多行注释

    # 星号、括号、逗号前后分开
    _data = _data.replace('(', ' ( ').replace(')', ' ) ').replace(',', ' , ')
    _data = _data.replace('*', ' * ').replace(';', '')  # 去掉分号

    _data = re.sub(r' +', ' ', _data)  # 多个空格合并成一个空格
    _data = _data.replace(' \n', '\n')  # 行末尾的空格也去掉

    return _data


def wrapper_constant(line):
    """ 提取常量行 """

    _, _name, _value = line.split(' ')
    _value = _value.rstrip('ul')  # u 和 l 结尾的数字

    return _name, '{0} = {1}\n'.format(_name, _value)


# re.compile(r'//[\s\S]*?\n')  # 删除单行注释
in_brackets = re.compile(r'\([\s\S]*?\)')  # 括号内的内容


def wrapper_callback(line):
    """ 提取回调函数，括号结尾的是回调函数 """

    _param = [wrapper_type(line[8: line.find('(') - 1])]  # 第 8 个字符开始
    _name_segment, _param_segment = in_brackets.findall(line)

    _name = _name_segment.split(' ')[-2]  # 倒数第二个是回调函数的名称

    if _param_segment == '( void )':  # 注意 void
        return _name, '{0} = C({1})'.format(_name, _param[0])

    for _segment in _param_segment.strip('()').split(','):
        _param.append(wrapper_type(_segment[:_segment.rfind(' ', None, -1)]))

    return _name, '{0} = C({1})'.format(_name, ', '.join(_param))


def wrapper_external(line):
    """ 提取接口函数 """

    line = line.replace('GL''API ', '').replace('API''ENTRY ', '')

    _split = line.find('(')
    _prev = line[:_split - 1]
    _last = line[_split + 1:-1]

    _split = _prev.rfind(' ')
    _return = wrapper_type(_prev[:_split])
    _name = _prev[_split + 1:]

    if _last == ' void ':
        return _name, "{0} = GL('{0}', {1})".format(_name, _return)

    _param = ', '.join(
        wrapper_type(_segment[:_segment.rfind(' ', None, -1)])
        for _segment in _last.split(',')
    )

    return _name, "{0} = GL('{0}', {1}, {2})".format(_name, _return, _param)


short_name = {
    'GL''enum': 'UInt',
    'GL''boolean': 'UByte',
    'GL''bitfield': 'UInt',
    'GL''byte': 'Byte',
    'GLint': 'Int',
    'GL''size''i': 'Int',
    'GLu''byte': 'UByte',
    'GLu''short': 'UShort',
    'GLu''int': 'UInt',
    'GL''float': 'Float',
    'GL''clamp''f': 'Float',
    'GL''clamp''d': 'Double',
    'GL''void': 'None',
    'void': 'None',
    'GL''double': 'Double',
    'GL''short': 'Short',
    'GL''sync': 'GLSyncP',
    'GL''size''i''ptr': 'Size',
    'GL''int''ptr': 'Size',
    'GL''char': 'Char',
    'GLu''int64': 'ULong',
    'GLint64': 'Long',
    '_cl_context': 'None',  # 不怎么使用的结构
    '_cl_event': 'None',
    'GLu''int64EXT': 'ULong',
    'GL''handleARB': 'Handle',
    'GL''charARB': 'Char',
    'GL''size''i''ptrARB': 'Size',
    'GL''int''ptrARB': 'Size',
    'GL''fixed': 'Int',
    'GL''int64EXT': 'Long',
    'GL''eglImageOES': 'VoidP',
    'GL''eglClientBufferEXT': 'VoidP',
    'GL''halfNV': 'UShort',
    'GL''vd''pauSurfaceNV': 'Size',  # Video Decode & Presentation API 4 Unix
}


def wrapper_type(type_segment):  # 转换为 python 类型，不考虑 signed unsigned
    _count = 0

    type_segment = type_segment.strip(' ')

    if ' ' in type_segment:
        # 先排除一些特殊关键字，不考虑结构以及静态标记
        _type = type_segment.replace('str''uct ', '').replace('const ', '')

        if ' ' in _type:
            _type, *_asterisk = _type.split(' ')  # 后面的都是 * 号咯
            _count = len(_asterisk)

    else:
        _type = type_segment

    _type = short_name.get(_type, _type)  # 不用在意特殊类型

    for _ in range(_count):
        if _type == 'None':
            _type = 'VoidP'
        elif _type == 'Char':
            _type = 'CharP'
        else:
            _type = 'P(%s)' % _type

    return _type


# 传递文件名称
import_head = 'from ..%s import *\n\n' % os.path.splitext(base_name)[0]

mod_name = []
ext_name = []


def wrapper_create_file(line, name, file):
    _sign = line.split(' ')[1]
    if _sign.startswith('GL_VERSION'):
        _new_name = '_GL_{2}{3}'.format(*_sign.split('_'))

    else:
        _new_name = '_{0}_{1}'.format(*_sign.split('_'))

    if name == _new_name:
        return name, file

    if name:
        file.write('\n')
        file.write(wrapper_pep8("__all__ = ['%s']" % ("', '".join(ext_name))))
        file.close()
        ext_name.clear()

    mod_name.append(_new_name)
    file = open(os.path.join(library, _new_name + '.py'), 'w')
    file.write(import_head)
    return _new_name, file


def wrapper_init():
    with open(os.path.join(library, '__init__.py'), 'w') as _file:
        for _mode_name in mod_name:
            _file.write('from .%s import *\n' % _mode_name)

        _file.write('\n\nclass OpenGLError(Exception):\n    ...\n')
        _file.write('\n\ndef gl_get(name):\n    return globals().get(name)\n')


def wrapper_pep8(single_line):
    """ 简易的 PEP8 风格 """

    if len(single_line) < 79:
        return single_line + '\n'

    _result = []
    _last_line = single_line[-1:] + '\n'  # 最末尾是一个括号，加上换行符
    _handle_line = single_line[:-1]  # 剩余未处理行
    _first_line = _handle_line[:78]
    _k = _first_line.find('(') + 1  # 取得一个括号
    if _k == 0:
        _k = _first_line.find('[') + 1

    _result.append(_first_line[:_k])  # 添加第一个结果
    _handle_line = '    ' + _handle_line[_k:]

    while len(_handle_line) >= 79:
        _next_line = _handle_line[:78]
        _k = _next_line.rfind(',') + 1
        _result.append(_handle_line[:_k])
        _handle_line = '   ' + _handle_line[_k:]  # 这里只要三个

    _result.append(_handle_line)
    _result.append(_last_line)
    return '\n'.join(_result)


# OpenGL 使用到的变量类型
Int = ctypes.c_int
UInt = ctypes.c_uint
Byte = ctypes.c_byte
UByte = ctypes.c_ubyte
Short = ctypes.c_short
UShort = ctypes.c_ushort
Long = ctypes.c_int64
ULong = ctypes.c_uint64
Float = ctypes.c_float
Double = ctypes.c_double
VoidP = ctypes.c_void_p
CharP = ctypes.c_char_p
P = ctypes.POINTER
C = ctypes.CFUNCTYPE
Size = ctypes.c_size_t
Handle = Size if system == 'Darwin' else UInt


class GLSync(ctypes.Structure):
    ...


GLSyncP = P(GLSync)

if system == 'Windows':  # 适配不同的系统
    class EXT:  # 扩展函数调用

        def __init__(self, name, restype, *arg_types):
            self._func = None
            self._name = bytes(ord(_c) for _c in name)
            self._type = ctypes.WINFUNCTYPE(restype, *arg_types)

        def __call__(self, *args):
            if self._func is None:  # 第一次调用勾取函数指针
                _address = _wglGetFunction(self._name)
                if not ctypes.cast(_address, P(Handle)):
                    return None
                self._func = ctypes.cast(_address, self._type)

            return self._func(*args)


    GL = dynamic(ctypes.windll.opengl32, EXT)  # 非扩展函数调用
    _wglGetFunction = GL('wglGetProcAddress', C(P(Handle)), CharP)


elif system == 'Darwin':
    GL = dynamic(ctypes.cdll.LoadLibrary(
        '/System/Library/Framework/OpenGL.framework/OpenGL'
    ))

else:
    import ctypes.util

    GL = dynamic(ctypes.cdll.LoadLibrary(
        ctypes.util.find_library('OpenGL')
    ))

__all__ = [
    'Byte', 'UByte', 'Short', 'UShort', 'Int', 'UInt', 'Long', 'ULong',
    'Float', 'Double', 'VoidP', 'CharP', 'Size', 'Handle', 'GLSyncP',
    'GL', 'P', 'C', 'wrapper'
]
