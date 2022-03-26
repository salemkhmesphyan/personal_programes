# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sniak.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import threading
global a,x1,g,y,u,l,d,s_t,x_e,y_e
a=0
x_e=200
y_e=100
s_t=19
x1=100
g=0
y=450
u=0
l=0
d=0


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(761, 622)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.framework = QtWidgets.QFrame(self.centralwidget)
        self.framework.setStyleSheet("background-color: qlineargradient(spread:reflect, x1:0.941, y1:0.165, x2:0.945, y2:0.17, stop:1 rgba(244, 141, 102, 255));")
        self.framework.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.framework.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.framework.setObjectName("framework")
        self.eat = QtWidgets.QLabel(self.framework)
        self.eat.setGeometry(QtCore.QRect(281, 120, 20, 21))
        self.eat.setStyleSheet("background-color: rgb(21, 7, 6);")
        self.eat.setText("")
        self.eat.setObjectName("eat")
        self.snik = QtWidgets.QSlider(self.framework)
        self.snik.setGeometry(QtCore.QRect(100, 450, 19, 20))
        self.snik.setMinimum(3)
        self.snik.setMaximum(4)
        self.snik.setPageStep(14)
        self.snik.setTracking(True)
        self.snik.setOrientation(QtCore.Qt.Horizontal)
        self.snik.setInvertedAppearance(True)
        self.snik.setInvertedControls(False)
        self.snik.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.snik.setObjectName("snik")
        self.gridLayout.addWidget(self.framework, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 761, 27))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.dockWidget = QtWidgets.QDockWidget(MainWindow)
        self.dockWidget.setObjectName("dockWidget")
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.dockWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.splitter = QtWidgets.QSplitter(self.dockWidgetContents)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.pushButton = QtWidgets.QPushButton(self.splitter)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.splitter)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.splitter)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.splitter)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.splitter)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.splitter)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout_2.addWidget(self.splitter, 0, 0, 1, 1)
        self.dockWidget.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", ">>"))
        self.pushButton_2.setText(_translate("MainWindow", "<<"))
        self.pushButton_3.setText(_translate("MainWindow", "^"))
        self.pushButton_4.setText(_translate("MainWindow", "U"))
        self.pushButton_5.setText(_translate("MainWindow", "start"))
        self.pushButton_6.setText(_translate("MainWindow", "stop"))
class NotePad(QtWidgets.QMainWindow):
	def __init__(self, parent=None):
		QtWidgets.QWidget.__init__(self, parent)#lambda:تضعها عند اسم الزر
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		#self.ui.pushButton.clicked.connect(self.go)
		self.ui.pushButton_5.clicked.connect(self.start)
		#self.ui.pushButton_3.clicked.connect(self.up)
		#self.ui.pushButton_2.clicked.connect(self.left)
		#self.ui.pushButton_4.clicked.connect(self.down)
		self.ui.pushButton_5.keyPressEvent=self.keyPressEvent
		self.ff()
	def ff(self):
		global a,g,x1,u,d,l,y,s_t,x_e,y_e
		threading.Timer(0.1, self.ff).start()
		if a==1:
			if g==1:
				x1+=5
				self.ui.snik.setGeometry(QtCore.QRect(x1, y, s_t, 20))
				self.bigsize()
			if u==1:
				y-=5
				self.ui.snik.setGeometry(QtCore.QRect(x1, y, s_t, 20))
				self.bigsize()
			if d==1:
				y+=5
				self.ui.snik.setGeometry(QtCore.QRect(x1, y, s_t, 20))
				self.bigsize()
			if l==1:
				x1-=5
				self.ui.snik.setGeometry(QtCore.QRect(x1, y, s_t, 20))
				self.bigsize()
				
	def keyPressEvent(self, event):
		
		if event.key() == QtCore.Qt.Key_Left:
			self.left()
		if event.key() == QtCore.Qt.Key_Up:
			self.up()
		if event.key() == QtCore.Qt.Key_Down:
			self.down()
		if event.key() == QtCore.Qt.Key_Right:
			self.go()
		
	def start(self):
		global a
		a=1
	def go(self):
		global g,u,l,d
		g=1
		u=0
		l=0
		d=0
	def up(self):
		global g,u,l,d
		g=0
		u=1
		l=0
		d=0
	def down(self):
		global g,u,l,d
		g=0
		u=0
		l=0
		d=1
	def left(self):
		global g,u,l,d
		g=0
		u=0
		l=1
		d=0
	def bigsize(self):
		global s_t,x_e,y_e,x1,y
		if (x1==x_e-1 and y==y_e) or (x1==x_e and y==y_e-1) or (x1==x_e and y==y_e+2)or(x1==x_e-2 and y==y_e+3):
			s_t+=10
			
			self.ui.snik.setGeometry(QtCore.QRect(x1, y, s_t, 20))
			
				

if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	myapp = NotePad()
	
myapp.show()
sys.exit(app.exec_())

