from jvm.runtime.nclass import NativeClass
from jvm.base.utils.print_utils import printb
from pwmio import PWMOut
from jvm.runtime.jobject import JObject
from layout import _int_2_pin

class DAC(NativeClass):
    def __init__(self):
        self.type = JObject.TYPE_NOBJ
        self.name = "board/DAC"
        self.methods = {
            "<init>-(II)V": self.init,
            "setValue-(Z)V": self.setValue,
            "setAnalog-(I)V": self.setAnalog,
            "getPinID-()I": self.getPinID,
            "getFrequency-()I": self.getFrequency,
            "deInit-()V": self.deInit
        }
        
    def init(self, frequency, pinID):
        printb(f'Creating DAC {pinID}')
        self.pinID = pinID
        self.pin = PWMOut(pin=_int_2_pin(pinID), frequency=frequency)
    
    def setValue(self, value):
        self.pin.duty_cycle =  65535 if value else 0
    
    def setAnalog(self, value):
        self.pin.duty_cycle = int(value)

    def getPinID(self):
        return self.pinID
    
    def getFrequency(self):
        return self.pin.frequency
    
    def deInit(self):
        self.pin.deinit()
        
    
    
        