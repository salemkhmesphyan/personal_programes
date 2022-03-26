# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mangesystem.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets, QtPrintSupport
import sqlite3
from datetime import date
import time
import datetime
global dgn
import sys
dgn=0
########################################sanfclass#############################################################
class Ui_MainWindow1(object):
    def setupUi(self, MainWindow1):
        MainWindow1.setObjectName("MainWindow1")
        MainWindow1.resize(612, 582)
        MainWindow1.setStyleSheet("\n"
"background-color: qlineargradient(spread:pad, x1:0.986, y1:0.006, x2:1, y2:0, stop:0 rgba(244, 179, 173, 255), stop:1 rgba(255, 255, 255, 255));")
        self.centralwidget = QtWidgets.QWidget(MainWindow1)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.splitter_5 = QtWidgets.QSplitter(self.groupBox)
        self.splitter_5.setOrientation(QtCore.Qt.Vertical)
        self.splitter_5.setObjectName("splitter_5")
        self.splitter_2 = QtWidgets.QSplitter(self.splitter_5)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.splitter = QtWidgets.QSplitter(self.splitter_2)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.widget = QtWidgets.QWidget(self.splitter)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pgemodsnfententerbarcod = QtWidgets.QLineEdit(self.widget)
        self.pgemodsnfententerbarcod.setObjectName("pgemodsnfententerbarcod")
        self.horizontalLayout.addWidget(self.pgemodsnfententerbarcod)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.widget1 = QtWidgets.QWidget(self.splitter)
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pgemodsnfcomentername = QtWidgets.QComboBox(self.widget1)
        self.pgemodsnfcomentername.setEditable(True)
        self.pgemodsnfcomentername.setObjectName("pgemodsnfcomentername")
        self.horizontalLayout_2.addWidget(self.pgemodsnfcomentername)
        self.label_3 = QtWidgets.QLabel(self.widget1)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.label_2 = QtWidgets.QLabel(self.splitter_2)
        self.label_2.setObjectName("label_2")
        self.splitter_4 = QtWidgets.QSplitter(self.splitter_5)
        self.splitter_4.setOrientation(QtCore.Qt.Vertical)
        self.splitter_4.setObjectName("splitter_4")
        self.widget2 = QtWidgets.QWidget(self.splitter_4)
        self.widget2.setObjectName("widget2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pgemodsnfentnamesnf = QtWidgets.QLineEdit(self.widget2)
        self.pgemodsnfentnamesnf.setObjectName("pgemodsnfentnamesnf")
        self.horizontalLayout_3.addWidget(self.pgemodsnfentnamesnf)
        self.label_5 = QtWidgets.QLabel(self.widget2)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.widget3 = QtWidgets.QWidget(self.splitter_4)
        self.widget3.setObjectName("widget3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget3)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pgemodsnfentdatesnf = QtWidgets.QLineEdit(self.widget3)
        self.pgemodsnfentdatesnf.setObjectName("pgemodsnfentdatesnf")
        self.horizontalLayout_4.addWidget(self.pgemodsnfentdatesnf)
        self.label_6 = QtWidgets.QLabel(self.widget3)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_4.addWidget(self.label_6)
        self.widget4 = QtWidgets.QWidget(self.splitter_4)
        self.widget4.setObjectName("widget4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget4)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pgemodsnfentbarcod = QtWidgets.QLineEdit(self.widget4)
        self.pgemodsnfentbarcod.setObjectName("pgemodsnfentbarcod")
        self.horizontalLayout_5.addWidget(self.pgemodsnfentbarcod)
        self.label_7 = QtWidgets.QLabel(self.widget4)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_5.addWidget(self.label_7)
        self.widget5 = QtWidgets.QWidget(self.splitter_4)
        self.widget5.setObjectName("widget5")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget5)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.pgemodsnfentamount = QtWidgets.QLineEdit(self.widget5)
        self.pgemodsnfentamount.setObjectName("pgemodsnfentamount")
        self.horizontalLayout_6.addWidget(self.pgemodsnfentamount)
        self.label_8 = QtWidgets.QLabel(self.widget5)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_6.addWidget(self.label_8)
        self.widget6 = QtWidgets.QWidget(self.splitter_4)
        self.widget6.setObjectName("widget6")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.widget6)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.pgemodsnfentpric = QtWidgets.QLineEdit(self.widget6)
        self.pgemodsnfentpric.setObjectName("pgemodsnfentpric")
        self.horizontalLayout_7.addWidget(self.pgemodsnfentpric)
        self.label_9 = QtWidgets.QLabel(self.widget6)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_7.addWidget(self.label_9)
        self.widget7 = QtWidgets.QWidget(self.splitter_4)
        self.widget7.setObjectName("widget7")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.widget7)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.pgemodsnfenttype = QtWidgets.QLineEdit(self.widget7)
        self.pgemodsnfenttype.setObjectName("pgemodsnfenttype")
        self.horizontalLayout_8.addWidget(self.pgemodsnfenttype)
        self.label_10 = QtWidgets.QLabel(self.widget7)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_8.addWidget(self.label_10)
        self.widget8 = QtWidgets.QWidget(self.splitter_4)
        self.widget8.setObjectName("widget8")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.widget8)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.pgemodsnfentdatepro = QtWidgets.QLineEdit(self.widget8)
        self.pgemodsnfentdatepro.setObjectName("pgemodsnfentdatepro")
        self.horizontalLayout_9.addWidget(self.pgemodsnfentdatepro)
        self.label_12 = QtWidgets.QLabel(self.widget8)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_9.addWidget(self.label_12)
        self.widget9 = QtWidgets.QWidget(self.splitter_4)
        self.widget9.setObjectName("widget9")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.widget9)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.pgemodsnfentdateout = QtWidgets.QLineEdit(self.widget9)
        self.pgemodsnfentdateout.setObjectName("pgemodsnfentdateout")
        self.horizontalLayout_10.addWidget(self.pgemodsnfentdateout)
        self.label_11 = QtWidgets.QLabel(self.widget9)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_10.addWidget(self.label_11)
        self.splitter_3 = QtWidgets.QSplitter(self.splitter_4)
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName("splitter_3")
        self.pgemodsnfbutdelet = QtWidgets.QPushButton(self.splitter_3)
        self.pgemodsnfbutdelet.setObjectName("pgemodsnfbutdelet")
        self.pgemodsnfbutsavemod = QtWidgets.QPushButton(self.splitter_3)
        self.pgemodsnfbutsavemod.setObjectName("pgemodsnfbutsavemod")
        self.gridLayout_2.addWidget(self.splitter_5, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 0, 1, 1, 1)
        MainWindow1.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow1)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 612, 27))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
       
        



        self.retranslateUi(MainWindow1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow1)

    def retranslateUi(self, MainWindow1):
        _translate = QtCore.QCoreApplication.translate
        MainWindow1.setWindowTitle(_translate("MainWindow1", "نافذة التعديلات"))
        self.groupBox.setTitle(_translate("MainWindow1", "تعديل او حذف اي صنف:"))
        self.label_4.setText(_translate("MainWindow1", "باستخدام الباركود:"))
        self.label_3.setText(_translate("MainWindow1", "باستخدام الاسم:"))
        self.label_2.setText(_translate("MainWindow1", "ادخل الصنف:"))
        self.label_5.setText(_translate("MainWindow1", "اسم الصنف:"))
        self.label_6.setText(_translate("MainWindow1", "تاريخ الادخال:"))
        self.label_7.setText(_translate("MainWindow1", "رقم الباركود:"))
        self.label_8.setText(_translate("MainWindow1", "الكمية:"))
        self.label_9.setText(_translate("MainWindow1", "السعر:"))
        self.label_10.setText(_translate("MainWindow1", "نوع الصنف:"))
        self.label_12.setText(_translate("MainWindow1", "تاريخ الانتاج:"))
        self.label_11.setText(_translate("MainWindow1", "تاريخ الانتهاء:"))
        self.pgemodsnfbutdelet.setText(_translate("MainWindow1", "حذف صنف"))
        self.pgemodsnfbutsavemod.setText(_translate("MainWindow1", "حفظ التعديلات"))
        
class NotePad1(QtWidgets.QMainWindow):
	def __init__(self, parent=None):
		QtWidgets.QWidget.__init__(self, parent)#lambda:تضعها عند اسم الزر
		self.ui1 = Ui_MainWindow1()
		self.ui1.setupUi(self)



##################################################main class1###########################################




class Ui_copyy(object):
   
    def setupUi(self, copyy):
        copyy.setObjectName("copyy")
        copyy.resize(524, 441)
        copyy.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(245, 224, 176, 255), stop:0.09 rgba(246, 189, 237, 255), stop:0.14 rgba(194, 207, 246, 255), stop:0.19 rgba(184, 160, 168, 255), stop:0.25 rgba(171, 186, 248, 255), stop:0.32 rgba(243, 248, 224, 255), stop:0.385 rgba(249, 162, 183, 255), stop:0.47 rgba(100, 115, 124, 255), stop:0.58 rgba(251, 205, 202, 255), stop:0.65 rgba(170, 128, 185, 255), stop:0.75 rgba(252, 222, 204, 255), stop:0.805 rgba(206, 122, 218, 255), stop:0.86 rgba(254, 223, 175, 255), stop:0.91 rgba(254, 236, 244, 255), stop:1 rgba(255, 191, 221, 255));")
        copyy.setDocumentMode(False)
        copyy.setDockNestingEnabled(True)
        copyy.setDockOptions(QtWidgets.QMainWindow.AllowNestedDocks|QtWidgets.QMainWindow.AllowTabbedDocks)
        copyy.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(copyy)
        self.centralwidget.setObjectName("centralwidget")
        self.c1 = QtWidgets.QRadioButton(self.centralwidget)
        self.c1.setGeometry(QtCore.QRect(120, 120, 101, 31))
        self.c1.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(40, 154, 244, 255), stop:1 rgba(255, 255, 255, 255));")
        self.c1.setObjectName("c1")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 30, 331, 41))
        self.label.setStyleSheet("font: 75 16pt \"Noto Sans\";")
        self.label.setObjectName("label")
        self.c2 = QtWidgets.QRadioButton(self.centralwidget)
        self.c2.setGeometry(QtCore.QRect(120, 180, 102, 31))
        self.c2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(40, 154, 244, 255), stop:1 rgba(255, 255, 255, 255));")
        self.c2.setObjectName("c2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(180, 250, 301, 31))
        self.label_2.setStyleSheet("font: 75 12pt \"Noto Sans\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(40, 154, 244, 255), stop:1 rgba(255, 255, 255, 255));")
        self.label_2.setObjectName("label_2")
        self.butok = QtWidgets.QPushButton(self.centralwidget)
        self.butok.setGeometry(QtCore.QRect(170, 350, 101, 31))
        self.butok.setStyleSheet("background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(214, 255, 170, 255), stop:1 rgba(255, 255, 255, 255));")
        self.butok.setObjectName("butok")
        self.enternumber = QtWidgets.QLineEdit(self.centralwidget)
        self.enternumber.setGeometry(QtCore.QRect(10, 240, 161, 51))
        self.enternumber.setStyleSheet("color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(244, 117, 117, 255), stop:1 rgba(255, 255, 255, 255));")
        self.enternumber.setObjectName("enternumber")
        copyy.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(copyy)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 524, 27))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        copyy.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(copyy)
        self.statusbar.setObjectName("statusbar")
        copyy.setStatusBar(self.statusbar)
        self.action_2 = QtWidgets.QAction(copyy)
        self.action_2.setObjectName("action_2")
        self.action_3 = QtWidgets.QAction(copyy)
        self.action_3.setObjectName("action_3")
        self.menu.addAction(self.action_2)
        self.menu.addAction(self.action_3)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(copyy)
        QtCore.QMetaObject.connectSlotsByName(copyy)

    def retranslateUi(self, copyy):
        _translate = QtCore.QCoreApplication.translate
        copyy.setWindowTitle(_translate("copyy", "MainWindow"))
        self.c1.setText(_translate("copyy", "نسخة تجريبية "))
        self.label.setText(_translate("copyy", "اختر نوع النسخة التي تريدها"))
        self.c2.setText(_translate("copyy", "نسخة أصلية"))
        self.label_2.setText(_translate("copyy", "ادخل رقم السيريال اذا كنت تريد نسخة اصلية:"))
        self.butok.setText(_translate("copyy", "موافق"))
        self.menu.setTitle(_translate("copyy", "ملاحظه"))
        self.action_2.setText(_translate("copyy", "عن النسخة التجريبيه"))
        self.action_3.setText(_translate("copyy", "عن النسخة الاصلية"))
class NotePad2(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)#lambda:تضعها عند اسم الزر
        self.ui2 = Ui_copyy()
        self.ui2.setupUi(self)
        self.ui2.butok.clicked.connect(self.cock)
        self.ui2.action_2.triggered.connect(self.noteex)
        self.ui2.action_3.triggered.connect(self.notenum)
    def cock(self):

    	if self.ui2.c1.isChecked() == True:
    		db3=sqlite3.connect('ship.db')
    		u1=[]
    		db3.row_factory=sqlite3.Row
    		db3.execute("insert into shb1(t1,t2) values(?,?)",('ap','p'))
    		db3.commit()
    		fg1=db3.execute("select * from shb1")
    		for n in fg1:
    			u1.append(["t2"])
    		if len(u1)>4:
    			message=QtWidgets.QMessageBox.information(self,'information','<FONT size=10 color=blue>عذرا عزيزي المستخدم لقد انتهت مدة الفترة التجريبية</FONT>')
    		
    		else:
	    		#self.app2 = QtWidgets.QApplication(sys.argv)
	    		self.myapp2 = NotePad()
	    		self.myapp2.show()
	    		#sys.exit(app2.exec_())
    	elif self.ui2.c2.isChecked() == True:
    		sir=str(self.ui2.enternumber.text())
    		if sir=="909090":
    			db5=sqlite3.connect('ship.db')
    			db5.row_factory=sqlite3.Row
    			db5.execute("insert into shb1(t1,t3) values(?,?)",('ooo','i'))
    			db5.commit()
    			
    			#app2 = QtWidgets.QApplication(sys.argv)
    			self.myapp2 = NotePad()
    			self.myapp2.show()
    			#sys.exit(app2.exec_())
    		else:message=QtWidgets.QMessageBox.information(self,'information','<FONT size=10 color=blue>خطاء في الرقم اعد المحاولة مره اخرى</FONT>')

    	else:
    		exit()

    def noteex(self):
    	message=QtWidgets.QMessageBox.information(self,'information','<FONT size=10 color=blue>النسخة التجريبيه في هذا البرنامج تكون بعدد مرات تشغيل البرنامج وهي 20 مره فقط ثم يتوقف البرنامج</FONT>')
    def notenum(self):
    	message=QtWidgets.QMessageBox.information(self,'information','<FONT size=10 color=blue>اذا كنت تريد نسخة اصللية للبرنامج عليك بادخال رقم السيريال اذا لم يكن لديك يرجاء الحصول عليه من الايميل التالي:<p>99zzz52@gmail.com</p><p>او الاتصال على الرقم :713151679</p></FONT>')


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     myapp = NotePad2()
# myapp.show()
# sys.exit(app.exec_())





