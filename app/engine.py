import chess
from random import choice
from app.evaluation import evaluate_board

from multiprocessing import Pool, cpu_count

class Engine:
    def __init__(self, engine_is_white):
        self.using_alpha_beta = True
        self.using_move_ordering = True
        self.engine_is_white = engine_is_white

    def get_ordered_moves(self, board: chess.Board):
        return list(board.legal_moves)

    def run_minimax(self, board, depth, move):
        board_copy = board.copy()
        board_copy.push(move)
        if board_copy.can_claim_draw():
            score = 0.0
        else:
            score = self.minimax(depth - 1, board_copy, -float("inf"), float("inf"), not self.engine_is_white)
        board_copy.pop()
        return move, score

    def get_best_move(self, board: chess.Board, depth: int, progress):
        if self.using_move_ordering:
            moves = self.get_ordered_moves(board)
        else:
            moves = list(board.legal_moves)
        best_score = -float("inf") if self.engine_is_white else float("inf")
        best_move = None

        args = []
        for move in moves:
            args.append((board, depth, move))
        with Pool(processes=len(moves)) as p:
            res = p.starmap(self.run_minimax, args)
            for move, score in res:
                if self.engine_is_white and score >= best_score:
                    best_score = score
                    best_move = move
                elif not self.engine_is_white and score <= best_score:
                    best_score = score
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