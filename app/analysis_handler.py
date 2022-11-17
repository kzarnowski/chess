import chess
from app.board_handler import BoardHandler
from app.engine import Engine
from GUI.qt_board import QtBoard

class AnalysisHandler(BoardHandler):
    def __init__(self, qt_board, engine):
        BoardHandler.__init__(self, engine, qt_board)