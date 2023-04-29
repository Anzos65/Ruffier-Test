from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout

app = QApplication([])

win1= QWidget()
win1.setWindowTitle("Ruffier Test")
win1.setMinimumSize(600,400)

win2= QWidget()
win2.setWindowTitle("Ruffier Test")
win2.setMinimumSize(600,400)

win3= QWidget()
win3.setWindowTitle("Ruffier Test")
win3.setMinimumSize(600,400)

#First window items
label1 = QLabel("intro")
label2 = QLabel("long intro text")
start = QPushButton("Start")
hline1 = QHBoxLayout()
hline2 = QHBoxLayout()
hline3 = QHBoxLayout()
def toWin2():
    win1.hide()
    win2.show()

hline1.addWidget(label1, alignment = Qt.AlignLeft)
hline2.addWidget(label2, alignment = Qt.AlignLeft)
hline3.addWidget(start, alignment = Qt.AlignCenter)

layout1 = QVBoxLayout()
layout1.addLayout(hline1)
layout1.addLayout(hline2)
layout1.addLayout(hline3)
win1.setLayout(layout1)
