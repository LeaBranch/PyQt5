from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication

from gui import Ui_MainWindow  # импорт нашего сгенерированного файла
import sys

p = ''
sum_x = ''
sum_o = ''
count = 1
win = [123, 132, 213, 231, 321, 312,
456, 465, 546, 564, 645, 654,
789, 798, 879, 897, 978, 987,
159, 195, 519, 591, 915, 951,
357, 375, 537, 573, 735, 753,
147, 174, 417, 471, 714, 741,
258, 285, 528, 582, 825, 852,
369, 396, 639, 396, 936, 963]

def bubbleSort(a):
    s = len(a)
    for i in range(s):
        for j in range(s-1):
            if (a[j] > a[j+1]):
                tmp = a[j]
                a[j] = a[j+1]
                a[j+1] = tmp


class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.oneFunc)
        self.ui.pushButton_2.clicked.connect(self.twoFunc)
        self.ui.pushButton_3.clicked.connect(self.threeFunc)
        self.ui.pushButton_4.clicked.connect(self.fourFunc)
        self.ui.pushButton_5.clicked.connect(self.fiveFunc)
        self.ui.pushButton_6.clicked.connect(self.sixFunc)
        self.ui.pushButton_7.clicked.connect(self.sevenFunc)
        self.ui.pushButton_8.clicked.connect(self.eightFunc)
        self.ui.pushButton_9.clicked.connect(self.nineFunc)
        self.ui.pushButton_Restart.clicked.connect(self.ResetFunc)

    def setPBFunc(self, pb, p, t):
        pb.setText(p)
        pb.setEnabled(t)

    def checkToWinFunc(self, p, num):
        global sum_x
        global sum_o

        if (p == "X"):
            sum_x = sum_x + str(num)
            print("sum_x: ", sum_x)
            if (int(sum_x) in win):
                print("X winner!")
                self.ui.lineEdit.setText("X winner!")
        if (p == "O"):
            sum_o = sum_o + str(num)
            print("sum_o: ", sum_o)
            if (int(sum_o) in win):
                print("O winner!")
                self.ui.lineEdit.setText("O winner!")

    def countFunc(self, pb, num):
        global count
        global p
        count = count + 1
        if (count %2 == 0): 
        	p = 'X'
        else: 
            p = 'O'
        self.setPBFunc(pb, p, False)
        self.checkToWinFunc(p, num)

    def oneFunc(self):
        self.countFunc(self.ui.pushButton, 1)
    
    def twoFunc(self):
        self.countFunc(self.ui.pushButton_2, 2)

    def threeFunc(self):
        self.countFunc(self.ui.pushButton_3, 3)

    def fourFunc(self):
        self.countFunc(self.ui.pushButton_4, 4)

    def fiveFunc(self):
        self.countFunc(self.ui.pushButton_5, 5)

    def sixFunc(self):
        self.countFunc(self.ui.pushButton_6, 6)

    def sevenFunc(self):
        self.countFunc(self.ui.pushButton_7, 7)

    def eightFunc(self):
        self.countFunc(self.ui.pushButton_8, 8)

    def nineFunc(self):
        self.countFunc(self.ui.pushButton_9, 9)

    def ResetFunc(self):
        global p
        global sum_x
        global sum_o
        global count
        p = ''
        sum_x = ''
        sum_o = ''
        count = 1
        self.setPBFunc(self.ui.pushButton, p, True)
        self.setPBFunc(self.ui.pushButton_2, p, True)
        self.setPBFunc(self.ui.pushButton_3, p, True)
        self.setPBFunc(self.ui.pushButton_4, p, True)
        self.setPBFunc(self.ui.pushButton_5, p, True)
        self.setPBFunc(self.ui.pushButton_6, p, True)
        self.setPBFunc(self.ui.pushButton_7, p, True)
        self.setPBFunc(self.ui.pushButton_8, p, True)
        self.setPBFunc(self.ui.pushButton_9, p, True)
        self.ui.lineEdit.setText(p)


    def keyPressEvent(self, e):
	    if e.key() == Qt.Key_Escape:
	        self.close()


 
app = QtWidgets.QApplication([])
application = mywindow()
application.show()
 
sys.exit(app.exec())