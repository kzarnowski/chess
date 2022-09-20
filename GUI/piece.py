from PyQt5.QtWidgets import QLabel, QSizePolicy
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QPixmap, QIcon
from GUI.helpers import get_piece_png_path, rc2an

class Piece(QLabel):
    def __init__(self, board, r, c, symbol):
        QLabel.__init__(self)
        self.board = board
        self.r = r
        self.c = c
        self.symbol = symbol
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.size = board.width() / 8
        pixmap = QIcon(get_piece_png_path(self.symbol)).pixmap(QSize(0.9 * self.size, 0.9 * self.size))
        self.setPixmap(pixmap)
        
    def mousePressEvent(self, event):
        print(self.r, self.c)
        self.board.parent.header.info.setText(f'{self.r}, {self.c}')
        an = rc2an((self.r,self.c), self.board.is_flipped)
        self.board.click_event(an)
