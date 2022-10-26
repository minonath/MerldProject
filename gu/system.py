import array
import base64
import os
import random
import struct
import types

# 空函数，用于替换其它函数
empty = (lambda *args, **kwargs: None)


def dynamic(library, fallback=None):
    """ 构造绑定动态库内部函数的函数

    参数：
        - _library 载入的动态库，需是 ctypes.CDLL 类型
        - fallback 读取动态库函数失败后的代替函数，默认进行打印输出
    返回：
        返回一个绑定函数，调用绑定函数才能进行完整绑定
    """

    def _bind(name, result_type, *argument_types):
        """ 绑定动态库内部函数

        参数：
            - name 需要绑定函数的名称
            - result_type 需要绑定函数的返回值，如果没有返回值也要填 None
            - argument_types 需要绑定函数的参数，如果没有参数这里不填
        返回：
            返回一个绑定函数，调用绑定函数才能进行完整绑定
        """
        try:
            _func = getattr(library, name)
            _func.restype = result_type
            setattr(_func, 'arg''types', argument_types)

        except AttributeError:
            if fallback:
                _func = fallback(name, result_type, *argument_types)
            else:
                def _func(*arguments):
                    print('<Invalid Function>', library, name, arguments)

        return _func

    return _bind


cache = '__py''cache__'  # python 文件运行会产生的缓存文件夹
proclaim = (
    b'iBL{Q4GJ0x0000DNk~Le0000m0000m2nGNE09OL}hX4QokV!;ARCt{2l}ir5AP5D$|E1e)H'
    b'%16w=}f|o!W+}*S^%XyiG{!zf$&p_-ituR-m1`U84z$louNbMF9=j4%A*aP`RpTb>c2+7t4'
    b'9k0-aT4O0v)bY1P~C;F=asDKx={M9t6e<c+Eio0plD5Mh' b'fhDb|pdkEdr;-*9cUBKsD-'
    b'Yl7Bt3OvWARe*ypkUXyu' b'qso6++>i_@%07*qoM6N<$f&'
)
password = base64.b85encode(proclaim)  # 这是资料文件的密钥
icon = base64.b85decode(proclaim)  # 默认的程序标志


def crypto(data, key):
    """ 加密和解密函数

    参数：
        - data 一个 bytes 数据
        - key 转换钥匙
    返回：
        返回转换后的 bytes 数据，以及它的长度
    """
    random.seed(key)  # 设置密钥

    _data = array.array('B', data)
    _length = len(_data)

    for _i in range(_length):  # 计算
        _data[_i] ^= random.getrandbits(8) ^ random.getrandbits(3)

    random.seed()  # 重置随机数

    return _data.tobytes(), _length


class Guru:
    """ 文件管理单元 """

    def __init__(self, path, index=None):
        self._guru_index = index or {}
        self._guru_path = os.path.abspath(path)

    def __iter__(self):
        return self._guru_index.__iter__()

    def guru_read(self, name):
        """ 获取文件的内容 """

    def guru_write(self, name, data):
        """ 写入文件的内容 """

    def guru_pack(self):
        """ 将文件夹打包成资源文件 """

    def guru_unpack(self):
        """ 将资源文件解包成文件夹 """


