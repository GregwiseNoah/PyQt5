#import pyqtgraph as pg
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QTabWidget, QWidget, QGridLayout
from PyQt5.QtCore import Qt
import sys

#temp
from PyQt5.QtGui import QPalette, QColor


#temp code
class Color(QWidget):

    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("work in progress")

        #main_layout = QGridLayout(self)
        #self.setLayout(main_layout)

        tab = QTabWidget(self)
        self.base(tab)
        self.fft(tab)
        # widget = QWidget()
        # widget.setLayout(layout)
        # self.setCentralWidget(widget)
    def base(self, tab):
        #base visualizations
        base = QWidget(self)
        layout = QGridLayout()
        base.setLayout(layout) 

        layout.addWidget(Color('red'), 0, 0)
        layout.addWidget(Color('green'), 1, 0)
        layout.addWidget(Color('blue'), 1, 1)
        layout.addWidget(Color('blue'), 2, 1)
        layout.addWidget(Color('purple'), 3, 1)

        tab.addTab(base, "Base visualizations")

    def fft(self, tab):
        #fft
        fft = QWidget(self)
        layout = QGridLayout()
        fft.setLayout(layout)
        layout.addWidget(Color('red'), 0, 0)
        layout.addWidget(Color('green'), 1, 0)

        
        tab.addTab(fft, "FFT visualizations")




    # self.fwd_i = pg.PlotWidget()
    # self.fwd_q = pg.PlotWidget()
    
    # self.trans_i = pg.PlotWidget()
    # self.trans_q = pg.PlotWidget()

    # self.angle_fwd = pg.PlotWidget()
    # self.angle_trans =  pg.PlotWidget()

    # self.phase_detuning = pg.PlotWidget()
    # self.PIsum= pg.PlotWidget() #Apparently PI_sum is a function

    # self.fft_trans = pg.PlotWidget()
    # self.fft_fwd = pg.PlotWidget()


def window():
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())

window()