from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit 
from instr import *
from window1 import Window1

app = QApplication([])

startWindow = Window1()
startWindow.show()
app.exec_()