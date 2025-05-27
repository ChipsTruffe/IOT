class DHTSensor:
    def __init__(self):
        self.temperature = 22
        self.humidity = 50

    def read(self):
        return self.temperature, self.humidity

    def update(self, temp, hum):
        self.temperature = temp
        self.humidity = hum
