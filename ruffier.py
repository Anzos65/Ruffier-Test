from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit 
from instr import *
from func import check

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
label1 = QLabel(txt_hello)
label2 = QLabel(txt_instruction)
start1 = QPushButton(txt_next)
vline1 = QVBoxLayout()
def toWin2():
    win1.hide()
    win2.show()

vline1.addWidget(label1, alignment = Qt.AlignLeft)
vline1.addWidget(label2, alignment = Qt.AlignLeft)
vline1.addWidget(start1, alignment = Qt.AlignCenter)
win1.setLayout(vline1)

#Second window items
def timerEvent():
    complete=False
    time = QTime(15, 0, 0)
    while complete == False:
        time = time.addSecs(-1)
        print(time)
        if time.toString("hh:mm:ss") == "00:00:00":
            timer.stop()
            complete=True
            print('Timer complete')

label3 = QLabel(txt_name)
line1 = QLineEdit(txt_hintname)
label4 = QLabel(txt_age)
line2 = QLineEdit(txt_hintage)
label5 = QLabel(txt_test1)
but1 = QPushButton(txt_starttest1)
line3 = QLineEdit(txt_hinttest1)
label6 = QLabel(txt_test2)
but2 = QPushButton(txt_starttest2)
but2.clicked.connect(timerEvent)
label7 = QLabel(txt_test3)
but3 = QPushButton(txt_starttest3)
line4 = QLineEdit(txt_hinttest2)
line5 = QLineEdit(txt_hinttest3)
start2 = QPushButton(txt_sendresults)
def toWin3():
    win2.hide()
    win3.show()
    values = check(line2, line3, line4, line5)

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
label8 = QLabel(txt_index)
label9 = QLabel(txt_workheart)
vline4 = QVBoxLayout()

vline4.addWidget(label8, alignment = Qt.AlignCenter)
vline4.addWidget(label9, alignment = Qt.AlignCenter)
win3.setLayout(vline4)

start1.clicked.connect(toWin2)
start2.clicked.connect(toWin3)

win1.show()
app.exec_()
