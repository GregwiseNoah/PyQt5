import pyqtgraph as pg
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QTabWidget, QWidget, QGridLayout, QPushButton, QLabel
from PyQt5.QtCore import Qt
import sys
import numpy as np
import scipy
import threading



pg.setConfigOption('background', 'w')
pg.setConfigOption('foreground', 'k')
##################################################
from PyQt5.QtGui import QPalette, QColor
from random import randint
##################################################


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
        self.plot_graph_fq = pg.PlotWidget()
        self.plot_graph_fi = pg.PlotWidget()
        self.plot_graph_tq = pg.PlotWidget()
        self.plot_graph_ti = pg.PlotWidget()
        self.plot_graph_fft_fwd = pg.PlotWidget()
        self.plot_graph_fft_trans = pg.PlotWidget()

        pen = pg.mkPen(color=(255, 0, 0))
        
        #Tab iq
        self.plot_graph_fq.setTitle("Forward signal (q)", color="b", size="20pt")
        self.plot_graph_fi.setTitle("Forward signal (i)", color="b", size="20pt")
        self.plot_graph_tq.setTitle("Transmitted signal (q)", color="b", size="20pt")
        self.plot_graph_ti.setTitle("Transmitted signal (i)", color="b", size="20pt")

        #Tab fft
        self.plot_graph_fft_fwd.setTitle("FFT of Forward signal", color="b", size="20pt")
        self.plot_graph_fft_trans.setTitle("FFt of Transmitted signal", color="b", size="20pt")
        
        styles = {"color": "red", "font-size": "18px"}

        self.plot_graph_fq.setLabel("left", "Amplitude", **styles)
        self.plot_graph_fq.setLabel("bottom", "Time (s)", **styles)
        self.plot_graph_fq.addLegend()
        self.plot_graph_fq.showGrid(x=True, y=True)
        self.plot_graph_fi.setLabel("left", "Amplitude", **styles)
        self.plot_graph_fi.setLabel("bottom", "Time (s)", **styles)
        self.plot_graph_fi.addLegend()
        self.plot_graph_fi.showGrid(x=True, y=True)
        self.plot_graph_tq.setLabel("left", "Amplitude", **styles)
        self.plot_graph_tq.setLabel("bottom", "Time (s)", **styles)
        self.plot_graph_tq.addLegend()
        self.plot_graph_tq.showGrid(x=True, y=True)
        self.plot_graph_ti.setLabel("left", "Amplitude", **styles)
        self.plot_graph_ti.setLabel("bottom", "Time (s)", **styles)
        self.plot_graph_ti.addLegend()
        self.plot_graph_ti.showGrid(x=True, y=True)

        self.plot_graph_fft_fwd.setLabel("left", "Amplitude", **styles)
        self.plot_graph_fft_fwd.setLabel("bottom", "Frequency", **styles)
        self.plot_graph_fft_fwd.addLegend()
        self.plot_graph_fft_fwd.showGrid(x=True, y=True)
        self.plot_graph_fft_trans.setLabel("left", "Amplitude", **styles)
        self.plot_graph_fft_trans.setLabel("bottom", "Frequency", **styles)
        self.plot_graph_fft_trans.addLegend()
        self.plot_graph_fft_trans.showGrid(x=True, y=True)

        #self.plot_graph_fq.setYRange(-2100, 2100)
        self.times = np.linspace(0.0019, 0.0026, 16384)
        self.time = list(self.times[68:78])
        # #Windows
        self.fwd_qs = np.load("D:\\Pyqt5\\Skeleton\\Data\\fwd_q_19.npy")
        self.fwd_is = np.load("D:\\Pyqt5\\Skeleton\\Data\\fwd_i_19.npy")
        self.trans_qs = np.load("D:\\Pyqt5\\Skeleton\\Data\\trans_q_19.npy")
        self.trans_is = np.load("D:\\Pyqt5\\Skeleton\\Data\\trans_i_19.npy")
        # Ubuntu
        # self.fwd_qs = np.load("/home/george/Documents/HZB/Pyqt5/PyQt5/Skeleton/Data/fwd_q_19.npy")
        # self.fwd_is = np.load("/home/george/Documents/HZB/Pyqt5/PyQt5/Skeleton/Data/fwd_i_19.npy")
        # self.trans_qs = np.load("/home/george/Documents/HZB/Pyqt5/PyQt5/Skeleton/Data/trans_q_19.npy")
        # self.trans_is = np.load("/home/george/Documents/HZB/Pyqt5/PyQt5/Skeleton/Data/trans_i_19.npy")

        self.fwd_q = self.fwd_qs[68:78].tolist()
        self.fwd_i = self.fwd_is[68:78].tolist()
        self.trans_q = self.trans_qs[68:78].tolist()
        self.trans_i = self.trans_is[68:78].tolist()

        ###### needs code here for defining fft
        self.fwd_r = self.fwd_qs*np.cos(2*np.pi*self.times + self.fwd_is*np.sin(2*np.pi*self.times))
        self.fft_fwd = scipy.fft.fft(self.fwd_r)
        self.freq_fwd = scipy.fft.fftfreq(np.size(self.times), 44.44e-6)

        self.trans_r = self.trans_qs*np.cos(2*np.pi*self.times + self.trans_is*np.sin(2*np.pi*self.times))
        self.fft_trans = scipy.fft.fft(self.trans_r)
        self.freq_fwd = scipy.fft.fftfreq(np.size(self.times), 44.44e-6)

        ######
        #print(self.freq_fwd, self.fft_fwd)

        #test plot with the inbuilt fft



        self.line_fft_fwd = self.plot_graph_fft_fwd.plot(
            self.freq_fwd,
            (abs(self.fft_fwd)),
            #name="forward transmitted q",
            pen=pg.mkPen('black', width = 2)#,
            # symbol="+",
            # symbolSize=15,
            # symbolBrush="black"
        ).setLogMode(False, True)

        self.line_fft_trans= self.plot_graph_fft_trans.plot(
            self.freq_fwd,
            abs(self.fft_trans),
            #name="forward transmitted q",
            pen=pg.mkPen('black', width = 2)#,
            # symbol="+",
            # symbolSize=15,
            # symbolBrush="black"
        ).setLogMode(False, True)

        # One way to do this, add all the elements of q and i now and then increment fwd_r and trans_r every time with the update function.


        '''
        Note to self, since fft is the most useful metric, it should be calculated on a packet basis and not sequentially
        '''

        self.line_fq = self.plot_graph_fq.plot(
            self.time,
            self.fwd_q,
            #name="forward transmitted q",
            pen=pen,
            symbol="+",
            symbolSize=15,
            symbolBrush="b"
        )

        #Just have to change i to q to combine the two plots, will do
        #later with better pens and separate code for clarity

        # It is now later and i don't know what i meant here.

        # okay got it, it means I can draw two plots on one graph if i use the same name
        self.line_fi = self.plot_graph_fi.plot(
            self.time,
            self.fwd_i,
            #name="forward transmitted i",
            pen=pen,
            symbol="+",
            symbolSize=15,
            symbolBrush="b"
        )

        self.line_ti = self.plot_graph_ti.plot(
            self.time,
            self.trans_i,
            #name="forward transmitted i",
            pen=pen,
            symbol="+",
            symbolSize=15,
            symbolBrush="b"
        )
        self.line_tq = self.plot_graph_tq.plot(
            self.time,
            self.trans_q,
            #name="forward transmitted i",
            pen=pen,
            symbol="+",
            symbolSize=15,
            symbolBrush="b"
        )
        # Add a timer to simulate new temperature measurements

        self.Timer = QLabel()

        self.i = 79
        self.timer = QtCore.QTimer()
        self.timer.setInterval(200)
        self.timer.timeout.connect(self.update_plot)
        self.timer.start()      

