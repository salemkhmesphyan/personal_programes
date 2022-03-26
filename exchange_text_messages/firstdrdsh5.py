# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'firstdrdsh.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!
import mysql.connector
from set_program import NotePad1
from playsound import playsound
from PyQt5 import QtCore, QtGui, QtWidgets,QtPrintSupport
import sqlite3,threading
from datetime import date
from PyQt5.QtGui import *
import time
import datetime
import os,sys
global ee,ff1,noreq,mr_to,smam,tkr,nmsg,numdr,sound1,sound2,port
port="19871"
sound1,sound2=0,0
numdr=0
smam=0
nmsg=0
today = str(date.today())
myconn=mysql.connector.connect(
host="localhost",
user="root",
password="715653366",
database="dr1")
cb1=myconn.cursor()
cb1.execute('create table if not exists users(ID INT AUTO_INCREMENT PRIMARY KEY,namusr VARCHAR(20),pass VARCHAR(20),applest VARCHAR(30))')
cb1.execute('create table if not exists usersdrdsh(ID INT AUTO_INCREMENT PRIMARY KEY,namusr VARCHAR(20),nammr VARCHAR(20),time VARCHAR(30),date VARCHAR(20),drdsh VARCHAR(20),shrk VARCHAR(5))')
cb1.execute('create table if not exists frinds(ID INT AUTO_INCREMENT PRIMARY KEY,idus VARCHAR(5),idfrind VARCHAR(5),sho VARCHAR(5))')
myconn.commit()
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        #MainWindow.setStyleSheet("background:#300F3;")
        MainWindow.setWindowIcon(QtGui.QIcon("shar1.png"))
        MainWindow.setWindowTitle("pyqt5")
        MainWindow.resize(666, 524)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.page)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.frame = QtWidgets.QFrame(self.page)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setStyleSheet("font: 75 12pt \"Noto Sans\";")
        self.label.setObjectName("label")
       
        self.verticalLayout.addWidget(self.label)
        self.splitter = QtWidgets.QSplitter(self.frame)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.en_log_usern = QtWidgets.QLineEdit(self.splitter)
        self.en_log_usern.setObjectName("en_log_usern")
        self.label_2 = QtWidgets.QLabel(self.splitter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.splitter)
        self.splitter_2 = QtWidgets.QSplitter(self.frame)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.en_log_pass = QtWidgets.QLineEdit(self.splitter_2)
        self.en_log_pass.setObjectName("en_log_pass")
        self.label_3 = QtWidgets.QLabel(self.splitter_2)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.splitter_2)
        self.but_log = QtWidgets.QPushButton(self.frame)
        self.but_log.setObjectName("but_log")
        self.verticalLayout.addWidget(self.but_log)
        self.gridLayout_3.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.frame, 0, 0, 1, 1)
        self.frame_2 = QtWidgets.QFrame(self.page)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setStyleSheet("font: 75 12pt \"Noto Sans\";")
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.splitter_3 = QtWidgets.QSplitter(self.frame_2)
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName("splitter_3")
        self.en_add_user = QtWidgets.QLineEdit(self.splitter_3)
        self.en_add_user.setObjectName("en_add_user")
        self.label_5 = QtWidgets.QLabel(self.splitter_3)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.splitter_3)
        self.splitter_4 = QtWidgets.QSplitter(self.frame_2)
        self.splitter_4.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_4.setObjectName("splitter_4")
        self.en_add_pass = QtWidgets.QLineEdit(self.splitter_4)
        self.en_add_pass.setObjectName("en_add_pass")
        self.label_6 = QtWidgets.QLabel(self.splitter_4)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.splitter_4)
        self.but_add = QtWidgets.QPushButton(self.frame_2)
        self.but_add.setObjectName("but_add")
        self.verticalLayout_2.addWidget(self.but_add)
        self.gridLayout_4.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.frame_2, 1, 0, 1, 1)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.page_2)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.splitter_6 = QtWidgets.QSplitter(self.page_2)
        self.splitter_6.setOrientation(QtCore.Qt.Vertical)
        self.splitter_6.setObjectName("splitter_6")
        self.label_7 = QtWidgets.QLabel(self.splitter_6)
        self.label_7.setStyleSheet("font: 75 11pt \"Noto Sans\";")
        self.label_7.setObjectName("label_7")
        self.line = QtWidgets.QFrame(self.splitter_6)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.en_alluser_search = QtWidgets.QLineEdit(self.splitter_6)
        self.en_alluser_search.setObjectName("en_alluser_search")
        self.lis_alluser = QtWidgets.QListWidget(self.splitter_6)
        self.item= QtWidgets.QListWidgetItem()
        
        
        self.lis_alluser.setObjectName("lis_alluser")
        self.splitter_5 = QtWidgets.QSplitter(self.splitter_6)
        self.splitter_5.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_5.setObjectName("splitter_5")
        self.but_arsalrequest = QtWidgets.QPushButton(self.splitter_5)
        self.but_arsalrequest.setObjectName("but_arsalrequest")
        self.but_mraslh = QtWidgets.QPushButton(self.splitter_5)
        self.but_mraslh.setObjectName("but_mraslh")
        self.gridLayout_6.addWidget(self.splitter_6, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.page_3)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.splitter_7 = QtWidgets.QSplitter(self.page_3)
        self.splitter_7.setOrientation(QtCore.Qt.Vertical)
        self.splitter_7.setObjectName("splitter_7")
        self.label_8 = QtWidgets.QLabel(self.splitter_7)
        self.label_8.setObjectName("label_8")
        self.textEdi_drdsh = QtWidgets.QTextEdit(self.splitter_7)
        self.textEdi_drdsh.setReadOnly(True)
        self.textEdi_drdsh.setObjectName("textEdi_drdsh")
        self.layoutWidget = QtWidgets.QWidget(self.splitter_7)
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.but_go = QtWidgets.QPushButton(self.layoutWidget)
        self.but_go.setObjectName("but_go")
        self.horizontalLayout.addWidget(self.but_go)
        self.en_text_go = QtWidgets.QLineEdit(self.layoutWidget)
        self.en_text_go.setObjectName("en_text_go")
        self.horizontalLayout.addWidget(self.en_text_go)
        self.gridLayout_7.addWidget(self.splitter_7, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.page_4)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.splitter_8 = QtWidgets.QSplitter(self.page_4)
        self.splitter_8.setOrientation(QtCore.Qt.Vertical)
        self.splitter_8.setObjectName("splitter_8")
        self.label_9 = QtWidgets.QLabel(self.splitter_8)
        self.label_9.setStyleSheet("font: 75 12pt \"Noto Sans\";")
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.line_2 = QtWidgets.QFrame(self.splitter_8)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.en_req_ser = QtWidgets.QLineEdit(self.splitter_8)
        self.en_req_ser.setObjectName("en_req_ser")
        self.list_req_user = QtWidgets.QListWidget(self.splitter_8)
        self.list_req_user.setObjectName("list_req_user")
        self.layoutWidget1 = QtWidgets.QWidget(self.splitter_8)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.but_req_don = QtWidgets.QPushButton(self.layoutWidget1)
        self.but_req_don.setObjectName("but_req_don")
        self.horizontalLayout_2.addWidget(self.but_req_don)
        self.but_req_ok = QtWidgets.QPushButton(self.layoutWidget1)
        self.but_req_ok.setObjectName("but_req_ok")
        self.horizontalLayout_2.addWidget(self.but_req_ok)
        self.gridLayout_8.addWidget(self.splitter_8, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.page_5)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.splitter_9 = QtWidgets.QSplitter(self.page_5)
        self.splitter_9.setOrientation(QtCore.Qt.Vertical)
        self.splitter_9.setObjectName("splitter_9")
        self.label_10 = QtWidgets.QLabel(self.splitter_9)
        self.label_10.setStyleSheet("font: 75 12pt \"Noto Sans\";")
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.line_3 = QtWidgets.QFrame(self.splitter_9)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.en_frind = QtWidgets.QLineEdit(self.splitter_9)
        self.en_frind.setObjectName("en_frind")
        self.list_frind = QtWidgets.QListWidget(self.splitter_9)
        self.list_frind.setObjectName("list_frind")
        self.layoutWidget2 = QtWidgets.QWidget(self.splitter_9)
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.but_mov_frind = QtWidgets.QPushButton(self.layoutWidget2)
        self.but_mov_frind.setObjectName("but_mov_frind")
        self.horizontalLayout_3.addWidget(self.but_mov_frind)
        self.but_mrslh_frind = QtWidgets.QPushButton(self.layoutWidget2)
        self.but_mrslh_frind.setObjectName("but_mrslh_frind")
        self.horizontalLayout_3.addWidget(self.but_mrslh_frind)
        self.gridLayout_9.addWidget(self.splitter_9, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_5)
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setObjectName("page_6")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.page_6)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.frame_3 = QtWidgets.QFrame(self.page_6)
        self.frame_3.setStyleSheet("background-color:#22429C;")
        
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.label_11 = QtWidgets.QLabel(self.frame_3)
        self.label_11.setText("")
        self.label_11.setPixmap(QPixmap("shar1.png"))
        self.label_11.setScaledContents(True)
        self.label_11.setObjectName("label_11")
        self.gridLayout_11.addWidget(self.label_11, 0, 0, 1, 1)
        self.gridLayout_10.addWidget(self.frame_3, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_6)
        self.gridLayout.addWidget(self.stackedWidget, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
       
        self.m1=self.menubar.addMenu("file")
        
        self.m2=self.menubar.addMenu("help")
        #file
        self.actionAbout = QtWidgets.QAction(QIcon("printer.gif"),"طباعة المحادثة",MainWindow)
        self.actionAbout.setObjectName("print")
        self.actionsett = QtWidgets.QAction(QIcon("sett.PNG"),"الضبط",MainWindow)
        self.actionsett.setObjectName("setting")
        self.actionClose = QtWidgets.QAction(QIcon("close.png"),"اغلاق",MainWindow)
        self.actionClose.setObjectName("close")
        self.actionClose.setShortcut("Ctrl+C")
        self.m1.addAction(self.actionAbout)
        self.m1.addAction(self.actionsett)
        self.m1.addAction(self.actionClose)
        #help
        self.actioninst = QtWidgets.QAction(QIcon("instr.png"),"تعليمات",MainWindow)
        self.actioninst.setObjectName("inst")
        self.actionabout = QtWidgets.QAction(QIcon("help.png"),"حول البرنامج",MainWindow)
        self.actionabout.setObjectName("about")
        self.m2.addAction(self.actioninst)
        self.m2.addAction(self.actionabout)
        
        self.menubar.setGeometry(QtCore.QRect(0, 0, 666, 27))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.dockWidget = QtWidgets.QDockWidget(MainWindow)
        self.dockWidget.setObjectName("dockWidget")
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setStyleSheet("background-color:#7fb0b7;border:1px solid #624B4B;")
        
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.dockWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.but_alluser_m = QtWidgets.QPushButton(self.dockWidgetContents)
        self.but_alluser_m.setIcon(QIcon("frinds1.png"))
        self.but_alluser_m.setObjectName("but_alluser_m")
        self.gridLayout_2.addWidget(self.but_alluser_m, 0, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.dockWidgetContents)
        self.pushButton_2.setIcon(QIcon("em.png"))
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_2.addWidget(self.pushButton_2, 1, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.dockWidgetContents)
        self.pushButton_3.setIcon(QIcon("email.svg"))
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_2.addWidget(self.pushButton_3, 4, 0, 1, 1)
        self.but_out = QtWidgets.QPushButton(self.dockWidgetContents)
        self.but_out.setIcon(QIcon("defa.gif"))
        self.but_out.setObjectName("but_out")
        self.gridLayout_2.addWidget(self.but_out, 5, 0, 1, 1)
        self.but_requ_m = QtWidgets.QPushButton(self.dockWidgetContents)
        self.but_requ_m.setObjectName("but_requ_m")
        self.but_requ_m.setIcon(QIcon("req1.jpeg"))
        self.gridLayout_2.addWidget(self.but_requ_m, 2, 0, 1, 1)
        self.but_frinds = QtWidgets.QPushButton(self.dockWidgetContents)
        self.but_frinds.setObjectName("but_frinds")
        self.gridLayout_2.addWidget(self.but_frinds, 3, 0, 1, 1)
        self.dockWidget.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockWidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(5)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "برنامج الرسائل النصية"))
        
        self.label.setText(_translate("MainWindow", "تسجيل الدخول"))
        self.label.setPixmap(QPixmap("log.jpeg"))
        self.label.setScaledContents(True)
        self.label_2.setText(_translate("MainWindow", "اسم المستخدم:"))
        self.label_3.setText(_translate("MainWindow", "كلمة المرور:"))
        self.but_log.setText(_translate("MainWindow", "دخول"))
        self.but_log.setIcon(QIcon("login.jpeg"))
        self.label_4.setText(_translate("MainWindow", "اضافة حساب جديد"))
        self.label_4.setPixmap(QPixmap("add2.jpeg"))
        self.label_4.setScaledContents(True)
        self.label_5.setText(_translate("MainWindow", "اسم المستخدم:"))
        self.label_6.setText(_translate("MainWindow", "كلمة المرور:"))
        self.but_add.setText(_translate("MainWindow", "اضافة"))
        self.but_add.setIcon(QIcon("add5.png"))
        self.label_7.setText(_translate("MainWindow", "<h5 align=center>جميع المستخدمين</h5>"))
        self.label_7.setStyleSheet("font-size:20px;")
        self.but_arsalrequest.setText(_translate("MainWindow", "ارسال طلب صداقة"))
        self.but_mraslh.setText(_translate("MainWindow", "مراسلة "))
        self.label_8.setText(_translate("MainWindow", "لايوجد جديد"))
        self.label_8.setStyleSheet("font-size:20px;")
        self.but_go.setText(_translate("MainWindow", ""))
        self.but_go.setIcon(QIcon("go1.jpeg"))
        self.but_go.setStyleSheet("border-radius:5px;")
        self.label_9.setText(_translate("MainWindow", "طلبات الصداقة:"))
        self.label_9.setStyleSheet("font-size:20px;")
        self.but_req_don.setText(_translate("MainWindow", "رفض"))
        self.but_req_ok.setText(_translate("MainWindow", "قبول"))
        self.label_10.setText(_translate("MainWindow", "الاصدقاء"))
        self.label_10.setStyleSheet("font-size:20px;")
        self.but_mov_frind.setText(_translate("MainWindow", "حذف الصداقة"))
        self.but_mrslh_frind.setText(_translate("MainWindow", "مراسلة"))
        self.but_alluser_m.setText(_translate("MainWindow", "المستخدمين"))
        self.pushButton_2.setText(_translate("MainWindow", "الرسائل الجديدة"))
        self.pushButton_3.setText(_translate("MainWindow", "دردشات جديدة"))
        self.but_out.setText(_translate("MainWindow", "تسجيل الخروج"))
        self.but_requ_m.setText(_translate("MainWindow", "طلبات الصداقة"))
        self.but_frinds.setText(_translate("MainWindow", "الاصدقاء"))
        self.but_frinds.setIcon(QIcon("frinds2.jpeg"))

