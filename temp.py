import sys
import numpy as np
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QApplication
import pyqtgraph as pg
from PIL import Image


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        grid = QGridLayout()
        self.setLayout(grid)
        self.Imv = pg.ImageView()
        win = pg.PlotWidget()
        win.plot(np.random.random_sample(40)*10)
        btn1 = QPushButton("Start")
        btn2 = QPushButton('Forward/backward')
        btn3 = QPushButton('Filters')
        grid.addWidget(self.Imv, 0, 0, 1, 1)
        grid.addWidget(win, 0, 1, 1, 1)
        grid.addWidget(btn1, 1, 0, 1, 1)
        grid.addWidget(btn2, 2, 0, 1, 1)
        grid.addWidget(btn3, 3, 0, 1, 1)
        btn1.clicked.connect(self.cap)
        self.move(300, 150)
        self.setWindowTitle('Scentific camera view')
        self.show()

    def cap(self):
        global Imv
        img = np.array(Image.open('D:/Frames/image7.jpg'))
        self.Imv.setImage(img.T)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())