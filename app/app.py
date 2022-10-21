import chess
from app.game_handler import GameHandler

class App():
    def __init__(self):
        self.gui = None
        self.game = None
    
    def new_game(self, qt_game):
        self.game = GameHandler(qt_game)
        