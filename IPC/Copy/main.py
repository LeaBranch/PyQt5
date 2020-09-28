import sys
import time
import os
import math

from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import (QApplication, QDialog,
                             QProgressBar, QPushButton, QSizePolicy)

class External(QThread):

    countChanged = pyqtSignal(int)

    def run(self):
        name = sys.argv[1]
        fdr = open(name, "r")
        size = os.path.getsize(name)
        onePer = size / 100
        newOnePer = math.ceil(onePer) 

        new_name = name.split('.')
        fin_name=new_name[0] + "(1)." + new_name[1]
        fdw = open(fin_name, "w")

        count = 0
        while(count < 100):
            text = fdr.read(newOnePer)
            fdw.write(text)
            count = count + 1
            self.countChanged.emit(count)
        fdr.close()
        fdw.close()

class Actions(QDialog):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle('Progress Bar')
        # self.setHorizontalPolicy(self, QSizePolicy.Fixed)
        self.progress = QProgressBar(self)
        self.progress.setGeometry(5, 5, 300-5, 25)
        self.progress.setMaximum(100)
        self.button = QPushButton('Start', self)
        self.button.move(0, 30)
        self.show()

        self.button.clicked.connect(self.onButtonClick)

    def onButtonClick(self):
        self.calc = External()
        self.calc.countChanged.connect(self.onCountChanged)
        self.calc.start()

    def onCountChanged(self, value):
        self.progress.setValue(value)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Actions()
    window.setHorizontalPolicy(QSizePolicy.Fixed)

    sys.exit(app.exec_())