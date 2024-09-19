from jvm.runtime.nclass import NativeClass
from jvm.base.utils.print_utils import printb
from analogio import AnalogIn
from jvm.runtime.jobject import JObject
from layout import _int_2_pin

class ADC(NativeClass):
    def __init__(self):
        self.type = JObject.TYPE_NOBJ
        self.name = "board/ADC"
        self.methods = {
            "<init>-(I)V": self.init,
            "getValue-()Z": self.getValue,
            "getAnalog-()I": self.getAnalog,
            "getPinID-()I": self.getPinID,
            "deInit-()V": self.deInit
        }
        
    def init(self, pinID):
        printb(f'Creating ADC {pinID}')
        self.pinID = pinID
        self.pin = AnalogIn(_int_2_pin(pinID))
    
    def getValue(self):
        return True if self.pin.value > 0 else False
    
    def getAnalog(self):
        return self.pin.value

    def getPinID(self):
        return self.pinID
    
    def deInit(self):
        self.pin.deinit()
        
    
    
        