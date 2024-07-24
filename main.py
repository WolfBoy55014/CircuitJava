# coding=utf-8

import path_import

from runtime.jclass import ClassLoader
from interpreter import interpreter

import supervisor
import microcontroller
import time

def parse_params():
    # args = sys.argv
    # if len(args) <= 1:
    #     print('use: python Zvm.py xx[.class]')
    #     print('eg: python Zvm.py main')
    #     print('eg: python Zvm.py main.class')
    #     return None
    name = "test/test"
    if name.endswith('.class'):
        name = name[:name.find('.class')]
    return name


def main():
    # Turn off Auto-reload
    supervisor.runtime.autoreload = False

    # Set Clock Speed
    microcontroller.cpu.frequency = 133 * 1000000 # 125000000
    print("Clock Speed:", microcontroller.cpu.frequency)
    print("CPU Temp:", microcontroller.cpu.temperature)
    
    class_file = parse_params()
    if class_file is None:
        return
    loader = ClassLoader()
    j_class = loader.load_class(class_file)
    print(j_class.name)
    method = j_class.get_main_method()
    start = time.monotonic()
    interpreter.Interpreter.exec_method(method)
    print("Execution Time:", time.monotonic() - start)


if __name__ == '__main__':
    main()
