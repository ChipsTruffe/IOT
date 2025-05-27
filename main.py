from examplesensor import DHTSensor
from actuators.actuator import Actuator
#from simulation.environment import Environment
from thingsboard.client import ThingsBoardClient
import time


sensor = DHTSensor()

# Actuators
windows = Actuator("WindowMotor")
irrigation = Actuator("Irrigation")
humidifier = Actuator("Humidifier")
heater = Actuator("Heater")

#env = Environment(sensor, window, irrigation)
client = ThingsBoardClient()


def updateActuators():
    command = client.getCommand()
    match command:
        case "heating on":
            heater.powerOn()
        case "heating off":
            heater.powerOff()
        case "windows open":
            windows.powerOn()
        case "windows close":
            windows.powerOff()
        case "humidifier on":
            humidifier.powerOn()
        case "humidifier off":
            humidifier.powerOff()
        case "irrigation on":
            irrigation.powerOn()
        case "irrigation off":
            irrigation.powerOff()
        case "nothing":
            pass
        case _:
            print(f"Command '{command}' is not recognized")

while True:
    #env.update()  # Simule l'évolution du climat
    updateActuators()

    temp, humidity = sensor.read()
    deltaTemp = 0
    deltaHum = 0

    if windows.isOn:
        pass
    if humidifier.isOn:
        pass
    if heater.isOn:
        pass
    
    temp += deltaTemp
    humidity += deltaHum
        
    #client.publish(temp, humidity)
    time.sleep(5)
