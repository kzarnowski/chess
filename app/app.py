import chess

from app.board_handler import BoardHandler
from app.game import Game

class App():
    def __init__(self):
        self.gui = None
        self.game = None
    
    def new_game(self):
        self.game = Game(self.gui.play, BoardHandler())
        