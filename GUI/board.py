from PyQt5.QtWidgets import QFrame, QVBoxLayout, QLabel, QWidget, QGridLayout, QPushButton
from PyQt5.QtCore import Qt
from GUI.helpers import an2rc, rc2an, FEN_PIECES
from GUI.piece import Piece
from GUI.square import Square

class Board(QFrame):
    def __init__(self, parent):
        QFrame.__init__(self)
        self.parent = parent
        self.is_flipped = True

        self.layout = QGridLayout()
        self.setLayout(self.layout)
        self.layout.setSpacing(0)
        self.pieces = {}

        for r in range(8):
            for c in range(8):
                square = Square(self, r, c)
                self.layout.addWidget(square, r, c)
        
        starting_fen = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'
        fen = 'r2q1nk1/1R2r2p/p2p2pQ/2pP1P1n/N7/P7/3N1PPP/1R4K1 w - - 1 26'
        self.set_position_from_fen(starting_fen)
    
    def put_piece(self, symbol, an):
        r, c = an2rc(an, self.is_flipped)
        piece = Piece(self, r, c, symbol)
        self.layout.addWidget(piece, r, c, alignment=Qt.AlignCenter)
        self.pieces[an] = piece
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

    def remove_piece(self, an):
        piece = self.pieces[an]
        self.layout.removeWidget(piece)
        piece.deleteLater()
        del self.pieces[an]
            
    def move_was_made(self, an_start, an_end):
        symbol = self.pieces[an_start].symbol
        self.remove_piece(an_start)
        if an_end in self.pieces.keys():
            self.remove_piece(an_end)
        self.put_piece(symbol, an_end)
    
    def click_event(self, an):
        self.parent.parent.app.click_event(an)
