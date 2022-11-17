from PyQt5.QtWidgets import QFrame

class QtAnalysisSidebar(QFrame):
    def __init__(self, parent, main_window):
        QFrame.__init__(self)
        self.parent = parent
        self.main_window = main_window