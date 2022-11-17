import chess
import chess.pgn
from app.engine import Engine
from datetime import date
from GUI.qt_game import QtGame
from app.board_handler import BoardHandler

class GameHandler(BoardHandler):
    def __init__(self, qt_game: QtGame, engine: Engine):
        BoardHandler.__init__(self, engine, qt_game.qt_board)
        self.qt_game = qt_game
        qt_game.game_handler = self
        self.move_in_progress = False
        self.active_an = None
    

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


    def update_sidebars(self, move: chess.Move):
        move_san = self.board.san(move)
        half_move_num = self.board.ply()
        self.qt_game.update_notation(move_san, half_move_num)
        self.qt_game.update_fen(self.board.fen())
    

    def resign(self):
        print("RESULT ENGINE WHITE: ", self.engine.is_white)
        result = '1-0' if self.engine.is_white else '0-1'
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


