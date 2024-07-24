import digitalio
import board


class GPIO:
    def __init__(self):

        self.pins = {}

    def write(self, pin_id, value):
        pin = None
        try:
            pin = self.pins[pin_id]
        except:
            if pin_id == 13:
                _pin = board.D13
            else:
                print("That Pin Does not exist!")
        
            _pin = digitalio.DigitalInOut(_pin)
            _pin.direction = digitalio.Direction.OUTPUT
            self.pins[pin_id] = _pin
            pin = _pin
        
        pin.value = bool(value)
