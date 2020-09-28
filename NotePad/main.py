from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QFontDialog, QFileDialog
from PyQt5.QtGui import QFont

from gui import Ui_MainWindow  # импорт нашего сгенерированного файла
import sys

i = 0
value = True
font = ''
W = 800
H = 600
fname = ""

class mywindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

# =========================================================
    # File
        new = self.ui.actionNew_File
        new.triggered.connect(self.newFunc)
        new.setShortcut("Ctrl+N")
        new.setStatusTip("Create new file")
        
        open = self.ui.actionOpen
        open.triggered.connect(self.openFunc)
        open.setShortcut("Ctrl+O")
        open.setStatusTip("Open the file")

        save = self.ui.actionSave
        save.triggered.connect(self.saveFunc)
        save.setShortcut("Ctrl+S")
        save.setStatusTip("Save the file")

        save_as = self.ui.actionSave_as
        save_as.triggered.connect(self.saveAsFunc)
        save_as.setShortcut("Ctrl+Shift+S")
        save_as.setStatusTip("Choose how save the file")

        quit = self.ui.actionQuit
        quit.triggered.connect(QtWidgets.qApp.quit)
        quit.setShortcut("Ctrl+Q")
        quit.setStatusTip("Exit application")

# ----Edit-------------------------------------------------
        undo = self.ui.actionUndo
        undo.triggered.connect(self.undoFunc)
        undo.setShortcut("Ctrl+Z")

        redo = self.ui.actionRedo
        redo.triggered.connect(self.redoFunc)
        redo.setShortcut("Ctrl+Shift+Z")

        cut = self.ui.actionCut
        cut.triggered.connect(self.cutFunc)
        cut.setShortcut("Ctrl+X")

        copy = self.ui.actionCopy
        copy.triggered.connect(self.copyFunc)
        copy.setShortcut("Ctrl+C")

        paste = self.ui.actionPaste
        paste.triggered.connect(self.pasteFunc)
        paste.setShortcut("Ctrl+V")
# ----View-------------------------------------------------        
        mini = self.ui.actionMinimize
        mini.triggered.connect(self.minFunc)
        mini.setShortcut("Ctrl+M")
        mini.setStatusTip("Minimize window")

        norm = self.ui.actionNormal_Window
        norm.triggered.connect(self.normFunc)
        norm.setShortcut("Ctrl+Shift+N")
        norm.setStatusTip("Set window normal size")

        full = self.ui.actionFullscreen
        full.triggered.connect(self.fullFunc)
        full.setShortcut("Ctrl+Shift+F")
        full.setStatusTip("Set window fullscreen")

        font = self.ui.actionSelect_Font
        font.triggered.connect(self.selectFontFunc)
        font.setShortcut("Ctrl+Alt+F")

        under = self.ui.actionUnderline_Ctrl_U
        under.triggered.connect(self.underFunc)
        under.setShortcut("Ctrl+U")

        bold = self.ui.actionBond_Ctrl_B
        bold.triggered.connect(self.boldFunc)
        bold.setShortcut("Ctrl+B")

        strike = self.ui.actionStrice
        strike.triggered.connect(self.strikeFunc)
        strike.setShortcut("Ctrl+Alt+S")

        italic = self.ui.actionItalic_Ctrl_I
        italic.triggered.connect(self.italicFunc)
        italic.setShortcut("Ctrl+I")
# ----Help-------------------------------------------------        
        about = self.ui.actionAbout
        about.triggered.connect(self.aboutFunc)
        about.setShortcut("F1")

# =========================================================

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()
# =========================================================
    def divFunc(self):
        global i
        global value

        i = i + 1
        if(i>1): 
            value = False
            i = 0
        else: value = True
        return value
# =========================================================

    # File
    def newFunc(self):
        text = self.ui.textEdit.toPlainText()
        if(len(text) != 0):
            self.qFunc()
 

    def openFunc(self):
        global fname
        fname, ok = QFileDialog.getOpenFileName(self, 'Open file', '/home')
        if (ok):
            with open(fname, 'r') as f:
                data = f.read()
                self.ui.textEdit.setText(data)


    def saveFunc(self):
        text = self.ui.textEdit.toPlainText()
        if(len(text) != 0):
            global fname
            if(len(fname) != 0):
                with open(fname, 'w') as f:
                    f.write(text)

    def saveAsFunc(self):
        fname, ok = QFileDialog.getSaveFileName(self, 'Save the file', '/home')
        if (ok):
            with open(fname, 'r') as f:
                data = f.read()
                self.ui.textEdit.setText(data)
        
# ----Edit-------------------------------------------------
    def undoFunc(self):
        self.ui.textEdit.undo()

    def redoFunc(self):
        self.ui.textEdit.redo()

    def cutFunc(self):
        self.ui.textEdit.cut()

    def copyFunc(self):
        self.ui.textEdit.copy()

    def pasteFunc(self):
        self.ui.textEdit.paste()

# ----View-------------------------------------------------
    def minFunc(self):
        self.showMinimized()

    def normFunc(self):
        global W, H
        self.ui.textEdit.setGeometry(QtCore.QRect(0, 0, W, H))
        self.showNormal()

    def fullFunc(self):
        self.showMaximized()
        self.ui.textEdit.setGeometry(QtCore.QRect(0, 0, 1366, 768))

    def selectFontFunc(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.ui.textEdit.setFont(font)

    def underFunc(self):
        self.ui.textEdit.setFontUnderline(self.divFunc())

    def boldFunc(self):
        if(self.divFunc()):
            self.ui.textEdit.setFontWeight(QFont.Bold)
        else:
            self.ui.textEdit.setFontWeight(QFont.Normal)
            
    def strikeFunc(self):

        fmt = self.ui.textEdit.currentCharFormat()
        fmt.setFontStrikeOut(not fmt.fontStrikeOut())
        self.ui.textEdit.setCurrentCharFormat(fmt)


    def italicFunc(self):
        self.ui.textEdit.setFontItalic(self.divFunc())

# ----Help-------------------------------------------------        
    def aboutFunc(self):
        print("hi!")
    

    def qFunc(self):
        
        result = QtWidgets.QMessageBox.question(self, "Confirm Dialog", "Save the changes?", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No| QtWidgets.QMessageBox.Cancel, QtWidgets.QMessageBox.Cancel)
        if (result == QtWidgets.QMessageBox.Yes):
            global fname
            if(len(fname) != 0): 
                self.saveFunc()
                self.ui.textEdit.setText('')

            else: 
                self.saveAsFunc()
                self.ui.textEdit.setText('')

        if (result == QtWidgets.QMessageBox.No):
            self.ui.textEdit.setText('')
        if (result == QtWidgets.QMessageBox.Cancel):
            pass


# =========================================================

app = QtWidgets.QApplication([])
application = mywindow()
application.show()
 
sys.exit(app.exec())
