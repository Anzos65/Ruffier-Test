from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit 
from instr import *
from window3 import Window3


class Window2(QWidget):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ruffier Test")
        self.setMinimumSize(win_width,win_height)
        
        self.nameLabel = QLabel(txt_name)
        self.nameInput = QLineEdit(txt_hintname)

        self.ageLabel = QLabel(txt_age)
        self.ageInput = QLineEdit(txt_hintage)

        self.test1Label = QLabel(txt_test1)
        self.test1Button = QPushButton(txt_starttest1)
        self.test1Input = QLineEdit(txt_hinttest1)

        self.test2Label = QLabel(txt_test2)
        self.test2Button = QPushButton(txt_starttest2)
        self.test2Input = QLineEdit(txt_hinttest2)
        self.test2Button.clicked.connect(self.timerEvent)

        self.test3Label = QLabel(txt_test3)
        self.test3Button = QPushButton(txt_starttest3)
        self.test3Input = QLineEdit(txt_hinttest3)

        self.nextButton = QPushButton(txt_sendresults)
        self.nextButton.clicked.connect(self.showNextWindow)

        self.vline = QVBoxLayout()
        self.vline2 = QVBoxLayout()
        self.hline = QHBoxLayout()

        self.vline.addWidget(self.nameLabel, alignment = Qt.AlignLeft )
        self.vline.addWidget(self.nameInput, alignment = Qt.AlignLeft )

        self.vline.addWidget(self.ageLabel, alignment = Qt.AlignLeft )
        self.vline.addWidget(self.ageInput, alignment = Qt.AlignLeft )

        self.vline.addWidget(self.test1Label, alignment = Qt.AlignLeft )
        self.vline.addWidget(self.test1Button, alignment = Qt.AlignLeft )
        self.vline.addWidget(self.test1Input, alignment = Qt.AlignLeft )

        self.vline.addWidget(self.test2Label, alignment = Qt.AlignLeft )
        self.vline.addWidget(self.test2Button, alignment = Qt.AlignLeft )
        self.vline.addWidget(self.test2Input, alignment = Qt.AlignLeft )

        self.vline.addWidget(self.test3Label, alignment = Qt.AlignLeft )
        self.vline.addWidget(self.test3Button, alignment = Qt.AlignLeft )
        self.vline.addWidget(self.test3Input, alignment = Qt.AlignLeft )

        self.vline.addWidget(self.nextButton, alignment = Qt.AlignLeft )

        self.hline.addLayout(self.vline)
        self.hline.addLayout(self.vline2)

        self.setLayout(self.hline)


    def timerEvent(self):
        complete = False
        time = QTime(15,0,0)
        while complete == False:
            time = time.addSecs(-1)
            print(time)
            if time.toString("hh:mm:ss") == "00:00:00":
                complete=True
            print('Timer complete')

    def showNextWindow(self):
        next_window = Window3()
        self.hide()
        next_window.show()