import pyqtgraph as pg
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QTabWidget, QWidget, QGridLayout
from PyQt5.QtCore import Qt
import sys
import numpy as np

#temp
from PyQt5.QtGui import QPalette, QColor
from random import randint


WIDTH = 1080
HEIGHT= 720

##########################################################
#temp code
class Color(QWidget):

    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)

x = np.linspace(0, 3.14, 100)
y = np.sin(x)
##########################################################

class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("work in progress")

        main_layout = QGridLayout(self)
        self.setLayout(main_layout)

###################################################
        self.plot_graph = pg.PlotWidget()
        #self.setCentralWidget(self.plot_graph)
        pen = pg.mkPen(color=(255, 0, 0))
        self.time = list(range(10))
        self.temperature = [randint(20, 40) for _ in range(10)]
        # Get a line reference
        self.line1 = self.plot_graph.plot(
            self.time,
            self.temperature,
            name="Temperature Sensor",
            pen=pen,
            symbol="+",
            symbolSize=15,
            symbolBrush="b",
        )
        self.timer = QtCore.QTimer()
        self.timer.setInterval(300)
        self.timer.timeout.connect(self.update_plot)
        self.timer.start()        
###################################################
        tab = QTabWidget(self)
        self.iq(tab, self.plot_graph)
        self.fft(tab)
        self.para(tab)
        # widget = QWidget()
        # widget.setLayout(layout)
        # self.setCentralWidget(widget)

        main_layout.addWidget(tab, 0, 0, 2, 1)

    def iq(self, tab, plot_graph):
        #iq visualizations
        iq = QWidget(self)
        layout = QGridLayout()
        iq.setLayout(layout) 

        fwd_i = pg.PlotWidget()
        fwd_i.plot(x,y)
        
        fwd_q = pg.PlotWidget()
        fwd_q.plot(x,np.cos(x))
        
        fwd_x = pg.PlotWidget()
        fwd_x.plot(x[:50],[randint(0,100) for _ in range(50)])
        
        layout.addWidget(plot_graph, 0, 0)
        layout.addWidget(fwd_i, 0, 1)
        layout.addWidget(fwd_q, 1, 0)
        layout.addWidget(fwd_x, 1, 1)
        # layout.addWidget(Color('purple'), 3, 1)
        tab.addTab(iq, "I/Q Stream")

    def fft(self, tab):
        #fft
        fft = QWidget(self)
        layout = QGridLayout()
        fft.setLayout(layout)
        layout.addWidget(Color('red'), 0, 0)
        layout.addWidget(Color('green'), 1, 0)

        
        tab.addTab(fft, "Spectrum")
    
    def para(self, tab):
        para = QWidget(self)
        layout = QGridLayout()
        para.setLayout(layout)
        layout.addWidget(Color("blue"), 0, 0)
        layout.addWidget(Color("pink"), 0, 1)

        tab.addTab(para, "Parameters")
###################################################
    def update_plot(self):
        self.time = self.time[1:]
        self.time.append(self.time[-1] + 1)
        self.temperature = self.temperature[1:]
        self.temperature.append(randint(20, 40))
        self.line1.setData(self.time, self.temperature)    
###################################################                
    # def fwd(self, x, y):
    #     fwd_i = pg.PlotWidget()
    #     return fwd_i.plot(x,y)
    
    #self.fwd_i_plot = fwd_i.plot(x, y)
    # self.fwd_q = pg.PlotWidget()
    
    # self.trans_i = pg.PlotWidget()
    # self.trans_q = pg.PlotWidget()

    # self.angle_fwd = pg.PlotWidget()
    # self.angle_trans =  pg.PlotWidget()

    # self.phase_detuning = pg.PlotWidget()
    # self.PIsum= pg.PlotWidget() #Apparently PI_sum is a function

    # self.fft_trans = pg.PlotWidget()
    # self.fft_fwd = pg.PlotWidget()

# class stream(QWidget):

#     def __init__(self):
#         super(, self).__init__()

#     def fwd_i(self):
#         self.fwd_i = pg.PlotWidget()
        


def window():
    app = QApplication(sys.argv)
    win = MainWindow()
    win.resize(WIDTH, HEIGHT)
    win.show()
    sys.exit(app.exec())

window()