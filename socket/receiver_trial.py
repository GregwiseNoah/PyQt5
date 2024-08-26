import socket
import threading

HEADER = 128

#have to find server ip and port 
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
#print(SERVER)
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[NEW CONNECTOIN] {addr} connected.")
    connected = True

    while connected:
        data = conn.recv(HEADER).decode(FORMAT)
        data.reshape((16,8)) #Most probably this will have to change once i know the type of data that is received, but this is an efficient
                            # way to split the incoming packet into 8 different streams
        for i in range(8):
            pass
            #QtWidget.update(data[i]) #fake code to send the stream to the gui, not happy that i have to rely on a for loop for this, still might be faster
        # if msg_length: 
        #     msg_length = int(msg_length)
        #     msg = conn.recv(msg_length).decode(FORMAT)
            # #Instead of using a disconnect message, just restart the application each time? No need to look at previous data/save it
            # if msg == DISCONNECT_MESSSAGE:
            #     connected = False
            # print(f"[{addr}]: {msg}")
            # conn.send("Message received".encode(FORMAT))
    conn.close()


def start():
    server.listen()
    print(f"[Listening Server is listening on {SERVER}]")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target = handle_client, args = (conn, addr))
        thread.start()
        #print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")

start()
