import socket
import threading

HEADER = 64
PORT = 5050
#SERVER = "127.0.1.1"
#Automatically retrieves ip address
SERVER = socket.gethostbyname(socket.gethostname())
#print(SERVER)
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'

#Steaming streaming data through IVP4
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[NEW CONNECTOIN] {addr} connected.")
    connected = True

    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        msg_length = int(msg_length)
        msg = conn.recv(msg_length).decode(FORMAT)
        print(f"[{addr}]: {msg}")

    
def start():
    server.listen()
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target = handle_client, args = (conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")



print("[STARTING]")
start()