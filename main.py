from simulation.environment import Environment
from thingsboard.client import ThingsBoardClient
import time
from config import *


"""
    def updateActuators(command):
        match command:
            case "heating on":
                self.heater.powerOn()
            case "heating off":
                self.heater.powerOff()
            case "windows open":
                self.windows.powerOn()
            case "windows close":
                self.windows.powerOff()
            case "humidifier on":
                self.humidifier.powerOn()
            case "humidifier off":
                self.humidifier.powerOff()
            case "irrigation on":
                self.irrigation.powerOn()
            case "irrigation off":
                self.irrigation.powerOff()
            case "nothing":
                pass
            case _:
                print(f"Command '{command}' is not recognized")"""


dt = 10 # en secondes


client = ThingsBoardClient()
env = Environment(CLIENT_ADDR, CLIENT_PORT)

while True:
    env.update(dt)  # Simule l'évolution du climat

    #client.publish(temp, humidity)
    time.sleep(5)
