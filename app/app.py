import chess
from app.game_handler import GameHandler
from app.engine import Engine

class App():
    def __init__(self):
        self.gui = None
        self.game = None
        self.engine = Engine()

        # Init default app settings
        self.playing_as_white = False
        self.engine_depth = 5
    
    def new_game(self, qt_game):
        self.game = GameHandler(qt_game, self.playing_as_white, self.engine)
        qt_game.qt_board.display_starting_position(self.playing_as_white)
        qt_game.qt_right_sidebar.notation.setText('')
        if not self.playing_as_white:
            self.game.make_engine_move()
        