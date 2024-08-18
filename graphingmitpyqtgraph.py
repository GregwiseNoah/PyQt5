from PyQt5 import QtWidgets, QtCore
import pyqtgraph as pg
import numpy as np


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        rand = 300*np.random.rand(100)

        self.plot_graph = pg.PlotWidget()
        self.plot_graph.addLegend()
        self.setCentralWidget(self.plot_graph)
        #self.plot_graph.setBackground("b")

        self.plot_graph.plot(np.linspace(-2,2, 100), rand, symbol = '+', symbolSize = 20, symbolBrush = "b", name = "random")
        pen = pg.mkPen(color = (255, 255 , 255), width = 2, style = QtCore.Qt.DashLine)
        self.plot_graph.plot(np.linspace(-2,2,1000), 300*(np.cos(np.linspace(-20, 20, 1000))).real, pen = pen, name = 'fft')
        self.plot_graph.plot(np.linspace(-2,2,1000), np.fft.fft(np.cos(np.linspace(-20, 20, 1000))).real, pen = 'b', name = "cosine")
        self.plot_graph.setTitle("linspace vs randomness")
        self.plot_graph.setLabel("left", "randomness")
        self.plot_graph.setLabel("bottom", "linspace")

app = QtWidgets.QApplication([])
main = MainWindow()
main.show()
app.exec()