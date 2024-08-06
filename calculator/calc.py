import sys
from PyQt5.QtWidgets import (
                    QApplication, QMainWindow, QWidget,
                    QGridLayout, QLineEdit, QPushButton,
                    QVBoxLayout
                    )
from PyQt5.QtCore import Qt

Window_size = 235
display_height = 35
button_size = 40

class PyCalcWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.setFixedSize(Window_size, Window_size)
        centralWidget = QWidget(self)
        self.setCentralWidget(centralWidget)

        self.generalLayout = QVBoxLayout()
        centralWidget.setLayout(self.generalLayout)
        self._createDisplay()
        self._createButtons()
    
    def _createDisplay(self):
        self.display = QLineEdit()
        self.display.setFixedHeight(display_height)
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.display.setReadOnly(True)
        self.generalLayout.addWidget(self.display)
    
    def _createButtons(self):
        self.buttonMap = {}
        buttonsLayout = QGridLayout()
        keyBoard =  [
                        ["7", "8", "9", "/", "C"],
                        ["4", "5", "6", "*", "("],
                        ["1", "2", "3", "-", ")"],
                        ["0", "00", ".", "+", "="],               
                    ]                 
        for row, keys in enumerate(keyBoard):
            for col, key in enumerate(keys):
                self.buttonMap[key] = QPushButton(key)
                self.buttonMap[key].setFixedSize(button_size, button_size)
                buttonsLayout.addWidget(self.buttonMap[key], row, col)
        self.generalLayout.addLayout(buttonsLayout)

def main():
    pycalcapp = QApplication([])
    pycalcwindow = PyCalcWindow()

    pycalcwindow.show()
    sys.exit(pycalcapp.exec())


if __name__ == "__main__":
    main()