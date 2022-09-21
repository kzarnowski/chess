import chess

class App():
    def __init__(self):
        self.gui = None
        self.board = None
        self.move_in_progress = False
        self.active_an = None
        self.new_game()

    def new_game(self):
        self.board = chess.Board()
    
    def click_event(self, an):
        if self.move_in_progress:
            try:
                move = chess.Move.from_uci(self.active_an + an)
                if move in self.board.legal_moves:
                    print(move.uci())
                    if self.board.is_castling(move):
                        self.handle_castling(move)
                    elif self.board.is_en_passant(move):
                        self.handle_en_passant(move)
                    else:
                        self.gui.play.board.move_was_made(self.active_an, an)
                    self.board.push(move)
                elif self.is_promotion(move):
                    is_white = self.board.turn == chess.WHITE
                    new_piece_symbol = self.gui.play.board.get_promotion_piece(is_white)
                    new_piece = chess.Piece.from_symbol(new_piece_symbol)
                    move.promotion = new_piece.piece_type
                    print(move.uci())
                    self.gui.play.board.promotion(self.active_an, an, new_piece_symbol)
                    self.board.push(move)
                else:
                    print('Illegal move')
            except ValueError:
                print('Illegal move')
            self.move_in_progress = False
            self.active_an = None
        else:
            square = chess.parse_square(an)
            piece = self.board.piece_at(square)
            if piece:
                self.move_in_progress = True
                self.active_an = an
    
    def handle_castling(self, move):
        if self.board.is_kingside_castling(move):
            if self.board.turn == chess.WHITE:
                self.gui.play.board.kingside_castle(is_white=True)
            else:
                self.gui.play.board.kingside_castle(is_white=False)
        else:
            print("QUEENSIDE CASTLING")
            if self.board.turn == chess.WHITE:
                self.gui.play.board.queenside_castle(is_white=True)
            else:
                self.gui.play.board.queenside_castle(is_white=False)
    
    def handle_en_passant(self, move):
        active_an = move.uci()[:2]
        an = move.uci()[-2:]
        rank = int(an[1])
        if self.board.turn == chess.WHITE:
            an_to_remove = an[0] + str(rank - 1)
        else:
            an_to_remove = an[0] + str(rank + 1)
        self.gui.play.board.en_passant(active_an, an, an_to_remove)


    def is_promotion(self, move):  
        promotion_uci = move.uci() + 'q'
        print(promotion_uci)
        return chess.Move.from_uci(promotion_uci) in self.board.legal_moves
        