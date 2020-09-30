from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QDesktopWidget

from gui import Ui_MainWindow  # импорт нашего сгенерированного файла
import sys
 
name = ''
with open("log.txt") as f:
    text = f.read()

class Output(QtCore.QThread):
    global text
    # text = f.read()
    mySignal1 = QtCore.pyqtSignal()
    mySignal2 = QtCore.pyqtSignal(str)
    def __init__(self, parent=None):
        QtCore.QThread.__init__(self, parent)
        def run(self):
                self.mySignal1.emit()
                self.mySignal2.emit(text)
                print(text)

class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.label.setText(name)

        self.outputObject = Output()
        self.outputObject.start()
        # print(text)

        self.outputObject.mySignal1.connect(self.onOutput1, Qt.QueuedConnection)
        # self.outputObject.mySignal2.connect(self.onOutput2, Qt.QueuedConnection)

    def onOutput1(self):
        self.ui.output.clear()
        print(text)
        

    # def onOutput2(self, text):
        # self.ui.output.setText(text)

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            f.close()
            self.close()
 
app = QtWidgets.QApplication([])

# разрешение экрана:
q= QDesktopWidget().availableGeometry()

if (len(sys.argv) != 2):
    print("Usage: Chat <name>")
    sys.exit()
name = sys.argv[1]


application = mywindow()
application.show()
 
sys.exit(app.exec())