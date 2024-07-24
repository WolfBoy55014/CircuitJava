import digitalio
import board
import base.utils.print_utils as print_utils
import base.utils.error_handler as error_handler

def __run_board_class(n_frame, method):
    #print("Running board class", method.jclass.name, method.name, method.descriptor)
    if method.name == 'write' and method.jclass.name == 'board/GPIO':
            if method.descriptor == '(IZ)V':
                pin = n_frame.local_vars.get_int(1)
                value = n_frame.local_vars.get_int(2)
                gpio.dWrite(pin, value)
    if method.name == 'read' and method.jclass.name == 'board/GPIO':
            if method.descriptor == '(I)Z':
                pin = n_frame.local_vars.get_int(1)
                n_frame.operand_stack.push_int(gpio.dRead(pin))
                n_frame.pc += 1
    if method.name == 'pullUp' and method.jclass.name == 'board/GPIO':
            if method.descriptor == '(I)V':
                pin = n_frame.local_vars.get_int(1)
                gpio.pullUp(pin)
    if method.name == 'pullDown' and method.jclass.name == 'board/GPIO':
            if method.descriptor == '(I)V':
                pin = n_frame.local_vars.get_int(1)
                gpio.pullDown(pin)
    if method.name == 'sayBoo' and method.jclass.name == 'CJ/test/Boo':
            if method.descriptor == '()V':
                print_utils.StreamPrinter.append_msg(n_frame.thread, 'Boo!')

def _int_2_pin(pin_id):
    if pin_id == 1:
        _pin = board.D1
    elif pin_id == 2:
        _pin = board.D2
    elif pin_id == 3:
        _pin = board.D3
    elif pin_id == 4:
        _pin = board.BUTTON
    elif pin_id == 5:
        _pin = board.D5
    elif pin_id == 6:
        _pin = board.D6
    elif pin_id == 7:
        _pin = board.D7
    elif pin_id == 8:
        _pin = board.D8
    elif pin_id == 9:
        _pin = board.D9
    elif pin_id == 10:
        _pin = board.D10
    elif pin_id == 11:
        _pin = board.D11
    elif pin_id == 12:
        _pin = board.D12
    elif pin_id == 13:
        _pin = board.D13
    elif pin_id == 14:
        _pin = board.D14
    elif pin_id == 15:
        _pin = board.D15
    elif pin_id == 16:
        _pin = board.D16
    elif pin_id == 17:
        _pin = board.D17
    elif pin_id == 18:
        _pin = board.D18
    elif pin_id == 19:
        _pin = board.D19
    elif pin_id == 20:
        _pin = board.D20
    elif pin_id == 21:
        _pin = board.D21
    elif pin_id == 22:
        _pin = board.D22
    elif pin_id == 23:
        _pin = board.D23
    elif pin_id == 24:
        _pin = board.D24
    elif pin_id == 25:
        _pin = board.D25
    elif pin_id == 26:
        _pin = board.D26
    elif pin_id == 27:
        _pin = board.D27
    elif pin_id == 28:
        _pin = board.D28
    elif pin_id == 29:
        _pin = board.D29
    else:
        print("That Pin Does not exist!")
    return _pin


class GPIO:
    def __init__(self):

        self.pins = {}

    def dWrite(self, pin_id, value):
        pin = None
        try:
            pin = self.pins[pin_id]
            if pin.direction == digitalio.Direction.INPUT:
                error_handler.rise_runtime_error("Pin {} is set to input, make sure to deinit it before using again".format(pin_id))
        except:
            _pin = _int_2_pin(pin_id)
            _pin = digitalio.DigitalInOut(_pin)
            _pin.direction = digitalio.Direction.OUTPUT
            self.pins[pin_id] = _pin
            pin = _pin
        
        pin.value = bool(value)
    
    def dRead(self, pin_id):
        pin = None
        try:
            pin = self.pins[pin_id]
            if pin.direction == digitalio.Direction.OUTPUT:
                error_handler.rise_runtime_error("Pin {} is set to output, make sure to deinit it before using again".format(pin_id))
        except:
            _pin = _int_2_pin(pin_id)
            _pin = digitalio.DigitalInOut(_pin)
            _pin.direction = digitalio.Direction.INPUT
            self.pins[pin_id] = _pin
            pin = _pin

        value = int(pin.value)
        return value

    def pullUp(self, pin_id):
        pin = None
        try:
            pin = self.pins[pin_id]
        except:
            error_handler.rise_runtime_error("Pin {} is not initialized before setting pullup".format(pin_id))
        
        pin.pull = digitalio.Pull.UP
        self.pins[pin_id] = pin
        
    def pullDown(self, pin_id):
        pin = None
        try:
            pin = self.pins[pin_id]
        except:
            error_handler.rise_runtime_error("Pin {} is not initialized before setting pulldown".format(pin_id))
        
        pin.pull = digitalio.Pull.DOWN

gpio = GPIO()