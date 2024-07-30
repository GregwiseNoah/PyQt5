import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        button = QPushButton("press me")
        button.setCheckable(True)
        button.clicked.connect(self.the_button_was_clicked)
        button.clicked.connect(self.the_button_was_toggled)


        self.setCentralWidget(button)

    def the_button_was_clicked(self):
            print("Clicked")
    def the_button_was_toggled(self, checked):
         print("Checked?", checked)

    #Clicked allows you to perform an action, clicking, on the window. 
    #Toggle allows you to toggle the button like a switch between on and off.
    #You have two option, either using it as a checkable (setCheckable(True)) 
    #or using it in the toggle state(set by default)
    # you can use it in multiple ways at the same time.
    



app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
