import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from random import choice

window_titles = ['My App',
                'My App',
                'Still My App',
                'Still My App',
                'What on earth',
                'What on earth',
                'This is surprising',
                'This is surprising',
                'Something went wrong'
                ]


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.N_times_clicked = 0
        self.setWindowTitle("My app")

        self.button = QPushButton("Press me")
        self.button.clicked.connect(self.clicked)
        self.windowTitleChanged.connect(self.title_changed)

        self.setCentralWidget(self.button)

    def clicked(self):
        print("clicked")
        new_title = choice(window_titles)
        print("setting title: %s" %new_title)
        self.setWindowTitle(new_title)
        # self.button.setText("You've already clicked on me")
        # self.button.setEnabled(False)

        # #change window title
        # self.setWindowTitle("One click and you're done")

    def title_changed(self, window_title):
        print("Window title changed: %s" %window_title)

        if window_title == "Something went wrong":
            self.button.setDisabled(True)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()