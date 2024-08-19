import sys
import os
import socket
from PyQt5 import QtCore, QtWidgets
#import pyqtgraph as pg


# UDP_IP = ""
# UDP_Port = 0

# sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# sock.bind((UDP_IP, UDP_Port))

# while True:
#     data, addr = sock.recvfrom(128)
#     print("received data = %s" % data)

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.UI()

    #This is where code for plotting needs to be added
    def UI(self):
        self.setWindowTitle("Visualiser")

        #Mainwindow
        self.main_widget = QWidget(self)
        self.setCentralWidget(self.main_widget)
        layout = QVBoxLayout(self.main_widget)

        
        layout.addWidget(self.plot_widget)

    self.plot_graph = pg.PlotWidget()