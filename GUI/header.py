from PyQt5.QtWidgets import QFrame, QHBoxLayout, QLabel
from GUI.menu import QtMenuButton

class QtHeader(QFrame):
    def __init__(self, parent):
        QFrame.__init__(self)
        self.parent = parent     
        self.info = QLabel("Info")
        layout = QHBoxLayout()
        layout.addWidget(QtMenuButton(self.parent.parent))
        layout.addWidget(self.info)
        self.setLayout(layout)