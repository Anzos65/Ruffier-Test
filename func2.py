from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit

age = 0
hr1 = 0
hr2 = 0
hr3 = 0

def check(line2, line3, line4, line5):
    age=line2.text()
    hr1=line3.text()
    hr2=line4.text()
    hr3=line5.text()
    print(age, hr1, hr2, hr3)
