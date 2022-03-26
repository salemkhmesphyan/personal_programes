# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'project5.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets, QtWidgets,QtPrintSupport

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtWidgets.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig)
import time
import sqlite3
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(808, 624)
        #MainWindow.setStyleSheet(_fromUtf8("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 235, 235, 206), stop:0.35 rgba(255, 188, 188, 80), stop:0.4 rgba(255, 162, 162, 80), stop:0.425 rgba(255, 132, 132, 156), stop:0.44 rgba(252, 128, 128, 80), stop:1 rgba(255, 255, 255, 0));"))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName(_fromUtf8("horizontalLayout_12"))
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setStyleSheet(_fromUtf8("font: 24pt \"Nimbus Sans L\";"))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout_3.addWidget(self.label_5)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.butaddwik = QtWidgets.QPushButton(self.tab)
        self.butaddwik.setObjectName(_fromUtf8("butaddwik"))
        self.horizontalLayout_9.addWidget(self.butaddwik)
        self.enaddwik = QtWidgets.QLineEdit(self.tab)
        self.enaddwik.setObjectName(_fromUtf8("enaddwik"))
        self.horizontalLayout_9.addWidget(self.enaddwik)
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setStyleSheet(_fromUtf8("font: 75 italic 12pt \"Noto Sans\";"))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_9.addWidget(self.label_6)
        self.verticalLayout_3.addLayout(self.horizontalLayout_9)
        self.line_3 = QtWidgets.QFrame(self.tab)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.verticalLayout_3.addWidget(self.line_3)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.comaddbock = QtWidgets.QComboBox(self.tab)
        self.comaddbock.setObjectName(_fromUtf8("comaddbock"))
        self.comaddbock.addItem(_fromUtf8(""))
        self.comaddbock.addItem(_fromUtf8(""))
        self.comaddbock.addItem(_fromUtf8(""))
        self.horizontalLayout_10.addWidget(self.comaddbock)
        self.label_9 = QtWidgets.QLabel(self.tab)
        self.label_9.setStyleSheet(_fromUtf8("font: 75 italic 12pt \"Noto Sans\";"))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.horizontalLayout_10.addWidget(self.label_9)
        self.enaddnamestud = QtWidgets.QLineEdit(self.tab)
        self.enaddnamestud.setObjectName(_fromUtf8("enaddnamestud"))
        self.horizontalLayout_10.addWidget(self.enaddnamestud)
        self.label_7 = QtWidgets.QLabel(self.tab)
        self.label_7.setStyleSheet(_fromUtf8("font: 75 italic 12pt \"Noto Sans\";"))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_10.addWidget(self.label_7)
        self.verticalLayout_3.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.enaddroom = QtWidgets.QLineEdit(self.tab)
        self.enaddroom.setObjectName(_fromUtf8("enaddroom"))
        self.horizontalLayout_11.addWidget(self.enaddroom)
        self.label_10 = QtWidgets.QLabel(self.tab)
        self.label_10.setStyleSheet(_fromUtf8("font: 75 italic 12pt \"Noto Sans\";"))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.horizontalLayout_11.addWidget(self.label_10)
        self.enaddnumberstud = QtWidgets.QLineEdit(self.tab)
        self.enaddnumberstud.setObjectName(_fromUtf8("enaddnumberstud"))
        self.horizontalLayout_11.addWidget(self.enaddnumberstud)
        self.label_8 = QtWidgets.QLabel(self.tab)
        self.label_8.setStyleSheet(_fromUtf8("font: 75 italic 12pt \"Noto Sans\";"))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout_11.addWidget(self.label_8)
        self.verticalLayout_3.addLayout(self.horizontalLayout_11)
        self.butaddstud = QtWidgets.QPushButton(self.tab)
        self.butaddstud.setObjectName(_fromUtf8("butaddstud"))
        self.verticalLayout_3.addWidget(self.butaddstud)
        self.horizontalLayout_12.addLayout(self.verticalLayout_3)
        self.line = QtWidgets.QFrame(self.tab)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.horizontalLayout_12.addWidget(self.line)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setStyleSheet(_fromUtf8("font: 24pt \"Nimbus Sans L\";"))
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_2.addWidget(self.label)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.comwikdaynow = QtWidgets.QComboBox(self.tab)
        self.comwikdaynow.setEditable(True)
        self.comwikdaynow.setObjectName(_fromUtf8("comwikdaynow"))
        self.horizontalLayout_5.addWidget(self.comwikdaynow)
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setStyleSheet(_fromUtf8("font: 75 italic 12pt \"Noto Sans\";"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_5.addWidget(self.label_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.entodaynow = QtWidgets.QLineEdit(self.tab)
        self.entodaynow.setObjectName(_fromUtf8("entodaynow"))
        self.horizontalLayout_6.addWidget(self.entodaynow)
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setStyleSheet(_fromUtf8("font: 75 italic 12pt \"Noto Sans\";"))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_6.addWidget(self.label_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.comtypeeta = QtWidgets.QComboBox(self.tab)
        self.comtypeeta.setObjectName(_fromUtf8("comtypeeta"))
        self.comtypeeta.addItem(_fromUtf8(""))
        self.comtypeeta.addItem(_fromUtf8(""))
        self.comtypeeta.addItem(_fromUtf8(""))
        self.horizontalLayout_8.addWidget(self.comtypeeta)
        self.label_15 = QtWidgets.QLabel(self.tab)
        self.label_15.setStyleSheet(_fromUtf8("font: 75 italic 12pt \"Noto Sans\";"))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.horizontalLayout_8.addWidget(self.label_15)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.ennumberstudnow = QtWidgets.QLineEdit(self.tab)
        self.ennumberstudnow.setObjectName(_fromUtf8("ennumberstudnow"))
        self.horizontalLayout_7.addWidget(self.ennumberstudnow)
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setStyleSheet(_fromUtf8("font: 75 italic 12pt \"Noto Sans\";"))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_7.addWidget(self.label_4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_12.addLayout(self.verticalLayout_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_12)
        self.line_4 = QtWidgets.QFrame(self.tab)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.verticalLayout_4.addWidget(self.line_4)
        self.gridLayout_3.addLayout(self.verticalLayout_4, 0, 0, 1, 1)
        self.tableWidget1 = QtWidgets.QTableWidget(self.tab)
        self.tableWidget1.setObjectName(_fromUtf8("tableWidget1"))
        self.tableWidget1.setColumnCount(13)
        self.tableWidget1.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget1.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget1.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget1.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget1.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget1.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget1.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget1.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget1.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget1.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget1.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget1.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget1.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget1.setHorizontalHeaderItem(12, item)
        self.gridLayout_3.addWidget(self.tableWidget1, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.gridLayout = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.comtypesearch = QtWidgets.QComboBox(self.tab_2)
        self.comtypesearch.setObjectName(_fromUtf8("comtypesearch"))
        self.comtypesearch.addItem(_fromUtf8(""))
        self.comtypesearch.addItem(_fromUtf8(""))
        self.comtypesearch.addItem(_fromUtf8(""))
        self.horizontalLayout.addWidget(self.comtypesearch)
        self.label_11 = QtWidgets.QLabel(self.tab_2)
        self.label_11.setStyleSheet(_fromUtf8("font: 75 italic 14pt \"Noto Sans\";"))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.horizontalLayout.addWidget(self.label_11)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.comsarchnamestud =  QtWidgets.QLineEdit(self.tab_2)
        self.comsarchnamestud.setObjectName(_fromUtf8("comsarchnamestud"))
        self.horizontalLayout_2.addWidget(self.comsarchnamestud)
        self.label_12 = QtWidgets.QLabel(self.tab_2)
        self.label_12.setStyleSheet(_fromUtf8("font: 75 italic 14pt \"Noto Sans\";"))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.horizontalLayout_2.addWidget(self.label_12)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.comsearchnumberblock = QtWidgets.QComboBox(self.tab_2)
        self.comsearchnumberblock.setObjectName(_fromUtf8("comsearchnumberblock"))
        self.comsearchnumberblock.addItem(_fromUtf8(""))
        self.comsearchnumberblock.addItem(_fromUtf8(""))
        self.comsearchnumberblock.addItem(_fromUtf8(""))
        self.horizontalLayout_3.addWidget(self.comsearchnumberblock)
        self.label_13 = QtWidgets.QLabel(self.tab_2)
        self.label_13.setStyleSheet(_fromUtf8("font: 75 italic 14pt \"Noto Sans\";"))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.horizontalLayout_3.addWidget(self.label_13)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.butsearch = QtWidgets.QPushButton(self.tab_2)
        self.butsearch.setObjectName(_fromUtf8("butsearch"))
        self.horizontalLayout_4.addWidget(self.butsearch)
        self.ensearchnumberroom = QtWidgets.QLineEdit(self.tab_2)
        self.ensearchnumberroom.setObjectName(_fromUtf8("ensearchnumberroom"))
        self.horizontalLayout_4.addWidget(self.ensearchnumberroom)
        self.label_14 = QtWidgets.QLabel(self.tab_2)
        self.label_14.setStyleSheet(_fromUtf8("font: 75 italic 14pt \"Noto Sans\";"))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.horizontalLayout_4.addWidget(self.label_14)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.line_5 = QtWidgets.QFrame(self.tab_2)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.verticalLayout.addWidget(self.line_5)
        self.tableWidget_2 = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidget_2.setObjectName(_fromUtf8("tableWidget_2"))
        self.tableWidget_2.setColumnCount(5)
        self.tableWidget_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, item)
        self.verticalLayout.addWidget(self.tableWidget_2)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 808, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "برنامج لتحظير وجبات الطعام في سكن الجامعة", None))
        self.label_5.setText(_translate("MainWindow", "الاضافات", None))
        self.butaddwik.setText(_translate("MainWindow", "اضافة اسبوع", None))
        self.label_6.setText(_translate("MainWindow", "اضافة أسبوع جديد:", None))
        self.comaddbock.setItemText(0, _translate("MainWindow", "BLOCK NUMBER 1", None))
        self.comaddbock.setItemText(1, _translate("MainWindow", "BLOCK NUMBER 2", None))
        self.comaddbock.setItemText(2, _translate("MainWindow", "BLOCK NUMBER 3", None))
        self.label_9.setText(_translate("MainWindow", "رقم العمارة:", None))
        self.label_7.setText(_translate("MainWindow", "اضافة اسم جديد:", None))
        self.label_10.setText(_translate("MainWindow", "رقم الغرفة:", None))
        self.label_8.setText(_translate("MainWindow", "رقم الطالب:", None))
        self.butaddstud.setText(_translate("MainWindow", "اضافةطالب", None))
        self.label.setText(_translate("MainWindow", "عمل اليوم هنا", None))
        self.label_2.setText(_translate("MainWindow", "الاسبوع:", None))
        self.label_3.setText(_translate("MainWindow", "اليوم:", None))
        self.comtypeeta.setItemText(0, _translate("MainWindow", "BREK FAST", None))
        self.comtypeeta.setItemText(1, _translate("MainWindow", "LINCH", None))
        self.comtypeeta.setItemText(2, _translate("MainWindow", "DINNER", None))
        self.label_15.setText(_translate("MainWindow", "نوع الوجبة:", None))
        self.label_4.setText(_translate("MainWindow", "رقم الطالب:", None))
        item = self.tableWidget1.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID", None))
        item = self.tableWidget1.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "رقم الطالب", None))
        item = self.tableWidget1.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "اسم الطالب", None))
        item = self.tableWidget1.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "السبت", None))
        item = self.tableWidget1.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "الاحد", None))
        item = self.tableWidget1.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "الاثنين", None))
        item = self.tableWidget1.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "الثلاثاء", None))
        item = self.tableWidget1.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "الاربعاء", None))
        item = self.tableWidget1.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "الخميس", None))
        item = self.tableWidget1.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "الجمعة", None))
        item = self.tableWidget1.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "الفطور", None))
        item = self.tableWidget1.horizontalHeaderItem(11)
        item.setText(_translate("MainWindow", "الغدا", None))
        item = self.tableWidget1.horizontalHeaderItem(12)
        item.setText(_translate("MainWindow", "العشاء", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Home page", None))
        self.comtypesearch.setItemText(0, _translate("MainWindow", "NAME STUDENT", None))
        self.comtypesearch.setItemText(1, _translate("MainWindow", "NUMBER BLOCK", None))
        self.comtypesearch.setItemText(2, _translate("MainWindow", "NUMBER ROOM", None))
        self.label_11.setText(_translate("MainWindow", "نوع البحث:", None))
        self.label_12.setText(_translate("MainWindow", "الاسم:", None))
        self.comsearchnumberblock.setItemText(0, _translate("MainWindow", "BLOCK NUMBER 1", None))
        self.comsearchnumberblock.setItemText(1, _translate("MainWindow", "BLOCK NUMBER 2", None))
        self.comsearchnumberblock.setItemText(2, _translate("MainWindow", "BLOCK NUMBER 3", None))
        self.label_13.setText(_translate("MainWindow", "رقم العمارة:", None))
        self.butsearch.setText(_translate("MainWindow", "search", None))
        self.label_14.setText(_translate("MainWindow", "رقم الغرفة:", None))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID", None))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "رقم الطالب", None))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "اسم الطالب", None))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "رقم العمارة", None))
        item = self.tableWidget_2.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "رقم الغرفة", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "search", None))


