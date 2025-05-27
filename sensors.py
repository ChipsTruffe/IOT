import socket

LISTENING_PORT = 5000


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