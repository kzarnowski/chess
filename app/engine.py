import chess
from random import choice

class Engine:
    def __init__(self):
        pass

    def get_best_move(self, board, depth):
        move = choice(board.legal_moves)
        return move