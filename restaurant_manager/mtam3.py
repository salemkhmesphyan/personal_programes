# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mtam1.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets,QtPrintSupport
from datetime import date
from PyQt5.QtCore import (QObject, QPointF, 
        QPropertyAnimation, pyqtProperty)
import time
import datetime
import sqlite3
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(845, 593)
        #MainWindow.resize(145, 93)
        self.anim = QPropertyAnimation(MainWindow, b'pos')
        self.anim.setDuration(2000)
        self.anim.setStartValue(QPointF(1, 100))
       
        self.anim.setEndValue(QPointF(200, 100))
        self.anim.start()
        MainWindow.setProperty('name','t8')
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setProperty('name','t1')
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.stackedWidget.setProperty('name','t3')
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.page.setProperty('name','t2')
        self.gridLayout_3 = QtWidgets.QGridLayout(self.page)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.splitter_2 = QtWidgets.QSplitter(self.page)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.pagmcompric = QtWidgets.QLineEdit(self.splitter_2)
        #self.pagmcompric.setEditable(True)
        self.pagmcompric.setObjectName("pagmcompric")
        self.label_3 = QtWidgets.QLabel(self.splitter_2)
        self.label_3.setObjectName("label_3")
        self.pagmqmi = QtWidgets.QComboBox(self.splitter_2)
        self.pagmqmi.setEditable(True)
        self.pagmqmi.setObjectName("pagmqmi")
        self.label_4 = QtWidgets.QLabel(self.splitter_2)
        self.label_4.setObjectName("label_4")
        self.pagmcomnameeat = QtWidgets.QComboBox(self.splitter_2)
        self.pagmcomnameeat.setEditable(True)
        self.pagmcomnameeat.setObjectName("pagmcomnameeat")
        self.label_2 = QtWidgets.QLabel(self.splitter_2)
        self.label_2.setObjectName("label_2")
        self.pagmcomtypemeal = QtWidgets.QComboBox(self.splitter_2)
        self.pagmcomtypemeal.setObjectName("pagmcomtypemeal")
        self.pagmcomtypemeal.addItem("")
        self.pagmcomtypemeal.addItem("")
        self.pagmcomtypemeal.addItem("")
        self.label = QtWidgets.QLabel(self.splitter_2)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.splitter_2)
        self.splitter_3 = QtWidgets.QSplitter(self.page)
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName("splitter_3")
        self.pagmcomprin = QtWidgets.QPushButton(self.splitter_3)
        self.pagmcomprin.setObjectName("pagmcomprin")
        self.pagmcomnewfile = QtWidgets.QPushButton(self.splitter_3)
        self.pagmcomnewfile.setObjectName("pagmcomnewfile")
        self.verticalLayout.addWidget(self.splitter_3)
        self.textEdit1 = QtWidgets.QTextEdit(self.page)
        self.textEdit1.setObjectName("textEdit1")
        self.verticalLayout.addWidget(self.textEdit1)
        self.gridLayout_3.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.page_3.setProperty('name','t5')
        self.gridLayout_5 = QtWidgets.QGridLayout(self.page_3)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.tabWidget = QtWidgets.QTabWidget(self.page_3)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setProperty('name','t6')

        self.tab.setObjectName("tab")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.t1comdateftor = QtWidgets.QComboBox(self.tab)
        self.t1comdateftor.setEditable(True)
        self.t1comdateftor.setObjectName("t1comdateftor")
        self.horizontalLayout.addWidget(self.t1comdateftor)
        self.label_15 = QtWidgets.QLabel(self.tab)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout.addWidget(self.label_15)
        self.t1comnumfator = QtWidgets.QComboBox(self.tab)
        self.t1comnumfator.setEditable(True)
        self.t1comnumfator.setObjectName("t1comnumfator")
        self.horizontalLayout.addWidget(self.t1comnumfator)
        self.label_14 = QtWidgets.QLabel(self.tab)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout.addWidget(self.label_14)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.t1butdateftor = QtWidgets.QPushButton(self.tab)
        self.t1butdateftor.setObjectName("t1butdateftor")
        self.horizontalLayout_2.addWidget(self.t1butdateftor)
        self.t1butprint = QtWidgets.QPushButton(self.tab)
        self.t1butprint.setObjectName("t1butprint")
        self.horizontalLayout_2.addWidget(self.t1butprint)
        self.t1butnumberftor = QtWidgets.QPushButton(self.tab)
        self.t1butnumberftor.setObjectName("t1butnumberftor")
        self.horizontalLayout_2.addWidget(self.t1butnumberftor)
        self.t1butshonumfto = QtWidgets.QPushButton(self.tab)
        self.t1butshonumfto.setObjectName("t1butshonumfto")
        self.horizontalLayout_2.addWidget(self.t1butshonumfto)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.textEdit3 = QtWidgets.QTextEdit(self.tab)
        self.textEdit3.setObjectName("textEdit3")
        self.verticalLayout_5.addWidget(self.textEdit3)
        self.gridLayout_6.addLayout(self.verticalLayout_5, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tab_2.setProperty('name','t7')
        self.gridLayout_7 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.t2comsnfher = QtWidgets.QComboBox(self.tab_2)
        self.t2comsnfher.setEditable(True)
        self.t2comsnfher.setObjectName("t2comsnfher")
        self.horizontalLayout_3.addWidget(self.t2comsnfher)
        self.label_18 = QtWidgets.QLabel(self.tab_2)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_3.addWidget(self.label_18)
        self.t2comchonumftor = QtWidgets.QComboBox(self.tab_2)
        self.t2comchonumftor.setEditable(True)
        self.t2comchonumftor.setObjectName("t2comchonumftor")
        self.horizontalLayout_3.addWidget(self.t2comchonumftor)
        self.label_17 = QtWidgets.QLabel(self.tab_2)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_3.addWidget(self.label_17)
        self.verticalLayout_6.addLayout(self.horizontalLayout_3)
        self.line = QtWidgets.QFrame(self.tab_2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_6.addWidget(self.line)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.t2butshomodfi = QtWidgets.QPushButton(self.tab_2)
        self.t2butshomodfi.setObjectName("t2butshomodfi")
        self.horizontalLayout_4.addWidget(self.t2butshomodfi)
        self.label_16 = QtWidgets.QLabel(self.tab_2)
        self.label_16.setStyleSheet("font: 75 12pt \"Noto Sans\";")
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_4.addWidget(self.label_16)
        self.verticalLayout_6.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.t2butmodfisnf = QtWidgets.QPushButton(self.tab_2)
        self.t2butmodfisnf.setObjectName("t2butmodfisnf")
        self.horizontalLayout_5.addWidget(self.t2butmodfisnf)
        self.t2entpricsnfmodfi = QtWidgets.QLineEdit(self.tab_2)
        self.t2entpricsnfmodfi.setObjectName("t2entpricsnfmodfi")
        self.horizontalLayout_5.addWidget(self.t2entpricsnfmodfi)
        self.label_21 = QtWidgets.QLabel(self.tab_2)
        self.label_21.setObjectName("label_21")
        self.horizontalLayout_5.addWidget(self.label_21)
        self.t2entqmisnfmodi = QtWidgets.QLineEdit(self.tab_2)
        self.t2entqmisnfmodi.setObjectName("t2entqmisnfmodi")
        self.horizontalLayout_5.addWidget(self.t2entqmisnfmodi)
        self.label_20 = QtWidgets.QLabel(self.tab_2)
        self.label_20.setObjectName("label_20")
        self.horizontalLayout_5.addWidget(self.label_20)
        self.t2entnamesnfmodfi = QtWidgets.QLineEdit(self.tab_2)
        self.t2entnamesnfmodfi.setObjectName("t2entnamesnfmodfi")
        self.horizontalLayout_5.addWidget(self.t2entnamesnfmodfi)
        self.label_19 = QtWidgets.QLabel(self.tab_2)
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_5.addWidget(self.label_19)
        self.verticalLayout_6.addLayout(self.horizontalLayout_5)
        self.line_2 = QtWidgets.QFrame(self.tab_2)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_6.addWidget(self.line_2)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.t2butchodeletsnf = QtWidgets.QPushButton(self.tab_2)
        self.t2butchodeletsnf.setObjectName("t2butchodeletsnf")
        self.horizontalLayout_6.addWidget(self.t2butchodeletsnf)
        self.label_22 = QtWidgets.QLabel(self.tab_2)
        self.label_22.setStyleSheet("font: 75 12pt \"Noto Sans\";")
        self.label_22.setObjectName("label_22")
        self.horizontalLayout_6.addWidget(self.label_22)
        self.verticalLayout_6.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.t2butdeletsnf = QtWidgets.QPushButton(self.tab_2)
        self.t2butdeletsnf.setObjectName("t2butdeletsnf")
        self.horizontalLayout_7.addWidget(self.t2butdeletsnf)
        self.t2entnamsnfdelet = QtWidgets.QLineEdit(self.tab_2)
        self.t2entnamsnfdelet.setObjectName("t2entnamsnfdelet")
        self.horizontalLayout_7.addWidget(self.t2entnamsnfdelet)
        self.label_23 = QtWidgets.QLabel(self.tab_2)
        self.label_23.setObjectName("label_23")
        self.horizontalLayout_7.addWidget(self.label_23)
        self.verticalLayout_6.addLayout(self.horizontalLayout_7)
        self.line_3 = QtWidgets.QFrame(self.tab_2)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_6.addWidget(self.line_3)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.t2butchoftordelet = QtWidgets.QPushButton(self.tab_2)
        self.t2butchoftordelet.setObjectName("t2butchoftordelet")
        self.horizontalLayout_8.addWidget(self.t2butchoftordelet)
        self.label_24 = QtWidgets.QLabel(self.tab_2)
        self.label_24.setStyleSheet("font: 75 12pt \"Noto Sans\";")
        self.label_24.setObjectName("label_24")
        self.horizontalLayout_8.addWidget(self.label_24)
        self.verticalLayout_6.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.t2butdeletftor = QtWidgets.QPushButton(self.tab_2)
        self.t2butdeletftor.setObjectName("t2butdeletftor")
        self.horizontalLayout_9.addWidget(self.t2butdeletftor)
        self.t2entnumftordelet = QtWidgets.QLineEdit(self.tab_2)
        self.t2entnumftordelet.setObjectName("t2entnumftordelet")
        self.horizontalLayout_9.addWidget(self.t2entnumftordelet)
        self.label_25 = QtWidgets.QLabel(self.tab_2)
        self.label_25.setObjectName("label_25")
        self.horizontalLayout_9.addWidget(self.label_25)
        self.verticalLayout_6.addLayout(self.horizontalLayout_9)
        self.gridLayout_7.addLayout(self.verticalLayout_6, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout_5.addWidget(self.tabWidget, 0, 1, 1, 1)
        self.stackedWidget.addWidget(self.page_3)
        self.page_2 = QtWidgets.QWidget()


        self.page_2.setObjectName("page_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.page_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.splitter_7 = QtWidgets.QSplitter(self.page_2)
        self.splitter_7.setOrientation(QtCore.Qt.Vertical)
        self.splitter_7.setObjectName("splitter_7")
        self.layoutWidget = QtWidgets.QWidget(self.splitter_7)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        self.label_8.setStyleSheet("font: 14pt \"Noto Sans\";")
        self.label_8.setObjectName("label_8")
        self.verticalLayout_2.addWidget(self.label_8)
        self.splitter_4 = QtWidgets.QSplitter(self.layoutWidget)
        self.splitter_4.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_4.setObjectName("splitter_4")
        self.butaddmeal = QtWidgets.QPushButton(self.splitter_4)
        self.butaddmeal.setObjectName("butaddmeal")
        self.entpricaddmeal = QtWidgets.QLineEdit(self.splitter_4)
        self.entpricaddmeal.setObjectName("entpricaddmeal")
        self.label_6 = QtWidgets.QLabel(self.splitter_4)
        self.label_6.setObjectName("label_6")
        self.entnamemealinadd = QtWidgets.QLineEdit(self.splitter_4)
        self.entnamemealinadd.setObjectName("entnamemealinadd")
        self.label_5 = QtWidgets.QLabel(self.splitter_4)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.splitter_4)
        self.layoutWidget1 = QtWidgets.QWidget(self.splitter_7)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_9 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_9.setStyleSheet("font: 14pt \"Noto Sans\";")
        self.label_9.setObjectName("label_9")
        self.verticalLayout_3.addWidget(self.label_9)
        self.splitter_5 = QtWidgets.QSplitter(self.layoutWidget1)
        self.splitter_5.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_5.setObjectName("splitter_5")
        self.entpricinmodimeal = QtWidgets.QLineEdit(self.splitter_5)
        self.entpricinmodimeal.setObjectName("entpricinmodimeal")
        self.label_11 = QtWidgets.QLabel(self.splitter_5)
        self.label_11.setObjectName("label_11")
        self.entnnewnamemeal = QtWidgets.QLineEdit(self.splitter_5)
        self.entnnewnamemeal.setObjectName("entnnewnamemeal")
        self.label_10 = QtWidgets.QLabel(self.splitter_5)
        self.label_10.setObjectName("label_10")
        self.comnamethemodmeal = QtWidgets.QComboBox(self.splitter_5)
        self.comnamethemodmeal.setObjectName("comnamethemodmeal")
        self.label_7 = QtWidgets.QLabel(self.splitter_5)
        self.label_7.setObjectName("label_7")
        self.butnameodmeal = QtWidgets.QPushButton(self.splitter_5)
        self.butnameodmeal.setObjectName("butnameodmeal")
        self.verticalLayout_3.addWidget(self.splitter_5)
        self.layoutWidget2 = QtWidgets.QWidget(self.splitter_7)
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_12 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_12.setStyleSheet("font: 14pt \"Noto Sans\";")
        self.label_12.setObjectName("label_12")
        self.verticalLayout_4.addWidget(self.label_12)
        self.splitter_6 = QtWidgets.QSplitter(self.layoutWidget2)
        self.splitter_6.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_6.setObjectName("splitter_6")
        self.butdelet = QtWidgets.QPushButton(self.splitter_6)
        self.butdelet.setObjectName("butdelet")
        self.comnameeatdelet = QtWidgets.QComboBox(self.splitter_6)
        self.comnameeatdelet.setObjectName("comnameeatdelet")
        self.label_13 = QtWidgets.QLabel(self.splitter_6)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_4.addWidget(self.splitter_6)
        self.gridLayout_4.addWidget(self.splitter_7, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_2)
        self.gridLayout.addWidget(self.stackedWidget, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 845, 27))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
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
        self.dockWidget = QtWidgets.QDockWidget(MainWindow)
        self.dockWidget.setObjectName("dockWidget")
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setProperty('name','t4')
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.dockWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.splitter = QtWidgets.QSplitter(self.dockWidgetContents)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.butpagmain = QtWidgets.QPushButton(self.splitter)
        self.butpagmain.setObjectName("butpagmain")
        self.butaddneweatinlist = QtWidgets.QPushButton(self.splitter)
        self.butaddneweatinlist.setObjectName("butaddneweatinlist")
        self.pushButton_3 = QtWidgets.QPushButton(self.splitter)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.splitter)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout_2.addWidget(self.splitter, 0, 0, 1, 1)
        self.dockWidget.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockWidget)
        ###############################3
        self.textEdit3.setProperty('id','tex')
        #################################################R
        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(1)
        MainWindow.destroyed.connect(self.pushButton_4.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "السعر:"))
        self.label_4.setText(_translate("MainWindow", "الكمية:"))
        self.label_2.setText(_translate("MainWindow", "اسم الماكول:"))
        self.pagmcomtypemeal.setItemText(0, _translate("MainWindow", "فطور"))
        self.pagmcomtypemeal.setItemText(1, _translate("MainWindow", "غدا"))
        self.pagmcomtypemeal.setItemText(2, _translate("MainWindow", "عشاء"))
        self.label.setText(_translate("MainWindow", "نوع الوجبة:"))
        self.pagmcomprin.setText(_translate("MainWindow", "طباعة"))
        self.pagmcomnewfile.setText(_translate("MainWindow", "فاتورة جديدة"))
        self.label_15.setText(_translate("MainWindow", "او بتاريخ اليوم :"))
        self.label_14.setText(_translate("MainWindow", "رقم الفاتورة:"))
        self.t1butdateftor.setText(_translate("MainWindow", "عرض الفواتير باستخدام اليوم"))
        self.t1butprint.setText(_translate("MainWindow", "طباعة"))
        self.t1butnumberftor.setText(_translate("MainWindow", "عرض عدد الفواتير"))
        self.t1butshonumfto.setText(_translate("MainWindow", "عرض الفواتير باستخدام رقم الفاتورة"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "معلومات كاملة عن الفواتير"))
        self.label_18.setText(_translate("MainWindow", "الاصناف الموجودة في الفاتورة:"))
        self.label_17.setText(_translate("MainWindow", "اختر رقم الفاتورة:"))
        self.t2butshomodfi.setText(_translate("MainWindow", "اختر الصنف المراد تعديلة من القائمة"))
        self.label_16.setText(_translate("MainWindow", "تعديل في الفاتورة في صنف معين:"))
        self.t2butmodfisnf.setText(_translate("MainWindow", "تعديل"))
        self.label_21.setText(_translate("MainWindow", "السعر:"))
        self.label_20.setText(_translate("MainWindow", "الكمية:"))
        self.label_19.setText(_translate("MainWindow", "اسم الصنف:"))
        self.t2butchodeletsnf.setText(_translate("MainWindow", "اختر الصنف المراد حذفة من القائمة"))
        self.label_22.setText(_translate("MainWindow", "حذف صنف معين من الفاتورة:"))
        self.t2butdeletsnf.setText(_translate("MainWindow", "حذف"))
        self.label_23.setText(_translate("MainWindow", "اسم الصنف:"))
        self.t2butchoftordelet.setText(_translate("MainWindow", "اختر رقم الفاتورة المراد حذفها من القائمة"))
        self.label_24.setText(_translate("MainWindow", "حذف فاتورة كاملة مع اصنافها:"))
        self.t2butdeletftor.setText(_translate("MainWindow", "حذف"))
        self.label_25.setText(_translate("MainWindow", "رقم الفاتورة:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "التعديل في الفواتير"))
        self.label_8.setText(_translate("MainWindow", "اضافة ماكولات جديدة:"))
        self.butaddmeal.setText(_translate("MainWindow", "اضافة"))
        self.label_6.setText(_translate("MainWindow", "السعر:"))
        self.label_5.setText(_translate("MainWindow", "اسم الماكول:"))
        self.label_9.setText(_translate("MainWindow", "التعديل في الماكولات:"))
        self.label_11.setText(_translate("MainWindow", "السعر:"))
        self.label_10.setText(_translate("MainWindow", "اسم الماكول الجديد:"))
        self.label_7.setText(_translate("MainWindow", "اسم الماكول المراد تعديلة:"))
        self.butnameodmeal.setText(_translate("MainWindow", "تعديل"))
        self.label_12.setText(_translate("MainWindow", "الحذف في الماكولات:"))
        self.butdelet.setText(_translate("MainWindow", "حذف"))
        self.label_13.setText(_translate("MainWindow", "اسم الماكول:"))
        self.butpagmain.setText(_translate("MainWindow", "الصفحة الرئيسية"))
        self.butaddneweatinlist.setText(_translate("MainWindow", "اضافة ماكولات جديدة"))
        self.pushButton_3.setText(_translate("MainWindow", "الصادرات والفواتير"))
        self.pushButton_4.setText(_translate("MainWindow", "خروج"))
        self.menuFile.setTitle(_translate("MainWindow", "مساعدة"))
        #self.actionAbout.setText(_translate("MainWindow", "حول البرنامج"))
        self.actionGo.setText(_translate("MainWindow", "حول البرنامج"))
        self.actionExit.setText(_translate("MainWindow", "خروج"))

class NotePad(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)#lambda:تضعها عند اسم الزر
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.butpagmain.clicked.connect(self.s1)
        self.ui.pushButton_3.clicked.connect(self.s2)
        self.ui.butaddneweatinlist.clicked.connect(self.s3)
        self.ui.butaddmeal.clicked.connect(self.addeat)
        self.ui.pagmcomnameeat.currentIndexChanged.connect(self.shopric)
        self.ui.pagmqmi.currentIndexChanged.connect(self.chngqmi2)
        self.ui.pushButton_4.clicked.connect(self.exx)
        self.ui.pagmcomnewfile.clicked.connect(self.deletbuffr2)
        self.ui.butnameodmeal.clicked.connect(self.modfieat)
        self.ui.butdelet.clicked.connect(self.deleeat)
        self.ui.t1butshonumfto.clicked.connect(self.shoftornumber)
        self.ui.t1butdateftor.clicked.connect(self.shoftordate)
        self.ui.t1butnumberftor.clicked.connect(self.numftor)
        self.ui.t2comchonumftor.currentIndexChanged.connect(self.chngnumb)
        self.ui.t2butshomodfi.clicked.connect(self.modfisnf)
        self.ui.t2butmodfisnf.clicked.connect(self.modfisnfnow)
        self.ui.t2butchodeletsnf.clicked.connect(self.delsnf)
        self.ui.t2butdeletsnf.clicked.connect(self.delsnfnow)
        self.ui.t2butchoftordelet.clicked.connect(self.delftora)
        self.ui.t2butdeletftor.clicked.connect(self.delftoranow)
        self.ui.pagmcomprin.clicked.connect(self.print1)
        self.ui.t1butprint.clicked.connect(self.print2)
        self.ui.actionExit.triggered.connect(self.out1)
        self.ui.actionGo.triggered.connect(self.instr)
        self.addeatcom1()
        self.addeatcom2()
        self.addeatcom3()
        self.storgftor1()
        self.storgftor2()
        self.ui.pagmqmi.addItem("{}".format("1"))
        self.ui.pagmqmi.addItem("{}".format("2"))
        self.ui.pagmqmi.addItem("{}".format("3"))
        self.ui.pagmqmi.addItem("{}".format("4"))
        self.ui.pagmqmi.addItem("{}".format("5"))
        self.ui.pagmqmi.addItem("{}".format("6"))
        self.ui.pagmqmi.addItem("{}".format("7"))
        self.ui.pagmqmi.addItem("{}".format("8"))
        self.ui.pagmqmi.addItem("{}".format("9"))
    def s1(self):
        self.ui.stackedWidget.setCurrentIndex(0)
    def s2(self):
        self.ui.stackedWidget.setCurrentIndex(1)
    def s3(self):
        self.ui.stackedWidget.setCurrentIndex(2)
    def exx(self):
        self.anim = QPropertyAnimation(self, b'pos')
        self.anim.setDuration(1000)
        self.anim.setStartValue(QPointF(200, 100))
        self.anim.setEndValue(QPointF(1, 100))
        self.anim.start()
        #time.sleep(1)
        #self.exec_()
        self.close()
    def out1(self):
        self.anim = QPropertyAnimation(self, b'pos')
        self.anim.setDuration(1000)
        self.anim.setStartValue(QPointF(200, 100))
        self.anim.setEndValue(QPointF(1, 100))
        self.anim.start()
        exit()
    def instr(self):
        message=QtWidgets.QMessageBox.information(self,'حول البرنامج','<FONT size=5 color=black>Copyright (C) 2020,By The programmer Salem khamis Bahien</FONT><br><p>Email:99zzz52@gmail.com</p><p>Telephon:713151679</p>')
        
########################################################################################################################
###########################################################################################################################     
    def addeat(self):
        nameeat1=str(self.ui.entnamemealinadd.text())
        priceat=str(self.ui.entpricaddmeal.text())
        db1=sqlite3.connect("mtam.db")
        db1.row_factory=sqlite3.Row
        db1.execute('create table if not exists addeat1(ID integer primary Key autoincrement,namet text,pret text)')
        db1.execute('''insert into addeat1(namet,pret) values(?,?)''',(nameeat1,priceat))
        db1.commit()
        message=QtWidgets.QMessageBox.information(self,'information','<FONT size=10 color=blue>Add Successfully</FONT>')
    def addeatcom1(self):
        db1=sqlite3.connect('mtam.db')
        db1.row_factory=sqlite3.Row
        sa=db1.execute("select * from addeat1")
        self.ui.pagmcomnameeat.addItem("{}".format("None"))
        for n in sa:
            self.ui.pagmcomnameeat.addItem("{}".format(n["namet"]))
        db1.close() 
    def shopric(self):
        typeat=str(self.ui.pagmcomtypemeal.currentText())
        nameeat=str(self.ui.pagmcomnameeat.currentText())
        qumi=str(self.ui.pagmqmi.currentText())
        priceate=str(self.ui.pagmcompric.text())
        tt=[]
        ft=sqlite3.connect('mtam.db')
        ft.row_factory=sqlite3.Row
        ft.execute('create table if not exists storgbuffer1(ID integer primary Key autoincrement,ftora text)')
        ft.commit()
        gb=ft.execute("select * from storgbuffer1")
        for t in gb:
            tt.append(t)
        kk=len(tt)
        if kk==0:
            ft.execute('insert into storgbuffer1(ftora) values(?)',("0"))
            ft.commit()
        ft1=ft.execute("select * from storgbuffer1")
        for y in ft1:
            ftttora=str(y["ftora"])
        
        x=datetime.datetime.now().hour
        s=datetime.datetime.now().minute
        a=datetime.datetime.now().second
        time1=str(str(x)+":"+str(s)+":"+str(a))
        today = str(date.today())
        e=0
        selecteat=str(self.ui.pagmcomnameeat.currentText())
        db1=sqlite3.connect('mtam.db')
        db1.row_factory=sqlite3.Row
        tab1=db1.execute("select * from addeat1 where namet='{}'".format(selecteat))
        for h in tab1:
            e=1
            stopricsnf=(h["pret"])
            f=int(stopricsnf)
            c=int(self.ui.pagmqmi.currentText())
            g=f*c
            self.ui.pagmcompric.setText(str(g))
            if e==1:
                rr=[]
                nameeatt=str(self.ui.pagmcomnameeat.currentText())
                db2=sqlite3.connect('mtam.db')
                db2.row_factory=sqlite3.Row
                db2.execute('create table if not exists storgbuffer2(ID integer primary Key autoincrement,stotypeate text,stonameaet text,stopriceat text,stoqmi text,stotimeeat text)')
                db2.commit()
                ggg=db2.execute("select stonameaet from storgbuffer2 where stonameaet='{}'".format(nameeatt))
                for x in ggg:
                    rr.append(x)
                fff=len(rr)
                if fff != 0:
                    dff=db2.execute("select * from storgbuffer2")#bgcolor='green'
                    self.ui.textEdit1.clear()
                    self.ui.textEdit1.append("<p align='left'>رقم الفاتورة: <font color=red>{}</font></p>".format(ftttora))
                    self.ui.textEdit1.append("<p align='left'>التاريخ: {}</p>".format(today))
                    self.ui.textEdit1.append("<p><table width='100%' border='1' cellpadding'5' ><caption><b><u><center>فاتورة المشتريات</center></u></b></caption><tr><td width=20%><u><center>نوع الوجبة</center></u></td><td width=20%><u><center>اسم الماكول</u></center></td><td width=20%><u><center>السعر</u></center></td><td width=20%><u><center>الكمية</u></center></td><td width=20%><u><center>الوقت</u></center></td></tr></table></p>")
                    for n in dff:
                        self.ui.textEdit1.append("<p><table width='100%' border='1' cellpadding'5' ><tr><td width=20%><center>{}</td><td width=20%><center>{}</td><td width=20%><center>{}</td><td width=20%><center>{}</td><td width=20%><center>{}</td></tr></table></p>".format(n["stotypeate"],n["stonameaet"],n["stopriceat"],n["stoqmi"],n["stotimeeat"]))
                    sum1=db2.execute("select sum(stopriceat) from storgbuffer2")
                    for d in sum1:
                        self.ui.textEdit1.append("<p><table width='100%' border='1' cellpadding'5' ><tr><td width=50%><center>{}</td><td width=50%><center>الاجمالي</center></td></tr></table></p>".format(d[0]))   
                else:
                    typeat=str(self.ui.pagmcomtypemeal.currentText())
                    nameeat=str(self.ui.pagmcomnameeat.currentText())
                    qumi=str(self.ui.pagmqmi.currentText())
                    priceate=str(self.ui.pagmcompric.text())
                    db1=sqlite3.connect('mtam.db')
                    db1.row_factory=sqlite3.Row
                    db1.execute('''insert into storgbuffer2(stotypeate,stonameaet,stopriceat,stoqmi,stotimeeat) values(?,?,?,?,?)''',(typeat,nameeat,priceate,qumi,today+'/'+time1))
                    db1.commit()
                    dff=db1.execute("select * from storgbuffer2")
                    self.ui.textEdit1.clear()
                    self.ui.textEdit1.append("<p align='left'>رقم الفاتورة: <font color=red>{}</font></p>".format(ftttora))
                    self.ui.textEdit1.append("<p align='left'>التاريخ: {}</p>".format(today))
                    self.ui.textEdit1.append("<p><table width='100%' border='1' cellpadding'5' ><caption><b><u><center>فاتورة المشتريات</center></u></b></caption><tr><td width=20%><u><center>نوع الوجبة</center></u></td><td width=20%><u><center>اسم الماكول</u></center></td><td width=20%><u><center>السعر</u></center></td><td width=20%><u><center>الكمية</u></center></td><td width=20%><u><center>الوقت</u></center></td></tr></table></p>")
                    for n in dff:
                        self.ui.textEdit1.append("<p><table width='100%' border='1' cellpadding'5' ><tr><td width=20%><center>{}</td><td width=20%><center>{}</td><td width=20%><center>{}</td><td width=20%><center>{}</td><td width=20%><center>{}</td></tr></table></p>".format(n["stotypeate"],n["stonameaet"],n["stopriceat"],n["stoqmi"],n["stotimeeat"]))
                    sum1=db2.execute("select sum(stopriceat) from storgbuffer2")
                    for d in sum1:
                        self.ui.textEdit1.append("<p><table width='100%' border='1' cellpadding'5' ><tr><td width=50%><center>{}</td><td width=50%><center>الاجمالي</center></td></tr></table></p>".format(d[0]))
    def chngqmi2(self):
        x=datetime.datetime.now().hour
        s=datetime.datetime.now().minute
        a=datetime.datetime.now().second
        time1=str(str(x)+":"+str(s)+":"+str(a))
        today = str(date.today())
        nameeat=str(self.ui.pagmcomnameeat.currentText())
        i=0
        if str(self.ui.pagmcompric.text()) !="":
            db1=sqlite3.connect('mtam.db')
            db1.row_factory=sqlite3.Row
            tab1=db1.execute("select * from addeat1 where namet='{}'".format(nameeat))
            for h in tab1:
                f=int(h["pret"])
                c=int(self.ui.pagmqmi.currentText())
                g=f*c
            self.ui.pagmcompric.setText(str(g))
            typeat=str(self.ui.pagmcomtypemeal.currentText())
            qumi=str(self.ui.pagmqmi.currentText())
            priceate=str(self.ui.pagmcompric.text())    
            db2=sqlite3.connect('mtam.db')
            db2.row_factory=sqlite3.Row
            tab2=db2.execute("select * from storgbuffer2 where stonameaet='{}'".format(nameeat))
            for l in tab2:
                i=1
            if i==1:
                db3=sqlite3.connect('mtam.db')
                db3.row_factory=sqlite3.Row
                db3.execute("delete from storgbuffer2 where stonameaet='{}'".format(nameeat))
                db3.commit()
                db3.execute('''insert into storgbuffer2(stotypeate,stonameaet,stopriceat,stoqmi,stotimeeat) values(?,?,?,?,?)''',(typeat,nameeat,priceate,qumi,today+'/'+time1))
                db3.commit()
                tab3=db3.execute("select * from storgbuffer2 where stonameaet='{}'".format(nameeat))
                for j in tab3:
                    self.ui.pagmcomnameeat.clear()
                    self.ui.pagmcomnameeat.addItem('{}'.format(j[2]))
                    self.addeatcom1()
    def deletbuffr2(self):#storg in database devic allowys and compution ftorh
        db2=sqlite3.connect('mtam.db')
        db2.row_factory=sqlite3.Row
        db2.execute('create table if not exists storgbuffer3(ID integer primary Key autoincrement,stotypeate text,stonameaet text,stopriceat text,stoqmi text,stotimeeat text,numbfator text)')
        db2.commit()
        tab2=db2.execute("select * from storgbuffer1")
        for x in tab2:
            ftttora=str(x["ftora"])
        tab3=db2.execute("select * from storgbuffer2")
        for h in tab3:
            db2.execute('''insert into storgbuffer3(stotypeate,stonameaet,stopriceat,stoqmi,stotimeeat,numbfator) values(?,?,?,?,?,?)''',(h["stotypeate"],h["stonameaet"],h["stopriceat"],h["stoqmi"],h["stotimeeat"],ftttora)) 
        db2.commit()
        fb1=db2.execute("select * from storgbuffer1")
        for k in fb1:
            num=int(k["ftora"])
        num+=1
        db2.execute("update storgbuffer1 set ftora='{}'".format(str(num)))  
        db2.commit()
        db2.execute('''delete from storgbuffer2''')
        db2.commit()
    def addeatcom2(self):
        db1=sqlite3.connect('mtam.db')
        db1.row_factory=sqlite3.Row
        sa=db1.execute("select * from addeat1")
        for n in sa:
            self.ui.comnamethemodmeal.addItem("{}".format(n["namet"]))    
    def modfieat(self):
        nammodfi=str(self.ui.comnamethemodmeal.currentText())
        newname=str(self.ui.entnnewnamemeal.text())
        newpric=str(self.ui.entpricinmodimeal.text())
        db1=sqlite3.connect("mtam.db")
        db1.row_factory=sqlite3.Row
        db1.execute("update addeat1 set namet='{}' ,pret='{}' where namet='{}'".format(newname,newpric,nammodfi))
        db1.commit()
        message=QtWidgets.QMessageBox.information(self,'information','<FONT size=10 color=blue>تم التعديل بنجاح</FONT>')
    def addeatcom3(self):
        db1=sqlite3.connect('mtam.db')
        db1.row_factory=sqlite3.Row
        sa=db1.execute("select * from addeat1")
        for n in sa:
            self.ui.comnameeatdelet.addItem("{}".format(n["namet"]))
    def deleeat(self):
        nameaettt=str(self.ui.comnameeatdelet.currentText())
        db1=sqlite3.connect('mtam.db')
        db1.row_factory=sqlite3.Row
        db1.execute("delete from addeat1 where namet='{}'".format(nameaettt))
        db1.commit()
        message=QtWidgets.QMessageBox.information(self,'information','<FONT size=10 color=blue>تم الحذف بنجاح</FONT>')
#####################################################tab1###################################################################
################################################################################################################################
###################################################################################################################################
    def storgftor1(self):
        db1=sqlite3.connect('mtam.db')
        db1.row_factory=sqlite3.Row
        sa=db1.execute("select distinct numbfator,stotimeeat from storgbuffer3")
        for n in sa:
            self.ui.t1comnumfator.addItem("{}".format(n["numbfator"]))
            self.ui.t1comdateftor.addItem("{}".format(n["stotimeeat"]))
    def shoftornumber(self):
        numftor=str(self.ui.t1comnumfator.currentText())
        db1=sqlite3.connect('mtam.db')
        db1.row_factory=sqlite3.Row
        sa=db1.execute("select * from storgbuffer3 where numbfator='{}'".format(numftor))
        for n in sa:
            gggg=str(n["stotimeeat"])

        self.ui.textEdit3.clear()
        self.ui.textEdit3.append("<p align='left'>رقم الفاتورة: <font color=red>{}</font></p>".format(numftor))
        self.ui.textEdit3.append("<p align='left'>التاريخ: {}</p>".format(gggg))
        self.ui.textEdit3.append("<p><table width='100%' border='1' cellpadding'5' ><caption><b><u><center>فاتورة المشتريات</center></u></b></caption><tr><td width=20%><u><center>نوع الوجبة</center></u></td><td width=20%><u><center>اسم الماكول</u></center></td><td width=20%><u><center>السعر</u></center></td><td width=20%><u><center>الكمية</u></center></td><td width=20%><u><center>الوقت</u></center></td></tr></table></p>")
        sa1=db1.execute("select * from storgbuffer3 where numbfator='{}'".format(numftor))
        for n in sa1:
            self.ui.textEdit3.append("<p><table width='100%' border='1' cellpadding'5' ><tr><td width=20%><center>{}</td><td width=20%><center>{}</td><td width=20%><center>{}</td><td width=20%><center>{}</td><td width=20%><center>{}</td></tr></table></p>".format(n["stotypeate"],n["stonameaet"],n["stopriceat"],n["stoqmi"],n["stotimeeat"]))
        sum1=db1.execute("select sum(stopriceat) from storgbuffer3 where numbfator='{}'".format(numftor))
        for d in sum1:
            self.ui.textEdit3.append("<p><table width='100%' border='1' cellpadding'5' ><tr><td width=50%><center>{}</td><td width=50%><center>الاجمالي</center></td></tr></table></p>".format(d[0]))
    def shoftordate(self):
        sss=[]
        numftor1=str(self.ui.t1comdateftor.currentText())
        numftor=numftor1[:10]
        db1=sqlite3.connect('mtam.db')
        db1.row_factory=sqlite3.Row
        sa=db1.execute("select distinct numbfator from storgbuffer3 where stotimeeat like '%{}%'".format(numftor))
        for n in sa:
            sss.append(str(n["numbfator"]))





        self.ui.textEdit3.clear()
        for f in sss:
            sa2=db1.execute("select * from storgbuffer3 where numbfator='{}'".format(f))
            self.ui.textEdit3.append("<p align='left'>رقم الفاتورة: <font color=red>{}</font></p>".format(f))
            self.ui.textEdit3.append("<p align='left'>التاريخ: {}</p>".format(numftor))
            self.ui.textEdit3.append("<p><table width='100%' border='1' cellpadding'5' ><caption><b><u><center>فاتورة المشتريات</center></u></b></caption><tr><td width=20%><u><center>نوع الوجبة</center></u></td><td width=20%><u><center>اسم الماكول</u></center></td><td width=20%><u><center>السعر</u></center></td><td width=20%><u><center>الكمية</u></center></td><td width=20%><u><center>الوقت</u></center></td></tr></table></p>")
            for n in sa2:
                self.ui.textEdit3.append("<p><table width='100%' border='1' cellpadding'5' ><tr><td width=20%><center>{}</td><td width=20%><center>{}</td><td width=20%><center>{}</td><td width=20%><center>{}</td><td width=20%><center>{}</td></tr></table></p>".format(n["stotypeate"],n["stonameaet"],n["stopriceat"],n["stoqmi"],n["stotimeeat"]))
            sum1=db1.execute("select sum(stopriceat) from storgbuffer3 where numbfator='{}'".format(f))
            for d in sum1:
                self.ui.textEdit3.append("<p><table width='100%' border='1' cellpadding'5' ><tr><td width=50%><center>{}</td><td width=50%><center>الاجمالي</center></td></tr></table></p>".format(d[0]))

            self.ui.textEdit3.append("<p align='center'><center>-----------------------------------------------------------------------------------------------------------------------------------------------------------------</p><br>")
    def numftor(self):
        j1=[]
        db1=sqlite3.connect('mtam.db')
        db1.row_factory=sqlite3.Row
        sa=db1.execute("select distinct numbfator from storgbuffer3")
        self.ui.textEdit3.clear()
        for h in sa:
            j1.append(h)
        numb=str(len(j1))
        self.ui.textEdit3.append("<center><p>عدد الفواتير هي:{}</p></center>".format(numb))
        self.ui.textEdit3.append("<center><p>كل الفواتير الموجودة هي</p></center>")
        sa4=db1.execute("select distinct numbfator from storgbuffer3")
        for x in sa4:
            self.ui.textEdit3.append("<p><table width='100%' border='1' cellpadding'5' ><tr><td width=50%><center>{}</center></td><td width=50%><center>رقم الفاتورة</center></td></tr></table></p>".format(x["numbfator"]))
            
        sa1=db1.execute("select sum(stopriceat) from storgbuffer3")
        for n in sa1:
            self.ui.textEdit3.append("<p><table width='100%' border='1' cellpadding'5' ><tr><td width=50%><center>{} ريال</td><td width=50%><center>الاجمالي الكلي لنقود</center></td></tr></table></p>".format(n[0]))
#####################################################################tab2##########################################################
##################################################################################################################################
#########################################################################################################################
    def storgftor2(self):
        db1=sqlite3.connect('mtam.db')
        db1.row_factory=sqlite3.Row
        sa=db1.execute("select distinct numbfator from storgbuffer3")
        for n in sa:
            self.ui.t2comchonumftor.addItem("{}".format(n["numbfator"]))
    def chngnumb(self):
        numftto=str(self.ui.t2comchonumftor.currentText())
        db1=sqlite3.connect('mtam.db')
        db1.row_factory=sqlite3.Row
        sa=db1.execute("select stonameaet from storgbuffer3 where numbfator='{}'".format(numftto))
        self.ui.t2comsnfher.clear()
        for n in sa:
            self.ui.t2comsnfher.addItem("{}".format(n["stonameaet"]))
    def modfisnf(self):
        numftto=str(self.ui.t2comchonumftor.currentText())
        chosnf=str(self.ui.t2comsnfher.currentText())
        db1=sqlite3.connect('mtam.db')
        db1.row_factory=sqlite3.Row
        sa=db1.execute("select * from storgbuffer3 where numbfator='{}' and stonameaet='{}'".format(numftto,chosnf))
        for n in sa:
            self.ui.t2entnamesnfmodfi.setText(n["stonameaet"])
            self.ui.t2entqmisnfmodi.setText(n["stoqmi"])
            self.ui.t2entpricsnfmodfi.setText(n["stopriceat"])
    def modfisnfnow(self):
        numftto=str(self.ui.t2comchonumftor.currentText())
        chosnf=str(self.ui.t2comsnfher.currentText())
        namemod=str(self.ui.t2entnamesnfmodfi.text())
        qmimod=str(self.ui.t2entqmisnfmodi.text())
        pricmod=str(self.ui.t2entpricsnfmodfi.text())
        db1=sqlite3.connect('mtam.db')
        db1.row_factory=sqlite3.Row
        db1.execute("update storgbuffer3 set stonameaet='{}',stoqmi='{}',stopriceat='{}' where numbfator='{}' and stonameaet='{}'".format(namemod,qmimod,pricmod,numftto,chosnf)) 
        db1.commit()
        message=QtWidgets.QMessageBox.information(self,'information','<FONT size=10 color=blue>تم تم تعديل الصنف بنجاح</FONT>')
    def delsnf(self):
        numftto=str(self.ui.t2comchonumftor.currentText())
        chosnf=str(self.ui.t2comsnfher.currentText())
        db1=sqlite3.connect('mtam.db')
        db1.row_factory=sqlite3.Row
        sa=db1.execute("select * from storgbuffer3 where numbfator='{}' and stonameaet='{}'".format(numftto,chosnf))
        for n in sa:
            self.ui.t2entnamsnfdelet.setText(n["stonameaet"])
    def delsnfnow(self):
        numftto=str(self.ui.t2comchonumftor.currentText())
        chosnf=str(self.ui.t2entnamsnfdelet.text())
        db1=sqlite3.connect('mtam.db')
        db1.row_factory=sqlite3.Row
        db1.execute("delete from storgbuffer3 where numbfator='{}' and stonameaet='{}'".format(numftto,chosnf))
        db1.commit()
        message=QtWidgets.QMessageBox.information(self,'information','<FONT size=10 color=blue>تم حذف الصنف بنجاح</FONT>')
    def delftora(self):
        numftto=str(self.ui.t2comchonumftor.currentText())
        self.ui.t2entnumftordelet.setText(numftto)
    def delftoranow(self):
        numftto=str(self.ui.t2entnumftordelet.text())
        db1=sqlite3.connect('mtam.db')
        db1.row_factory=sqlite3.Row
        db1.execute("delete from storgbuffer3 where numbfator='{}'".format(numftto))
        db1.commit()
        message=QtWidgets.QMessageBox.information(self,'information','<FONT size=10 color=blue>تم حذف الفاتورة بنجاح</FONT>')

    def print1(self):#printer##################################printer##################################################
        if self.ui.textEdit1.toPlainText() !="":
            printer =QtPrintSupport.QPrintDialog()
            #printer.setFullPage(True)
            #dialog = QtGui.QPrintDialog(printer)
            if printer.exec_() == QtWidgets.QDialog.Accepted:
                self.ui.textEdit1.document().print_(printer.printer())
                printer.exec_()

    def print2(self):#printer##################################printer##################################################
        if self.ui.textEdit3.toPlainText() !="":
            printer =QtPrintSupport.QPrintDialog()
            #printer.setFullPage(True)
            #dialog = QtGui.QPrintDialog(printer)
            if printer.exec_() == QtWidgets.QDialog.Accepted:
                self.ui.textEdit3.document().print_(printer.printer())
                printer.exec_() 
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    myapp = NotePad()
    st="""QWidget{font-family:times;font-size:15px;border-radius:5px;}
    QWidget[name=t1]{background-color:#6D730C;}
    QPushButton{background-color:#2466B6;border-radius:5px;color:#E1DDD3;border:1px solid blue;}
    QPushButton:hover{background-color:green;}
    QTextEdit{background-color:#F7CEA4;border:1px solid blue;}
    QLineEdit{background-color:#F7CEA4;border:1px solid blue;}
    QStackedWidget[name=t3]{background-color:#E91978;}
    QWidget[name=t2]{background-color:#953CCC;border-radius:5px;}
    QWidget[name=t4]{background-color:red;border-radius:5px;}
    QWidget[name=t5]{background-color:brown;border-radius:5px;}
    QWidget[name=t6]{background-color:#179672;border-radius:5px;}
    QWidget[name=t7]{background-color:#179672;border-radius:5px;}
    QComboBox{background-color:#2E74A1;border-radius:5px;text-align:center;border:1px solid blue;}
    QMessageBox{background-color:#2E74A1;border-radius:5px;}
    QMenu{background-color:#2E74A1;border:1px solid blue;}
    QWidget[name=t8]{background-color:#908973;}


"""
    app.setStyleSheet(st)
myapp.show()
sys.exit(app.exec_())

