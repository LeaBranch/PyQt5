from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QWidget, QApplication, QDesktopWidget, QAbstractItemView
# from PyQt5.QtGui import QAbstractItemView
from PyQt5.QtCore import Qt

from gui import Ui_MainWindow  # импорт нашего сгенерированного файла
import sys, os, time

#divFunc
i = 0
value = True

#Resolution
W, H = 800, 600
twW, twH = W, 519

#Navigation
path = '.'
D_path = ''

#table
num_of_col = 0
lineCount = 0
list_ = []

#Others
fname = ""
q = 0
fp_value = False

class mywindow(QtWidgets.QMainWindow):

    def divFunc(self):
        global i
        global value

        i = i + 1
        if(i>1): 
            value = False
            i = 0
        else: value = True
        return value

    def Head(self, flag):
        path = os.getcwd()
        if flag == True:
            self.ui.lineEdit.setText(path)
        if flag == False:
            if(path == '/'): 
                self.ui.lineEdit.setText('/')
            else: 
                tmp = os.path.split(path)
                self.ui.lineEdit.setText(tmp[1])

    def tableLoad(self):
        global list_
        global fp_value

        fp_value = self.ui.full_path.isChecked()
        self.Head(fp_value)

        list_ = os.listdir()
        lineCount = len(list_)
        self.ui.tableWidget.setRowCount(lineCount)
        for i in range(lineCount):
            # Name
            self.ui.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(list_[i]))
            # Size
            _size = os.path.getsize(list_[i])
            self.ui.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(str(_size)))
            # Type
            if (os.path.isdir(list_[i]) is True):
                self.ui.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem("folder"))
            # если это файл
            else:
                self.ui.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem("file"))
            # если это исполняемый файл(приложение)
            # if (os.access(list_[i], os.X_OK)):
                # self.ui.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem("exec file"))
            # Modified time
            _time = os.path.getctime(list_[i])
            self.ui.tableWidget.setItem(i, 3, QtWidgets.QTableWidgetItem(time.ctime(_time)))
        # отмена изменений в ячейке
        self.ui.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)


    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

# =========================================================
        num_of_col = self.ui.tableWidget.columnCount()
        header = self.ui.tableWidget.horizontalHeader()  
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch) 
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents) 
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents) 
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents) 
        
        self.ui.groupBox.setVisible(False)
        fp_value = self.ui.full_path.isChecked()

        os.chdir(path)
        self.Head(fp_value)
        self.tableLoad()

# ========================Call=============================
# ----Buttons----------------------------------------------
        _back = self.ui.pushButton_1
        _back.clicked.connect(self._backFunc)
        _back.setShortcut("Alt+Left")
        _back.setStatusTip("Go back")

        _forward = self.ui.pushButton_2
        _forward.clicked.connect(self._forwardFunc)
        _forward.setShortcut("Alt+Right")
        _forward.setStatusTip("Go forward")
        _forward.setEnabled(False)

        find = self.ui.pushButton_Find
        find.clicked.connect(self.findFunc)
        find.setShortcut("Ctrl+F")

        settings = self.ui.pushButton_Settings
        settings.clicked.connect(self.settingsFunc)
        settings.setShortcut("F10")

        self.ui.full_path.clicked.connect(self.fpFunc)
        self.ui.show_hidden.clicked.connect(self.shFunc)
        self.ui.show_sidebar.clicked.connect(self.ssFunc)
        self.ui.select_all.clicked.connect(self.saFunc)
# ----File-------------------------------------------------    
        new_fol = self.ui.actionCreate_folder
        new_fol.triggered.connect(self.newFolderFunc)
        new_fol.setShortcut("Ctrl+N")
        new_fol.setStatusTip("Create new folder")        

        new_file = self.ui.actionCreate_file
        new_file.triggered.connect(self.newFileFunc)
        new_file.setShortcut("Ctrl+Shift+N")
        new_file.setStatusTip("Create new file")

        quit = self.ui.actionQuit
        quit.triggered.connect(QtWidgets.qApp.quit)
        quit.setShortcut("Ctrl+Q")
        quit.setStatusTip("Exit application")
# ----Edit-------------------------------------------------

        cut = self.ui.actionCut
        cut.triggered.connect(self.cutFunc)
        cut.setShortcut("Ctrl+X")

        copy = self.ui.actionCopy
        copy.triggered.connect(self.copyFunc)
        copy.setShortcut("Ctrl+C")

        paste = self.ui.actionPaste
        paste.triggered.connect(self.pasteFunc)
        paste.setShortcut("Ctrl+V")

        move = self.ui.actionMove
        move.triggered.connect(self.moveFunc)
        move.setShortcut("Ctrl+M")

        rename = self.ui.actionRename
        rename.triggered.connect(self.renameFunc)
        rename.setShortcut("F2")

        _del = self.ui.actionDelete
        _del.triggered.connect(self.moveFunc)
        _del.setShortcut("Delete")
