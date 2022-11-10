import os
import string

FEN_PIECES = 'rnbqkpRNBQKP'

def get_piece_png_path(fen):
    root = os.path.join('images', 'pieces')
    color = 'w' if fen.isupper() else 'b'
    piece = fen.lower()
    return os.path.join(root, color+piece)

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


LANG = {
    'game': {
        'export_pgn': {
            'EN': 'Export PGN',
            'PL': 'Zapisz PGN'
        },
        'copy_fen': {
            'EN': 'Copy FEN',
            'PL': 'Kopiuj FEN'
        },
        'resign': {
            'EN': 'Resign',
            'PL': 'Poddaj się'
        },
        'menu': {
            'EN': 'Menu',
            'PL': 'Menu'
        },
        'your_turn': {
            'EN': 'Your turn',
            'PL': 'Twój ruch'
        },
        'engine_turn': {
            'EN': 'Computer is thinking...',
            'PL': 'Komputer myśli...'
        },
        'result': {
            'EN': 'Result',
            'PL': 'Wynik'
        }
    },
    'menu': {
        'new_game': {
            'EN': 'New Game',
            'PL': 'Nowa Gra'
        },
        'settings': {
            'EN': 'Settings',
            'PL': 'Opcje'
        },
        'exit': {
            'EN': 'Exit',
            'PL': 'Zamknij'
        }
    },
    'settings': {
        'play_as': {
            'title': {
                'EN': 'Play as:',
                'PL': 'Graj jako:'
            },
            'random': {
                'EN': 'Random',
                'PL': 'Losowo'
            },
            'white': {
                'EN': 'White',
                'PL': 'Białe'
            },
            'black': {
                'EN': 'Black',
                'PL': 'Czarne'
            },
        },
        'language': {
            'title': {
                'EN': 'Choose language:',
                'PL': 'Wybierz język:'
            },
            'english': {
                'EN': 'English',
                'PL': 'angielski'
            },
            'polish': {
                'EN': 'Polish',
                'PL': 'polski'
            }
        },
        'board_color': {
            'title': {
                'EN': 'Board color:',
                'PL': 'Kolor szachownicy:'
            }
        },
        'engine_level': {
            'title': {
                'EN': 'Engine level',
                'PL': 'Poziom silnika'
            },
            'easy': {
                'EN': 'Easy',
                'PL': 'Łatwy'
            },
            'medium': {
                'EN': 'Medium',
                'PL': 'Średni'
            },
            'hard': {
                'EN': 'Hard',
                'PL': 'Trudny'
            }
        },
        'save': {
            'EN': 'Save',
            'PL': 'Zapisz'
        },
        'cancel': {
            'EN': 'Cancel',
            'PL': 'Anuluj'
        }
    }
}