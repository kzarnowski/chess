from PyQt5.QtWidgets import QLabel, QWidget
from GUI.helpers import rc2an
from GUI.config import squares_color, theme

class QtSquare(QLabel):
    def __init__(self, board, r, c):
        QWidget.__init__(self, board)
        self.board = board
        self.r = r
        self.c = c
        if r % 2 == c % 2:
            self.color = squares_color[theme]['light']
        else:
            self.color = squares_color[theme]['dark'] 
        self.setStyleSheet(f'background-color: {self.color}')

    def set_color(self, color):
        self.setStyleSheet(f'background-color: {color}')

    def mousePressEvent(self, event):
        print(self.r, self.c)
        print("RC2AN:", rc2an((self.r,self.c), self.board.is_flipped))
        self.board.parent.header.info.setText(f'{self.r}, {self.c}')
        an = rc2an((self.r,self.c), self.board.is_flipped)
        self.board.click_event(an)