#######################################################main class2###########################################
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(975, 612)

        MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:0, stop:1 rgba(125, 117, 244, 255));")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 235, 235, 206), stop:0.35 rgba(255, 188, 188, 80), stop:0.4 rgba(255, 162, 162, 80), stop:0.425 rgba(255, 132, 132, 156), stop:0.44 rgba(252, 128, 128, 80), stop:1 rgba(255, 255, 255, 0));")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.page)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.frame_2 = QtWidgets.QFrame(self.page)
        self.frame_2.setStyleSheet("background-color: qradialgradient(spread:reflect, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(117, 244, 78, 255), stop:1 rgba(255, 255, 255, 255));")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.pagemain = QtWidgets.QTabWidget(self.frame_2)
        self.pagemain.setObjectName("pagemain")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.splitter_4 = QtWidgets.QSplitter(self.tab)
        self.splitter_4.setOrientation(QtCore.Qt.Vertical)
        self.splitter_4.setObjectName("splitter_4")
        self.splitter_2 = QtWidgets.QSplitter(self.splitter_4)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.pagmtab1comqmi = QtWidgets.QComboBox(self.splitter_2)
        self.pagmtab1comqmi.setEditable(True)
        self.pagmtab1comqmi.setObjectName("pagmtab1comqmi")
        self.pagmtab1comqmi.addItem("")
        self.pagmtab1comqmi.addItem("")
        self.pagmtab1comqmi.addItem("")
        self.pagmtab1comqmi.addItem("")
        self.pagmtab1comqmi.addItem("")
        self.pagmtab1comqmi.addItem("")
        self.pagmtab1comqmi.addItem("")
        self.pagmtab1comqmi.addItem("")
        self.pagmtab1comqmi.addItem("")
        self.pagmtab1comqmi.addItem("")
        self.label_3 = QtWidgets.QLabel(self.splitter_2)
        self.label_3.setStyleSheet("font: 75 italic 11pt \"Noto Sans\";\n"
"font: 75 11pt \"Noto Sans\";")
        self.label_3.setObjectName("label_3")
        self.pagmtab1entprc = QtWidgets.QLineEdit(self.splitter_2)
        self.pagmtab1entprc.setObjectName("pagmtab1entprc")
        self.label_2 = QtWidgets.QLabel(self.splitter_2)
        self.label_2.setStyleSheet("font: 75 italic 11pt \"Noto Sans\";\n"
"font: 75 11pt \"Noto Sans\";")
        self.label_2.setObjectName("label_2")
        self.pagmtab1entbarkod = QtWidgets.QLineEdit(self.splitter_2)
        self.pagmtab1entbarkod.setText("")
        self.pagmtab1entbarkod.setObjectName("pagmtab1entbarkod")
        self.label = QtWidgets.QLabel(self.splitter_2)
        self.label.setStyleSheet("font: 75 italic 11pt \"Noto Sans\";\n"
"font: 75 11pt \"Noto Sans\";")
        self.label.setObjectName("label")
        self.splitter_3 = QtWidgets.QSplitter(self.splitter_4)
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName("splitter_3")
        self.pagmtab1butdelet = QtWidgets.QPushButton(self.splitter_3)
        self.pagmtab1butdelet.setObjectName("pagmtab1butdelet")
        self.pagmtab1butprint = QtWidgets.QPushButton(self.splitter_3)
        self.pagmtab1butprint.setObjectName("pagmtab1butprint")
        self.pagmtab1text = QtWidgets.QTextEdit(self.splitter_4)
        self.pagmtab1text.setObjectName("pagmtab1text")
        self.gridLayout_5.addWidget(self.splitter_4, 0, 0, 1, 1)
        self.pagemain.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.splitter_7 = QtWidgets.QSplitter(self.tab_2)
        self.splitter_7.setOrientation(QtCore.Qt.Vertical)
        self.splitter_7.setObjectName("splitter_7")
        self.splitter_5 = QtWidgets.QSplitter(self.splitter_7)
        self.splitter_5.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_5.setObjectName("splitter_5")
        self.pagmtab2comqmi = QtWidgets.QComboBox(self.splitter_5)
        self.pagmtab2comqmi.setEditable(True)
        self.pagmtab2comqmi.setObjectName("pagmtab2comqmi")
        self.pagmtab2comqmi.addItem("")
        self.pagmtab2comqmi.addItem("")
        self.pagmtab2comqmi.addItem("")
        self.pagmtab2comqmi.addItem("")
        self.pagmtab2comqmi.addItem("")
        self.pagmtab2comqmi.addItem("")
        self.pagmtab2comqmi.addItem("")
        self.pagmtab2comqmi.addItem("")
        self.pagmtab2comqmi.addItem("")
        self.pagmtab2comqmi.addItem("")
        self.label_6 = QtWidgets.QLabel(self.splitter_5)
        self.label_6.setStyleSheet("font: 75 11pt \"Noto Sans\";")
        self.label_6.setObjectName("label_6")
        self.pagmtab2butpric = QtWidgets.QLineEdit(self.splitter_5)
        self.pagmtab2butpric.setObjectName("pagmtab2butpric")
        self.label_5 = QtWidgets.QLabel(self.splitter_5)
        self.label_5.setStyleSheet("font: 75 11pt \"Noto Sans\";")
        self.label_5.setObjectName("label_5")
        self.pagmtab2comnamesnf = QtWidgets.QComboBox(self.splitter_5)
        self.pagmtab2comnamesnf.setEditable(True)
        self.pagmtab2comnamesnf.setObjectName("pagmtab2comnamesnf")
        self.label_4 = QtWidgets.QLabel(self.splitter_5)
        self.label_4.setStyleSheet("font: 75 11pt \"Noto Sans\";")
        self.label_4.setObjectName("label_4")
        self.splitter_6 = QtWidgets.QSplitter(self.splitter_7)
        self.splitter_6.setOrientation(QtCore.Qt.Vertical)
        self.splitter_6.setObjectName("splitter_6")
        self.layoutWidget = QtWidgets.QWidget(self.splitter_6)
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pagmtab2butdelet = QtWidgets.QPushButton(self.layoutWidget)
        self.pagmtab2butdelet.setObjectName("pagmtab2butdelet")
        self.horizontalLayout.addWidget(self.pagmtab2butdelet)
        self.pagmtab2butprint = QtWidgets.QPushButton(self.layoutWidget)
        self.pagmtab2butprint.setObjectName("pagmtab2butprint")
        self.horizontalLayout.addWidget(self.pagmtab2butprint)
        self.pagmtab2text = QtWidgets.QTextEdit(self.splitter_6)
        self.pagmtab2text.setObjectName("pagmtab2text")
        self.gridLayout_6.addWidget(self.splitter_7, 0, 0, 1, 1)
        self.pagemain.addTab(self.tab_2, "")
        self.gridLayout_4.addWidget(self.pagemain, 0, 1, 1, 1)
        self.gridLayout_3.addWidget(self.frame_2, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page)
        self.pagereport = QtWidgets.QWidget()
        self.pagereport.setObjectName("pagereport")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.pagereport)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.frame_4 = QtWidgets.QFrame(self.pagereport)
        self.frame_4.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0.036, y2:1, stop:0 rgba(0, 255, 100, 255), stop:0.0318182 rgba(234, 216, 11, 255), stop:0.05 rgba(255, 149, 58, 255), stop:0.0727273 rgba(169, 255, 75, 255));")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.splitter_10 = QtWidgets.QSplitter(self.frame_4)
        self.splitter_10.setOrientation(QtCore.Qt.Vertical)
        self.splitter_10.setObjectName("splitter_10")
        self.layoutWidget1 = QtWidgets.QWidget(self.splitter_10)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pagreportcomtypereport = QtWidgets.QComboBox(self.layoutWidget1)
        self.pagreportcomtypereport.setEditable(True)
        self.pagreportcomtypereport.setObjectName("pagreportcomtypereport")
        self.pagreportcomtypereport.addItem("")
        self.pagreportcomtypereport.addItem("")
        self.pagreportcomtypereport.addItem("")
        self.horizontalLayout_3.addWidget(self.pagreportcomtypereport)
        self.label_12 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_12.setStyleSheet("font: 75 11pt \"Noto Sans\";")
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_3.addWidget(self.label_12)
        self.pagreportcomaboutreport = QtWidgets.QComboBox(self.layoutWidget1)
        self.pagreportcomaboutreport.setEditable(True)
        self.pagreportcomaboutreport.setObjectName("pagreportcomaboutreport")
        self.pagreportcomaboutreport.addItem("")
        self.pagreportcomaboutreport.addItem("")
        self.pagreportcomaboutreport.addItem("")
        self.pagreportcomaboutreport.addItem("")
        self.horizontalLayout_3.addWidget(self.pagreportcomaboutreport)
        self.label_11 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_11.setStyleSheet("font: 75 11pt \"Noto Sans\";")
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_3.addWidget(self.label_11)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pagreportcomoncdetermain = QtWidgets.QComboBox(self.layoutWidget1)
        self.pagreportcomoncdetermain.setEditable(True)
        self.pagreportcomoncdetermain.setObjectName("pagreportcomoncdetermain")
        self.horizontalLayout_4.addWidget(self.pagreportcomoncdetermain)
        self.label_13 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_13.setStyleSheet("font: 75 11pt \"Noto Sans\";")
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_4.addWidget(self.label_13)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pagreportcomononc = QtWidgets.QComboBox(self.layoutWidget1)
        self.pagreportcomononc.setEditable(True)
        self.pagreportcomononc.setObjectName("pagreportcomononc")
        self.horizontalLayout_5.addWidget(self.pagreportcomononc)
        self.label_15 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_15.setStyleSheet("font: 75 11pt \"Noto Sans\";")
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_5.addWidget(self.label_15)
        self.pagreportcomfromonc_2 = QtWidgets.QComboBox(self.layoutWidget1)
        self.pagreportcomfromonc_2.setEditable(True)
        self.pagreportcomfromonc_2.setObjectName("pagreportcomfromonc_2")
        self.horizontalLayout_5.addWidget(self.pagreportcomfromonc_2)
        self.label_14 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_14.setStyleSheet("font: 75 11pt \"Noto Sans\";")
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_5.addWidget(self.label_14)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.pagreportbutprintreport = QtWidgets.QPushButton(self.layoutWidget1)
        self.pagreportbutprintreport.setObjectName("pagreportbutprintreport")
        self.verticalLayout_4.addWidget(self.pagreportbutprintreport)
        self.textEdit_3 = QtWidgets.QTextEdit(self.splitter_10)
        self.textEdit_3.setObjectName("textEdit_3")
        self.gridLayout_13.addWidget(self.splitter_10, 0, 0, 1, 1)
        self.gridLayout_12.addWidget(self.frame_4, 0, 1, 1, 1)
        self.stackedWidget.addWidget(self.pagereport)
        self.pageenterdata = QtWidgets.QWidget()
        self.pageenterdata.setObjectName("pageenterdata")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.pageenterdata)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.splitter_17 = QtWidgets.QSplitter(self.pageenterdata)
        self.splitter_17.setOrientation(QtCore.Qt.Vertical)
        self.splitter_17.setObjectName("splitter_17")
        self.layoutWidget2 = QtWidgets.QWidget(self.splitter_17)
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_7 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_7.setStyleSheet("font: 75 12pt \"Noto Sans\";")
        self.label_7.setObjectName("label_7")
        self.verticalLayout_2.addWidget(self.label_7)
        self.line = QtWidgets.QFrame(self.layoutWidget2)
        self.line.setStyleSheet("color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.splitter_14 = QtWidgets.QSplitter(self.splitter_17)
        self.splitter_14.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_14.setObjectName("splitter_14")
        self.pagenterdatacomqmesenf = QtWidgets.QComboBox(self.splitter_14)
        self.pagenterdatacomqmesenf.setEditable(True)
        self.pagenterdatacomqmesenf.setObjectName("pagenterdatacomqmesenf")
        self.pagenterdatacomqmesenf.addItem("")
        self.pagenterdatacomqmesenf.addItem("")
        self.pagenterdatacomqmesenf.addItem("")
        self.pagenterdatacomqmesenf.addItem("")
        self.label_10 = QtWidgets.QLabel(self.splitter_14)
        self.label_10.setStyleSheet("font: 75 11pt \"Noto Sans\";")
        self.label_10.setObjectName("label_10")
        self.pagenterdataentbarcod = QtWidgets.QLineEdit(self.splitter_14)
        self.pagenterdataentbarcod.setObjectName("pagenterdataentbarcod")
        self.label_9 = QtWidgets.QLabel(self.splitter_14)
        self.label_9.setStyleSheet("font: 75 11pt \"Noto Sans\";")
        self.label_9.setObjectName("label_9")
        self.pagenterdataentnamesenf = QtWidgets.QLineEdit(self.splitter_14)
        self.pagenterdataentnamesenf.setObjectName("pagenterdataentnamesenf")
        self.label_8 = QtWidgets.QLabel(self.splitter_14)
        self.label_8.setStyleSheet("font: 75 11pt \"Noto Sans\";")
        self.label_8.setObjectName("label_8")
        self.splitter_15 = QtWidgets.QSplitter(self.splitter_17)
        self.splitter_15.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_15.setObjectName("splitter_15")
        self.pagenterdatacomtypesnf = QtWidgets.QComboBox(self.splitter_15)
        self.pagenterdatacomtypesnf.setObjectName("pagenterdatacomtypesnf")
        self.pagenterdatacomtypesnf.addItem("")
        self.pagenterdatacomtypesnf.addItem("")
        self.pagenterdatacomtypesnf.addItem("")
        self.label_22 = QtWidgets.QLabel(self.splitter_15)
        self.label_22.setStyleSheet("font: 75 11pt \"Noto Sans\";")
        self.label_22.setObjectName("label_22")
        self.pagenterdataentpricsanf = QtWidgets.QLineEdit(self.splitter_15)
        self.pagenterdataentpricsanf.setObjectName("pagenterdataentpricsanf")
        self.label_21 = QtWidgets.QLabel(self.splitter_15)
        self.label_21.setStyleSheet("font: 75 11pt \"Noto Sans\";")
        self.label_21.setObjectName("label_21")
        self.splitter_16 = QtWidgets.QSplitter(self.splitter_17)
        self.splitter_16.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_16.setObjectName("splitter_16")
        self.pagenterdataentdateoutsanf = QtWidgets.QLineEdit(self.splitter_16)
        self.pagenterdataentdateoutsanf.setText("")
        self.pagenterdataentdateoutsanf.setObjectName("pagenterdataentdateoutsanf")
        self.label_29 = QtWidgets.QLabel(self.splitter_16)
        self.label_29.setStyleSheet("font: 75 11pt \"Noto Sans\";")
        self.label_29.setObjectName("label_29")
        self.pagenterdataentdateproductsanf = QtWidgets.QLineEdit(self.splitter_16)
        self.pagenterdataentdateproductsanf.setObjectName("pagenterdataentdateproductsanf")
        self.label_28 = QtWidgets.QLabel(self.splitter_16)
        self.label_28.setStyleSheet("font: 75 11pt \"Noto Sans\";")
        self.label_28.setObjectName("label_28")
        self.pagenterdatabutaddsanf = QtWidgets.QPushButton(self.splitter_17)
        self.pagenterdatabutaddsanf.setStyleSheet("font: 75 11pt \"Noto Sans\";")
        self.pagenterdatabutaddsanf.setObjectName("pagenterdatabutaddsanf")
        self.line_3 = QtWidgets.QFrame(self.splitter_17)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout_11.addWidget(self.splitter_17, 0, 0, 1, 1)
        self.splitter_21 = QtWidgets.QSplitter(self.pageenterdata)
        self.splitter_21.setOrientation(QtCore.Qt.Vertical)
        self.splitter_21.setObjectName("splitter_21")
        self.layoutWidget3 = QtWidgets.QWidget(self.splitter_21)
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_23 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_23.setStyleSheet("font: 75 12pt \"Noto Sans\";")
        self.label_23.setObjectName("label_23")
        self.verticalLayout_3.addWidget(self.label_23)
        self.line_4 = QtWidgets.QFrame(self.layoutWidget3)
        self.line_4.setStyleSheet("color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout_3.addWidget(self.line_4)
        self.splitter_18 = QtWidgets.QSplitter(self.splitter_21)
        self.splitter_18.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_18.setObjectName("splitter_18")
        self.pagenterdatacomqmemstord = QtWidgets.QComboBox(self.splitter_18)
        self.pagenterdatacomqmemstord.setEditable(True)
        self.pagenterdatacomqmemstord.setObjectName("pagenterdatacomqmemstord")
        self.pagenterdatacomqmemstord.addItem("")
        self.pagenterdatacomqmemstord.addItem("")
        self.pagenterdatacomqmemstord.addItem("")
        self.pagenterdatacomqmemstord.addItem("")
        self.label_25 = QtWidgets.QLabel(self.splitter_18)
        self.label_25.setStyleSheet("font: 75 11pt \"Noto Sans\";")
        self.label_25.setObjectName("label_25")
        self.pagenterdataentnamemstord = QtWidgets.QLineEdit(self.splitter_18)
        self.pagenterdataentnamemstord.setText("")
        self.pagenterdataentnamemstord.setObjectName("pagenterdataentnamemstord")
        self.label_32 = QtWidgets.QLabel(self.splitter_18)
        self.label_32.setStyleSheet("font: 75 11pt \"Noto Sans\";")
        self.label_32.setObjectName("label_32")
        self.pagenterdataentmsdertored = QtWidgets.QLineEdit(self.splitter_18)
        self.pagenterdataentmsdertored.setObjectName("pagenterdataentmsdertored")
        self.label_24 = QtWidgets.QLabel(self.splitter_18)
        self.label_24.setStyleSheet("font: 75 11pt \"Noto Sans\";")
        self.label_24.setObjectName("label_24")
        self.splitter_19 = QtWidgets.QSplitter(self.splitter_21)
        self.splitter_19.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_19.setObjectName("splitter_19")
        self.pagenterdataentpricmstord = QtWidgets.QLineEdit(self.splitter_19)
        self.pagenterdataentpricmstord.setObjectName("pagenterdataentpricmstord")
        self.label_27 = QtWidgets.QLabel(self.splitter_19)
        self.label_27.setStyleSheet("font: 75 11pt \"Noto Sans\";")
        self.label_27.setObjectName("label_27")
        self.pagenterdataentdatemstord = QtWidgets.QLineEdit(self.splitter_19)
        self.pagenterdataentdatemstord.setObjectName("pagenterdataentdatemstord")
        self.label_26 = QtWidgets.QLabel(self.splitter_19)
        self.label_26.setStyleSheet("font: 75 11pt \"Noto Sans\";")
        self.label_26.setObjectName("label_26")
        self.splitter_20 = QtWidgets.QSplitter(self.splitter_21)
        self.splitter_20.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_20.setObjectName("splitter_20")
        self.pagenterdataentdateoutmstord = QtWidgets.QLineEdit(self.splitter_20)
        self.pagenterdataentdateoutmstord.setText("")
        self.pagenterdataentdateoutmstord.setObjectName("pagenterdataentdateoutmstord")
        self.label_31 = QtWidgets.QLabel(self.splitter_20)
        self.label_31.setStyleSheet("font: 75 11pt \"Noto Sans\";")
        self.label_31.setObjectName("label_31")
        self.pagenterdataentdateprodectmstord = QtWidgets.QLineEdit(self.splitter_20)
        self.pagenterdataentdateprodectmstord.setObjectName("pagenterdataentdateprodectmstord")
        self.label_30 = QtWidgets.QLabel(self.splitter_20)
        self.label_30.setStyleSheet("font: 75 11pt \"Noto Sans\";")
        self.label_30.setObjectName("label_30")
        self.pagenterdatabutaddmstord = QtWidgets.QPushButton(self.splitter_21)
        self.pagenterdatabutaddmstord.setStyleSheet("font: 75 11pt \"Noto Sans\";")
        self.pagenterdatabutaddmstord.setObjectName("pagenterdatabutaddmstord")
        self.gridLayout_11.addWidget(self.splitter_21, 1, 0, 1, 1)
        self.stackedWidget.addWidget(self.pageenterdata)
        self.pageastalmat = QtWidgets.QWidget()
        self.pageastalmat.setObjectName("pageastalmat")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.pageastalmat)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.splitter_9 = QtWidgets.QSplitter(self.pageastalmat)
        self.splitter_9.setOrientation(QtCore.Qt.Vertical)
        self.splitter_9.setObjectName("splitter_9")
        self.splitter_8 = QtWidgets.QSplitter(self.splitter_9)
        self.splitter_8.setOrientation(QtCore.Qt.Vertical)
        self.splitter_8.setObjectName("splitter_8")
        self.scrollArea = QtWidgets.QScrollArea(self.splitter_8)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 735, 76))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.groupBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox.setObjectName("groupBox")
        self.line_8 = QtWidgets.QFrame(self.groupBox)
        self.line_8.setGeometry(QtCore.QRect(320, 120, 81, 16))
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.label_33 = QtWidgets.QLabel(self.groupBox)
        self.label_33.setGeometry(QtCore.QRect(530, 30, 111, 41))
        self.label_33.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(40, 154, 244, 255), stop:1 rgba(255, 255, 255, 255));")
        self.label_33.setObjectName("label_33")
        self.line_6 = QtWidgets.QFrame(self.groupBox)
        self.line_6.setGeometry(QtCore.QRect(397, 60, 131, 20))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.label_34 = QtWidgets.QLabel(self.groupBox)
        self.label_34.setGeometry(QtCore.QRect(230, 20, 91, 41))
        self.label_34.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(40, 154, 244, 255), stop:1 rgba(255, 255, 255, 255));")
        self.label_34.setObjectName("label_34")
        self.comboBox_10 = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_10.setGeometry(QtCore.QRect(80, 110, 131, 41))
        self.comboBox_10.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(40, 154, 244, 255), stop:1 rgba(255, 255, 255, 255));")
        self.comboBox_10.setEditable(True)
        self.comboBox_10.setObjectName("comboBox_10")
        self.pagstalmentbarcod = QtWidgets.QLineEdit(self.groupBox)
        self.pagstalmentbarcod.setGeometry(QtCore.QRect(80, 20, 141, 41))
        self.pagstalmentbarcod.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:0, stop:1 rgba(125, 117, 244, 255));\n"
