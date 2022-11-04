import chess
import chess.pgn
from app.worker import  EngineWorker
from datetime import date

class GameHandler():
    def __init__(self, qt_game, playing_as_white, engine):
        self.qt_game = qt_game
        qt_game.game_handler = self
        self.qt_board = qt_game.qt_board
        self.board = chess.Board()
        self.move_in_progress = False
        self.active_an = None
        self.is_player_move = playing_as_white
        self.playing_as_white = playing_as_white
        self.engine = engine
        self.depth = 4
        self.pgn = self.create_pgn()
    
    def get_pgn(self):
        pgn = chess.pgn.Game()
        pgn = pgn.from_board(self.board)
        pgn.headers['Event'] = 'New Game'
        pgn.headers['Date'] = date.today().strftime('%Y.%m.%d')
        pgn.headers['Site'] = 'Chess App'
        pgn.headers['Round'] = '1'
        pgn.headers['White'] = 'User' if self.playing_as_white else 'Computer'
        pgn.headers['Black'] = 'Computer' if self.playing_as_white else 'User'
        return pgn

    def create_pgn(self):
        pgn = chess.pgn.Game()
        pgn.headers['Event'] = 'New Game'
        pgn.headers['Date'] = date.today().strftime('%Y.%m.%d')
        pgn.headers['Site'] = 'Chess App'
        pgn.headers['Round'] = '1'
        pgn.headers['White'] = 'User' if self.playing_as_white else 'Computer'
        pgn.headers['Black'] = 'Computer' if self.playing_as_white else 'User'
        return pgn

    def get_worker(self):
        worker = EngineWorker(self.engine, self.board, self.depth)
        worker.signals.result.connect(self.handle_worker_result)
        worker.signals.finished.connect(self.handle_worker_complete)
        worker.signals.progress.connect(self.handle_worker_progress)
        return worker

    def handle_worker_result(self, move):
        if self.board.is_castling(move):
            self.update_sidebars(move)
            self.handle_castling(move)
            self.board.push(move)
        elif self.board.is_en_passant(move):
            self.update_sidebars(move)
            self.handle_en_passant(move)
            self.board.push(move)
        else:
            self.update_sidebars(move)
            self.board.push(move)
            self.display_engine_move(move)
            
        self.pgn.add_main_variation(move)
        print(move)

    def handle_worker_progress(self, data):
        print(data)

    def handle_worker_complete(self):
        self.is_player_move = True
        
        print("Completed")

    def make_engine_move(self):
        worker = self.get_worker()
        self.qt_game.threadpool.start(worker)
        
    def display_engine_move(self, move):
        an_start = move.uci()[:2]
        an_end = move.uci()[2:4]
        if self.is_promotion(move):
            new_piece_symbol = move.uci()[4]
            self.qt_board.promotion(an_start, an_end, new_piece_symbol)
        else:
            if self.board.is_castling(move):
                self.handle_castling(move)
            elif self.board.is_en_passant(move):
                self.handle_en_passant(move)
            else:
                self.qt_board.move_was_made(an_start, an_end)

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
                        self.qt_board.move_was_made(self.active_an, an)
                elif self.is_promotion(move):
                    is_white = self.board.turn == chess.WHITE
                    new_piece_symbol = self.qt_board.get_promotion_piece(is_white)
                    new_piece = chess.Piece.from_symbol(new_piece_symbol)
                    move.promotion = new_piece.piece_type
                    self.qt_board.promotion(self.active_an, an, new_piece_symbol)               
                else:
                    raise ValueError
            except ValueError:
                print('Illegal move')
                self.move_in_progress = False
                self.active_an = None
            else:
                self.update_sidebars(move)
                self.board.push(move)
                self.pgn.add_main_variation(move)
                self.move_in_progress = False
                self.active_an = None
                outcome = self.board.outcome()
                if outcome:
                    self.qt_game.display_result(outcome.result())
                else:
                    self.is_player_move = False
                    self.make_engine_move()     
        else:
            square = chess.parse_square(an)
            piece = self.board.piece_at(square)
            if piece:
                self.move_in_progress = True
                self.active_an = an
                #self.qt_board.display_highlight_at_active_square(an)

    def handle_castling(self, move):
        if self.board.is_kingside_castling(move):
            if self.board.turn == chess.WHITE:
                self.qt_board.kingside_castle(is_white=True)
            else:
                self.qt_board.kingside_castle(is_white=False)
        else:
            print("QUEENSIDE CASTLING")
            if self.board.turn == chess.WHITE:
                self.qt_board.queenside_castle(is_white=True)
            else:
                self.qt_board.queenside_castle(is_white=False)
    

    def handle_en_passant(self, move):
        active_an = move.uci()[:2]
        an = move.uci()[-2:]
        rank = int(an[1])
        if self.board.turn == chess.WHITE:
            an_to_remove = an[0] + str(rank - 1)
        else:
            an_to_remove = an[0] + str(rank + 1)
        self.qt_board.en_passant(active_an, an, an_to_remove)


    def is_promotion(self, move):  
        promotion_uci = move.uci() + 'q'
        is_user_promotion = chess.Move.from_uci(promotion_uci) in self.board.legal_moves
        is_engine_promotion = move in self.board.legal_moves
        return is_user_promotion or is_engine_promotion
    

    def check_outcome(self):
        outcome = self.board.outcome()
        if outcome:
            self.qt_game.display_result(outcome.result())

    def update_sidebars(self, move):
        move_san = self.board.san(move)
        half_move_num = self.board.ply()
        self.qt_game.update_notation(move_san, half_move_num)
        self.qt_game.update_fen(self.board.fen())