###################################################
        tab = QTabWidget(self)
        self.iq(tab, self.plot_graph_fq, self.plot_graph_fi , self.plot_graph_ti, self.plot_graph_tq, self.Timer)
        self.fft(tab,self.plot_graph_fft_fwd, self.plot_graph_fft_trans)
        self.para(tab)
        # widget = QWidget()
        # widget.setLayout(layout)
        # self.setCentralWidget(widget)

        main_layout.addWidget(tab, 0, 0, 2, 1)




    def iq(self, tab, plot_graph_fq, plot_graph_fi, plot_graph_ti, plot_graph_tq, Timer):


        #iq visualizations
        iq = QWidget(self)
        layout = QGridLayout()
        iq.setLayout(layout) 
        
        
        layout.addWidget(plot_graph_fq, 0, 0)
        layout.addWidget(plot_graph_fi, 0, 2)
        layout.addWidget(plot_graph_tq, 1, 0)
        layout.addWidget(plot_graph_ti, 1, 2)
        # layout.addWidget(Color('purple'), 3, 1)
        tab.addTab(iq, "I/Q Stream")

        #Time widget
        
        Timer.setText(f"Time = {self.times[self.i]:.5f}")
        layout.addWidget(Timer, 2, 1)

        #pause button
        self.button = QPushButton("Pause", self)
        layout.addWidget(self.button, 3, 1)
        self.button.setCheckable(True)
        #self.button.clicked.connect(self.toggle_pause)
        self.paused = True


    #The problem with this approach is that it doesn't make sense to just pause the plotting logic, but to freeze the plot and let the plotting
    #go on in the background so that the user always gets a live view of the plot.
    def toggle_pause(self):
        if self.button.isChecked():
            self.button.setText("Resume")

        else: 
            self.plot_graph_fq.setYRange(-100+min(self.fwd_q), 100+max(self.fwd_q) )
            self.plot_graph_fi.setYRange(-100+min(self.fwd_i), 100+max(self.fwd_i) )
            self.line_fq.setData(self.time, self.fwd_q)
            self.line_fi.setData(self.time, self.fwd_i)
            self.line_ti.setData(self.time, self.trans_i)
            self.line_tq.setData(self.time, self.trans_q)
            self.button.setText("Pause")

    def fft(self, tab, plot_graph_fft_fwd, plot_graph_fft_trans):

        fft = QWidget(self)
        layout = QGridLayout()
        fft.setLayout(layout)

        layout.addWidget(plot_graph_fft_fwd, 0, 0)
        layout.addWidget(plot_graph_fft_trans, 1, 0)

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
        self.time.append(self.times[self.i])
        self.fwd_q = self.fwd_q[1:]
        self.fwd_q.append(self.fwd_qs[self.i])
        
        self.fwd_i = self.fwd_i[1:]
        self.fwd_i.append(self.fwd_is[self.i])

        self.trans_q = self.trans_q[1:]
        self.trans_q.append(self.trans_qs[self.i])

        self.trans_i = self.trans_i[1:]
        self.trans_i.append(self.trans_is[self.i])
        
       
        #print(self.i, self.fwd_qs[self.i])
        self.i+=1  
        self.Timer.setText(f"Time = {self.times[self.i]:.7f}")

        self.toggle_pause()


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




''''
Actual fps calculation
0.0007 ms is the data I'm plotting right now.
This itself corresponds to 1428 fps to plot all the data in real time (1s)
With a delay of 150 ms or at 6fps, the time i will need to plot 16,384 points
                                                                is 2457 seconds
Wouldn't the data have to be extremely slowed downau to be readable in real time?
'''