class Directory(Guru):
    """ 以文件夹形式存在的文件管理单元 """

    def __init__(self, path):
        Guru.__init__(self, path)
        self.guru_refresh()

    def guru_refresh(self):
        """ 建立 / 重建文件目录的缓存 """

        _length = len(self._guru_path) + 1  # 文件夹路径名称的长度，包含斜杠

        for _dir_path, _, _file_names in os.walk(self._guru_path):
            for _name in _file_names:
                if _name.startswith('.'):
                    continue
                _name = os.path.join(_dir_path, _name)[_length:]  # 相对路径
                _name.replace('\\', '/')  # 统一替换为 slash
                if cache in _name:  # 跳过 python 自带的缓存
                    continue
                self._guru_index[_name] = self._guru_path + '/' + _name

    def guru_read(self, name):
        if name not in self._guru_index:
            self.guru_refresh()

        try:
            _path = self._guru_index[name]
            with open(_path, 'rb') as _f:
                return _f.read()
        except (IndexError, FileNotFoundError):
            return b''

    def guru_write(self, name, data):
        """ 使用相对路径，以及 slash ，不要用 backslash """

        self._guru_index[name] = _target = self._guru_path + '/' + name

        _path = os.path.dirname(_target)
        if not os.path.exists(_path):
            os.makedirs(_path)

        with open(_target, 'wb') as _f:
            _f.write(data)

    def guru_pack(self):
        """ 打包文件夹

        文件存档结构如下
            - 资源段：所有的文件按排序存储，进行加密
            - 索引段：以（文件名：文件初始位置，文件长度，文件密钥）储存的字典
        """
        self.guru_refresh()  # 重建缓存

        _guru_file = open(self._guru_path + '.guru', 'wb')
        _data_index = {}

        _guru_file.write(b'Guru\x00\x00\x00\x00\x00\x00\x00\x00')  # 头部预留
        _start_position = 12

        _p1, _p2 = 0, len(self._guru_index)

        for _target in self._guru_index:  # 这是数据段
            with open(os.path.join(self._guru_path, _target), 'rb') as _f:
                _data = _f.read()
            _key = random.getrandbits(32)  # 8-bytes _key 随机 8 位密码
            _data, _data_len = crypto(_data, _key)  # 加密
            _guru_file.write(_data)
            _data_index[_target] = _key, _start_position, _data_len  # 索引段
            _start_position += _data_len
            _p1 += 1
            print('{}/{} - {} - {:3g}'.format(_p1, _p2, _target, _data_len))

        _data_info = array.array('B')  # 这是索引段
        _data_name = array.array('B')
        for _name, _value in _data_index.items():  # 把记录的文件索引打包成块
            _data_name.extend(_name.encode())
            _data_name.append(0)
            _data_info.extend(
                crypto(struct.pack('3I', *_value), password)[0])

        _data_name, _data_name_len = crypto(_data_name, password)
        _guru_file.write(_data_name)
        _guru_file.write(_data_info.tobytes())

        _guru_file.seek(4, 0)  # 重写文件头
        _guru_file.write(struct.pack('2I', _start_position, _data_name_len))

        _guru_file.close()


class GuruFile(Guru):
    """ 以特殊文件存在的文件管理单元

    GuruFile 需要验证后创建
    """

    def __init__(self, path, file, index):
        Guru.__init__(self, path, index)
        self._guru_file = file

    def __del__(self):
        """ 尝试关闭释放文件 """
        self._guru_file and self._guru_file.close()

    def guru_read(self, name):
        if name not in self._guru_index:  # 因为打包好了，所以不存在索引缺失
            return b''

        _chunk, _length = crypto(self._guru_index[name], password)

        assert _length == 12

        _key, _position, _length = struct.unpack('3I', _chunk)
        self._guru_file.seek(_position, 0)
        data = self._guru_file.read(_length)
        return crypto(data, _key)[0]

    def guru_unpack(self):
        _target_directory, _sign = os.path.splitext(self._guru_path)

        assert _sign == '.guru'

        _p1, _p2 = 0, len(self._guru_index)

        for _k in self._guru_index:
            _path = os.path.join(_target_directory, _k)
            _dir_path = os.path.dirname(_path)

            if not os.path.exists(_dir_path):
                os.makedirs(_dir_path)

            with open(_path, 'wb') as _f:
                _f.write(self.guru_read(_k))

            _p1 += 1
            print('{}/{} - {}'.format(_p1, _p2, _k))


def guru_file(path):
    """ 进行 GuruFile 文件测试，如果测试成功则载入 """
    try:
        _file = open(path, 'rb')
        _sign, _pos, _length = struct.unpack('3I', _file.read(12))

        assert _sign == 1970435399  # b'Guru'

        _file.seek(_pos, 0)  # 解压索引段
        _n = crypto(
            _file.read(_length), password)[0].split(b'\x00')
        _k = len(_n) - 1
        _index = dict(
            (_n[_i].decode(), _file.read(12)) for _i in range(_k))

        return GuruFile(path, _file, _index)

    except Exception as _e:
        print(_e)

    return None


