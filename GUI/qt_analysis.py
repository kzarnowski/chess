from PyQt5.QtWidgets import QFrame, QHBoxLayout
from GUI.qt_board import QtBoard
from GUI.qt_analysis_sidebar import QtAnalysisSidebar
from PyQt5.QtCore import QThreadPool

class QtAnalysis(QFrame):
    def __init__(self, main_window):
        QFrame.__init__(self)
        self.parent = main_window
        self.analysis_handler = None
        self.qt_board = QtBoard(self)
        self.qt_sidebar = QtAnalysisSidebar(self, main_window)

        layout = QHBoxLayout()
        layout.addWidget(self.qt_board, 3)
        layout.addWidget(self.qt_sidebar, 1)

        self.setLayout(layout)
        self.threadpool = QThreadPool()

    def new_analysis(self, engine_is_white, board_color_num):
        self.qt_board.set_squares_color(board_color_num)
        self.qt_board.display_starting_position(engine_is_white)
        self.qt_board.setEnabled(True)
    
    def get_handler(self):
        return self.analysis_handler
    
    def set_info(self, info):
        self.qt_sidebar.info.setText(info)
