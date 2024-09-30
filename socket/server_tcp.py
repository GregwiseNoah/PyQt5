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
DISCONNECT_MESSSAGE = "!DISCONNECT"
#Steaming streaming data through IVP4
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[NEW CONNECTOIN] {addr} connected.")
    connected = True

    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length: 
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)

            if msg == DISCONNECT_MESSSAGE:
                connected = False
            print(f"[{addr}]: {msg}")
            conn.send("Message received".encode(FORMAT))
    conn.close()

    
def start():
    server.listen()
    print(f"[Listening Server is listening on {SERVER}]")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target = handle_client, args = (conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")



print("[STARTING]")
start()