"font: 75 9pt \"Noto Sans\";")
        self.pagstalmentbarcod.setText("")
        self.pagstalmentbarcod.setObjectName("pagstalmentbarcod")
        self.line_5 = QtWidgets.QFrame(self.groupBox)
        self.line_5.setGeometry(QtCore.QRect(327, 30, 201, 20))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_7 = QtWidgets.QFrame(self.groupBox)
        self.line_7.setGeometry(QtCore.QRect(390, 70, 20, 61))
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.label_35 = QtWidgets.QLabel(self.groupBox)
        self.label_35.setGeometry(QtCore.QRect(240, 110, 81, 41))
        self.label_35.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(40, 154, 244, 255), stop:1 rgba(255, 255, 255, 255));")
        self.label_35.setObjectName("label_35")
        self.gridLayout_9.addWidget(self.groupBox, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.pagstalmtabl = QtWidgets.QTextEdit(self.splitter_8)
        
        self.pagstalmtabl.setObjectName("pagstalmtabl")
        
        self.frame_3 = QtWidgets.QFrame(self.splitter_9)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.groupBox_2 = QtWidgets.QGroupBox(self.frame_3)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pagstalmbutqmetremain = QtWidgets.QPushButton(self.groupBox_2)
        self.pagstalmbutqmetremain.setObjectName("pagstalmbutqmetremain")
        self.horizontalLayout_2.addWidget(self.pagstalmbutqmetremain)
        #self.pagstalmbutmodesadrat = QtWidgets.QPushButton(self.groupBox_2)
        #self.pagstalmbutmodesadrat.setObjectName("pagstalmbutmodesadrat")
        #self.horizontalLayout_2.addWidget(self.pagstalmbutmodesadrat)
        #self.pagstalmbutmodemstordat = QtWidgets.QPushButton(self.groupBox_2)
        #self.pagstalmbutmodemstordat.setObjectName("pagstalmbutmodemstordat")
        #self.horizontalLayout_2.addWidget(self.pagstalmbutmodemstordat)
        self.pagstalmbutmodesenf = QtWidgets.QPushButton(self.groupBox_2)
        self.pagstalmbutmodesenf.setObjectName("pagstalmbutmodesenf")
        self.horizontalLayout_2.addWidget(self.pagstalmbutmodesenf)
        self.gridLayout_10.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.gridLayout_8.addWidget(self.groupBox_2, 0, 0, 1, 1)
        self.gridLayout_7.addWidget(self.splitter_9, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.pageastalmat)
        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 975, 27))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)###################
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
       
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionGo = QtWidgets.QAction(MainWindow)
        self.actionGo.setObjectName("actionGo")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        #self.menuFile.addAction(self.actionAbout)
        self.menuFile.addAction(self.actionGo)
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())
#############################################
        self.dockWidget = QtWidgets.QDockWidget(MainWindow)
        self.dockWidget.setFeatures(QtWidgets.QDockWidget.DockWidgetFloatable|QtWidgets.QDockWidget.DockWidgetMovable)
        self.dockWidget.setAllowedAreas(QtCore.Qt.NoDockWidgetArea)
        self.dockWidget.setObjectName("dockWidget")
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.dockWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame = QtWidgets.QFrame(self.dockWidgetContents)
        self.frame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(244, 117, 117, 255), stop:1 rgba(255, 255, 255, 255));")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.splitter = QtWidgets.QSplitter(self.frame)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.butmainpage = QtWidgets.QPushButton(self.splitter)
        self.butmainpage.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(245, 224, 176, 255), stop:0.09 rgba(246, 189, 237, 255), stop:0.14 rgba(194, 207, 246, 255), stop:0.19 rgba(184, 160, 168, 255), stop:0.25 rgba(171, 186, 248, 255), stop:0.32 rgba(243, 248, 224, 255), stop:0.385 rgba(249, 162, 183, 255), stop:0.47 rgba(100, 115, 124, 255), stop:0.58 rgba(251, 205, 202, 255), stop:0.65 rgba(170, 128, 185, 255), stop:0.75 rgba(252, 222, 204, 255), stop:0.805 rgba(206, 122, 218, 255), stop:0.86 rgba(254, 223, 175, 255), stop:0.91 rgba(254, 236, 244, 255), stop:1 rgba(255, 191, 221, 255));\n"
"font: 75 20pt \"NanumMyeongjo\";")
        self.butmainpage.setAutoDefault(False)
        self.butmainpage.setFlat(False)
        self.butmainpage.setObjectName("butmainpage")
        self.butastalam = QtWidgets.QPushButton(self.splitter)
        self.butastalam.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(245, 224, 176, 255), stop:0.09 rgba(246, 189, 237, 255), stop:0.14 rgba(194, 207, 246, 255), stop:0.19 rgba(184, 160, 168, 255), stop:0.25 rgba(171, 186, 248, 255), stop:0.32 rgba(243, 248, 224, 255), stop:0.385 rgba(249, 162, 183, 255), stop:0.47 rgba(100, 115, 124, 255), stop:0.58 rgba(251, 205, 202, 255), stop:0.65 rgba(170, 128, 185, 255), stop:0.75 rgba(252, 222, 204, 255), stop:0.805 rgba(206, 122, 218, 255), stop:0.86 rgba(254, 223, 175, 255), stop:0.91 rgba(254, 236, 244, 255), stop:1 rgba(255, 191, 221, 255));\n"
"border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(244, 117, 117, 255), stop:1 rgba(255, 255, 255, 255));\n"
"font: 75 20pt \"NanumMyeongjo\";")
        self.butastalam.setObjectName("butastalam")
        self.butreport = QtWidgets.QPushButton(self.splitter)
        self.butreport.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(245, 224, 176, 255), stop:0.09 rgba(246, 189, 237, 255), stop:0.14 rgba(194, 207, 246, 255), stop:0.19 rgba(184, 160, 168, 255), stop:0.25 rgba(171, 186, 248, 255), stop:0.32 rgba(243, 248, 224, 255), stop:0.385 rgba(249, 162, 183, 255), stop:0.47 rgba(100, 115, 124, 255), stop:0.58 rgba(251, 205, 202, 255), stop:0.65 rgba(170, 128, 185, 255), stop:0.75 rgba(252, 222, 204, 255), stop:0.805 rgba(206, 122, 218, 255), stop:0.86 rgba(254, 223, 175, 255), stop:0.91 rgba(254, 236, 244, 255), stop:1 rgba(255, 191, 221, 255));\n"
"font: 75 20pt \"NanumMyeongjo\";")
        self.butreport.setObjectName("butreport")
        self.butenterdata = QtWidgets.QPushButton(self.splitter)
        self.butenterdata.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(245, 224, 176, 255), stop:0.09 rgba(246, 189, 237, 255), stop:0.14 rgba(194, 207, 246, 255), stop:0.19 rgba(184, 160, 168, 255), stop:0.25 rgba(171, 186, 248, 255), stop:0.32 rgba(243, 248, 224, 255), stop:0.385 rgba(249, 162, 183, 255), stop:0.47 rgba(100, 115, 124, 255), stop:0.58 rgba(251, 205, 202, 255), stop:0.65 rgba(170, 128, 185, 255), stop:0.75 rgba(252, 222, 204, 255), stop:0.805 rgba(206, 122, 218, 255), stop:0.86 rgba(254, 223, 175, 255), stop:0.91 rgba(254, 236, 244, 255), stop:1 rgba(255, 191, 221, 255));\n"
