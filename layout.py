import board
from jvm.base.utils.print_utils import printb

_BOARD = "METROESP32S2"

def _int_2_pin(pin_id):
    if _BOARD == "PIPICO":
        return _pipico(pin_id)
    elif _BOARD == "FRP2040":
        return _frp2040(pin_id)
    elif _BOARD == "METROESP32S3":
        return _metroesp32s3(pin_id)
    elif _BOARD == "METROESP32S2":
        return _metroesp32s2(pin_id)
    else:
        printb("Board not supported")
        raise Exception("Board not supported")
    
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

def _metroesp32s3(pin_id):
    if pin_id == 1:
        _pin = board.A5
    elif pin_id == 2:
        _pin = board.D2
    elif pin_id == 3:
        _pin = board.D3
    elif pin_id == 4:
        _pin = board.D4
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
        _pin = board.A0
    elif pin_id == 15:
        _pin = board.A1
    elif pin_id == 16:
        _pin = board.A2
    elif pin_id == 17:
        _pin = board.A3
    elif pin_id == 18:
        _pin = board.A4
    elif pin_id == 21:
        _pin = board.MISO
    elif pin_id == 39:
        _pin = board.SCK
    elif pin_id == 40:
        _pin = board.TX
    elif pin_id == 41:
        _pin = board.RX
    elif pin_id == 42:
        _pin = board.MOSI
    elif pin_id == 43:
        _pin = board.DEBUG_TX
    elif pin_id == 44:
        _pin = board.DEBUG_RX
    elif pin_id == 45:
        _pin = board.SD_CS
    elif pin_id == 46:
        _pin = board.NEOPIXEL
    elif pin_id == 47:
        _pin = board.SDA
    elif pin_id == 48:
        _pin = board.SCL
    else:
        print("That Pin Does not exist!")
    return _pin

def _metroesp32s2(pin_id):
    if pin_id == 1:
        _pin = board.A2
    elif pin_id == 2:
        _pin = board.A3
    elif pin_id == 3:
        _pin = board.A4
    elif pin_id == 4:
        _pin = board.A5
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
        _pin = board.A0
    elif pin_id == 18:
        _pin = board.A1
    elif pin_id == 21:
        _pin = board.D21
    elif pin_id == 33:
        _pin = board.SDA
    elif pin_id == 34:
        _pin = board.SCL
    elif pin_id == 35:
        _pin = board.MOSI
    elif pin_id == 36:
        _pin = board.SCK
    elif pin_id == 37:
        _pin = board.MISO
    elif pin_id == 38:
        _pin = board.DEBUG_RX
    elif pin_id == 45:
        _pin = board.NEOPIXEL
    else:
        print("That Pin Does not exist!")
    return _pin
    
