from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QDesktopWidget

from gui import Ui_MainWindow  # импорт нашего сгенерированного файла
import sys
 
name = ''

class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.label.setText(name)


    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()
 
app = QtWidgets.QApplication([])

# разрешение экрана:
q= QDesktopWidget().availableGeometry()

if (len(sys.argv) != 2):
    print("Usage: Chat <name>")
    sys.exit()
else: name = sys.argv[1]

application = mywindow()
application.show()
 
sys.exit(app.exec())