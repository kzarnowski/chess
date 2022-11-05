from PyQt5.QtWidgets import QFrame, QVBoxLayout, QLabel, QTextEdit, QPushButton, QFileDialog, QApplication
from GUI.qt_menu import QtMenuButton

class QtSidebar(QFrame):
    def __init__(self, parent, main_window):
        QFrame.__init__(self)
        self.parent = parent
        self.main_window = main_window

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.notation = QTextEdit()
        self.notation.setReadOnly(True)

        self.fen = QTextEdit()
        self.fen.setReadOnly(True)
        self.fen.setFixedHeight(100)

        self.info = QLabel("Info")
        
        self.export_pgn = QPushButton('Export PGN')
        self.export_pgn.clicked.connect(self.export_pgn_clicked)
        self.copy_fen = QPushButton('Copy FEN')
        self.copy_fen.clicked.connect(self.copy_fen_clicked)
        layout.addWidget(QLabel('PGN'))
        layout.addWidget(self.notation)
        layout.addWidget(self.export_pgn)
        layout.addWidget(QLabel('FEN'))
        layout.addWidget(self.fen)
        layout.addWidget(self.copy_fen)
        layout.addWidget(QtMenuButton(self.main_window))
        layout.addWidget(self.info)

    def export_pgn_clicked(self):
        pgn = self.parent.game_handler.get_pgn()
        filename = QFileDialog.getSaveFileName(filter='(*.pgn)')[0]
        if filename:
            print(pgn, file=open(filename, "w"), end="\n\n")
    
    def copy_fen_clicked(self):
        cb = QApplication.clipboard()
        cb.clear(mode=cb.Clipboard)
        cb.setText(self.fen.toPlainText(), mode=cb.Clipboard)