class NotePad(QtWidgets.QMainWindow):
	def __init__(self, parent=None):
		QtWidgets.QWidget.__init__(self, parent)#lambda:تضعها عند اسم الزر
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		t=time.asctime(time.localtime(time.time()))
		self.ui.enaddwik.setText(t)
		self.ui.butaddwik.clicked.connect(self.addwikee)
		self.ui.butaddstud.clicked.connect(self.addnamestud)
		#QtCore.QObject.connect(self.ui.ennumberstudnow,QtCore.SIGNAL("textChanged(QString)"),self.enterowrknow)
		self.ui.ennumberstudnow.textChanged.connect(self.enterowrknow)
		#self.ui.comtypesearch
		#QtCore.QObject.connect(self.ui.comsarchnamestud,QtCore.SIGNAL("textChanged(QString)"),self.searchname)
		self.ui.comsarchnamestud.textChanged.connect(self.searchname)
		self.ui.entodaynow.setText(t[:3])
		self.ui.butsearch.clicked.connect(self.typeser)
		try:
		
			self.showstorgdatabase()
		except:
				message=QtWidgets.QMessageBox.information(self,'information','<FONT size=10 color=blue>غير موجود</FONT>')



########################################################################TAB 1###########################################################
	def addwikee(self):
		adddatabase=str(self.ui.enaddwik.text())
		s=adddatabase+".db"
		db=sqlite3.connect(s)
		db.row_factory=sqlite3.Row
		db.execute('create table if not exists tb1(ID integer primary Key autoincrement,numberstudent text,namestudent text,STR text,SUN text,MOU text,TUS text,WED text,THR text,FRA text,brek text,lunsh text,dinner text)')
		self.storgnamedata(adddatabase)
		db.commit()	
		db.close()
		message=QtWidgets.QMessageBox.information(self,'information','<FONT size=10 color=blue>تم اضافة الاسبوه بنجاح</FONT>')
	def storgnamedata(self,g):
		db=sqlite3.connect("storgnd.db")
		db.row_factory=sqlite3.Row
		db.execute('create table if not exists tb1(ID integer primary Key autoincrement,namedb text,nm1 text)')
		db.execute("insert into tb1(namedb,nm1) values(?,?)",(g,g))
		db.commit()
		db.close()
		
	def showstorgdatabase(self):
		db=sqlite3.connect("storgnd.db")
		db.row_factory=sqlite3.Row
		sd=db.execute('select * from tb1')
		try:
			
			for h in sd:
				self.ui.comwikdaynow.addItem("{}".format(h["namedb"]))
		except:
			message=QtWidgets.QMessageBox.information(self,'information','<FONT size=10 color=blue>غير موجود</FONT>')	

	def addnamestud(self):
		enaddnamestud=str(self.ui.enaddnamestud.text())
		enaddnumberstud	=str(self.ui.enaddnumberstud.text())		
		choosaddnumberblock=str(self.ui.comaddbock.currentText())
		enaddnumberroom=str(self.ui.enaddroom.text())
		db=sqlite3.connect("addnewstudent.db")
		db.row_factory=sqlite3.Row
		db.execute('create table if not exists tb1(ID integer primary Key autoincrement,numstud text,namstud text,numblock text,numroom text)')
		db.execute("insert into tb1(numstud,namstud,numblock,numroom) values(?,?,?,?)",(enaddnumberstud,enaddnamestud,choosaddnumberblock,enaddnumberroom))
		db.commit()
		db.close()
		message=QtWidgets.QMessageBox.information(self,'information','<FONT size=10 color=blue>تم الاضافة بنجاح</FONT>')
		self.ui.enaddnamestud.clear()
		self.ui.enaddnumberstud.clear()
		self.ui.enaddroom.clear()
		message=QtWidgets.QMessageBox.information(self,'information','<FONT size=10 color=blue>Add Successfully</FONT>')
