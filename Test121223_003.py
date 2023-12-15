import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic

import googletrans

form_class = uic.loadUiType("UI_test002.ui")

class MyGoogleTrans(QMainWindow, form_class):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

        self.setWindowTitle("Google 번역기 1.0")
        self.setWindowIcon(QIcon("..\icon\google.png"))
        self.statusBar().showMessage("Google Translator Apps v1.0 copyright 2023")

        self.pushButton.clicked.connect(self.btnClick)
        self.clearbutton.clicked.connect(self.ClearClick)

    def btnClick(self):
        self.textEdit.setText("안녕하세요, Button Clicked")

    def ClearClick(self):
        self.textEdit.clear()

app = QApplication(sys.argv)
myProgram = MyWindow()
myProgram.show()
app.exec_()

