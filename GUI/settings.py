from PyQt5.QtWidgets import QFrame, QVBoxLayout, QPushButton, QLabel
from GUI.menu import MenuButton
from GUI.header import Header

class Settings(QFrame):
    def __init__(self, parent):
        QFrame.__init__(self)
        self.parent = parent
        self.header = Header(self)

        settings_layout = QVBoxLayout()
        settings_layout.addWidget(QLabel("Help"))

        layout = QVBoxLayout()
        layout.addWidget(self.header, 1)
        layout.addLayout(settings_layout, 23)
        self.setLayout(layout)