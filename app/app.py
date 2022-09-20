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
                    self.board.push(move)
                    self.gui.play.board.move_was_made(self.active_an, an)
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
    