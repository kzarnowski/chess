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
                        pass
                    elif self.is_promotion(move):
                        # TODO
                        pass
                    else:
                        self.gui.play.board.move_was_made(self.active_an, an)
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
    
    def is_promotion(self, move):
        return False
        #TODO