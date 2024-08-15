import numexpr as ne
import sys
from PyQt5.QtWidgets import (
                    QApplication, QMainWindow, QWidget,
                    QGridLayout, QLineEdit, QPushButton,
                    QVBoxLayout
                    )
from PyQt5.QtCore import Qt
from functools import partial

Window_size = 235
display_height = 35
button_size = 40

error_message = "Error"

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

    def setDisplayText(self, text):
        self,display.setText(text)
        self.display.setFcous()
    
    def displayText(self):
        return self.display.text()
    def clearDisplay(self):
        self.setDisplayText("")

def evaluateExpressin(expression):
    try:
        result = str(ne.evaluate(expression, {}, {}))
    except Exception:
        result = error_message
    return result


class PyCalc:
    def __init__(self, model, view):
        self._evaluate = model
        self._view = view
        self._connectSignalsAndSlots()

    def _calculateResult(self):
        result = self._evaluate(expression = self._view.displayText())
        self._view.setDisplayText(result)
    
    def _buildExpression(self, subExpression):
        if self._view.displayText() == error_message:
            self._view.clearDisplay()
        expression = self._view.displayText() + subExpression
        self._view.setDisplayText(expression)
    
    def _connectSignalAndSlots(self):
        for keySymbol, button in self._view.buttonMap.items()
        


def main():
    pycalcapp = QApplication([])
    pycalcwindow = PyCalcWindow()

    pycalcwindow.show()
    sys.exit(pycalcapp.exec())


if __name__ == "__main__":
    main()