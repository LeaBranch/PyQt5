from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QDesktopWidget

from gui import Ui_MainWindow  # импорт нашего сгенерированного файла
import sys, os
 

name = ''

class Output(QtCore.QThread):
    global f
    mySignal1 = QtCore.pyqtSignal(str)

    def __init__(self, parent=None):
        QtCore.QThread.__init__(self, parent)

    def run(self):
        text = f.read()
        self.mySignal1.emit(text)

class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.label.setText(name)

        self.outputObject = Output()
        self.outputObject.start()
        self.outputObject.mySignal1.connect(self.onOutput1, Qt.QueuedConnection)
        
    def onOutput1(self, text):
        self.ui.output.clear()
        self.ui.output.setText(text)
        
    def keyPressEvent(self, e):
        global f
        if e.key() == Qt.Key_Escape:
            f.close()
            self.close()
 
# --------------------------------------------------------

if (len(sys.argv) != 2):
    print("Usage: Chat <name>")
    sys.exit()
name = sys.argv[1]

if (os.path.exists("log.txt")):
    f = open("log.txt")
else: 
    f = open("log.txt", "w")
    f.close()
    f = open("log.txt")

app = QtWidgets.QApplication([])

# разрешение экрана:
q= QDesktopWidget().availableGeometry()


application = mywindow()
application.show()
 
sys.exit(app.exec())