import socketserver
import numpy as np
import queue
import threading
import time


# Queue
packet_queue = queue.Queue()

#Iteration for file name (have to find a better way to do this)
global iteration
iteration = 1

# Define the server address and port
SERVER_IP = '127.0.1.1'  # Localhost
SERVER_PORT = 5050      # Port to listen on

# Buffer size for receiving data 
BUFFER_SIZE = 1024

class MyUDPHandler(socketserver.BaseRequestHandler):
    
    def handle(self):
        # The data is available as self.request[0] and the client address as self.client_address
        data = self.request[0]  # Data received from the client
        socket = self.request[1]  

        #print(f"Received {len(data)} bytes from {self.client_address}")

        # Convert the received bytes back into a numpy array of float64 values
        received_data = np.frombuffer(data, dtype=np.float64)
        
        # Print or process the received data
        print(f"Received data: {received_data}")

        packet_queue.put(received_data)



def udp_start():
    with socketserver.UDPServer((SERVER_IP, SERVER_PORT), MyUDPHandler) as server:
        print(f"UDP server is listening on {SERVER_IP}:{SERVER_PORT}...")
    

        server.serve_forever()

#Function to process data
def data_processer():

    print(packet_queue)
    if not packet_queue.empty():


        raw = packet_queue.get()
        num_blocks = len(raw) // 8
        raw_reshaped = raw.reshape((num_blocks, 8))
    
        fwd_i = raw_reshaped[:, 0]
        fwd_q =  raw_reshaped[:, 1]
        trans_i = raw_reshaped[:, 2]
        trans_q = raw_reshaped[:, 3]
        angle_fwd = raw_reshaped[:, 4]
        angle_trans= raw_reshaped[:, 5]
        phase_detuning = raw_reshaped[:, 6]
        PI_sum = raw_reshaped[:, 7]

        np.save(f'fwd_i_{iteration}_{time.strftime("%H%M%S")}')
        print('processed')

        iteration += 1





udp_thread = threading.Thread(target = udp_start)
processor_thread = threading.Thread(target = data_processer)

udp_thread.start()
processor_thread.start()