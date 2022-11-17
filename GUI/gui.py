from PyQt5.QtWidgets import QMainWindow, QStackedWidget, QApplication
from PyQt5.QtCore import QSize, QThreadPool

from GUI.qt_menu import QtMenu
from GUI.qt_game import QtGame
from GUI.qt_settings import QtSettings
from GUI.qt_help import QtHelp

WINDOW_SIZE = (1000, 800)

class Gui(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.app = None
        self.setFixedSize(QSize(*WINDOW_SIZE))
        self.setWindowTitle('Chess')

        # Init gui settings
        self.theme = 'classic'
        self.setStyleSheet('QtMenu, QtHelp, QtGame, QtSettings {background-image : url(images/background.jpg);}')
        self.stack = QStackedWidget(self)

        self.qt_menu = QtMenu(self)
        self.qt_game = QtGame(self)
        self.qt_settings = QtSettings(self)

        self.stack.insertWidget(0, self.qt_menu)
        self.stack.insertWidget(1, self.qt_game)
        self.stack.insertWidget(2, self.qt_settings)
        # self.stack.insertWidget(3, self.qt_help)

        self.stack.setCurrentWidget(self.qt_menu)
        self.setCentralWidget(self.stack)
        self.center()
        self.show()

    def center(self):
        frame_geometry = self.frameGeometry()
        active_screen = QApplication.desktop().screenNumber(
            QApplication.desktop().cursor().pos())
        center_point = QApplication.desktop().screenGeometry(active_screen).center()
        frame_geometry.moveCenter(center_point)
        self.move(frame_geometry.topLeft())

    

    