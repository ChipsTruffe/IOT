#from sensors.dht_sensor import DHTSensor
from actuators.window import Window
from actuators.irrigation import Irrigation
#from simulation.environment import Environment
from thingsboard.client import ThingsBoardClient
import time

#sensor = DHTSensor()
window = Window()
irrigation = Irrigation()
#env = Environment(sensor, window, irrigation)
client = ThingsBoardClient()

while True:
    #env.update()  # Simule l'évolution du climat
    #temp, humidity = sensor.read()
    #window.control(temp, humidity)
    #irrigation.control(temp, humidity)
    #client.publish(temp, humidity)
    time.sleep(5)
