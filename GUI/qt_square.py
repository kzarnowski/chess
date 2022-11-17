from PyQt5.QtWidgets import QLabel, QWidget
from GUI.helpers import rc2an

class QtSquare(QLabel):
    def __init__(self, qt_board, r, c):
        QWidget.__init__(self, qt_board)
        self.qt_board = qt_board
        self.r = r
        self.c = c
        # if r % 2 == c % 2:
        #     self.color = self.qt_board.get_squares_color(1)['light']
        # else:
        #     self.color = self.qt_board.get_squares_color(1)['dark'] 
        # self.setStyleSheet(f'background-color: {self.color}')

    def set_colors(self, colors):
        if self.r % 2 == self.c % 2:
            self.setStyleSheet(f"background-color: {colors['light']}")
        else:
            self.setStyleSheet(f"background-color: {colors['dark']}")

    def mousePressEvent(self, event):
        # print(self.r, self.c)
        # print("RC2AN:", rc2an((self.r,self.c), self.qt_board.is_flipped))
        self.qt_board.parent.qt_sidebar.info.setText(f'{self.r}, {self.c}')
        an = rc2an((self.r,self.c), self.qt_board.is_flipped)
        self.qt_board.click_event(an)
