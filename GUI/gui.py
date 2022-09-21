from PyQt5.QtWidgets import QMainWindow, QStackedWidget
from PyQt5.QtCore import QSize

from GUI.config import WINDOW_SIZE
from GUI.menu import QtMenu
from GUI.play import QtPlay
from GUI.settings import QtSettings
from GUI.help import QtHelp

class Gui(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.app = None
        self.setFixedSize(QSize(*WINDOW_SIZE))
        self.setWindowTitle('Chess')

        self.stack = QStackedWidget(self)

        self.menu = QtMenu(self)
        self.play = QtPlay(self)
        self.settings = QtSettings(self)
        self.help = QtHelp(self)

        self.stack.insertWidget(0, self.menu)
        self.stack.insertWidget(1, self.play)
        self.stack.insertWidget(2, self.settings)
        self.stack.insertWidget(3, self.help)

        self.stack.setCurrentWidget(self.menu)

        self.setCentralWidget(self.stack)
        self.show()