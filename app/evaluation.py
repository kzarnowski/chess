import chess
import numpy as np


MAX_VALUE = 50000

""" https://www.chessprogramming.org/Point_Value - Larry Kaufman"""
PIECE_VALUES = {
    chess.PAWN: 100,
    chess.KNIGHT: 350,
    chess.BISHOP: 350,
    chess.ROOK: 525,
    chess.QUEEN: 1000,
    chess.KING: MAX_VALUE
}

PAWN_POS_WHITE = np.array([
     0,   0,   0,   0,   0,   0,   0,   0,
     5,  10,  10, -20, -20,  10,  10,   5,
     5,  -5, -10,   0,   0, -10,  -5,   5,
     0,   0,   0,  20,  20,   0,   0,   0,
     5,   5,  10,  25,  25,  10,   5,   5,
    10,  10,  20,  30,  30,  20,  10,  10,
    50,  50,  50,  50,  50,  50,  50,  50,
     0,   0,   0,   0,   0,   0,   0,   0
], dtype=np.int8)
PAWN_POS_BLACK = np.flip(PAWN_POS_WHITE)


KNIGHT_POS_WHITE = np.array([
    -50, -40, -30, -30, -30, -30, -40, -50,
    -40, -20, 0, 0, 0, 0, -20, -40,
    -30, 0, 10, 15, 15, 10, 0, -30,
    -30, 5, 15, 20, 20, 15, 5, -30,
    -30, 0, 15, 20, 20, 15, 0, -30,
    -30, 5, 10, 15, 15, 10, 5, -30,
    -40, -20, 0, 5, 5, 0, -20, -40,
    -50, -40, -30, -30, -30, -30, -40, -50
], dtype=np.int8)
KNIGHT_POS_BLACK = KNIGHT_POS_WHITE


BISHOP_POS_WHITE = np.array([
    -20, -10, -10, -10, -10, -10, -10, -20,
    -10, 5, 0, 0, 0, 0, 5, -10,
    -10, 10, 10, 10, 10, 10, 10, -10,
    -10, 0, 10, 10, 10, 10, 0, -10,
    -10, 5, 5, 10, 10, 5, 5, -10,
    -10, 0, 5, 10, 10, 5, 0, -10,
    -10, 0, 0, 0, 0, 0, 0, -10,
    -20, -10, -10, -10, -10, -10, -10, -20
], dtype=np.int8)
BISHOP_POS_BLACK = np.flip(BISHOP_POS_WHITE)


ROOK_POS_WHITE = np.array([
    0, 0, 0, 5, 5, 0, 0, 0,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    5, 10, 10, 10, 10, 10, 10, 5,
    0, 0, 0, 0, 0, 0, 0, 0
], dtype=np.int8)
ROOK_POS_BLACK = np.flip(ROOK_POS_WHITE)


QUEEN_POS_WHITE = np.array([
    -20, -10, -10, -5, -5, -10, -10, -20,
    -10, 0, 0, 0, 0, 0, 0, -10,
    -10, 0, 5, 5, 5, 5, 0, -10,
    -5, 0, 5, 5, 5, 5, 0, -5,
    0, 0, 5, 5, 5, 5, 0, -5,
    -10, 5, 5, 5, 5, 5, 0, -10,
    -10, 0, 5, 0, 0, 0, 0, -10,
    -20, -10, -10, -5, -5, -10, -10, -20
], dtype=np.int8)
QUEEN_POS_BLACK = QUEEN_POS_WHITE


KING_POS_WHITE = np.array([
    20, 30, 10, 0, 0, 10, 30, 20,
    20, 20, 0, 0, 0, 0, 20, 20,
    -10, -20, -20, -20, -20, -20, -20, -10,
    20, -30, -30, -40, -40, -30, -30, -20,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30
], dtype=np.int8)
KING_POS_BLACK = np.flip(KING_POS_WHITE)