####################################################work now########################################################################		
	def enterowrknow(self):
		wikenow=str(self.ui.comwikdaynow.currentText())
		w=wikenow+".db"

		eatnow=str(self.ui.comtypeeta.currentText())

		daynow=str(self.ui.entodaynow.text())
		
		numstudnow=str(self.ui.ennumberstudnow.text())
		op1=0
		op2=0
		db2=sqlite3.connect(w)
		db2.row_factory=sqlite3.Row
		sh=db2.execute('select * from tb1 where numberstudent="{}"'.format(numstudnow))		
		for n in sh:
			if numstudnow==n["numberstudent"]:
				op1=1
				self.chickday()
				self.chickeate()
				while self.ui.tableWidget1.rowCount() >0:
					self.ui.tableWidget1.removeRow(0)
				self.shr(numstudnow)
				#for rowindx,rowdata in enumerate(n):
			 	#	self.ui.tableWidget1.insertRow(rowindx)
				#	for colmindx,colmdata in enumerate(rowdata):
			 	#		self.ui.tableWidget1.setItem(rowindx,colmindx,QtWidgets.QTableWidgetItem(str(colmdata)))
			elif numstudnow!=n["numberstudent"]:
				
				numstudnow=str(self.ui.ennumberstudnow.text())
				db1=sqlite3.connect("addnewstudent.db")
				db1.row_factory=sqlite3.Row
				sf=db1.execute("select * from tb1 where numstud='{}'".format(numstudnow))
				for g in sf:
					
					self.ui.enaddnamestud.clear()
					self.ui.enaddnamestud.setText(g['namstud'])
					a=str(self.ui.enaddnamestud.text())#numberstudent text,namestudent text,STR text,SUN text,MOU text,TUS text,WED text,THR text,FRA text,brek text,lunsh text,dinner
					qw=db2.execute("insert into tb1(numberstudent,namestudent,STR,SUN,MOU,TUS,WED,THR,FRA,brek,lunsh,dinner) values(?,?,?,?,?,?,?,?,?,?,?,?)",(numstudnow,a,"F","F","F","F","F","F","F","F","F","F"))	
					self.chickday()
					self.chickeate()
					while self.ui.tableWidget1.rowCount() >0:
						self.ui.tableWidget1.removeRow(0)
					for rowindx,rowdata in enumerate(sh):
				 		self.ui.tableWidget1.insertRow(rowindx)
				 		
				 		for colmindx,colmdata in enumerate(rowdata):
				 			self.ui.tableWidget1.setItem(rowindx,colmindx,QtWidgets.QTableWidgetItem(str(colmdata)))
		if op1==0:
				
				numstudnow=str(self.ui.ennumberstudnow.text())
				db1=sqlite3.connect("addnewstudent.db")
				db1.row_factory=sqlite3.Row
				sf=db1.execute("select * from tb1 where numstud='{}'".format(numstudnow))
				for g in sf:
					if numstudnow==g['numstud']:
							op2=1
							
							self.ui.enaddnamestud.clear()
							self.ui.enaddnamestud.setText(g['namstud'])
							self.conow()
					#a=str(self.ui.enaddnamestud.text())#numberstudent text,namestudent text,STR text,SUN text,MOU text,TUS text,WED text,THR text,FRA text,brek text,lunsh text,dinner
					#qw=db2.execute("insert into tb1(numberstudent,namestudent,STR,SUN,MOU,TUS,WED,THR,FRA,brek,lunsh,dinner) values(?,?,?,?,?,?,?,?,?,?,?,?)",(numstudnow,a,"F","F","F","F","F","F","F","F","F","F"))	
					#self.chickday()
					#self.chickeate()
					#self.ui.enaddnamestud.clear()
					
	def conow(self):
			wikenow=str(self.ui.comwikdaynow.currentText())
			w=wikenow+".db"
			eatnow=str(self.ui.comtypeeta.currentText())

			daynow=str(self.ui.entodaynow.text())
		
			numstudnow=str(self.ui.ennumberstudnow.text())
			a=str(self.ui.enaddnamestud.text())	
			db1=sqlite3.connect(w)
			db1.row_factory=sqlite3.Row	
			db1.execute("insert into tb1(numberstudent,namestudent,STR,SUN,MOU,TUS,WED,THR,FRA,brek,lunsh,dinner) values(?,?,?,?,?,?,?,?,?,?,?,?)",(numstudnow,a,"F","F","F","F","F","F","F","F","F","F"))
			db1.commit()
			self.ui.enaddnamestud.clear()
			db2=sqlite3.connect(w)
			db2.row_factory=sqlite3.Row
			sh=db2.execute('select * from tb1 where numberstudent="{}"'.format(numstudnow))		
			for n in sh:
				if numstudnow==n["numberstudent"]:
		 			self.chickday()	
		 			self.chickeate()
		 			while self.ui.tableWidget1.rowCount() >0:
		 				self.ui.tableWidget1.removeRow(0)
		 			self.shr(numstudnow)	
	def shr(self,t):
		 wikenow=str(self.ui.comwikdaynow.currentText())
		 w=wikenow+".db"
		 db2=sqlite3.connect(w)
		 db2.row_factory=sqlite3.Row
		 sh=db2.execute('select * from tb1 where numberstudent="{}"'.format(t))
		 for rowindx,rowdata in enumerate(sh):
		 	 self.ui.tableWidget1.insertRow(rowindx)
		 	 for colmindx,colmdata in enumerate(rowdata):
		 	 	self.ui.tableWidget1.setItem(rowindx,colmindx,QtWidgets.QTableWidgetItem(str(colmdata)))
			 			
	def chickeate(self):
		wikenow=str(self.ui.comwikdaynow.currentText())
		w=wikenow+".db"
		eatnow=str(self.ui.comtypeeta.currentText())
		daynow=str(self.ui.entodaynow .text())
		numstudnow=str(self.ui.ennumberstudnow.text())
		if eatnow=="BREK FAST":
			self.brekfast()
		if eatnow=="LINCH":
			self.lun()
		if eatnow=="DINNER":
			self.din()
	def brekfast(self):
		wikenow=str(self.ui.comwikdaynow.currentText())
		w=wikenow+".db"
		eatnow=str(self.ui.comtypeeta.currentText())
		daynow=str(self.ui.entodaynow .text())
		numstudnow=str(self.ui.ennumberstudnow.text())
		db=sqlite3.connect(w)
		db.row_factory=sqlite3.Row
		if daynow=="Sat":

			sh=db.execute("select brek from tb1 where numberstudent='{}'and STR='{}'".format(numstudnow,"T"))
			for d in sh:
				if "B/Sat"==d['brek']:
					message=QtWidgets.QMessageBox.information(self,'information','<FONT size=10 color=blue>STOOP</FONT>')
				else:
					db.execute("update tb1 set brek='B/Sat' where numberstudent='{}'".format(numstudnow))
					db.commit()
		if daynow=="Sun":

			sh=db.execute("select brek from tb1 where numberstudent='{}'and SUN='{}'".format(numstudnow,"T"))
			for d in sh:
				if "B/Sun"==d['brek']:
					message=QtWidgets.QMessageBox.information(self,'information','<FONT size=10 color=blue>STOOP</FONT>')
				else:
					db.execute("update tb1 set brek='B/Sun' where numberstudent='{}'".format(numstudnow))
					db.commit()
		if daynow=="Mon":

			sh=db.execute("select brek from tb1 where numberstudent='{}'and MOU='{}'".format(numstudnow,"T"))
			for d in sh:
				if "B/Mon"==d['brek']:
					message=QtWidgets.QMessageBox.information(self,'information','<FONT size=10 color=blue>STOOP</FONT>')
				else:
					db.execute("update tb1 set brek='B/Mon' where numberstudent='{}'".format(numstudnow))
					db.commit()
		if daynow=="Tue":

			sh=db.execute("select brek from tb1 where numberstudent='{}'and TUS='{}'".format(numstudnow,"T"))
			for d in sh:
				if "B/Tue"==d['brek']:
					message=QtWidgets.QMessageBox.information(self,'information','<FONT size=10 color=blue>STOOP</FONT>')
				else:
					db.execute("update tb1 set brek='B/Tue' where numberstudent='{}'".format(numstudnow))
					db.commit()
		if daynow=="Wed":

			sh=db.execute("select brek from tb1 where numberstudent='{}'and WED='{}'".format(numstudnow,"T"))
			for d in sh:
				if "B/Wed"==d['brek']:
					message=QtWidgets.QMessageBox.information(self,'information','<FONT size=10 color=blue>STOOP</FONT>')
				else:
					db.execute("update tb1 set brek='B/Wed' where numberstudent='{}'".format(numstudnow))
					db.commit()
		if daynow=="Thu":

			sh=db.execute("select brek from tb1 where numberstudent='{}'and THR='{}'".format(numstudnow,"T"))
			for d in sh:
				if "B/Thu"==d['brek']:
					message=QtWidgets.QMessageBox.information(self,'information','<FONT size=10 color=blue>STOOP</FONT>')
				else:
					db.execute("update tb1 set brek='B/Thu' where numberstudent='{}'".format(numstudnow))
					db.commit()
		if daynow=="Fri":

			sh=db.execute("select brek from tb1 where numberstudent='{}'and FRA='{}'".format(numstudnow,"T"))
			for d in sh:
				if "B/Fri"==d['brek']:
					message=QtWidgets.QMessageBox.information(self,'information','<FONT size=10 color=blue>STOOP</FONT>')
				else:
					db.execute("update tb1 set brek='B/Fri' where numberstudent='{}'".format(numstudnow))
					db.commit()																			
	def lun(self):
		wikenow=str(self.ui.comwikdaynow.currentText())
		w=wikenow+".db"
		eatnow=str(self.ui.comtypeeta.currentText())
		daynow=str(self.ui.entodaynow .text())
		numstudnow=str(self.ui.ennumberstudnow.text())
		db=sqlite3.connect(w)
		db.row_factory=sqlite3.Row
		if daynow=="Sat":

			sh=db.execute("select lunsh from tb1 where numberstudent='{}'and STR='{}'".format(numstudnow,"T"))
			for d in sh:
				if "L/Sat"==d['lunsh']:
					message=QtWidgets.QMessageBox.information(self,'information','<FONT size=10 color=blue>STOOP</FONT>')
				else:
					db.execute("update tb1 set lunsh='L/Sat' where numberstudent='{}'".format(numstudnow))
					db.commit()
		if daynow=="Sun":

			sh=db.execute("select lunsh from tb1 where numberstudent='{}'and SUN='{}'".format(numstudnow,"T"))
			for d in sh:
				if "L/Sun"==d['lunsh']:
					message=QtWidgets.QMessageBox.information(self,'information','<FONT size=10 color=blue>STOOP</FONT>')
				else:
					db.execute("update tb1 set lunsh='L/Sun' where numberstudent='{}'".format(numstudnow))
					db.commit()
		if daynow=="Mon":

			sh=db.execute("select lunsh from tb1 where numberstudent='{}'and MOU='{}'".format(numstudnow,"T"))
			for d in sh:
				if "L/Mon"==d['lunsh']:
					message=QtWidgets.QMessageBox.information(self,'information','<FONT size=10 color=blue>STOOP</FONT>')
				else:
					db.execute("update tb1 set lunsh='L/Mon' where numberstudent='{}'".format(numstudnow))
					db.commit()
		if daynow=="Tue":

			sh=db.execute("select lunsh from tb1 where numberstudent='{}'and TUS='{}'".format(numstudnow,"T"))
			for d in sh:
				if "L/Tue"==d['lunsh']:
					message=QtWidgets.QMessageBox.information(self,'information','<FONT size=10 color=blue>STOOP</FONT>')
				else:
					db.execute("update tb1 set lunsh='L/Tue' where numberstudent='{}'".format(numstudnow,))
					db.commit()
		if daynow=="Wed":

			sh=db.execute("select lunsh from tb1 where numberstudent='{}'and WED='{}'".format(numstudnow,"T"))
			for d in sh:
				if "L/Wed"==d['lunsh']:
					message=QtWidgets.QMessageBox.information(self,'information','<FONT size=10 color=blue>STOOP</FONT>')
				else:
					db.execute("update tb1 set lunsh='L/Wed' where numberstudent='{}'".format(numstudnow))
					db.commit()
		if daynow=="Thu":

			sh=db.execute("select lunsh from tb1 where numberstudent='{}'and THR='{}'".format(numstudnow,"T"))
			for d in sh:
				if "L/Thu"==d['lunsh']:
					message=QtWidgets.QMessageBox.information(self,'information','<FONT size=10 color=blue>STOOP</FONT>')
				else:
					db.execute("update tb1 set lunsh='L/Thu' where numberstudent='{}'".format(numstudnow))
					db.commit()
		if daynow=="Fri":

			sh=db.execute("select lunsh from tb1 where numberstudent='{}'and FRA='{}'".format(numstudnow,"T"))
			for d in sh:
				if "L/Fri"==d['lunsh']:
					message=QtWidgets.QMessageBox.information(self,'information','<FONT size=10 color=blue>STOOP</FONT>')
				else:
					db.execute("update tb1 set lunsh='L/Fri' where numberstudent='{}'".format(numstudnow))
					db.commit()
	def din(self):
		wikenow=str(self.ui.comwikdaynow.currentText())
		w=wikenow+".db"
		eatnow=str(self.ui.comtypeeta.currentText())
		daynow=str(self.ui.entodaynow .text())
		numstudnow=str(self.ui.ennumberstudnow.text())
		db=sqlite3.connect(w)
		db.row_factory=sqlite3.Row
		if daynow=="Sat":

			sh=db.execute("select dinner from tb1 where numberstudent='{}'and STR='{}'".format(numstudnow,"T"))
			for d in sh:
				if "D/Sat"==d['dinner']:
					message=QtWidgets.QMessageBox.information(self,'information','<FONT size=10 color=blue>STOOP</FONT>')
				else:
					db.execute("update tb1 set dinner='D/Sat' where numberstudent='{}'".format(numstudnow))
					db.commit()
		if daynow=="Sun":

			sh=db.execute("select dinner from tb1 where numberstudent='{}'and SUN='{}'".format(numstudnow,"T"))
			for d in sh:
				if "D/Sun"==d['dinner']:
					message=QtWidgets.QMessageBox.information(self,'information','<FONT size=10 color=blue>STOOP</FONT>')
				else:
					db.execute("update tb1 set dinner='D/Sun' where numberstudent='{}'".format(numstudnow))
					db.commit()
		if daynow=="Mon":

			sh=db.execute("select dinner from tb1 where numberstudent='{}'and MOU='{}'".format(numstudnow,"T"))
			for d in sh:
				if "D/Mon"==d['dinner']:
					message=QtWidgets.QMessageBox.information(self,'information','<FONT size=10 color=blue>STOOP</FONT>')
				else:
					db.execute("update tb1 set dinner='D/Mon' where numberstudent='{}'".format(numstudnow))
					db.commit()
		if daynow=="Tue":

			sh=db.execute("select dinner from tb1 where numberstudent='{}'and TUS='{}'".format(numstudnow,"T"))
			for d in sh:
				if "D/Tue"==d['dinner']:
					message=QtWidgets.QMessageBox.information(self,'information','<FONT size=10 color=blue>STOOP</FONT>')
				else:
					db.execute("update tb1 set dinner='D/Tue' where numberstudent='{}'".format(numstudnow))
					db.commit()
		if daynow=="Wed":

			sh=db.execute("select dinner from tb1 where numberstudent='{}'and WED='{}'".format(numstudnow,"T"))
			for d in sh:
				if "D/Wed"==d['dinner']:
					message=QtWidgets.QMessageBox.information(self,'information','<FONT size=10 color=blue>STOOP</FONT>')
				else:
					db.execute("update tb1 set dinner='D/Wed' where numberstudent='{}'".format(numstudnow))
					db.commit()
		if daynow=="Thu":

			sh=db.execute("select dinner from tb1 where numberstudent='{}'and THR='{}'".format(numstudnow,"T"))
			for d in sh:
				if "D/Thu"==d['dinner']:
					message=QtWidgets.QMessageBox.information(self,'information','<FONT size=10 color=blue>STOOP</FONT>')
				else:
					db.execute("update tb1 set dinner='D/Thu' where numberstudent='{}'".format(numstudnow))
					db.commit()
		if daynow=="Fri":

			sh=db.execute("select dinner from tb1 where numberstudent='{}'and FRA='{}'".format(numstudnow,"T"))
			for d in sh:
				if "D/Fri"==d['dinner']:
					message=QtWidgets.QMessageBox.information(self,'information','<FONT size=10 color=blue>STOOP</FONT>')
				else:
					db.execute("update tb1 set dinner='D/Fri' where numberstudent='{}'".format(numstudnow))
					db.commit()									

	def chickday(self):
		daynow=str(self.ui.entodaynow .text())
		if daynow=='Sat':
			self.strday()
		if daynow=='Sun':
			self.sunday()
		if daynow=='Mon':
			self.mouday()
		if daynow=='Tue':
			self.tusday()
		if daynow=='Wed':
			self.weday()
		if daynow=='Thu':
			self.thrday()
		if daynow=='Fri':
			self.fraday()
	def strday(self):
		daynow=str(self.ui.entodaynow .text())
		wikenow=str(self.ui.comwikdaynow.currentText())
		w=wikenow+".db"
		numstudnow=str(self.ui.ennumberstudnow.text())
		db=sqlite3.connect(w)
		db.row_factory=sqlite3.Row
		sh=db.execute("select STR from tb1 where numberstudent='{}'".format(numstudnow))
		for k in sh:
			if "T"!=k['STR']:
				
				db.execute('update tb1 set STR="T" where numberstudent="{}"'.format(numstudnow))
				db.commit()
	def sunday(self):
		daynow=str(self.ui.entodaynow .text())
		wikenow=str(self.ui.comwikdaynow.currentText())
		w=wikenow+".db"
		numstudnow=str(self.ui.ennumberstudnow.text())
		db=sqlite3.connect(w)
		db.row_factory=sqlite3.Row
		sh=db.execute("select SUN from tb1 where numberstudent='{}'".format(numstudnow))
		for k in sh:
			if "T"!=k['SUN']:
				db.execute('update tb1 set SUN="{}" where numberstudent="{}"'.format("T",numstudnow))
				db.commit()
	def mouday(self):
		daynow=str(self.ui.entodaynow .text())
		wikenow=str(self.ui.comwikdaynow.currentText())
		w=wikenow+".db"
		numstudnow=str(self.ui.ennumberstudnow.text())
		db=sqlite3.connect(w)
		db.row_factory=sqlite3.Row
		sh=db.execute("select MOU from tb1 where numberstudent='{}'".format(numstudnow))
		for k in sh:
			if "T"!=k['MOU']:
				db.execute('update tb1 set MOU="{}" where numberstudent="{}"'.format("T",numstudnow))
				db.commit()
	def tusday(self):
		daynow=str(self.ui.entodaynow .text())
		wikenow=str(self.ui.comwikdaynow.currentText())
		w=wikenow+".db"
		numstudnow=str(self.ui.ennumberstudnow.text())
		db=sqlite3.connect(w)
		db.row_factory=sqlite3.Row
		sh=db.execute("select TUS from tb1 where numberstudent='{}'".format(numstudnow))
		for k in sh:
			if "T"!=k['TUS']:
				db.execute('update tb1 set TUS="{}" where numberstudent="{}"'.format("T",numstudnow))
				db.commit()
	def weday(self):
		
		daynow=str(self.ui.entodaynow .text())
		wikenow=str(self.ui.comwikdaynow.currentText())
		w=wikenow+".db"
		numstudnow=str(self.ui.ennumberstudnow.text())
		db=sqlite3.connect(w)
		db.row_factory=sqlite3.Row
		sh=db.execute("select WED from tb1 where numberstudent='{}'".format(numstudnow))
		for k in sh:
			if "T"!=k['WED']:
				
				l="T"
				db=sqlite3.connect(w)
				db.row_factory=sqlite3.Row 
				db.execute('update tb1 set WED="T" where numberstudent="{}"'.format(numstudnow))
				db.commit()
				#db.execute("insert into tb1(WED) where numberstudent='{}'")
				
	def thrday(self):
		daynow=str(self.ui.entodaynow .text())
		wikenow=str(self.ui.comwikdaynow.currentText())
		w=wikenow+".db"
		numstudnow=str(self.ui.ennumberstudnow.text())
		db=sqlite3.connect(w)
		db.row_factory=sqlite3.Row
		sh=db.execute("select THR from tb1 where numberstudent='{}'".format(numstudnow))
		for k in sh:
			if "T"!=k['THR']:
				
				db.execute('update tb1 set THR="T" where numberstudent="{}"'.format(numstudnow))
				db.commit()
	def fraday(self):
		daynow=str(self.ui.entodaynow .text())
		wikenow=str(self.ui.comwikdaynow.currentText())
		w=wikenow+".db"
		numstudnow=str(self.ui.ennumberstudnow.text())
		db=sqlite3.connect(w)
		db.row_factory=sqlite3.Row
		sh=db.execute("select FRA from tb1 where numberstudent='{}'".format(numstudnow))
		for k in sh:
			if "T"!=k['FRA']:
				db.execute('update tb1 set FRA="{}" where numberstudent="{}"'.format("T",numstudnow))
				db.commit()																		
