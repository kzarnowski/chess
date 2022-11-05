import chess
from random import choice
from app.evaluation import evaluate_board
import time

from multiprocessing import Pool, Process, cpu_count, Value

class Engine:
    def __init__(self, is_white, depth):
        self.using_alpha_beta = True
        self.using_move_ordering = True
        self.is_white = is_white
        self.depth = depth

    def get_ordered_moves(self, board: chess.Board):
        return list(board.legal_moves)

    def run_minimax(self, board, depth, move, returned_score):
        board_copy = board.copy()
        board_copy.push(move)
        if board_copy.can_claim_draw():
            score = 0.0
        else:
            score = self.minimax(depth - 1, board_copy, -float("inf"), float("inf"), not self.is_white)
        board_copy.pop()
        #return move, score # when using pool instead of process
        returned_score.value = score

    def get_best_move(self, board: chess.Board, progress):
        if self.using_move_ordering:
            moves = self.get_ordered_moves(board)
        else:
            moves = list(board.legal_moves)
        best_score = -float("inf") if self.is_white else float("inf")
        best_move = None

        args = []
        for move in moves:
            args.append((board, self.depth, move))

        """ Pool """
        # start_time = time.time()
        # with Pool(processes=cpu_count()) as p:
        #     res = p.starmap(self.run_minimax, args)
        # for move, score in res:
        #     if self.engine_is_white and score >= best_score:
        #         best_score = score
        #         best_move = move
        #     elif not self.engine_is_white and score <= best_score:
        #         best_score = score
        #         best_move = move
        # print(f'TIME: {time.time() - start_time}')
        # return best_move
        """ Process """
        processes = []
        returned_scores = []
        start_time = time.time()
        for move in moves:
            process_score = Value('d', 0.0)
            returned_scores.append(process_score)
            p = Process(target=self.run_minimax, args=(board, self.depth, move, process_score))
            processes.append(p)
            p.start()
        for process in processes:
            process.join()
        print(f'TIME: {time.time() - start_time}')
        scores = [process_score.value for process_score in returned_scores]
        if self.is_white:
            return moves[max(range(len(scores)), key=scores.__getitem__)]
        else:
            return moves[min(range(len(scores)), key=scores.__getitem__)]

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