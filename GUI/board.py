from re import L
from PyQt5.QtWidgets import QFrame, QVBoxLayout, QLabel, QWidget, QGridLayout, QPushButton
from GUI.config import squares_color, theme

class Board(QFrame):
    def __init__(self, parent):
        QFrame.__init__(self)
        self.parent = parent

        self.layout = QGridLayout()
        self.setLayout(self.layout)
        self.layout.setSpacing(0)

        for r in range(8):
            for c in range(8):
                #square = Square(self, r, c)
                square = QWidget(self)
                #square = Square2(self)
                if r % 2 == c % 2:
                    square.setStyleSheet('background-color: #F0D9B5')
                else:
                    square.setStyleSheet('background-color: #B58863')
                self.layout.addWidget(square, r, c)

class Square2(QWidget):
    def __init__(self, parent):
        QWidget.__init__(self)
        self.parent = parent

class Square(QWidget):
    def __init__(self, parent, r, c):
        QWidget.__init__(self)
        self.parent = parent
        self.r = r
        self.c = c
        if r % 2 == c % 2:
            self.color = squares_color[theme]['dark']
        else:
            self.color = squares_color[theme]['light'] 
        self.setStyleSheet(f'background-color: {self.color}') 

    def mousePressEvent(self, event):
        print(self.r, self.c)
        self.parent.parent.header.info.setText(f'{self.r}, {self.c}')
        
    # def square_clicked(self):
    #     print(self.r, self.c)
    #     self.parent.parent.header.info.setText(f'{self.r}, {self.c}')
