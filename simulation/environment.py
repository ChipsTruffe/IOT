import random
from devices.actuator import Actuator
from devices.sensors import *
from simulation.dataset import import_filter_data, s_to_values
from config import *


class Environment:
    def __init__(self):
        self.tempSensor = temperatureSensor()
        self.humSensor = humiditySensor()

        self.windows = Actuator("WindowMotor")
        self.irrigation = Actuator("Irrigation")
        self.humidifier = Actuator("Humidifier")
        self.heater = Actuator("Heater")

        self.data = import_filter_data(DATASETPATH_MALOE, 2024110600,2025020612, 73329001)
        self.time = 0 # en secondes

    def update(self, dt):
        self.time += dt # en secondes

        # Simulation
        ## Getting external and internal values
        tempin = float(self.tempSensor.read())
        humin = float(self.humSensor.read())
        tempext, humext = s_to_values(self.data, self.time , ["T", "U"] ) #ask for T,U, get back T,U

        

        exchange_coeff = 0.01 if self.windows.isOn else 0.001
        temp_exchange_term = (tempext - tempin) * exchange_coeff

        heat_term = 0.1 if self.heater.isOn else 0
        cold_term = -0.1 if self.humidifier.isOn else 0

        humidifier_term = 1 if self.humidifier.isOn else 0 
        humidity_exchange_term = 3 * exchange_coeff * (humext - humin) #facteur 3 arbitraire

        dT = (temp_exchange_term + heat_term + cold_term) * dt #temperature delta
        dU = (humidifier_term + humidity_exchange_term) * dt #humidity delta
        

        
        humin += dU
        tempin += dT
        
        self.tempSensor.update(tempin)
        self.humSensor.update(humin)
