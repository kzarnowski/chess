import chess
from random import choice
from app.evaluation import evaluate_board

MATE_SCORE     = 1000000000
MATE_THRESHOLD =  999000000

class Engine:
    def __init__(self):
        self.using_alpha_beta = False
        self.using_move_ordering = True

    def get_ordered_moves(self, board: chess.Board):
        return list(board.legal_moves)

    def get_best_move(self, board: chess.Board, depth: int, progress):
        engine_is_white = board.turn == chess.WHITE
        if self.using_move_ordering:
            moves = self.get_ordered_moves(board)
        else:
            moves = list(board.legal_moves)
        best_score = -float("inf") if engine_is_white else float("inf")
        best_move = None

        for move in moves:
            board.push(move)
            if board.can_claim_draw():
                value = 0.0
            else:
                value = self.minimax(depth - 1, board, -float("inf"), float("inf"), not engine_is_white)
            board.pop()
            if engine_is_white and value >= best_score:
                best_score = value
                best_move = move
            elif not engine_is_white and value <= best_score:
                best_score = value
                best_move = move
        return best_move

    def minimax(self, depth, board: chess.Board, alpha, beta, engine_is_white):
        if board.is_checkmate():
            return -1000000000 if engine_is_white else 1000000000
        elif board.is_game_over():
            return 0
        if depth == 0:
            return evaluate_board(board)

        best_score = -float('inf') if engine_is_white else float('inf')
        if self.using_move_ordering:
            moves = self.get_ordered_moves(board)
        else:
            moves = list(board.legal_moves)
        for move in moves:
            board.push(move)
            score = self.minimax(depth - 1, board, alpha, beta, not engine_is_white)
            board.pop()
            if engine_is_white:
                best_score = max(best_score, score)
                alpha = max(alpha, best_score)
            else:
                best_score = min(best_score, score)
                beta = min(beta, best_score)
            if self.using_alpha_beta and beta <= alpha:
                return best_score
        return best_score