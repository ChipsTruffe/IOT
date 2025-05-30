import random
from math import e
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

        self.data = import_filter_data(DATASETPATH_MALOE, 2024060611,2025020612, 73329001)
        self.time = 0 # en secondes

##MODIFICATION (A VOIR)############################################
        self.humext = 0
        self.tempext = 0
##FIN MODIFICATION#################################################

    def update(self, dt):
        self.time += dt # en secondes

        # Simulation
        ## Getting external and internal values
        tempin = float(self.tempSensor.read())
        humin = float(self.humSensor.read())
        self.tempext, self.humext = s_to_values(self.data, self.time , ["T", "U"] ) #ask for T,U, get back T,U

        

        T_exchange_coeff = (10 if self.windows.isOn else 3) * 1000 # transfer coeff * surface area
        T_capacitance = 5 * 10**5 #found online

        U_exchange_coeff = (20 if self.windows.isOn else 1) * 1000  # transfer coeff * surface area
        U_capacitance = 5 * 10**5 #to tweak

        heater_term = 30000 if self.heater.isOn else 0 #to tweak
        humidifier_term = 5000 if self.humidifier.isOn else 0 #to tweak

        target_U = self.humext + (humidifier_term) / U_exchange_coeff
        U_tau = U_capacitance / U_exchange_coeff
        
        target_T = self.tempext +  (heater_term - humidifier_term) / T_exchange_coeff
        T_tau = T_capacitance / T_exchange_coeff #caracteristic time   


        tempin = target_T + (tempin - target_T)*e**(-dt / T_tau)
        humin = target_U + (humin - target_U)*e**(-dt / U_tau)

        
        self.tempSensor.update(tempin)
        self.humSensor.update(humin)