# ----View-------------------------------------------------        
        mini = self.ui.actionMinimize
        mini.triggered.connect(self.minFunc)
        mini.setShortcut("Ctrl+Alt+M")
        mini.setStatusTip("Minimize window")

        norm = self.ui.actionNormal
        norm.triggered.connect(self.normFunc)
        norm.setShortcut("Ctrl+Alt+N")
        norm.setStatusTip("Set window normal size")

        full = self.ui.actionFullscreen
        full.triggered.connect(self.fullFunc)
        full.setShortcut("Ctrl+Alt+F")
        full.setStatusTip("Set window fullscreen")
# ----Help-------------------------------------------------        
        about = self.ui.actionAbout
        about.triggered.connect(self.aboutFunc)
        about.setShortcut("F1")
# ----Table------------------------------------------------
        self.ui.tableWidget.cellDoubleClicked.connect(self.cellClickFunc)
# ===================Initialization========================
# ----Buttons----------------------------------------------
    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()
    

    def fpFunc(self):
        fp_value = self.ui.full_path.isChecked()
        self.Head(fp_value)
        print(fp_value)

    def shFunc(self):
        pass

    def ssFunc(self):
        pass

    def saFunc(self):
        pass

    def _backFunc(self):
        global D_path
        global fp_value
        path = os.getcwd()
        tmp = os.path.split(path)
        D_path = tmp[1]
        os.chdir("..")        
        self.tableLoad()
        self.ui.pushButton_2.setEnabled(True)

    def _forwardFunc(self):
        global D_path
        os.chdir(D_path)
        self.tableLoad()
        self.ui.pushButton_2.setEnabled(False)
        
        D_path = ''

    def findFunc(self):
        print ("find!")

    def settingsFunc(self):
        self.ui.groupBox.setVisible(self.divFunc())
# ----File-------------------------------------------------
    def newFolderFunc(self):
        _newPath = os.getcwd() + "/New_folder"
        folder = os.mkdir(_newPath)
        self.tableLoad()
        

    def newFileFunc(self):
        pass       
# ----Edit-------------------------------------------------
    def cutFunc(self):
        self.ui.textEdit.cut()

    def copyFunc(self):
        self.ui.textEdit.copy()

    def pasteFunc(self):
        self.ui.textEdit.paste()
    
    def moveFunc(self):
        pass

    def renameFunc(self):
        pass

    def _delFunc(self):
        pass
# ----View-------------------------------------------------
    def minFunc(self):
        self.showMinimized()

    def normFunc(self):
        self.showNormal()
        self.ui.tableWidget.setGeometry(QtCore.QRect(0, 40, twW, twH))
        self.ui.lineEdit.setGeometry(QtCore.QRect(80, 0, 600, 41))    
        self.ui.pushButton_Settings.move(740, 0)
        self.ui.pushButton_Find.move(680, 0)
        self.ui.groupBox.move(640,0)

    def fullFunc(self):
        self.showMaximized()
        self.ui.tableWidget.setGeometry(QtCore.QRect(0, 0, q.width(), q.height()-41))
        self.ui.lineEdit.setGeometry(QtCore.QRect(80, 0, q.width()-200, 41))        
        self.ui.tableWidget.move(0,41)
        self.ui.pushButton_Settings.move(q.width()-60, 0)
        self.ui.pushButton_Find.move(q.width()-120, 0)
        self.ui.groupBox.move(q.width()-160, +40)
# ----Help-------------------------------------------------        
    def aboutFunc(self):
        print("hi!")# ----Table------------------------------------------------

# ----Table------------------------------------------------
    def cellClickFunc(self):
        currCol = self.ui.tableWidget.currentColumn()
        if(currCol == 0):
            curRow = self.ui.tableWidget.currentRow()
            # print(curRow)

                # если выбранный эл-т явл. папкой
            if (os.path.isdir(list_[curRow]) is True):
                print("isFolder")
                os.chdir(list_[curRow])
                self.Head(fp_value)
                self.tableLoad()

            # если это файл
            if (os.path.isfile(list_[curRow])):
                # subprocess.call(["NotePad.py", "list_[choice-1]", "-r"], shell=True)
                # os.execl("NotePad.py",  "list_[curRow-1]", "-r")
                print('isFile!')

            # если это исполняемый файл(приложение)
            if (os.access(list_[curRow], os.X_OK)):
                print('isExecFile!')



app = QtWidgets.QApplication([])
q= QDesktopWidget().availableGeometry()
application = mywindow()
application.show()

sys.exit(app.exec())
