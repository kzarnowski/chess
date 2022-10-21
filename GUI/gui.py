from PyQt5.QtWidgets import QMainWindow, QStackedWidget
from PyQt5.QtCore import QSize

from GUI.config import WINDOW_SIZE
from GUI.qt_menu import QtMenu
from GUI.qt_game import QtGame
from GUI.qt_settings import QtSettings
from GUI.qt_help import QtHelp

class Gui(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.app = None
        self.setFixedSize(QSize(*WINDOW_SIZE))
        self.setWindowTitle('Chess')

        self.stack = QStackedWidget(self)

        self.qt_menu = QtMenu(self)
        self.qt_game = QtGame(self)
        self.qt_settings = QtSettings(self)
        self.qt_help = QtHelp(self)

        self.stack.insertWidget(0, self.qt_menu)
        self.stack.insertWidget(1, self.qt_game)
        self.stack.insertWidget(2, self.qt_settings)
        self.stack.insertWidget(3, self.qt_help)

        self.stack.setCurrentWidget(self.qt_menu)

        self.setCentralWidget(self.stack)
        self.show()