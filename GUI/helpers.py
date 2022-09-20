import os
import string

FEN_PIECES = 'rnbqkpRNBQKP'

def get_piece_png_path(fen):
    from GUI.config import theme
    root = os.path.join('images', 'pieces')
    color = 'w' if fen.isupper() else 'b'
    piece = fen.lower()
    return os.path.join(root, theme, color+piece)

def an2rc(an, is_flipped):
    """ Convert algebraic notation (a8, c7) to a (r,c) pair """
    if is_flipped:
        r = int(an[1]) - 1      
        c = 7 - (ord(an[0]) - 97) # a = 7, ..., h = 0
    else:
        r = 8 - int(an[1])
        c = ord(an[0]) - 97 # a = 0, ..., h = 7
    return r, c

def rc2an(rc, is_flipped):
    """ Convert (r, c) pair to algebraic notation (a8, c7)"""
    if is_flipped:
        rank = str(rc[0] + 1)
        file = chr(104 - rc[1])
    else:
        rank = str(8 - rc[0])
        file = chr(rc[1] + 97)
    return file + rank