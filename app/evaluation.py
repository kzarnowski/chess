import chess

""" https://www.chessprogramming.org/Point_Value - Larry Kaufman"""
PIECE_VALUES = {
    chess.PAWN: 100,
    chess.KNIGHT: 350,
    chess.BISHOP: 350,
    chess.ROOK: 525,
    chess.QUEEN: 1000,
    chess.KING: 10000
}


def evaluate_board(board: chess.Board):
    score = 0
    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if not piece:
            continue
        value = PIECE_VALUES[piece.piece_type]
        score += value if piece.color == chess.WHITE else -value
    return score
