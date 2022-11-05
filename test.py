from PyQt5 import QtWidgets
from multiprocessing import Pool, cpu_count


def run(move, board, depth):
    print(move, ' ', board, ' ', depth)
    return move*2

if __name__ == "__main__":
    processes = cpu_count()
    board = 20
    depth = 30
    with Pool(processes=processes) as p:
        res = p.starmap(run, [
            (1, board, depth),
            (2, board, depth),
            (3, board, depth),
            (4, board, depth),
            (5, board, depth),
            (6, board, depth),
            (7, board, depth),
            (8, board, depth),
        ])
        print(res)

    args = [(1, board, depth),
            (2, board, depth),
            (3, board, depth),
            (4, board, depth),
            (5, board, depth),
            (6, board, depth),
            (7, board, depth),
            (8, board, depth)]
    
    for x, y, z in args:
        print(x, y, z)
    