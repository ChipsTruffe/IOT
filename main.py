from simulation.environment import Environment
from thingsboard.client import ThingsBoardClient
import time
from config import *


dt = 3600 # in seconds
# WARNING : if dt is too high, the simulation overshoots and the values skyrockets 


client = ThingsBoardClient()
env = Environment()

def updateActuators(control):
    if control['window']:
        env.windows.powerOn()
    else:
        env.windows.powerOff()
    
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

    tempext = env.tempext
    humext = env.humext
    client.publish(temp, hum)
    client.publish_ext(tempext,humext)
    control = client.get_controls_state()
    updateActuators(control)

    time.sleep(5)
