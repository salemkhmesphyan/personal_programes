## -*- coding: utf-8 -*-

## Form implementation generated from reading ui file 'jump.ui'
##
## Created by: PyQt5 UI code generator 5.5.1
##
## WARNING! All changes made in this file will be lost!

#from PyQt5 import QtCore, QtGui, QtWidgets

#class Ui_MainWindow(object):
    #def setupUi(self, MainWindow):
        #MainWindow.setObjectName("MainWindow")
        #MainWindow.resize(639, 548)
        #self.centralwidget = QtWidgets.QWidget(MainWindow)
        #self.centralwidget.setObjectName("centralwidget")
        #self.label = QtWidgets.QLabel(self.centralwidget)
        #self.label.setGeometry(QtCore.QRect(550, 400, 91, 101))
        #self.label.setText("")
        #self.label.setPixmap(QtGui.QPixmap(":/same/back.png"))
        #self.label.setScaledContents(True)
        #self.label.setObjectName("label")
        #self.label_2 = QtWidgets.QLabel(self.centralwidget)
        #self.label_2.setGeometry(QtCore.QRect(0, 410, 111, 81))
        #self.label_2.setText("")
        #self.label_2.setPixmap(QtGui.QPixmap(":/same/down.png"))
        #self.label_2.setScaledContents(True)
        #self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        #self.label_2.setWordWrap(False)
        #self.label_2.setIndent(-1)
        #self.label_2.setObjectName("label_2")
        #self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        #self.pushButton.setGeometry(QtCore.QRect(390, 30, 85, 27))
        #self.pushButton.setObjectName("pushButton")
        #self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        #self.pushButton_2.setGeometry(QtCore.QRect(160, 30, 85, 27))
        #self.pushButton_2.setObjectName("pushButton_2")
        #MainWindow.setCentralWidget(self.centralwidget)
        #self.menubar = QtWidgets.QMenuBar(MainWindow)
        #self.menubar.setGeometry(QtCore.QRect(0, 0, 639, 27))
        #self.menubar.setObjectName("menubar")
        #MainWindow.setMenuBar(self.menubar)
        #self.statusbar = QtWidgets.QStatusBar(MainWindow)
        #self.statusbar.setObjectName("statusbar")
        #MainWindow.setStatusBar(self.statusbar)

        #self.retranslateUi(MainWindow)
        #QtCore.QMetaObject.connectSlotsByName(MainWindow)

    #def retranslateUi(self, MainWindow):
        #_translate = QtCore.QCoreApplication.translate
        #MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        #self.pushButton.setText(_translate("MainWindow", "ابدء"))
        #self.pushButton_2.setText(_translate("MainWindow", "قفز"))

#import ff_rc

#if __name__ == "__main__":
    #import sys
    #app = QtWidgets.QApplication(sys.argv)
    #MainWindow = QtWidgets.QMainWindow()
    #ui = Ui_MainWindow()
    #ui.setupUi(MainWindow)
    #MainWindow.show()
    #sys.exit(app.exec_())
import sys

from PyQt5.QtCore import *
from PyQt5.QtGui  import *
from PyQt5.QtWidgets import *
 
class MainGui(object):
    def setupUi(self, MainWindow):
        MainWindow.resize(218, 379)
        self.centralwidget = QWidget(MainWindow)
        self.layout = QVBoxLayout(self.centralwidget)
        self.p_text = QPlainTextEdit(self.centralwidget)
        self.layout.addWidget(self.p_text)
        MainWindow.setCentralWidget(self.centralwidget)

        self.centralwidget.keyPressEvent = self.keyPressEvent

    def keyPressEvent(self, e):
        print("event", e)
        if e.key()  == Qt.Key_Return :
            print(' return')
        elif e.key() == Qt.Key_Enter :   
            print(' enter')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = MainGui()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
