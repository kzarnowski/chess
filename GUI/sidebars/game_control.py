from PyQt5.QtWidgets import QFrame, QVBoxLayout, QLabel

class QtGameControlSidebar(QFrame):
    def __init__(self, parent):
        QFrame.__init__(self)
        self.parent = parent

        layout = QVBoxLayout()
        layout.addWidget(QLabel('GameControl'))
        self.setLayout(layout)