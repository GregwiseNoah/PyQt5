from pyqtgraph.Qt import QtGui, QtCore, QtWidgets
import temp_gui as gui
import sys
import pyqtgraph as pg
import collections
import random
import time
import math
import numpy as np

class DynamicPlotter:

    def __init__(self, plot, sampleinterval=0.1, timewindow=10., size=(600, 350)):
        # Data stuff
        self.interval = int(sampleinterval * 1000)
        self.bufsize = int(timewindow / sampleinterval)
        self.databuffer = collections.deque([0.0] * self.bufsize, self.bufsize)
        self.x = np.linspace(-timewindow, 0.0, self.bufsize)
        self.y = np.zeros(self.bufsize, dtype=float)
        
        # PyQtGraph stuff
        self.plt = plot
        self.plt.setTitle('EEG/ECG Live Plot')
        self.plt.resize(*size)
        self.plt.showGrid(x=True, y=True)
        #self.plt.setXRange(5,20, padding=0)
        self.plt.setLabel('left', 'Amplitude', 'uVrms')
        self.plt.setLabel('bottom', 'Time', 's')
        self.curve = self.plt.plot(self.x, self.y, pen=(255, 0, 0))

        # QTimer
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.updateplot)
        self.timer.start(self.interval)

    def getdata(self):
        frequency = 0.5
        noise = random.normalvariate(0., 1.)
        new = 10. * math.sin(time.time() * frequency * 2 * math.pi) + noise
        return new

    def updateplot(self):
        self.databuffer.append(self.getdata())
        self.y[:] = self.databuffer
        self.curve.setData(self.x, self.y)


class MainWindow(QtWidgets.QMainWindow, gui.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)
        self.setupUi(self)
        self.plots = []
        for plot in (self.ch1PlotWidget, self.ch2PlotWidget, self.ch3PlotWidget):
            self.plots.append(
                DynamicPlotter(plot, sampleinterval=0.05, timewindow=5.)
                )


if __name__ == "__main__":
    app = QtGui.QGuiApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
