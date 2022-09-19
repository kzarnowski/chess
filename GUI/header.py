from PyQt5.QtWidgets import QFrame, QHBoxLayout
from GUI.menu import MenuButton

class Header(QFrame):
    def __init__(self, parent):
        QFrame.__init__(self)
        self.parent = parent     
        layout = QHBoxLayout()
        layout.addWidget(MenuButton(self.parent.parent))
        self.setLayout(layout)