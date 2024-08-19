from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


def window():

    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(720, 720, 200, 200)
    win.setWindowTitle("Title")

    label = QtWidgets.QLabel(win)
    label.setText("Some text")
    label.move(50,50)


    win.show()
    sys.exit(app.exec())

window()