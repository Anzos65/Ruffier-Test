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
vline1 = QVBoxLayout()
def toWin2():
    win1.hide()
    win2.show()

vline1.addWidget(label1, alignment = Qt.AlignLeft)
vline1.addWidget(label2, alignment = Qt.AlignLeft)
vline1.addWidget(start, alignment = Qt.AlignCenter)
win1.setLayout(vline1)

start.clicked.connect(toWin2)

win1.show()
app.exec_()
