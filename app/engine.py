import chess
from random import choice
from app.evaluation import get_board_score, is_endgame, get_move_score
import time
from collections import defaultdict

MAX_SCORE = 1000000000

class Engine:
    def __init__(self, is_white, current_settings):
        
        self.is_white = is_white
        self.count = 0
        self.history = {}
        self.best_move = None

        if current_settings['engine_level'] == 1:
            self.depth = 3
        elif current_settings['engine_level'] == 2:
            self.depth = 4
        elif current_settings['engine_level'] == 3:
            self.depth = 5

        self.using_alpha_beta = current_settings['alpha_beta']
        self.using_move_ordering = current_settings['move_ordering']
        self.using_quiescence_search = current_settings['quiescence_search']
        self.using_zobrist_hashing = current_settings['zobrist_hashing']

    def get_ordered_moves(self, board: chess.Board, quiescence_search):
        endgame = is_endgame(board)

        def order(move):
            side = 1 if board.turn == chess.WHITE else -1
            history_score = side * self.history[board.turn][move.uci()]
            return get_move_score(board, move, endgame) + history_score
        
        moves = board.legal_moves
        if quiescence_search:
            moves = [move for move in moves if board.gives_check(move) or board.is_capture(move)]

        # moves = board.generate_legal_captures() if captures_only else board.legal_moves
        ordered_moves = sorted(moves, key=order, reverse=board.turn == chess.WHITE)
        return ordered_moves


    def get_best_move(self, board: chess.Board, progress):
        self.count = 0
        self.history = {
            chess.WHITE: defaultdict(int),
            chess.BLACK: defaultdict(int)
        }
        start_time = time.time()
        res =  self.minimax(self.depth, board, -float("inf"), float("inf"), self.is_white)[0]
        print('Evaluated: ', self.count, f'TIME: {time.time() - start_time}')
        return res

    def quiescence_search(self, board: chess.Board, alpha, beta, engine_is_white):
        if board.is_checkmate():
            self.count += 1
            return -MAX_SCORE if engine_is_white else MAX_SCORE
        elif board.is_game_over():
            self.count += 1
            return 0
        
        self.count += 1
        best_score = get_board_score(board)
        if engine_is_white:
            alpha = max(alpha, best_score)
        else:
            beta = min(beta, best_score)
        if self.using_alpha_beta and alpha >= beta:
            return best_score

        if self.using_move_ordering:
            moves = self.get_ordered_moves(board, quiescence_search=True)
        else:
            moves = [move for move in board.legal_moves if board.gives_check(move) or board.is_capture(move)]
        # if len(moves) == 0:
        #     print(board.fen())
        for move in moves:
            board.push(move)
            score = self.quiescence_search(board, alpha, beta, not engine_is_white)
            board.pop()
            if engine_is_white:
                best_score = max(score, best_score)
                alpha = max(alpha, best_score)
            else:
                best_score = min(score, best_score)
                beta = min(beta, best_score)
            if self.using_alpha_beta and alpha >= beta:
                break
        return best_score

    def minimax(self, depth, board: chess.Board, alpha, beta, engine_is_white):
        if board.is_checkmate():
            self.count += 1
            return -MAX_SCORE if engine_is_white else MAX_SCORE
        elif board.is_game_over():
            self.count += 1
            return 0
        if depth == 0:
            if self.using_quiescence_search:
                return self.quiescence_search(board, alpha, beta, not engine_is_white)
            else:
                return get_board_score(board)
            

        best_score = -float('inf') if engine_is_white else float('inf')
        best_move = None
        if self.using_move_ordering:
            moves = self.get_ordered_moves(board, quiescence_search=False)
        else:
            moves = list(board.legal_moves)
        for move in moves:
            board.push(move)
            score = self.minimax(depth - 1, board, alpha, beta, not engine_is_white)
            board.pop()
            if engine_is_white:
                if score > best_score:
                    best_score = score
                    best_move = move
                alpha = max(alpha, best_score)
            else:
                if score < best_score:
                    best_score = score
                    best_move = move
                beta = min(beta, best_score)
            if self.using_alpha_beta and alpha >= beta:
                if not board.is_capture(move):
                    self.history[board.turn][move.uci()] += depth ** 2
                break
        if depth == self.depth:
            return best_move, best_score
        else:
            return best_score

