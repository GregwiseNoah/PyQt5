import sys
import matplotlib
matplotlib.use("Qt5Agg")

from PyQt5 import QtCore, QtWidgets

from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure
import numpy as np

class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent = None, width =5, height = 4, dpi = 100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        sc = MplCanvas(self, width=5, height=4, dpi=100)
        sc.axes.plot(np.linspace(-5,5 ,100), np.sin(np.linspace(-5, 5, 100)))
        self.setCentralWidget(sc)

        self. show()

app = QtWidgets.QApplication(sys.argv)
w = MainWindow()
app.exec()