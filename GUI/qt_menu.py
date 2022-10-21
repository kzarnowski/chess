from PyQt5.QtWidgets import QFrame, QVBoxLayout, QPushButton, QLabel

class QtMenu(QFrame):
    def __init__(self, parent):
        QFrame.__init__(self)
        self.parent = parent
        game_btn = QPushButton("Game")
        game_btn.clicked.connect(self.game)
        settings_btn = QPushButton("Settings")
        settings_btn.clicked.connect(self.settings)
        help_btn = QPushButton("Help")
        help_btn.clicked.connect(self.help)
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Menu"))
        layout.addWidget(game_btn)
        layout.addWidget(settings_btn)
        layout.addWidget(help_btn)
        self.setLayout(layout)
    
    def game(self):
        self.parent.app.new_game(self.parent.qt_game)
        self.parent.stack.setCurrentWidget(self.parent.qt_game)

    def settings(self):
        self.parent.stack.setCurrentWidget(self.parent.qt_settings)

    def help(self):
        self.parent.stack.setCurrentWidget(self.parent.qt_help)

class QtMenuButton(QPushButton):
    def __init__(self, main_window):
        QPushButton.__init__(self)
        self.main_window = main_window
        self.setText('Menu')
        self.clicked.connect(self.btn_clicked)
        
    def btn_clicked(self):
        self.main_window.stack.setCurrentWidget(self.main_window.qt_menu)
        