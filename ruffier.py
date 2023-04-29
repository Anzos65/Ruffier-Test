from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel

app = QApplication([])
win1= QWidget()
win2= QWidget()
win3= QWidget()

win1.setWindowTitle("Ruffier Test")
win1.show()

app.exec_()