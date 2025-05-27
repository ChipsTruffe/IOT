from actuator import Actuator

class WindowMotor(Actuator):
    def __init__(self, temperatureChange, humidityChange):
        super().__init__(temperatureChange, humidityChange)
    
