import sys
from PyQt5.QtWidgets import (
        QApplication,
        QLabel,
        QMainWindow,
        QStatusBar,
        QToolBar,
)

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main window")
        self.setCentralWidget(QLabel("Central widget"))
        self._createMenu()
        self._createToolBar()
        self._createStatusBar()

    def _createMenu(self):
        menu = self.menuBar().addMenu("&Menu")
        menu.addAction("&Exit", self.close)

    def _createToolBar(self):
        tools = QToolBar()
        tools.addAction("Open", self.close)
        self.addToolBar(tools)
    
    def _createStatusBar(self):
        status = QStatusBar()
        status.showMessage("Ich bin status bar")
        self.setStatusBar(status)

if __name__ == "__main__":
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())

