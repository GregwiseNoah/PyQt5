import socket
import numpy as np
import struct
import os
import threading

HOST ='127.0.1.1' #socket.gethostbyname(socket.gethostname())
PORT = 5050
BUFFER_SIZE = 10240  # Adjust based on expected packet size

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_socket.bind((HOST, PORT))


def save_data_to_file(data, file_name='udp_received_data.npy'):
    np.save(file_name, data)  # Save data as NumPy array (binary format)

def udp_server():
    
    print(f"UDP server is listening on {HOST}:{PORT}")
    
    received_data = []

    try:
        while True:
            data, client_address = udp_socket.recvfrom(BUFFER_SIZE)

            print(data.decode())
            print(f"Received {len(data)} bytes from {client_address}")

            # num_floats = len(data) // 8  
            # float_data = struct.unpack(f'{num_floats}d', data)
            # print(f"Received data: {float_data}")
            
            # received_data.extend(float_data)
            #received_data.append(data)
            
            #save_data_to_file(np.array(received_data))
            save_data_to_file(np.array(data.decode()))
    
    except KeyboardInterrupt:
        print("\nServer is shutting down.")
    
    finally:
        udp_socket.close()
        print("UDP server closed.")

if __name__ == "__main__":
    t = threading.Thread(target = udp_server)
    t.start()
