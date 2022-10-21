from PyQt5.QtWidgets import QFrame, QVBoxLayout, QPushButton, QLabel
from GUI.qt_menu import QtMenuButton
from GUI.qt_header import QtHeader

class QtSettings(QFrame):
    def __init__(self, parent):
        QFrame.__init__(self)
        self.parent = parent
        self.header = QtHeader(self)

        settings_layout = QVBoxLayout()
        settings_layout.addWidget(QLabel("Help"))

        layout = QVBoxLayout()
        layout.addWidget(self.header, 1)
        layout.addLayout(settings_layout, 23)
        self.setLayout(layout)