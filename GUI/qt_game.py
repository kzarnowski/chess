from PyQt5.QtWidgets import QFrame, QVBoxLayout, QHBoxLayout, QPushButton, QLabel
from PyQt5.QtCore import QThreadPool
from GUI.qt_board import QtBoard
from GUI.qt_sidebar import QtSidebar

class QtGame(QFrame):
    def __init__(self, main_window):
        QFrame.__init__(self)
        self.parent = main_window
        self.game_handler = None

        self.qt_board = QtBoard(self)
        self.qt_sidebar = QtSidebar(self, main_window)

        layout = QHBoxLayout()
        layout.addWidget(self.qt_board, 3)
        layout.addWidget(self.qt_sidebar, 1)

        self.setLayout(layout)

        self.threadpool = QThreadPool()

    def new_game(self, engine_is_white, board_color_num):
        self.qt_board.set_squares_color(board_color_num)
        self.qt_board.display_starting_position(engine_is_white)
        self.qt_board.setEnabled(True)
        self.qt_sidebar.notation.setText('')
        self.set_info('New Game')

    def get_promotion_piece(self, is_white):
        piece = self.qt_board.get_promotion_piece(is_white)
        return piece
    
    def display_result(self, result):
        self.set_info(f'Result: {result}')
        self.qt_board.setEnabled(False)
    
    def update_notation(self, move_san, half_move_num):
        full_move_num = half_move_num // 2 + 1
        is_white_move = not half_move_num % 2
        current_text = self.qt_sidebar.notation.toPlainText()
        if is_white_move:
            notation = current_text + ' ' + str(full_move_num) + '. ' + move_san
        else:
            notation = current_text + ',  ' + move_san
        self.qt_sidebar.notation.setText(notation) 
    
    def update_fen(self, fen_str):
        self.qt_sidebar.fen.setText(fen_str)

    def set_info(self, info):
        self.qt_sidebar.info.setText(info)
    
    def get_handler(self):
        return self.game_handler

    def set_controls_enabled(self, is_enabled):
        self.qt_sidebar.undo.setEnabled(is_enabled)
        self.qt_sidebar.resign.setEnabled(is_enabled)
        self.qt_sidebar.draw.setEnabled(is_enabled)

    