"font: 75  20pt \"NanumMyeongjo\";")
        self.butenterdata.setObjectName("butenterdata")
        self.butout = QtWidgets.QPushButton(self.splitter)
        self.butout.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(245, 224, 176, 255), stop:0.09 rgba(246, 189, 237, 255), stop:0.14 rgba(194, 207, 246, 255), stop:0.19 rgba(184, 160, 168, 255), stop:0.25 rgba(171, 186, 248, 255), stop:0.32 rgba(243, 248, 224, 255), stop:0.385 rgba(249, 162, 183, 255), stop:0.47 rgba(100, 115, 124, 255), stop:0.58 rgba(251, 205, 202, 255), stop:0.65 rgba(170, 128, 185, 255), stop:0.75 rgba(252, 222, 204, 255), stop:0.805 rgba(206, 122, 218, 255), stop:0.86 rgba(254, 223, 175, 255), stop:0.91 rgba(254, 236, 244, 255), stop:1 rgba(255, 191, 221, 255));\n"
"font: 75 20pt \"NanumMyeongjo\";")
        self.butout.setObjectName("butout")
        self.verticalLayout.addWidget(self.splitter)
        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)
        self.dockWidget.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockWidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        self.pagemain.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "برنامج محاسبة"))
        self.pagmtab1comqmi.setItemText(0, _translate("MainWindow", "1"))
        self.pagmtab1comqmi.setItemText(1, _translate("MainWindow", "2"))
        self.pagmtab1comqmi.setItemText(2, _translate("MainWindow", "3"))
        self.pagmtab1comqmi.setItemText(3, _translate("MainWindow", "4"))
        self.pagmtab1comqmi.setItemText(4, _translate("MainWindow", "5"))
        self.pagmtab1comqmi.setItemText(5, _translate("MainWindow", "6"))
        self.pagmtab1comqmi.setItemText(6, _translate("MainWindow", "7"))
        self.pagmtab1comqmi.setItemText(7, _translate("MainWindow", "8"))
        self.pagmtab1comqmi.setItemText(8, _translate("MainWindow", "9"))
        self.pagmtab1comqmi.setItemText(9, _translate("MainWindow", "10"))
        self.label_3.setText(_translate("MainWindow", "الكمية:"))
        self.label_2.setText(_translate("MainWindow", "السعر:"))
        self.label.setText(_translate("MainWindow", "ادخل الباركود:"))
        self.pagmtab1butdelet.setText(_translate("MainWindow", "فاتورة جديدة"))
        self.pagmtab1butprint.setText(_translate("MainWindow", "طباعة"))
        self.pagemain.setTabText(self.pagemain.indexOf(self.tab), _translate("MainWindow", "استعلام اكتروني"))
        self.pagmtab2comqmi.setItemText(0, _translate("MainWindow", "1"))
        self.pagmtab2comqmi.setItemText(1, _translate("MainWindow", "2"))
        self.pagmtab2comqmi.setItemText(2, _translate("MainWindow", "3"))
        self.pagmtab2comqmi.setItemText(3, _translate("MainWindow", "4"))
        self.pagmtab2comqmi.setItemText(4, _translate("MainWindow", "5"))
        self.pagmtab2comqmi.setItemText(5, _translate("MainWindow", "6"))
        self.pagmtab2comqmi.setItemText(6, _translate("MainWindow", "7"))
        self.pagmtab2comqmi.setItemText(7, _translate("MainWindow", "8"))
        self.pagmtab2comqmi.setItemText(8, _translate("MainWindow", "9"))
        self.pagmtab2comqmi.setItemText(9, _translate("MainWindow", "10"))
        self.label_6.setText(_translate("MainWindow", "الكمية:"))
        self.label_5.setText(_translate("MainWindow", "السعر:"))
        self.label_4.setText(_translate("MainWindow", "اسم الصنف:"))
        self.pagmtab2butdelet.setText(_translate("MainWindow", "فاتورة جديدة"))
        self.pagmtab2butprint.setText(_translate("MainWindow", "طباعة"))
        self.pagemain.setTabText(self.pagemain.indexOf(self.tab_2), _translate("MainWindow", "استعلام يدوي"))
        self.pagreportcomtypereport.setItemText(0, _translate("MainWindow", "عام"))
        self.pagreportcomtypereport.setItemText(1, _translate("MainWindow", "من فترة محددة"))
        self.pagreportcomtypereport.setItemText(2, _translate("MainWindow", "من فترة الى فترة معينة"))
        self.label_12.setText(_translate("MainWindow", "نوع التقرير:"))
        self.pagreportcomaboutreport.setItemText(0, _translate("MainWindow", "الاصناف"))
        self.pagreportcomaboutreport.setItemText(1, _translate("MainWindow", "الواردات"))
        self.pagreportcomaboutreport.setItemText(2, _translate("MainWindow", "الصادرات"))
        self.pagreportcomaboutreport.setItemText(3, _translate("MainWindow", "الكميات المتبقية من الاصناف"))
        self.label_11.setText(_translate("MainWindow", "تقرير عن:"))
        self.label_13.setText(_translate("MainWindow", "فترة محددة:"))
        self.label_15.setText(_translate("MainWindow", "الى فترة:"))
        self.label_14.setText(_translate("MainWindow", "من فترة:"))
        self.pagreportbutprintreport.setText(_translate("MainWindow", "طباعة"))
        self.label_7.setText(_translate("MainWindow", "اضافة صنف جديد:-"))
        self.pagenterdatacomqmesenf.setItemText(0, _translate("MainWindow", "1"))
        self.pagenterdatacomqmesenf.setItemText(1, _translate("MainWindow", "2"))
        self.pagenterdatacomqmesenf.setItemText(2, _translate("MainWindow", "3"))
        self.pagenterdatacomqmesenf.setItemText(3, _translate("MainWindow", "4"))
        self.label_10.setText(_translate("MainWindow", "الكمية:"))
        self.label_9.setText(_translate("MainWindow", "رقم الباركود:"))
        self.label_8.setText(_translate("MainWindow", "اسم الصنف:"))
        self.pagenterdatacomtypesnf.setItemText(0, _translate("MainWindow", "كرتون"))
        self.pagenterdatacomtypesnf.setItemText(1, _translate("MainWindow", "حبة"))
        self.pagenterdatacomtypesnf.setItemText(2, _translate("MainWindow", "كيس"))
        self.label_22.setText(_translate("MainWindow", "نوعة:"))
        self.label_21.setText(_translate("MainWindow", "السعر:"))
        self.label_29.setText(_translate("MainWindow", "تاريخ الانتهاء:"))
        self.label_28.setText(_translate("MainWindow", "تاريخ الانتاج:"))
        self.pagenterdatabutaddsanf.setText(_translate("MainWindow", "اضافة الصنف"))
        self.label_23.setText(_translate("MainWindow", "اضافة مستوردات:-"))
        self.pagenterdatacomqmemstord.setItemText(0, _translate("MainWindow", "1"))
        self.pagenterdatacomqmemstord.setItemText(1, _translate("MainWindow", "2"))
        self.pagenterdatacomqmemstord.setItemText(2, _translate("MainWindow", "3"))
        self.pagenterdatacomqmemstord.setItemText(3, _translate("MainWindow", "4"))
        self.label_25.setText(_translate("MainWindow", "الكمية:"))
        self.label_32.setText(_translate("MainWindow", "اسم الصنف المستورد:"))
        self.label_24.setText(_translate("MainWindow", "مصدر التوريد:"))
        self.label_27.setText(_translate("MainWindow", "السعر:"))
        self.label_26.setText(_translate("MainWindow", "التاريخ:"))
        self.label_31.setText(_translate("MainWindow", "تاريخ الانتهاء:"))
        self.label_30.setText(_translate("MainWindow", "تاريخ الانتاج:"))
        self.pagenterdatabutaddmstord.setText(_translate("MainWindow", "اضافة المستورد"))
        self.groupBox.setTitle(_translate("MainWindow", "الاستعلام"))
        self.label_33.setText(_translate("MainWindow", "استعلام عن اي صنف:"))
        self.label_34.setText(_translate("MainWindow", "ادخل الباركود:"))
        self.label_35.setText(_translate("MainWindow", "ادخال يدوي:"))
        
        self.groupBox_2.setTitle(_translate("MainWindow", "التعديلات"))
        self.pagstalmbutqmetremain.setText(_translate("MainWindow", "مصروف اليوم"))
        #self.pagstalmbutmodesadrat.setText(_translate("MainWindow", "تعديل في الصادرات"))
        #self.pagstalmbutmodemstordat.setText(_translate("MainWindow", "تعديل في المستوردات"))
        self.pagstalmbutmodesenf.setText(_translate("MainWindow", "تعديل اي صنف "))
        self.butmainpage.setText(_translate("MainWindow", "الصفحة الرئيسية"))
        self.butastalam.setText(_translate("MainWindow", "استعلام"))
        self.butreport.setText(_translate("MainWindow", "التقارير"))
        self.butenterdata.setText(_translate("MainWindow", "ادخال البيانات"))
        self.butout.setText(_translate("MainWindow", "خروج"))
        self.menuFile.setTitle(_translate("MainWindow", "مساعدة"))
        #self.actionAbout.setText(_translate("MainWindow", "حول البرنامج"))
        self.actionGo.setText(_translate("MainWindow", "حول البرنامج"))
        self.actionExit.setText(_translate("MainWindow", "خروج"))
class NotePad(QtWidgets.QMainWindow):
	def __init__(self, parent=None):
		QtWidgets.QWidget.__init__(self, parent)#lambda:تضعها عند اسم الزر
		self.ui = Ui_MainWindow() 
		self.ui.setupUi(self)
		today = str(date.today())
		self.ui.pagstalmbutmodesenf.clicked.connect(self.modsnf)
		self.ui.pagstalmbutqmetremain.clicked.connect(self.determony)
		self.ui.pagenterdatabutaddmstord.clicked.connect(self.addmstord)
		self.ui.pagenterdataentdatemstord.setText(today)
		self.ui.pagenterdataentdateoutsanf.setText(today)
		self.ui.pagenterdataentdateoutmstord.setText(today)
		self.ui.pagenterdataentdateproductsanf.setText(today)
		self.ui.pagenterdataentdateprodectmstord.setText(today)
		self.ui.butmainpage.clicked.connect(self.ss1)
		self.ui.butenterdata.clicked.connect(self.ss2)
		self.ui.butreport.clicked.connect(self.ss3)
		self.ui.butastalam.clicked.connect(self.ss4)
		self.ui.butout.clicked.connect(self.out1)
		self.ui.pagenterdatabutaddsanf.clicked.connect(self.addsinf)
		#self.ui.pagenterdatabutaddmstord.clicked.connect(self.addmstord)
		self.ui.pagmtab1entbarkod.textChanged.connect(self.stalmcod1)
		self.ui.pagmtab1comqmi.currentIndexChanged.connect(self.modamount)
		self.ui.pagmtab1butdelet.clicked.connect(self.deletbuffr1)
		self.ui.pagmtab2comnamesnf.currentIndexChanged.connect(self.showprqm)
		self.ui.pagmtab2comqmi.currentIndexChanged.connect(self.chngqmi2)
		self.ui.pagmtab2butdelet.clicked.connect(self.deletbuffr2)
		self.ui.pagmtab2butprint.clicked.connect(self.dellof)
		self.ui.pagmtab1butprint.clicked.connect(self.printer1)
		self.ui.pagreportcomaboutreport.activated.connect(self.chosreport)
		self.ui.pagreportcomtypereport.activated.connect(self.chosreport)
		self.ui.pagreportcomtypereport.activated.connect(self.reportsenf)
		self.ui.pagreportcomtypereport.activated.connect(self.reportordat)
		self.ui.pagreportcomtypereport.activated.connect(self.reportsadrat)
		self.ui.pagreportcomtypereport.activated.connect(self.reportamounremain)
		self.ui.pagreportbutprintreport.clicked.connect(self.printreport)
		self.ui.pagreportcomoncdetermain.activated.connect(self.showsnf)
		self.ui.pagreportcomononc.activated.connect(self.showinto)
		self.ui.pagreportcomfromonc_2.activated.connect(self.showinto)
		self.ui.pagstalmentbarcod.textChanged.connect(self.showsnfintable1)
		self.ui.comboBox_10.activated.connect(self.showsnfintable2)

		self.ui.actionExit.triggered.connect(self.out1)
		self.ui.actionGo.triggered.connect(self.instr)
		self.insertcomsnf()
		self.addsnf()
		self.chosreport()
########################################################################################		
	def ss1(self):#the page main                                                        #
		#self.ui.stackedWidget.addWidget(self.ui.page)									#
		#self.ui.page.setCurrentIndex(1)												#	
		self.ui.stackedWidget.setCurrentIndex(0)#u'ركز يبدا من الصفر وليس الواحد' 		#
		
	def ss2(self):
		#self.ui.stackedWidget.addWidget(self.ui.pageenterdata)							#
		#self.ui.pageenterdata.setCurrentIndex(2)										#	
		self.ui.stackedWidget.setCurrentIndex(2)										#
																						#			
	def ss3(self):
		#self.ui.stackedWidget.addWidget(self.ui.pagereport)							#		
		#self.ui.pagereport.setCurrentIndex(3)											#
		self.ui.stackedWidget.setCurrentIndex(1)#u'ركز يبدا من الصفر وليس الواحد'		#
																						#			
	def ss4(self):																		#			
		#self.ui.stackedWidget.addWidget(self.ui.pageastalmat)							#
		#self.ui.pageastalmat.setCurrentIndex(4)										#
		self.ui.stackedWidget.setCurrentIndex(3)										#
	def out1(self):
		exit()
	def instr(self):
		message=QtWidgets.QMessageBox.information(self,'حول البرنامج','<FONT size=5 color=black>Copyright (C) 2020,By The programmer Salem khamis Bahien.</FONT><p>A programming using a library PyQt5.</p><p>Email:99zzz52@gmail.com</p><p>Telephon:713151679</p>')

																					#	
#	#	#	#	#	#	#	#	#	#	#	#	#	#	#	#	#	#	#	#	#	#	#

##################page enter data################################################################
#################################################################################################
	def addsinf(self):
		today = str(date.today())
		nammsnf=str(self.ui.pagenterdataentnamesenf.text())
		barcodsnf=str(self.ui.pagenterdataentbarcod.text())
		amountsnf=str(self.ui.pagenterdatacomqmesenf.currentText())
		pricsinf=str(self.ui.pagenterdataentpricsanf.text())
		typesenf=str(self.ui.pagenterdatacomtypesnf.currentText())
		dateprosnf=str(self.ui.pagenterdataentdateproductsanf.text())
		dateoutsnf=str(self.ui.pagenterdataentdateoutsanf.text())
		db1=sqlite3.connect('programcompution.db')
		db1.row_factory=sqlite3.Row
		db1.execute('create table if not exists tableaddsinf(ID integer primary Key autoincrement,datanamesnf text,datadatesnf text,databarcodsnf text,dataamountsnf text,datapricsnf text,datatypesnf text,datadateprodsnf text,datadateoutsnf text)')
		db1.execute('''insert into tableaddsinf(datanamesnf,datadatesnf,databarcodsnf,dataamountsnf,datapricsnf,datatypesnf,datadateprodsnf,datadateoutsnf) values(?,?,?,?,?,?,?,?)''',(nammsnf,today,barcodsnf,amountsnf,pricsinf,typesenf,dateprosnf,dateoutsnf))
		db1.commit()
		message=QtWidgets.QMessageBox.information(self,'information','<FONT size=10 color=blue>Add Successfully</FONT>')
	def addmstord(self):
		sourstored=str(self.ui.pagenterdataentmsdertored.text())
		namemstord=str(self.ui.pagenterdataentnamemstord.text())
		amountmstord=str(self.ui.pagenterdatacomqmemstord.currentText())
		datamstord=str(self.ui.pagenterdataentdatemstord.text())
		pricmstord=	str(self.ui.pagenterdataentpricmstord.text())
		datapromstord=str(self.ui.pagenterdataentdateprodectmstord.text())
		dataoutmstord=str(self.ui.pagenterdataentdateoutmstord.text())
		db1=sqlite3.connect('programcompution.db')
		db1.row_factory=sqlite3.Row
		db1.execute('create table if not exists tableaddmstord(ID integer primary Key autoincrement,sourcmstord text,nammstord text,amunmstord text,datemstord text,prismtord text,datepromstord text,dateoutmstord text)')
		db1.execute('''insert into tableaddmstord(sourcmstord,nammstord,amunmstord,datemstord,prismtord,datepromstord,dateoutmstord) values(?,?,?,?,?,?,?)''',(sourstored,namemstord,amountmstord,datamstord,pricmstord,datapromstord,dataoutmstord))
		db1.commit()
		message=QtWidgets.QMessageBox.information(self,'information','<FONT size=10 color=blue>Add Successfully</FONT>')

