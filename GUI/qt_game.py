from PyQt5.QtWidgets import QFrame, QVBoxLayout, QHBoxLayout, QPushButton, QLabel
from PyQt5.QtCore import QThreadPool
from PyQt5.QtGui import QTextCursor
from GUI.sidebars.qt_left_sidebar import QtLeftSidebar
from GUI.sidebars.qt_right_sidebar import QtRightSidebar
from GUI.qt_board import QtBoard
from GUI.qt_header import QtHeader
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


    def move_was_made(self, an_start, an_end):
        self.qt_board.move_was_made(an_start, an_end)
    
    def kingside_castle(self, is_white):
        self.qt_board.kingside_castle(is_white)

    def queenside_castle(self, is_white):
        self.qt_board.queenside_castle(is_white)
    
    def en_passant(self, active_an, an, an_to_remove):
        self.qt_board.en_passant(active_an, an, an_to_remove)
    
    def promotion(self, active_an, an, new_piece_symbol):
        self.qt_board.promotion(active_an, an, new_piece_symbol)
    
    def get_promotion_piece(self, is_white):
        piece = self.qt_board.get_promotion_piece(is_white)
        return piece
    
    def display_result(self, result):
        self.qt_sidebar.info.setText(f'Result: {result}')
    
    def update_notation(self, move_san, half_move_num):
        full_move_num = half_move_num // 2 + 1
        is_white_move = not half_move_num % 2
        current_text = self.qt_sidebar.notation.toPlainText()
        if is_white_move:
            notation = current_text + str(full_move_num) + '. ' + move_san
        else:
            notation = current_text + ',  ' + move_san + '\n'
        self.qt_sidebar.notation.setText(notation) 
    
    def update_fen(self, fen_str):
        self.qt_sidebar.fen.setText(fen_str)

    
