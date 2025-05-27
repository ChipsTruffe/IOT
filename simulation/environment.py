import random

class Environment:
    def __init__(self, sensor, window, irrigation):
        self.sensor = sensor
        self.window = window
        self.irrigation = irrigation

    def update(self):
        temp, hum = self.sensor.read()

        # Simulation simplifiée
        if self.window.open:
            temp -= random.uniform(0.1, 0.5)
        else:
            temp += random.uniform(0.1, 0.3)

        if self.irrigation.on:
            hum += random.uniform(0.5, 1.0)
        else:
            hum -= random.uniform(0.2, 0.5)

        self.sensor.update(round(temp, 1), round(hum, 1))
