import max30100 as m
import calculator as calc

class Device():

    __led_red_off = 0
    __led_ir_off = 20.8
    __activity = False

    def __init__(self,
                 led_red = 20.8,
                 led_ir = 20.8):
        self.__led_red_on = led_red
        self.__led_ir_on = led_ir
        self.disactivate()
        
    def activate(self):
        self.__device = m.MAX30100(led_current_red = self.__led_red_on, 
                                   led_current_ir = self.__led_ir_on)
        self.__device.enable_spo2()
        self.__activity = True

    def disactivate(self):
        self.__device = m.MAX30100(led_current_red = self.__led_red_off, 
                                   led_current_ir = self.__led_ir_off)
        self.__device.enable_spo2()
        self.__activity = False

    def update(self):
        self.__device.read_sensor()
        self.__device.red, self.__device.ir
        self._red = calc.getLastValue(self.__device.buffer_red)
        self._ir = calc.getLastValue(self.__device.buffer_ir)
        self._shO2 = calc.calculateShO2(self._red, self._ir)

    def getRed(self):
        return self._red

    def getIR(self):
        return self._ir

    def getShO2(self):
        return self._shO2

    def isFingerIn(self):
        if self._ir > 1000:
            return True
        return False

    def isActive(self):
        return self.__activity
        
        
        


    
