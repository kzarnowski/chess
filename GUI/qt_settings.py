from PyQt5.QtWidgets import QFrame, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QRadioButton, QButtonGroup
from GUI.qt_menu import QtMenuButton
from GUI.qt_header import QtHeader

class QtSettings(QFrame):
    def __init__(self, parent):
        QFrame.__init__(self)
        self.parent = parent

        layout = QVBoxLayout()
        self.setLayout(layout)

        options = QHBoxLayout()
        buttons = QHBoxLayout()

        layout.addLayout(options, 9)
        layout.addLayout(buttons, 1)

        c1 = QVBoxLayout()
        c2 = QVBoxLayout()
        options.addLayout(c1)
        options.addLayout(c2)
        
        play_buttons = QButtonGroup(self)
        self.play_white = QRadioButton('White')
        self.play_black = QRadioButton('Black')
        self.play_random = QRadioButton('Random')
        self.play_random.setChecked(True)
        c1.addWidget(QLabel('Play as:'))
        c1.addWidget(self.play_random)
        c1.addWidget(self.play_white)
        c1.addWidget(self.play_black)
        play_buttons.addButton(self.play_random)
        play_buttons.addButton(self.play_white)
        play_buttons.addButton(self.play_black)

        lang_buttons = QButtonGroup(self)
        self.lang_english = QRadioButton('English')
        self.lang_english.setChecked(True)
        self.lang_polish = QRadioButton('Polish')
        c1.addWidget(QLabel('Language:'))
        c1.addWidget(self.lang_english)
        c1.addWidget(self.lang_polish)
        lang_buttons.addButton(self.lang_english)
        lang_buttons.addButton(self.lang_polish)
        
        color_buttons = QButtonGroup(self)
        self.color1 = QRadioButton('Color 1')
        self.color2 = QRadioButton('Color 2')
        self.color3 = QRadioButton('Color 3')
        self.color1.setChecked(True)
        color_buttons.addButton(self.color1)
        color_buttons.addButton(self.color2)
        color_buttons.addButton(self.color3)
        c2.addWidget(QLabel('Board colors:'))
        c2.addWidget(self.color1)
        c2.addWidget(self.color2)
        c2.addWidget(self.color3)

        level_buttons = QButtonGroup(self)
        self.easy = QRadioButton('Easy')
        self.medium = QRadioButton('Medium')
        self.hard = QRadioButton('Hard')
        self.easy.setChecked(True)
        level_buttons.addButton(self.easy)
        level_buttons.addButton(self.medium)
        level_buttons.addButton(self.hard)
        c2.addWidget(QLabel('Engine level:'))
        c2.addWidget(self.easy)
        c2.addWidget(self.medium)
        c2.addWidget(self.hard)

        button_height = self.parent.frameGeometry().height() / 10
        self.save_btn = QPushButton('Save')
        self.save_btn.setFixedHeight(button_height)
        self.cancel_btn = QPushButton('Cancel')
        self.cancel_btn.setFixedHeight(button_height)
        buttons.addWidget(self.save_btn)
        buttons.addWidget(self.cancel_btn)