import numpy as np
import pyqtgraph as pg
from PyQt5 import QtCore, QtWidgets



class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.plot_graph = pg.PlotWidget()
        self.setCentralWidget(self.plot_graph)
        self.plot_graph.setBackground("w")
        pen = pg.mkPen(color=(255, 0, 0))
        self.plot_graph.setTitle("Live Plot of Forward transmitted signal (q)", color="b", size="20pt")
        styles = {"color": "red", "font-size": "18px"}
        self.plot_graph.setLabel("left", "Data", **styles)
        self.plot_graph.setLabel("bottom", "Time (s)", **styles)
        self.plot_graph.addLegend()
        self.plot_graph.showGrid(x=True, y=True)
        #self.plot_graph.setYRange(-2100, 2100)
        self.times = np.linspace(0.0019, 0.0026, 16384)
        self.time = list(self.times[68:78])
        self.fwd_qs = np.load("D:\Pyqt5\Skeleton\Data\q_19.npy")
        self.fwd_q = self.fwd_qs[68:78].tolist()#list(self.fwd_qs[0:10])

        # Get a line reference
        self.line = self.plot_graph.plot(
            self.time,
            self.fwd_q,
            name="forward transmitted q",
            pen=pen,
            symbol="+",
            symbolSize=15,
            symbolBrush="b",
        )
        # Add a timer to simulate new temperature measurements
        self.i = 79
        self.timer = QtCore.QTimer()
        self.timer.setInterval(300)
        self.timer.timeout.connect(self.update_plot)
        self.timer.start()
        

    def update_plot(self):
        # for i in range(len(self.fwd_q[10:])):

        self.time = self.time[1:]
        self.time.append(self.times[self.i])
        self.fwd_q = self.fwd_q[1:]
        self.fwd_q.append(self.fwd_qs[self.i])
        self.line.setData(self.time, self.fwd_q)
        self.plot_graph.setYRange(-100+min(self.fwd_q), 100+max(self.fwd_q) )
        #print(self.i, self.fwd_qs[self.i])
        self.i+=1

app = QtWidgets.QApplication([])
main = MainWindow()
main.show()
app.exec()