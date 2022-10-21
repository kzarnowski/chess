from PyQt5.QtWidgets import QFrame, QVBoxLayout, QPushButton, QLabel
from GUI.qt_menu import QtMenuButton

class QtHelp(QFrame):
    def __init__(self, parent):
        QFrame.__init__(self)
        self.parent = parent

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Help"))
        layout.addWidget(QtMenuButton(self.parent))
        self.setLayout(layout)