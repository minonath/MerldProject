import ctypes

char_pointer = ctypes.POINTER(ctypes.c_char)

float_epsilon = 1e-7
double_epsilon = 1e-16


class Array:
    UByte = ctypes.c_ubyte
    Byte = ctypes.c_byte
    UShort = ctypes.c_ushort
    Short = ctypes.c_short
    UInt = ctypes.c_uint
    Int = ctypes.c_int
    ULong = ctypes.c_ulong
    Long = ctypes.c_long
    Float = ctypes.c_float
    Double = ctypes.c_double

    _array_name = {
        UByte: 'UByte', Byte: 'Byte', UShort: 'UShort', Short: 'Short',
        UInt: 'UInt', Int: 'Int', ULong: 'ULong', Long: 'Long',
        Float: 'Float', Double: 'Double'
    }

    # --------------------------------------------------------------------
    # 数组创建方式：
    # __init__      直接创建空数组
    # array_at      创建目标指针的数组容器，注意内存安全
    # array_copy    从已有数组复制

    def __init__(self, data_nums, data_type):
        self._array_type = data_type
        self._array_nums = data_nums
        self._array_data = (data_type * data_nums)()  # 初始化
        self._array_unit = unit_length = ctypes.sizeof(data_type)
        self._array_size = unit_length * data_nums
        self._array_here = ctypes.addressof(self._array_data)  # 复制地址
        self._as_parameter_ = ctypes.cast(  # 默认使用类型指针，上面的是野指针
            self._array_here, ctypes.POINTER(data_type)
        )

    @classmethod
    def array_at(cls, address, data_nums, data_type=UByte):
        _array = object.__new__(cls)
        _array._array_type = data_type
        _array._array_nums = data_nums
        _array._array_data = ctypes.cast(
            address, ctypes.POINTER(data_type * data_nums))[0]
        _array._array_unit = unit_length = ctypes.sizeof(data_type)
        _array._array_size = unit_length * data_nums
        _array._array_here = ctypes.addressof(_array._array_data)
        _array._as_parameter_ = ctypes.cast(
            _array._array_here, ctypes.POINTER(data_type)
        )
        return _array

    def array_copy(self):
        return self.__class__(*self)

    # --------------------------------------------------------------------
    # 数组读取方式
    # __getitem__   读取指定位置 1 个元素
    # __bytes__     读取为字节数组
    # __repr__      读取为文本
    # array_read    读取指定位置多个元素

    def __getitem__(self, item):
        return self._array_data[item]

    def __bytes__(self):
        return ctypes.cast(self._array_data, char_pointer)[:self._array_size]

    def __repr__(self):
        return '({} * {})({})'.format(
            Array._array_name[self._array_type], self._array_nums,
            ', '.join('{:.6g}'.format(num) for num in self._array_data))

    def array_read(self, index, size):
        if size >= self._array_nums - index:
            size = self._array_nums - index
        return self._array_data[index:index + size]

    # --------------------------------------------------------------------
    # 数组属性

    @property
    def array_size(self):
        return self._array_size

    @property
    def array_nums(self):
        return self._array_nums

    @property
    def array_address(self):
        # 这是数组内存的地址头，实际上是一个野指针
        # 有些绑定的 C 语言函数需要类型指针，要用 _as_parameter_ 获取
        # 如果不需要类型指针，比如 glSubData 之类的，用野指针就行
        return self._array_here

    # --------------------------------------------------------------------
    # 数组赋值方式

    def __setitem__(self, key, value):
        self._array_data[key] = value

    def __call__(self, *values):
        _value_size = len(values)
        if _value_size > self._array_size:
            self._array_data[:] = values[:self._array_size]
        else:
            self._array_data[:_value_size] = values
        return self

    def array_write(self, index, *elements):
        for _e in elements:
            if index < self._array_nums:
                self._array_data[index] = _e
                index += 1
        return index

    def array_offset(self, offset=0):
        # 将数列的某个元素作为类型指针传出，如果参数为零，等同于 _as_parameter_
        return ctypes.cast(
            self._array_here + offset * ctypes.sizeof(self._array_type),
            ctypes.POINTER(self._array_type)
        )

    @array_address.setter
    def array_address(self, address):
        # 修改 array_address 可以读取目标内存的数据，注意内存不要越界
        # 这里是转化为有长度有类型的指针，也就是 type[size] 的结构指针
        _structure = ctypes.POINTER(self._array_type * self._array_size)
        _structure_data = ctypes.cast(address, _structure)[0]
        self._array_data[:] = _structure_data

    # --------------------------------------------------------------------
    # 改变数组长度，会切换内存位置

    def array_adjust(self, data_nums):
        _data_next = (self._array_type * data_nums)()  # 初始化
        _data_size = self._array_unit * data_nums
        ctypes.memmove(
            _data_next, self._array_data, min(self._array_size, _data_size))
        self._array_nums = data_nums
        self._array_data = _data_next
        self._array_size = _data_size
        self._array_here = ctypes.addressof(self._array_data)
        self._as_parameter_ = ctypes.cast(
            self._array_here, ctypes.POINTER(self._array_type)
        )


class UBytes(Array):
    def __init__(self, *values, data_nums=0):
        if data_nums == 0:
            data_nums = len(values)

        Array.__init__(self, data_nums, Array.UByte)
        self.__call__(*values)


class Bytes(Array):
    def __init__(self, *values, data_nums=0):
        if data_nums == 0:
            data_nums = len(values)

        Array.__init__(self, data_nums, Array.Byte)
        self.__call__(*values)


class UShorts(Array):
    def __init__(self, *values, data_nums=0):
        if data_nums == 0:
            data_nums = len(values)

        Array.__init__(self, data_nums, Array.UShort)
        self.__call__(*values)


class Shorts(Array):
    def __init__(self, *values, data_nums=0):
        if data_nums == 0:
            data_nums = len(values)

        Array.__init__(self, data_nums, Array.Short)
        self.__call__(*values)


class UInts(Array):
    def __init__(self, *values, data_nums=0):
        if data_nums == 0:
            data_nums = len(values)

        Array.__init__(self, data_nums, Array.UInt)
        self.__call__(*values)


class Ints(Array):
    def __init__(self, *values, data_nums=0):
        if data_nums == 0:
            data_nums = len(values)

        Array.__init__(self, data_nums, Array.Int)
        self.__call__(*values)


class ULongs(Array):
    def __init__(self, *values, data_nums=0):
        if data_nums == 0:
            data_nums = len(values)

        Array.__init__(self, data_nums, Array.ULong)
        self.__call__(*values)


class Longs(Array):
    def __init__(self, *values, data_nums=0):
        if data_nums == 0:
            data_nums = len(values)

        Array.__init__(self, data_nums, Array.Long)
        self.__call__(*values)


class Floats(Array):
    def __init__(self, *values, data_nums=0):
        if data_nums == 0:
            data_nums = len(values)

        Array.__init__(self, data_nums, Array.Float)
        self.__call__(*values)


class Doubles(Array):
    def __init__(self, *values, data_nums=0):
        if data_nums == 0:
            data_nums = len(values)

        Array.__init__(self, data_nums, Array.Double)
        self.__call__(*values)


__all__ = [
    'Array', 'UBytes', 'Bytes', 'UShorts', 'Shorts', 'UInts', 'Ints',
    'ULongs', 'Longs', 'Floats', 'Doubles', 'float_epsilon', 'double_epsilon'
]
