from actuator import Actuator

class Heater(Actuator):
    def __init__(self, tempChange):
        super.__init__(tempChange, 0)