import chess
import chess.pgn
from app.board_handler import BoardHandler
from app.engine import Engine
from GUI.qt_board import QtBoard
from GUI.qt_analysis import QtAnalysis

class AnalysisHandler(BoardHandler):
    def __init__(self, qt_analysis, engine):
        BoardHandler.__init__(self, engine, qt_analysis)
        self.qt_analysis = qt_analysis
        qt_analysis.analysis_handler = self
        self.game = None
    
    def import_pgn(self, filename):
        pgn = open(filename)
        self.game = chess.pgn.read_game(pgn)
        self.board = self.game.board()
        self.display_board()
        self.update_sidebars()
    
    def update_sidebars(self):
        self.qt_analysis.qt_sidebar.notation.setText(str(self.game))
        self.qt_analysis.qt_sidebar.fen.setText(self.board.fen())

    def display_board(self):
        self.qt_analysis.qt_board.set_position_from_fen(self.board.fen())