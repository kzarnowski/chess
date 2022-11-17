from PyQt5.QtWidgets import QLabel, QWidget
from GUI.helpers import rc2an

class QtSquare(QLabel):
    def __init__(self, qt_board, r, c):
        QWidget.__init__(self, qt_board)
        self.qt_board = qt_board
        self.r = r
        self.c = c

    def set_colors(self, colors):
        if self.r % 2 == self.c % 2:
            self.setStyleSheet(f"background-color: {colors['light']}")
        else:
            self.setStyleSheet(f"background-color: {colors['dark']}")

    def mousePressEvent(self, event):
        self.qt_board.parent.qt_sidebar.info.setText(rc2an((self.r,self.c), self.qt_board.is_flipped))
        an = rc2an((self.r,self.c), self.qt_board.is_flipped)
        self.qt_board.click_event(an)
