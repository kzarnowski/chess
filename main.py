from GUI.gui import Gui
from app.app import App
from PyQt5.QtWidgets import QApplication
import sys

if __name__ == '__main__':
    ChessGame = QApplication(sys.argv)
    gui = Gui()
    app = App()
    gui.app = app
    app.gui = gui
    sys.exit(ChessGame.exec_())


    