# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'jump.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QRect
import threading
global e,u,p,d,i,g,ttt
e=0
p=390
u=0
d=200
i=0
g=200
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(639, 548)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 390, 50, 50))
        self.label.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.0181818, y2:0.0227273, stop:0 rgba(244, 117, 117, 255), stop:1 rgba(78, 255, 255, 255));")
        self.label.setPixmap(QtGui.QPixmap(":/same/back.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(540, 390, 50, 50))
        self.label_2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(244, 117, 117, 255), stop:1 rgba(255, 255, 255, 255));")
        self.label_2.setPixmap(QtGui.QPixmap(":/same/down.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_2.setWordWrap(False)
        self.label_2.setIndent(-1)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(390, 30, 85, 27))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(160, 30, 85, 27))
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 639, 27))
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
        self.label.setText(_translate("MainWindow", ".."))
        self.label_2.setText(_translate("MainWindow", "."))
        self.pushButton.setText(_translate("MainWindow", "ابدء"))
        self.pushButton_2.setText(_translate("MainWindow", "قفز"))
class NotePad(QtWidgets.QMainWindow):
	def __init__(self, parent=None):
		QtWidgets.QWidget.__init__(self, parent)#lambda:تضعها عند اسم الزر
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.ff()
		self.ui.pushButton.clicked.connect(self.ii)
		#self.ui.pushButton_2.clicked.connect(self.g1)
		self.ui.pushButton.keyPressEvent=self.keyPressEvent
		#print(self.ui.label_2.geometry(QtCore.QRect.getRect()))
	def ff(self):
		global e,u,p,i,d,g,ttt
		threading.Timer(0.1, self.ff).start()
		if e==g or e==p or e==450:
			e=0
			self.dd()
		else:
				
			self.dd()
		if i==1:
			
			if p<200:
				
				if d==200:
					
					self.ui.label_2.setGeometry(QtCore.QRect(500, g, 50, 50))
					g+=10
				if g>=390:
					u=0
					#i=0
					d=0
					g=200
					
					
					
			else:
				self.ui.label_2.setGeometry(QtCore.QRect(500, p, 50, 50))
				p-=10
			
			#if p>=390:
			#	i=0
		
	def dd(self):
		global e,p,u,i,d
		
		e+=10
		ddd=e
		x1=ddd
		#x2=
		self.ui.label.setGeometry(QtCore.QRect(x1, 390, 50, 50))
		#if u==1:
		#	i=1
			
			#if p>100:
			#	i=1
			#	u=0
			
		
			
		
	def ii(self):
		global u
	def ss(self):
		global u,p,i,d
		#u=1
		i=1
		d=200
		p=390
		#self.ui.label_2.setGeometry(QtCore.QRect(500, 390, 111, 81))
	def keyPressEvent(self, event):
		global u,p,i,d
		if event.key() == QtCore.Qt.Key_Up:
			self.ss()
			#i=1
			#d=200
			#p=390
	def g1(self):
		global u,p,i,d,ttt
		#ttt.join()			

if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	myapp = NotePad()
	
myapp.show()
sys.exit(app.exec_())