KING_POS_WHITE_ENDGAME = np.array([
    -50, -30, -30, -30, -30, -30, -30, -50,
    -30, -30,  0,  0,  0,  0, -30, -30,
    -30, -10, 20, 30, 30, 20, -10, -30,
    -30, -10, 30, 40, 40, 30, -10, -30,
    -30, -10, 30, 40, 40, 30, -10, -30,
    -30, -10, 20, 30, 30, 20, -10, -30,
    -30, -20, -10,  0,  0, -10, -20, -30,
    -50, -40, -30, -20, -20, -30, -40, -50
], dtype=np.int8)
KING_POS_BLACK_ENDGAME = np.flip(KING_POS_WHITE_ENDGAME)


def is_endgame(board: chess.Board):
    white_queens = len(board.pieces(chess.QUEEN, chess.WHITE))
    black_queens = len(board.pieces(chess.QUEEN, chess.BLACK))
    white_minors = len(board.pieces(chess.BISHOP, chess.WHITE)) + len(board.pieces(chess.KNIGHT, chess.WHITE))
    black_minors = len(board.pieces(chess.BISHOP, chess.BLACK)) + len(board.pieces(chess.KNIGHT, chess.BLACK))
    white_rooks = len(board.pieces(chess.ROOK, chess.WHITE))
    black_rooks = len(board.pieces(chess.ROOK, chess.BLACK))
    no_queens = white_queens + black_queens == 0
    queens_and_minors = white_queens + black_queens == 2 and white_rooks + black_rooks == 0 and white_minors + black_minors <= 2
    queen_vs_two = white_queens == 1 and black_queens == 0 and black_minors + black_rooks <= 2
    two_vs_queen = black_queens == 1 and white_queens == 0 and white_minors + white_rooks <= 2
    return no_queens or queens_and_minors or queen_vs_two or two_vs_queen


def get_board_score(board: chess.Board):
    endgame = is_endgame(board)
    score = 0
    for square, piece in board.piece_map().items():
        value = PIECE_VALUES[piece.piece_type]
        value += get_piece_position_score(piece, square, endgame)
        score += value if piece.color == chess.WHITE else -value       
    return score


def get_move_score(board: chess.Board, move: chess.Move, endgame):
    side = 1 if board.turn == chess.WHITE else -1
    if move.promotion:
        return MAX_VALUE * side

    piece = board.piece_at(move.from_square)
    start_value = get_piece_position_score(piece, move.from_square, endgame)
    end_value = get_piece_position_score(piece, move.to_square, endgame)
    square_change = end_value - start_value

    capture_change = 0
    if board.is_capture(move):
        capture_change = get_capture_score(board, move)
    
    move_evaluation = (square_change + capture_change) * side
    return move_evaluation

def get_piece_position_score(piece: chess.Piece, square: chess.Square, endgame: bool):
    is_white = piece.color == chess.WHITE
    if piece.piece_type == chess.PAWN:
        table = PAWN_POS_WHITE if is_white else PAWN_POS_BLACK
    elif piece.piece_type == chess.KNIGHT:
        table = KNIGHT_POS_WHITE if is_white else KNIGHT_POS_BLACK
    elif piece.piece_type == chess.BISHOP:
        table = BISHOP_POS_WHITE if is_white else BISHOP_POS_BLACK
    elif piece.piece_type == chess.ROOK:
        table = ROOK_POS_WHITE if is_white else ROOK_POS_BLACK
    elif piece.piece_type == chess.QUEEN:
        table = QUEEN_POS_WHITE if is_white else QUEEN_POS_BLACK
    elif endgame:
        table = KING_POS_WHITE_ENDGAME if is_white else KING_POS_BLACK_ENDGAME
    else:
        table = KING_POS_WHITE if is_white else KING_POS_BLACK
    return table[square]

def get_capture_score(board: chess.Board, move: chess.Move):
    if board.is_en_passant(move):
        return PIECE_VALUES[chess.PAWN]
    move_piece = board.piece_at(move.from_square)
    captured_piece = board.piece_at(move.to_square)
    captured_piece_score = PIECE_VALUES[captured_piece.piece_type] + get_piece_position_score(captured_piece, move.to_square, False)
    capture_evaluation = PIECE_VALUES[move_piece.piece_type] - captured_piece_score
    return capture_evaluation
