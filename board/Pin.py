from jvm.runtime.nclass import NativeClass
from jvm.base.utils.print_utils import printb
from digitalio import DigitalInOut, Pull, Direction
from jvm.runtime.jobject import JObject
import board

_BOARD = "PIPICO"

class Pin(NativeClass):
    def __init__(self):
        self.type = JObject.TYPE_NOBJ
        self.name = "board/Pin"
        self.methods = {
            "<init>-(IZ)V": self.init,
            "setValue-(Z)V": self.setValue,
            "setValue-(I)V": self.setValue,
            "getValue-()Z": self.getValue,
            "getValueInt-()I": self.getValueInt,
            "getPinID-()I": self.getPinID,
            "isInput-()Z": self.getIsInput,
            "setPullUp-()V": self.setPullUp,
            "setPullDown-()V": self.setPullDown,
            "setFloating-()V": self.setFloating,
            "deInit-()V": self.deInit
        }
    
    @staticmethod
    def _int_2_pin(pin_id):
        if _BOARD == "PIPICO":
            return Pin._pipico(pin_id)
        elif _BOARD == "FRP2040":
            return Pin._frp2040(pin_id)
        else:
            printb("Board not supported")
            raise Exception("Board not supported")


    @staticmethod
    def _frp2040(pin_id):
        if pin_id == 0:
            _pin = board.TX
        elif pin_id == 1:
            _pin = board.RX
        elif pin_id == 2:
            _pin = board.SDA
        elif pin_id == 3:
            _pin = board.SCL
        elif pin_id == 4:
            _pin = board.BUTTON
        # elif pin_id == 5:
        #     _pin = board.D5
        elif pin_id == 6:
            _pin = board.D4
        elif pin_id == 7:
            _pin = board.D5
        elif pin_id == 8:
            _pin = board.D6
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
        # elif pin_id == 14:
        #     _pin = board.D14
        # elif pin_id == 15:
        #     _pin = board.D15
        elif pin_id == 16:
            _pin = board.NEOPIXEL
        # elif pin_id == 17:
        #     _pin = board.D17
        elif pin_id == 18:
            _pin = board.SCK
        elif pin_id == 19:
            _pin = board.MOSI
        elif pin_id == 20:
            _pin = board.MISO
        # elif pin_id == 21:
        #     _pin = board.D21
        # elif pin_id == 22:
        #     _pin = board.D22
        # elif pin_id == 23:
        #     _pin = board.D23
        elif pin_id == 24:
            _pin = board.D24
        elif pin_id == 25:
            _pin = board.D25
        elif pin_id == 26:
            _pin = board.A0
        elif pin_id == 27:
            _pin = board.A1
        elif pin_id == 28:
            _pin = board.A2
        elif pin_id == 29:
            _pin = board.A3
        else:
            print("That Pin Does not exist!")
        return _pin
    
    @staticmethod
    def _pipico(pin_id):
        if pin_id == 0:
            _pin = board.GP0
        elif pin_id == 1:
            _pin = board.GP1
        elif pin_id == 2:
            _pin = board.GP2
        elif pin_id == 3:
            _pin = board.GP3
        elif pin_id == 4:
            _pin = board.GP4
        elif pin_id == 5:
            _pin = board.GP5
        elif pin_id == 6:
            _pin = board.GP6
        elif pin_id == 7:
            _pin = board.GP7
        elif pin_id == 8:
            _pin = board.GP8
        elif pin_id == 9:
            _pin = board.GP9
        elif pin_id == 10:
            _pin = board.GP10
        elif pin_id == 11:
            _pin = board.GP11
        elif pin_id == 12:
            _pin = board.GP12
        elif pin_id == 13:
            _pin = board.GP13
        elif pin_id == 14:
            _pin = board.GP14
        elif pin_id == 15:
            _pin = board.GP15
        elif pin_id == 16:
            _pin = board.GP16
        elif pin_id == 17:
            _pin = board.GP17
        elif pin_id == 18:
            _pin = board.GP18
        elif pin_id == 19:
            _pin = board.GP19
        elif pin_id == 20:
            _pin = board.GP20
        elif pin_id == 21:
            _pin = board.GP21
        elif pin_id == 22:
            _pin = board.GP22
        elif pin_id == 23:
            _pin = board.GP23
        elif pin_id == 24:
            _pin = board.VBUS_SENSE
        elif pin_id == 25:
            _pin = board.LED
        elif pin_id == 26:
            _pin = board.GP26_A0
        elif pin_id == 27:
            _pin = board.GP27_A1
        elif pin_id == 28:
            _pin = board.GP28_A2
        elif pin_id == 29:
            _pin = board.VOLTAGE_MONITOR
        else:
            print("That Pin Does not exist!")
        return _pin
    

    def init(self, isInput, pinID):
        printb(f'Creating Pin {pinID} as {isInput}')
        self.pinID = pinID
        self.isInput = isInput
        self.pin = DigitalInOut(Pin._int_2_pin(pinID))
        self.pin.direction = Direction.INPUT if isInput else Direction.OUTPUT
    
    def setValue(self, value):
        if not self.isInput:
           self.pin.value = bool(value)
        else:
            raise Exception(f'Pin {self.pinID} is an input pin, can\'t set value.')
    
    def getValue(self):
        return self.pin.value
    
    def getValueInt(self):
        return int(self.pin.value)
    
    def getPinID(self):
        return self.pinID
    
    def getIsInput(self):
        return self.isInput
    
    def setPullUp(self):
        if self.isInput:
            self.pin.pull = Pull.UP
        else:
            raise Exception(f'Pin {self.pinID} is an output pin, can\'t set pull up.')
        
    def setPullDown(self):
        if self.isInput:
            self.pin.pull = Pull.DOWN
        else:
            raise Exception(f'Pin {self.pinID} is an output pin, can\'t set pull down.')
        
    def setFloating(self):
        if self.isInput:
            self.pin.pull = None
        else:
            raise Exception(f'Pin {self.pinID} is an output pin, can\'t set floating.')
    
    def deInit(self):
        self.pin.deinit()
        
    
    
        