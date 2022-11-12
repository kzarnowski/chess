from app.engine import Engine
import chess

engine = Engine(False, 6)
progress = ''
board = chess.Board()
board.set_fen('r3k2r/p1ppqp2/1n2pnp1/3PN3/1p2P3/2N2Q2/PPPB1PpP/R3K2R b - - 0 1')
print(board)

move1 = engine.get_best_move(board, progress)
print(move1)
board.push(move1)