class Actuator:
    def __init__(self, name):
        self.name = name
        self.isOn = False

    def powerOn(self):
        self.isOn = True
    
    def powerOff(self):
        self.isOn = False
    
