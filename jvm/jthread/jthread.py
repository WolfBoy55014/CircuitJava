# coding=utf-8


from jvm.runtime.jclass import Method
#import threading


class JThread(object):
    @staticmethod
    def start_new_thread(method):
        t = NativeThread(method)
        t.start()


class NativeThread():
    def __init__(self, method):
        #super(NativeThread, self).__init__()
        self.method = method

    def run(self):
        from jvm.interpreter.interpreter import Interpreter
        Interpreter.exec_method(self.method)


class GCThread(object):
    pass
