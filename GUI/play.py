from PyQt5.QtWidgets import QFrame, QVBoxLayout, QHBoxLayout, QPushButton, QLabel
from GUI.sidebars.game_control import GameControlSidebar
from GUI.sidebars.notation import NotationSidebar
from GUI.board import Board
from GUI.header import Header

class Play(QFrame):
    def __init__(self, parent):
        QFrame.__init__(self)
        self.parent = parent

        self.header = Header(self)

        self.game_control = GameControlSidebar(self)
        self.board = Board(self)
        self.notation = NotationSidebar(self)

        play_layout = QHBoxLayout()
        play_layout.addWidget(self.game_control, 1)
        play_layout.addWidget(self.board, 2)
        play_layout.addWidget(self.notation, 1)

        layout = QVBoxLayout()
        layout.addWidget(self.header, 1)
        layout.addLayout(play_layout, 23)
        self.setLayout(layout)