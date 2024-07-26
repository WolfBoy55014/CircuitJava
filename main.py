# coding=utf-8

import jvm.path_import

from jvm.runtime.jclass import ClassLoader
from jvm.interpreter import interpreter

import supervisor
import microcontroller
import time
from os import getenv


def main():
    # Turn off Auto-reload
    supervisor.runtime.autoreload = False

    # Set Clock Speed
    microcontroller.cpu.frequency = 100 * 1000000 # 125000000
    print("Clock Speed:", microcontroller.cpu.frequency)
    print("CPU Temp:", microcontroller.cpu.temperature)
    
    class_file = getenv("MAIN_JAVA_FILE", "Main")
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
