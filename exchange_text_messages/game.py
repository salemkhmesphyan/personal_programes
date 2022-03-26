# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'game.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

import random
global sho,a1,a2,a3,aa1,aa2,aa3,aaa1,aaa2,aaa3,ww,dd,ww1,dd1,ww2,dd2,ck,en,sho1,sho2
sho1=[]
sho2=[]
sho=['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21']
ck=0
a1=[]#set 1 in operation 1
a2=[]#set 2 in operation 1
a3=[]#set 3 in operation 1
aa1=[]#set 1 in operation 2
aa2=[]#set 2 in operation 2
aa3=[]#set 3 in operation 2
aaa1=[]#set 1 in operation 3
aaa2=[]#set 2 in operation 3
aaa3=[]#set 3 in operation 3
ok=['1','2']
ww=1
dd=25
ww1=1
dd1=25
ww2=1
dd2=25
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(625, 565)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.splitter_3 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_3.setOrientation(QtCore.Qt.Vertical)
        self.splitter_3.setObjectName("splitter_3")
        self.splitter = QtWidgets.QSplitter(self.splitter_3)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.lista = QtWidgets.QListWidget(self.splitter)
        self.lista.setObjectName("lista")
        self.listb = QtWidgets.QListWidget(self.splitter)
        self.listb.setObjectName("listb")
        self.listc = QtWidgets.QListWidget(self.splitter)
        self.listc.setObjectName("listc")
        self.splitter_2 = QtWidgets.QSplitter(self.splitter_3)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.chec_a = QtWidgets.QCheckBox(self.splitter_2)
        self.chec_a.setObjectName("chec_a")
        self.check_b = QtWidgets.QCheckBox(self.splitter_2)
        self.check_b.setObjectName("check_b")
        self.check_c = QtWidgets.QCheckBox(self.splitter_2)
        self.check_c.setObjectName("check_c")
        self.widget = QtWidgets.QWidget(self.splitter_3)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.but_star = QtWidgets.QPushButton(self.widget)
        self.but_star.setObjectName("but_star")
        self.horizontalLayout.addWidget(self.but_star)
        self.but_try = QtWidgets.QPushButton(self.widget)
        self.but_try.setObjectName("but_try")
        self.horizontalLayout.addWidget(self.but_try)
        self.but_close = QtWidgets.QPushButton(self.widget)
        self.but_close.setObjectName("but_close")
        self.horizontalLayout.addWidget(self.but_close)
        self.gridLayout.addWidget(self.splitter_3, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 625, 27))
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
        self.chec_a.setText(_translate("MainWindow", "A"))
        self.check_b.setText(_translate("MainWindow", "B"))
        self.check_c.setText(_translate("MainWindow", "C"))
        self.but_star.setText(_translate("MainWindow", "START"))
        self.but_try.setText(_translate("MainWindow", "TRY"))
        self.but_close.setText(_translate("MainWindow", "CLOSE"))
class NotePad(QtWidgets.QMainWindow):
	def __init__(self, parent=None):
		QtWidgets.QWidget.__init__(self, parent)#lambda:تضعها عند اسم الزر
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.ui.chec_a.stateChanged.connect(self.groupa)
		self.ui.check_b.stateChanged.connect(self.groupb)
		self.ui.check_c.stateChanged.connect(self.groupc)
		global sho,a1,a2,a3,aa1,aa2,aa3,aaa1,aaa2,aaa3,ww,dd,ww1,dd1,ww2,dd2
		#sho=['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21']
		while dd>ww:#loop order random
		
			rr=random.choice(sho)
			if ww<8:
				a1.append(rr)
				d=sho.index(rr)
				del sho[d]
				#print(d)

				#print("a1",a1)
			if (ww>9) and (ww<17):
				a2.append(rr)
				d=sho.index(rr)
				del sho[d]
				#print(d)
				#print("a2",a2)
			if ww>17:
				a3.append(rr)
				d=sho.index(rr)
				del sho[d]
				#print (d)
				#print("a3",a3)
			ww+=1
		for n in a1:
			self.ui.lista.insertItem(0,'{}'.format(n))
		for n in a2:
			self.ui.listb.insertItem(0,'{}'.format(n))
		for n in a3:
			self.ui.listc.insertItem(0,'{}'.format(n))
	def ckgroup(self):
		global ck,en
		if ck==1:
			self.opertion1()
		if ck==2:
			self.opertion2()
		if ck==3:
			self.opertion3()
			
			print(sho2)			
	def groupa(self):
		global ck,en
		ck+=1
		en=1
		self.ui.chec_a.setChecked(False)
		self.ui.check_b.setChecked(False)
		self.ui.check_c.setChecked(False)
		self.ckgroup()
	def groupb(self):
		global ck,en
		ck+=1
		en=2
		self.ui.chec_a.setChecked(False)
		self.ui.check_b.setChecked(False)
		self.ui.check_c.setChecked(False)
		self.ckgroup()
	def groupc(self):
		global ck,en
		ck+=1
		en=3
		self.ui.chec_a.setChecked(False)
		self.ui.check_b.setChecked(False)
		self.ui.check_c.setChecked(False)
		self.ckgroup()
	def opertion1(self):
		if en==1:
			self.set1()
		if en==2:
			self.set2()
		if en==3:
			self.set3()
		self.sort2()
	def set1(self):
		global sho
		for y in a2:
			sho.append(y)
		for y in a1:
			sho.append(y)
		for y in a3:
			sho.append(y)
			#print(sho)
	def set2(self):
		global sho
		for y in a1:
			sho.append(y)
		for y in a2:
			sho.append(y)
		for y in a3:
			sho.append(y)
			#print(sho)
	def set3(self):
		global sho
		for y in a1:
			sho.append(y)
		for y in a3:
			sho.append(y)
		for y in a2:
			sho.append(y)
		#print(sho)
	def sort2(self):
		global sho
		for n in sho:
			f=sho.index(n)
			if f==0:
				aa1.append(n)
			if f==3:
				aa1.append(n)
			if f==6:
				aa1.append(n)
			if f==9:
				aa1.append(n)
			if f==12:
				aa1.append(n)
			if f==15:
				aa1.append(n)
			if f==18:
				aa1.append(n)
			if f==1:
				aa2.append(n)
			if f==4:
				aa2.append(n)
			if f==7:
				aa2.append(n)
			if f==10:
				aa2.append(n)
			if f==13:
				aa2.append(n)
			if f==16:
				aa2.append(n)
			if f==19:
				aa2.append(n)
			if f==2:
				aa3.append(n)
			if f==5:
				aa3.append(n)
			if f==8:
				aa3.append(n)
			if f==11:
				aa3.append(n)
			if f==14:
				aa3.append(n)
			if f==17:
				aa3.append(n)
			if f==20:
				aa3.append(n)
		self.ui.lista.clear()
		self.ui.listb.clear()
		self.ui.listc.clear()
		for n in aa1:
			self.ui.lista.insertItem(0,'{}'.format(n))
		for n in aa2:
			self.ui.listb.insertItem(0,'{}'.format(n))
		for n in aa3:
			self.ui.listc.insertItem(0,'{}'.format(n))
