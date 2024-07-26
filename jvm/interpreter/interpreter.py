# coding=utf-8

from jvm.runtime.thread import Thread, Frame
from jvm.base.utils import print_utils
from jvm.interpreter.code_parser import CodeParser
from jvm.instruction import instruction
from jvm.jgc.gc import GC
#import threading


class Interpreter(object):
    def __init__(self):
        self.thread = None

    def run(self, method):
        #print_utils.print_jvm_status(threading.currentThread.__name__)
        print_utils.print_jvm_status('\n=================== running status =====================\n')
        self.thread = Thread.new_thread()
        thread = self.thread
        frame = Frame(thread, method)
        thread.add_frame(frame)
        code_parser = CodeParser(method.code)
        while True:
            if not thread.has_frame():
                break
            GC.check_gc()
            frame = thread.top_frame()
            method = frame.method
            code_parser.reset(method.code, frame.pc)
            ins_code = code_parser.read_code()
            print_utils.print_jvm_status('ins_code: %x' % ins_code)
            ins = instruction.get_instruction(ins_code)
            ins.read_operands(code_parser)
            thread.pc = frame.pc  # 保存上一条 pc
            frame.pc = code_parser.pc
            ins.execute_wrapper(frame)

        print_utils.print_jvm_status('\n=================== output =====================')
        print_utils.StreamPrinter.print_all(thread)
        Thread.finish_thread(thread)

    @staticmethod
    def exec_method(method):
        m_interpreter = Interpreter()
        m_interpreter.run(method)
