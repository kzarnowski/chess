import abc
import chess
from app.worker import  EngineWorker
from app.engine import Engine
from GUI.qt_board import QtBoard

class BoardHandler:
    def __init__(self, engine: Engine, qt_board: QtBoard):
        self.board = chess.Board()
        self.engine = engine
        self.qt_board = qt_board

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

    @abc.abstractmethod
    def handle_worker_progress(self, data):
        return

    @abc.abstractmethod
    def handle_worker_complete(self):
        return

    @abc.abstractmethod
    def run_engine(self):
        return