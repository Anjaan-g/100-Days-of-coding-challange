import socket
import threading

HEADER = 64
PORT = 5050
# SERVER = "192.168.100.34" '''This is hardcoded for this computer'''
SERVER = socket.gethostbyname(socket.gethostname()) #This is dynamic and works on every computer.
ADDR = (SERVER,PORT)

#Type of addresses we're working with.
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        msg = conn.recv(HEADER)

def start():
    server.listen()
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS]{threading.activeCount()-1}")

print("[STARTING] server is starting...")
start()