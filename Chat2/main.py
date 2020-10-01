from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QDesktopWidget

from gui import Ui_MainWindow  # импорт нашего сгенерированного файла
import sys, os, time
 

name = ''
# outputText = ''
input_text = ''

class Output(QtCore.QThread):
    global f
    mySignal1 = QtCore.pyqtSignal(str)

    def __init__(self, parent=None):
        QtCore.QThread.__init__(self, parent)

    def run(self):
        global outputText
        while (1):
            outputText = f.read()
            self.mySignal1.emit(outputText)
            f.seek(0)
            # time.sleep(1)


class Input(QtCore.QThread):
    def __init__(self, parent=None):
        QtCore.QThread.__init__(self, parent)

    def run(self):
        global f
        global input_text
        print("this is message:", input_text)
        f.seek(2)
        f.write(name + ": " + input_text + "\n")

class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

# ------вывод имени--------------------
        self.ui.label.setText(name)
# ------включение кнопки---------------
        self.ui.sendButton.clicked.connect(self.inputThreadCall)

# ------вызов потока OUTPUT------------
        self.outputObject = Output()
        self.outputObject.start()

        self.outputObject.mySignal1.connect(self.onOutput, Qt.QueuedConnection)

# ------исполнение GUI для OUTPUT-------------
    def onOutput(self, text):
        # global outputText
        # self.ui.output.clear()
        self.ui.output.setText(text)

# ------вызов потока INPUT-------------
    def inputThreadCall(self):
        global input_text
        input_text = self.ui.input.toPlainText()
        
        self.inputObject = Input()
        self.inputObject.start()

        self.ui.input.clear()
        
    def keyPressEvent(self, e):
        global f
        if e.key() == Qt.Key_Escape:
            f.close()
            self.close()

 
#=======================================================

if (len(sys.argv) != 2):
    print("Usage: Chat <name>")
    sys.exit()
name = sys.argv[1]

f = open("log.txt", "r+")

app = QtWidgets.QApplication([])

# разрешение экрана:
q= QDesktopWidget().availableGeometry()


application = mywindow()
application.show()
 
sys.exit(app.exec())