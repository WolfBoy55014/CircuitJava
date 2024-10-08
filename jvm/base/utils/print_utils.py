# coding=utf-8

from jvm.base import jvm_config

_ORANGE = f"\u001b[38;2;{255};{100};{0}m"
_BLUE = f"\u001b[38;2;{0};{100};{255}m"
_DEFAULT = f"\u001b[0m"

def printo(msg):
    if jvm_config.log_jvm_status:
        print(_ORANGE + str(msg) + _DEFAULT)

def printb(msg):
    if jvm_config.log_jvm_status:
        print(_BLUE + str(msg) + _DEFAULT)

def print_error(msg):
    print("error: " + msg)


def print_jvm_status(msg):
    if jvm_config.log_jvm_status:
        print(msg)


def print_msg(msg):
    print(msg)


class StreamPrinter(object):
    msgs = {}

    @staticmethod
    def print_all(thread):
        if thread in StreamPrinter.msgs:
            msgs = StreamPrinter.msgs[thread]
            for msg in msgs:
                print_msg(msg)

    @staticmethod
    def append_msg(thread, msg):
        if jvm_config.print_in_real_time:
            print_msg(msg)
        else:
            if thread in StreamPrinter.msgs:
                StreamPrinter.msgs[thread].append(msg)
            else:
                StreamPrinter.msgs[thread] = []
                StreamPrinter.msgs[thread].append(msg)