######################################page maintab1###################################################################
######################################################################################################################

	def stalmcod1(self):
		#try:	#stonamesnf
			
			tt=[]
			ft=sqlite3.connect('storgtsder.db')
			ft.row_factory=sqlite3.Row
			ft.execute('create table if not exists storgbuffer3(ID integer primary Key autoincrement,ftora text)')
			ft.commit()
			gb=ft.execute("select * from storgbuffer3")
			for t in gb:
				tt.append(t)
			kk=len(tt)
			if kk==0:
				ft.execute('insert into storgbuffer3(ftora) values(?)',("0"))
				ft.commit()
			ft1=ft.execute("select * from storgbuffer3")	
			for y in ft1:
				ftttora=str(y["ftora"])
				
			x=datetime.datetime.now().hour
			s=datetime.datetime.now().minute
			a=datetime.datetime.now().second
			time1=str(str(x)+":"+str(s)+":"+str(a))
			today = str(date.today())
			e=0
			codstalm1=str(self.ui.pagmtab1entbarkod.text())
			db1=sqlite3.connect('programcompution.db')
			db1.row_factory=sqlite3.Row
			tab1=db1.execute("select * from tableaddsinf where databarcodsnf='{}'".format(codstalm1))

			for h in tab1:
				e=1
				stonamesnf=h["datanamesnf"]
				stopricsnf=h["datapricsnf"]
				stocodsnf=h["databarcodsnf"]
				self.ui.pagmtab1entprc.setText(h["datapricsnf"])
				f=int(self.ui.pagmtab1entprc.text())
				c=int(self.ui.pagmtab1comqmi.currentText())
				g=f*c
				self.ui.pagmtab1entprc.setText(str(g))
				gp=str(self.ui.pagmtab1entprc.text())
				qm=str(self.ui.pagmtab1comqmi.currentText())
			if e==1:
				rr=[]
				barcod=str(self.ui.pagmtab1entbarkod.text())
				stoamounsnf=str(self.ui.pagmtab1comqmi.currentText())
				db2=sqlite3.connect('storgtsder.db')
				db2.row_factory=sqlite3.Row
				db2.execute('create table if not exists storgbuffer1(ID integer primary Key autoincrement,stobufnamesnf text,stobufbarcodsnf text,stobufpricsnf text,stobufamountsnf text,stobufdatesnf text,stobuftimesnf)')
				db2.commit()
				ggg=db2.execute("select stobufbarcodsnf from storgbuffer1 where stobufbarcodsnf='{}'".format(barcod))
				for x in ggg:
					rr.append(x)
				fff=len(rr)	
				if fff != 0:
					#db2.execute('''insert into storgbuffer1(stobufnamesnf,stobufbarcodsnf,stobufpricsnf,stobufamountsnf,stobufdatesnf,stobuftimesnf) values(?,?,?,?,?,?)''',(stonamesnf,stocodsnf,gp,qm,today,time1))
					#db2.commit()

					dff=db2.execute("select * from storgbuffer1")#bgcolor='green'
					self.ui.pagmtab1text.clear()
					self.ui.pagmtab1text.append("<p align='left'>رقم الفاتورة: <font color=red>{}</font></p>".format(ftttora))
					self.ui.pagmtab1text.append("<p align='left'>التاريخ: {}</p>".format(today))
					self.ui.pagmtab1text.append("<p><table width='100%' border='1' cellpadding'5' ><caption><b><u><center>فاتورة المشتريات</center></u></b></caption><tr><td width=20%><u><center>اسم البضاعة</center></u></td><td width=20%><u><center>السعر</u></center></td><td width=20%><u><center>الكمية</u></center></td><td width=20%><u><center>التاريخ</u></center></td><td width=20%><u><center>الوقت</u></center></td></tr>")
					for n in dff:
						pric1=str(self.ui.pagmtab1entprc.text())
						amount1=str(self.ui.pagmtab1comqmi.currentText())
						yy=str(self.ui.pagmtab1text.toPlainText())
						#self.ui.pagmtab1text.clear()
						#if yy =="":

							#self.ui.pagmtab1text.append("<p><table width='100%' border='5' cellpadding'5' bgcolor='green'><caption><b><u><center>فاتورة المشتريات</center></u></b></caption><tr><td><u><center>اسم البضاعة</center></u></td><td><u><center>السعر</u></center></td><td><u><center>الكمية</u></center></td><td><u><center>التاريخ</u></center></td><td><u><center>الوقت</u></center></td></tr>")
							#self.ui.pagmtab1text.append("<p><table width='100%' border='5' cellpadding'5' bgcolor='green'><tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr></table></p>".format(n["stobufnamesnf"],n["stobufpricsnf"],n["stobufamountsnf"],n["stobufdatesnf"],n["stobuftimesnf"]))
						#else:
							
						self.ui.pagmtab1text.append("<p><table width='100%' border='1' cellpadding'5' ><tr><td width=20%><center>{}</td><td width=20%><center>{}</td><td width=20%><center>{}</td><td width=20%><center>{}</td><td width=20%><center>{}</td></tr></table></p>".format(n["stobufnamesnf"],n["stobufpricsnf"],n["stobufamountsnf"],n["stobufdatesnf"],n["stobuftimesnf"]))
					sum1=db2.execute("select sum(stobufpricsnf) from storgbuffer1")
					for d in sum1:
						self.ui.pagmtab1text.append("<p><table width='100%' border='1' cellpadding'5' ><tr><td width=50%><center>{}</td><td width=50%><center>الاجمالي</td></tr></table></p>".format(d[0]))
				
				else:
					db2.execute('''insert into storgbuffer1(stobufnamesnf,stobufbarcodsnf,stobufpricsnf,stobufamountsnf,stobufdatesnf,stobuftimesnf) values(?,?,?,?,?,?)''',(stonamesnf,stocodsnf,gp,qm,today,time1))
					db2.commit()
					dff=db2.execute("select * from storgbuffer1")
					self.ui.pagmtab1text.clear()
					self.ui.pagmtab1text.append("<p align='left'>رقم الفاتورة: <font color=red>{}</font></p>".format(ftttora))
					self.ui.pagmtab1text.append("<p align='left'>التاريخ: {}</p>".format(today))
					self.ui.pagmtab1text.append("<p><table width='100%' border='1' cellpadding'5' ><caption><b><u><center>فاتورة المشتريات</center></u></b></caption><tr><td width=20%><u><center>اسم البضاعة</center></u></td><td width=20%><u><center>السعر</u></center></td><td width=20%><u><center>الكمية</u></center></td><td width=20%><u><center>التاريخ</u></center></td><td width=20%><u><center>الوقت</u></center></td></tr>")
					for n in dff:
						pric1=str(self.ui.pagmtab1entprc.text())
						amount1=str(self.ui.pagmtab1comqmi.currentText())
						yy=str(self.ui.pagmtab1text.toPlainText())
						#self.ui.pagmtab1text.clear()
						#if yy =="":

							#self.ui.pagmtab1text.append("<p><table width='100%' border='5' cellpadding'5' bgcolor='green'><caption><b><u><center>فاتورة المشتريات</center></u></b></caption><tr><td><u><center>اسم البضاعة</center></u></td><td><u><center>السعر</u></center></td><td><u><center>الكمية</u></center></td><td><u><center>التاريخ</u></center></td><td><u><center>الوقت</u></center></td></tr>")
							#self.ui.pagmtab1text.append("<p><table width='100%' border='5' cellpadding'5' bgcolor='green'><tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr></table></p>".format(n["stobufnamesnf"],n["stobufpricsnf"],n["stobufamountsnf"],n["stobufdatesnf"],n["stobuftimesnf"]))
						#else:
							
						self.ui.pagmtab1text.append("<p><table width='100%' border='1' cellpadding'5' ><tr><td width=20%><center>{}</td><td width=20%><center>{}</td><td width=20%><center>{}</td><td width=20%><center>{}</td><td width=20%><center>{}</td></tr></table></p>".format(n["stobufnamesnf"],n["stobufpricsnf"],n["stobufamountsnf"],n["stobufdatesnf"],n["stobuftimesnf"]))
					sum1=db2.execute("select sum(stobufpricsnf) from storgbuffer1")
					for d in sum1:
						self.ui.pagmtab1text.append("<p><table width='100%' border='1' cellpadding'5' ><tr><td width=50%><center>{}</td><td width=50%><center>الاجمالي</center></td></tr></table></p>".format(d[0]))
				

		#except:
			#QtWidgets.QMessageBox.information(self,'information','<FONT size=10 color=blue>لا تعصد</FONT>')

	def modamount(self):
		try:
			x=datetime.datetime.now().hour
			s=datetime.datetime.now().minute
			a=datetime.datetime.now().second
			time1=str(str(x)+":"+str(s)+":"+str(a))
			today = str(date.today())
			
			i=0
			codstalm1=str(self.ui.pagmtab1entbarkod.text())
			if self.ui.pagmtab1entprc.text() !="":
				db1=sqlite3.connect('programcompution.db')
				db1.row_factory=sqlite3.Row
				tab1=db1.execute("select * from tableaddsinf where databarcodsnf='{}'".format(codstalm1))
				for h in tab1:
					f=int(h["datapricsnf"])
					c=int(self.ui.pagmtab1comqmi.currentText())	
					g=f*c
					self.ui.pagmtab1entprc.setText(str(g))
				pric=str(self.ui.pagmtab1entprc.text())
				amount=str(self.ui.pagmtab1comqmi.currentText())	
				db2=sqlite3.connect('storgtsder.db')
				db2.row_factory=sqlite3.Row
				tab2=db2.execute("select * from storgbuffer1 where stobufbarcodsnf='{}'".format(codstalm1))
				for l in tab2:
					i=1
					stonamesnf=str(l["stobufnamesnf"])
				if i==1:
					db3=sqlite3.connect('storgtsder.db')
					db3.row_factory=sqlite3.Row
					db3.execute("delete from storgbuffer1 where stobufbarcodsnf='{}'".format(codstalm1))
					db3.commit()
					db3.execute('''insert into storgbuffer1(stobufnamesnf,stobufbarcodsnf,stobufpricsnf,stobufamountsnf,stobufdatesnf,stobuftimesnf) values(?,?,?,?,?,?)''',(stonamesnf,codstalm1,pric,amount,today,time1))
					db3.commit()
					tab3=db3.execute("select * from storgbuffer1 where stobufbarcodsnf='{}'".format(codstalm1))
					for j in tab3:
						self.ui.pagmtab1entbarkod.clear()
						self.ui.pagmtab1entbarkod.setText(j["stobufbarcodsnf"])
		except:
			QtWidgets.QMessageBox.information(self,'information','<FONT size=10 color=blue>لا تعصد</FONT>')				

	def deletbuffr1(self):
			db2=sqlite3.connect('storgtsder.db')
			db2.row_factory=sqlite3.Row
			db2.execute('create table if not exists storgbuffer2(ID integer primary Key autoincrement,stobufnamesnf text,stobufbarcodsnf text,stobufpricsnf text,stobufamountsnf text,stobufdatesnf text,stobuftimesnf text)')
			db2.commit()
			tab3=db2.execute("select * from storgbuffer1")
			for h in tab3:
				db2.execute('''insert into storgbuffer2(stobufnamesnf,stobufbarcodsnf,stobufpricsnf,stobufamountsnf,stobufdatesnf,stobuftimesnf) values(?,?,?,?,?,?)''',(h["stobufnamesnf"],h["stobufbarcodsnf"],h["stobufpricsnf"],h["stobufamountsnf"],h["stobufdatesnf"],h["stobuftimesnf"]))	
			
			db2.commit()	
			#db2.execute('''delete from storgbuffer1''')
			#db2.execute("insert into storgbuffer1(stobufnamesnf,stobufbarcodsnf,stobufpricsnf,stobufamountsnf,stobufdatesnf,stobuftimesnf)values(?,?,?,?,?,?)",("اسم الصنف","رقم الباركود","السعر","الكمية","التاريخ","الوقت"))
			#db2.commit()
			fb1=db2.execute("select * from storgbuffer3")
			for k in fb1:
				num=int(k["ftora"])
			num+=1	
			db2.execute("update storgbuffer3 set ftora='{}'".format(str(num)))	
			db2.commit()
			bfr1=db2.execute("select * from storgbuffer1")
		
			for n in bfr1:
				db1=sqlite3.connect('programcompution.db')
				db1.row_factory=sqlite3.Row
				bfr2=db1.execute("select * from tableaddsinf where databarcodsnf='{}'".format(n["stobufbarcodsnf"]))
				for x in bfr2:
					d=int(x["dataamountsnf"])-int(n["stobufamountsnf"])
					
					db1.execute("update tableaddsinf set dataamountsnf='{}' where databarcodsnf='{}'".format(str(d),x["databarcodsnf"]))
					db1.commit()
			db2.execute('''delete from storgbuffer1''')
			db2.commit()
	def printer1(self):
		if self.ui.pagmtab1text.toPlainText() !="":
			printer =QtPrintSupport.QPrintDialog()
			#printer.setFullPage(True)
			#dialog = QtGui.QPrintDialog(printer)
			if printer.exec_() == QtWidgets.QDialog.Accepted:
				self.ui.pagmtab1text.document().print_(printer.printer())
				printer.exec_()		
