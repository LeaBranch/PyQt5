from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication

from gui import Ui_MainWindow  # импорт нашего сгенерированного файла
import sys

p = ''
class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
# ====ВЫЗОВ================================================

        # цифры
        self.ui.pushButton_1.clicked.connect(self.oneFunc)
        self.ui.pushButton_2.clicked.connect(self.twoFunc)
        self.ui.pushButton_3.clicked.connect(self.threeFunc)
        self.ui.pushButton_4.clicked.connect(self.fourFunc)
        self.ui.pushButton_5.clicked.connect(self.fiveFunc)
        self.ui.pushButton_6.clicked.connect(self.sixFunc)
        self.ui.pushButton_7.clicked.connect(self.sevenFunc)
        self.ui.pushButton_8.clicked.connect(self.eightFunc)
        self.ui.pushButton_9.clicked.connect(self.nineFunc)
        self.ui.pushButton_0.clicked.connect(self.zeroFunc)

        # символы
        self.ui.pushButton_del.clicked.connect(self.delFunc)
        self.ui.pushButton_equ.clicked.connect(self.equFunc)
        self.ui.pushButton_plus.clicked.connect(self.plusFunc)
        self.ui.pushButton_minus.clicked.connect(self.minusFunc)
        self.ui.pushButton_mult.clicked.connect(self.multFunc)
        self.ui.pushButton_div.clicked.connect(self.divFunc)

# ====СИГНАЛЫ==============================================

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()

# ====ИНИЦИАЛИЗАЦИЯ========================================

    def oneFunc(self):
    	global p
    	p = p + '1'
    	self.ui.lineEdit.setText(p)

    def twoFunc(self):
    	global p
    	p = p + '2'
    	self.ui.lineEdit.setText(p)

    def threeFunc(self):
    	global p
    	p = p + '3'
    	self.ui.lineEdit.setText(p)

    def fourFunc(self):
    	global p
    	p = p + '4'
    	self.ui.lineEdit.setText(p)

    def fiveFunc(self):
    	global p
    	p = p + '5'
    	self.ui.lineEdit.setText(p)

    def sixFunc(self):
    	global p
    	p = p + '6'
    	self.ui.lineEdit.setText(p)

    def sevenFunc(self):
    	global p
    	p = p + '7'
    	self.ui.lineEdit.setText(p)

    def eightFunc(self):
    	global p
    	p = p + '8'
    	self.ui.lineEdit.setText(p)

    def nineFunc(self):
    	global p
    	p = p + '9'
    	self.ui.lineEdit.setText(p)

    def zeroFunc(self):
    	global p

    	if(p.find("/") == (len(p)-1)): 
    		p = 'Division by Zero!'
    	else:
	    	p = p + '0'
    	self.ui.lineEdit.setText(p)

# =========================================================

    def delFunc(self):
    	global p
    	p = ''
    	self.ui.lineEdit.setText(p)

    def equFunc(self):
    	global p
    	p = str(eval(p))
    	# p = str(p)
    	self.ui.lineEdit.setText(p)

    def plusFunc(self):
    	global p
    	p = p + '+'
    	self.ui.lineEdit.setText(p)

    def minusFunc(self):
    	global p
    	p = p + '-'
    	self.ui.lineEdit.setText(p)

    def multFunc(self):
    	global p
    	p = p + '*'
    	self.ui.lineEdit.setText(p)

    def divFunc(self):
    	global p
    	p = p + '/'
    	self.ui.lineEdit.setText(p)

# =========================================================

app = QtWidgets.QApplication([])
application = mywindow()
application.show()

sys.exit(app.exec())