#######################################################tab1 finshed##############################################################
#####################################################tab2 start ##############################################################
	def searchname(self):
		g=str(self.ui.comtypesearch.currentText())
		nm=str(self.ui.comsarchnamestud.text())
		if g=='NAME STUDENT':
			db=sqlite3.connect('addnewstudent.db')
			db.row_factory=sqlite3.Row
			sh=db.execute("select * from tb1 where namstud like '%{}%'".format(nm))
			while self.ui.tableWidget_2.rowCount() >0:
				self.ui.tableWidget_2.removeRow(0)
			for rowindx,rowdata in enumerate(sh):
			 	self.ui.tableWidget_2.insertRow(rowindx)
			 	for colmindx,colmdata in enumerate(rowdata):
			 		self.ui.tableWidget_2.setItem(rowindx,colmindx,QtWidgets.QTableWidgetItem(str(colmdata)))						
	def typeser(self):
		g=str(self.ui.comtypesearch.currentText())
		if g=='NUMBER BLOCK':
			self.serBlock()
		elif g=='NUMBER ROOM':
			self.serroom()		 		

	def serBlock(self):
			nm=str(self.ui.comsearchnumberblock.currentText())
			db=sqlite3.connect('addnewstudent.db')
			db.row_factory=sqlite3.Row
			sh=db.execute("select * from tb1 where numblock like '%{}%'".format(nm))
			while self.ui.tableWidget_2.rowCount() >0:
				self.ui.tableWidget_2.removeRow(0)
			for rowindx,rowdata in enumerate(sh):
			 	self.ui.tableWidget_2.insertRow(rowindx)
			 	for colmindx,colmdata in enumerate(rowdata):
			 		self.ui.tableWidget_2.setItem(rowindx,colmindx,QtWidgets.QTableWidgetItem(str(colmdata)))
	def serroom(self):
			nm=str(self.ui.ensearchnumberroom.text())
			db=sqlite3.connect('addnewstudent.db')
			db.row_factory=sqlite3.Row
			sh=db.execute("select * from tb1 where numroom='{}'".format(nm))
			while self.ui.tableWidget_2.rowCount() >0:
				self.ui.tableWidget_2.removeRow(0)
			for rowindx,rowdata in enumerate(sh):
			 	self.ui.tableWidget_2.insertRow(rowindx)
			 	for colmindx,colmdata in enumerate(rowdata):
			 		self.ui.tableWidget_2.setItem(rowindx,colmindx,QtWidgets.QTableWidgetItem(str(colmdata)))		 		
		
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    myapp = NotePad()
    st="""QPushButton{border-radius:10px;border:2px solid white;background-color:rgb(84, 158, 255);}
    QPushButton:hover{background-color:green;border:2px solid red;}
    QLineEdit{background-color:white;border-radius:5px;}
    QLineEdit:hover{background-color:green;color:white;border:2px solid red;}
    QComboBox:hover{background-color:green;color:white;border:2px solid red;}
    QComboBox{border-radius:5px;}
    QListWidget:hover{background-color:green;color:white;border:2px solid red;}
    
    QLabel{border-radius:5px;border:2px solid white;}
    QMenu{border-radius:5px;border:2px solid white;}
    QMenuBar{border-radius:5px;border:2px solid white;}
    QMenuBar:hover{border-radius:5px;border:2px ridge red;background-color:#65CF5B;}
    """
    app.setStyleSheet(st)
myapp.show()
sys.exit(app.exec_())