class NotePad(QtWidgets.QMainWindow):
	def __init__(self,x,parent=None):
		QtWidgets.QWidget.__init__(self, parent)#lambda:تضعها عند اسم الزر
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.ui.from2=x
		############################settings
		self.ui.from2.ui1.but_chang_user.clicked.connect(self.change_user)
		self.ui.from2.ui1.but_chang_pass.clicked.connect(self.change_pass)
		self.ui.from2.ui1.but_save_all.clicked.connect(self.ckset)
		###################################################################
		self.shomin()
		#self.icon()
		self.showalluser()
		self.shoreq()
		self.ui.lis_alluser.itemClicked.connect(self.choosser)
		self.ui.list_req_user.itemClicked.connect(self.choosreq)
		self.ui.list_frind.itemClicked.connect(self.choosfrind)
		self.ui.but_mraslh.clicked.connect(self.mraslh)
		self.ui.but_go.clicked.connect(self.go)
		self.ui.but_arsalrequest.clicked.connect(self.reqfrind)
		self.ui.but_requ_m.clicked.connect(self.shotabreq)
		self.ui.but_req_ok.clicked.connect(self.ok1)
		self.ui.but_alluser_m.clicked.connect(self.shoalluser)
		self.ui.but_frinds.clicked.connect(self.shofrinds)
		self.ui.but_mrslh_frind.clicked.connect(self.mraslh_for_frind)
		self.ui.but_mov_frind.clicked.connect(self.removfrind)
		self.ui.but_add.clicked.connect(self.adduser1)
		self.ui.but_log.clicked.connect(self.sing)
		self.ui.but_out.clicked.connect(self.logout)
		self.ui.pushButton_2.clicked.connect(self.shodr)
		self.ui.pushButton_3.clicked.connect(self.icon)
		self.ui.but_req_don.clicked.connect(self.ignorefrind)
		self.ui.en_alluser_search.textChanged.connect(self.searsh_user)
		self.ui.en_frind.textChanged.connect(self.search_frind)
		self.ui.en_text_go.returnPressed.connect(self.go)
		self.ui.actionClose.triggered.connect(self.ex)
		self.ui.actionabout.triggered.connect(self.about)
		self.ui.actionAbout.triggered.connect(self.printers)
		self.ui.actioninst.triggered.connect(self.helps)
		self.ui.actionsett.triggered.connect(self.showset)
		self.shofrind()
		self.ck()
	def ex(self):
		global tkr
		tkr=0
		self.destroy()
		sys.exit()
		
	def shotabreq(self):
		global smam
		self.ui.stackedWidget.setCurrentIndex(3)
		smam=0
		self.shoreq()
	def shoalluser(self):
		global tkr,smam
		tkr=1
		self.ui.stackedWidget.setCurrentIndex(1)
		self.showalluser()
		smam=0
	def shofrinds(self):
		global smam
		self.ui.stackedWidget.setCurrentIndex(4)
		smam=0
		self.shofrind()
	def sing(self):
		global tkr,smam
		smam=0
		n1= str(self.ui.en_log_usern.text())
		pa1= str(self.ui.en_log_pass.text())
		t=time.asctime(time.localtime(time.time()))
		myconn=mysql.connector.connect(
		host="localhost",
		user="root",
		password="715653366",
		database="dr1")
		cb=myconn.cursor()
		cb.execute("select namusr,pass from users where namusr='{}' and pass='{}'".format(n1,pa1))
		y=cb.fetchall()
		myconn.close()
		if len(y)>0:
			self.ui.stackedWidget.setCurrentIndex(5)
			gg=open(".us.text","w")
			gg.write(n1)
			gg.close()
			self.ui.but_alluser_m.setEnabled(True)
			self.ui.but_requ_m.setEnabled(True)
			self.ui.but_frinds.setEnabled(True)
			self.ui.but_out.setEnabled(True)
			self.ui.pushButton_2.setEnabled(True)
			self.ui.pushButton_3.setEnabled(True)
			
			self.stateuse()
			tkr=1
			self.chikmsg()
			
		else:
			self.ui.stackedWidget.setCurrentIndex(0)
			message=QtWidgets.QMessageBox.information(self,'information','<FONT size=10 color=blue>خطاء في طلمة المرور او المستخدم</FONT>')

		
	def adduser1(self):
		
		n1= str(self.ui.en_add_user.text())
		pa1= str(self.ui.en_add_pass.text())
		t=time.asctime(time.localtime(time.time()))
		myconn=mysql.connector.connect(
		host="localhost",
		user="root",
		password="715653366",
		database="dr1")
		cb=myconn.cursor()
		sql="INSERT INTO users (namusr,pass,applest) VALUES(%s, %s, %s)"
		value=(n1,pa1,str(t))
		cb.execute("select namusr from users where namusr='{}'".format(n1))
		y=cb.fetchall()
		#myconn.close()
		if len(y)==0:
			if (n1=="")or(pa1==""):
				message=QtWidgets.QMessageBox.information(self,'information','<FONT size=10 color=blue>لو سمحت املاء جميع الحقول</FONT>')
			else:	
				cb.execute(sql,value)
				myconn.commit()
				myconn.close()
				message=QtWidgets.QMessageBox.information(self,'information','<FONT size=10 color=blue>تم اضافة الحساب بنجاح</FONT>')
		else:
			message=QtWidgets.QMessageBox.information(self,'information','<FONT size=10 color=blue>للاسف الاسم موجود اختار اسم اخر</FONT>')
	def shomin(self):
		global tkr,smam
		
		#self.ui.stackedWidget.setCurrentIndex(5)
		
		e=os.path.exists(".us.text")
		if e==0:
			gg1=open(".us.text","w")
			#gg1.write(n1)
			gg1.close()

		gg=open(".us.text","r")
		tt=gg.read()
		gg.close()
		
		if tt.strip()=="":
			self.ui.stackedWidget.setCurrentIndex(0)
			self.ui.but_alluser_m.setEnabled(False)
			self.ui.pushButton_2.setEnabled(False)
			self.ui.pushButton_3.setEnabled(False)
			self.ui.but_requ_m.setEnabled(False)
			self.ui.but_frinds.setEnabled(False)
			self.ui.but_out.setEnabled(False)
			smam=0
		else:
			
			self.stateuse()
			self.ui.stackedWidget.setCurrentIndex(5)
			
			#self.ui.stackedWidget.setCurrentIndex(1)
			tkr=1
			self.chikmsg()
			smam=0
			
	def showalluser(self):
		global ee,ff1,noreq
		self.ui.lis_alluser.clear()
		noreq=[]
		ff1=[]
		ee=[]
		gg=open(".us.text","r")
		t1=gg.read()
		gg.close()
		myconn=mysql.connector.connect(
		host="localhost",
		user="root",
		password="715653366",
		database="dr1")
		cb=myconn.cursor()
		cb.execute("select ID from users where namusr='{}'".format(t1.strip()))
		frsh=cb.fetchall()
		#self.ui.list_req_user.clear()
		if len(frsh)>0:
			for g in frsh:
				d=g[0]
			
			cb.execute("select namusr from users u inner join frinds f on u.id=f.idfrind where f.idus='{}'and sho='0'".format(d))
			nofrind=cb.fetchall()#this is no frinds but wait down
			for x in nofrind:
				noreq.append(x[0])
			
			cb.execute("select u.id,namusr from users u inner join frinds f on u.id=f.idus where f.idfrind={} and sho='1'".format(d))
			frsh1=cb.fetchall()
			
			for y in frsh1:
				ee.append(y[0])
				ee.append(y[1])
		
				
		
		self.ui.en_alluser_search.clear()
		cb.execute("select * from users where not namusr='{}'".format(t1.strip()))
		frsh2=cb.fetchall()
		self.ui.but_alluser_m.setText("المستخدمين"+"\n"+str(len(frsh2)))
		for n in frsh2:
			ff1.append(n[1])
			if n[0] in ee:
				#self.ui.lis_alluser.insertItem(0,'{}>> \t frind'.format(n[1]))
				item = QtWidgets.QListWidgetItem()
				icon = QtGui.QIcon()
				icon.addPixmap(QtGui.QPixmap("avatar.png"), QtGui.QIcon.Selected, QtGui.QIcon.Off)
				item.setIcon(icon)
				item.setText('{}>> \t frind'.format(n[1]))
				self.ui.lis_alluser.addItem(item)
			else:
				#self.ui.lis_alluser.insertItem(0,'{}>> \t unfrind'.format(n[1]))
				item = QtWidgets.QListWidgetItem()
				icon = QtGui.QIcon()
				icon.addPixmap(QtGui.QPixmap("avatar.png"), QtGui.QIcon.Selected, QtGui.QIcon.Off)
				item.setIcon(icon)
				item.setText('{}>> \t unfrind'.format(n[1]))
				self.ui.lis_alluser.addItem(item)
				
	def choosser(self):#function choos username
		global ee
		item = self.ui.lis_alluser.currentItem()
		r=str(item.text())
		
		if "unfrind" in r:
			w=r.find(">>")
			w1=r[:w].strip()
		else:
			w=r.find(">>")
			w1=r[:w].strip()
			#print("frind")
		self.ui.en_alluser_search.setText(w1)
	def mraslh(self):
		global ee,mr_to,smam
		mrasl=str(self.ui.en_alluser_search.text())
		if mrasl in ee:
			
			self.ui.stackedWidget.setCurrentIndex(2)
			mr_to=mrasl
			smam=1
			self.upmsg()
			gg=open(".us.text","r")
			t=gg.read()
			gg.close()
			myconn=mysql.connector.connect(
			host="localhost",
			user="root",
			password="715653366",
			database="dr1")
			cb=myconn.cursor()
			cb.execute("select * from usersdrdsh where (namusr='{}' and nammr='{}')or(namusr='{}' and nammr='{}')".format(t.strip(),mrasl,mrasl,t.strip()))
			d=cb.fetchall()
			cb.execute("select applest from users where namusr='{}'".format(mrasl))
			e1=cb.fetchall()
			for x in e1:
				o1=x[0]
			
			self.ui.label_8.setText(mrasl+"\n"+o1)
			self.ui.textEdi_drdsh.clear()
			for n in d:
				if n[1]==t.strip():
					self.ui.textEdi_drdsh.append("<font color='blue' size=9><b>{}</b>::>{}</font>".format(n[1],n[5]))
				else:
					self.ui.textEdi_drdsh.append("<font color='green' size=9>{}//::<b>{}</b></font>".format(n[5],n[1]))
		else:message=QtWidgets.QMessageBox.information(self,'information','<FONT size=10 color=blue>لو سمحت ارسل طلب صداقة</FONT>')
	def go(self):
		
		gg=open(".us.text","r")
		t1=gg.read()
		gg.close()
		drr=str(self.ui.en_text_go.text())
		nam=self.ui.label_8.text()
		nam1=nam.find("\n")
		t=time.asctime(time.localtime(time.time()))
		x=datetime.datetime.now().hour
		s=datetime.datetime.now().minute
		a=datetime.datetime.now().second
		time1=str(str(x)+":"+str(s)+":"+str(a))
		myconn=mysql.connector.connect(
		host="localhost",
		user="root",
		password="715653366",
		database="dr1")
		cb=myconn.cursor()
		sql='insert into usersdrdsh(namusr,nammr,time,date,drdsh,shrk) values(%s,%s,%s,%s,%s,%s)'
		value=(t1.strip(),nam[:nam1],t,today,drr,"0")
		#cb.execute("insert into usersdrdsh(namusr,nammr,time,date,drdsh,shrk) values(?,?,?,?,?,?)",(t1.strip(),nam[:nam1],t,today,drr,"0"))
		cb.execute(sql,value)
		myconn.commit()
		self.ui.textEdi_drdsh.clear()
		self.ui.en_text_go.clear()
		
		cb.execute("select * from usersdrdsh where (namusr='{}' and nammr='{}')or(namusr='{}' and nammr='{}')".format(t1.strip(),nam[:nam1],nam[:nam1],t1.strip()))
		d=cb.fetchall()
		cb.execute("select applest from users where namusr='{}'".format(nam[:nam1]))
		e1=cb.fetchall()
		myconn.close()
		for x in e1:
			o1=x[0]
		self.ui.label_8.setText(nam[:nam1]+"\n"+o1)
		for n in d:
			if n[1]==t1.strip():
				#self.ui.textEdi_drdsh.append(n[2]+":--"+n[5]+"\n")
				self.ui.textEdi_drdsh.append("<font color='blue' size=9>{}::>{}</font>".format(n[1],n[5]))
			else:
				self.ui.textEdi_drdsh.append("<font color='green' size=9>{}//::{}</font>".format(n[5],n[1]))
	def reqfrind(self):
		global ee,ff1,noreq
		frind=str(self.ui.en_alluser_search.text())
		if frind in ff1:
			if frind in ee:
				pass
			else:
				if frind in noreq:
					message=QtWidgets.QMessageBox.information(self,'information','<FONT size=10 color=blue>طلب الصداقة موجود</FONT>')
				else:
					
					gg=open(".us.text","r")
					t1=gg.read()
					gg.close()
					
					myconn=mysql.connector.connect(
					host="localhost",
					user="root",
					password="715653366",
					database="dr1")
					cb=myconn.cursor()
					cb.execute("select * from users where namusr='{}' or namusr='{}'".format(t1.strip(),frind))
					frsh=cb.fetchall()
					for n in frsh:
						if n[1]==t1.strip():
							idus=n[0]
						else:
							idfrin=n[0]
					#cb.execute('create table if not exists frinds(ID integer primary Key autoincrement,idus text,idfrind text,sho text)')
					sql='insert into frinds(idus,idfrind,sho) values(%s,%s,%s)'
					value=(idus,idfrin,"0")
					cb.execute(sql,value)
					myconn.commit()
					message=QtWidgets.QMessageBox.information(self,'information','<FONT size=10 color=blue>تم ارسال الطلب بنجاح</FONT>')
		else:	message=QtWidgets.QMessageBox.information(self,'information','<FONT size=10 color=blue>غير معروف</FONT>')
	def shoreq(self):
		
		#streq=[]
		gg=open(".us.text","r")
		t1=gg.read()
		gg.close()
		myconn=mysql.connector.connect(
		host="localhost",
		user="root",
		password="715653366",
		database="dr1")
		cb=myconn.cursor()
		
		cb.execute("select ID from users where namusr='{}'".format(t1.strip()))
		frsh=cb.fetchall()
		self.ui.en_req_ser.clear()
		self.ui.list_req_user.clear()
		
		if len(frsh)>0:
			
			for g in frsh:
				d=g[0]
			cb.execute("select namusr from users u inner join frinds f on u.id=f.idus where f.idfrind={} and sho='0'".format(d))
			frsh1=cb.fetchall()
			self.ui.but_requ_m.setText("طلبات الصداقة"+"\n"+str(len(frsh1)))
			if frsh1==[]:
				self.ui.label_9.clear()
				self.ui.label_9.setText("طلبات الصداقة"+"لاتوجد طلبات صداقة:")
				#self.ui.list_req_user.insertItem(0,'{}'.format("لاتوجد طلبات صداقة"))
			else:
				for r in frsh1:
					item = QtWidgets.QListWidgetItem()
					icon = QtGui.QIcon()
					icon.addPixmap(QtGui.QPixmap("avatar.png"), QtGui.QIcon.Selected, QtGui.QIcon.Off)
					item.setIcon(icon)
					item.setText(r[0])
					self.ui.list_req_user.addItem(item)
					#self.ui.list_req_user.insertItem(0,'{}'.format(r[0]))
		else:
			pass
	def choosreq(self):#choos frinds from list
		item = self.ui.list_req_user.currentItem()
		r=str(item.text())
		self.ui.en_req_ser.setText(r)
	def ok1(self):
		
		frind=self.ui.en_req_ser.text()
		gg=open(".us.text","r")
		t1=gg.read()
		gg.close()
		myconn=mysql.connector.connect(
		host="localhost",
		user="root",
		password="715653366",
		database="dr1")
		cb=myconn.cursor()
		cb.execute("select * from users where namusr='{}' or namusr='{}'".format(t1.strip(),frind))
		frsh=cb.fetchall()
		if len(frsh)>1:
			print(len(frsh))
			for n in frsh:
				if n[1]==t1.strip():
					idus=n[0]
				else:
					idfrin=n[0]
			cb.execute("update frinds set sho='1' where idus={} and idfrind={}".format(idfrin,idus))
			sql='insert into frinds(idus,idfrind,sho) values(%s,%s,%s)'
			value=(idus,idfrin,"1")
			cb.execute(sql,value)
			myconn.commit()
			message=QtWidgets.QMessageBox.information(self,'information','<FONT size=10 color=blue>تم قبول الطلب</FONT>')
		else:
			message=QtWidgets.QMessageBox.information(self,'information','<FONT size=10 color=blue>غير معروف</FONT>')
	def shofrind(self):
		
		gg=open(".us.text","r")
		t1=gg.read()
		gg.close()
		myconn=mysql.connector.connect(
		host="localhost",
		user="root",
		password="715653366",
		database="dr1")
		cb=myconn.cursor()
		cb.execute("select ID from users where namusr='{}'".format(t1.strip()))
		frsh=cb.fetchall()
		self.ui.list_frind.clear()
		if len(frsh)>0:

			for g in frsh:
				d=g[0]
			cb.execute("select namusr from users u inner join frinds f on u.id=f.idus where f.idfrind={} and sho='1'".format(d))
			frsh1=cb.fetchall()
			self.ui.but_frinds.setText("الاصدقاء"+"\n"+str(len(frsh1)))
			if frsh1==[]:
				self.ui.label_10.setText(self.ui.label_9.text()+"لايوجد اصدقاء")
				#self.ui.list_req_user.insertItem(0,'{}'.format("لاتوجد طلبات صداقة"))
			else:
				for r in frsh1:
					item = QtWidgets.QListWidgetItem()
					icon = QtGui.QIcon()
					icon.addPixmap(QtGui.QPixmap("avatar.png"), QtGui.QIcon.Selected, QtGui.QIcon.Off)
					item.setIcon(icon)
					item.setText(r[0])
					self.ui.list_frind.addItem(item)
					#self.ui.list_frind.insertItem(0,'{}'.format(r[0]))
		else:
			pass
	def choosfrind(self):#choos frinds from list
		item = self.ui.list_frind.currentItem()
		r=str(item.text())
		self.ui.en_frind.setText(r)
	def mraslh_for_frind(self):
		
		mrasl=str(self.ui.en_frind.text())
		global ee,mr_to,smam
		if mrasl in ee:
			self.ui.stackedWidget.setCurrentIndex(2)
			smam=1
			mr_to=mrasl
			smam=1
			self.upmsg()
			gg=open(".us.text","r")
			t=gg.read()
			gg.close()
			myconn=mysql.connector.connect(
			host="localhost",
			user="root",
			password="715653366",
			database="dr1")
			
			cb=myconn.cursor()
			cb.execute("select * from usersdrdsh where (namusr='{}' and nammr='{}')or(namusr='{}' and nammr='{}')".format(t.strip(),mrasl,mrasl,t.strip()))
			d=cb.fetchall()
			cb.execute("select applest from users where namusr='{}'".format(mrasl))
			e1=cb.fetchall()
			for x in e1:
				o1=x[0]
			
			self.ui.label_8.setText(mrasl+"\n"+o1)
			self.ui.textEdi_drdsh.clear()
			for n in d:
				if n[1]==t.strip():
					self.ui.textEdi_drdsh.append("<font color='blue' size=9>{}::{}</font>".format(n[1],n[5]))
				else:
					self.ui.textEdi_drdsh.append("<font color='green' size=9>{}::{}</font>".format(n[5],n[1]))
		else:message=QtWidgets.QMessageBox.information(self,'information','<FONT size=10 color=blue>غير معروف</FONT>')
			
	def removfrind(self):
		
		frind=self.ui.en_frind.text()
		gg=open(".us.text","r")
		t1=gg.read()
		gg.close()
		myconn=mysql.connector.connect(
		host="localhost",
		user="root",
		password="715653366",
		database="dr1")
		cb=myconn.cursor()
		cb.execute("select * from users where namusr='{}' or namusr='{}'".format(t1.strip(),frind))
		frsh=cb.fetchall()
		if len(frsh)>1:
			
			for n in frsh:
				if n[1]==t1.strip():
					idus=n[0]
				else:
					idfrin=n[0]
			cb.execute("delete from frinds where idus={} and idfrind={} and sho='1'".format(idfrin,idus))
			cb.execute("delete from frinds where idus={} and idfrind={} and sho='1'".format(idus,idfrin))
			myconn.commit()
			self.ui.en_frind.clear()
			self.ui.list_frind.clear()
			self.shofrind()
			message=QtWidgets.QMessageBox.information(self,'information','<FONT size=10 color=blue>تم حذف الصداقة بنجاح</FONT>')
		else:
			message=QtWidgets.QMessageBox.information(self,'information','<FONT size=10 color=blue>غير معروف</FONT>')
	def logout(self):
		global tkr
		message=QtWidgets.QMessageBox.question(self,'question',"<font size=8>هل انتة متاكد من تسجيل الخروج من هذا الحساب</font>")
		if message==QtWidgets.QMessageBox.Yes:
			tkr=0
			self.ui.stackedWidget.setCurrentIndex(0)
			os.remove(".us.text")
			self.ui.but_alluser_m.setEnabled(False)
			self.ui.pushButton_2.setEnabled(False)
			self.ui.pushButton_3.setEnabled(False)
			self.ui.but_requ_m.setEnabled(False)
			self.ui.but_frinds.setEnabled(False)
			self.ui.but_out.setEnabled(False)
			message=QtWidgets.QMessageBox.information(self,'information','<FONT size=10 color=blue>تم تسجيل الخروج بنجاح</FONT>')
		else:
			pass
			
	def stateuse(self):
		
		gg=open(".us.text","r")
		t1=gg.read()
		gg.close()
		if t1.strip()=="":
			pass
		else:
			myconn=mysql.connector.connect(
			host="localhost",
			user="root",
			password="715653366",
			database="dr1")
			cb=myconn.cursor()
			cb.execute("update users set applest='{}' where namusr='{}'".format("متصل",t1.strip()))
			myconn.commit()
	def closeEvent(self, event):
		global tkr
		
		if True:
			t=time.asctime(time.localtime(time.time()))
			e=os.path.exists(".us.text")
			if e==1:
				gg=open(".us.text","r")
				t1=gg.read()
				gg.close()
				if t1.strip()=="":
					pass
				else:
					tkr=0
					myconn=mysql.connector.connect(
					host="localhost",
					user="root",
					password="715653366",
					database="dr1")
					cb=myconn.cursor()
					cb.execute("update users set applest='{}' where namusr='{}'".format(str(t),t1.strip()))
					myconn.commit()
	def upmsg(self):
		global mr_to
		gg=open(".us.text","r")
		t1=gg.read()
		gg.close()
		myconn=mysql.connector.connect(
		host="localhost",
		user="root",
		password="715653366",
		database="dr1")
		cb=myconn.cursor()
		cb.execute("update usersdrdsh set shrk='1' where nammr='{}' and namusr='{}' and shrk='0'".format(t1.strip(),mr_to))
		myconn.commit()
		myconn.close()
	def chikmsg(self):
		global smam,tkr,nmsg,numdr,sound1,sound2
		rk='0'
		
		if tkr==1:
			gg=open(".us.text","r")
			t1=gg.read()
			gg.close()
			myconn=mysql.connector.connect(
			host="localhost",
			user="root",
			password="715653366",
			database="dr1")
			cb9=myconn.cursor()
			cb9.execute("select * from usersdrdsh where shrk='0' and nammr='{}'".format(t1.strip()))
			vmsg=cb9.fetchall()
			if len(vmsg)>0:
				sound1=len(vmsg)
				gs1=[]
				numdr=1
				rk=str(len(vmsg))
				nam=self.ui.label_8.text()
				nam1=nam.find("\n")
				if smam==1:
					cb9.execute("select applest from users where namusr='{}'".format(nam[:nam1].strip()))
					e1=cb9.fetchall()
					myconn.close()
					for x in e1:
						o1=x[0]
					self.ui.label_8.setText(nam[:nam1].strip()+"\n"+o1)
					gs2=[]
					nam=self.ui.label_8.text()
					nam1=nam.find("\n")
					y5=nam[:nam1].strip()
					
					for n in vmsg:
						gs2.append(n[1])
					if y5 in gs2:
						nmsg=1
						self.ui.pushButton_2.setText("الرسائل الجديدة"+"\n"+rk)
				else:
					#self.ui.pushButton_2.setText("الدردشات الجديد"+"\n"+rk)
					nmsg=0
				if sound1==sound2:
					pass
				else:
					playsound("2.mp3",block=False)##########################sound
					sound2=sound1
				
				nummsg=len(vmsg)
				self.ui.pushButton_3.setText("الدردشات الجديدة"+"\n"+str(nummsg))
			else:
				nmsg=0
				
				self.ui.pushButton_2.setText("الرسائل الجديدة"+"\n"+rk)
				self.ui.pushButton_3.setText("الدردشات الجديدة"+"\n"+"0")
				numdr=0
				nam=self.ui.label_8.text()
				nam1=nam.find("\n")
				if smam==1:
					myconn=mysql.connector.connect(
					host="localhost",
					user="root",
					password="715653366",
					database="dr1")
					cb=myconn.cursor()
					cb.execute("select applest from users where namusr='{}'".format(nam[:nam1].strip()))
					e1=cb.fetchall()
					if len(e1)>0:
						for x in e1:
							o2=x[0]
						self.ui.label_8.setText(nam[:nam1].strip()+"\n"+o2)
			
			
			threading.Timer(1, self.chikmsg).start()
		else:
			pass
	def shodr(self):
		global nmsg
		if nmsg==1:
			nam=self.ui.label_8.text()
			nam1=nam.find("\n")
			y5=nam[:nam1].strip()
			self.ui.en_frind.setText(y5)
			self.mraslh_for_frind()
	def ignorefrind(self):#ignor requst frindes
		frind=self.ui.en_req_ser.text()
		gg=open(".us.text","r")
		t1=gg.read()
		gg.close()
		myconn=mysql.connector.connect(
		host="localhost",
		user="root",
		password="715653366",
		database="dr1")
		cb=myconn.cursor()
		cb.execute("select * from users where namusr='{}' or namusr='{}'".format(t1.strip(),frind))
		frsh=cb.fetchall()
		if len(frsh)>1:
			
			for n in frsh:
				if n[1]==t1.strip():
					idus=n[0]
				else:
					idfrin=n[0]
			cb.execute("delete from frinds where idus={} and idfrind={} and sho='0'".format(idfrin,idus))
			
			myconn.commit()
			self.ui.en_req_ser.clear()
			self.ui.list_req_user.clear()
			self.shofrind()
			message=QtWidgets.QMessageBox.information(self,'information','<FONT size=10 color=blue>تم رفض الطلب</FONT>')
		else:
			message=QtWidgets.QMessageBox.information(self,'information','<FONT size=10 color=blue>غير معروف</FONT>')
	def icon(self):
		global numdr
		if numdr==1:
			sh=[]
			gg=open(".us.text","r")
			t1=gg.read()
			gg.close()
			sh.append("")
			myconn=mysql.connector.connect(
			host="localhost",
			user="root",
			password="715653366",
			database="dr1")
			cb=myconn.cursor()
			cb.execute("select * from usersdrdsh where shrk='0' and nammr='{}'".format(t1.strip()))
			vmsg=cb.fetchall()
			for n in vmsg:
				sh.append(n[1])
			ok = QtWidgets.QInputDialog.getItem(self,"قائمة المراسلين","اختار المستخدم المراد مراسلتة",sh,0,False)
			if ok=="":
				pass
			else:
				
				self.ui.en_frind.setText(ok[0])
				self.mraslh_for_frind()
