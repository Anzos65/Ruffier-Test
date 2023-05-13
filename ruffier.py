from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit
from instr import *

app = QApplication([])

win1= QWidget()
win1.setWindowTitle("Ruffier Test")
win1.setMinimumSize(win_width, win_height)

win2= QWidget()
win2.setWindowTitle("Ruffier Test")
win2.setMinimumSize(win_width, win_height)

win3= QWidget()
win3.setWindowTitle("Ruffier Test")
win3.setMinimumSize(win_width, win_height)

#First window items
label1 = QLabel("lorem ipsum dolor sit amet")
label2 = QLabel("lorem ipsum dolor sit amet")
start1 = QPushButton("Start")
vline1 = QVBoxLayout()
def toWin2():
    win1.hide()
    win2.show()

vline1.addWidget(label1, alignment = Qt.AlignLeft)
vline1.addWidget(label2, alignment = Qt.AlignLeft)
vline1.addWidget(start1, alignment = Qt.AlignCenter)
win1.setLayout(vline1)

#Second window items
label3 = QLabel("Enter your full name:")
line1 = QLineEdit("Full name")
label4 = QLabel("Full years:")
line2 = QLineEdit("0")
label5 = QLabel("lorem ipsum dolor sit amet")
but1 = QPushButton("Start the first test")
line3 = QLineEdit("0")
label6 = QLabel("lorem ipsum dolor sit amet")
but2 = QPushButton("Start doing squats")
label7 = QLabel("lorem ipsum dolor sit amet")
but3 = QPushButton("Start the final test")
line4 = QLineEdit("0")
line5 = QLineEdit("0")
start2 = QPushButton("Send the results")
def toWin3():
    win2.hide()
    win3.show()

vline2 = QVBoxLayout()
vline3 = QVBoxLayout()
layout1 = QHBoxLayout()

vline2.addWidget(label3, alignment = Qt.AlignLeft)
vline2.addWidget(line1, alignment = Qt.AlignLeft)
vline2.addWidget(label4, alignment = Qt.AlignLeft)
vline2.addWidget(line2, alignment = Qt.AlignLeft)
vline2.addWidget(label5, alignment = Qt.AlignLeft)
vline2.addWidget(but1, alignment = Qt.AlignLeft)
vline2.addWidget(line3, alignment = Qt.AlignLeft)
vline2.addWidget(label6, alignment = Qt.AlignLeft)
vline2.addWidget(but2, alignment = Qt.AlignLeft)
vline2.addWidget(label7, alignment = Qt.AlignLeft)
vline2.addWidget(but3, alignment = Qt.AlignLeft)
vline2.addWidget(line4, alignment = Qt.AlignLeft)
vline2.addWidget(line5, alignment = Qt.AlignLeft)
vline2.addWidget(start2, alignment = Qt.AlignCenter)

layout1.addLayout(vline2)
layout1.addLayout(vline3)
win2.setLayout(layout1)

#Third window items
label8 = QLabel("lorem ipsum dolor sit amet")
label9 = QLabel("lorem ipsum dolor sit amet")
vline4 = QVBoxLayout()

vline4.addWidget(label8, alignment = Qt.AlignCenter)
vline4.addWidget(label9, alignment = Qt.AlignCenter)
win3.setLayout(vline4)


start1.clicked.connect(toWin2)
start2.clicked.connect(toWin3)

win1.show()
app.exec_()
