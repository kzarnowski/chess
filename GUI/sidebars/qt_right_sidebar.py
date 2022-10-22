from PyQt5.QtWidgets import QFrame, QVBoxLayout, QLabel, QTextEdit

class QtRightSidebar(QFrame):
    def __init__(self, parent):
        QFrame.__init__(self)
        self.parent = parent

        layout = QVBoxLayout()
        layout.addWidget(QLabel('Right Sidebar'))
        self.setLayout(layout)

        self.notation = QTextEdit()
        self.notation.setReadOnly(True)

        layout.addWidget(self.notation)
