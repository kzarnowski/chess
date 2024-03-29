from PyQt5.QtWidgets import QFrame, QVBoxLayout, QLabel, QWidget, QGridLayout, QPushButton
from PyQt5.QtCore import Qt
from GUI.helpers import an2rc, rc2an, FEN_PIECES
from GUI.qt_piece import QtPiece
from GUI.qt_square import QtSquare
from GUI.qt_promotion_dialog import QtPromotionDialog

class QtBoard(QFrame):
    def __init__(self, parent):
        QFrame.__init__(self)
        self.parent = parent
        self.gui = parent.parent
        self.is_flipped = False
        self.layout = QGridLayout()
        self.setLayout(self.layout)
        self.layout.setSpacing(0)
        self.pieces = {}
        self.squares = {}

        for r in range(8):
            for c in range(8):
                square = QtSquare(self, r, c)
                self.layout.addWidget(square, r, c)
                self.squares[str(r)+str(c)] = square

        print(len(self.squares.values()))

    def display_starting_position(self, engine_is_white):
        self.is_flipped = engine_is_white
        self.remove_all_pieces() # remove pieces from previous game   
        starting_fen = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'
        self.set_position_from_fen(starting_fen)

    def remove_all_pieces(self):
        for an in list(self.pieces.keys()):
            self.remove_piece(an)

    def get_squares_color(self, color_num):
        colors = {
            'dark': '#b88a4a',
            'light': '#e3c16f'
        }
        if color_num == 2:
            colors['dark'] = '#769656'
            colors['light'] = '#eeeed2'
        elif color_num == 3:
            colors['dark'] = '#4b648a'
            colors['light'] = '#d0dff4'
        return colors
    
    def set_squares_color(self, color_num):
        colors = self.get_squares_color(color_num)
        for square in self.squares.values():
            square.set_colors(colors)
    
    def put_piece(self, symbol, an):
        r, c = an2rc(an, self.is_flipped)
        piece = QtPiece(self, r, c, symbol)
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
            
    def click_event(self, an):
        self.gui.app.game.handle_board_click_event(an)
    
    def display_standard_move(self, an_start, an_end):
        symbol = self.pieces[an_start].symbol
        self.remove_piece(an_start)
        if an_end in self.pieces.keys():
            self.remove_piece(an_end)
        self.put_piece(symbol, an_end)
    
    def display_kingside_castle(self, is_white):
        if is_white:
            self.remove_piece('e1')
            self.remove_piece('h1')
            self.put_piece('K', 'g1')
            self.put_piece('R', 'f1')
        else:
            self.remove_piece('e8')
            self.remove_piece('h8')
            self.put_piece('k', 'g8')
            self.put_piece('r', 'f8')
    
    def display_queenside_castle(self, is_white):
        if is_white:
            self.remove_piece('e1')
            self.remove_piece('a1')
            self.put_piece('K', 'c1')
            self.put_piece('R', 'd1')
        else:
            self.remove_piece('e8')
            self.remove_piece('a8')
            self.put_piece('k', 'c8')
            self.put_piece('r', 'd8')
    
    def display_en_passant(self, active_an, an, an_to_remove):
        self.display_standard_move(active_an, an)
        self.remove_piece(an_to_remove)
    
    def display_promotion(self, active_an, an, new_piece_symbol):
        self.remove_piece(active_an)
        if an in self.pieces.keys():
            self.remove_piece(an)
        self.put_piece(new_piece_symbol, an)

    def get_promotion_piece(self, is_white):
        dialog = QtPromotionDialog(is_white, self.get_squares_color()['light'])
        option = dialog.exec()
        symbol = chr(option)
        print(symbol)
        return symbol

    def display_highlight_at_active_square(self, an):
        # r, c = an2rc(an, self.is_flipped)
        # active_square = self.squares[str(r+c)]
        # active_square.set_color('#9e9897')
        piece = self.pieces[an]
        piece.highlight()

    def get_square_from_an(self, an):
        pass

        