###################################################################################searcher
	def searsh_user(self):
		global ee,ff1
		gg=open(".us.text","r")
		t1=gg.read()
		gg.close()
		nuser=self.ui.en_alluser_search.text()
		self.ui.lis_alluser.clear()
		myconn=mysql.connector.connect(
		host="localhost",
		user="root",
		password="715653366",
		database="dr1")
		cb=myconn.cursor()
		cb.execute("select * from users where not namusr='{}' and namusr like '%{}%' ".format(t1.strip(),nuser))
		frsh2=cb.fetchall()
		for n in frsh2:
			ff1.append(n[1])
			if n[0] in ee:
				#self.ui.lis_alluser.insertItem(0,'{}>> \t frind'.format(n[1]))
				item = QtWidgets.QListWidgetItem()
				icon = QtGui.QIcon()
				icon.addPixmap(QtGui.QPixmap("avatar.png"), QtGui.QIcon.Selected, QtGui.QIcon.Off)
				item.setIcon(icon)
				item.setText('{}>> \t frind'.format(n[1]))
				self.ui.lis_alluser.addItem(item)
			else:
				#self.ui.lis_alluser.insertItem(0,'{}>> \t unfrind'.format(n[1]))
				item = QtWidgets.QListWidgetItem()
				icon = QtGui.QIcon()
				icon.addPixmap(QtGui.QPixmap("avatar.png"), QtGui.QIcon.Selected, QtGui.QIcon.Off)
				item.setIcon(icon)
				item.setText('{}>> \t unfrind'.format(n[1]))
				self.ui.lis_alluser.addItem(item)
	def search_frind(self):
		
		nfrind=str(self.ui.en_frind.text())
		gg=open(".us.text","r")
		t1=gg.read()
		gg.close()
		myconn=mysql.connector.connect(
		host="localhost",
		user="root",
		password="715653366",
		database="dr1")
		cb1=myconn.cursor()
		cb1.execute("select ID from users where namusr='{}'".format(t1.strip()))
		frsh=cb1.fetchall()
		self.ui.list_frind.clear()
		if len(frsh)>0:
			for g in frsh:
				d=g[0]
			cb1.execute("select namusr from users u inner join frinds f on u.id=f.idus where f.idfrind={} and sho='1' and u.namusr like '%{}%' ".format(d,nfrind))
			frsh1=cb1.fetchall()
			for r in frsh1:
				item = QtWidgets.QListWidgetItem()
				icon = QtGui.QIcon()
				icon.addPixmap(QtGui.QPixmap("avatar.png"), QtGui.QIcon.Selected, QtGui.QIcon.Off)
				item.setIcon(icon)
				item.setText(r[0])
				self.ui.list_frind.addItem(item)
				#self.ui.list_frind.insertItem(0,'{}'.format(r[0]))
		else:
			pass	
				
