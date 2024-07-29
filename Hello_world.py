from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow
import sys

#QApplication instance for each application

app = QApplication(sys.argv) #sys.argv is to pass command line 
#arguments to the application. Instead you can put an empty list.

# window = QWidget()
# window.show() #Windows are hidden by default

# window = QPushButton("Click on me")
# window.show()

window = QMainWindow()
window.show()

app.exec()


#code after is only run after app is closed

print("Hello World")