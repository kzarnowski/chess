from PyQt5.QtWidgets import QFrame, QVBoxLayout, QLabel, QWidget, QGridLayout, QPushButton
from PyQt5.QtCore import Qt
from GUI.config import squares_color, theme
from GUI.helpers import an2rc, rc2an, FEN_PIECES
from GUI.piece import Piece

class Board(QFrame):
    def __init__(self, parent):
        QFrame.__init__(self)
        self.parent = parent
        self.is_flipped = True

        self.layout = QGridLayout()
        self.setLayout(self.layout)
        self.layout.setSpacing(0)

        for r in range(8):
            for c in range(8):
                square = Square(self, r, c)
                self.layout.addWidget(square, r, c)
        
        starting_fen = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'
        fen = 'r2q1nk1/1R2r2p/p2p2pQ/2pP1P1n/N7/P7/3N1PPP/1R4K1 w - - 1 26'
        self.set_position_from_fen(starting_fen)
    
    def put_piece(self, symbol, square):
        r, c = an2rc(square, self.is_flipped)
        piece = Piece(self, r, c, symbol)
        self.layout.addWidget(piece, r, c, alignment=Qt.AlignCenter)
        #print("PUT PIECE: ", symbol, " ", r, " ", c, " ", square)
    
    def set_position_from_fen(self, fen):
        fen = fen.split()[0]
        rows = fen.split('/')

        r = 0
        while r < 8:
            c = 0
            i = 0
            while c < 8:
                print(r, " ", c)
                symbol = rows[r][i]
                if symbol in FEN_PIECES:
                    if self.is_flipped:   
                        self.put_piece(symbol, rc2an((7-r, 7-c), self.is_flipped))
                    else:
                        self.put_piece(symbol, rc2an((r, c), self.is_flipped)) 
                    c += 1
                elif symbol.isdigit():
                    c += int(symbol)
                i += 1
            r += 1
            
                           

class Square(QLabel):
    def __init__(self, parent, r, c):
        QWidget.__init__(self, parent)
        self.parent = parent
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
        print("RC2AN:", rc2an((self.r,self.c), self.parent.is_flipped))
        self.parent.parent.header.info.setText(f'{self.r}, {self.c}')

    

