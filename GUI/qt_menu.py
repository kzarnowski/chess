from PyQt5.QtWidgets import QFrame, QVBoxLayout, QPushButton, QLabel, QApplication
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import sys

class QtMenu(QFrame):
    def __init__(self, parent):
        QFrame.__init__(self)
        self.parent = parent
        self.btn_text = {
            'game': 'New Game',
            'settings': 'Settings',
            'exit': 'Exit'
        }

        self.setContentsMargins(300, 200, 300, 100)
        layout = QVBoxLayout()
        title = QLabel()
        title_font = QFont()
        title_font.setPointSize(80)
        title_font.setBold(True)
        title.setFixedWidth(400)
        title.setFont(title_font)
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)
        layout.addWidget(QtMenuItemButton(self, 'game'))
        layout.addWidget(QtMenuItemButton(self, 'settings'))
        layout.addWidget(QtMenuItemButton(self, 'exit'))
        self.setLayout(layout)
    
    def game(self):
        self.parent.app.new_game(self.parent.qt_game)
        self.parent.stack.setCurrentWidget(self.parent.qt_game)

    def settings(self):
        self.parent.stack.setCurrentWidget(self.parent.qt_settings)
    
    def exit(self):
        QApplication.quit()
        sys.exit()

class QtMenuButton(QPushButton):
    def __init__(self, main_window):
        QPushButton.__init__(self)
        self.main_window = main_window
        self.setText('Menu')
        self.clicked.connect(self.btn_clicked)
        
    def btn_clicked(self):
        self.main_window.stack.setCurrentWidget(self.main_window.qt_menu)

class QtMenuItemButton(QPushButton):
    def __init__(self, qt_menu, func):
        QPushButton.__init__(self, qt_menu.btn_text[func])
        self.qt_menu = qt_menu
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.setFont(font)
        self.setFixedSize(400, 50)
        self.clicked.connect(getattr(qt_menu, func))