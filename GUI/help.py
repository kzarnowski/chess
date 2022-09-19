from PyQt5.QtWidgets import QFrame, QVBoxLayout, QPushButton, QLabel
from GUI.menu import MenuButton

class Help(QFrame):
    def __init__(self, parent):
        QFrame.__init__(self)
        self.parent = parent

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Help"))
        layout.addWidget(MenuButton(self.parent))
        self.setLayout(layout)