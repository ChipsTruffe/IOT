import socket
import numpy as np

SENDING_PORT = 5000

# receive a command from the Thingsboard server
def getCommandFromServer():
    return "nothing"

# send the temperature to captor sensor (socket s)
def sendTemperature(s, temp_to_send):
    payload = str(temp_to_send) + '\n'
    s.sendall(payload.encode())


def main():
    # Connect to temperature sensor
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("127.0.0.1", SENDING_PORT))

    time_step = 5 # in seconds
    size = int(24 * 60 * 60 / time_step) # number of time steps in a day
    temperature_real = np.random.randint(0, 40, size)
    temperature_adjusted = 0.0
    
    # actuators
    heating_on = False
    windows_open = False
    
    for dt in range(size):
        current_temp = temperature_real[dt]
        command = getCommandFromServer()
        match command:
            case "heating on":
                heating_on = True
            case "heating off":
                heating_on = False
            case "windows open":
                windows_open = True
            case "windows close":
                windows_open = False
            case "nothing":
                pass
            case _:
                print(f"Command '{command}' is not recognized")
        sendTemperature(s, current_temp)
    s.close()

main()