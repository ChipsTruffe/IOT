from actuator import Actuator

class Humidifer(Actuator):
    def __init__(self, humidityChange):
        super.__init__(0, humidityChange)