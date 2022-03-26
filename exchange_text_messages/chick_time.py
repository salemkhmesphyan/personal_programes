# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chick_time.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import threading
global r
from PyQt5.QtCore import QDir, Qt, QUrl
r=1
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 591)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(300, 340, 85, 27))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(70, 340, 85, 27))
        self.pushButton_3.setObjectName("pushButton_3")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(160, 190, 113, 27))
        self.lineEdit.setObjectName("lineEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 480, 27))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "if 1"))
        self.pushButton_3.setText(_translate("MainWindow", "start"))
class NotePad(QtWidgets.QMainWindow):#from her start game
	def __init__(self, parent=None):
		QtWidgets.QWidget.__init__(self, parent)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.ui.pushButton.clicked.connect(self.trans)
		self.ui.pushButton_3.clicked.connect(self.go)
		#self.tim()
	def tim(self):
		global r
		if r==1:
			self.ui.lineEdit.clear()
			self.ui.lineEdit.setText("ok")
			threading.Timer(1, self.tim).start()
		else:
			self.ui.lineEdit.clear()
	def trans(self):
		d=['','2','32','454','54']
		ok = QtWidgets.QInputDialog.getItem(self,"hello","list",d,0,False)
		if ok[0]=='':
			print("no select")
		else:print("select")
	def go(self):
		fileName= QtWidgets.QFileDialog.getOpenFileName(self)
		self.ui.lineEdit.clear()
		#self.ui.lineEdit.setText(QUrl.fromLocalFile(fileName))
		#r=fileName.find(",")
		self.ui.lineEdit.setText(fileName[0])
		#print(fileName)
if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	myapp = NotePad()
	
myapp.show()
sys.exit(app.exec_())