########################################################tab2#####################################################################
#################################################################################################################################

	def insertcomsnf(self):
		db1=sqlite3.connect('programcompution.db')
		db1.row_factory=sqlite3.Row
		gl=db1.execute("select * from tableaddsinf")
		hh=self.ui.pagmtab2comnamesnf.currentText()
		self.ui.pagmtab2comnamesnf.addItem("ننن")
		for n in gl:
			self.ui.pagmtab2comnamesnf.addItem("{}".format(n["datanamesnf"]))
	def showprqm(self):
		tt=[]
		ft=sqlite3.connect('storgtsder.db')
		ft.row_factory=sqlite3.Row
		ft.execute('create table if not exists storgbuffer3(ID integer primary Key autoincrement,ftora text)')
		ft.commit()
		gb=ft.execute("select * from storgbuffer3")
		for t in gb:
			tt.append(t)
		kk=len(tt)
		if kk==0:
			ft.execute('insert into storgbuffer3(ftora) values(?)',("0"))
			ft.commit()
		ft1=ft.execute("select * from storgbuffer3")	
		for y in ft1:
			ftttora=str(y["ftora"])


		rr=[]
		x=datetime.datetime.now().hour
		s=datetime.datetime.now().minute
		a=datetime.datetime.now().second
		time1=str(str(x)+":"+str(s)+":"+str(a))
		today = str(date.today())
		r=0
		namesnftb2=str(self.ui.pagmtab2comnamesnf.currentText())
		db1=sqlite3.connect('programcompution.db')
		db1.row_factory=sqlite3.Row
		gl=db1.execute("select * from tableaddsinf where datanamesnf='{}'".format(namesnftb2))
		for n in gl:#entpric intab2 is but
			r=1
			self.ui.pagmtab2butpric.setText(n["datapricsnf"])
			f=int(self.ui.pagmtab2butpric.text())
			c=int(self.ui.pagmtab2comqmi.currentText())
			g=f*c
			self.ui.pagmtab2butpric.setText(str(g))
		if r==1:
			db2=sqlite3.connect('storgtsder.db')
			db2.row_factory=sqlite3.Row
			db2.execute('create table if not exists storgbuffer1(ID integer primary Key autoincrement,stobufnamesnf text,stobufbarcodsnf text,stobufpricsnf text,stobufamountsnf text,stobufdatesnf text,stobuftimesnf text)')
			db2.commit()
			ggg=db2.execute("select stobufnamesnf from storgbuffer1 where stobufnamesnf='{}'".format(namesnftb2))
			for x in ggg:
					rr.append(x)
			fff=len(rr)	
			if fff != 0:
				#db2.execute('''insert into storgbuffer1(stobufnamesnf,stobufbarcodsnf,stobufpricsnf,stobufamountsnf,stobufdatesnf,stobuftimesnf) values(?,?,?,?,?,?)''',(stonamesnf,stocodsnf,gp,qm,today,time1))
				#db2.commit()
				dff=db2.execute("select * from storgbuffer1")#bgcolor='green'
				self.ui.pagmtab2text.clear()
				self.ui.pagmtab2text.append("<p align='left'>رقم الفاتورة: <font color=red>{}</font></p>".format(ftttora))
				self.ui.pagmtab2text.append("<p align='left'>التاريخ: {}</p>".format(today))
				self.ui.pagmtab2text.append("<p><table width='100%' border='1' cellpadding'5' ><caption><b><u><center>فاتورة المشتريات</center></u></b></caption><tr><td width=20%><u><center>اسم البضاعة</center></u></td><td width=20%><u><center>السعر</u></center></td><td width=20%><u><center>الكمية</u></center></td><td width=20%><u><center>التاريخ</u></center></td><td width=20%><u><center>الوقت</u></center></td></tr>")
				for n in dff:
					pric1=str(self.ui.pagmtab2butpric.text())
					amount1=str(self.ui.pagmtab2comqmi.currentText())
					yy=str(self.ui.pagmtab1text.toPlainText())

						#self.ui.pagmtab1text.clear()
						#if yy =="":

							#self.ui.pagmtab1text.append("<p><table width='100%' border='5' cellpadding'5' bgcolor='green'><caption><b><u><center>فاتورة المشتريات</center></u></b></caption><tr><td><u><center>اسم البضاعة</center></u></td><td><u><center>السعر</u></center></td><td><u><center>الكمية</u></center></td><td><u><center>التاريخ</u></center></td><td><u><center>الوقت</u></center></td></tr>")
							#self.ui.pagmtab1text.append("<p><table width='100%' border='5' cellpadding'5' bgcolor='green'><tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr></table></p>".format(n["stobufnamesnf"],n["stobufpricsnf"],n["stobufamountsnf"],n["stobufdatesnf"],n["stobuftimesnf"]))
						#else:
							
					self.ui.pagmtab2text.append("<p><table width='100%' border='1' cellpadding'5' ><tr><td width=20%><center>{}</td><td width=20%><center>{}</td><td width=20%><center>{}</td><td width=20%><center>{}</td><td width=20%><center>{}</td></tr></table></p>".format(n["stobufnamesnf"],n["stobufpricsnf"],n["stobufamountsnf"],n["stobufdatesnf"],n["stobuftimesnf"]))
				sum1=db2.execute("select sum(stobufpricsnf) from storgbuffer1")
				for d in sum1:
					self.ui.pagmtab2text.append("<p><table width='100%' border='1' cellpadding'5' ><tr><td width=50%><center>{}</td><td width=50%><center>الاجمالي</td></tr></table></p>".format(d[0]))
				

			else:
				pric1=str(self.ui.pagmtab2butpric.text())
				amount1=str(self.ui.pagmtab2comqmi.currentText())
				db1=sqlite3.connect('programcompution.db')
				db1.row_factory=sqlite3.Row
				gl=db1.execute("select * from tableaddsinf where datanamesnf='{}'".format(namesnftb2))
				for j in gl:
					d=str(j["databarcodsnf"])
					
				db2.execute('''insert into storgbuffer1(stobufnamesnf,stobufbarcodsnf,stobufpricsnf,stobufamountsnf,stobufdatesnf,stobuftimesnf) values(?,?,?,?,?,?)''',(namesnftb2,d,pric1,amount1,today,time1))
				db2.commit()
				dff=db2.execute("select * from storgbuffer1")
				self.ui.pagmtab2text.clear()
				self.ui.pagmtab2text.append("<p align='left'>رقم الفاتورة: <font color=red>{}</font></p>".format(ftttora))
				self.ui.pagmtab2text.append("<p align='left'>التاريخ: {}</p>".format(today))
				self.ui.pagmtab2text.append("<p><table width='100%' border='1' cellpadding'5' ><caption><b><u><center>فاتورة المشتريات</center></u></b></caption><tr><td width=20%><u><center>اسم البضاعة</center></u></td><td width=20%><u><center>السعر</u></center></td><td width=20%><u><center>الكمية</u></center></td><td width=20%><u><center>التاريخ</u></center></td><td width=20%><u><center>الوقت</u></center></td></tr>")
				for n in dff:
					
					self.ui.pagmtab2text.append("<p><table width='100%' border='1' cellpadding'5' ><tr><td width=20%><center>{}</td><td width=20%><center>{}</td><td><center>{}</td><td width=20%><center>{}</td><td width=20%><center>{}</td></tr></table></p>".format(n["stobufnamesnf"],n["stobufpricsnf"],n["stobufamountsnf"],n["stobufdatesnf"],n["stobuftimesnf"]))
				sum1=db2.execute("select sum(stobufpricsnf) from storgbuffer1")
				for d in sum1:
					self.ui.pagmtab2text.append("<p><table width='100%' border='1' cellpadding'5' ><tr><td width=50%><center>{}</td><td width=50%><center>الاجمالي</td></tr></table></p>".format(d[0]))
				

	#except:
		#QtWidgets.QMessageBox.information(self,'information','<FONT size=10 color=blue>لا تعصد</FONT>')	
	def chngqmi2(self):
		x=datetime.datetime.now().hour
		s=datetime.datetime.now().minute
		a=datetime.datetime.now().second
		time1=str(str(x)+":"+str(s)+":"+str(a))
		today = str(date.today())
		namesnftb2=str(self.ui.pagmtab2comnamesnf.currentText())
		i=0
		if self.ui.pagmtab2butpric.text() !="":
			db1=sqlite3.connect('programcompution.db')
			db1.row_factory=sqlite3.Row
			tab1=db1.execute("select * from tableaddsinf where datanamesnf='{}'".format(namesnftb2))
			for h in tab1:
				f=int(h["datapricsnf"])
				c=int(self.ui.pagmtab2comqmi.currentText())
				g=f*c
				self.ui.pagmtab2butpric.setText(str(g))
			pric=str(self.ui.pagmtab2butpric.text())
			amount=str(self.ui.pagmtab2comqmi.currentText())	
			db2=sqlite3.connect('storgtsder.db')
			db2.row_factory=sqlite3.Row
			tab2=db2.execute("select * from storgbuffer1 where stobufnamesnf='{}'".format(namesnftb2))
			for l in tab2:
				i=1
				stonamesnf=str(l["stobufbarcodsnf"])
			if i==1:
				db3=sqlite3.connect('storgtsder.db')
				db3.row_factory=sqlite3.Row
				db3.execute("delete from storgbuffer1 where stobufnamesnf='{}'".format(namesnftb2))
				db3.commit()
				db3.execute('''insert into storgbuffer1(stobufnamesnf,stobufbarcodsnf,stobufpricsnf,stobufamountsnf,stobufdatesnf,stobuftimesnf) values(?,?,?,?,?,?)''',(namesnftb2,stonamesnf,pric,amount,today,time1))
				db3.commit()

				tab3=db3.execute("select * from storgbuffer1 where stobufnamesnf='{}'".format(namesnftb2))
				for j in tab3:
					self.ui.pagmtab2comnamesnf.clear()
					self.ui.pagmtab2comnamesnf.addItem('{}'.format(j[1]))
					self.insertcomsnf()
						
	def deletbuffr2(self):#storg in database devic allowys and compution ftorh
		db2=sqlite3.connect('storgtsder.db')
		db2.row_factory=sqlite3.Row
		db2.execute('create table if not exists storgbuffer2(ID integer primary Key autoincrement,stobufnamesnf text,stobufbarcodsnf text,stobufpricsnf text,stobufamountsnf text,stobufdatesnf text,stobuftimesnf text)')
		db2.commit()

		tab3=db2.execute("select * from storgbuffer1")
		for h in tab3:
			db2.execute('''insert into storgbuffer2(stobufnamesnf,stobufbarcodsnf,stobufpricsnf,stobufamountsnf,stobufdatesnf,stobuftimesnf) values(?,?,?,?,?,?)''',(h["stobufnamesnf"],h["stobufbarcodsnf"],h["stobufpricsnf"],h["stobufamountsnf"],h["stobufdatesnf"],h["stobuftimesnf"]))	
		db2.commit()	
		# db2.execute('''delete from storgbuffer1''')
		# db2.commit()
		fb1=db2.execute("select * from storgbuffer3")
		for k in fb1:
			num=int(k["ftora"])
		num+=1	
		db2.execute("update storgbuffer3 set ftora='{}'".format(str(num)))	
		db2.commit()
		bfr1=db2.execute("select * from storgbuffer1")
		
		for n in bfr1:
			db1=sqlite3.connect('programcompution.db')
			db1.row_factory=sqlite3.Row
			bfr2=db1.execute("select * from tableaddsinf where databarcodsnf='{}'".format(n["stobufbarcodsnf"]))
			for x in bfr2:
				d=int(x["dataamountsnf"])-int(n["stobufamountsnf"])
				
				db1.execute("update tableaddsinf set dataamountsnf='{}' where databarcodsnf='{}'".format(str(d),x["databarcodsnf"]))
				db1.commit()
		db2.execute('''delete from storgbuffer1''')
		db2.commit()		
	def dellof(self):#printer##################################printer##################################################
		# db2=sqlite3.connect('storgtsder.db')
		# db2.row_factory=sqlite3.Row	
		# db2.execute('''delete from storgbuffer2 ''')
		# db2.commit()
		if self.ui.pagmtab2text.toPlainText() !="":
			printer =QtPrintSupport.QPrintDialog()
			#printer.setFullPage(True)
			#dialog = QtGui.QPrintDialog(printer)
			if printer.exec_() == QtWidgets.QDialog.Accepted:
				self.ui.pagmtab2text.document().print_(printer.printer())
				printer.exec_()	
###############################################page report#####################################################################
################################################################################################################################
	def chosreport(self):
		chreport=str(self.ui.pagreportcomaboutreport.currentText())
		if chreport =="الاصناف":
			self.reportsenf()
		if chreport =="الواردات":
			self.reportordat()
		if chreport =="الصادرات":
			self.reportsadrat()
		if chreport =="الكميات المتبقية من الاصناف":
			self.reportamounremain()

	def reportsenf(self):
		typtgrer=str(self.ui.pagreportcomtypereport.currentText())
		if typtgrer =="عام":
			self.amsnf()
		if typtgrer =="من فترة محددة":
			self.detrmainsnf()
		if typtgrer =="من فترة الى فترة معينة":
			self.intosnf()
