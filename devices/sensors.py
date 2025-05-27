import socket


class Sensor():
    def __init__(self):
        self.temperature = 22
        self.humidity = 50

        #self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #self.s.connect(("addr", port))
        #print(f"[INFO] Sensor connected to server")
    


class temperatureSensor(Sensor):
    def read(self):
        return self.temperature
    
    def update(self, newTemp):
        self.temperature = newTemp
        #payload = f"temperature:{self.temperature}".encode()
        #self.s.sendall(payload)

class humiditySensor(Sensor):
    def read(self):
        return self.humidity
    
    def update(self,newHum):
        self.humidity = newHum
        #payload = f"humidity:{self.humidity}".encode()
        #self.s.sendall(payload)
