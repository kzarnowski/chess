from PyQt5.QtWidgets import QFrame, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QRadioButton, QButtonGroup, QCheckBox
from PyQt5.QtGui import QFont

class QtSettings(QFrame):
    def __init__(self, parent):
        QFrame.__init__(self)
        self.parent = parent

        layout = QVBoxLayout()
        self.setLayout(layout)

        dashboard = QHBoxLayout()
        buttons = QHBoxLayout()

        layout.addLayout(dashboard, 9)
        layout.addLayout(buttons, 1)

        options = QVBoxLayout()
        options.setContentsMargins(50, 50, 0, 50)
        help = QVBoxLayout()
        help.setContentsMargins(0, 50, 0, 50)

        header_font = QFont()
        header_font.setPointSize(25)
        help_header = QLabel('Help')
        help_header.setFont(header_font)
        help_text = QLabel()
        help_text.setFixedSize(600, 515)
        with open('help.txt', 'r') as file:
            help_text.setText(file.read())

        dashboard.addLayout(options, 1)
        dashboard.addLayout(help, 2)

        help.addWidget(help_header)
        help.addWidget(help_text)
        
        user_settings_label = QLabel('User settings')
        user_settings_label.setFixedHeight(50)
        user_settings_label.setFont(header_font)
        options.addWidget(user_settings_label)

        self.play_buttons = QButtonGroup(self)
        play_white = QRadioButton('White')
        play_black = QRadioButton('Black')
        play_random = QRadioButton('Random')
        play_random.setChecked(True)
        play_label = QLabel('Play as:')
        play_label.setFixedHeight(20)
        options.addWidget(play_label)
        options.addWidget(play_random)
        options.addWidget(play_white)
        options.addWidget(play_black)
        self.play_buttons.addButton(play_random)
        self.play_buttons.addButton(play_white)
        self.play_buttons.addButton(play_black)
        self.play_buttons.setId(play_random, 1)
        self.play_buttons.setId(play_white, 2)
        self.play_buttons.setId(play_black, 3)
        
        self.color_buttons = QButtonGroup(self)
        color1 = QRadioButton('Color 1')
        color2 = QRadioButton('Color 2')
        color3 = QRadioButton('Color 3')
        color3.setChecked(True)
        self.color_buttons.addButton(color1)
        self.color_buttons.addButton(color2)
        self.color_buttons.addButton(color3)
        self.color_buttons.setId(color1, 1)
        self.color_buttons.setId(color2, 2)
        self.color_buttons.setId(color3, 3)
        color_label = QLabel('Board color:')
        color_label.setFixedHeight(20)
        options.addWidget(color_label)
        options.addWidget(color1)
        options.addWidget(color2)
        options.addWidget(color3)

        self.level_buttons = QButtonGroup(self)
        easy = QRadioButton('Easy')
        medium = QRadioButton('Medium')
        hard = QRadioButton('Hard')
        medium.setChecked(True)
        self.level_buttons.addButton(easy)
        self.level_buttons.addButton(medium)
        self.level_buttons.addButton(hard)
        self.level_buttons.setId(easy, 1)
        self.level_buttons.setId(medium, 2)
        self.level_buttons.setId(hard, 3)

        level_label = QLabel('Engine level:')
        level_label.setFixedHeight(20)
        options.addWidget(level_label)
        options.addWidget(easy)
        options.addWidget(medium)
        options.addWidget(hard)

        button_height = self.parent.frameGeometry().height() / 10
        self.save_btn = QPushButton('Save')
        self.save_btn.setFixedSize(self.parent.frameGeometry().width() / 2, button_height)
        self.save_btn.clicked.connect(self.save)
        buttons.addWidget(self.save_btn)
    
        advanced_settings_label = QLabel('Advanced settings')
        advanced_settings_label.setFixedHeight(50)
        header_font = QFont()
        header_font.setPointSize(25)
        advanced_settings_label.setFont(header_font)
        options.addWidget(advanced_settings_label)

        self.alpha_beta_btn = QCheckBox('Alpha-Beta pruning')
        self.alpha_beta_btn.setChecked(True)
        self.move_ordering_btn = QCheckBox('Move ordering')
        self.move_ordering_btn.setChecked(True)
        self.quiescence_search_btn = QCheckBox('Quiescence search')
        self.quiescence_search_btn.setChecked(True)
        self.zobrist_btn = QCheckBox('Zobrist hashing')
        self.zobrist_btn.setChecked(False)

        options.addWidget(self.alpha_beta_btn)
        options.addWidget(self.move_ordering_btn)
        options.addWidget(self.quiescence_search_btn)
        options.addWidget(self.zobrist_btn)

    def save(self):
        self.parent.stack.setCurrentWidget(self.parent.qt_menu)
    
    def get_current_settings(self):
        return {
            'play_as': self.play_buttons.checkedId(),
            'board_color': self.color_buttons.checkedId(),
            'engine_level': self.level_buttons.checkedId(),
            'alpha_beta': self.alpha_beta_btn.isChecked(),
            'move_ordering': self.move_ordering_btn.isChecked(),
            'quiescence_search': self.quiescence_search_btn.isChecked(),
            'zobrist_hashing': self.zobrist_btn.isChecked()
        }