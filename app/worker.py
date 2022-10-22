"""
Kod ponizszego pliku został zaczerpnięty z:
https://www.pythonguis.com/tutorials/multithreading-pyqt-applications-qthreadpool/
"""

from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot, QRunnable
from chess import Move
import traceback
import sys

class Signals(QObject):
    finished = pyqtSignal()
    error = pyqtSignal(tuple)
    result = pyqtSignal(Move)
    progress = pyqtSignal(str)

class EngineWorker(QRunnable):
    def __init__(self, engine, board, depth):
        super(EngineWorker, self).__init__()
        
        self.signals = Signals()
        self.engine = engine
        self.board = board 
        self.depth = depth

    @pyqtSlot()
    def run(self):
        try:
            result = self.engine.get_best_move(self.board, self.depth, self.signals.progress)
        except:
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit((exctype, value, traceback.format_exc()))
        else:
            self.signals.result.emit(result)
        finally:
            self.signals.finished.emit()