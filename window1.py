from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit
from instr import *
from window2 import Window2

class Window1(QWidget):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ruffier Test")
        self.setMinimumSize(win_width,win_height)
        
        self.helloLabel = QLabel(txt_hello)
        self.instructionsLabel = QLabel(txt_instruction)
        self.startButton = QPushButton(txt_next)
        self.startButton.clicked.connect(self.showNextWindow)
        self.vline = QVBoxLayout()
        self.vline.addWidget(self.helloLabel, alignment = Qt.AlignLeft)
        self.vline.addWidget(self.instructionsLabel, alignment = Qt.AlignLeft)
        self.vline.addWidget(self.startButton, alignment = Qt.AlignCenter)
        self.setLayout(self.vline)

    def showNextWindow(self):
        next_window = Window2()
        self.hide()
        next_window.show()