from PyQt5.QtWidgets import QFrame, QVBoxLayout, QHBoxLayout, QTextEdit, QLabel, QPushButton, QApplication, QFileDialog
from GUI.qt_menu import QtMenuButton

class QtAnalysisSidebar(QFrame):
    def __init__(self, parent, main_window):
        QFrame.__init__(self)
        self.parent = parent
        self.main_window = main_window

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.notation = QTextEdit()
        self.notation.setReadOnly(True)
        self.import_pgn = QPushButton('Import PGN')
        self.import_pgn.clicked.connect(self.import_pgn_clicked)

        self.fen = QTextEdit()
        self.fen.setReadOnly(True)
        self.fen.setFixedHeight(100)

        self.info = QLabel("Info")
        self.copy_fen = QPushButton('Copy FEN')
        self.copy_fen.clicked.connect(self.copy_fen_clicked)

        buttons = QHBoxLayout()
        previous_move = QPushButton('←')
        next_move = QPushButton('→')
        buttons.addWidget(previous_move)
        buttons.addWidget(next_move)

        layout.addWidget(QLabel('PGN'))
        layout.addWidget(self.notation)
        layout.addWidget(self.import_pgn)
        layout.addWidget(QLabel('FEN'))
        layout.addWidget(self.fen)
        layout.addWidget(self.copy_fen)
        layout.addLayout(buttons)
        layout.addWidget(QtMenuButton(self.main_window))
        layout.addWidget(self.info)

    def copy_fen_clicked(self):
        cb = QApplication.clipboard()
        cb.clear(mode=cb.Clipboard)
        cb.setText(self.fen.toPlainText(), mode=cb.Clipboard)
    
    def import_pgn_clicked(self):
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.ExistingFile)
        filename = dialog.getOpenFileName(filter='(*.pgn)')[0]
        if filename:
            self.parent.analysis_handler.import_pgn(filename)