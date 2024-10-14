import socket
import numpy as np
import time
 # Server details (IP and Port)
SERVER_IP = '127.0.1.1'  # Localhost (change to actual IP if needed)
SERVER_PORT = 5050      # Port of the UDP server
MAX_PACKET_SIZE = 1024   # Set the packet size to exactly 1024 bytes
# Create a UDP socket
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Generate a random array of data that is exactly 1024 bytes long
# Since each double (float64) is 8 bytes, we need 1024 / 8 = 128 double-precision floats
data_to_send = np.random.rand(128).astype(np.float64)
print(data_to_send)
# Convert the numeric data to bytes
data_in_bytes = data_to_send.tobytes()
# Send the data in a single packet (since it is exactly 1024 bytes)
udp_socket.sendto(data_in_bytes, (SERVER_IP, SERVER_PORT))

# Close the UDP socket after sending the data
udp_socket.close()


print('Random data (1024 bytes) has been sent over UDP.')
