import chess
from app.game_handler import GameHandler
from app.engine import Engine

class App():
    def __init__(self):
        self.gui = None
        self.game = None
        # Init default app settings
        self.engine_is_white = True
    
    def new_game(self, qt_game):
        self.game = GameHandler(qt_game, Engine(self.engine_is_white, depth=4))
        qt_game.new_game(self.engine_is_white)
        if self.engine_is_white:
            self.game.run_engine()
        