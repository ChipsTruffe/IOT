from simulation.environment import Environment
from thingsboard.client import ThingsBoardClient
import time
from config import *


dt = 10 # en secondes


client = ThingsBoardClient()
env = Environment()

def updateActuators(control):
    if control['window']:
        env.window.powerOn()
    else:
        env.window.powerOff()
    
    if control['heater']:
        env.heater.powerOn()
    else:
        env.heater.powerOff()

    if control['irrigation']:
        env.irrigation.powerOn()
    else:
        env.irrigation.powerOff()

    if control['humidifier']:
        env.humidifier.powerOn()
    else:
        env.humidifier.powerOff()
 

while True:
    env.update(dt)  # Simule l'évolution du climat
    temp = env.tempSensor.read()
    hum = env.humSensor.read()
    client.publish(temp, hum)
    control = client.get_controls_state()
    updateActuators(control)

    time.sleep(5)