#################################################tool bar##########################3
	
	def about(self):
		s="""
		تم البرمجة بواسطة المهندس 
		سالم خميس بهيان
		
		"""			
		message=QtWidgets.QMessageBox.about(self,'Defloper',s)
	def printers(self):
		if self.ui.textEdi_drdsh.toPlainText()=="":
			message=QtWidgets.QMessageBox.warning(self,'warning',"لاتوجد اي محادثة")
		else:
			printer =QtPrintSupport.QPrintDialog()
			if printer.exec_() == QtWidgets.QDialog.Accepted:
				self.ui.textEdi_drdsh.document().print_(printer.printer())
				printer.exec_()
	def helps(self):
		s="""
		this step when open first program:
		1-if enter first time sign up becuese
		 create account then login.
		2-Add frinds to frinds list by sending 
		friendship request from users. 
		"""
		message=QtWidgets.QMessageBox.information(self,'information',"<font size=8>{}</font>".format(s))
#####################################################3settings3##############################################
#############################################################################################################
	def showset(self):#functin show form set
		self.ui.from2.show()
	def change_user(self):
		global tkr
		usold=str(self.ui.from2.ui1.en_user_old.text())
		usnew=str(self.ui.from2.ui1.en_user_new.text())
		
		if tkr==1:
			gg=open(".us.text","r")
			t1=gg.read()
			gg.close()
			myconn=mysql.connector.connect(
			host="localhost",
			user="root",
			password="715653366",
			database="dr1")
			cb1=myconn.cursor()
			cb1.execute("select namusr from users where namusr='{}'".format(t1.strip()))
			frsh1=cb1.fetchall()
			cb1.execute("select namusr from users where namusr='{}'".format(usnew))
			frsh2=cb1.fetchall()
			if len(frsh1)>0:
				if len(frsh2)==0:
					if usnew=="":
						message=QtWidgets.QMessageBox.information(self,'information','<FONT size=10 color=blue>لو سمحت املاء جميع الحقول</FONT>')
					else:
						
						cb1.execute("update users set namusr='{}' where namusr='{}'".format(usnew,t1.strip()))
						cb1.execute("update usersdrdsh set namusr='{}' where namusr='{}'".format(usnew,t1.strip()))
						cb1.execute("update usersdrdsh set nammr='{}' where nammr='{}'".format(usnew,t1.strip()))
						myconn.commit()
						gg=open(".us.text","w")
						gg.write(usnew)
						gg.close()
						message=QtWidgets.QMessageBox.information(self,'information',"<font size=8>تم تغيير الاسم بنجاح</font>")
				else:
					message=QtWidgets.QMessageBox.information(self,'information',"<font size=8>الاسم موجود الرجاء اختار اسم اخر</font>")
			else:
				message=QtWidgets.QMessageBox.information(self,'information',"<font size=8>اسم المستخدم الذي ادخلتة غير موجود</font>")	
	def change_pass(self):
		global tkr
		passold=str(self.ui.from2.ui1.en_pass_old.text())
		passnew=str(self.ui.from2.ui1.en_pass_new.text())
		if tkr==1:
			gg=open(".us.text","r")
			t1=gg.read()
			gg.close()
			myconn=mysql.connector.connect(
			host="localhost",
			user="root",
			password="715653366",
			database="dr1")
			cb1=myconn.cursor()
			cb1.execute("select namusr,pass from users where namusr='{}' and pass='{}'".format(t1.strip(),passold))
			frsh1=cb1.fetchall()
			if len(frsh1)>0:
				if passnew=="":
					message=QtWidgets.QMessageBox.information(self,'information','<FONT size=10 color=blue>لو سمحت املاء جميع الحقول</FONT>')
				else:
					cb1.execute("update users set pass='{}' where namusr='{}' and pass='{}'".format(passnew,t1.strip(),passold))
					myconn.commit()				
					message=QtWidgets.QMessageBox.information(self,'information',"<font size=8>تم تغيير كلمة المرور بنجاح</font>")
			else:
				message=QtWidgets.QMessageBox.information(self,'information',"<font size=8>كلمة المرور التي ادخلتها غير صحيحية</font>")	
		
	def ck(self):
		stst=[]
		db1=sqlite3.connect("set_drdsh")
		cb1=db1.cursor()
		cb1.execute("select * from set1 ")
		frsh1=cb1.fetchall()
		for n in frsh1:
			stst.append(n[1])
			stst.append(n[2])
			stst.append(n[3])
			stst.append(n[4])
		st="""QPushButton{border-radius:10px;border:2px solid white;background-color:#040776;font-size:20px;}
		QPushButton:hover{background-color:#040776;border:2px solid #00071f;color:#452659;font-size:15px;}
		QLineEdit{background-color:white;font-size:13px;border-radius:5px;border:2px solid white;}
		QLineEdit:hover{background-color:#5D5753;color:white;border:2px solid red;}
		
		QComboBox{background-color:white;font-size:13px;border-radius:5px;border:2px solid white;}
		QListWidget:hover{background-color:#5D5753;color:#120600;border:2px solid #DD652B;}
		QTextEdit{background-color:#EADBBC;}
		QWidget{background-color:#452659;color:white;font-family:KacstQurn,Suruma;}
		QListWidget{border:2px solid #624B4B;font-size:13px;}
		
		QLabel{border-radius:5px;border:1px solid white;background-color:#8d68aa;}
		QMenu{border-radius:5px;border:2px solid white;}
		QMenuBar{border-radius:5px;border:2px solid white;}
		QMenuBar:hover{border-radius:5px;border:2px ridge red;background-color:#65CF5B;}"""
		night="""QPushButton{border-radius:10px;border:2px solid #624B4B;background-color:rgb(84, 158, 255);font-size:20px;}
		QPushButton:hover{background-color:#588C56;border:2px solid green;color:#495370;font-size:15px;}
		QLineEdit{background-color:#588C56;font-size:20px;border-radius:5px;border:2px solid #624B4B;}
		QLineEdit:hover{background-color:#97DE94;color:black;border:2px solid #624B4B;}
		
		QComboBox{background-color:white;font-size:13px;border-radius:5px;border:2px solid white;}
		QListWidget:hover{background-color:#97DE94;color:white;border:2px solid #588C56;}
		QListWidget{border:2px solid #624B4B;font-size:13px;}
		QTextEdit{background-color:#EADBBC;}
		QWidget{background-color:#8A9BCA;color:black;font-family:KacstQurn,Suruma;}
		QLabel{border-radius:5px;border:2px solid #624B4B;}
		QMenu{border-radius:5px;border:2px solid white;}
		QMenuBar{border-radius:5px;border:2px solid #624B4B;}
		QMenuBar:hover{border-radius:5px;border:2px ridge red;background-color:#7fb0b7;}"""
		if stst[0]=='0':
			app.setStyleSheet(night)
			self.ui.from2.ui1.radio_nourmal.setChecked(True)
			#self.ui.from2.ui1.radio_dark.setChecked(False)
		else:
			self.ui.from2.ui1.radio_dark.setChecked(True)
			#self.ui.from2.ui1.radio_nourmal.setChecked(False)
			app.setStyleSheet(st)
		self.ui.from2.ui1.spin_drdsh.setValue(int(stst[1]))
		self.ui.from2.ui1.spin_list.setValue(int(stst[2]))
		self.ui.from2.ui1.spin_text_search.setValue(int(stst[3]))
		set_size="QTextEdit{font-size:"+str(stst[1])+"px;}QListWidget{font-size:"+str(stst[2])+"px;}QLineEdit{font-size:"+str(stst[3])+"px;}"
		self.ui.centralwidget.setStyleSheet(set_size)
	def ckset(self):
		db1=sqlite3.connect("set_drdsh")
		cb1=db1.cursor()
		setvs1=str(self.ui.from2.ui1.spin_drdsh.value())
		setvs2=str(self.ui.from2.ui1.spin_list.value())
		setvs3=str(self.ui.from2.ui1.spin_text_search.value())
		if self.ui.from2.ui1.radio_nourmal.isChecked()==True:
			cb1.execute("update set1 set nourm_night='0',size_drdsh='{}',size_list='{}',size_line='{}' where id=1".format(setvs1,setvs2,setvs3))
			db1.commit()
		else:
			cb1.execute("update set1 set nourm_night='1',size_drdsh='{}',size_list='{}',size_line='{}' where id=1".format(setvs1,setvs2,setvs3))
			db1.commit()
		self.ck()	
			
			
			
			
	
	
		
