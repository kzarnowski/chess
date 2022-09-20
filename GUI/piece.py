from PyQt5.QtWidgets import QLabel, QSizePolicy
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QPixmap, QIcon
from GUI.helpers import get_piece_png_path

class Piece(QLabel):
    def __init__(self, board, r, c, fen):
        QLabel.__init__(self)
        self.board = board
        self.r = r
        self.c = c
        self.fen = fen
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.size = board.width() / 8
        pixmap = QIcon(get_piece_png_path(self.fen)).pixmap(QSize(0.9 * self.size, 0.9 * self.size))
        self.setPixmap(pixmap)
        
    def mousePressEvent(self, event):
        print(self.r, self.c)
        self.board.parent.header.info.setText(f'{self.r}, {self.c}')