###################################################1 finshed##################################\\
	def opertion2(self):
		global en
		if en==1:
			self.set11()
		if en==2:
			self.set22()
		if en==3:
			self.set33()
		self.sort3()
	def set11(self):
		global sho1
		for y in aa2:
			sho1.append(y)
		for y in aa1:
			sho1.append(y)
		for y in aa3:
			sho1.append(y)
			#print(sho)
	def set22(self):
		global sho1
		for y in aa1:
			sho1.append(y)
		for y in aa2:
			sho1.append(y)
		for y in aa3:
			sho1.append(y)
			#print(sho)
	def set33(self):
		global sho1
		for y in aa1:
			sho1.append(y)
		for y in aa3:
			sho1.append(y)
		for y in aa2:
			sho1.append(y)
		#print(sho)
	def sort3(self):
		global sho1
		for n in sho1:
			f=sho1.index(n)
			if f==0:
				aaa1.append(n)
			if f==3:
				aaa1.append(n)
			if f==6:
				aaa1.append(n)
			if f==9:
				aaa1.append(n)
			if f==12:
				aaa1.append(n)
			if f==15:
				aaa1.append(n)
			if f==18:
				aaa1.append(n)
			if f==1:
				aa2.append(n)
			if f==4:
				aaa2.append(n)
			if f==7:
				aaa2.append(n)
			if f==10:
				aaa2.append(n)
			if f==13:
				aaa2.append(n)
			if f==16:
				aaa2.append(n)
			if f==19:
				aaa2.append(n)
			if f==2:
				aaa3.append(n)
			if f==5:
				aaa3.append(n)
			if f==8:
				aaa3.append(n)
			if f==11:
				aaa3.append(n)
			if f==14:
				aaa3.append(n)
			if f==17:
				aaa3.append(n)
			if f==20:
				aaa3.append(n)
		self.ui.lista.clear()
		self.ui.listb.clear()
		self.ui.listc.clear()
		for n in aaa1:
			self.ui.lista.insertItem(0,'{}'.format(n))
		for n in aaa2:
			self.ui.listb.insertItem(0,'{}'.format(n))
		for n in aaa3:
			self.ui.listc.insertItem(0,'{}'.format(n))
	def opertion3(self):
		global en
		if en==1:
			self.set111()
		if en==2:
			self.set222()
		if en==3:
			self.set333()
	def set111(self):
		global sho2
		for y in aaa2:
			sho2.append(y)
		for y in aaa1:
			sho2.append(y)
		for y in aaa3:
			sho2.append(y)
			#print(sho)
	def set222(self):
		global sho2
		for y in aaa1:
			sho2.append(y)
		for y in aaa2:
			sho2.append(y)
		for y in aaa3:
			sho2.append(y)
			#print(sho)
	def set333(self):
		global sho2
		for y in aaa1:
			sho2.append(y)
		for y in aaa3:
			sho2.append(y)
		for y in aaa2:
			sho2.append(y)
				
		
if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	myapp = NotePad()
	
myapp.show()
sys.exit(app.exec_())

