from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit 
from instr import *

class Window3(QWidget):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ruffier Test")
        self.setMinimumSize(win_width,win_height)

        self.indexLabel = QLabel(txt_index)
        self.workHeartLabel = QLabel(txt_workheart)
        self.vline = QVBoxLayout()

        self.vline.addWidget(self.indexLabel, alignment = Qt.AlignCenter)
        self.vline.addWidget(self.workHeartLabel, alignment = Qt.AlignCenter)

        self.setLayout(self.vline)