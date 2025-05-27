import random
from devices.actuator import Actuator
from devices.sensors import *
import dataset
from config import *


class Environment:
    def __init__(self, addr, port):
        self.tempSensor = temperatureSensor(addr, port)
        self.humSensor = humiditySensor(addr, port)

        self.windows = Actuator("WindowMotor")
        self.irrigation = Actuator("Irrigation")
        self.humidifier = Actuator("Humidifier")
        self.heater = Actuator("Heater")

        self.data = dataset.import_filter_data(DATASETPATH_THEO, 2024110600,2025020612, 73329001)
        self.time = 0 # en secondes

    def update(self, dt):
        self.time += dt # en secondes

        # Simulation simplifiée
        tempin = self.tempSensor.read()
        humin = self.humSensor.read()
        
        if self.window.isOn:
            tempin -= random.uniform(0.1, 0.5)
        else:
            tempin += random.uniform(0.1, 0.3)

        if self.irrigation.isOn:
            humin += random.uniform(0.5, 1.0)
        else:
            humin -= random.uniform(0.2, 0.5)

        tempext, humext = dataset.s_to_values(self.data, self.time , ["T", "U"] )
        humin += (humext - humin) * 0.01
        tempin += (tempext - tempin) * 0.01
        
        self.tempSensor.update(tempin)
        self.humSensor.update(humin)
