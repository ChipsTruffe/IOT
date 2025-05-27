class Actuator:
    def __init__(self, temperatureChange, humidityChange):
        self.isOn = False
        self.tempChange = temperatureChange
        self.humidityChange = humidityChange

    def powerOn(self):
        self.isOn = True
    
    def powerOff(self):
        self.isOn = False

    def action(self, temperature, humidity):
        return (temperature+self.tempChange, humidity+self.humidityChange)