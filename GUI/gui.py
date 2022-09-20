from PyQt5.QtWidgets import QMainWindow, QStackedWidget
from PyQt5.QtCore import QSize

from GUI.config import WINDOW_SIZE
from GUI.menu import Menu
from GUI.play import Play
from GUI.settings import Settings
from GUI.help import Help

class Gui(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.app = None
        self.setFixedSize(QSize(*WINDOW_SIZE))
        self.setWindowTitle('Chess')

        self.stack = QStackedWidget(self)

        self.menu = Menu(self)
        self.play = Play(self)
        self.settings = Settings(self)
        self.help = Help(self)

        self.stack.insertWidget(0, self.menu)
        self.stack.insertWidget(1, self.play)
        self.stack.insertWidget(2, self.settings)
        self.stack.insertWidget(3, self.help)

        self.stack.setCurrentWidget(self.menu)

        self.setCentralWidget(self.stack)
        self.show()