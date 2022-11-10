import sys

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        button = QPushButton("Press Me!")

        # Set the central widget of the Window.
        self.setCentralWidget(button)

    def keyPressEvent(self, event) -> None:
        key = event.key()

        if key == Qt.Key_P:
            print("P CLICKED")
        elif key == Qt.Key_X:
            print("X Clicked")
        elif key == Qt.Key_Left:
            print("Left")
        else:
            print("Other clicked")


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()