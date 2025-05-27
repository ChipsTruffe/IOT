import socket

LISTENING_PORT = 5000

class sensor():
    def __init__(self, type : str):
        self.temperature = 22
        self.humidity = 50
        self.type = type
    def read(self):
        if self.type == "temperature":
            return self.temperature
        elif self.type == "humidity":
            return self.humidity
    def update(self, data):
        if self.type == "temperature":
            self.temperature = data
        elif self.type == "humidity":
            self.humidity = data

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