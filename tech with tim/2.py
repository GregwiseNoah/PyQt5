from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

def clicked():
    print("clicked")
   
def window():

    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(720, 720, 2000, 200)
    win.setWindowTitle("Title")

    label = QtWidgets.QLabel(win)
    label.setText("Some text")
    label.move(50,50)

    def update():
        label.setText("Yay you clicked the button, now im free")
        
    b1 = QtWidgets.QPushButton(win)
    b1.setText("Click me")
    b1.clicked.connect(clicked)
    b1.clicked.connect(update)



    win.show()
    sys.exit(app.exec())

window()