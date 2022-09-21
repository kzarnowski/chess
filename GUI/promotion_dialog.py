from PyQt5.QtWidgets import QDialog, QGridLayout, QLabel
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon
from GUI.config import squares_color, theme
from GUI.helpers import get_piece_png_path

class QtPromotionDialog(QDialog):
    def __init__(self, is_white):
        QDialog.__init__(self)
        self.setWindowTitle("Promotion")
        self.layout = QGridLayout()
        self.setLayout(self.layout)

        if is_white:
            self.pieces = ['Q', 'R', 'B', 'N']
        else:
            self.pieces = ['q', 'r', 'b', 'n']

        for index in range(4):
            square = QtClickableLabel(self, index)
            square_color = squares_color[theme]['light']
            square.setStyleSheet(f'background-color: {square_color}')
            piece = QtClickableLabel(self, index)
            piece.setAttribute(Qt.WA_TranslucentBackground)
            pixmap = QIcon(get_piece_png_path(self.pieces[index])).pixmap(square.size())
            piece.setPixmap(pixmap)
            self.layout.addWidget(square, 0, index)
            self.layout.addWidget(piece, 0, index, alignment=Qt.AlignCenter)
    
    def set_option(self, index):
        self.done(ord(self.pieces[index]))

class QtClickableLabel(QLabel):
    def __init__(self, dialog, index):
        QLabel.__init__(self)
        self.dialog = dialog
        self.index = index
    
    def mousePressEvent(self, event):
        self.dialog.set_option(self.index)