from PyQt5 import QtWidgets
import pyqtgraph as pg
import numpy as np


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
    
        self.plot_graph = pg.PlotWidget()
        self.setCentralWidget(self.plot_graph)
        self.plot_graph.plot(np.linspace(-2,2,1000), 20*(np.cos(np.linspace(-200, 200, 1000))).real, pen = 'b')
        self.plot_graph.plot(np.linspace(-2,2,1000), np.fft.fft(np.cos(np.linspace(-200, 200, 1000))).real, pen = 'r')


app = QtWidgets.QApplication([])
main = MainWindow()
main.show()
app.exec()