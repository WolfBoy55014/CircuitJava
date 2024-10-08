# coding=utf-8

from jvm.base.stack import Stack
from jvm.base.utils.print_utils import print_jvm_status
import jvm.runtime as runtime
import struct


# 这个 thread 是抽象的 thread
class Thread(object):
    __thread_pool = []

    def __init__(self):
        self.pc = 0
        self.stack = JavaStack()

    @staticmethod
    def new_thread():
        t = Thread()
        Thread.__thread_pool.append(t)
        return t

    @staticmethod
    def finish_thread(t):
        Thread.__thread_pool.remove(t)

    @staticmethod
    def all_thread():
        return Thread.__thread_pool

    def add_frame(self, frame):
        self.stack.add_frame(frame)

    def top_frame(self):
        return self.stack.top_frame()

    def pop_frame(self):
        self.stack.pop_frame()

    def has_frame(self):
        return self.stack.has_frame()

    def all_frames(self):
        return self.stack.all_frames()


class JavaStack(object):
    def __init__(self):
        self.__frames = []

    def has_frame(self):
        return len(self.__frames) > 0

    def add_frame(self, frame):
        self.__frames.append(frame)

    def pop_frame(self):
        self.__frames.pop()

    def top_frame(self):
        return self.__frames[len(self.__frames) - 1]

    def all_frames(self):
        return self.__frames


class Frame(object):
    def __init__(self, thread, method):
        self.pc = 0
        self.thread = thread
        self.method = method
        self.max_stack = method.max_stack
        self.max_locals = method.max_locals
        self.operand_stack = OperandStack(self.max_stack)
        self.local_vars = LocalVars(self.max_locals)
        self.dynamic_linking = DynamicLinking()

    def print_cur_state(self):
        print_jvm_status('max_stack: ' + str(self.max_stack))
        print_jvm_status('max_locals: ' + str(self.max_locals))
        print_jvm_status('operand_stack: ' + str(self.operand_stack.size()))
        print_jvm_status(self.operand_stack)
        print_jvm_status('local_vars: ' + str(self.local_vars.size()))
        print_jvm_status(self.local_vars)


class Slot(object):
    def __init__(self):
        self.num = None
        self.ref = None


# 局部变量表
class LocalVars(object):
    def __init__(self, size):
        self.__size = size
        self.__items = [None] * size
        for i in range(size):
            self.__items[i] = Slot()

    def __str__(self):
        s = ''
        for i in self.__items:
            s += str(i)
            s += '\n'
        return s

    def size(self):
        return self.__size

    def print_state(self):
        print_jvm_status(self.__items)

    def get_items(self):
        return self.__items

    def __add_num_to_item(self, index, data):
        slot = self.__items[index]
        slot.num = data

    def __get_num_from_item(self, index):
        return self.__items[index].num

    def __add_ref_to_item(self, index, ref):
        slot = self.__items[index]
        slot.ref = ref

    def __get_ref_from_item(self, index):
        return self.__items[index].ref

    def add_int(self, index, data):
        self.__add_num_to_item(index, struct.pack('i', data))

    def get_int(self, index):
        return struct.unpack('i', self.__get_num_from_item(index))[0]

    def add_long(self, index, data):
        packed = struct.pack('q', data)
        self.__add_num_to_item(index, packed[:4])
        self.__add_num_to_item(index + 1, packed[4:])

    def get_long(self, index):
        first = self.__get_num_from_item(index)
        last = self.__get_num_from_item(index + 1)
        return struct.unpack('q', first + last)[0]

    # TODO: python3 里 float 也是 8 字节，float 精度存疑
    def add_float(self, index, data):
        self.__add_num_to_item(index, struct.pack('f', data))

    def get_float(self, index):
        return struct.unpack('f', self.__get_num_from_item(index))[0]

    def add_double(self, index, data):
        packed = struct.pack('d', data)
        self.__add_num_to_item(index, packed[:4])
        self.__add_num_to_item(index + 1, packed[4:])

    def get_double(self, index):
        first = self.__get_num_from_item(index)
        last = self.__get_num_from_item(index + 1)
        return struct.unpack('d', first + last)[0]

    def add_ref(self, index, ref):
        self.__add_ref_to_item(index, ref)

    def get_ref(self, index):
        return self.__get_ref_from_item(index)


class Entry(object):
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return str(self.data)


# 操作数栈
class OperandStack(object):
    def __init__(self, size):
        self.__size = size
        self.__stack = Stack()

    def size(self):
        return self.__size

    def print_state(self):
        self.__stack.print_state()

    def clear(self):
        self.__stack.clear()

    # !!! notice !!!  如果是非 jref 的数据，这个方法返回的是封装后的 eg: int 返回的实际是 JInteger   主要是方便 push 使用
    # 如果以后需要真实数据，再改吧
    def top(self, index=None):
        if index is None:
            return self.__stack.peek().data
        else:
            return self.__stack.get_val_at(index).data

    # 类型1 指的是占一个 slot 的类型: int, float, ref
    def is_top_type1(self, index=None):
        ref = None
        if index is None:
            ref = self.__stack.peek().data
        else:
            ref = self.__stack.get_val_at(index).data
        if isinstance(ref, runtime.jclass.JInteger) or isinstance(ref, runtime.jclass.JFloat) \
                or isinstance(ref, runtime.jclass.JRef):
            return True
        return False

    def push(self, data):
        entry = Entry(data)
        self.__stack.push(entry)

    def pop(self, index=-1):
        ref = self.__stack.pop(index).data
        if isinstance(ref, runtime.jclass.JInteger) or isinstance(ref, runtime.jclass.JFloat) \
                or isinstance(ref, runtime.jclass.JLong) or isinstance(ref, runtime.jclass.JDouble):
            return ref.data
        return ref

    def pop_raw(self):
        return self.__stack.pop().data

    def push_int(self, data):
        jint = runtime.jclass.JInteger()
        jint.data = data
        self.push(jint)

    def pop_int(self, index=-1):
        return self.pop(index)

    def push_long(self, data):
        jlong = runtime.jclass.JLong()
        jlong.data = data
        self.push(jlong)

    def pop_long(self, index=-1):
        return self.pop(index)

    def push_float(self, data):
        jfloat = runtime.jclass.JFloat()
        jfloat.data = data
        self.push(jfloat)

    def pop_float(self, index=-1):
        return self.pop(index)

    def push_double(self, data):
        jdouble = runtime.jclass.JDouble()
        jdouble.data = data
        self.push(jdouble)

    def pop_double(self, index=-1):
        return self.pop(index)

    def push_ref(self, ref):
        self.push(ref)

    def pop_ref(self, index=-1):
        return self.pop(index)

    def get_all_data(self):
        return self.__stack.items()

    def __str__(self):
        s = ''
        for i in self.__stack.items():
            s += str(i)
            s += '\n'
        return s


class DynamicLinking(object):
    def __init__(self):
        pass


def test_local_var():
    local_vars = LocalVars(9)
    local_vars.add_long(0, 2147483680)
    print(local_vars.get_long(0))

    local_vars.add_int(2, 8)
    print(local_vars.get_int(2))

    local_vars.add_double(3, 2147483680.1231231312)
    print(local_vars.get_double(3))

    local_vars.add_float(5, 8.111)
    print(local_vars.get_float(5))


def test_main():
    pass


if __name__ == "__main__":
    test_local_var()
    # test_main()
