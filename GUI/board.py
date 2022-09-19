from PyQt5.QtWidgets import QFrame, QVBoxLayout, QLabel

class Board(QFrame):
    def __init__(self, parent):
        QFrame.__init__(self)
        self.parent = parent

        layout = QVBoxLayout()
        layout.addWidget(QLabel('Board'))
        self.setLayout(layout)