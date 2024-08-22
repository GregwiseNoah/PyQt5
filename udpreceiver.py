import sys
import socket
import numpy as np
import pyqtgraph as pg
from scipy.fft import fft
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget

class FFTVisualizer(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.initUI()
        self.initUDP()
    
    def initUI(self):
        self.setWindowTitle('UDP FFT Visualizer')
        
        # Set up the main widget
        self.main_widget = QWidget(self)
        self.setCentralWidget(self.main_widget)
        layout = QVBoxLayout(self.main_widget)
        
        # Set up the plot widget
        self.plot_widget = pg.PlotWidget()
        layout.addWidget(self.plot_widget)
        
        # Plot settings
        self.plot = self.plot_widget.plot(pen='y')
        self.plot_widget.setYRange(0, 100, padding=0.1)
        self.plot_widget.setXRange(0, 64, padding=0.1)
        
        self.show()

    def initUDP(self):
        self.udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.udp_socket.bind(('0.0.0.0', 12345))  # Listen on all interfaces, port 12345
        self.udp_socket.settimeout(0.1)  # Set a timeout to avoid blocking
        
        # Start the timer for receiving and processing data
        self.timer = pg.QtCore.QTimer()
        self.timer.timeout.connect(self.update_plot)
        self.timer.start(100)  # Update every 100 ms

    def update_plot(self):
        try:
            # Receive the UDP packet
            data, _ = self.udp_socket.recvfrom(16)  # 16 bytes = 128 bits
            
            # Convert data to numpy array of floats
            data = np.frombuffer(data, dtype=np.uint8).astype(np.float32)
            
            # Perform FFT
            fft_result = np.abs(fft(data))[:64]  # Take first 64 components
            
            # Update plot
            self.plot.setData(fft_result)
        
        except socket.timeout:
            pass  # If no data is received, just skip the update

def main():
    app = QApplication(sys.argv)
    visualizer = FFTVisualizer()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
