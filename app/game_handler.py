import chess

class GameHandler():
    def __init__(self, qt_game, playing_as_white, engine):
        self.qt_game = qt_game
        self.board = chess.Board()
        self.move_in_progress = False
        self.active_an = None
        self.is_player_move = playing_as_white
        self.engine = engine
    
    def board_click_event(self, an):
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
                        self.qt_game.move_was_made(self.active_an, an)
                elif self.is_promotion(move):
                    is_white = self.board.turn == chess.WHITE
                    new_piece_symbol = self.qt_game.get_promotion_piece(is_white)
                    new_piece = chess.Piece.from_symbol(new_piece_symbol)
                    move.promotion = new_piece.piece_type
                    print(move.uci())
                    self.qt_game.promotion(self.active_an, an, new_piece_symbol)               
                else:
                    raise ValueError
            except ValueError:
                print('Illegal move')
            else:
                self.board.push(move)
                self.check_outcome()
            self.move_in_progress = False
            self.active_an = None
            self.is_player_move = False
        else:
            square = chess.parse_square(an)
            piece = self.board.piece_at(square)
            if piece:
                self.move_in_progress = True
                self.active_an = an

    def handle_castling(self, move):
        if self.board.is_kingside_castling(move):
            if self.board.turn == chess.WHITE:
                self.qt_game.kingside_castle(is_white=True)
            else:
                self.qt_game.kingside_castle(is_white=False)
        else:
            print("QUEENSIDE CASTLING")
            if self.board.turn == chess.WHITE:
                self.qt_game.queenside_castle(is_white=True)
            else:
                self.qt_game.queenside_castle(is_white=False)
    

    def handle_en_passant(self, move):
        active_an = move.uci()[:2]
        an = move.uci()[-2:]
        rank = int(an[1])
        if self.board.turn == chess.WHITE:
            an_to_remove = an[0] + str(rank - 1)
        else:
            an_to_remove = an[0] + str(rank + 1)
        self.qt_game.en_passant(active_an, an, an_to_remove)


    def is_promotion(self, move):  
        promotion_uci = move.uci() + 'q'
        print(promotion_uci)
        return chess.Move.from_uci(promotion_uci) in self.board.legal_moves
    

    def check_outcome(self):
        outcome = self.board.outcome()
        if outcome:
            self.qt_game.display_result(outcome.result())


