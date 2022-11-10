from PyQt5.QtWidgets import QFrame, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QRadioButton, QButtonGroup
from GUI.qt_menu import QtMenuButton
from GUI.qt_header import QtHeader

class QtSettings(QFrame):
    def __init__(self, parent):
        QFrame.__init__(self)
        self.parent = parent

        layout = QVBoxLayout()
        self.setLayout(layout)

        options = QVBoxLayout()
        buttons = QHBoxLayout()

        layout.addLayout(options, 9)
        layout.addLayout(buttons, 1)
        
        play_buttons = QButtonGroup(self)
        self.play_white = QRadioButton('White')
        self.play_black = QRadioButton('Black')
        self.play_random = QRadioButton('Random')
        self.play_random.setChecked(True)
        play_label = QLabel('Play as:')
        play_label.setFixedHeight(50)
        options.addWidget(play_label)
        options.addWidget(self.play_random)
        options.addWidget(self.play_white)
        options.addWidget(self.play_black)
        play_buttons.addButton(self.play_random)
        play_buttons.addButton(self.play_white)
        play_buttons.addButton(self.play_black)

        # self.lang_buttons = QButtonGroup(self)
        # self.lang_english = QRadioButton('English')
        # self.lang_english.setChecked(True)
        # self.lang_polish = QRadioButton('Polish')
        # options.addWidget(QLabel('Language:'))
        # options.addWidget(self.lang_english)
        # options.addWidget(self.lang_polish)
        # self.lang_buttons.addButton(self.lang_english)
        # self.lang_buttons.addButton(self.lang_polish)
        
        color_buttons = QButtonGroup(self)
        self.color1 = QRadioButton('Color 1')
        self.color2 = QRadioButton('Color 2')
        self.color3 = QRadioButton('Color 3')
        self.color1.setChecked(True)
        color_buttons.addButton(self.color1)
        color_buttons.addButton(self.color2)
        color_buttons.addButton(self.color3)
        color_label = QLabel('Board color:')
        color_label.setFixedHeight(50)
        options.addWidget(color_label)
        options.addWidget(self.color1)
        options.addWidget(self.color2)
        options.addWidget(self.color3)

        level_buttons = QButtonGroup(self)
        self.easy = QRadioButton('Easy')
        self.medium = QRadioButton('Medium')
        self.hard = QRadioButton('Hard')
        self.easy.setChecked(True)
        level_buttons.addButton(self.easy)
        level_buttons.addButton(self.medium)
        level_buttons.addButton(self.hard)
        level_label = QLabel('Engine level:')
        level_label.setFixedHeight(50)
        options.addWidget(level_label)
        options.addWidget(self.easy)
        options.addWidget(self.medium)
        options.addWidget(self.hard)

        button_height = self.parent.frameGeometry().height() / 10
        self.save_btn = QPushButton('Save')
        self.save_btn.setFixedHeight(button_height)
        self.save_btn.clicked.connect(self.save)
        self.cancel_btn = QPushButton('Cancel')
        self.cancel_btn.setFixedHeight(button_height)
        self.cancel_btn.clicked.connect(self.cancel)
        buttons.addWidget(self.save_btn)
        buttons.addWidget(self.cancel_btn)
    
    def get_current_lang(self):
        """ Get current language from settings, default: EN """
        return self.lang_buttons.checkedButton().text()
    
    def cancel(self):
        self.parent.stack.setCurrentWidget(self.parent.qt_menu)
    
    def save(self):
        self.parent.stack.setCurrentWidget(self.parent.qt_menu)
        