import chess
import chess.pgn
from app.board_handler import BoardHandler
from app.engine import Engine
from GUI.qt_board import QtBoard
from GUI.qt_analysis import QtAnalysis

class AnalysisHandler(BoardHandler):
    def __init__(self, qt_analysis, engine):
        BoardHandler.__init__(self, engine, qt_analysis.qt_board)
        self.qt_analysis = qt_analysis
        qt_analysis.analysis_handler = self
        self.game = None
        self.moves = None
        self.move_num = None
    
    def import_pgn(self, filename):
        pgn = open(filename)
        self.game = chess.pgn.read_game(pgn)
        self.board = self.game.board()
        self.moves = list(self.game.mainline_moves())
        self.move_num = 0
        self.display_board()
        self.update_sidebars(None)
    
    def update_sidebars(self, move):
        self.qt_analysis.qt_sidebar.notation.setText(str(self.game))
        self.qt_analysis.qt_sidebar.fen.setText(self.board.fen())

    def display_board(self):
        self.qt_analysis.qt_board.set_position_from_fen(self.board.fen())
    
    def handle_board_click_event(self, an):
        pass

    def handle_previous_move(self):
        if not self.moves:
            return
        if self.move_num == 0:
            self.qt_analysis.set_info('Start of game')
            return
        self.board.pop()
        self.qt_analysis.qt_board.set_position_from_fen(self.board.fen())
        self.move_num -= 1

    def handle_next_move(self):
        if not self.moves:
            return
        if self.move_num >= len(self.moves):
            self.qt_analysis.set_info('End of game')
            return
        move = self.moves[self.move_num]
        self.handle_engine_move(move)
        self.move_num += 1