#funciton is reportsenf olny##################################################################################3			
	def amsnf(self):
		chreport=str(self.ui.pagreportcomaboutreport.currentText())
		if chreport == "الاصناف":
			db1=sqlite3.connect('programcompution.db')
			db1.row_factory=sqlite3.Row
			snf=db1.execute("select * from tableaddsinf")
			self.ui.textEdit_3.clear()
			self.ui.textEdit_3.append("<p><table width='100%' border='1' cellpadding'5' ><caption><b><u><center>تقرير عن الكميات المتبقية</center></u></b></caption><tr><td width=12.5%><u><center>اسم الصنف</center></u></td><td width=12.5%><u><center>تاريخ الادخال</u></center></td><td width=12.5%><u><center>رقم الباركود</u></center></td><td width=12.5%><u><center>الكمية</u></center></td><td width=12.5%><u><center>السعر</u></center></td><td width=12.5%><u><center>نوع</center></u></td><td width=12.5%><u><center>تاريخ الانتاج</center></u></td><td width=12.5%><u><center>تاريخ الانتهاء</center></u></td></tr></table></p>")
			for g in snf:
				self.ui.textEdit_3.append("<p><table width='100%' border='1' cellpadding'5' ><tr><td width=12.5%><center>{}</td><td width=12.5%><center>{}</td><td width=12.5%><center>{}</td><td width=12.5%><center>{}</td><td width=12.5%><center>{}</td><td width=12.5%><center>{}</td><td width=12.5%><center>{}</td><td width=12.5%><center>{}</td></tr></table></p>".format(g["datanamesnf"],g["datadatesnf"],g["databarcodsnf"],g["dataamountsnf"],g["datapricsnf"],g["datatypesnf"],g["datadateprodsnf"],g["datadateoutsnf"]))
	def detrmainsnf(self):
		db1=sqlite3.connect('programcompution.db')
		db1.row_factory=sqlite3.Row
		snf=db1.execute("select * from tableaddsinf")
		self.ui.pagreportcomoncdetermain.clear()
		for g in snf:
			self.ui.pagreportcomoncdetermain.addItem('{}'.format(g["datadatesnf"]))
	def showsnf(self):#هذة ممكن تضع بافي الاستعلامات فيها
		chreport=str(self.ui.pagreportcomaboutreport.currentText())
		if chreport == "الاصناف":
			typtgrer=str(self.ui.pagreportcomtypereport.currentText())
			if typtgrer == "من فترة محددة":
				sereh=str(self.ui.pagreportcomoncdetermain.currentText())
				db1=sqlite3.connect('programcompution.db')
				db1.row_factory=sqlite3.Row
				snf=db1.execute("select * from tableaddsinf where  datadatesnf like '%{}%'".format(sereh))
				self.ui.textEdit_3.clear()
				self.ui.textEdit_3.append("<p><table width='100%' border='1' cellpadding'5' ><caption><b><u><center>تقرير عن الكميات المتبقية</center></u></b></caption><tr><td width=12.5%><u><center>اسم الصنف</center></u></td><td width=12.5%><u><center>تاريخ الادخال</u></center></td><td width=12.5%><u><center>رقم الباركود</u></center></td><td width=12.5%><u><center>الكمية</u></center></td><td width=12.5%><u><center>السعر</u></center></td><td width=12.5%><u><center>نوع</center></u></td><td width=12.5%><u><center>تاريخ الانتاج</center></u></td><td width=12.5%><u><center>تاريخ الانتهاء</center></u></td></tr></table></p>")
				for g in snf:
					self.ui.textEdit_3.append("<p><table width='100%' border='1' cellpadding'5' ><tr><td width=12.5%><center>{}</td><td width=12.5%><center>{}</td><td width=12.5%><center>{}</td><td width=12.5%><center>{}</td><td width=12.5%><center>{}</td><td width=12.5%><center>{}</td><td width=12.5%><center>{}</td><td width=12.5%><center>{}</td></tr></table></p>".format(g["datanamesnf"],g["datadatesnf"],g["databarcodsnf"],g["dataamountsnf"],g["datapricsnf"],g["datatypesnf"],g["datadateprodsnf"],g["datadateoutsnf"]))
		if 	chreport == "الواردات":
			typtgrer=str(self.ui.pagreportcomtypereport.currentText())
			if typtgrer == "من فترة محددة":
				sereh1=str(self.ui.pagreportcomoncdetermain.currentText())
				db2=sqlite3.connect('programcompution.db')
				db2.row_factory=sqlite3.Row
				snf1=db2.execute("select * from tableaddmstord where datemstord like '%{}%'".format(sereh1))
				self.ui.textEdit_3.clear()
				self.ui.textEdit_3.append("<p><table width='100%' border='1' cellpadding'5' ><caption><b><u><center>تقرير لفترة محدودة عن الواردات</center></u></b></caption><tr><td width=14.3%><u><center>اسم المصدر</center></u></td><td width=14.3%><u><center>اسم المستورد</u></center></td><td width=14.3%><u><center>الكمية</u></center></td><td width=14.3%><u><center>تاريخ الاستيراد</u></center></td><td width=14.3%><u><center>السعر</u></center></td><td width=14.3%><u><center>تاريخ الانتاج</center></u></td><td width=14.3%><u><center>تاريخ الانتهاء</center></u></td></tr></table></p>")
				for g in snf1:
					self.ui.textEdit_3.append("<p><table width='100%' border='1' cellpadding'5' ><tr><td width=14.3%><center>{}</td><td width=14.3%><center>{}</td><td width=14.3%><center>{}</td><td width=14.3%><center>{}</td><td width=14.3%><center>{}</td><td width=14.3%><center>{}</td><td width=14.3%><center>{}</td></tr></table></p>".format(g["sourcmstord"],g["nammstord"],g["amunmstord"],g["datemstord"],g["prismtord"],g["datepromstord"],g["dateoutmstord"]))
		if chreport =="الصادرات":
			typtgrer=str(self.ui.pagreportcomtypereport.currentText())
			if typtgrer == "من فترة محددة":
				sereh2=str(self.ui.pagreportcomoncdetermain.currentText())
				db1=sqlite3.connect('storgtsder.db')
				db1.row_factory=sqlite3.Row
				snf3=db1.execute("select * from storgbuffer2 where stobufdatesnf like '%{}%'".format(sereh2))
				self.ui.textEdit_3.clear()
				self.ui.textEdit_3.append("<p><table width='100%' border='1' cellpadding'5' ><caption><b><u><center>تقرير في فترة محدودة عن الصادرات</center></u></b></caption><tr><td width=16.7%><u><center>اسم الصنف</center></u></td><td width=16.7%><u><center>رقم الباركود</u></center></td><td width=16.7%><u><center>السعر</u></center></td><td width=16.7%><u><center>الكمية</u></center></td><td width=16.7%><u><center>تاريخ التصدير</u></center></td><td width=16.7%><u><center>وقت التصدير</center></u></td></tr></table></p>")
				for g in snf3:
					self.ui.textEdit_3.append("<p><table width='100%' border='1' cellpadding'5' ><tr><td width=16.7%><center>{}</td><td width=16.7%><center>{}</td><td width=16.7%><center>{}</td><td width=16.7%><center>{}</td><td width=16.7%><center>{}</td><td width=16.7%><center>{}</td></tr></table></p>".format(g["stobufnamesnf"],g["stobufbarcodsnf"],g["stobufpricsnf"],g["stobufamountsnf"],g["stobufdatesnf"],g["stobuftimesnf"]))						
	
	def intosnf(self):
		db1=sqlite3.connect('programcompution.db')
		db1.row_factory=sqlite3.Row
		snf=db1.execute("select * from tableaddsinf")
		self.ui.pagreportcomononc.clear()
		self.ui.pagreportcomfromonc_2.clear()
		for g in snf:
			self.ui.pagreportcomononc.addItem('{}'.format(g["datadatesnf"]))
			self.ui.pagreportcomfromonc_2.addItem('{}'.format(g["datadatesnf"]))
	def showinto(self):#هذة ممكن تضع بافي الاستعلامات فيها
		chreport=str(self.ui.pagreportcomaboutreport.currentText())
		if chreport == "الاصناف":#الاصناف
			typtgrer=str(self.ui.pagreportcomtypereport.currentText())
			if typtgrer == "من فترة الى فترة معينة":
				s1=str(self.ui.pagreportcomononc.currentText())
				s2=str(self.ui.pagreportcomfromonc_2.currentText())
				db1=sqlite3.connect('programcompution.db')
				db1.row_factory=sqlite3.Row
				snf=db1.execute("select * from tableaddsinf where datadatesnf between '{}' and '{}'".format(s2,s1))
				self.ui.textEdit_3.clear()
				self.ui.textEdit_3.append("<p><table width='100%' border='1' cellpadding'5' ><caption><b><u><center>تقرير عن الكميات المتبقية</center></u></b></caption><tr><td width=12.5%><u><center>اسم الصنف</center></u></td><td width=12.5%><u><center>تاريخ الادخال</u></center></td><td width=12.5%><u><center>رقم الباركود</u></center></td><td width=12.5%><u><center>الكمية</u></center></td><td width=12.5%><u><center>السعر</u></center></td><td width=12.5%><u><center>نوع</center></u></td><td width=12.5%><u><center>تاريخ الانتاج</center></u></td><td width=12.5%><u><center>تاريخ الانتهاء</center></u></td></tr></table></p>")
				for g in snf:
					self.ui.textEdit_3.append("<p><table width='100%' border='1' cellpadding'5' ><tr><td width=12.5%><center>{}</td><td width=12.5%><center>{}</td><td width=12.5%><center>{}</td><td width=12.5%><center>{}</td><td width=12.5%><center>{}</td><td width=12.5%><center>{}</td><td width=12.5%><center>{}</td><td width=12.5%><center>{}</td></tr></table></p>".format(g["datanamesnf"],g["datadatesnf"],g["databarcodsnf"],g["dataamountsnf"],g["datapricsnf"],g["datatypesnf"],g["datadateprodsnf"],g["datadateoutsnf"]))
		chreport=str(self.ui.pagreportcomaboutreport.currentText())
		if chreport == "الواردات":#الواردات
			typtgrer=str(self.ui.pagreportcomtypereport.currentText())
			if typtgrer == "من فترة الى فترة معينة":		
				s11=str(self.ui.pagreportcomononc.currentText())
				s22=str(self.ui.pagreportcomfromonc_2.currentText())
				db2=sqlite3.connect('programcompution.db')
				db2.row_factory=sqlite3.Row
				snf1=db2.execute("select * from tableaddmstord where datemstord between '{}' and '{}'".format(s22,s11))
				self.ui.textEdit_3.clear()
				self.ui.textEdit_3.append("<p><table width='100%' border='1' cellpadding'5' ><caption><b><u><center>تقرير من فترة الى فترة معينة عن الواردات</center></u></b></caption><tr><td width=14.3%><u><center>اسم المصدر</center></u></td><td width=14.3%><u><center>اسم المستورد</u></center></td><td width=14.3%><u><center>الكمية</u></center></td><td width=14.3%><u><center>تاريخ الاستيراد</u></center></td><td width=14.3%><u><center>السعر</u></center></td><td width=14.3%><u><center>تاريخ الانتاج</center></u></td><td width=14.3%><u><center>تاريخ الانتهاء</center></u></td></tr></table></p>")
				for g in snf1:
					self.ui.textEdit_3.append("<p><table width='100%' border='1' cellpadding'5' ><tr><td width=14.3%><center>{}</td><td width=14.3%><center>{}</td><td width=14.3%><center>{}</td><td width=14.3%><center>{}</td><td width=14.3%><center>{}</td><td width=14.3%><center>{}</td><td width=14.3%><center>{}</td></tr></table></p>".format(g["sourcmstord"],g["nammstord"],g["amunmstord"],g["datemstord"],g["prismtord"],g["datepromstord"],g["dateoutmstord"]))
		if chreport =="الصادرات":#الصادرات
			typtgrer=str(self.ui.pagreportcomtypereport.currentText())
			if typtgrer == "من فترة الى فترة معينة":
				s111=str(self.ui.pagreportcomononc.currentText())
				s222=str(self.ui.pagreportcomfromonc_2.currentText())
				db3=sqlite3.connect('storgtsder.db')
				db3.row_factory=sqlite3.Row
				snf2=db3.execute("select * from storgbuffer2 where stobufdatesnf between '{}' and '{}'".format(s222,s111))
				self.ui.textEdit_3.clear()
				self.ui.textEdit_3.append("<p><table width='100%' border='1' cellpadding'5' ><caption><b><u><center>تقرير من فترة الى فترة معينة عن الصادرات</center></u></b></caption><tr><td width=16.7%><u><center>اسم الصنف</center></u></td><td width=16.7%><u><center>رقم الباركود</u></center></td><td width=16.7%><u><center>السعر</u></center></td><td width=16.7%><u><center>الكمية</u></center></td><td width=16.7%><u><center>تاريخ التصدير</u></center></td><td width=16.7%><u><center>وقت التصدير</center></u></td></tr></table></p>")
				for g in snf2:
					self.ui.textEdit_3.append("<p><table width='100%' border='1' cellpadding'5' ><tr><td width=16.7%><center>{}</td><td width=16.7%><center>{}</td><td width=16.7%><center>{}</td><td width=16.7%><center>{}</td><td width=16.7%><center>{}</td><td width=16.7%><center>{}</td></tr></table></p>".format(g["stobufnamesnf"],g["stobufbarcodsnf"],g["stobufpricsnf"],g["stobufamountsnf"],g["stobufdatesnf"],g["stobuftimesnf"]))						
	
#funciton is reportord olny##################################################################################3
	def reportordat(self):
		typtgrer=str(self.ui.pagreportcomtypereport.currentText())
		if typtgrer =="عام":
			self.amord()
		if typtgrer =="من فترة محددة":
			self.detrmainord()
		if typtgrer =="من فترة الى فترة معينة":
			self.intoord()
	def amord(self):
		chreport=str(self.ui.pagreportcomaboutreport.currentText())
		if chreport == "الواردات":

			db1=sqlite3.connect('programcompution.db')
			db1.row_factory=sqlite3.Row
			snf=db1.execute("select * from tableaddmstord")
			self.ui.textEdit_3.clear()
			self.ui.textEdit_3.append("<p><table width='100%' border='1' cellpadding'5' ><caption><b><u><center>تقرير عام عن الواردات</center></u></b></caption><tr><td width=14.3%><u><center>اسم المصدر</center></u></td><td width=14.3%><u><center>اسم المستورد</u></center></td><td width=14.3%><u><center>الكمية</u></center></td><td width=14.3%><u><center>تاريخ الاستيراد</u></center></td><td width=14.3%><u><center>السعر</u></center></td><td width=14.3%><u><center>تاريخ الانتاج</center></u></td><td width=14.3%><u><center>تاريخ الانتهاء</center></u></td></tr></table></p>")
			for g in snf:
				self.ui.textEdit_3.append("<p><table width='100%' border='1' cellpadding'5' ><tr><td width=14.3%><center>{}</td><td width=14.3%><center>{}</td><td width=14.3%><center>{}</td><td width=14.3%><center>{}</td><td width=14.3%><center>{}</td><td width=14.3%><center>{}</td><td width=14.3%><center>{}</td></tr></table></p>".format(g["sourcmstord"],g["nammstord"],g["amunmstord"],g["datemstord"],g["prismtord"],g["datepromstord"],g["dateoutmstord"]))						
	def detrmainord(self):
		db1=sqlite3.connect('programcompution.db')
		db1.row_factory=sqlite3.Row
		snf=db1.execute("select * from tableaddmstord")
		self.ui.pagreportcomoncdetermain.clear()
		for g in snf:
			self.ui.pagreportcomoncdetermain.addItem('{}'.format(g["datemstord"]))
	def intoord(self):
		db1=sqlite3.connect('programcompution.db')
		db1.row_factory=sqlite3.Row
		snf=db1.execute("select * from tableaddmstord")		
		self.ui.pagreportcomononc.clear()
		self.ui.pagreportcomfromonc_2.clear()
		for g in snf:
			#self.ui.pagreportcomoncdetermain.addItem('{}'.format(g["datemstord"]))
			self.ui.pagreportcomononc.addItem('{}'.format(g["datemstord"]))
			self.ui.pagreportcomfromonc_2.addItem('{}'.format(g["datemstord"]))