if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	sett=NotePad1()
	myapp = NotePad(sett)
	
	st="""QPushButton{border-radius:10px;border:2px solid white;background-color:#040776;font-size:20px;}
	QPushButton:hover{background-color:#040776;border:2px solid #00071f;color:#452659;font-size:15px;}
	QLineEdit{background-color:white;font-size:13px;border-radius:5px;border:2px solid white;}
	QLineEdit:hover{background-color:#5D5753;color:white;border:2px solid red;}
	QComboBox:hover{background-color:green;color:white;border:2px solid red;}
	QComboBox{border-radius:5px;}
	QListWidget:hover{background-color:#5D5753;color:#120600;border:2px solid #DD652B;}
	QTextEdit{background-color:#EADBBC;text-align:center;}
	QWidget{background-color:#452659;color:white;font-family:KacstQurn,Suruma;}
	QListWidget{border:2px solid #624B4B;font-size:13px;}
	
	QLabel{border-radius:5px;border:1px solid white;background-color:#8d68aa;}
	QMenu{border-radius:5px;border:2px solid white;}
	QMenuBar{border-radius:5px;border:2px solid white;}
	QMenuBar:hover{border-radius:5px;border:2px ridge red;background-color:#65CF5B;}"""
	night="""QPushButton{border-radius:10px;border:2px solid #624B4B;background-color:rgb(84, 158, 255);font-size:20px;}
	QPushButton:hover{background-color:#588C56;border:2px solid green;color:#495370;font-size:15px;}
	QLineEdit{background-color:#588C56;font-size:20px;border-radius:5px;border:2px solid #624B4B;}
	QLineEdit:hover{background-color:#97DE94;color:black;border:2px solid #624B4B;}
	QComboBox:hover{background-color:green;color:white;border:2px solid #624B4B;}
	QComboBox{border-radius:5px;}
	QListWidget:hover{background-color:#97DE94;color:white;border:2px solid #588C56;}
	QListWidget{border:2px solid #624B4B;font-size:13px;}
	QTextEdit{background-color:#EADBBC;text-align:center;}
	QWidget{background-color:#8A9BCA;color:black;font-family:KacstQurn,Suruma;}
	QLabel{border-radius:5px;border:2px solid #624B4B;}
	QMenu{border-radius:5px;border:2px solid white;}
	QMenuBar{border-radius:5px;border:2px solid #624B4B;}
	QMenuBar:hover{border-radius:5px;border:2px ridge red;background-color:#7fb0b7;}"""
	#app.setStyleSheet(night)
	myapp.show()

	sys.exit(app.exec_())

