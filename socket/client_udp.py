import socket 
import threading 
#import random

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
localhost = socket.gethostbyname(socket.gethostname())
client.bind((localhost, 5052))
name = input("")

def receive():
    while True:
        try:
            message, _ = cliet.recvfrom(1024)
            print(message.decode)
        except:
            pass

t = threading.Thread(target=receive)
t.start()

client.sendto(f"SIGNUPTAG:{name}".encode(), (localhost, 9999))

while True:
    message = input("")
    if message == "q":
        exit()
    else:
        client.sendto(f"{name}: {message}".encode(), (localhost, 9999))