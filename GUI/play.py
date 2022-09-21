from PyQt5.QtWidgets import QFrame, QVBoxLayout, QHBoxLayout, QPushButton, QLabel
from GUI.sidebars.game_control import QtGameControlSidebar
from GUI.sidebars.notation import QtNotationSidebar
from GUI.board import QtBoard
from GUI.header import QtHeader

class QtPlay(QFrame):
    def __init__(self, parent):
        QFrame.__init__(self)
        self.parent = parent

        self.header = QtHeader(self)

        self.game_control = QtGameControlSidebar(self)
        self.board = QtBoard(self)
        self.notation = QtNotationSidebar(self)

        play_layout = QHBoxLayout()
        play_layout.addWidget(self.game_control, 1)
        play_layout.addWidget(self.board, 2)
        play_layout.addWidget(self.notation, 1)

        layout = QVBoxLayout()
        layout.addWidget(self.header, 1)
        layout.addLayout(play_layout, 23)
        self.setLayout(layout)