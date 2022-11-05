import chess
import chess.pgn
from app.worker import  EngineWorker
from app.engine import Engine
from datetime import date
from GUI.qt_game import QtGame

class GameHandler():
    def __init__(self, qt_game: QtGame, engine: Engine):
        self.qt_game = qt_game
        qt_game.game_handler = self
        self.qt_board = qt_game.qt_board
        self.board = chess.Board()
        self.move_in_progress = False
        self.active_an = None
        self.engine = engine
    

    def handle_board_click_event(self, an):
        if self.move_in_progress:
            try:
                move = chess.Move.from_uci(self.active_an + an)
                if move in self.board.legal_moves:
                    self.handle_standard_move(move)
                elif self.is_promotion(move):
                    self.handle_promotion(move)       
                else:
                    raise ValueError
                self.move_in_progress = False
                self.active_an = None
                outcome = self.board.outcome()
                if outcome:
                    self.qt_game.display_result(outcome.result())
                else:
                    self.run_engine()
            except ValueError:
                self.qt_game.set_info('Illegal move')
                self.move_in_progress = False
                self.active_an = None   
        else:
            square = chess.parse_square(an)
            piece = self.board.piece_at(square)
            if piece:
                self.move_in_progress = True
                self.active_an = an
                # self.qt_board.display_highlight_at_active_square(an)


    def handle_engine_move(self, move):
        an_start = move.uci()[:2]
        an_end = move.uci()[2:4]
        if self.is_promotion(move):
            new_piece_symbol = move.uci()[4]
            self.qt_board.display_promotion(an_start, an_end, new_piece_symbol)
        else:
            self.handle_standard_move(move)


    def handle_standard_move(self, move):
        """ Display a move that is not a promotion """
        an_start = move.uci()[:2]
        an_end = move.uci()[2:4]
        if self.board.is_castling(move):
            self.handle_castling(move)
        elif self.board.is_en_passant(move):
            self.handle_en_passant(move)
        else:
            self.qt_board.display_standard_move(an_start, an_end)
        self.update_sidebars(move)
        self.board.push(move)


    def handle_castling(self, move):
        if self.board.is_kingside_castling(move):
            self.qt_board.display_kingside_castle(is_white=self.board.turn == chess.WHITE)
        else:
            self.qt_board.display_queenside_castle(is_white=self.board.turn == chess.WHITE)
    

    def handle_promotion(self, move: chess.Move):
        an_start = move.uci()[:2]
        an_end = move.uci()[-2:]
        is_white = self.board.turn == chess.WHITE
        new_piece_symbol = self.qt_board.get_promotion_piece(is_white)
        new_piece = chess.Piece.from_symbol(new_piece_symbol)
        move.promotion = new_piece.piece_type
        self.qt_board.display_promotion(an_start, an_end, new_piece_symbol)
        self.update_sidebars(move)
        self.board.push(move)


    def handle_en_passant(self, move: chess.Move):
        an_start = move.uci()[:2]
        an_end = move.uci()[-2:]
        rank = int(an_end[1])
        if self.board.turn == chess.WHITE:
            an_to_remove = an_end[0] + str(rank - 1)
        else:
            an_to_remove = an_end[0] + str(rank + 1)
        self.qt_board.display_en_passant(an_start, an_end, an_to_remove)


    def get_worker(self):
        worker = EngineWorker(self.engine, self.board)
        worker.signals.result.connect(self.handle_engine_move)
        worker.signals.finished.connect(self.handle_worker_complete)
        worker.signals.progress.connect(self.handle_worker_progress)
        return worker


    def handle_worker_progress(self, data):
        print(data)


    def handle_worker_complete(self):
        outcome = self.board.outcome()
        if outcome:
            self.qt_game.display_result(outcome.result())
        else:
            self.qt_game.set_info('Your turn')


    def run_engine(self):
        self.qt_game.set_info('Computer is thinking ⏳')
        worker = self.get_worker()
        self.qt_game.threadpool.start(worker)


    def is_promotion(self, move: chess.Move):  
        promotion_uci = move.uci() + 'q'
        is_user_promotion = chess.Move.from_uci(promotion_uci) in self.board.legal_moves
        is_engine_promotion = len(move.uci()) == 5 and move in self.board.legal_moves
        return is_user_promotion or is_engine_promotion


    def update_sidebars(self, move: chess.Move):
        move_san = self.board.san(move)
        half_move_num = self.board.ply()
        self.qt_game.update_notation(move_san, half_move_num)
        self.qt_game.update_fen(self.board.fen())
    

    def resign(self):
        result = '1-0' if self.engine.is_white else '1-0'
        self.qt_game.display_result(result)


    def get_pgn(self):
        pgn = chess.pgn.Game()
        pgn = pgn.from_board(self.board)
        pgn.headers['Event'] = 'New Game'
        pgn.headers['Date'] = date.today().strftime('%Y.%m.%d')
        pgn.headers['Site'] = 'Chess App'
        pgn.headers['Round'] = '1'
        pgn.headers['White'] = 'Computer' if self.engine.is_white else 'User'
        pgn.headers['Black'] = 'User' if self.engine.is_white else 'Computer'
        return pgn