##############################funcions about report sadrat#####################################################
################################################################################################################
	def reportsadrat(self):
		typtgrer=str(self.ui.pagreportcomtypereport.currentText())
		if typtgrer =="عام":
			self.amsadrat()
		if typtgrer =="من فترة محددة":
			self.detrmainsadrat()
		if typtgrer =="من فترة الى فترة معينة":
			self.intosadrat()

	def amsadrat(self):
		chreport=str(self.ui.pagreportcomaboutreport.currentText())
		if chreport == "الصادرات":
			db1=sqlite3.connect('storgtsder.db')
			db1.row_factory=sqlite3.Row
			snf=db1.execute("select * from storgbuffer2")
			self.ui.textEdit_3.clear()
			self.ui.textEdit_3.append("<p><table width='100%' border='1' cellpadding'5' ><caption><b><u><center>تقرير عام عن الصادرات</center></u></b></caption><tr><td width=16.7%><u><center>اسم الصنف</center></u></td><td width=16.7%><u><center>رقم الباركود</u></center></td><td width=16.7%><u><center>السعر</u></center></td><td width=16.7%><u><center>الكمية</u></center></td><td width=16.7%><u><center>تاريخ التصدير</u></center></td><td width=16.7%><u><center>وقت التصدير</center></u></td></tr></table></p>")
			for g in snf:
				self.ui.textEdit_3.append("<p><table width='100%' border='1' cellpadding'5' ><tr><td width=16.7%><center>{}</td><td width=16.7%><center>{}</td><td width=16.7%><center>{}</td><td width=16.7%><center>{}</td><td width=16.7%><center>{}</td><td width=16.7%><center>{}</td></tr></table></p>".format(g["stobufnamesnf"],g["stobufbarcodsnf"],g["stobufpricsnf"],g["stobufamountsnf"],g["stobufdatesnf"],g["stobuftimesnf"]))						
	
	def detrmainsadrat(self):
		db1=sqlite3.connect('storgtsder.db')
		db1.row_factory=sqlite3.Row
		snf=db1.execute("select * from storgbuffer2 ")	
		self.ui.pagreportcomoncdetermain.clear()
		for g in snf:
			self.ui.pagreportcomoncdetermain.addItem('{}'.format(g["stobufdatesnf"]))
	def intosadrat(self):
		db1=sqlite3.connect('storgtsder.db')
		db1.row_factory=sqlite3.Row
		snf=db1.execute("select * from storgbuffer2 ")
		self.ui.pagreportcomononc.clear()
		self.ui.pagreportcomfromonc_2.clear()
		for g in snf:
			#self.ui.pagreportcomoncdetermain.addItem('{}'.format(g["datemstord"]))
			self.ui.pagreportcomononc.addItem('{}'.format(g["stobufdatesnf"]))
			self.ui.pagreportcomfromonc_2.addItem('{}'.format(g["stobufdatesnf"]))
###########################################الكميات المتبقية###333#####################################################33
##############################################################################################################################
#####################################################################################################################################
	def reportamounremain(self):
		db1=sqlite3.connect('programcompution.db')
		db1.row_factory=sqlite3.Row
		snf=db1.execute("select * from tableaddsinf")
		self.ui.textEdit_3.clear()
		self.ui.textEdit_3.append("<p><table width='100%' border='1' cellpadding'5' ><caption><b><u><center>تقرير عن الكميات المتبقية</center></u></b></caption><tr><td width=12.5%><u><center>اسم الصنف</center></u></td><td width=12.5%><u><center>تاريخ الادخال</u></center></td><td width=12.5%><u><center>رقم الباركود</u></center></td><td width=12.5%><u><center>الكمية</u></center></td><td width=12.5%><u><center>السعر</u></center></td><td width=12.5%><u><center>نوع</center></u></td><td width=12.5%><u><center>تاريخ الانتاج</center></u></td><td width=12.5%><u><center>تاريخ الانتهاء</center></u></td></tr></table></p>")
		for g in snf:
			self.ui.textEdit_3.append("<p><table width='100%' border='1' cellpadding'5' ><tr><td width=12.5%><center>{}</td><td width=12.5%><center>{}</td><td width=12.5%><center>{}</td><td width=12.5%><center>{}</td><td width=12.5%><center>{}</td><td width=12.5%><center>{}</td><td width=12.5%><center>{}</td><td width=12.5%><center>{}</td></tr></table></p>".format(g["datanamesnf"],g["datadatesnf"],g["databarcodsnf"],g["dataamountsnf"],g["datapricsnf"],g["datatypesnf"],g["datadateprodsnf"],g["datadateoutsnf"]))			

#printer#############################33
	def printreport(self):
		if self.ui.textEdit_3.toPlainText() !="":
			printer =QtPrintSupport.QPrintDialog()
			#printer.setFullPage(True)
			#dialog = QtGui.QPrintDialog(printer)
			if printer.exec_() == QtWidgets.QDialog.Accepted:
				self.ui.textEdit_3.document().print_(printer.printer())
				printer.exec_()
	def showsnfintable1(self):
		cher=str(self.ui.pagstalmentbarcod.text())
		db1=sqlite3.connect('programcompution.db')
		db1.row_factory=sqlite3.Row
		snf=db1.execute("select * from tableaddsinf where databarcodsnf='{}'".format(cher))
		self.ui.pagstalmtabl.clear()
		self.ui.pagstalmtabl.append("<p><table width='100%' border='1' cellpadding'5' ><caption><b><u><center>استعلام عن صنف معين</center></u></b></caption><tr><td width=14.3%><u><center>اسم الصنف</center></u></td><td width=14.3%><t><u><center>تاريخ الادخال</u></center></td><td width=14.3%><u><center>رقم الباركود</u></center></td><td width=14.3%><u><center>السعر</u></center></td><td width=14.3%><u><center>تاريخ الانتاج</center></u></td><td width=14.3%><u><center>تاريخ الانتهاء</center></u></td><td width=14.3%><u><center>الكميات المتبقية من هذا النوع</center></u></td></tr></table></p>")
		for g in snf:
			self.ui.pagstalmtabl.append("<p><table width='100%' border='1' cellpadding'5' ><tr><td width=14.3%><center>{}</td><td width=14.3%><center>{}</td><td width=14.3%><center>{}</td><td width=14.3%><center>{}</td><td width=14.3%><center>{}</td><td width=14.3%><center>{}</td><td width=14.3%><center>{}</td></tr></table></p>".format(g["datanamesnf"],g["datadatesnf"],g["databarcodsnf"],g["datapricsnf"],g["datadateprodsnf"],g["datadateoutsnf"],g["dataamountsnf"]))			

	def showsnfintable2(self):
		cher=str(self.ui.comboBox_10.currentText())
		db1=sqlite3.connect('programcompution.db')
		db1.row_factory=sqlite3.Row
		snf=db1.execute("select * from tableaddsinf where datanamesnf='{}'".format(cher))
		self.ui.pagstalmtabl.clear()
		self.ui.pagstalmtabl.append("<p><table width='100%' border='1' cellpadding'5' ><caption><b><u><center>استعلام عن صنف معين</center></u></b></caption><tr><td width=14.3%><u><center>اسم الصنف</center></u></td><td width=14.3%><t><u><center>تاريخ الادخال</u></center></td><td width=14.3%><u><center>رقم الباركود</u></center></td><td width=14.3%><u><center>السعر</u></center></td><td width=14.3%><u><center>تاريخ الانتاج</center></u></td><td width=14.3%><u><center>تاريخ الانتهاء</center></u></td><td width=14.3%><u><center>الكميات المتبقية من هذا النوع</center></u></td></tr></table></p>")
		for g in snf:
			self.ui.pagstalmtabl.append("<p><table width='100%' border='1' cellpadding'5' ><tr><td width=14.3%><center>{}</td><td width=14.3%><center>{}</td><td width=14.3%><center>{}</td><td width=14.3%><center>{}</td><td width=14.3%><center>{}</td><td width=14.3%><center>{}</td><td width=14.3%><center>{}</td></tr></table></p>".format(g["datanamesnf"],g["datadatesnf"],g["databarcodsnf"],g["datapricsnf"],g["datadateprodsnf"],g["datadateoutsnf"],g["dataamountsnf"]))			

	def addsnf(self):
		db1=sqlite3.connect('programcompution.db')
		db1.row_factory=sqlite3.Row
		snf=db1.execute("select datanamesnf from tableaddsinf")
		for g in snf:
			self.ui.comboBox_10.addItem('{}'.format(g["datanamesnf"]))	
	###################################المصروف اليومي########################################################
	def determony(self):
		e=0
		today = str(date.today())
		db1=sqlite3.connect('storgtsder.db')
		db1.row_factory=sqlite3.Row
		snf=db1.execute("select sum(stobufpricsnf) from storgbuffer2 where stobufdatesnf='{}'".format(today))
		try:
			for x in snf:
				e=1
				message=QtWidgets.QMessageBox.information(self,'information','<FONT size=10 color=blue>مصروف اليوم هو{}</FONT>'.format(x[0]))
			if e==0:
				message=QtWidgets.QMessageBox.information(self,'information','<FONT size=10 color=blue>عذرا لايوجد اي مصروف في هذا اليوم</FONT>')
		except:
			print('not msrof')

##################################################modefissss#################################################


	def addmodsnf(self):
		
		db1=sqlite3.connect('programcompution.db')
		db1.row_factory=sqlite3.Row
		snf=db1.execute("select * from tableaddsinf")
		for g in snf:

			self.modsnfshw.ui1.pgemodsnfcomentername.addItem('{}'.format(g["datanamesnf"]))
	def modsnfserbarcod(self):
		global dgn
		dgn=1
		chikmodbarsnf=str(self.modsnfshw.ui1.pgemodsnfententerbarcod.text())
		db1=sqlite3.connect('programcompution.db')
		db1.row_factory=sqlite3.Row
		snf=db1.execute("select * from tableaddsinf where databarcodsnf='{}'".format(chikmodbarsnf))
		for g in snf:
			self.modsnfshw.ui1.pgemodsnfentnamesnf.setText(g["datanamesnf"])
			self.modsnfshw.ui1.pgemodsnfentdatesnf.setText(g["datadatesnf"])
			self.modsnfshw.ui1.pgemodsnfentbarcod.setText(g["databarcodsnf"])
			self.modsnfshw.ui1.pgemodsnfentamount.setText(g["dataamountsnf"])
			self.modsnfshw.ui1.pgemodsnfentpric.setText(g["datapricsnf"])
			self.modsnfshw.ui1.pgemodsnfenttype.setText(g["datatypesnf"])
			self.modsnfshw.ui1.pgemodsnfentdatepro.setText(g["datadateprodsnf"])
			self.modsnfshw.ui1.pgemodsnfentdateout.setText(g["datadateoutsnf"])
	def modsnfsername(self):
		global dgn
		chikmodbarsnf=str(self.modsnfshw.ui1.pgemodsnfcomentername.currentText())
		db1=sqlite3.connect('programcompution.db')
		db1.row_factory=sqlite3.Row
		snf=db1.execute("select * from tableaddsinf where datanamesnf='{}'".format(chikmodbarsnf))
		for g in snf:
			self.modsnfshw.ui1.pgemodsnfententerbarcod.setText(g["databarcodsnf"])
			self.modsnfshw.ui1.pgemodsnfentnamesnf.setText(g["datanamesnf"])
			self.modsnfshw.ui1.pgemodsnfentdatesnf.setText(g["datadatesnf"])
			self.modsnfshw.ui1.pgemodsnfentbarcod.setText(g["databarcodsnf"])
			self.modsnfshw.ui1.pgemodsnfentamount.setText(g["dataamountsnf"])
			self.modsnfshw.ui1.pgemodsnfentpric.setText(g["datapricsnf"])
			self.modsnfshw.ui1.pgemodsnfenttype.setText(g["datatypesnf"])
			self.modsnfshw.ui1.pgemodsnfentdatepro.setText(g["datadateprodsnf"])
			self.modsnfshw.ui1.pgemodsnfentdateout.setText(g["datadateoutsnf"])
		
	def modsnfmod(self):
		message1=QtWidgets.QMessageBox.question(self,'Question',"هل انتة متاكد من تعديل الصنف",QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
		if message1==QtWidgets.QMessageBox.Yes:

			chikmodbarsnf=str(self.modsnfshw.ui1.pgemodsnfententerbarcod.text())
			s1=str(self.modsnfshw.ui1.pgemodsnfentnamesnf.text())
			s2=str(self.modsnfshw.ui1.pgemodsnfentdatesnf.text())
			s3=str(self.modsnfshw.ui1.pgemodsnfentbarcod.text())
			s4=str(self.modsnfshw.ui1.pgemodsnfentamount.text())
			s5=str(self.modsnfshw.ui1.pgemodsnfentpric.text())
			s6=str(self.modsnfshw.ui1.pgemodsnfenttype.text())
			s7=str(self.modsnfshw.ui1.pgemodsnfentdatepro.text())
			s8=str(self.modsnfshw.ui1.pgemodsnfentdateout.text())
			db1=sqlite3.connect('programcompution.db')
			db1.row_factory=sqlite3.Row
			db1.execute("update tableaddsinf set datanamesnf='{}',datadatesnf='{}',databarcodsnf='{}',dataamountsnf='{}',datapricsnf='{}',datatypesnf='{}',datadateprodsnf='{}',datadateoutsnf='{}' where databarcodsnf='{}'".format(s1,s2,s3,s4,s5,s6,s7,s8,chikmodbarsnf))		
			db1.commit()
			message=QtWidgets.QMessageBox.information(self,'information','<FONT size=10 color=blue>تم تعديل الصنف بنجاح</FONT>')
		
	def deletsnf(self):
		message1=QtWidgets.QMessageBox.question(self,'Question',"هل انتة متاكد من حذف الصنف",QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
		if message1==QtWidgets.QMessageBox.Yes:
			chikmodbarsnf=str(self.modsnfshw.ui1.pgemodsnfententerbarcod.text())
			db1=sqlite3.connect('programcompution.db')
			db1.row_factory=sqlite3.Row
			db1.execute("delete from tableaddsinf where databarcodsnf='{}'".format(chikmodbarsnf))
			db1.commit()	

			message=QtWidgets.QMessageBox.information(self,'information','<FONT size=10 color=blue>تم حذف الصنف بنجاح</FONT>')
	
	def modsnf(self):
		self.modsnfshw=NotePad1()
		self.addmodsnf()
		self.modsnfshw.ui1.pgemodsnfbutsavemod.clicked.connect(self.modsnfmod)
		self.modsnfshw.ui1.pgemodsnfbutdelet.clicked.connect(self.deletsnf)
		self.modsnfshw.ui1.pgemodsnfententerbarcod.textChanged.connect(self.modsnfserbarcod)
		self.modsnfshw.ui1.pgemodsnfcomentername.activated.connect(self.modsnfsername)
		self.modsnfshw.show()

# if __name__ == "__main__":
# 	import sys
# 	app = QtWidgets.QApplication(sys.argv)
# 	myapp = NotePad()
# myapp.show()
# sys.exit(app.exec_())


#####################################chik################################3
db2=sqlite3.connect('ship.db')
u=[]
db2.row_factory=sqlite3.Row
db2.execute('create table if not exists shb1(ID integer primary Key autoincrement,t1 text,t2 text,t3 text)')
db2.commit()
ff=db2.execute("select * from shb1")
for n in ff:
	u.append(n['t1'])
if len(u)==0:

	app = QtWidgets.QApplication(sys.argv)
	myapp = NotePad2()
	myapp.show()
	sys.exit(app.exec_())
else:
	
	if u[0]=="ooo":
		app = QtWidgets.QApplication(sys.argv)
		myapp = NotePad()
		myapp.show()
		sys.exit(app.exec_())
	else:
		u2=[]
		db4=sqlite3.connect('ship.db')
		db4.row_factory=sqlite3.Row
		ff1=db2.execute("select * from shb1")
		for h in ff1:
			u2.append(h["t2"])
		
		if len(u2)>=4:
			
			app = QtWidgets.QApplication(sys.argv)
			myapp = NotePad2()
			myapp.show()
			sys.exit(app.exec_())
			
		else:
			db4.execute("insert into shb1(t2) values(?)",('2'))
			db4.commit()
			app = QtWidgets.QApplication(sys.argv)
			myapp = NotePad()
			myapp.show()
			sys.exit(app.exec_())

    	
