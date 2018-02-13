from OmegaExpansion import oledExp
import time

class Monitor():

    _status = 1

    def __init__(self):
        self._status = oledExp.driverInit()

    def write(self, text):
        self._status = oledExp.setCursor(3, 0)
        self._status = oledExp.write(text)

    def time(self):
        self.write(time.strftime("        %H:%M        "))

    def isIn(self):
        if self._status == 0:
            return True
        else:
            return False
    
