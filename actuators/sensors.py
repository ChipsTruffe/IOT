import socket
import dataset

LISTENING_PORT = 5000

class sensor():
    def __init__(self, type : str):
        self.temperature = 22
        self.humidity = 50
        self.type = type
class temperatureSensor(sensor):
    def read(self):
        return self.temperature
    def update(self, newTemp):
        self.temperature = newTemp
class humiditySensor(sensor):
    def read(self):
        return self.humidity
    def update(self,newHum):
        self.humidity = newHum 

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("127.0.0.1", LISTENING_PORT))
    s.listen()
    print(f"Listening on {LISTENING_PORT}")

    conn, addr = s.accept()
    with conn:
        print(f"Connected with {addr}")
        while True:
            data = conn.recv(1024)
            if data:
                print(data.decode())
    s.close()

        

main()