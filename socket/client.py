import socket


HEADER = 64
PORT = 5050
#SERVER = "127.0.1.1"
#Automatically retrieves ip address
SERVER = socket.gethostbyname(socket.gethostname())
#print(SERVER)
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSSAGE = "!DISCONNECT"


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' '*(HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))


send("Hello World!")
send("Hello World!3")
send("Hello World!45")


send(DISCONNECT_MESSSAGE)