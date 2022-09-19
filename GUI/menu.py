from PyQt5.QtWidgets import QFrame, QVBoxLayout, QPushButton, QLabel

class Menu(QFrame):
    def __init__(self, parent):
        QFrame.__init__(self)
        self.parent = parent
        play_btn = QPushButton("Play")
        play_btn.clicked.connect(self.play)
        settings_btn = QPushButton("Settings")
        settings_btn.clicked.connect(self.settings)
        help_btn = QPushButton("Help")
        help_btn.clicked.connect(self.help)
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Menu"))
        layout.addWidget(play_btn)
        layout.addWidget(settings_btn)
        layout.addWidget(help_btn)
        self.setLayout(layout)
    
    def play(self):
        self.parent.stack.setCurrentWidget(self.parent.play)

    def settings(self):
        self.parent.stack.setCurrentWidget(self.parent.settings)

    def help(self):
        self.parent.stack.setCurrentWidget(self.parent.help)

class MenuButton(QPushButton):
    def __init__(self, main_window):
        QPushButton.__init__(self)
        self.main_window = main_window
        self.setText('Menu')
        self.clicked.connect(self.btn_clicked)
        
    def btn_clicked(self):
        self.main_window.stack.setCurrentWidget(self.main_window.menu)
        