class Resource:
    """ 文件管理 """

    def __init__(self):
        self._resource_name = None  # 默认数据单元的名称
        self._resource_guru = None  # 默认数据单元的实例
        self._resource_order = []  # 数据单元装载顺序
        self._resource_loaded = {}  # 数据单元集合
        self._resource_index = {}  # 所有更新的文件索引

    def __repr__(self):
        return 'Resource'

    def __str__(self):
        """ 可以使用此方法检查可用的文件管理单元 """

        return str(self._resource_order)

    @property
    def resource_default(self):
        return self._resource_guru

    @resource_default.setter
    def resource_default(self, path):
        """ 设置默认文件 """

        if path in self._resource_order:
            self._resource_name = path
            self._resource_guru = self._resource_loaded[path]
        else:
            self._resource_name = None
            self._resource_guru = None

    def resource_load(self, *path):
        """ 载入资源文件或者目录

        参数：
            - path 为相对路径文本，载入成功后会记录在 _resource_order 里
        """
        for _p in path:
            if _p in self._resource_order:
                continue

            if not os.path.exists(_p):
                _p += '.guru'  # 增加默认后缀再次尝试
                if not os.path.exists(_p):  # 不存在就不会加载
                    continue

            if os.path.isdir(_p):  # 文件夹优先
                _guru = Directory(_p)
            else:  # 一般不存在不是文件也不是文件夹的东西
                _guru = guru_file(_p)
            if not _guru:
                continue

            self._resource_order.append(_p)  # 加入序列
            self._resource_loaded[_p] = _guru

            for _data_name in _guru:
                self._resource_index[_data_name] = _guru

        if self._resource_order:  # 最后加载的设为默认文件
            self.resource_default = self._resource_order[-1]

    def resource_unload(self, *path):
        """ 卸载文件

        如果参数为空，等同于刷新索引
        参数值必须在 _resource_order 内，可以调用 __str__ 查看
        """

        for _p in path:
            if _p in self._resource_order:
                self._resource_order.remove(_p)
                self._resource_loaded.pop(_p)

        self.resource_refresh()

    def resource_refresh(self):
        self._resource_index.clear()  # 清空文件索引

        if self._resource_order:
            self.resource_default = self._resource_order[-1]

            for _path_name in self._resource_order:  # 有顺序重构文件索引
                _guru = self._resource_loaded[_path_name]
                if isinstance(_guru, Directory):
                    _guru.guru_refresh()

                for data_name in _guru:
                    self._resource_index[data_name] = _guru

        else:
            self.resource_default = None

    def resource_read(self, name):
        _target_guru = self._resource_index.get(name, self.resource_default)

        if _target_guru:
            return _target_guru.guru_read(name)

        return b''

    def resource_write(self, name, data):
        if self.resource_default:
            self.resource_unpack()  # 尝试一次解包
            self.resource_default.guru_write(name, data)
            self._resource_index[name] = self.resource_default

    def resource_pack(self):
        if isinstance(self.resource_default, Directory):
            self.resource_default.guru_pack()

    def resource_unpack(self):
        if isinstance(self.resource_default, GuruFile):
            self.resource_default.guru_unpack()
            _guru_name = self._resource_name  # 重新载入，以文件夹为主

            assert _guru_name.endswith('.guru')

            self.resource_unload(_guru_name)
            self.resource_load(_guru_name[:-5])


resource = Resource()

script_format = ('script/{}', 'script/{}.py', '{}', '{}.py')
image_format = ('image/{}', 'image/{}.png', '{}', '{}.png')
# audio_format = ('audio/{}', 'audio/{}.ogg', '{}', '{}.ogg')


def script(name):
    """ 读取文件资源里的脚本，制作成库后返回 """

    _module = types.ModuleType('gu_user_' + name)

    for _format in script_format:
        _script = resource.resource_read(_format.format(name))
        if _script:
            try:
                exec(_script, _module.__dict__)
            except Exception as _e:
                print(_e)

    return _module


def image(name):
    """ 读取文件资源里的 png 图片 """

    for _format in image_format:
        _image = resource.resource_read(_format.format(name))
        if _image:
            return _image

    return icon


__all__ = ['empty', 'dynamic', 'icon', 'resource', 'script', 'image']
