from jvm.runtime.nclass import NativeClass
from jvm.base.utils.print_utils import printb
from digitalio import DigitalInOut, Pull, Direction
from jvm.runtime.jobject import JObject
from layout import _int_2_pin

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
    
    def init(self, isInput, pinID):
        printb(f'Creating Pin {pinID} as {isInput}')
        self.pinID = pinID
        self.isInput = isInput
        self.pin = DigitalInOut(_int_2_pin(pinID))
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
        
    
    
        