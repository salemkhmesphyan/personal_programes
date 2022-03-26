# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mangschool.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from PyQt5.QtCore import (QObject, QPointF, 
        QPropertyAnimation, pyqtProperty)
###################################################################################################################
class Ui_notepad3(object):
    def setupUi(self, notepad):
        notepad.setObjectName("notepad")
        notepad.resize(QtCore.QSize(QtCore.QRect(0,0,668,536).size()).expandedTo(notepad.minimumSizeHint()))
        self.centralwidget = QtWidgets.QWidget(notepad)
        self.centralwidget.setObjectName("centralwidget")
        self.button_open = QtWidgets.QPushButton(self.centralwidget)
        self.button_open.setGeometry(QtCore.QRect(20,10,201,27))
        self.button_open.setObjectName("button_open")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(440,10,201,27))
        self.pushButton_2.setObjectName("pushButton_2")
        self.editor_window = QtWidgets.QTextEdit(self.centralwidget)
        self.editor_window.setGeometry(QtCore.QRect(23,50,611,431))
        self.editor_window.setObjectName("editor_window")
        self.button_save = QtWidgets.QPushButton(self.centralwidget)
        self.button_save.setGeometry(QtCore.QRect(230,10,201,27))


        self.button_save.setObjectName("button_save")
        notepad.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(notepad)
        self.menubar.setGeometry(QtCore.QRect(0,0,668,25))
        self.menubar.setObjectName("menubar")
        notepad.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(notepad)
        self.statusbar.setObjectName("statusbar")
        notepad.setStatusBar(self.statusbar)
        self.retranslateUi(notepad)
        #QtCore.QObject.connect(self.pushButton_2,QtCore.SIGNAL("clicked()"),notepad.close)
        QtCore.QMetaObject.connectSlotsByName(notepad)
    def retranslateUi(self, notepad):
        notepad.setWindowTitle(QtWidgets.QApplication.translate("notepad",
        "MainWindow", None))
        self.button_open.setText(QtWidgets.QApplication.translate("notepad",
        "Open", None))
        self.pushButton_2.setText(QtWidgets.QApplication.translate
        ("notepad", "Create file", None))
        self.button_save.setText(QtWidgets.QApplication.translate("notepad",
        "save", None))
class NotePad3(QtWidgets.QMainWindow):
   def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_notepad3()
        self.ui.setupUi(self)
        self.ui.button_open.clicked.connect(self.file_dialog)
        self.ui.button_save.clicked.connect(self.file_save)
        self.ui.editor_window.textChanged.connect(self.enable_save)
        self.ui.pushButton_2.clicked.connect(self.cretfile)
        self.ui.button_save.setEnabled(False)
   def file_dialog(self):
   	  	if self.ui.button_save.isEnabled():
   	  		message=QtWidgets.QMessageBox.question(self, 'save file ?','save changes ?',QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)
   	  		if message == QtWidgets.QMessageBox.Yes:
   	  			self.file_save()
   	  			self.ui.button_save.setEnabled(False)
   	  	elif message == QtWidgets.QMessageBox.No:
   	  		self.ui.button_save.setEnabled(False)
   	  		self.ui.editor_window.clear()
   	  		file_dialog = QtWidgets.QFileDialog(self)
   	  		self.filename = file_dialog.getOpenFileName()
   	  		from os.path import isfile
   	  		if isfile(self.filename):
   	  			text = open(self.filename).read()
   	  			self.ui.editor_window.append(text)
   	  	else:
   	  		file_dialog = QtWidgets.QFileDialog(self)
   	  		self.filename = file_dialog.getOpenFileName()
   	  		from os.path import isfile
   	  		if isfile(self.filename):
   	  			text = open(self.filename).read()
   	  			self.ui.editor_window.append(text)
   	  			self.ui.button_save.setEnabled(False)
   def enable_save(self):
   		self.ui.button_save.setEnabled(True)
   def file_save(self):
   		from os.path import isfile
   		file_dialog = QtWidgets.QFileDialog(self)
   		self.filename = file_dialog.getOpenFileName()
   		if isfile(self.filename):
   			file = open(self.filename, 'w')
   			file.write(self.ui.editor_window.toPlainText())
   			file.close()
   def cretfile(self):
   		file_dialog = QtWidgets.QFileDialog(self)
   		self.filename = (file_dialog.getSaveFileName())
   		file = open(self.filename, 'a')
   		file.write(self.ui.editor_window.toPlainText())
   		file.close()
####################################################################################################################
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(977, 765)
        self.anim = QPropertyAnimation(MainWindow, b'pos')
        self.anim.setDuration(1000)
        self.anim.setStartValue(QPointF(1, 100))
        self.anim.setEndValue(QPointF(200, 100))
        self.anim.start()
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 0, 0, 255), stop:0.166 rgba(255, 255, 0, 255), stop:0.333 rgba(0, 255, 0, 255), stop:0.5 rgba(0, 255, 255, 255), stop:0.666 rgba(0, 0, 255, 255), stop:0.833 rgba(255, 0, 255, 255), stop:1 rgba(255, 0, 0, 255));")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setStyleSheet("background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(214, 255, 170, 255), stop:1 rgba(255, 255, 255, 255));")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.page)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.page)
        self.tabWidget.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(9, 41, 4, 255), stop:0.085 rgba(2, 79, 0, 255), stop:0.19 rgba(50, 147, 22, 255), stop:0.275 rgba(236, 191, 49, 255), stop:0.39 rgba(243, 61, 34, 255), stop:0.555 rgba(135, 81, 60, 255), stop:0.667 rgba(121, 75, 255, 255), stop:0.825 rgba(164, 255, 244, 255), stop:0.885 rgba(104, 222, 71, 255), stop:1 rgba(93, 128, 0, 255));\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(244, 117, 117, 255), stop:0.550296 rgba(190, 255, 172, 255), stop:0.604545 rgba(178, 162, 17, 255), stop:1 rgba(255, 255, 255, 255));")
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabWidget.setMovable(True)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.splitter_3 = QtWidgets.QSplitter(self.tab)
        self.splitter_3.setOrientation(QtCore.Qt.Vertical)
        self.splitter_3.setObjectName("splitter_3")
        self.layoutWidget = QtWidgets.QWidget(self.splitter_3)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setStyleSheet("font: oblique 18pt \"mry_KacstQurn\";")
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.t1t1enaddnamrow = QtWidgets.QLineEdit(self.layoutWidget)
        self.t1t1enaddnamrow.setObjectName("t1t1enaddnamrow")
        self.horizontalLayout.addWidget(self.t1t1enaddnamrow)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.t1t1comrowaddnewrow = QtWidgets.QComboBox(self.layoutWidget)
        self.t1t1comrowaddnewrow.setObjectName("t1t1comrowaddnewrow")
        self.t1t1comrowaddnewrow.addItem("")
        self.t1t1comrowaddnewrow.addItem("")
        self.t1t1comrowaddnewrow.addItem("")
        self.t1t1comrowaddnewrow.addItem("")
        self.t1t1comrowaddnewrow.addItem("")
        self.horizontalLayout.addWidget(self.t1t1comrowaddnewrow)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.t1t1butaddrow = QtWidgets.QPushButton(self.layoutWidget)
        self.t1t1butaddrow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(245, 224, 176, 255), stop:0.09 rgba(246, 189, 237, 255), stop:0.14 rgba(194, 207, 246, 255), stop:0.19 rgba(184, 160, 168, 255), stop:0.25 rgba(171, 186, 248, 255), stop:0.32 rgba(243, 248, 224, 255), stop:0.385 rgba(249, 162, 183, 255), stop:0.47 rgba(100, 115, 124, 255), stop:0.58 rgba(251, 205, 202, 255), stop:0.65 rgba(170, 128, 185, 255), stop:0.75 rgba(252, 222, 204, 255), stop:0.805 rgba(206, 122, 218, 255), stop:0.86 rgba(254, 223, 175, 255), stop:0.91 rgba(254, 236, 244, 255), stop:1 rgba(255, 191, 221, 255));")
        self.t1t1butaddrow.setObjectName("t1t1butaddrow")
        self.verticalLayout.addWidget(self.t1t1butaddrow)
        self.layoutWidget1 = QtWidgets.QWidget(self.splitter_3)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_4.setStyleSheet("font: oblique 18pt \"mry_KacstQurn\";")
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.t1t1comnamestud = QtWidgets.QComboBox(self.layoutWidget1)
        self.t1t1comnamestud.setObjectName("t1t1comnamestud")
        self.horizontalLayout_2.addWidget(self.t1t1comnamestud)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_6.setFrameShape(QtWidgets.QFrame.Box)
        self.label_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_6.setText("اسم الصف:")
        self.label_6.setTextFormat(QtCore.Qt.PlainText)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        self.t1t1comaddstudrow = QtWidgets.QComboBox(self.layoutWidget1)
        self.t1t1comaddstudrow.setObjectName("t1t1comaddstudrow")
        self.t1t1comaddstudrow.addItem("")
        self.t1t1comaddstudrow.addItem("")
        self.t1t1comaddstudrow.addItem("")
        self.t1t1comaddstudrow.addItem("")
        self.t1t1comaddstudrow.addItem("")
        self.horizontalLayout_2.addWidget(self.t1t1comaddstudrow)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.t1t1enaddnamestud = QtWidgets.QLineEdit(self.layoutWidget1)
        self.t1t1enaddnamestud.setText("")
        self.t1t1enaddnamestud.setObjectName("t1t1enaddnamestud")
        self.horizontalLayout_3.addWidget(self.t1t1enaddnamestud)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_3.addWidget(self.label_7)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.splitter_2 = QtWidgets.QSplitter(self.layoutWidget1)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.t1t1butrefrs = QtWidgets.QPushButton(self.splitter_2)
        self.t1t1butrefrs.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(245, 224, 176, 255), stop:0.09 rgba(246, 189, 237, 255), stop:0.14 rgba(194, 207, 246, 255), stop:0.19 rgba(184, 160, 168, 255), stop:0.25 rgba(171, 186, 248, 255), stop:0.32 rgba(243, 248, 224, 255), stop:0.385 rgba(249, 162, 183, 255), stop:0.47 rgba(100, 115, 124, 255), stop:0.58 rgba(251, 205, 202, 255), stop:0.65 rgba(170, 128, 185, 255), stop:0.75 rgba(252, 222, 204, 255), stop:0.805 rgba(206, 122, 218, 255), stop:0.86 rgba(254, 223, 175, 255), stop:0.91 rgba(254, 236, 244, 255), stop:1 rgba(255, 191, 221, 255));")
        self.t1t1butrefrs.setObjectName("t1t1butrefrs")
        self.t1t1butaddnamestud = QtWidgets.QPushButton(self.splitter_2)
        self.t1t1butaddnamestud.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(245, 224, 176, 255), stop:0.09 rgba(246, 189, 237, 255), stop:0.14 rgba(194, 207, 246, 255), stop:0.19 rgba(184, 160, 168, 255), stop:0.25 rgba(171, 186, 248, 255), stop:0.32 rgba(243, 248, 224, 255), stop:0.385 rgba(249, 162, 183, 255), stop:0.47 rgba(100, 115, 124, 255), stop:0.58 rgba(251, 205, 202, 255), stop:0.65 rgba(170, 128, 185, 255), stop:0.75 rgba(252, 222, 204, 255), stop:0.805 rgba(206, 122, 218, 255), stop:0.86 rgba(254, 223, 175, 255), stop:0.91 rgba(254, 236, 244, 255), stop:1 rgba(255, 191, 221, 255));")
        self.t1t1butaddnamestud.setObjectName("t1t1butaddnamestud")
        self.verticalLayout_2.addWidget(self.splitter_2)
        self.gridLayout_4.addWidget(self.splitter_3, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout()
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout()
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.t1t2comnamstud = QtWidgets.QComboBox(self.tab_2)
        self.t1t2comnamstud.setEditable(True)
        self.t1t2comnamstud.setObjectName("t1t2comnamstud")
        self.horizontalLayout_6.addWidget(self.t1t2comnamstud)
        self.label_10 = QtWidgets.QLabel(self.tab_2)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_6.addWidget(self.label_10)
        self.t1t2comnamerow = QtWidgets.QComboBox(self.tab_2)
        self.t1t2comnamerow.setObjectName("t1t2comnamerow")
        self.horizontalLayout_6.addWidget(self.t1t2comnamerow)
        self.label_9 = QtWidgets.QLabel(self.tab_2)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_6.addWidget(self.label_9)
        self.t1t2comrow = QtWidgets.QComboBox(self.tab_2)
        self.t1t2comrow.setObjectName("t1t2comrow")
        self.t1t2comrow.addItem("")
        self.t1t2comrow.addItem("")
        self.t1t2comrow.addItem("")
        self.t1t2comrow.addItem("")
        self.t1t2comrow.addItem("")
        self.horizontalLayout_6.addWidget(self.t1t2comrow)
        self.label_8 = QtWidgets.QLabel(self.tab_2)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_6.addWidget(self.label_8)
        self.verticalLayout_17.addLayout(self.horizontalLayout_6)
        self.t1t2butsho = QtWidgets.QPushButton(self.tab_2)
        self.t1t2butsho.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(245, 224, 176, 255), stop:0.09 rgba(246, 189, 237, 255), stop:0.14 rgba(194, 207, 246, 255), stop:0.19 rgba(184, 160, 168, 255), stop:0.25 rgba(171, 186, 248, 255), stop:0.32 rgba(243, 248, 224, 255), stop:0.385 rgba(249, 162, 183, 255), stop:0.47 rgba(100, 115, 124, 255), stop:0.58 rgba(251, 205, 202, 255), stop:0.65 rgba(170, 128, 185, 255), stop:0.75 rgba(252, 222, 204, 255), stop:0.805 rgba(206, 122, 218, 255), stop:0.86 rgba(254, 223, 175, 255), stop:0.91 rgba(254, 236, 244, 255), stop:1 rgba(255, 191, 221, 255));")
        self.t1t2butsho.setObjectName("t1t2butsho")
        self.verticalLayout_17.addWidget(self.t1t2butsho)
        self.verticalLayout_18.addLayout(self.verticalLayout_17)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout()
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.label_38 = QtWidgets.QLabel(self.tab_2)
        self.label_38.setObjectName("label_38")
        self.verticalLayout_16.addWidget(self.label_38)
        self.gr50 = QtWidgets.QLineEdit(self.tab_2)
        self.gr50.setObjectName("gr50")
        self.verticalLayout_16.addWidget(self.gr50)
        self.as50 = QtWidgets.QLineEdit(self.tab_2)
        self.as50.setObjectName("as50")
        self.verticalLayout_16.addWidget(self.as50)
        self.ar50 = QtWidgets.QLineEdit(self.tab_2)
        self.ar50.setObjectName("ar50")
        self.verticalLayout_16.addWidget(self.ar50)
        self.en50 = QtWidgets.QLineEdit(self.tab_2)
        self.en50.setObjectName("en50")
        self.verticalLayout_16.addWidget(self.en50)
        self.re50 = QtWidgets.QLineEdit(self.tab_2)
        self.re50.setObjectName("re50")
        self.verticalLayout_16.addWidget(self.re50)
        self.ah50 = QtWidgets.QLineEdit(self.tab_2)
        self.ah50.setObjectName("ah50")
        self.verticalLayout_16.addWidget(self.ah50)
        self.ki50 = QtWidgets.QLineEdit(self.tab_2)
        self.ki50.setObjectName("ki50")
        self.verticalLayout_16.addWidget(self.ki50)
        self.vi50 = QtWidgets.QLineEdit(self.tab_2)
        self.vi50.setObjectName("vi50")
        self.verticalLayout_16.addWidget(self.vi50)
        self.jg50 = QtWidgets.QLineEdit(self.tab_2)
        self.jg50.setObjectName("jg50")
        self.verticalLayout_16.addWidget(self.jg50)
        self.tr50 = QtWidgets.QLineEdit(self.tab_2)
        self.tr50.setObjectName("tr50")
        self.verticalLayout_16.addWidget(self.tr50)
        self.mb50 = QtWidgets.QLineEdit(self.tab_2)
        self.mb50.setObjectName("mb50")
        self.verticalLayout_16.addWidget(self.mb50)
        self.al50 = QtWidgets.QLineEdit(self.tab_2)
        self.al50.setObjectName("al50")
        self.verticalLayout_16.addWidget(self.al50)
        self.jm50 = QtWidgets.QLineEdit(self.tab_2)
        self.jm50.setObjectName("jm50")
        self.verticalLayout_16.addWidget(self.jm50)
        self.ff50 = QtWidgets.QLineEdit(self.tab_2)
        self.ff50.setObjectName("ff50")
        self.verticalLayout_16.addWidget(self.ff50)
        self.mj50 = QtWidgets.QLineEdit(self.tab_2)
        self.mj50.setObjectName("mj50")
        self.verticalLayout_16.addWidget(self.mj50)
        self.horizontalLayout_4.addLayout(self.verticalLayout_16)
        self.verticalLayout_15 = QtWidgets.QVBoxLayout()
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.label_37 = QtWidgets.QLabel(self.tab_2)
        self.label_37.setObjectName("label_37")
        self.verticalLayout_15.addWidget(self.label_37)
        self.gr30 = QtWidgets.QLineEdit(self.tab_2)
        self.gr30.setObjectName("gr30")
        self.verticalLayout_15.addWidget(self.gr30)
        self.as30 = QtWidgets.QLineEdit(self.tab_2)
        self.as30.setObjectName("as30")
        self.verticalLayout_15.addWidget(self.as30)
        self.ar30 = QtWidgets.QLineEdit(self.tab_2)
        self.ar30.setObjectName("ar30")
        self.verticalLayout_15.addWidget(self.ar30)
        self.en30 = QtWidgets.QLineEdit(self.tab_2)
        self.en30.setObjectName("en30")
        self.verticalLayout_15.addWidget(self.en30)
        self.re30 = QtWidgets.QLineEdit(self.tab_2)
        self.re30.setObjectName("re30")
        self.verticalLayout_15.addWidget(self.re30)
        self.ah30 = QtWidgets.QLineEdit(self.tab_2)
        self.ah30.setObjectName("ah30")
        self.verticalLayout_15.addWidget(self.ah30)
        self.ki30 = QtWidgets.QLineEdit(self.tab_2)
        self.ki30.setObjectName("ki30")
        self.verticalLayout_15.addWidget(self.ki30)
        self.vi30 = QtWidgets.QLineEdit(self.tab_2)
        self.vi30.setObjectName("vi30")
        self.verticalLayout_15.addWidget(self.vi30)
        self.jg30 = QtWidgets.QLineEdit(self.tab_2)
        self.jg30.setObjectName("jg30")
        self.verticalLayout_15.addWidget(self.jg30)
        self.tr30 = QtWidgets.QLineEdit(self.tab_2)
        self.tr30.setObjectName("tr30")
        self.verticalLayout_15.addWidget(self.tr30)
        self.mb30 = QtWidgets.QLineEdit(self.tab_2)
        self.mb30.setObjectName("mb30")
        self.verticalLayout_15.addWidget(self.mb30)
        self.al30 = QtWidgets.QLineEdit(self.tab_2)
        self.al30.setObjectName("al30")
        self.verticalLayout_15.addWidget(self.al30)
        self.jm30 = QtWidgets.QLineEdit(self.tab_2)
        self.jm30.setObjectName("jm30")
        self.verticalLayout_15.addWidget(self.jm30)
        self.ff30 = QtWidgets.QLineEdit(self.tab_2)
        self.ff30.setObjectName("ff30")
        self.verticalLayout_15.addWidget(self.ff30)
        self.mj30 = QtWidgets.QLineEdit(self.tab_2)
        self.mj30.setObjectName("mj30")
        self.verticalLayout_15.addWidget(self.mj30)
        self.horizontalLayout_4.addLayout(self.verticalLayout_15)
        self.verticalLayout_14 = QtWidgets.QVBoxLayout()
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.label_36 = QtWidgets.QLabel(self.tab_2)
        self.label_36.setObjectName("label_36")
        self.verticalLayout_14.addWidget(self.label_36)
        self.gr20 = QtWidgets.QLineEdit(self.tab_2)
        self.gr20.setObjectName("gr20")
        self.verticalLayout_14.addWidget(self.gr20)
        self.as20 = QtWidgets.QLineEdit(self.tab_2)
        self.as20.setObjectName("as20")
        self.verticalLayout_14.addWidget(self.as20)
        self.ar20 = QtWidgets.QLineEdit(self.tab_2)
        self.ar20.setObjectName("ar20")
        self.verticalLayout_14.addWidget(self.ar20)
        self.en20 = QtWidgets.QLineEdit(self.tab_2)
        self.en20.setObjectName("en20")
        self.verticalLayout_14.addWidget(self.en20)
        self.re20 = QtWidgets.QLineEdit(self.tab_2)
        self.re20.setObjectName("re20")
        self.verticalLayout_14.addWidget(self.re20)
        self.ah20 = QtWidgets.QLineEdit(self.tab_2)
        self.ah20.setObjectName("ah20")
        self.verticalLayout_14.addWidget(self.ah20)
        self.ki20 = QtWidgets.QLineEdit(self.tab_2)
        self.ki20.setObjectName("ki20")
        self.verticalLayout_14.addWidget(self.ki20)
        self.vi20 = QtWidgets.QLineEdit(self.tab_2)
        self.vi20.setObjectName("vi20")
        self.verticalLayout_14.addWidget(self.vi20)
        self.jg20 = QtWidgets.QLineEdit(self.tab_2)
        self.jg20.setObjectName("jg20")
        self.verticalLayout_14.addWidget(self.jg20)
        self.tr20 = QtWidgets.QLineEdit(self.tab_2)
        self.tr20.setObjectName("tr20")
        self.verticalLayout_14.addWidget(self.tr20)
        self.mb20 = QtWidgets.QLineEdit(self.tab_2)
        self.mb20.setObjectName("mb20")
        self.verticalLayout_14.addWidget(self.mb20)
        self.al20 = QtWidgets.QLineEdit(self.tab_2)
        self.al20.setObjectName("al20")
        self.verticalLayout_14.addWidget(self.al20)
        self.jm20 = QtWidgets.QLineEdit(self.tab_2)
        self.jm20.setObjectName("jm20")
        self.verticalLayout_14.addWidget(self.jm20)
        self.ff20 = QtWidgets.QLineEdit(self.tab_2)
        self.ff20.setObjectName("ff20")
        self.verticalLayout_14.addWidget(self.ff20)
        self.mj20 = QtWidgets.QLineEdit(self.tab_2)
        self.mj20.setObjectName("mj20")
        self.verticalLayout_14.addWidget(self.mj20)
        self.horizontalLayout_4.addLayout(self.verticalLayout_14)
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_35 = QtWidgets.QLabel(self.tab_2)
        self.label_35.setObjectName("label_35")
        self.verticalLayout_13.addWidget(self.label_35)
        self.grsum2 = QtWidgets.QLineEdit(self.tab_2)
        self.grsum2.setObjectName("grsum2")
        self.verticalLayout_13.addWidget(self.grsum2)
        self.assum2 = QtWidgets.QLineEdit(self.tab_2)
        self.assum2.setObjectName("assum2")
        self.verticalLayout_13.addWidget(self.assum2)
        self.arsum2 = QtWidgets.QLineEdit(self.tab_2)
        self.arsum2.setObjectName("arsum2")
        self.verticalLayout_13.addWidget(self.arsum2)
        self.ensum2 = QtWidgets.QLineEdit(self.tab_2)
        self.ensum2.setObjectName("ensum2")
        self.verticalLayout_13.addWidget(self.ensum2)
        self.resum2 = QtWidgets.QLineEdit(self.tab_2)
        self.resum2.setObjectName("resum2")
        self.verticalLayout_13.addWidget(self.resum2)
        self.ahsum2 = QtWidgets.QLineEdit(self.tab_2)
        self.ahsum2.setObjectName("ahsum2")
        self.verticalLayout_13.addWidget(self.ahsum2)
        self.kisum2 = QtWidgets.QLineEdit(self.tab_2)
        self.kisum2.setObjectName("kisum2")
        self.verticalLayout_13.addWidget(self.kisum2)
        self.visum2 = QtWidgets.QLineEdit(self.tab_2)
        self.visum2.setObjectName("visum2")
        self.verticalLayout_13.addWidget(self.visum2)
        self.jgsum2 = QtWidgets.QLineEdit(self.tab_2)
        self.jgsum2.setObjectName("jgsum2")
        self.verticalLayout_13.addWidget(self.jgsum2)
        self.trsum2 = QtWidgets.QLineEdit(self.tab_2)
        self.trsum2.setObjectName("trsum2")
        self.verticalLayout_13.addWidget(self.trsum2)
        self.mbsum2 = QtWidgets.QLineEdit(self.tab_2)
        self.mbsum2.setObjectName("mbsum2")
        self.verticalLayout_13.addWidget(self.mbsum2)
        self.alsum2 = QtWidgets.QLineEdit(self.tab_2)
        self.alsum2.setObjectName("alsum2")
        self.verticalLayout_13.addWidget(self.alsum2)
        self.jmsum2 = QtWidgets.QLineEdit(self.tab_2)
        self.jmsum2.setObjectName("jmsum2")
        self.verticalLayout_13.addWidget(self.jmsum2)
        self.ffsum2 = QtWidgets.QLineEdit(self.tab_2)
        self.ffsum2.setObjectName("ffsum2")
        self.verticalLayout_13.addWidget(self.ffsum2)
        self.mjsum2 = QtWidgets.QLineEdit(self.tab_2)
        self.mjsum2.setObjectName("mjsum2")
        self.verticalLayout_13.addWidget(self.mjsum2)
        self.horizontalLayout_4.addLayout(self.verticalLayout_13)
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_34 = QtWidgets.QLabel(self.tab_2)
        self.label_34.setObjectName("label_34")
        self.verticalLayout_12.addWidget(self.label_34)
        self.grsum1 = QtWidgets.QLineEdit(self.tab_2)
        self.grsum1.setObjectName("grsum1")
        self.verticalLayout_12.addWidget(self.grsum1)
        self.assum1 = QtWidgets.QLineEdit(self.tab_2)
        self.assum1.setObjectName("assum1")
        self.verticalLayout_12.addWidget(self.assum1)
        self.arsum1 = QtWidgets.QLineEdit(self.tab_2)
        self.arsum1.setObjectName("arsum1")
        self.verticalLayout_12.addWidget(self.arsum1)
        self.ensum1 = QtWidgets.QLineEdit(self.tab_2)
        self.ensum1.setObjectName("ensum1")
        self.verticalLayout_12.addWidget(self.ensum1)
        self.resum1 = QtWidgets.QLineEdit(self.tab_2)
        self.resum1.setObjectName("resum1")
        self.verticalLayout_12.addWidget(self.resum1)
        self.ahsum1 = QtWidgets.QLineEdit(self.tab_2)
        self.ahsum1.setObjectName("ahsum1")
        self.verticalLayout_12.addWidget(self.ahsum1)
        self.kisum1 = QtWidgets.QLineEdit(self.tab_2)
        self.kisum1.setObjectName("kisum1")
        self.verticalLayout_12.addWidget(self.kisum1)
        self.visum1 = QtWidgets.QLineEdit(self.tab_2)
        self.visum1.setObjectName("visum1")
        self.verticalLayout_12.addWidget(self.visum1)
        self.jgsum1 = QtWidgets.QLineEdit(self.tab_2)
        self.jgsum1.setObjectName("jgsum1")
        self.verticalLayout_12.addWidget(self.jgsum1)
        self.trsum1 = QtWidgets.QLineEdit(self.tab_2)
        self.trsum1.setObjectName("trsum1")
        self.verticalLayout_12.addWidget(self.trsum1)
        self.mbsum1 = QtWidgets.QLineEdit(self.tab_2)
        self.mbsum1.setObjectName("mbsum1")
        self.verticalLayout_12.addWidget(self.mbsum1)
        self.alsum1 = QtWidgets.QLineEdit(self.tab_2)
        self.alsum1.setObjectName("alsum1")
        self.verticalLayout_12.addWidget(self.alsum1)
        self.jmsum1 = QtWidgets.QLineEdit(self.tab_2)
        self.jmsum1.setObjectName("jmsum1")
        self.verticalLayout_12.addWidget(self.jmsum1)
        self.ffsum1 = QtWidgets.QLineEdit(self.tab_2)
        self.ffsum1.setObjectName("ffsum1")
        self.verticalLayout_12.addWidget(self.ffsum1)
        self.mjsum1 = QtWidgets.QLineEdit(self.tab_2)
        self.mjsum1.setObjectName("mjsum1")
        self.verticalLayout_12.addWidget(self.mjsum1)
        self.horizontalLayout_4.addLayout(self.verticalLayout_12)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_33 = QtWidgets.QLabel(self.tab_2)
        self.label_33.setObjectName("label_33")
        self.verticalLayout_11.addWidget(self.label_33)
        self.grtest2 = QtWidgets.QLineEdit(self.tab_2)
        self.grtest2.setObjectName("grtest2")
        self.verticalLayout_11.addWidget(self.grtest2)
        self.astest2 = QtWidgets.QLineEdit(self.tab_2)
        self.astest2.setObjectName("astest2")
        self.verticalLayout_11.addWidget(self.astest2)
        self.artest2 = QtWidgets.QLineEdit(self.tab_2)
        self.artest2.setObjectName("artest2")
        self.verticalLayout_11.addWidget(self.artest2)
        self.entest2 = QtWidgets.QLineEdit(self.tab_2)
        self.entest2.setObjectName("entest2")
        self.verticalLayout_11.addWidget(self.entest2)
        self.retest2 = QtWidgets.QLineEdit(self.tab_2)
        self.retest2.setObjectName("retest2")
        self.verticalLayout_11.addWidget(self.retest2)
        self.ahtest2 = QtWidgets.QLineEdit(self.tab_2)
        self.ahtest2.setObjectName("ahtest2")
        self.verticalLayout_11.addWidget(self.ahtest2)
        self.kitest2 = QtWidgets.QLineEdit(self.tab_2)
        self.kitest2.setObjectName("kitest2")
        self.verticalLayout_11.addWidget(self.kitest2)
        self.vitest2 = QtWidgets.QLineEdit(self.tab_2)
        self.vitest2.setObjectName("vitest2")
        self.verticalLayout_11.addWidget(self.vitest2)
        self.jgtest2 = QtWidgets.QLineEdit(self.tab_2)
        self.jgtest2.setObjectName("jgtest2")
        self.verticalLayout_11.addWidget(self.jgtest2)
        self.trtest2 = QtWidgets.QLineEdit(self.tab_2)
        self.trtest2.setObjectName("trtest2")
        self.verticalLayout_11.addWidget(self.trtest2)
        self.altest2 = QtWidgets.QLineEdit(self.tab_2)
        self.altest2.setObjectName("altest2")
        self.verticalLayout_11.addWidget(self.altest2)
        self.mbtest2 = QtWidgets.QLineEdit(self.tab_2)
        self.mbtest2.setObjectName("mbtest2")
        self.verticalLayout_11.addWidget(self.mbtest2)
        self.jmtest2 = QtWidgets.QLineEdit(self.tab_2)
        self.jmtest2.setObjectName("jmtest2")
        self.verticalLayout_11.addWidget(self.jmtest2)
        self.fftest2 = QtWidgets.QLineEdit(self.tab_2)
        self.fftest2.setObjectName("fftest2")
        self.verticalLayout_11.addWidget(self.fftest2)
        self.mjtest2 = QtWidgets.QLineEdit(self.tab_2)
        self.mjtest2.setObjectName("mjtest2")
        self.verticalLayout_11.addWidget(self.mjtest2)
        self.horizontalLayout_4.addLayout(self.verticalLayout_11)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_31 = QtWidgets.QLabel(self.tab_2)
        self.label_31.setObjectName("label_31")
        self.verticalLayout_10.addWidget(self.label_31)
        self.grsh2 = QtWidgets.QLineEdit(self.tab_2)
        self.grsh2.setObjectName("grsh2")
        self.verticalLayout_10.addWidget(self.grsh2)
        self.assh2 = QtWidgets.QLineEdit(self.tab_2)
        self.assh2.setObjectName("assh2")
        self.verticalLayout_10.addWidget(self.assh2)
        self.arsh2 = QtWidgets.QLineEdit(self.tab_2)
        self.arsh2.setObjectName("arsh2")
        self.verticalLayout_10.addWidget(self.arsh2)
        self.ensh2 = QtWidgets.QLineEdit(self.tab_2)
        self.ensh2.setObjectName("ensh2")
        self.verticalLayout_10.addWidget(self.ensh2)
        self.resh2 = QtWidgets.QLineEdit(self.tab_2)
        self.resh2.setObjectName("resh2")
        self.verticalLayout_10.addWidget(self.resh2)
        self.ahsh2 = QtWidgets.QLineEdit(self.tab_2)
        self.ahsh2.setObjectName("ahsh2")
        self.verticalLayout_10.addWidget(self.ahsh2)
        self.kish2 = QtWidgets.QLineEdit(self.tab_2)
        self.kish2.setObjectName("kish2")
        self.verticalLayout_10.addWidget(self.kish2)
        self.vish2 = QtWidgets.QLineEdit(self.tab_2)
        self.vish2.setObjectName("vish2")
        self.verticalLayout_10.addWidget(self.vish2)
        self.jgsh2 = QtWidgets.QLineEdit(self.tab_2)
        self.jgsh2.setObjectName("jgsh2")
        self.verticalLayout_10.addWidget(self.jgsh2)
        self.trsh2 = QtWidgets.QLineEdit(self.tab_2)
        self.trsh2.setObjectName("trsh2")
        self.verticalLayout_10.addWidget(self.trsh2)
        self.mbsh2 = QtWidgets.QLineEdit(self.tab_2)
        self.mbsh2.setObjectName("mbsh2")
        self.verticalLayout_10.addWidget(self.mbsh2)
        self.alsh2 = QtWidgets.QLineEdit(self.tab_2)
        self.alsh2.setObjectName("alsh2")
        self.verticalLayout_10.addWidget(self.alsh2)
        self.jmsh2 = QtWidgets.QLineEdit(self.tab_2)
        self.jmsh2.setObjectName("jmsh2")
        self.verticalLayout_10.addWidget(self.jmsh2)
        self.ffsh2 = QtWidgets.QLineEdit(self.tab_2)
        self.ffsh2.setObjectName("ffsh2")
        self.verticalLayout_10.addWidget(self.ffsh2)
        self.mjsh2 = QtWidgets.QLineEdit(self.tab_2)
        self.mjsh2.setObjectName("mjsh2")
        self.verticalLayout_10.addWidget(self.mjsh2)
        self.horizontalLayout_4.addLayout(self.verticalLayout_10)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_30 = QtWidgets.QLabel(self.tab_2)
        self.label_30.setObjectName("label_30")
        self.verticalLayout_9.addWidget(self.label_30)
        self.grwork2 = QtWidgets.QLineEdit(self.tab_2)
        self.grwork2.setObjectName("grwork2")
        self.verticalLayout_9.addWidget(self.grwork2)
        self.aswork2 = QtWidgets.QLineEdit(self.tab_2)
        self.aswork2.setObjectName("aswork2")
        self.verticalLayout_9.addWidget(self.aswork2)
        self.arwork2 = QtWidgets.QLineEdit(self.tab_2)
        self.arwork2.setObjectName("arwork2")
        self.verticalLayout_9.addWidget(self.arwork2)
        self.enwork2 = QtWidgets.QLineEdit(self.tab_2)
        self.enwork2.setObjectName("enwork2")
        self.verticalLayout_9.addWidget(self.enwork2)
        self.rework2 = QtWidgets.QLineEdit(self.tab_2)
        self.rework2.setObjectName("rework2")
        self.verticalLayout_9.addWidget(self.rework2)
        self.ahwork2 = QtWidgets.QLineEdit(self.tab_2)
        self.ahwork2.setObjectName("ahwork2")
        self.verticalLayout_9.addWidget(self.ahwork2)
        self.kiwork2 = QtWidgets.QLineEdit(self.tab_2)
        self.kiwork2.setObjectName("kiwork2")
        self.verticalLayout_9.addWidget(self.kiwork2)
        self.viwork2 = QtWidgets.QLineEdit(self.tab_2)
        self.viwork2.setObjectName("viwork2")
        self.verticalLayout_9.addWidget(self.viwork2)
        self.jgwork2 = QtWidgets.QLineEdit(self.tab_2)
        self.jgwork2.setObjectName("jgwork2")
        self.verticalLayout_9.addWidget(self.jgwork2)
        self.trwork2 = QtWidgets.QLineEdit(self.tab_2)
        self.trwork2.setObjectName("trwork2")
        self.verticalLayout_9.addWidget(self.trwork2)
        self.mbwork2 = QtWidgets.QLineEdit(self.tab_2)
        self.mbwork2.setObjectName("mbwork2")
        self.verticalLayout_9.addWidget(self.mbwork2)
        self.alwork2 = QtWidgets.QLineEdit(self.tab_2)
        self.alwork2.setObjectName("alwork2")
        self.verticalLayout_9.addWidget(self.alwork2)
        self.jmwork2 = QtWidgets.QLineEdit(self.tab_2)
        self.jmwork2.setObjectName("jmwork2")
        self.verticalLayout_9.addWidget(self.jmwork2)
        self.ffwork2 = QtWidgets.QLineEdit(self.tab_2)
        self.ffwork2.setObjectName("ffwork2")
        self.verticalLayout_9.addWidget(self.ffwork2)
        self.mjwork2 = QtWidgets.QLineEdit(self.tab_2)
        self.mjwork2.setObjectName("mjwork2")
        self.verticalLayout_9.addWidget(self.mjwork2)
        self.horizontalLayout_4.addLayout(self.verticalLayout_9)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_32 = QtWidgets.QLabel(self.tab_2)
        self.label_32.setObjectName("label_32")
        self.verticalLayout_8.addWidget(self.label_32)
        self.grmo2 = QtWidgets.QLineEdit(self.tab_2)
        self.grmo2.setObjectName("grmo2")
        self.verticalLayout_8.addWidget(self.grmo2)
        self.asmo2 = QtWidgets.QLineEdit(self.tab_2)
        self.asmo2.setObjectName("asmo2")
        self.verticalLayout_8.addWidget(self.asmo2)
        self.armo2 = QtWidgets.QLineEdit(self.tab_2)
        self.armo2.setObjectName("armo2")
        self.verticalLayout_8.addWidget(self.armo2)
        self.enmo2 = QtWidgets.QLineEdit(self.tab_2)
        self.enmo2.setObjectName("enmo2")
        self.verticalLayout_8.addWidget(self.enmo2)
        self.remo2 = QtWidgets.QLineEdit(self.tab_2)
        self.remo2.setObjectName("remo2")
        self.verticalLayout_8.addWidget(self.remo2)
        self.ahmo2 = QtWidgets.QLineEdit(self.tab_2)
        self.ahmo2.setObjectName("ahmo2")
        self.verticalLayout_8.addWidget(self.ahmo2)
        self.kimo2 = QtWidgets.QLineEdit(self.tab_2)
        self.kimo2.setObjectName("kimo2")
        self.verticalLayout_8.addWidget(self.kimo2)
        self.vimo2 = QtWidgets.QLineEdit(self.tab_2)
        self.vimo2.setObjectName("vimo2")
        self.verticalLayout_8.addWidget(self.vimo2)
        self.jgmo2 = QtWidgets.QLineEdit(self.tab_2)
        self.jgmo2.setObjectName("jgmo2")
        self.verticalLayout_8.addWidget(self.jgmo2)
        self.trmo2 = QtWidgets.QLineEdit(self.tab_2)
        self.trmo2.setObjectName("trmo2")
        self.verticalLayout_8.addWidget(self.trmo2)
        self.mbmo2 = QtWidgets.QLineEdit(self.tab_2)
        self.mbmo2.setObjectName("mbmo2")
        self.verticalLayout_8.addWidget(self.mbmo2)
        self.almo2 = QtWidgets.QLineEdit(self.tab_2)
        self.almo2.setObjectName("almo2")
        self.verticalLayout_8.addWidget(self.almo2)
        self.jmmo2 = QtWidgets.QLineEdit(self.tab_2)
        self.jmmo2.setObjectName("jmmo2")
        self.verticalLayout_8.addWidget(self.jmmo2)
        self.ffmo2 = QtWidgets.QLineEdit(self.tab_2)
        self.ffmo2.setObjectName("ffmo2")
        self.verticalLayout_8.addWidget(self.ffmo2)
        self.mjmo2 = QtWidgets.QLineEdit(self.tab_2)
        self.mjmo2.setObjectName("mjmo2")
        self.verticalLayout_8.addWidget(self.mjmo2)
        self.horizontalLayout_4.addLayout(self.verticalLayout_8)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_29 = QtWidgets.QLabel(self.tab_2)
        self.label_29.setObjectName("label_29")
        self.verticalLayout_7.addWidget(self.label_29)
        self.grtest1 = QtWidgets.QLineEdit(self.tab_2)
        self.grtest1.setObjectName("grtest1")
        self.verticalLayout_7.addWidget(self.grtest1)
        self.astest1 = QtWidgets.QLineEdit(self.tab_2)
        self.astest1.setObjectName("astest1")
        self.verticalLayout_7.addWidget(self.astest1)
        self.artest1 = QtWidgets.QLineEdit(self.tab_2)
        self.artest1.setObjectName("artest1")
        self.verticalLayout_7.addWidget(self.artest1)
        self.entest1 = QtWidgets.QLineEdit(self.tab_2)
        self.entest1.setObjectName("entest1")
        self.verticalLayout_7.addWidget(self.entest1)
        self.retest1 = QtWidgets.QLineEdit(self.tab_2)
        self.retest1.setObjectName("retest1")
        self.verticalLayout_7.addWidget(self.retest1)
        self.ahtest1 = QtWidgets.QLineEdit(self.tab_2)
        self.ahtest1.setObjectName("ahtest1")
        self.verticalLayout_7.addWidget(self.ahtest1)
        self.kitest1 = QtWidgets.QLineEdit(self.tab_2)
        self.kitest1.setObjectName("kitest1")
        self.verticalLayout_7.addWidget(self.kitest1)
        self.vitest1 = QtWidgets.QLineEdit(self.tab_2)
        self.vitest1.setObjectName("vitest1")
        self.verticalLayout_7.addWidget(self.vitest1)
        self.jgtest1 = QtWidgets.QLineEdit(self.tab_2)
        self.jgtest1.setObjectName("jgtest1")
        self.verticalLayout_7.addWidget(self.jgtest1)
        self.trtest1 = QtWidgets.QLineEdit(self.tab_2)
        self.trtest1.setObjectName("trtest1")
        self.verticalLayout_7.addWidget(self.trtest1)
        self.mbtest1 = QtWidgets.QLineEdit(self.tab_2)
        self.mbtest1.setObjectName("mbtest1")
        self.verticalLayout_7.addWidget(self.mbtest1)
        self.altest1 = QtWidgets.QLineEdit(self.tab_2)
        self.altest1.setObjectName("altest1")
        self.verticalLayout_7.addWidget(self.altest1)
        self.jmtest1 = QtWidgets.QLineEdit(self.tab_2)
        self.jmtest1.setObjectName("jmtest1")
        self.verticalLayout_7.addWidget(self.jmtest1)
        self.fftest1 = QtWidgets.QLineEdit(self.tab_2)
        self.fftest1.setObjectName("fftest1")
        self.verticalLayout_7.addWidget(self.fftest1)
        self.mjtest1 = QtWidgets.QLineEdit(self.tab_2)
        self.mjtest1.setObjectName("mjtest1")
        self.verticalLayout_7.addWidget(self.mjtest1)
        self.horizontalLayout_4.addLayout(self.verticalLayout_7)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_28 = QtWidgets.QLabel(self.tab_2)
        self.label_28.setObjectName("label_28")
        self.verticalLayout_6.addWidget(self.label_28)
        self.grsh1 = QtWidgets.QLineEdit(self.tab_2)
        self.grsh1.setObjectName("grsh1")
        self.verticalLayout_6.addWidget(self.grsh1)
        self.assh1 = QtWidgets.QLineEdit(self.tab_2)
        self.assh1.setObjectName("assh1")
        self.verticalLayout_6.addWidget(self.assh1)
        self.arsh1 = QtWidgets.QLineEdit(self.tab_2)
        self.arsh1.setObjectName("arsh1")
        self.verticalLayout_6.addWidget(self.arsh1)
        self.ensh1 = QtWidgets.QLineEdit(self.tab_2)
        self.ensh1.setObjectName("ensh1")
        self.verticalLayout_6.addWidget(self.ensh1)
        self.resh1 = QtWidgets.QLineEdit(self.tab_2)
        self.resh1.setObjectName("resh1")
        self.verticalLayout_6.addWidget(self.resh1)
        self.ahsh1 = QtWidgets.QLineEdit(self.tab_2)
        self.ahsh1.setObjectName("ahsh1")
        self.verticalLayout_6.addWidget(self.ahsh1)
        self.kish1 = QtWidgets.QLineEdit(self.tab_2)
        self.kish1.setObjectName("kish1")
        self.verticalLayout_6.addWidget(self.kish1)
        self.vish1 = QtWidgets.QLineEdit(self.tab_2)
        self.vish1.setObjectName("vish1")
        self.verticalLayout_6.addWidget(self.vish1)
        self.jgsh1 = QtWidgets.QLineEdit(self.tab_2)
        self.jgsh1.setObjectName("jgsh1")
        self.verticalLayout_6.addWidget(self.jgsh1)
        self.trsh1 = QtWidgets.QLineEdit(self.tab_2)
        self.trsh1.setObjectName("trsh1")
        self.verticalLayout_6.addWidget(self.trsh1)
        self.mbsh1 = QtWidgets.QLineEdit(self.tab_2)
        self.mbsh1.setObjectName("mbsh1")
        self.verticalLayout_6.addWidget(self.mbsh1)
        self.alsh1 = QtWidgets.QLineEdit(self.tab_2)
        self.alsh1.setObjectName("alsh1")
        self.verticalLayout_6.addWidget(self.alsh1)
        self.jmsh1 = QtWidgets.QLineEdit(self.tab_2)
        self.jmsh1.setObjectName("jmsh1")
        self.verticalLayout_6.addWidget(self.jmsh1)
        self.ffsh1 = QtWidgets.QLineEdit(self.tab_2)
        self.ffsh1.setObjectName("ffsh1")
        self.verticalLayout_6.addWidget(self.ffsh1)
        self.mjsh1 = QtWidgets.QLineEdit(self.tab_2)
        self.mjsh1.setObjectName("mjsh1")
        self.verticalLayout_6.addWidget(self.mjsh1)
        self.horizontalLayout_4.addLayout(self.verticalLayout_6)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_27 = QtWidgets.QLabel(self.tab_2)
        self.label_27.setObjectName("label_27")
        self.verticalLayout_5.addWidget(self.label_27)
        self.grwork1 = QtWidgets.QLineEdit(self.tab_2)
        self.grwork1.setObjectName("grwork1")
        self.verticalLayout_5.addWidget(self.grwork1)
        self.aswork1 = QtWidgets.QLineEdit(self.tab_2)
        self.aswork1.setObjectName("aswork1")
        self.verticalLayout_5.addWidget(self.aswork1)
        self.arwork1 = QtWidgets.QLineEdit(self.tab_2)
        self.arwork1.setObjectName("arwork1")
        self.verticalLayout_5.addWidget(self.arwork1)
        self.enwork1 = QtWidgets.QLineEdit(self.tab_2)
        self.enwork1.setObjectName("enwork1")
        self.verticalLayout_5.addWidget(self.enwork1)
        self.rework1 = QtWidgets.QLineEdit(self.tab_2)
        self.rework1.setObjectName("rework1")
        self.verticalLayout_5.addWidget(self.rework1)
        self.ahwork1 = QtWidgets.QLineEdit(self.tab_2)
        self.ahwork1.setObjectName("ahwork1")
        self.verticalLayout_5.addWidget(self.ahwork1)
        self.kiwork1 = QtWidgets.QLineEdit(self.tab_2)
        self.kiwork1.setObjectName("kiwork1")
        self.verticalLayout_5.addWidget(self.kiwork1)
        self.viwork1 = QtWidgets.QLineEdit(self.tab_2)
        self.viwork1.setObjectName("viwork1")
        self.verticalLayout_5.addWidget(self.viwork1)
        self.jgwork1 = QtWidgets.QLineEdit(self.tab_2)
        self.jgwork1.setObjectName("jgwork1")
        self.verticalLayout_5.addWidget(self.jgwork1)
        self.trwork1 = QtWidgets.QLineEdit(self.tab_2)
        self.trwork1.setObjectName("trwork1")
        self.verticalLayout_5.addWidget(self.trwork1)
        self.mbwork1 = QtWidgets.QLineEdit(self.tab_2)
        self.mbwork1.setObjectName("mbwork1")
        self.verticalLayout_5.addWidget(self.mbwork1)
        self.alwork1 = QtWidgets.QLineEdit(self.tab_2)
        self.alwork1.setObjectName("alwork1")
        self.verticalLayout_5.addWidget(self.alwork1)
        self.jmwork1 = QtWidgets.QLineEdit(self.tab_2)
        self.jmwork1.setObjectName("jmwork1")
        self.verticalLayout_5.addWidget(self.jmwork1)
        self.ffwork1 = QtWidgets.QLineEdit(self.tab_2)
        self.ffwork1.setObjectName("ffwork1")
        self.verticalLayout_5.addWidget(self.ffwork1)
        self.mjwork1 = QtWidgets.QLineEdit(self.tab_2)
        self.mjwork1.setObjectName("mjwork1")
        self.verticalLayout_5.addWidget(self.mjwork1)
        self.horizontalLayout_4.addLayout(self.verticalLayout_5)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_26 = QtWidgets.QLabel(self.tab_2)
        self.label_26.setObjectName("label_26")
        self.verticalLayout_4.addWidget(self.label_26)
        self.grmo1 = QtWidgets.QLineEdit(self.tab_2)
        self.grmo1.setObjectName("grmo1")
        self.verticalLayout_4.addWidget(self.grmo1)
        self.asmo1 = QtWidgets.QLineEdit(self.tab_2)
        self.asmo1.setObjectName("asmo1")
        self.verticalLayout_4.addWidget(self.asmo1)
        self.armo1 = QtWidgets.QLineEdit(self.tab_2)
        self.armo1.setObjectName("armo1")
        self.verticalLayout_4.addWidget(self.armo1)
        self.enmo1 = QtWidgets.QLineEdit(self.tab_2)
        self.enmo1.setObjectName("enmo1")
        self.verticalLayout_4.addWidget(self.enmo1)
        self.remo1 = QtWidgets.QLineEdit(self.tab_2)
        self.remo1.setObjectName("remo1")
        self.verticalLayout_4.addWidget(self.remo1)
        self.ahmo1 = QtWidgets.QLineEdit(self.tab_2)
        self.ahmo1.setObjectName("ahmo1")
        self.verticalLayout_4.addWidget(self.ahmo1)
        self.kimo1 = QtWidgets.QLineEdit(self.tab_2)
        self.kimo1.setObjectName("kimo1")
        self.verticalLayout_4.addWidget(self.kimo1)
        self.vimo1 = QtWidgets.QLineEdit(self.tab_2)
        self.vimo1.setObjectName("vimo1")
        self.verticalLayout_4.addWidget(self.vimo1)
        self.jgmo1 = QtWidgets.QLineEdit(self.tab_2)
        self.jgmo1.setObjectName("jgmo1")
        self.verticalLayout_4.addWidget(self.jgmo1)
        self.trmo1 = QtWidgets.QLineEdit(self.tab_2)
        self.trmo1.setObjectName("trmo1")
        self.verticalLayout_4.addWidget(self.trmo1)
        self.mbmo1 = QtWidgets.QLineEdit(self.tab_2)
        self.mbmo1.setObjectName("mbmo1")
        self.verticalLayout_4.addWidget(self.mbmo1)
        self.almo1 = QtWidgets.QLineEdit(self.tab_2)
        self.almo1.setObjectName("almo1")
        self.verticalLayout_4.addWidget(self.almo1)
        self.jmmo1 = QtWidgets.QLineEdit(self.tab_2)
        self.jmmo1.setObjectName("jmmo1")
        self.verticalLayout_4.addWidget(self.jmmo1)
        self.ffmo1 = QtWidgets.QLineEdit(self.tab_2)
        self.ffmo1.setObjectName("ffmo1")
        self.verticalLayout_4.addWidget(self.ffmo1)
        self.mjmo1 = QtWidgets.QLineEdit(self.tab_2)
        self.mjmo1.setObjectName("mjmo1")
        self.verticalLayout_4.addWidget(self.mjmo1)
        self.horizontalLayout_4.addLayout(self.verticalLayout_4)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_11 = QtWidgets.QLabel(self.tab_2)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_3.addWidget(self.label_11)
        self.label_12 = QtWidgets.QLabel(self.tab_2)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_3.addWidget(self.label_12)
        self.label_13 = QtWidgets.QLabel(self.tab_2)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_3.addWidget(self.label_13)
        self.label_14 = QtWidgets.QLabel(self.tab_2)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_3.addWidget(self.label_14)
        self.label_15 = QtWidgets.QLabel(self.tab_2)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_3.addWidget(self.label_15)
        self.label_16 = QtWidgets.QLabel(self.tab_2)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_3.addWidget(self.label_16)
        self.label_17 = QtWidgets.QLabel(self.tab_2)
        self.label_17.setObjectName("label_17")
        self.verticalLayout_3.addWidget(self.label_17)
        self.label_18 = QtWidgets.QLabel(self.tab_2)
        self.label_18.setObjectName("label_18")
        self.verticalLayout_3.addWidget(self.label_18)
        self.label_19 = QtWidgets.QLabel(self.tab_2)
        self.label_19.setObjectName("label_19")
        self.verticalLayout_3.addWidget(self.label_19)
        self.label_20 = QtWidgets.QLabel(self.tab_2)
        self.label_20.setObjectName("label_20")
        self.verticalLayout_3.addWidget(self.label_20)
        self.label_21 = QtWidgets.QLabel(self.tab_2)
        self.label_21.setObjectName("label_21")
        self.verticalLayout_3.addWidget(self.label_21)
        self.label_22 = QtWidgets.QLabel(self.tab_2)
        self.label_22.setObjectName("label_22")
        self.verticalLayout_3.addWidget(self.label_22)
        self.label_23 = QtWidgets.QLabel(self.tab_2)
        self.label_23.setObjectName("label_23")
        self.verticalLayout_3.addWidget(self.label_23)
        self.label_24 = QtWidgets.QLabel(self.tab_2)
        self.label_24.setObjectName("label_24")
        self.verticalLayout_3.addWidget(self.label_24)
        self.label_25 = QtWidgets.QLabel(self.tab_2)
        self.label_25.setObjectName("label_25")
        self.verticalLayout_3.addWidget(self.label_25)
        self.label_41 = QtWidgets.QLabel(self.tab_2)
        self.label_41.setObjectName("label_41")
        self.verticalLayout_3.addWidget(self.label_41)
        self.horizontalLayout_4.addLayout(self.verticalLayout_3)
        self.verticalLayout_18.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.t1t2butdeletstu = QtWidgets.QPushButton(self.tab_2)
        self.t1t2butdeletstu.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(245, 224, 176, 255), stop:0.09 rgba(246, 189, 237, 255), stop:0.14 rgba(194, 207, 246, 255), stop:0.19 rgba(184, 160, 168, 255), stop:0.25 rgba(171, 186, 248, 255), stop:0.32 rgba(243, 248, 224, 255), stop:0.385 rgba(249, 162, 183, 255), stop:0.47 rgba(100, 115, 124, 255), stop:0.58 rgba(251, 205, 202, 255), stop:0.65 rgba(170, 128, 185, 255), stop:0.75 rgba(252, 222, 204, 255), stop:0.805 rgba(206, 122, 218, 255), stop:0.86 rgba(254, 223, 175, 255), stop:0.91 rgba(254, 236, 244, 255), stop:1 rgba(255, 191, 221, 255));")
        self.t1t2butdeletstu.setObjectName("t1t2butdeletstu")
        self.horizontalLayout_5.addWidget(self.t1t2butdeletstu)
        self.t1t2butsavmod = QtWidgets.QPushButton(self.tab_2)
        self.t1t2butsavmod.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(245, 224, 176, 255), stop:0.09 rgba(246, 189, 237, 255), stop:0.14 rgba(194, 207, 246, 255), stop:0.19 rgba(184, 160, 168, 255), stop:0.25 rgba(171, 186, 248, 255), stop:0.32 rgba(243, 248, 224, 255), stop:0.385 rgba(249, 162, 183, 255), stop:0.47 rgba(100, 115, 124, 255), stop:0.58 rgba(251, 205, 202, 255), stop:0.65 rgba(170, 128, 185, 255), stop:0.75 rgba(252, 222, 204, 255), stop:0.805 rgba(206, 122, 218, 255), stop:0.86 rgba(254, 223, 175, 255), stop:0.91 rgba(254, 236, 244, 255), stop:1 rgba(255, 191, 221, 255));")
        self.t1t2butsavmod.setObjectName("t1t2butsavmod")
        self.horizontalLayout_5.addWidget(self.t1t2butsavmod)
        self.t1t2enrateo = QtWidgets.QLineEdit(self.tab_2)
        self.t1t2enrateo.setObjectName("t1t2enrateo")
        self.horizontalLayout_5.addWidget(self.t1t2enrateo)
        self.label_40 = QtWidgets.QLabel(self.tab_2)
        self.label_40.setObjectName("label_40")
        self.horizontalLayout_5.addWidget(self.label_40)
        self.t1t2ensumall = QtWidgets.QLineEdit(self.tab_2)
        self.t1t2ensumall.setObjectName("t1t2ensumall")
        self.horizontalLayout_5.addWidget(self.t1t2ensumall)
        self.label_39 = QtWidgets.QLabel(self.tab_2)
        self.label_39.setObjectName("label_39")
        self.horizontalLayout_5.addWidget(self.label_39)
        self.verticalLayout_18.addLayout(self.horizontalLayout_5)
        self.gridLayout_5.addLayout(self.verticalLayout_18, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.verticalLayout_55 = QtWidgets.QVBoxLayout()
        self.verticalLayout_55.setObjectName("verticalLayout_55")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.t1t3comnamstud = QtWidgets.QComboBox(self.tab_3)
        self.t1t3comnamstud.setEditable(True)
        self.t1t3comnamstud.setObjectName("t1t3comnamstud")
        self.horizontalLayout_19.addWidget(self.t1t3comnamstud)
        self.label_128 = QtWidgets.QLabel(self.tab_3)
        self.label_128.setObjectName("label_128")
        self.horizontalLayout_19.addWidget(self.label_128)
        self.t1t3comnamerow = QtWidgets.QComboBox(self.tab_3)
        self.t1t3comnamerow.setObjectName("t1t3comnamerow")
        self.horizontalLayout_19.addWidget(self.t1t3comnamerow)
        self.label_84 = QtWidgets.QLabel(self.tab_3)
        self.label_84.setObjectName("label_84")
        self.horizontalLayout_19.addWidget(self.label_84)
        self.t1t3comrow = QtWidgets.QComboBox(self.tab_3)
        self.t1t3comrow.setObjectName("t1t3comrow")
        self.t1t3comrow.addItem("")
        self.t1t3comrow.addItem("")
        self.t1t3comrow.addItem("")
        self.t1t3comrow.addItem("")
        self.t1t3comrow.addItem("")
        self.horizontalLayout_19.addWidget(self.t1t3comrow)
        self.label_83 = QtWidgets.QLabel(self.tab_3)
        self.label_83.setObjectName("label_83")
        self.horizontalLayout_19.addWidget(self.label_83)
        self.verticalLayout_55.addLayout(self.horizontalLayout_19)
        self.t1t3butprint1 = QtWidgets.QPushButton(self.tab_3)
        self.t1t3butprint1.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(245, 224, 176, 255), stop:0.09 rgba(246, 189, 237, 255), stop:0.14 rgba(194, 207, 246, 255), stop:0.19 rgba(184, 160, 168, 255), stop:0.25 rgba(171, 186, 248, 255), stop:0.32 rgba(243, 248, 224, 255), stop:0.385 rgba(249, 162, 183, 255), stop:0.47 rgba(100, 115, 124, 255), stop:0.58 rgba(251, 205, 202, 255), stop:0.65 rgba(170, 128, 185, 255), stop:0.75 rgba(252, 222, 204, 255), stop:0.805 rgba(206, 122, 218, 255), stop:0.86 rgba(254, 223, 175, 255), stop:0.91 rgba(254, 236, 244, 255), stop:1 rgba(255, 191, 221, 255));")
        self.t1t3butprint1.setObjectName("t1t3butprint1")
        self.verticalLayout_55.addWidget(self.t1t3butprint1)
        self.t1t3butshoanyrow = QtWidgets.QPushButton(self.tab_3)
        self.t1t3butshoanyrow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(245, 224, 176, 255), stop:0.09 rgba(246, 189, 237, 255), stop:0.14 rgba(194, 207, 246, 255), stop:0.19 rgba(184, 160, 168, 255), stop:0.25 rgba(171, 186, 248, 255), stop:0.32 rgba(243, 248, 224, 255), stop:0.385 rgba(249, 162, 183, 255), stop:0.47 rgba(100, 115, 124, 255), stop:0.58 rgba(251, 205, 202, 255), stop:0.65 rgba(170, 128, 185, 255), stop:0.75 rgba(252, 222, 204, 255), stop:0.805 rgba(206, 122, 218, 255), stop:0.86 rgba(254, 223, 175, 255), stop:0.91 rgba(254, 236, 244, 255), stop:1 rgba(255, 191, 221, 255));")
        self.t1t3butshoanyrow.setObjectName("t1t3butshoanyrow")
        self.verticalLayout_55.addWidget(self.t1t3butshoanyrow)
        self.textEdit1 = QtWidgets.QTextEdit(self.tab_3)
        self.textEdit1.setObjectName("textEdit1")
        self.verticalLayout_55.addWidget(self.textEdit1)
        self.gridLayout_10.addLayout(self.verticalLayout_55, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_10 = QtWidgets.QWidget()
        self.tab_10.setObjectName("tab_10")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.tab_10)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.verticalLayout_56 = QtWidgets.QVBoxLayout()
        self.verticalLayout_56.setObjectName("verticalLayout_56")
        self.splitter_8 = QtWidgets.QSplitter(self.tab_10)
        self.splitter_8.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_8.setObjectName("splitter_8")
        self.t1t4comnameobject = QtWidgets.QComboBox(self.splitter_8)
        self.t1t4comnameobject.setEditable(True)
        self.t1t4comnameobject.setObjectName("t1t4comnameobject")
        self.label_132 = QtWidgets.QLabel(self.splitter_8)
        self.label_132.setObjectName("label_132")
        self.t1t4comnamerow = QtWidgets.QComboBox(self.splitter_8)
        self.t1t4comnamerow.setObjectName("t1t4comnamerow")
        self.label_130 = QtWidgets.QLabel(self.splitter_8)
        self.label_130.setObjectName("label_130")
        self.t1t4comrow = QtWidgets.QComboBox(self.splitter_8)
        self.t1t4comrow.setObjectName("t1t4comrow")
        self.t1t4comrow.addItem("")
        self.t1t4comrow.addItem("")
        self.t1t4comrow.addItem("")
        self.t1t4comrow.addItem("")
        self.t1t4comrow.addItem("")
        self.label_129 = QtWidgets.QLabel(self.splitter_8)
        self.label_129.setObjectName("label_129")
        self.verticalLayout_56.addWidget(self.splitter_8)
        self.t1t4butshostudobjct = QtWidgets.QPushButton(self.tab_10)
        self.t1t4butshostudobjct.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(245, 224, 176, 255), stop:0.09 rgba(246, 189, 237, 255), stop:0.14 rgba(194, 207, 246, 255), stop:0.19 rgba(184, 160, 168, 255), stop:0.25 rgba(171, 186, 248, 255), stop:0.32 rgba(243, 248, 224, 255), stop:0.385 rgba(249, 162, 183, 255), stop:0.47 rgba(100, 115, 124, 255), stop:0.58 rgba(251, 205, 202, 255), stop:0.65 rgba(170, 128, 185, 255), stop:0.75 rgba(252, 222, 204, 255), stop:0.805 rgba(206, 122, 218, 255), stop:0.86 rgba(254, 223, 175, 255), stop:0.91 rgba(254, 236, 244, 255), stop:1 rgba(255, 191, 221, 255));")
        self.t1t4butshostudobjct.setObjectName("t1t4butshostudobjct")
        self.verticalLayout_56.addWidget(self.t1t4butshostudobjct)
        self.t1t4butprint2 = QtWidgets.QPushButton(self.tab_10)
        self.t1t4butprint2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(245, 224, 176, 255), stop:0.09 rgba(246, 189, 237, 255), stop:0.14 rgba(194, 207, 246, 255), stop:0.19 rgba(184, 160, 168, 255), stop:0.25 rgba(171, 186, 248, 255), stop:0.32 rgba(243, 248, 224, 255), stop:0.385 rgba(249, 162, 183, 255), stop:0.47 rgba(100, 115, 124, 255), stop:0.58 rgba(251, 205, 202, 255), stop:0.65 rgba(170, 128, 185, 255), stop:0.75 rgba(252, 222, 204, 255), stop:0.805 rgba(206, 122, 218, 255), stop:0.86 rgba(254, 223, 175, 255), stop:0.91 rgba(254, 236, 244, 255), stop:1 rgba(255, 191, 221, 255));")
        self.t1t4butprint2.setObjectName("t1t4butprint2")
        self.verticalLayout_56.addWidget(self.t1t4butprint2)
        self.textEdit2 = QtWidgets.QTextEdit(self.tab_10)
        self.textEdit2.setObjectName("textEdit2")
        self.verticalLayout_56.addWidget(self.textEdit2)
        self.gridLayout_11.addLayout(self.verticalLayout_56, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_10, "")
        self.gridLayout_2.addWidget(self.tabWidget, 0, 1, 1, 1)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.page_2)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout()
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.page_2)
        self.calendarWidget.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(9, 41, 4, 255), stop:0.085 rgba(2, 79, 0, 255), stop:0.19 rgba(50, 147, 22, 255), stop:0.275 rgba(236, 191, 49, 255), stop:0.39 rgba(243, 61, 34, 255), stop:0.555 rgba(135, 81, 60, 255), stop:0.667 rgba(121, 75, 255, 255), stop:0.825 rgba(164, 255, 244, 255), stop:0.885 rgba(104, 222, 71, 255), stop:1 rgba(93, 128, 0, 255));")
        self.calendarWidget.setGridVisible(True)
        self.calendarWidget.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.ISOWeekNumbers)
        self.calendarWidget.setObjectName("calendarWidget")
        self.verticalLayout_19.addWidget(self.calendarWidget)
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.page_2)
        self.dateTimeEdit.setStyleSheet("font: 75 16pt \"Noto Sans Bengali\";\n"
"color: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(35, 40, 3, 255), stop:0.16 rgba(136, 106, 22, 255), stop:0.225 rgba(166, 140, 41, 255), stop:0.285 rgba(204, 181, 74, 255), stop:0.345 rgba(235, 219, 102, 255), stop:0.415 rgba(245, 236, 112, 255), stop:0.52 rgba(209, 190, 76, 255), stop:0.57 rgba(187, 156, 51, 255), stop:0.635 rgba(168, 142, 42, 255), stop:0.695 rgba(202, 174, 68, 255), stop:0.75 rgba(218, 202, 86, 255), stop:0.815 rgba(208, 187, 73, 255), stop:0.88 rgba(187, 156, 51, 255), stop:0.935 rgba(137, 108, 26, 255), stop:1 rgba(35, 40, 3, 255));")
        self.dateTimeEdit.setFrame(True)
        self.dateTimeEdit.setReadOnly(False)
        self.dateTimeEdit.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.dateTimeEdit.setAccelerated(False)
        self.dateTimeEdit.setKeyboardTracking(True)
        self.dateTimeEdit.setTimeSpec(QtCore.Qt.LocalTime)
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.verticalLayout_19.addWidget(self.dateTimeEdit)
        self.scrollArea = QtWidgets.QScrollArea(self.page_2)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 769, 313))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.btnaddnotc = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.btnaddnotc.setObjectName("btnaddnotc")
        self.horizontalLayout_7.addWidget(self.btnaddnotc)
        self.btnmchn = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.btnmchn.setObjectName("btnmchn")
        self.horizontalLayout_7.addWidget(self.btnmchn)
        self.gridLayout_7.addLayout(self.horizontalLayout_7, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_19.addWidget(self.scrollArea)
        self.gridLayout_6.addLayout(self.verticalLayout_19, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_2)
        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 977, 27))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.dockWidget_3 = QtWidgets.QDockWidget(MainWindow)
        self.dockWidget_3.setStyleSheet("font: 75 oblique 14pt \"Noto Sans Armenian\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(245, 224, 176, 255), stop:0.09 rgba(246, 189, 237, 255), stop:0.14 rgba(194, 207, 246, 255), stop:0.19 rgba(184, 160, 168, 255), stop:0.25 rgba(171, 186, 248, 255), stop:0.32 rgba(243, 248, 224, 255), stop:0.385 rgba(249, 162, 183, 255), stop:0.47 rgba(100, 115, 124, 255), stop:0.58 rgba(251, 205, 202, 255), stop:0.65 rgba(170, 128, 185, 255), stop:0.75 rgba(252, 222, 204, 255), stop:0.805 rgba(206, 122, 218, 255), stop:0.86 rgba(254, 223, 175, 255), stop:0.91 rgba(254, 236, 244, 255), stop:1 rgba(255, 191, 221, 255));")
        self.dockWidget_3.setFloating(False)
        self.dockWidget_3.setFeatures(QtWidgets.QDockWidget.DockWidgetFloatable|QtWidgets.QDockWidget.DockWidgetMovable|QtWidgets.QDockWidget.DockWidgetVerticalTitleBar)
        self.dockWidget_3.setObjectName("dockWidget_3")
        self.dockWidgetContents_3 = QtWidgets.QWidget()
        self.dockWidgetContents_3.setObjectName("dockWidgetContents_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.dockWidgetContents_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.splitter = QtWidgets.QSplitter(self.dockWidgetContents_3)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.butterm1 = QtWidgets.QPushButton(self.splitter)
        self.butterm1.setObjectName("butterm1")
        self.butterm2 = QtWidgets.QPushButton(self.splitter)
        self.butterm2.setObjectName("butterm2")
        self.butaddtion = QtWidgets.QPushButton(self.splitter)
        self.butaddtion.setObjectName("butaddtion")
        self.butexite = QtWidgets.QPushButton(self.splitter)
        self.butexite.setObjectName("butexite")
        self.gridLayout_3.addWidget(self.splitter, 0, 0, 1, 1)
        self.dockWidget_3.setWidget(self.dockWidgetContents_3)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockWidget_3)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "اضافة صف جديد:"))
        self.label_2.setText(_translate("MainWindow", "اسم الصف:"))
        self.t1t1comrowaddnewrow.setItemText(0, _translate("MainWindow", "اولى ثانوي"))
        self.t1t1comrowaddnewrow.setItemText(1, _translate("MainWindow", "ثاني علمي"))
        self.t1t1comrowaddnewrow.setItemText(2, _translate("MainWindow", "ثالث علمي"))
        self.t1t1comrowaddnewrow.setItemText(3, _translate("MainWindow", "ثاني ادبي"))
        self.t1t1comrowaddnewrow.setItemText(4, _translate("MainWindow", "ثالث ادبي"))
        self.label.setText(_translate("MainWindow", "الصف:"))
        self.t1t1butaddrow.setText(_translate("MainWindow", "اضافة الصف"))
        self.label_4.setText(_translate("MainWindow", "اضافة طالب جديد:"))
        self.t1t1comaddstudrow.setItemText(0, _translate("MainWindow", "اولى ثانوي"))
        self.t1t1comaddstudrow.setItemText(1, _translate("MainWindow", "ثاني علمي"))
        self.t1t1comaddstudrow.setItemText(2, _translate("MainWindow", "ثالث علمي"))
        self.t1t1comaddstudrow.setItemText(3, _translate("MainWindow", "ثاني ادبي"))
        self.t1t1comaddstudrow.setItemText(4, _translate("MainWindow", "ثالث ادبي"))
        self.label_5.setText(_translate("MainWindow", "الصف:"))
        self.label_7.setText(_translate("MainWindow", "اسم الطالب:"))
        self.t1t1butrefrs.setText(_translate("MainWindow", "تحديث"))
        self.t1t1butaddnamestud.setText(_translate("MainWindow", "اضافة طالب"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "الاضافات الجديدة"))
        self.label_10.setText(_translate("MainWindow", "اسم الطالب:"))
        self.label_9.setText(_translate("MainWindow", "اسم الصف:"))
        self.t1t2comrow.setItemText(0, _translate("MainWindow", "اولى ثانوي"))
        self.t1t2comrow.setItemText(1, _translate("MainWindow", "ثانية علمي"))
        self.t1t2comrow.setItemText(2, _translate("MainWindow", "ثالثة علمي"))
        self.t1t2comrow.setItemText(3, _translate("MainWindow", "ثانية ادبي"))
        self.t1t2comrow.setItemText(4, _translate("MainWindow", "ثالثة ادبي"))
        self.label_8.setText(_translate("MainWindow", "الصف:"))
        self.t1t2butsho.setText(_translate("MainWindow", "عرض"))
        self.label_38.setText(_translate("MainWindow", "50%"))
        self.label_37.setText(_translate("MainWindow", "30%"))
        self.label_36.setText(_translate("MainWindow", "20%"))
        self.label_35.setText(_translate("MainWindow", "ش2"))
        self.label_34.setText(_translate("MainWindow", "ش1"))
        self.label_33.setText(_translate("MainWindow", "تحريري2"))
        self.label_31.setText(_translate("MainWindow", "شفوي2"))
        self.label_30.setText(_translate("MainWindow", "واجبات2"))
        self.label_32.setText(_translate("MainWindow", "مواظبة2"))
        self.label_29.setText(_translate("MainWindow", "تحريري1"))
        self.label_28.setText(_translate("MainWindow", "شفوي1"))
        self.label_27.setText(_translate("MainWindow", "واجبات1"))
        self.label_26.setText(_translate("MainWindow", "مواظبة1"))
        self.label_11.setText(_translate("MainWindow", "المواد/التقسيم:"))
        self.label_12.setText(_translate("MainWindow", "القران الكريم:"))
        self.label_13.setText(_translate("MainWindow", "اسلامية:"))
        self.label_14.setText(_translate("MainWindow", "اللغة العربية:"))
        self.label_15.setText(_translate("MainWindow", "اللغة الانجليزية:"))
        self.label_16.setText(_translate("MainWindow", "الرياضيات:"))
        self.label_17.setText(_translate("MainWindow", "الاحياء:"))
        self.label_18.setText(_translate("MainWindow", "الكيمياء:"))
        self.label_19.setText(_translate("MainWindow", "الفيزياء:"))
        self.label_20.setText(_translate("MainWindow", "جغرافيا:"))
        self.label_21.setText(_translate("MainWindow", "تاريخ:"))
        self.label_22.setText(_translate("MainWindow", "مبادئ علم الاقتصاد:"))
        self.label_23.setText(_translate("MainWindow", "علم الاجتماع:"))
        self.label_24.setText(_translate("MainWindow", "جغرافيا الخرائط:"))
        self.label_25.setText(_translate("MainWindow", "الفلسفة والمنطق:"))
        self.label_41.setText(_translate("MainWindow", "مجتمع"))
        self.t1t2butdeletstu.setText(_translate("MainWindow", "حذف طالب"))
        self.t1t2butsavmod.setText(_translate("MainWindow", "حفظ التعديلات"))
        self.label_40.setText(_translate("MainWindow", "النسبة:"))
        self.label_39.setText(_translate("MainWindow", "المجموع الكلي:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "تعديل الدرجات"))
        self.label_128.setText(_translate("MainWindow", "اسم الطالب:"))
        self.label_84.setText(_translate("MainWindow", "اسم الصف:"))
        self.t1t3comrow.setItemText(0, _translate("MainWindow", "اولى ثانوي"))
        self.t1t3comrow.setItemText(1, _translate("MainWindow", "ثاني علمي"))
        self.t1t3comrow.setItemText(2, _translate("MainWindow", "ثالث علمي"))
        self.t1t3comrow.setItemText(3, _translate("MainWindow", "ثاني ادبي"))
        self.t1t3comrow.setItemText(4, _translate("MainWindow", "ثالث ادبي"))
        self.label_83.setText(_translate("MainWindow", "الصف:"))
        self.t1t3butprint1.setText(_translate("MainWindow", "طباعة"))
        self.t1t3butshoanyrow.setText(_translate("MainWindow", "عرض درجات الطالب في جميع المواد"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "عرض درجات الطالب في جميع المواد"))
        self.label_132.setText(_translate("MainWindow", "اسم المادة:"))
        self.label_130.setText(_translate("MainWindow", "اسم الصف:"))
        self.t1t4comrow.setItemText(0, _translate("MainWindow", "اولى ثانوي"))
        self.t1t4comrow.setItemText(1, _translate("MainWindow", "ثاني علمي"))
        self.t1t4comrow.setItemText(2, _translate("MainWindow", "ثالث علمي"))
        self.t1t4comrow.setItemText(3, _translate("MainWindow", "ثاني ادبي"))
        self.t1t4comrow.setItemText(4, _translate("MainWindow", "ثالث ادبي"))
        self.label_129.setText(_translate("MainWindow", "الصف:"))
        self.t1t4butshostudobjct.setText(_translate("MainWindow", "عرض درجات الطالب"))
        self.t1t4butprint2.setText(_translate("MainWindow", "طباعة"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_10), _translate("MainWindow", "عرض درجات جميع الطلاب"))
        self.btnaddnotc.setText(_translate("MainWindow", "اضافة ملاحظة جديدة"))
        self.btnmchn.setText(_translate("MainWindow", "الة حاسبة"))
        self.butterm1.setText(_translate("MainWindow", "الفصل الاول"))
        self.butterm2.setText(_translate("MainWindow", "الفصل االثاني"))
        self.butaddtion.setText(_translate("MainWindow", "اضافيات"))
        self.butexite.setText(_translate("MainWindow", "خروج"))

class NotePad(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)#lambda:تضعها عند اسم الزر
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.t1t1butrefrs.clicked.connect(self.upd)
        self.ui.t1t1butaddrow.clicked.connect(self.addrow)
        self.ui.t1t1butaddnamestud.clicked.connect(self.addstud)
        self.ui.t1t2butsho.clicked.connect(self.showstu1)
        self.ui.t1t2butsavmod.clicked.connect(self.modtab1)
        self.ui.t1t1comaddstudrow.currentIndexChanged.connect(self.storenamrow)
        self.ui.t1t2comrow.currentIndexChanged.connect(self.stocom)
        self.ui.t1t3comrow.currentIndexChanged.connect(self.stocom3)
        self.ui.t1t4comrow.currentIndexChanged.connect(self.stocom4)
        self.ui.t1t4comrow.currentIndexChanged.connect(self.stoobject)
        self.ui.t1t2comnamerow.currentIndexChanged.connect(self.stostud)
        self.ui.t1t3comnamerow.currentIndexChanged.connect(self.stostud3)
        self.ui.t1t3butshoanyrow.clicked.connect(self.sho1)
        self.ui.t1t4butshostudobjct.clicked.connect(self.shoobject)
        self.ui.t1t2butdeletstu.clicked.connect(self.destud)
        self.ui.butterm1.clicked.connect(self.s1)
        self.ui.butaddtion.clicked.connect(self.s2)
        self.ui.butexite.clicked.connect(self.out1)
        self.ui.btnmchn.clicked.connect(self.alh)
        self.ui.btnaddnotc.clicked.connect(self.cret)


        self.storenamrow()



        #################################################slidat#########################################
        ##################################################################################################
    def s1(self):
   	    self.ui.stackedWidget.setCurrentIndex(0)
    def s2(self):
        self.ui.stackedWidget.setCurrentIndex(1)
    def out1(self):
        exit()

        ####################################################################################################
        #############################################################################################################
    def addrow(self):
        namerow=str(self.ui.t1t1enaddnamrow.text())
        namerow2=str(self.ui.t1t1comrowaddnewrow.currentText())
        if namerow2=="اولى ثانوي":

            db1=sqlite3.connect('mngschool.db')
            db1.row_factory=sqlite3.Row
            db1.execute('create table if not exists tabladdrow(ID integer primary Key autoincrement,namrow text,roww text)')
            db1.execute('''insert into tabladdrow(namrow,roww) values(?,?)''',(namerow,namerow2))
            db1.commit()
        if namerow2=="ثاني علمي":

            db1=sqlite3.connect('mngschool2a.db')
            db1.row_factory=sqlite3.Row
            db1.execute('create table if not exists tabladdrow(ID integer primary Key autoincrement,namrow text,roww text)')
            db1.execute('''insert into tabladdrow(namrow,roww) values(?,?)''',(namerow,namerow2))
            db1.commit()
        if namerow2=="ثالث علمي":

            db1=sqlite3.connect('mngschool3a.db')
            db1.row_factory=sqlite3.Row
            db1.execute('create table if not exists tabladdrow(ID integer primary Key autoincrement,namrow text,roww text)')
            db1.execute('''insert into tabladdrow(namrow,roww) values(?,?)''',(namerow,namerow2))
            db1.commit()
        if namerow2=="ثاني ادبي":

            db1=sqlite3.connect('mngschool2d.db')
            db1.row_factory=sqlite3.Row
            db1.execute('create table if not exists tabladdrow(ID integer primary Key autoincrement,namrow text,roww text)')
            db1.execute('''insert into tabladdrow(namrow,roww) values(?,?)''',(namerow,namerow2))
            db1.commit()
        if namerow2=="ثالث ادبي":

            db1=sqlite3.connect('mngschool3d.db')
            db1.row_factory=sqlite3.Row
            db1.execute('create table if not exists tabladdrow(ID integer primary Key autoincrement,namrow text,roww text)')
            db1.execute('''insert into tabladdrow(namrow,roww) values(?,?)''',(namerow,namerow2))
            db1.commit()                
        message=QtWidgets.QMessageBox.information(self,'information','<FONT size=10 color=blue>Add Successfully</FONT>')        
    def storenamrow(self):
        r1=str(self.ui.t1t1comaddstudrow.currentText())
        if r1=="اولى ثانوي":

            db1=sqlite3.connect('mngschool.db')
            db1.row_factory=sqlite3.Row
            d1=db1.execute("select * from tabladdrow")
            self.ui.t1t1comnamestud.clear()
            for x in d1:
                self.ui.t1t1comnamestud.addItem("{}".format(x["namrow"]))
        if r1=="ثاني علمي":

            db1=sqlite3.connect('mngschool2a.db')
            db1.row_factory=sqlite3.Row
            d1=db1.execute("select * from tabladdrow")
            self.ui.t1t1comnamestud.clear()
            for x in d1:
                self.ui.t1t1comnamestud.addItem("{}".format(x["namrow"]))
        if r1=="ثالث علمي":

            db1=sqlite3.connect('mngschool3a.db')
            db1.row_factory=sqlite3.Row
            d1=db1.execute("select * from tabladdrow")
            self.ui.t1t1comnamestud.clear()
            for x in d1:
                self.ui.t1t1comnamestud.addItem("{}".format(x["namrow"]))

        if r1=="ثاني ادبي":

            db1=sqlite3.connect('mngschool2d.db')
            db1.row_factory=sqlite3.Row
            d1=db1.execute("select * from tabladdrow")
            self.ui.t1t1comnamestud.clear()
            for x in d1:
                self.ui.t1t1comnamestud.addItem("{}".format(x["namrow"])) 
        if r1=="ثالث ادبي":

            db1=sqlite3.connect('mngschool3d.db')
            db1.row_factory=sqlite3.Row
            d1=db1.execute("select * from tabladdrow")
            self.ui.t1t1comnamestud.clear()
            for x in d1:
                self.ui.t1t1comnamestud.addItem("{}".format(x["namrow"]))                               
    def upd(self):
        #self.storenamrow()
        self.stocom()
        self.stostud()
    def addstud(self):
        sturow=str(self.ui.t1t1comaddstudrow.currentText())
        namrowstu=str(self.ui.t1t1comnamestud.currentText())
        namestudy=str(self.ui.t1t1enaddnamestud.text())
        if sturow=="اولى ثانوي":

            db1=sqlite3.connect('mngschool.db')
            db1.row_factory=sqlite3.Row
            db1.execute('create table if not exists tabladdstudynt(ID integer primary Key autoincrement,namst text,rowst text)')
            db1.execute('''insert into tabladdstudynt(namst,rowst) values(?,?)''',(namestudy,namrowstu))
            db1.commit()
            db1.execute('create table if not exists qran(ID integer primary Key autoincrement,namst text,namero text,mo1 text,work1 text,sh1 text,test1 text,mo2 text,work2 text,sh2 text,test2 text,s1 text,s2 text,su20 text,su30 text,su50 text)')
            db1.execute('''insert into qran(namst,namero,mo1,work1,sh1,test1,mo2,work2,sh2,test2,s1,s2,su20,su30,su50) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',(namestudy,namrowstu,"0","0","0","0","0","0","0","0","0","0","0","0","0"))
            db1.commit()#########qran
            db1.execute('create table if not exists aslame(ID integer primary Key autoincrement,namst text,namero text,mo1 text,work1 text,sh1 text,test1 text,mo2 text,work2 text,sh2 text,test2 text,s1 text,s2 text,su20 text,su30 text,su50 text)')
            db1.execute('''insert into aslame(namst,namero,mo1,work1,sh1,test1,mo2,work2,sh2,test2,s1,s2,su20,su30,su50) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',(namestudy,namrowstu,"0","0","0","0","0","0","0","0","0","0","0","0","0"))
            db1.commit()
            db1.execute('create table if not exists arbic(ID integer primary Key autoincrement,namst text,namero text,mo1 text,work1 text,sh1 text,test1 text,mo2 text,work2 text,sh2 text,test2 text,s1 text,s2 text,su20 text,su30 text,su50 text)')
            db1.execute('''insert into arbic(namst,namero,mo1,work1,sh1,test1,mo2,work2,sh2,test2,s1,s2,su20,su30,su50) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',(namestudy,namrowstu,"0","0","0","0","0","0","0","0","0","0","0","0","0"))
            db1.commit()
            db1.execute('create table if not exists english(ID integer primary Key autoincrement,namst text,namero text,mo1 text,work1 text,sh1 text,test1 text,mo2 text,work2 text,sh2 text,test2 text,s1 text,s2 text,su20 text,su30 text,su50 text)')
            db1.execute('''insert into english(namst,namero,mo1,work1,sh1,test1,mo2,work2,sh2,test2,s1,s2,su20,su30,su50) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',(namestudy,namrowstu,"0","0","0","0","0","0","0","0","0","0","0","0","0"))
            db1.commit()
            db1.execute('create table if not exists readeat(ID integer primary Key autoincrement,namst text,namero text,mo1 text,work1 text,sh1 text,test1 text,mo2 text,work2 text,sh2 text,test2 text,s1 text,s2 text,su20 text,su30 text,su50 text)')
            db1.execute('''insert into readeat(namst,namero,mo1,work1,sh1,test1,mo2,work2,sh2,test2,s1,s2,su20,su30,su50) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',(namestudy,namrowstu,"0","0","0","0","0","0","0","0","0","0","0","0","0"))
            db1.commit()
            db1.execute('create table if not exists ahya(ID integer primary Key autoincrement,namst text,namero text,mo1 text,work1 text,sh1 text,test1 text,mo2 text,work2 text,sh2 text,test2 text,s1 text,s2 text,su20 text,su30 text,su50 text)')
            db1.execute('''insert into ahya(namst,namero,mo1,work1,sh1,test1,mo2,work2,sh2,test2,s1,s2,su20,su30,su50) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',(namestudy,namrowstu,"0","0","0","0","0","0","0","0","0","0","0","0","0"))
            db1.commit()
            db1.execute('create table if not exists qimia(ID integer primary Key autoincrement,namst text,namero text,mo1 text,work1 text,sh1 text,test1 text,mo2 text,work2 text,sh2 text,test2 text,s1 text,s2 text,su20 text,su30 text,su50 text)')
            db1.execute('''insert into qimia(namst,namero,mo1,work1,sh1,test1,mo2,work2,sh2,test2,s1,s2,su20,su30,su50) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',(namestudy,namrowstu,"0","0","0","0","0","0","0","0","0","0","0","0","0"))
            db1.commit()
            db1.execute('create table if not exists visia(ID integer primary Key autoincrement,namst text,namero text,mo1 text,work1 text,sh1 text,test1 text,mo2 text,work2 text,sh2 text,test2 text,s1 text,s2 text,su20 text,su30 text,su50 text)')
            db1.execute('''insert into visia(namst,namero,mo1,work1,sh1,test1,mo2,work2,sh2,test2,s1,s2,su20,su30,su50) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',(namestudy,namrowstu,"0","0","0","0","0","0","0","0","0","0","0","0","0"))
            db1.commit()
            db1.execute('create table if not exists gjravi(ID integer primary Key autoincrement,namst text,namero text,mo1 text,work1 text,sh1 text,test1 text,mo2 text,work2 text,sh2 text,test2 text,s1 text,s2 text,su20 text,su30 text,su50 text)')
            db1.execute('''insert into gjravi(namst,namero,mo1,work1,sh1,test1,mo2,work2,sh2,test2,s1,s2,su20,su30,su50) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',(namestudy,namrowstu,"0","0","0","0","0","0","0","0","0","0","0","0","0"))
            db1.commit()
            db1.execute('create table if not exists mjtma(ID integer primary Key autoincrement,namst text,namero text,mo1 text,work1 text,sh1 text,test1 text,mo2 text,work2 text,sh2 text,test2 text,s1 text,s2 text,su20 text,su30 text,su50 text)')
            db1.execute('''insert into mjtma(namst,namero,mo1,work1,sh1,test1,mo2,work2,sh2,test2,s1,s2,su20,su30,su50) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',(namestudy,namrowstu,"0","0","0","0","0","0","0","0","0","0","0","0","0"))
            db1.commit()
            db1.execute('create table if not exists treh(ID integer primary Key autoincrement,namst text,namero text,mo1 text,work1 text,sh1 text,test1 text,mo2 text,work2 text,sh2 text,test2 text,s1 text,s2 text,su20 text,su30 text,su50 text)')
            db1.execute('''insert into treh(namst,namero,mo1,work1,sh1,test1,mo2,work2,sh2,test2,s1,s2,su20,su30,su50) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',(namestudy,namrowstu,"0","0","0","0","0","0","0","0","0","0","0","0","0"))
            db1.commit()   
            message=QtWidgets.QMessageBox.information(self,'information','<FONT size=10 color=blue>Add Successfully</FONT>')    

        if sturow=="ثاني علمي":

            db1=sqlite3.connect('mngschool2a.db')
            db1.row_factory=sqlite3.Row
            db1.execute('create table if not exists tabladdstudynt(ID integer primary Key autoincrement,namst text,rowst text)')
            db1.execute('''insert into tabladdstudynt(namst,rowst) values(?,?)''',(namestudy,namrowstu))
            db1.commit()
            db1.execute('create table if not exists qran(ID integer primary Key autoincrement,namst text,namero text,mo1 text,work1 text,sh1 text,test1 text,mo2 text,work2 text,sh2 text,test2 text,s1 text,s2 text,su20 text,su30 text,su50 text)')
            db1.execute('''insert into qran(namst,namero,mo1,work1,sh1,test1,mo2,work2,sh2,test2,s1,s2,su20,su30,su50) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',(namestudy,namrowstu,"0","0","0","0","0","0","0","0","0","0","0","0","0"))
            db1.commit()#########qran
            db1.execute('create table if not exists aslame(ID integer primary Key autoincrement,namst text,namero text,mo1 text,work1 text,sh1 text,test1 text,mo2 text,work2 text,sh2 text,test2 text,s1 text,s2 text,su20 text,su30 text,su50 text)')
            db1.execute('''insert into aslame(namst,namero,mo1,work1,sh1,test1,mo2,work2,sh2,test2,s1,s2,su20,su30,su50) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',(namestudy,namrowstu,"0","0","0","0","0","0","0","0","0","0","0","0","0"))
            db1.commit()
            db1.execute('create table if not exists arbic(ID integer primary Key autoincrement,namst text,namero text,mo1 text,work1 text,sh1 text,test1 text,mo2 text,work2 text,sh2 text,test2 text,s1 text,s2 text,su20 text,su30 text,su50 text)')
            db1.execute('''insert into arbic(namst,namero,mo1,work1,sh1,test1,mo2,work2,sh2,test2,s1,s2,su20,su30,su50) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',(namestudy,namrowstu,"0","0","0","0","0","0","0","0","0","0","0","0","0"))
            db1.commit()
            db1.execute('create table if not exists english(ID integer primary Key autoincrement,namst text,namero text,mo1 text,work1 text,sh1 text,test1 text,mo2 text,work2 text,sh2 text,test2 text,s1 text,s2 text,su20 text,su30 text,su50 text)')
            db1.execute('''insert into english(namst,namero,mo1,work1,sh1,test1,mo2,work2,sh2,test2,s1,s2,su20,su30,su50) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',(namestudy,namrowstu,"0","0","0","0","0","0","0","0","0","0","0","0","0"))
            db1.commit()
            db1.execute('create table if not exists readeat(ID integer primary Key autoincrement,namst text,namero text,mo1 text,work1 text,sh1 text,test1 text,mo2 text,work2 text,sh2 text,test2 text,s1 text,s2 text,su20 text,su30 text,su50 text)')
            db1.execute('''insert into readeat(namst,namero,mo1,work1,sh1,test1,mo2,work2,sh2,test2,s1,s2,su20,su30,su50) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',(namestudy,namrowstu,"0","0","0","0","0","0","0","0","0","0","0","0","0"))
            db1.commit()
            db1.execute('create table if not exists ahya(ID integer primary Key autoincrement,namst text,namero text,mo1 text,work1 text,sh1 text,test1 text,mo2 text,work2 text,sh2 text,test2 text,s1 text,s2 text,su20 text,su30 text,su50 text)')
            db1.execute('''insert into ahya(namst,namero,mo1,work1,sh1,test1,mo2,work2,sh2,test2,s1,s2,su20,su30,su50) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',(namestudy,namrowstu,"0","0","0","0","0","0","0","0","0","0","0","0","0"))
            db1.commit()
            db1.execute('create table if not exists qimia(ID integer primary Key autoincrement,namst text,namero text,mo1 text,work1 text,sh1 text,test1 text,mo2 text,work2 text,sh2 text,test2 text,s1 text,s2 text,su20 text,su30 text,su50 text)')
            db1.execute('''insert into qimia(namst,namero,mo1,work1,sh1,test1,mo2,work2,sh2,test2,s1,s2,su20,su30,su50) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',(namestudy,namrowstu,"0","0","0","0","0","0","0","0","0","0","0","0","0"))
            db1.commit()
            db1.execute('create table if not exists visia(ID integer primary Key autoincrement,namst text,namero text,mo1 text,work1 text,sh1 text,test1 text,mo2 text,work2 text,sh2 text,test2 text,s1 text,s2 text,su20 text,su30 text,su50 text)')
            db1.execute('''insert into visia(namst,namero,mo1,work1,sh1,test1,mo2,work2,sh2,test2,s1,s2,su20,su30,su50) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',(namestudy,namrowstu,"0","0","0","0","0","0","0","0","0","0","0","0","0"))
            db1.commit()
            message=QtWidgets.QMessageBox.information(self,'information','<FONT size=10 color=blue>Add Successfully</FONT>')     
        if sturow=="ثالث علمي":

            db1=sqlite3.connect('mngschool3a.db')
            db1.row_factory=sqlite3.Row
            db1.execute('create table if not exists tabladdstudynt(ID integer primary Key autoincrement,namst text,rowst text)')
            db1.execute('''insert into tabladdstudynt(namst,rowst) values(?,?)''',(namestudy,namrowstu))
            db1.commit()
            db1.execute('create table if not exists qran(ID integer primary Key autoincrement,namst text,namero text,mo1 text,work1 text,sh1 text,test1 text,mo2 text,work2 text,sh2 text,test2 text,s1 text,s2 text,su20 text,su30 text,su50 text)')
            db1.execute('''insert into qran(namst,namero,mo1,work1,sh1,test1,mo2,work2,sh2,test2,s1,s2,su20,su30,su50) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',(namestudy,namrowstu,"0","0","0","0","0","0","0","0","0","0","0","0","0"))
            db1.commit()#########qran
            db1.execute('create table if not exists aslame(ID integer primary Key autoincrement,namst text,namero text,mo1 text,work1 text,sh1 text,test1 text,mo2 text,work2 text,sh2 text,test2 text,s1 text,s2 text,su20 text,su30 text,su50 text)')
            db1.execute('''insert into aslame(namst,namero,mo1,work1,sh1,test1,mo2,work2,sh2,test2,s1,s2,su20,su30,su50) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',(namestudy,namrowstu,"0","0","0","0","0","0","0","0","0","0","0","0","0"))
            db1.commit()
            db1.execute('create table if not exists arbic(ID integer primary Key autoincrement,namst text,namero text,mo1 text,work1 text,sh1 text,test1 text,mo2 text,work2 text,sh2 text,test2 text,s1 text,s2 text,su20 text,su30 text,su50 text)')
            db1.execute('''insert into arbic(namst,namero,mo1,work1,sh1,test1,mo2,work2,sh2,test2,s1,s2,su20,su30,su50) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',(namestudy,namrowstu,"0","0","0","0","0","0","0","0","0","0","0","0","0"))
            db1.commit()
            db1.execute('create table if not exists english(ID integer primary Key autoincrement,namst text,namero text,mo1 text,work1 text,sh1 text,test1 text,mo2 text,work2 text,sh2 text,test2 text,s1 text,s2 text,su20 text,su30 text,su50 text)')
            db1.execute('''insert into english(namst,namero,mo1,work1,sh1,test1,mo2,work2,sh2,test2,s1,s2,su20,su30,su50) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',(namestudy,namrowstu,"0","0","0","0","0","0","0","0","0","0","0","0","0"))
            db1.commit()
            db1.execute('create table if not exists readeat(ID integer primary Key autoincrement,namst text,namero text,mo1 text,work1 text,sh1 text,test1 text,mo2 text,work2 text,sh2 text,test2 text,s1 text,s2 text,su20 text,su30 text,su50 text)')
            db1.execute('''insert into readeat(namst,namero,mo1,work1,sh1,test1,mo2,work2,sh2,test2,s1,s2,su20,su30,su50) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',(namestudy,namrowstu,"0","0","0","0","0","0","0","0","0","0","0","0","0"))
            db1.commit()
            db1.execute('create table if not exists ahya(ID integer primary Key autoincrement,namst text,namero text,mo1 text,work1 text,sh1 text,test1 text,mo2 text,work2 text,sh2 text,test2 text,s1 text,s2 text,su20 text,su30 text,su50 text)')
            db1.execute('''insert into ahya(namst,namero,mo1,work1,sh1,test1,mo2,work2,sh2,test2,s1,s2,su20,su30,su50) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',(namestudy,namrowstu,"0","0","0","0","0","0","0","0","0","0","0","0","0"))
            db1.commit()
            db1.execute('create table if not exists qimia(ID integer primary Key autoincrement,namst text,namero text,mo1 text,work1 text,sh1 text,test1 text,mo2 text,work2 text,sh2 text,test2 text,s1 text,s2 text,su20 text,su30 text,su50 text)')
            db1.execute('''insert into qimia(namst,namero,mo1,work1,sh1,test1,mo2,work2,sh2,test2,s1,s2,su20,su30,su50) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',(namestudy,namrowstu,"0","0","0","0","0","0","0","0","0","0","0","0","0"))
            db1.commit()
            db1.execute('create table if not exists visia(ID integer primary Key autoincrement,namst text,namero text,mo1 text,work1 text,sh1 text,test1 text,mo2 text,work2 text,sh2 text,test2 text,s1 text,s2 text,su20 text,su30 text,su50 text)')
            db1.execute('''insert into visia(namst,namero,mo1,work1,sh1,test1,mo2,work2,sh2,test2,s1,s2,su20,su30,su50) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',(namestudy,namrowstu,"0","0","0","0","0","0","0","0","0","0","0","0","0"))
            db1.commit()
            message=QtWidgets.QMessageBox.information(self,'information','<FONT size=10 color=blue>Add Successfully</FONT>')     
        if sturow=="ثاني ادبي":

            db1=sqlite3.connect('mngschool2d.db')
            db1.row_factory=sqlite3.Row
            db1.execute('create table if not exists tabladdstudynt(ID integer primary Key autoincrement,namst text,rowst text)')
            db1.execute('''insert into tabladdstudynt(namst,rowst) values(?,?)''',(namestudy,namrowstu))
            db1.commit()
            db1.execute('create table if not exists qran(ID integer primary Key autoincrement,namst text,namero text,mo1 text,work1 text,sh1 text,test1 text,mo2 text,work2 text,sh2 text,test2 text,s1 text,s2 text,su20 text,su30 text,su50 text)')
            db1.execute('''insert into qran(namst,namero,mo1,work1,sh1,test1,mo2,work2,sh2,test2,s1,s2,su20,su30,su50) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',(namestudy,namrowstu,"0","0","0","0","0","0","0","0","0","0","0","0","0"))
            db1.commit()#########qran
            db1.execute('create table if not exists aslame(ID integer primary Key autoincrement,namst text,namero text,mo1 text,work1 text,sh1 text,test1 text,mo2 text,work2 text,sh2 text,test2 text,s1 text,s2 text,su20 text,su30 text,su50 text)')
            db1.execute('''insert into aslame(namst,namero,mo1,work1,sh1,test1,mo2,work2,sh2,test2,s1,s2,su20,su30,su50) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',(namestudy,namrowstu,"0","0","0","0","0","0","0","0","0","0","0","0","0"))
            db1.commit()
            db1.execute('create table if not exists arbic(ID integer primary Key autoincrement,namst text,namero text,mo1 text,work1 text,sh1 text,test1 text,mo2 text,work2 text,sh2 text,test2 text,s1 text,s2 text,su20 text,su30 text,su50 text)')
            db1.execute('''insert into arbic(namst,namero,mo1,work1,sh1,test1,mo2,work2,sh2,test2,s1,s2,su20,su30,su50) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',(namestudy,namrowstu,"0","0","0","0","0","0","0","0","0","0","0","0","0"))
            db1.commit()
            db1.execute('create table if not exists english(ID integer primary Key autoincrement,namst text,namero text,mo1 text,work1 text,sh1 text,test1 text,mo2 text,work2 text,sh2 text,test2 text,s1 text,s2 text,su20 text,su30 text,su50 text)')
            db1.execute('''insert into english(namst,namero,mo1,work1,sh1,test1,mo2,work2,sh2,test2,s1,s2,su20,su30,su50) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',(namestudy,namrowstu,"0","0","0","0","0","0","0","0","0","0","0","0","0"))
            db1.commit()
            db1.execute('create table if not exists readeat(ID integer primary Key autoincrement,namst text,namero text,mo1 text,work1 text,sh1 text,test1 text,mo2 text,work2 text,sh2 text,test2 text,s1 text,s2 text,su20 text,su30 text,su50 text)')
            db1.execute('''insert into readeat(namst,namero,mo1,work1,sh1,test1,mo2,work2,sh2,test2,s1,s2,su20,su30,su50) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',(namestudy,namrowstu,"0","0","0","0","0","0","0","0","0","0","0","0","0"))
            db1.commit()
            db1.execute('create table if not exists gjravi(ID integer primary Key autoincrement,namst text,namero text,mo1 text,work1 text,sh1 text,test1 text,mo2 text,work2 text,sh2 text,test2 text,s1 text,s2 text,su20 text,su30 text,su50 text)')
            db1.execute('''insert into gjravi(namst,namero,mo1,work1,sh1,test1,mo2,work2,sh2,test2,s1,s2,su20,su30,su50) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',(namestudy,namrowstu,"0","0","0","0","0","0","0","0","0","0","0","0","0"))
            db1.commit()
            db1.execute('create table if not exists treh(ID integer primary Key autoincrement,namst text,namero text,mo1 text,work1 text,sh1 text,test1 text,mo2 text,work2 text,sh2 text,test2 text,s1 text,s2 text,su20 text,su30 text,su50 text)')
            db1.execute('''insert into treh(namst,namero,mo1,work1,sh1,test1,mo2,work2,sh2,test2,s1,s2,su20,su30,su50) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',(namestudy,namrowstu,"0","0","0","0","0","0","0","0","0","0","0","0","0"))
            db1.commit()
            db1.execute('create table if not exists mbada(ID integer primary Key autoincrement,namst text,namero text,mo1 text,work1 text,sh1 text,test1 text,mo2 text,work2 text,sh2 text,test2 text,s1 text,s2 text,su20 text,su30 text,su50 text)')
            db1.execute('''insert into mbada(namst,namero,mo1,work1,sh1,test1,mo2,work2,sh2,test2,s1,s2,su20,su30,su50) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',(namestudy,namrowstu,"0","0","0","0","0","0","0","0","0","0","0","0","0"))
            db1.commit()
            db1.execute('create table if not exists almaljtma(ID integer primary Key autoincrement,namst text,namero text,mo1 text,work1 text,sh1 text,test1 text,mo2 text,work2 text,sh2 text,test2 text,s1 text,s2 text,su20 text,su30 text,su50 text)')
            db1.execute('''insert into almaljtma(namst,namero,mo1,work1,sh1,test1,mo2,work2,sh2,test2,s1,s2,su20,su30,su50) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',(namestudy,namrowstu,"0","0","0","0","0","0","0","0","0","0","0","0","0"))
            db1.commit()
            message=QtWidgets.QMessageBox.information(self,'information','<FONT size=10 color=blue>Add Successfully</FONT>')     
        if sturow=="ثالث ادبي":

            db1=sqlite3.connect('mngschool3d.db')
            db1.row_factory=sqlite3.Row
            db1.execute('create table if not exists tabladdstudynt(ID integer primary Key autoincrement,namst text,rowst text)')
            db1.execute('''insert into tabladdstudynt(namst,rowst) values(?,?)''',(namestudy,namrowstu))
            db1.commit()
            db1.execute('create table if not exists qran(ID integer primary Key autoincrement,namst text,namero text,mo1 text,work1 text,sh1 text,test1 text,mo2 text,work2 text,sh2 text,test2 text,s1 text,s2 text,su20 text,su30 text,su50 text)')
            db1.execute('''insert into qran(namst,namero,mo1,work1,sh1,test1,mo2,work2,sh2,test2,s1,s2,su20,su30,su50) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',(namestudy,namrowstu,"0","0","0","0","0","0","0","0","0","0","0","0","0"))
            db1.commit()#########qran
            db1.execute('create table if not exists aslame(ID integer primary Key autoincrement,namst text,namero text,mo1 text,work1 text,sh1 text,test1 text,mo2 text,work2 text,sh2 text,test2 text,s1 text,s2 text,su20 text,su30 text,su50 text)')
            db1.execute('''insert into aslame(namst,namero,mo1,work1,sh1,test1,mo2,work2,sh2,test2,s1,s2,su20,su30,su50) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',(namestudy,namrowstu,"0","0","0","0","0","0","0","0","0","0","0","0","0"))
            db1.commit()
            db1.execute('create table if not exists arbic(ID integer primary Key autoincrement,namst text,namero text,mo1 text,work1 text,sh1 text,test1 text,mo2 text,work2 text,sh2 text,test2 text,s1 text,s2 text,su20 text,su30 text,su50 text)')
            db1.execute('''insert into arbic(namst,namero,mo1,work1,sh1,test1,mo2,work2,sh2,test2,s1,s2,su20,su30,su50) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',(namestudy,namrowstu,"0","0","0","0","0","0","0","0","0","0","0","0","0"))
            db1.commit()
            db1.execute('create table if not exists english(ID integer primary Key autoincrement,namst text,namero text,mo1 text,work1 text,sh1 text,test1 text,mo2 text,work2 text,sh2 text,test2 text,s1 text,s2 text,su20 text,su30 text,su50 text)')
            db1.execute('''insert into english(namst,namero,mo1,work1,sh1,test1,mo2,work2,sh2,test2,s1,s2,su20,su30,su50) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',(namestudy,namrowstu,"0","0","0","0","0","0","0","0","0","0","0","0","0"))
            db1.commit()
            db1.execute('create table if not exists readeat(ID integer primary Key autoincrement,namst text,namero text,mo1 text,work1 text,sh1 text,test1 text,mo2 text,work2 text,sh2 text,test2 text,s1 text,s2 text,su20 text,su30 text,su50 text)')
            db1.execute('''insert into readeat(namst,namero,mo1,work1,sh1,test1,mo2,work2,sh2,test2,s1,s2,su20,su30,su50) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',(namestudy,namrowstu,"0","0","0","0","0","0","0","0","0","0","0","0","0"))
            db1.commit()
            db1.execute('create table if not exists gjmap(ID integer primary Key autoincrement,namst text,namero text,mo1 text,work1 text,sh1 text,test1 text,mo2 text,work2 text,sh2 text,test2 text,s1 text,s2 text,su20 text,su30 text,su50 text)')
            db1.execute('''insert into gjmap(namst,namero,mo1,work1,sh1,test1,mo2,work2,sh2,test2,s1,s2,su20,su30,su50) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',(namestudy,namrowstu,"0","0","0","0","0","0","0","0","0","0","0","0","0"))
            db1.commit()
            db1.execute('create table if not exists treh(ID integer primary Key autoincrement,namst text,namero text,mo1 text,work1 text,sh1 text,test1 text,mo2 text,work2 text,sh2 text,test2 text,s1 text,s2 text,su20 text,su30 text,su50 text)')
            db1.execute('''insert into treh(namst,namero,mo1,work1,sh1,test1,mo2,work2,sh2,test2,s1,s2,su20,su30,su50) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',(namestudy,namrowstu,"0","0","0","0","0","0","0","0","0","0","0","0","0"))
            db1.commit()
            db1.execute('create table if not exists ffff(ID integer primary Key autoincrement,namst text,namero text,mo1 text,work1 text,sh1 text,test1 text,mo2 text,work2 text,sh2 text,test2 text,s1 text,s2 text,su20 text,su30 text,su50 text)')
            db1.execute('''insert into ffff(namst,namero,mo1,work1,sh1,test1,mo2,work2,sh2,test2,s1,s2,su20,su30,su50) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',(namestudy,namrowstu,"0","0","0","0","0","0","0","0","0","0","0","0","0"))
            db1.commit()
            
            message=QtWidgets.QMessageBox.information(self,'information','<FONT size=10 color=blue>Add Successfully</FONT>')     

#########################################################tab2##########################################################################

    def stocom(self):
        r1=str(self.ui.t1t2comrow.currentText())
        if r1=="اولى ثانوي":
            db1=sqlite3.connect('mngschool.db')
            db1.row_factory=sqlite3.Row
            d1=db1.execute("select * from tabladdrow")
            self.ui.t1t2comnamerow.clear()
            for x in d1:
                self.ui.t1t2comnamerow.addItem("{}".format(x["namrow"]))
        if r1=="ثانية علمي":
            db1=sqlite3.connect('mngschool2a.db')
            db1.row_factory=sqlite3.Row
            d1=db1.execute("select * from tabladdrow")
            self.ui.t1t2comnamerow.clear()
            for x in d1:
                self.ui.t1t2comnamerow.addItem("{}".format(x["namrow"]))
        if r1=="ثالثة علمي":
            db1=sqlite3.connect('mngschool3a.db')
            db1.row_factory=sqlite3.Row
            d1=db1.execute("select * from tabladdrow")
            self.ui.t1t2comnamerow.clear()
            for x in d1:
                self.ui.t1t2comnamerow.addItem("{}".format(x["namrow"]))
        if r1=="ثانية ادبي":
            db1=sqlite3.connect('mngschool2d.db')
            db1.row_factory=sqlite3.Row
            d1=db1.execute("select * from tabladdrow")
            self.ui.t1t2comnamerow.clear()
            for x in d1:
                self.ui.t1t2comnamerow.addItem("{}".format(x["namrow"]))
        if r1=="ثالثة ادبي":
            db1=sqlite3.connect('mngschool3d.db')
            db1.row_factory=sqlite3.Row
            d1=db1.execute("select * from tabladdrow")
            self.ui.t1t2comnamerow.clear()
            for x in d1:
                self.ui.t1t2comnamerow.addItem("{}".format(x["namrow"]))                                

    def stostud(self):
        r1=str(self.ui.t1t2comrow.currentText())
        r2=str(self.ui.t1t2comnamerow.currentText())
        if r1=="اولى ثانوي":
            db1=sqlite3.connect('mngschool.db')
            db1.row_factory=sqlite3.Row
            dd=db1.execute("select * from tabladdstudynt where rowst='{}'".format(r2))
            self.ui.t1t2comnamstud.clear()
            for x in dd:
                self.ui.t1t2comnamstud.addItem("{}".format(x["namst"]))
        if r1=="ثانية علمي":
            db1=sqlite3.connect('mngschool2a.db')
            db1.row_factory=sqlite3.Row
            dd=db1.execute("select * from tabladdstudynt where rowst='{}'".format(r2))
            self.ui.t1t2comnamstud.clear()
            for x in dd:
                self.ui.t1t2comnamstud.addItem("{}".format(x["namst"]))
        if r1=="ثالثة علمي":
            db1=sqlite3.connect('mngschool3a.db')
            db1.row_factory=sqlite3.Row
            dd=db1.execute("select * from tabladdstudynt where rowst='{}'".format(r2))
            self.ui.t1t2comnamstud.clear()
            for x in dd:
                self.ui.t1t2comnamstud.addItem("{}".format(x["namst"]))
        if r1=="ثانية ادبي":
            db1=sqlite3.connect('mngschool2d.db')
            db1.row_factory=sqlite3.Row
            dd=db1.execute("select * from tabladdstudynt where rowst='{}'".format(r2))
            self.ui.t1t2comnamstud.clear()
            for x in dd:
                self.ui.t1t2comnamstud.addItem("{}".format(x["namst"]))
        if r1=="ثالثة ادبي":
            db1=sqlite3.connect('mngschool3d.db')
            db1.row_factory=sqlite3.Row
            dd=db1.execute("select * from tabladdstudynt where rowst='{}'".format(r2))
            self.ui.t1t2comnamstud.clear()
            for x in dd:
                self.ui.t1t2comnamstud.addItem("{}".format(x["namst"]))                                 
    def showstu1(self):
        namrow=str(self.ui.t1t2comrow.currentText())
        if namrow=="اولى ثانوي": 
            narow=str(self.ui.t1t2comnamerow.currentText())
            namstud=str(self.ui.t1t2comnamstud.currentText())
            db1=sqlite3.connect('mngschool.db')
            db1.row_factory=sqlite3.Row
            sa1=db1.execute("select * from qran where namst='{}' and namero='{}'".format(namstud,narow))
            for n in sa1:
                self.ui.grmo1.setText(n["mo1"])
                self.ui.grmo2.setText(n["mo2"])
                self.ui.grsh1.setText(n["sh1"])
                self.ui.grsh2.setText(n["sh2"])
                self.ui.grtest1.setText(n["test1"])
                self.ui.grtest2.setText(n["test2"])
                self.ui.grwork1.setText(n["work1"])
                self.ui.grwork2.setText(n["work2"])
                self.ui.grsum1.setText(n["s1"])
                self.ui.grsum2.setText(n["s2"])
                self.ui.gr20.setText(n["su20"])
                self.ui.gr30.setText(n["su30"])
                self.ui.gr50.setText(n["su50"])
            self.showstu2()
            self.showstu3()
            self.showstu4()
            self.showstu5()
            self.showstu6()
            self.showstu7()
            self.showstu8()
            self.showstu9()
            self.showstu10()
            self.showstu11()
            self.jmmm()
            self.flsfh()
            self.mbadaalm()
            self.almalajtma()

            self.shosum()
        if namrow=="ثانية علمي": 
            narow=str(self.ui.t1t2comnamerow.currentText())
            namstud=str(self.ui.t1t2comnamstud.currentText())
            db1=sqlite3.connect('mngschool2a.db')
            db1.row_factory=sqlite3.Row
            sa1=db1.execute("select * from qran where namst='{}' and namero='{}'".format(namstud,narow))
            for n in sa1:
                self.ui.grmo1.setText(n["mo1"])
                self.ui.grmo2.setText(n["mo2"])
                self.ui.grsh1.setText(n["sh1"])
                self.ui.grsh2.setText(n["sh2"])
                self.ui.grtest1.setText(n["test1"])
                self.ui.grtest2.setText(n["test2"])
                self.ui.grwork1.setText(n["work1"])
                self.ui.grwork2.setText(n["work2"])
                self.ui.grsum1.setText(n["s1"])
                self.ui.grsum2.setText(n["s2"])
                self.ui.gr20.setText(n["su20"])
                self.ui.gr30.setText(n["su30"])
                self.ui.gr50.setText(n["su50"])
            self.showstu2a2()
            self.showstu2a3()
            self.showstu2a4()
            self.showstu2a5()
            self.showstu2a6()
            self.showstu2a7()
            self.showstu2a8()
            self.jmmm()
            self.flsfh()
            self.mbadaalm()
            self.almalajtma()
            self.jgrr()
            self.mjtmaa()
            self.trehh()
            self.shosum()
        if namrow=="ثالثة علمي": 
            narow=str(self.ui.t1t2comnamerow.currentText())
            namstud=str(self.ui.t1t2comnamstud.currentText())
            db1=sqlite3.connect('mngschool3a.db')
            db1.row_factory=sqlite3.Row
            sa1=db1.execute("select * from qran where namst='{}' and namero='{}'".format(namstud,narow))
            for n in sa1:
                self.ui.grmo1.setText(n["mo1"])
                self.ui.grmo2.setText(n["mo2"])
                self.ui.grsh1.setText(n["sh1"])
                self.ui.grsh2.setText(n["sh2"])
                self.ui.grtest1.setText(n["test1"])
                self.ui.grtest2.setText(n["test2"])
                self.ui.grwork1.setText(n["work1"])
                self.ui.grwork2.setText(n["work2"])
                self.ui.grsum1.setText(n["s1"])
                self.ui.grsum2.setText(n["s2"])
                self.ui.gr20.setText(n["su20"])
                self.ui.gr30.setText(n["su30"])
                self.ui.gr50.setText(n["su50"])
            self.showstu3a2()
            self.showstu3a3()
            self.showstu3a4()
            self.showstu3a5()
            self.showstu3a6()
            self.showstu3a7()
            self.showstu3a8()
            self.jmmm()
            self.flsfh()
            self.mbadaalm()
            self.almalajtma()
            self.jgrr()
            self.mjtmaa()
            self.trehh()
            self.shosum()
        if namrow=="ثانية ادبي": 
            narow=str(self.ui.t1t2comnamerow.currentText())
            namstud=str(self.ui.t1t2comnamstud.currentText())
            db1=sqlite3.connect('mngschool2d.db')
            db1.row_factory=sqlite3.Row
            sa1=db1.execute("select * from qran where namst='{}' and namero='{}'".format(namstud,narow))
            for n in sa1:
                self.ui.grmo1.setText(n["mo1"])
                self.ui.grmo2.setText(n["mo2"])
                self.ui.grsh1.setText(n["sh1"])
                self.ui.grsh2.setText(n["sh2"])
                self.ui.grtest1.setText(n["test1"])
                self.ui.grtest2.setText(n["test2"])
                self.ui.grwork1.setText(n["work1"])
                self.ui.grwork2.setText(n["work2"])
                self.ui.grsum1.setText(n["s1"])
                self.ui.grsum2.setText(n["s2"])
                self.ui.gr20.setText(n["su20"])
                self.ui.gr30.setText(n["su30"])
                self.ui.gr50.setText(n["su50"])
            self.showstu2d2()
            self.showstu2d3()
            self.showstu2d4()
            self.showstu2d5()
            self.showstu2d6()
            self.showstu2d7()
            self.showstu2d8()
            self.showstu2d9()
            self.jmmm()
            self.flsfh()
            self.mjtmaa()
            self.kimmm()
            self.visiaaa()
            self.ahyaaa()
            self.shosum()
        if namrow=="ثالثة ادبي": 
            narow=str(self.ui.t1t2comnamerow.currentText())
            namstud=str(self.ui.t1t2comnamstud.currentText())
            db1=sqlite3.connect('mngschool3d.db')
            db1.row_factory=sqlite3.Row
            sa1=db1.execute("select * from qran where namst='{}' and namero='{}'".format(namstud,narow))
            for n in sa1:
                self.ui.grmo1.setText(n["mo1"])
                self.ui.grmo2.setText(n["mo2"])
                self.ui.grsh1.setText(n["sh1"])
                self.ui.grsh2.setText(n["sh2"])
                self.ui.grtest1.setText(n["test1"])
                self.ui.grtest2.setText(n["test2"])
                self.ui.grwork1.setText(n["work1"])
                self.ui.grwork2.setText(n["work2"])
                self.ui.grsum1.setText(n["s1"])
                self.ui.grsum2.setText(n["s2"])
                self.ui.gr20.setText(n["su20"])
                self.ui.gr30.setText(n["su30"])
                self.ui.gr50.setText(n["su50"])
            self.showstu3d2()
            self.showstu3d3()
            self.showstu3d4()
            self.showstu3d5()
            self.showstu3d6()
            self.showstu3d7()
            self.showstu3d8()
            self.mjtmaa()
            self.mbadaalm()
            self.almalajtma()
            self.jgrr()
            
            self.kimmm()
            self.visiaaa()
            self.ahyaaa()
            self.shosum()                           
    def showstu2(self):
        namrow=str(self.ui.t1t2comrow.currentText())
        if namrow=="اولى ثانوي": 
            narow=str(self.ui.t1t2comnamerow.currentText())
            namstud=str(self.ui.t1t2comnamstud.currentText())
            db1=sqlite3.connect('mngschool.db')
            db1.row_factory=sqlite3.Row
            sa1=db1.execute("select * from aslame where namst='{}' and namero='{}'".format(namstud,narow))
            for n in sa1:
                self.ui.asmo1.setText(n["mo1"])
                self.ui.asmo2.setText(n["mo2"])
                self.ui.assh1.setText(n["sh1"])
                self.ui.assh2.setText(n["sh2"])
                self.ui.astest1.setText(n["test1"])
                self.ui.astest2.setText(n["test2"])
                self.ui.aswork1.setText(n["work1"])
                self.ui.aswork2.setText(n["work2"])
                self.ui.assum1.setText(n["s1"])
                self.ui.assum2.setText(n["s2"])
                self.ui.as20.setText(n["su20"])
                self.ui.as30.setText(n["su30"])
                self.ui.as50.setText(n["su50"])                    
    def showstu3(self):
        namrow=str(self.ui.t1t2comrow.currentText())
        if namrow=="اولى ثانوي": 
            narow=str(self.ui.t1t2comnamerow.currentText())
            namstud=str(self.ui.t1t2comnamstud.currentText())
            db1=sqlite3.connect('mngschool.db')
            db1.row_factory=sqlite3.Row
            sa1=db1.execute("select * from arbic where namst='{}' and namero='{}'".format(namstud,narow))
            for n in sa1:
                self.ui.armo1.setText(n["mo1"])
                self.ui.armo2.setText(n["mo2"])
                self.ui.arsh1.setText(n["sh1"])
                self.ui.arsh2.setText(n["sh2"])
                self.ui.artest1.setText(n["test1"])
                self.ui.artest2.setText(n["test2"])
                self.ui.arwork1.setText(n["work1"])
                self.ui.arwork2.setText(n["work2"])
                self.ui.arsum1.setText(n["s1"])
                self.ui.arsum2.setText(n["s2"])
                self.ui.ar20.setText(n["su20"])
                self.ui.ar30.setText(n["su30"])
                self.ui.ar50.setText(n["su50"])            
    def showstu4(self):
        namrow=str(self.ui.t1t2comrow.currentText())
        if namrow=="اولى ثانوي": 
            narow=str(self.ui.t1t2comnamerow.currentText())
            namstud=str(self.ui.t1t2comnamstud.currentText())
            db1=sqlite3.connect('mngschool.db')
            db1.row_factory=sqlite3.Row
            sa1=db1.execute("select * from english where namst='{}' and namero='{}'".format(namstud,narow))
            for n in sa1:
                self.ui.enmo1.setText(n["mo1"])
                self.ui.enmo2.setText(n["mo2"])
                self.ui.ensh1.setText(n["sh1"])
                self.ui.ensh2.setText(n["sh2"])
                self.ui.entest1.setText(n["test1"])
                self.ui.entest2.setText(n["test2"])
                self.ui.enwork1.setText(n["work1"])
                self.ui.enwork2.setText(n["work2"])
                self.ui.ensum1.setText(n["s1"])
                self.ui.ensum2.setText(n["s2"])
                self.ui.en20.setText(n["su20"])
                self.ui.en30.setText(n["su30"])
                self.ui.en50.setText(n["su50"])
    def showstu5(self):
        namrow=str(self.ui.t1t2comrow.currentText())
        if namrow=="اولى ثانوي": 
            narow=str(self.ui.t1t2comnamerow.currentText())
            namstud=str(self.ui.t1t2comnamstud.currentText())
            db1=sqlite3.connect('mngschool.db')
            db1.row_factory=sqlite3.Row
            sa1=db1.execute("select * from readeat where namst='{}' and namero='{}'".format(namstud,narow))
            for n in sa1:
                self.ui.remo1.setText(n["mo1"])
                self.ui.remo2.setText(n["mo2"])
                self.ui.resh1.setText(n["sh1"])
                self.ui.resh2.setText(n["sh2"])
                self.ui.retest1.setText(n["test1"])
                self.ui.retest2.setText(n["test2"])
                self.ui.rework1.setText(n["work1"])
                self.ui.rework2.setText(n["work2"])
                self.ui.resum1.setText(n["s1"])
                self.ui.resum2.setText(n["s2"])
                self.ui.re20.setText(n["su20"])
                self.ui.re30.setText(n["su30"])
                self.ui.re50.setText(n["su50"])            
    def showstu6(self):
        namrow=str(self.ui.t1t2comrow.currentText())
        if namrow=="اولى ثانوي": 
            narow=str(self.ui.t1t2comnamerow.currentText())
            namstud=str(self.ui.t1t2comnamstud.currentText())
            db1=sqlite3.connect('mngschool.db')
            db1.row_factory=sqlite3.Row
            sa1=db1.execute("select * from ahya where namst='{}' and namero='{}'".format(namstud,narow))
            for n in sa1:
                self.ui.ahmo1.setText(n["mo1"])
                self.ui.ahmo2.setText(n["mo2"])
                self.ui.ahsh1.setText(n["sh1"])
                self.ui.ahsh2.setText(n["sh2"])
                self.ui.ahtest1.setText(n["test1"])
                self.ui.ahtest2.setText(n["test2"])
                self.ui.ahwork1.setText(n["work1"])
                self.ui.ahwork2.setText(n["work2"])
                self.ui.ahsum1.setText(n["s1"])
                self.ui.ahsum2.setText(n["s2"])
                self.ui.ah20.setText(n["su20"])
                self.ui.ah30.setText(n["su30"])
                self.ui.ah50.setText(n["su50"]) 
    def showstu7(self):
        namrow=str(self.ui.t1t2comrow.currentText())
        if namrow=="اولى ثانوي": 
            narow=str(self.ui.t1t2comnamerow.currentText())
            namstud=str(self.ui.t1t2comnamstud.currentText())
            db1=sqlite3.connect('mngschool.db')
            db1.row_factory=sqlite3.Row
            sa1=db1.execute("select * from qimia where namst='{}' and namero='{}'".format(namstud,narow))
            for n in sa1:
                self.ui.kimo1.setText(n["mo1"])
                self.ui.kimo2.setText(n["mo2"])
                self.ui.kish1.setText(n["sh1"])
                self.ui.kish2.setText(n["sh2"])
                self.ui.kitest1.setText(n["test1"])
                self.ui.kitest2.setText(n["test2"])
                self.ui.kiwork1.setText(n["work1"])
                self.ui.kiwork2.setText(n["work2"])
                self.ui.kisum1.setText(n["s1"])
                self.ui.kisum2.setText(n["s2"])
                self.ui.ki20.setText(n["su20"])
                self.ui.ki30.setText(n["su30"])
                self.ui.ki50.setText(n["su50"])
    def showstu8(self):
        namrow=str(self.ui.t1t2comrow.currentText())
        if namrow=="اولى ثانوي": 
            narow=str(self.ui.t1t2comnamerow.currentText())
            namstud=str(self.ui.t1t2comnamstud.currentText())
            db1=sqlite3.connect('mngschool.db')
            db1.row_factory=sqlite3.Row
            sa1=db1.execute("select * from visia where namst='{}' and namero='{}'".format(namstud,narow))
            for n in sa1:
                self.ui.vimo1.setText(n["mo1"])
                self.ui.vimo2.setText(n["mo2"])
                self.ui.vish1.setText(n["sh1"])
                self.ui.vish2.setText(n["sh2"])
                self.ui.vitest1.setText(n["test1"])
                self.ui.vitest2.setText(n["test2"])
                self.ui.viwork1.setText(n["work1"])
                self.ui.viwork2.setText(n["work2"])
                self.ui.visum1.setText(n["s1"])
                self.ui.visum2.setText(n["s2"])
                self.ui.vi20.setText(n["su20"])
                self.ui.vi30.setText(n["su30"])
                self.ui.vi50.setText(n["su50"])
    def showstu9(self):
        namrow=str(self.ui.t1t2comrow.currentText())
        if namrow=="اولى ثانوي": 
            narow=str(self.ui.t1t2comnamerow.currentText())
            namstud=str(self.ui.t1t2comnamstud.currentText())
            db1=sqlite3.connect('mngschool.db')
            db1.row_factory=sqlite3.Row
            sa1=db1.execute("select * from gjravi where namst='{}' and namero='{}'".format(namstud,narow))
            for n in sa1:
                self.ui.jgmo1.setText(n["mo1"])
                self.ui.jgmo2.setText(n["mo2"])
                self.ui.jgsh1.setText(n["sh1"])
                self.ui.jgsh2.setText(n["sh2"])
                self.ui.jgtest1.setText(n["test1"])
                self.ui.jgtest2.setText(n["test2"])
                self.ui.jgwork1.setText(n["work1"])
                self.ui.jgwork2.setText(n["work2"])
                self.ui.jgsum1.setText(n["s1"])
                self.ui.jgsum2.setText(n["s2"])
                self.ui.jg20.setText(n["su20"])
                self.ui.jg30.setText(n["su30"])
                self.ui.jg50.setText(n["su50"])
    def showstu10(self):
        namrow=str(self.ui.t1t2comrow.currentText())
        if namrow=="اولى ثانوي": 
            narow=str(self.ui.t1t2comnamerow.currentText())
            namstud=str(self.ui.t1t2comnamstud.currentText())
            db1=sqlite3.connect('mngschool.db')
            db1.row_factory=sqlite3.Row
            sa1=db1.execute("select * from treh where namst='{}' and namero='{}'".format(namstud,narow))
            for n in sa1:
                self.ui.trmo1.setText(n["mo1"])
                self.ui.trmo2.setText(n["mo2"])
                self.ui.trsh1.setText(n["sh1"])
                self.ui.trsh2.setText(n["sh2"])
                self.ui.trtest1.setText(n["test1"])
                self.ui.trtest2.setText(n["test2"])
                self.ui.trwork1.setText(n["work1"])
                self.ui.trwork2.setText(n["work2"])
                self.ui.trsum1.setText(n["s1"])
                self.ui.trsum2.setText(n["s2"])
                self.ui.tr20.setText(n["su20"])
                self.ui.tr30.setText(n["su30"])
                self.ui.tr50.setText(n["su50"])
    def showstu11(self):
        namrow=str(self.ui.t1t2comrow.currentText())
        if namrow=="اولى ثانوي": 
            narow=str(self.ui.t1t2comnamerow.currentText())
            namstud=str(self.ui.t1t2comnamstud.currentText())
            db1=sqlite3.connect('mngschool.db')
            db1.row_factory=sqlite3.Row
            sa1=db1.execute("select * from mjtma where namst='{}' and namero='{}'".format(namstud,narow))
            for n in sa1:
                self.ui.mjmo1.setText(n["mo1"])
                self.ui.mjmo2.setText(n["mo2"])
                self.ui.mjsh1.setText(n["sh1"])
                self.ui.mjsh2.setText(n["sh2"])
                self.ui.mjtest1.setText(n["test1"])
                self.ui.mjtest2.setText(n["test2"])
                self.ui.mjwork1.setText(n["work1"])
                self.ui.mjwork2.setText(n["work2"])
                self.ui.mjsum1.setText(n["s1"])
                self.ui.mjsum2.setText(n["s2"])
                self.ui.mj20.setText(n["su20"])
                self.ui.mj30.setText(n["su30"])
                self.ui.mj50.setText(n["su50"]) 
    def modtab1(self):
        namrow=str(self.ui.t1t2comrow.currentText())
        if namrow=="اولى ثانوي":
            narow=str(self.ui.t1t2comnamerow.currentText())
            namstud=str(self.ui.t1t2comnamstud.currentText())
            
            if int(self.ui.grsh1.text())==0:
                s11=0
            if int(self.ui.grwork1.text())==0:
                s11=0
            if int(self.ui.grtest1.text())==0:
                s11=0
            if int(self.ui.grmo1.text())==0:
                s11=0
            else:               
                mot1=int(self.ui.grmo1.text())/5
                sht1=int(self.ui.grsh1.text())/5
                workt1=int(self.ui.grwork1.text())/5
                testt1=int(self.ui.grtest1.text())/5
                s11=(mot1+sht1+workt1+testt1)/2

            if int(self.ui.grsh2.text())==0:
                s22=0
            if int(self.ui.grwork2.text())==0:
                s22=0
            if int(self.ui.grtest2.text())==0:
                s22=0
            if int(self.ui.grmo2.text())==0:
                s22=0
            else:
                        
                mot2=int(self.ui.grmo2.text())/5
                sht2=int(self.ui.grsh2.text())/5
                workt2=int(self.ui.grwork2.text())/5
                testt2=int(self.ui.grtest2.text())/5
                s22=(mot2+sht2+workt2+testt2)/2

            sut20=s11+s22

            sut50=int(self.ui.gr30.text())+sut20
            db1=sqlite3.connect('mngschool.db')
            db1.row_factory=sqlite3.Row

            db1.execute("update qran set mo1='{}',mo2='{}',sh1='{}',sh2='{}',test1='{}',test2='{}',work1='{}',work2='{}',s1='{}',s2='{}',su20='{}',su30='{}',su50='{}' where namst='{}' and namero='{}'".format(str(self.ui.grmo1.text()),str(self.ui.grmo2.text()),str(self.ui.grsh1.text()),str(self.ui.grsh2.text()),str(str(self.ui.grtest1.text())),str(self.ui.grtest2.text()),str(self.ui.grwork1.text()),str(self.ui.grwork2.text()),str(s11),str(s22),str(sut20),str(self.ui.gr30.text()),str(sut50),namstud,narow))
            db1.commit()
            self.modtab2()
            self.modtab3()
            self.modtab4()
            self.modtab5()
            self.modtab6()
            self.modtab7()
            self.modtab8()
            self.modtab9()
            self.modtab10()
            self.modtab11()


            message=QtWidgets.QMessageBox.information(self,'information','<FONT size=10 color=blue>save modifis</FONT>')
        if namrow=="ثانية علمي":
            narow=str(self.ui.t1t2comnamerow.currentText())
            namstud=str(self.ui.t1t2comnamstud.currentText())
            
            if int(self.ui.grsh1.text())==0:
                s11=0
            if int(self.ui.grwork1.text())==0:
                s11=0
            if int(self.ui.grtest1.text())==0:
                s11=0
            if int(self.ui.grmo1.text())==0:
                s11=0
            else:               
                mot1=int(self.ui.grmo1.text())/5
                sht1=int(self.ui.grsh1.text())/5
                workt1=int(self.ui.grwork1.text())/5
                testt1=int(self.ui.grtest1.text())/5
                s11=(mot1+sht1+workt1+testt1)/2

            if int(self.ui.grsh2.text())==0:
                s22=0
            if int(self.ui.grwork2.text())==0:
                s22=0
            if int(self.ui.grtest2.text())==0:
                s22=0
            if int(self.ui.grmo2.text())==0:
                s22=0
            else:
                        
                mot2=int(self.ui.grmo2.text())/5
                sht2=int(self.ui.grsh2.text())/5
                workt2=int(self.ui.grwork2.text())/5
                testt2=int(self.ui.grtest2.text())/5
                s22=(mot2+sht2+workt2+testt2)/2

            sut20=s11+s22

            sut50=int(self.ui.gr30.text())+sut20
            db1=sqlite3.connect('mngschool2a.db')
            db1.row_factory=sqlite3.Row

            db1.execute("update qran set mo1='{}',mo2='{}',sh1='{}',sh2='{}',test1='{}',test2='{}',work1='{}',work2='{}',s1='{}',s2='{}',su20='{}',su30='{}',su50='{}' where namst='{}' and namero='{}'".format(str(self.ui.grmo1.text()),str(self.ui.grmo2.text()),str(self.ui.grsh1.text()),str(self.ui.grsh2.text()),str(str(self.ui.grtest1.text())),str(self.ui.grtest2.text()),str(self.ui.grwork1.text()),str(self.ui.grwork2.text()),str(s11),str(s22),str(sut20),str(self.ui.gr30.text()),str(sut50),namstud,narow))
            db1.commit()
            self.modtab2a2()
            self.modtab2a3()
            self.modtab2a4()
            self.modtab2a5()
            self.modtab2a6()
            self.modtab2a7()
            self.modtab2a8()
            message=QtWidgets.QMessageBox.information(self,'information','<FONT size=10 color=blue>save modifis</FONT>')

        if namrow=="ثالثة علمي":
            narow=str(self.ui.t1t2comnamerow.currentText())
            namstud=str(self.ui.t1t2comnamstud.currentText())
            
            if int(self.ui.grsh1.text())==0:
                s11=0
            if int(self.ui.grwork1.text())==0:
                s11=0
            if int(self.ui.grtest1.text())==0:
                s11=0
            if int(self.ui.grmo1.text())==0:
                s11=0
            else:               
                mot1=int(self.ui.grmo1.text())/5
                sht1=int(self.ui.grsh1.text())/5
                workt1=int(self.ui.grwork1.text())/5
                testt1=int(self.ui.grtest1.text())/5
                s11=(mot1+sht1+workt1+testt1)/2

            if int(self.ui.grsh2.text())==0:
                s22=0
            if int(self.ui.grwork2.text())==0:
                s22=0
            if int(self.ui.grtest2.text())==0:
                s22=0
            if int(self.ui.grmo2.text())==0:
                s22=0
            else:
                        
                mot2=int(self.ui.grmo2.text())/5
                sht2=int(self.ui.grsh2.text())/5
                workt2=int(self.ui.grwork2.text())/5
                testt2=int(self.ui.grtest2.text())/5
                s22=(mot2+sht2+workt2+testt2)/2

            sut20=s11+s22

            sut50=int(self.ui.gr30.text())+sut20
            db1=sqlite3.connect('mngschool3a.db')
            db1.row_factory=sqlite3.Row

            db1.execute("update qran set mo1='{}',mo2='{}',sh1='{}',sh2='{}',test1='{}',test2='{}',work1='{}',work2='{}',s1='{}',s2='{}',su20='{}',su30='{}',su50='{}' where namst='{}' and namero='{}'".format(str(self.ui.grmo1.text()),str(self.ui.grmo2.text()),str(self.ui.grsh1.text()),str(self.ui.grsh2.text()),str(str(self.ui.grtest1.text())),str(self.ui.grtest2.text()),str(self.ui.grwork1.text()),str(self.ui.grwork2.text()),str(s11),str(s22),str(sut20),str(self.ui.gr30.text()),str(sut50),namstud,narow))
            db1.commit()
            self.modtab3a2()
            self.modtab3a3()
            self.modtab3a4()
            self.modtab3a5()
            self.modtab3a6()
            self.modtab3a7()
            self.modtab3a8()
            message=QtWidgets.QMessageBox.information(self,'information','<FONT size=10 color=blue>save modifis</FONT>')        

        if namrow=="ثانية ادبي":
            narow=str(self.ui.t1t2comnamerow.currentText())
            namstud=str(self.ui.t1t2comnamstud.currentText())
            
            if int(self.ui.grsh1.text())==0:
                s11=0
            if int(self.ui.grwork1.text())==0:
                s11=0
            if int(self.ui.grtest1.text())==0:
                s11=0
            if int(self.ui.grmo1.text())==0:
                s11=0
            else:               
                mot1=int(self.ui.grmo1.text())/5
                sht1=int(self.ui.grsh1.text())/5
                workt1=int(self.ui.grwork1.text())/5
                testt1=int(self.ui.grtest1.text())/5
                s11=(mot1+sht1+workt1+testt1)/2

            if int(self.ui.grsh2.text())==0:
                s22=0
            if int(self.ui.grwork2.text())==0:
                s22=0
            if int(self.ui.grtest2.text())==0:
                s22=0
            if int(self.ui.grmo2.text())==0:
                s22=0
            else:
                        
                mot2=int(self.ui.grmo2.text())/5
                sht2=int(self.ui.grsh2.text())/5
                workt2=int(self.ui.grwork2.text())/5
                testt2=int(self.ui.grtest2.text())/5
                s22=(mot2+sht2+workt2+testt2)/2

            sut20=s11+s22

            sut50=int(self.ui.gr30.text())+sut20
            db1=sqlite3.connect('mngschool2d.db')
            db1.row_factory=sqlite3.Row

            db1.execute("update qran set mo1='{}',mo2='{}',sh1='{}',sh2='{}',test1='{}',test2='{}',work1='{}',work2='{}',s1='{}',s2='{}',su20='{}',su30='{}',su50='{}' where namst='{}' and namero='{}'".format(str(self.ui.grmo1.text()),str(self.ui.grmo2.text()),str(self.ui.grsh1.text()),str(self.ui.grsh2.text()),str(str(self.ui.grtest1.text())),str(self.ui.grtest2.text()),str(self.ui.grwork1.text()),str(self.ui.grwork2.text()),str(s11),str(s22),str(sut20),str(self.ui.gr30.text()),str(sut50),namstud,narow))
            db1.commit()
            self.modtab2d2()
            self.modtab2d3()
            self.modtab2d4()
            self.modtab2d5()
            self.modtab2d6()
            self.modtab2d7()
            self.modtab2d8()
            self.modtab2d9()

            message=QtWidgets.QMessageBox.information(self,'information','<FONT size=10 color=blue>save modifis</FONT>')

        if namrow=="ثالثة ادبي":
            narow=str(self.ui.t1t2comnamerow.currentText())
            namstud=str(self.ui.t1t2comnamstud.currentText())
            
            if int(self.ui.grsh1.text())==0:
                s11=0
            if int(self.ui.grwork1.text())==0:
                s11=0
            if int(self.ui.grtest1.text())==0:
                s11=0
            if int(self.ui.grmo1.text())==0:
                s11=0
            else:               
                mot1=int(self.ui.grmo1.text())/5
                sht1=int(self.ui.grsh1.text())/5
                workt1=int(self.ui.grwork1.text())/5
                testt1=int(self.ui.grtest1.text())/5
                s11=(mot1+sht1+workt1+testt1)/2

            if int(self.ui.grsh2.text())==0:
                s22=0
            if int(self.ui.grwork2.text())==0:
                s22=0
            if int(self.ui.grtest2.text())==0:
                s22=0
            if int(self.ui.grmo2.text())==0:
                s22=0
            else:
                        
                mot2=int(self.ui.grmo2.text())/5
                sht2=int(self.ui.grsh2.text())/5
                workt2=int(self.ui.grwork2.text())/5
                testt2=int(self.ui.grtest2.text())/5
                s22=(mot2+sht2+workt2+testt2)/2

            sut20=s11+s22

            sut50=int(self.ui.gr30.text())+sut20
            db1=sqlite3.connect('mngschool3d.db')
            db1.row_factory=sqlite3.Row

            db1.execute("update qran set mo1='{}',mo2='{}',sh1='{}',sh2='{}',test1='{}',test2='{}',work1='{}',work2='{}',s1='{}',s2='{}',su20='{}',su30='{}',su50='{}' where namst='{}' and namero='{}'".format(str(self.ui.grmo1.text()),str(self.ui.grmo2.text()),str(self.ui.grsh1.text()),str(self.ui.grsh2.text()),str(str(self.ui.grtest1.text())),str(self.ui.grtest2.text()),str(self.ui.grwork1.text()),str(self.ui.grwork2.text()),str(s11),str(s22),str(sut20),str(self.ui.gr30.text()),str(sut50),namstud,narow))
            db1.commit()
            self.modtab3d2()
            self.modtab3d3()
            self.modtab3d4()
            self.modtab3d5()
            self.modtab3d6()
            self.modtab3d7()
            self.modtab3d8()
            

            message=QtWidgets.QMessageBox.information(self,'information','<FONT size=10 color=blue>save modifis</FONT>')    
    def modtab2(self):
        namrow=str(self.ui.t1t2comrow.currentText()) 
        if namrow=="اولى ثانوي":
            narow=str(self.ui.t1t2comnamerow.currentText())
            namstud=str(self.ui.t1t2comnamstud.currentText())
            if int(self.ui.assh1.text())==0:
                s11=0
            if int(self.ui.aswork1.text())==0:
                s11=0
            if int(self.ui.astest1.text())==0:
                s11=0
            if int(self.ui.asmo1.text())==0:
                s11=0
            else:               
                mot1=int(self.ui.asmo1.text())/5
                sht1=int(self.ui.assh1.text())/5
                workt1=int(self.ui.aswork1.text())/5
                testt1=int(self.ui.astest1.text())/5
                s11=(mot1+sht1+workt1+testt1)/2

            if int(self.ui.assh2.text())==0:
                s22=0
            if int(self.ui.aswork2.text())==0:
                s22=0
            if int(self.ui.astest2.text())==0:
                s22=0
            if int(self.ui.asmo2.text())==0:
                s22=0
            else:
                        
                mot2=int(self.ui.asmo2.text())/5
                sht2=int(self.ui.assh2.text())/5
                workt2=int(self.ui.aswork2.text())/5
                testt2=int(self.ui.astest2.text())/5
                s22=(mot2+sht2+workt2+testt2)/2

            sut20=s11+s22

            sut50=int(self.ui.as30.text())+sut20
            db1=sqlite3.connect('mngschool.db')
            db1.row_factory=sqlite3.Row

            db1.execute("update aslame set mo1='{}',mo2='{}',sh1='{}',sh2='{}',test1='{}',test2='{}',work1='{}',work2='{}',s1='{}',s2='{}',su20='{}',su30='{}',su50='{}' where namst='{}' and namero='{}'".format(str(self.ui.asmo1.text()),str(self.ui.asmo2.text()),str(self.ui.assh1.text()),str(self.ui.assh2.text()),str(str(self.ui.astest1.text())),str(self.ui.astest2.text()),str(self.ui.aswork1.text()),str(self.ui.aswork2.text()),str(s11),str(s22),str(sut20),str(self.ui.as30.text()),str(sut50),namstud,narow))
            db1.commit()    

    def modtab3(self):
        namrow=str(self.ui.t1t2comrow.currentText()) 
        if namrow=="اولى ثانوي":
            narow=str(self.ui.t1t2comnamerow.currentText())
            namstud=str(self.ui.t1t2comnamstud.currentText())
            if int(self.ui.arsh1.text())==0:
                s11=0
            if int(self.ui.arwork1.text())==0:
                s11=0
            if int(self.ui.artest1.text())==0:
                s11=0
            if int(self.ui.armo1.text())==0:
                s11=0
            else:               
                mot1=int(self.ui.armo1.text())/5
                sht1=int(self.ui.arsh1.text())/5
                workt1=int(self.ui.arwork1.text())/5
                testt1=int(self.ui.artest1.text())/5
                s11=(mot1+sht1+workt1+testt1)/2

            if int(self.ui.arsh2.text())==0:
                s22=0
            if int(self.ui.arwork2.text())==0:
                s22=0
            if int(self.ui.artest2.text())==0:
                s22=0
            if int(self.ui.armo2.text())==0:
                s22=0
            else:
                        
                mot2=int(self.ui.armo2.text())/5
                sht2=int(self.ui.arsh2.text())/5
                workt2=int(self.ui.arwork2.text())/5
                testt2=int(self.ui.artest2.text())/5
                s22=(mot2+sht2+workt2+testt2)/2

            sut20=s11+s22

            sut50=int(self.ui.ar30.text())+sut20
            db1=sqlite3.connect('mngschool.db')
            db1.row_factory=sqlite3.Row

            db1.execute("update arbic set mo1='{}',mo2='{}',sh1='{}',sh2='{}',test1='{}',test2='{}',work1='{}',work2='{}',s1='{}',s2='{}',su20='{}',su30='{}',su50='{}' where namst='{}' and namero='{}'".format(str(self.ui.armo1.text()),str(self.ui.armo2.text()),str(self.ui.arsh1.text()),str(self.ui.arsh2.text()),str(str(self.ui.artest1.text())),str(self.ui.artest2.text()),str(self.ui.arwork1.text()),str(self.ui.arwork2.text()),str(s11),str(s22),str(sut20),str(self.ui.ar30.text()),str(sut50),namstud,narow))
            db1.commit()    
    def modtab4(self):
        namrow=str(self.ui.t1t2comrow.currentText()) 
        if namrow=="اولى ثانوي":
            narow=str(self.ui.t1t2comnamerow.currentText())
            namstud=str(self.ui.t1t2comnamstud.currentText())
            if int(self.ui.ensh1.text())==0:
                s11=0
            if int(self.ui.enwork1.text())==0:
                s11=0
            if int(self.ui.entest1.text())==0:
                s11=0
            if int(self.ui.enmo1.text())==0:
                s11=0
            else:               
                mot1=int(self.ui.enmo1.text())/5
                sht1=int(self.ui.ensh1.text())/5
                workt1=int(self.ui.enwork1.text())/5
                testt1=int(self.ui.entest1.text())/5
                s11=(mot1+sht1+workt1+testt1)/2

            if int(self.ui.ensh2.text())==0:
                s22=0
            if int(self.ui.enwork2.text())==0:
                s22=0
            if int(self.ui.entest2.text())==0:
                s22=0
            if int(self.ui.enmo2.text())==0:
                s22=0
            else:
                        
                mot2=int(self.ui.enmo2.text())/5
                sht2=int(self.ui.ensh2.text())/5
                workt2=int(self.ui.enwork2.text())/5
                testt2=int(self.ui.entest2.text())/5
                s22=(mot2+sht2+workt2+testt2)/2

            sut20=s11+s22

            sut50=int(self.ui.en30.text())+sut20
            db1=sqlite3.connect('mngschool.db')
            db1.row_factory=sqlite3.Row

            db1.execute("update english set mo1='{}',mo2='{}',sh1='{}',sh2='{}',test1='{}',test2='{}',work1='{}',work2='{}',s1='{}',s2='{}',su20='{}',su30='{}',su50='{}' where namst='{}' and namero='{}'".format(str(self.ui.enmo1.text()),str(self.ui.enmo2.text()),str(self.ui.ensh1.text()),str(self.ui.ensh2.text()),str(str(self.ui.entest1.text())),str(self.ui.entest2.text()),str(self.ui.enwork1.text()),str(self.ui.enwork2.text()),str(s11),str(s22),str(sut20),str(self.ui.en30.text()),str(sut50),namstud,narow))
            db1.commit()    
    def modtab5(self):
        namrow=str(self.ui.t1t2comrow.currentText()) 
        if namrow=="اولى ثانوي":
            narow=str(self.ui.t1t2comnamerow.currentText())
            namstud=str(self.ui.t1t2comnamstud.currentText())
            if int(self.ui.ahsh1.text())==0:
                s11=0
            if int(self.ui.ahwork1.text())==0:
                s11=0
            if int(self.ui.ahtest1.text())==0:
                s11=0
            if int(self.ui.ahmo1.text())==0:
                s11=0
            else:               
                mot1=int(self.ui.ahmo1.text())/5
                sht1=int(self.ui.ahsh1.text())/5
                workt1=int(self.ui.ahwork1.text())/5
                testt1=int(self.ui.ahtest1.text())/5
                s11=(mot1+sht1+workt1+testt1)/2

            if int(self.ui.ahsh2.text())==0:
                s22=0
            if int(self.ui.ahwork2.text())==0:
                s22=0
            if int(self.ui.ahtest2.text())==0:
                s22=0
            if int(self.ui.ahmo2.text())==0:
                s22=0
            else:
                        
                mot2=int(self.ui.ahmo2.text())/5
                sht2=int(self.ui.ahsh2.text())/5
                workt2=int(self.ui.ahwork2.text())/5
                testt2=int(self.ui.ahtest2.text())/5
                s22=(mot2+sht2+workt2+testt2)/2

            sut20=s11+s22

            sut50=int(self.ui.ah30.text())+sut20
            db1=sqlite3.connect('mngschool.db')
            db1.row_factory=sqlite3.Row

            db1.execute("update ahya set mo1='{}',mo2='{}',sh1='{}',sh2='{}',test1='{}',test2='{}',work1='{}',work2='{}',s1='{}',s2='{}',su20='{}',su30='{}',su50='{}' where namst='{}' and namero='{}'".format(str(self.ui.ahmo1.text()),str(self.ui.ahmo2.text()),str(self.ui.ahsh1.text()),str(self.ui.ahsh2.text()),str(str(self.ui.ahtest1.text())),str(self.ui.ahtest2.text()),str(self.ui.ahwork1.text()),str(self.ui.ahwork2.text()),str(s11),str(s22),str(sut20),str(self.ui.ah30.text()),str(sut50),namstud,narow))
            db1.commit()
    def modtab6(self):####readeat
        namrow=str(self.ui.t1t2comrow.currentText()) 
        if namrow=="اولى ثانوي":
            narow=str(self.ui.t1t2comnamerow.currentText())
            namstud=str(self.ui.t1t2comnamstud.currentText())
            if int(self.ui.resh1.text())==0:
                s11=0
            if int(self.ui.rework1.text())==0:
                s11=0
            if int(self.ui.retest1.text())==0:
                s11=0
            if int(self.ui.remo1.text())==0:
                s11=0
            else:               
                mot1=int(self.ui.remo1.text())/5
                sht1=int(self.ui.resh1.text())/5
                workt1=int(self.ui.rework1.text())/5
                testt1=int(self.ui.retest1.text())/5
                s11=(mot1+sht1+workt1+testt1)/2

            if int(self.ui.resh2.text())==0:
                s22=0
            if int(self.ui.rework2.text())==0:
                s22=0
            if int(self.ui.retest2.text())==0:
                s22=0
            if int(self.ui.remo2.text())==0:
                s22=0
            else:
                        
                mot2=int(self.ui.remo2.text())/5
                sht2=int(self.ui.resh2.text())/5
                workt2=int(self.ui.rework2.text())/5
                testt2=int(self.ui.retest2.text())/5
                s22=(mot2+sht2+workt2+testt2)/2

            sut20=s11+s22

            sut50=int(self.ui.re30.text())+sut20
            db1=sqlite3.connect('mngschool.db')
            db1.row_factory=sqlite3.Row

            db1.execute("update readeat set mo1='{}',mo2='{}',sh1='{}',sh2='{}',test1='{}',test2='{}',work1='{}',work2='{}',s1='{}',s2='{}',su20='{}',su30='{}',su50='{}' where namst='{}' and namero='{}'".format(str(self.ui.remo1.text()),str(self.ui.remo2.text()),str(self.ui.resh1.text()),str(self.ui.resh2.text()),str(str(self.ui.retest1.text())),str(self.ui.retest2.text()),str(self.ui.rework1.text()),str(self.ui.rework2.text()),str(s11),str(s22),str(sut20),str(self.ui.re30.text()),str(sut50),namstud,narow))
            db1.commit()
    def modtab7(self):
        namrow=str(self.ui.t1t2comrow.currentText()) 
        if namrow=="اولى ثانوي":
            narow=str(self.ui.t1t2comnamerow.currentText())
            namstud=str(self.ui.t1t2comnamstud.currentText())
            if int(self.ui.kish1.text())==0:
                s11=0
            if int(self.ui.kiwork1.text())==0:
                s11=0
            if int(self.ui.kitest1.text())==0:
                s11=0
            if int(self.ui.kimo1.text())==0:
                s11=0
            else:               
                mot1=int(self.ui.kimo1.text())/5
                sht1=int(self.ui.kish1.text())/5
                workt1=int(self.ui.kiwork1.text())/5
                testt1=int(self.ui.kitest1.text())/5
                s11=(mot1+sht1+workt1+testt1)/2

            if int(self.ui.kish2.text())==0:
                s22=0
            if int(self.ui.kiwork2.text())==0:
                s22=0
            if int(self.ui.kitest2.text())==0:
                s22=0
            if int(self.ui.kimo2.text())==0:
                s22=0
            else:
                        
                mot2=int(self.ui.kimo2.text())/5
                sht2=int(self.ui.kish2.text())/5
                workt2=int(self.ui.kiwork2.text())/5
                testt2=int(self.ui.kitest2.text())/5
                s22=(mot2+sht2+workt2+testt2)/2

            sut20=s11+s22

            sut50=int(self.ui.ki30.text())+sut20
            db1=sqlite3.connect('mngschool.db')
            db1.row_factory=sqlite3.Row

            db1.execute("update qimia set mo1='{}',mo2='{}',sh1='{}',sh2='{}',test1='{}',test2='{}',work1='{}',work2='{}',s1='{}',s2='{}',su20='{}',su30='{}',su50='{}' where namst='{}' and namero='{}'".format(str(self.ui.kimo1.text()),str(self.ui.kimo2.text()),str(self.ui.kish1.text()),str(self.ui.kish2.text()),str(str(self.ui.kitest1.text())),str(self.ui.kitest2.text()),str(self.ui.kiwork1.text()),str(self.ui.kiwork2.text()),str(s11),str(s22),str(sut20),str(self.ui.ki30.text()),str(sut50),namstud,narow))
            db1.commit()
    def modtab8(self):
        namrow=str(self.ui.t1t2comrow.currentText()) 
        if namrow=="اولى ثانوي":
            narow=str(self.ui.t1t2comnamerow.currentText())
            namstud=str(self.ui.t1t2comnamstud.currentText())
            if int(self.ui.vish1.text())==0:
                s11=0
            if int(self.ui.viwork1.text())==0:
                s11=0
            if int(self.ui.vitest1.text())==0:
                s11=0
            if int(self.ui.vimo1.text())==0:
                s11=0
            else:               
                mot1=int(self.ui.vimo1.text())/5
                sht1=int(self.ui.vish1.text())/5
                workt1=int(self.ui.viwork1.text())/5
                testt1=int(self.ui.vitest1.text())/5
                s11=(mot1+sht1+workt1+testt1)/2

            if int(self.ui.vish2.text())==0:
                s22=0
            if int(self.ui.viwork2.text())==0:
                s22=0
            if int(self.ui.vitest2.text())==0:
                s22=0
            if int(self.ui.vimo2.text())==0:
                s22=0
            else:
                        
                mot2=int(self.ui.vimo2.text())/5
                sht2=int(self.ui.vish2.text())/5
                workt2=int(self.ui.viwork2.text())/5
                testt2=int(self.ui.vitest2.text())/5
                s22=(mot2+sht2+workt2+testt2)/2

            sut20=s11+s22

            sut50=int(self.ui.vi30.text())+sut20
            db1=sqlite3.connect('mngschool.db')
            db1.row_factory=sqlite3.Row

            db1.execute("update visia set mo1='{}',mo2='{}',sh1='{}',sh2='{}',test1='{}',test2='{}',work1='{}',work2='{}',s1='{}',s2='{}',su20='{}',su30='{}',su50='{}' where namst='{}' and namero='{}'".format(str(self.ui.vimo1.text()),str(self.ui.vimo2.text()),str(self.ui.vish1.text()),str(self.ui.vish2.text()),str(str(self.ui.vitest1.text())),str(self.ui.vitest2.text()),str(self.ui.viwork1.text()),str(self.ui.viwork2.text()),str(s11),str(s22),str(sut20),str(self.ui.vi30.text()),str(sut50),namstud,narow))
            db1.commit()
    def modtab9(self):
        namrow=str(self.ui.t1t2comrow.currentText()) 
        if namrow=="اولى ثانوي":
            narow=str(self.ui.t1t2comnamerow.currentText())
            namstud=str(self.ui.t1t2comnamstud.currentText())
            if int(self.ui.jgsh1.text())==0:
                s11=0
            if int(self.ui.jgwork1.text())==0:
                s11=0
            if int(self.ui.jgtest1.text())==0:
                s11=0
            if int(self.ui.jgmo1.text())==0:
                s11=0
            else:               
                mot1=int(self.ui.jgmo1.text())/5
                sht1=int(self.ui.jgsh1.text())/5
                workt1=int(self.ui.jgwork1.text())/5
                testt1=int(self.ui.jgtest1.text())/5
                s11=(mot1+sht1+workt1+testt1)/2

            if int(self.ui.jgsh2.text())==0:
                s22=0
            if int(self.ui.jgwork2.text())==0:
                s22=0
            if int(self.ui.jgtest2.text())==0:
                s22=0
            if int(self.ui.jgmo2.text())==0:
                s22=0
            else:
                        
                mot2=int(self.ui.jgmo2.text())/5
                sht2=int(self.ui.jgsh2.text())/5
                workt2=int(self.ui.jgwork2.text())/5
                testt2=int(self.ui.jgtest2.text())/5
                s22=(mot2+sht2+workt2+testt2)/2

            sut20=s11+s22

            sut50=int(self.ui.jg30.text())+sut20
            db1=sqlite3.connect('mngschool.db')
            db1.row_factory=sqlite3.Row

            db1.execute("update gjravi set mo1='{}',mo2='{}',sh1='{}',sh2='{}',test1='{}',test2='{}',work1='{}',work2='{}',s1='{}',s2='{}',su20='{}',su30='{}',su50='{}' where namst='{}' and namero='{}'".format(str(self.ui.jgmo1.text()),str(self.ui.jgmo2.text()),str(self.ui.jgsh1.text()),str(self.ui.jgsh2.text()),str(str(self.ui.jgtest1.text())),str(self.ui.jgtest2.text()),str(self.ui.jgwork1.text()),str(self.ui.jgwork2.text()),str(s11),str(s22),str(sut20),str(self.ui.jg30.text()),str(sut50),namstud,narow))
            db1.commit()
    def modtab10(self):
        namrow=str(self.ui.t1t2comrow.currentText()) 
        if namrow=="اولى ثانوي":
            narow=str(self.ui.t1t2comnamerow.currentText())
            namstud=str(self.ui.t1t2comnamstud.currentText())
            if int(self.ui.trsh1.text())==0:
                s11=0
            if int(self.ui.trwork1.text())==0:
                s11=0
            if int(self.ui.trtest1.text())==0:
                s11=0
            if int(self.ui.trmo1.text())==0:
                s11=0
            else:               
                mot1=int(self.ui.trmo1.text())/5
                sht1=int(self.ui.trsh1.text())/5
                workt1=int(self.ui.trwork1.text())/5
                testt1=int(self.ui.trtest1.text())/5
                s11=(mot1+sht1+workt1+testt1)/2

            if int(self.ui.trsh2.text())==0:
                s22=0
            if int(self.ui.trwork2.text())==0:
                s22=0
            if int(self.ui.trtest2.text())==0:
                s22=0
            if int(self.ui.trmo2.text())==0:
                s22=0
            else:
                        
                mot2=int(self.ui.trmo2.text())/5
                sht2=int(self.ui.trsh2.text())/5
                workt2=int(self.ui.trwork2.text())/5
                testt2=int(self.ui.trtest2.text())/5
                s22=(mot2+sht2+workt2+testt2)/2

            sut20=s11+s22

            sut50=int(self.ui.tr30.text())+sut20
            db1=sqlite3.connect('mngschool.db')
            db1.row_factory=sqlite3.Row

            db1.execute("update treh set mo1='{}',mo2='{}',sh1='{}',sh2='{}',test1='{}',test2='{}',work1='{}',work2='{}',s1='{}',s2='{}',su20='{}',su30='{}',su50='{}' where namst='{}' and namero='{}'".format(str(self.ui.trmo1.text()),str(self.ui.trmo2.text()),str(self.ui.trsh1.text()),str(self.ui.trsh2.text()),str(str(self.ui.trtest1.text())),str(self.ui.trtest2.text()),str(self.ui.trwork1.text()),str(self.ui.trwork2.text()),str(s11),str(s22),str(sut20),str(self.ui.tr30.text()),str(sut50),namstud,narow))
            db1.commit()
    def modtab11(self):
        namrow=str(self.ui.t1t2comrow.currentText()) 
        if namrow=="اولى ثانوي":
            narow=str(self.ui.t1t2comnamerow.currentText())
            namstud=str(self.ui.t1t2comnamstud.currentText())
            if int(self.ui.mjsh1.text())==0:
                s11=0
            if int(self.ui.mjwork1.text())==0:
                s11=0
            if int(self.ui.mjtest1.text())==0:
                s11=0
            if int(self.ui.mjmo1.text())==0:
                s11=0
            else:               
                mot1=int(self.ui.mjmo1.text())/5
                sht1=int(self.ui.mjsh1.text())/5
                workt1=int(self.ui.mjwork1.text())/5
                testt1=int(self.ui.mjtest1.text())/5
                s11=(mot1+sht1+workt1+testt1)/2

            if int(self.ui.mjsh2.text())==0:
                s22=0
            if int(self.ui.mjwork2.text())==0:
                s22=0
            if int(self.ui.mjtest2.text())==0:
                s22=0
            if int(self.ui.mjmo2.text())==0:
                s22=0
            else:
                        
                mot2=int(self.ui.mjmo2.text())/5
                sht2=int(self.ui.mjsh2.text())/5
                workt2=int(self.ui.mjwork2.text())/5
                testt2=int(self.ui.mjtest2.text())/5
                s22=(mot2+sht2+workt2+testt2)/2

            sut20=s11+s22

            sut50=int(self.ui.mj30.text())+sut20
            db1=sqlite3.connect('mngschool.db')
            db1.row_factory=sqlite3.Row

            db1.execute("update mjtma set mo1='{}',mo2='{}',sh1='{}',sh2='{}',test1='{}',test2='{}',work1='{}',work2='{}',s1='{}',s2='{}',su20='{}',su30='{}',su50='{}' where namst='{}' and namero='{}'".format(str(self.ui.mjmo1.text()),str(self.ui.mjmo2.text()),str(self.ui.mjsh1.text()),str(self.ui.mjsh2.text()),str(str(self.ui.mjtest1.text())),str(self.ui.mjtest2.text()),str(self.ui.mjwork1.text()),str(self.ui.mjwork2.text()),str(s11),str(s22),str(sut20),str(self.ui.mj30.text()),str(sut50),namstud,narow))
            db1.commit()

    
######################################2almy################################################################################
    def showstu2a2(self):
        namrow=str(self.ui.t1t2comrow.currentText())
        if namrow=="ثانية علمي": 
            narow=str(self.ui.t1t2comnamerow.currentText())
            namstud=str(self.ui.t1t2comnamstud.currentText())
            db1=sqlite3.connect('mngschool2a.db')
            db1.row_factory=sqlite3.Row
            sa1=db1.execute("select * from aslame where namst='{}' and namero='{}'".format(namstud,narow))
            for n in sa1:
                self.ui.asmo1.setText(n["mo1"])
                self.ui.asmo2.setText(n["mo2"])
                self.ui.assh1.setText(n["sh1"])
                self.ui.assh2.setText(n["sh2"])
                self.ui.astest1.setText(n["test1"])
                self.ui.astest2.setText(n["test2"])
                self.ui.aswork1.setText(n["work1"])
                self.ui.aswork2.setText(n["work2"])
                self.ui.assum1.setText(n["s1"])
                self.ui.assum2.setText(n["s2"])
                self.ui.as20.setText(n["su20"])
                self.ui.as30.setText(n["su30"])
                self.ui.as50.setText(n["su50"])
    def showstu2a3(self):
        namrow=str(self.ui.t1t2comrow.currentText())
        if namrow=="ثانية علمي": 
            narow=str(self.ui.t1t2comnamerow.currentText())
            namstud=str(self.ui.t1t2comnamstud.currentText())
            db1=sqlite3.connect('mngschool2a.db')
            db1.row_factory=sqlite3.Row
            sa1=db1.execute("select * from arbic where namst='{}' and namero='{}'".format(namstud,narow))
            for n in sa1:
                self.ui.armo1.setText(n["mo1"])
                self.ui.armo2.setText(n["mo2"])
                self.ui.arsh1.setText(n["sh1"])
                self.ui.arsh2.setText(n["sh2"])
                self.ui.artest1.setText(n["test1"])
                self.ui.artest2.setText(n["test2"])
                self.ui.arwork1.setText(n["work1"])
                self.ui.arwork2.setText(n["work2"])
                self.ui.arsum1.setText(n["s1"])
                self.ui.arsum2.setText(n["s2"])
                self.ui.ar20.setText(n["su20"])
                self.ui.ar30.setText(n["su30"])
                self.ui.ar50.setText(n["su50"])
    def showstu2a4(self):
        namrow=str(self.ui.t1t2comrow.currentText())
        if namrow=="ثانية علمي": 
            narow=str(self.ui.t1t2comnamerow.currentText())
            namstud=str(self.ui.t1t2comnamstud.currentText())
            db1=sqlite3.connect('mngschool2a.db')
            db1.row_factory=sqlite3.Row
            sa1=db1.execute("select * from english where namst='{}' and namero='{}'".format(namstud,narow))
            for n in sa1:
                self.ui.enmo1.setText(n["mo1"])
                self.ui.enmo2.setText(n["mo2"])
                self.ui.ensh1.setText(n["sh1"])
                self.ui.ensh2.setText(n["sh2"])
                self.ui.entest1.setText(n["test1"])
                self.ui.entest2.setText(n["test2"])
                self.ui.enwork1.setText(n["work1"])
                self.ui.enwork2.setText(n["work2"])
                self.ui.ensum1.setText(n["s1"])
                self.ui.ensum2.setText(n["s2"])
                self.ui.en20.setText(n["su20"])
                self.ui.en30.setText(n["su30"])
                self.ui.en50.setText(n["su50"])
    def showstu2a5(self):
        namrow=str(self.ui.t1t2comrow.currentText())
        if namrow=="ثانية علمي": 
            narow=str(self.ui.t1t2comnamerow.currentText())
            namstud=str(self.ui.t1t2comnamstud.currentText())
            db1=sqlite3.connect('mngschool2a.db')
            db1.row_factory=sqlite3.Row
            sa1=db1.execute("select * from readeat where namst='{}' and namero='{}'".format(namstud,narow))
            for n in sa1:
                self.ui.remo1.setText(n["mo1"])
                self.ui.remo2.setText(n["mo2"])
                self.ui.resh1.setText(n["sh1"])
                self.ui.resh2.setText(n["sh2"])
                self.ui.retest1.setText(n["test1"])
                self.ui.retest2.setText(n["test2"])
                self.ui.rework1.setText(n["work1"])
                self.ui.rework2.setText(n["work2"])
                self.ui.resum1.setText(n["s1"])
                self.ui.resum2.setText(n["s2"])
                self.ui.re20.setText(n["su20"])
                self.ui.re30.setText(n["su30"])
                self.ui.re50.setText(n["su50"])                                   
    def showstu2a6(self):
        namrow=str(self.ui.t1t2comrow.currentText())
        if namrow=="ثانية علمي": 
            narow=str(self.ui.t1t2comnamerow.currentText())
            namstud=str(self.ui.t1t2comnamstud.currentText())
            db1=sqlite3.connect('mngschool2a.db')
            db1.row_factory=sqlite3.Row
            sa1=db1.execute("select * from ahya where namst='{}' and namero='{}'".format(namstud,narow))
            for n in sa1:
                self.ui.ahmo1.setText(n["mo1"])
                self.ui.ahmo2.setText(n["mo2"])
                self.ui.ahsh1.setText(n["sh1"])
                self.ui.ahsh2.setText(n["sh2"])
                self.ui.ahtest1.setText(n["test1"])
                self.ui.ahtest2.setText(n["test2"])
                self.ui.ahwork1.setText(n["work1"])
                self.ui.ahwork2.setText(n["work2"])
                self.ui.ahsum1.setText(n["s1"])
                self.ui.ahsum2.setText(n["s2"])
                self.ui.ah20.setText(n["su20"])
                self.ui.ah30.setText(n["su30"])
                self.ui.ah50.setText(n["su50"])
    def showstu2a7(self):
        namrow=str(self.ui.t1t2comrow.currentText())
        if namrow=="ثانية علمي": 
            narow=str(self.ui.t1t2comnamerow.currentText())
            namstud=str(self.ui.t1t2comnamstud.currentText())
            db1=sqlite3.connect('mngschool2a.db')
            db1.row_factory=sqlite3.Row
            sa1=db1.execute("select * from qimia where namst='{}' and namero='{}'".format(namstud,narow))
            for n in sa1:
                self.ui.kimo1.setText(n["mo1"])
                self.ui.kimo2.setText(n["mo2"])
                self.ui.kish1.setText(n["sh1"])
                self.ui.kish2.setText(n["sh2"])
                self.ui.kitest1.setText(n["test1"])
                self.ui.kitest2.setText(n["test2"])
                self.ui.kiwork1.setText(n["work1"])
                self.ui.kiwork2.setText(n["work2"])
                self.ui.kisum1.setText(n["s1"])
                self.ui.kisum2.setText(n["s2"])
                self.ui.ki20.setText(n["su20"])
                self.ui.ki30.setText(n["su30"])
                self.ui.ki50.setText(n["su50"])
    def showstu2a8(self):
        namrow=str(self.ui.t1t2comrow.currentText())
        if namrow=="ثانية علمي": 
            narow=str(self.ui.t1t2comnamerow.currentText())
            namstud=str(self.ui.t1t2comnamstud.currentText())
            db1=sqlite3.connect('mngschool2a.db')
            db1.row_factory=sqlite3.Row
            sa1=db1.execute("select * from visia where namst='{}' and namero='{}'".format(namstud,narow))
            for n in sa1:
                self.ui.vimo1.setText(n["mo1"])
                self.ui.vimo2.setText(n["mo2"])
                self.ui.vish1.setText(n["sh1"])
                self.ui.vish2.setText(n["sh2"])
                self.ui.vitest1.setText(n["test1"])
                self.ui.vitest2.setText(n["test2"])
                self.ui.viwork1.setText(n["work1"])
                self.ui.viwork2.setText(n["work2"])
                self.ui.visum1.setText(n["s1"])
                self.ui.visum2.setText(n["s2"])
                self.ui.vi20.setText(n["su20"])
                self.ui.vi30.setText(n["su30"])
                self.ui.vi50.setText(n["su50"])

    
    def modtab2a2(self):
        namrow=str(self.ui.t1t2comrow.currentText()) 
        if namrow=="ثانية علمي":
            narow=str(self.ui.t1t2comnamerow.currentText())
            namstud=str(self.ui.t1t2comnamstud.currentText())
            if int(self.ui.assh1.text())==0:
                s11=0
            if int(self.ui.aswork1.text())==0:
                s11=0
            if int(self.ui.astest1.text())==0:
                s11=0
            if int(self.ui.asmo1.text())==0:
                s11=0
            else:               
                mot1=int(self.ui.asmo1.text())/5
                sht1=int(self.ui.assh1.text())/5
                workt1=int(self.ui.aswork1.text())/5
                testt1=int(self.ui.astest1.text())/5
                s11=(mot1+sht1+workt1+testt1)/2

            if int(self.ui.assh2.text())==0:
                s22=0
            if int(self.ui.aswork2.text())==0:
                s22=0
            if int(self.ui.astest2.text())==0:
                s22=0
            if int(self.ui.asmo2.text())==0:
                s22=0
            else:
                        
                mot2=int(self.ui.asmo2.text())/5
                sht2=int(self.ui.assh2.text())/5
                workt2=int(self.ui.aswork2.text())/5
                testt2=int(self.ui.astest2.text())/5
                s22=(mot2+sht2+workt2+testt2)/2

            sut20=s11+s22

            sut50=int(self.ui.as30.text())+sut20
            db1=sqlite3.connect('mngschool2a.db')
            db1.row_factory=sqlite3.Row

            db1.execute("update aslame set mo1='{}',mo2='{}',sh1='{}',sh2='{}',test1='{}',test2='{}',work1='{}',work2='{}',s1='{}',s2='{}',su20='{}',su30='{}',su50='{}' where namst='{}' and namero='{}'".format(str(self.ui.asmo1.text()),str(self.ui.asmo2.text()),str(self.ui.assh1.text()),str(self.ui.assh2.text()),str(str(self.ui.astest1.text())),str(self.ui.astest2.text()),str(self.ui.aswork1.text()),str(self.ui.aswork2.text()),str(s11),str(s22),str(sut20),str(self.ui.as30.text()),str(sut50),namstud,narow))
            db1.commit()
    def modtab2a3(self):
        namrow=str(self.ui.t1t2comrow.currentText()) 
        if namrow=="ثانية علمي":
            narow=str(self.ui.t1t2comnamerow.currentText())
            namstud=str(self.ui.t1t2comnamstud.currentText())
            if int(self.ui.arsh1.text())==0:
                s11=0
            if int(self.ui.arwork1.text())==0:
                s11=0
            if int(self.ui.artest1.text())==0:
                s11=0
            if int(self.ui.armo1.text())==0:
                s11=0
            else:               
                mot1=int(self.ui.armo1.text())/5
                sht1=int(self.ui.arsh1.text())/5
                workt1=int(self.ui.arwork1.text())/5
                testt1=int(self.ui.artest1.text())/5
                s11=(mot1+sht1+workt1+testt1)/2

            if int(self.ui.arsh2.text())==0:
                s22=0
            if int(self.ui.arwork2.text())==0:
                s22=0
            if int(self.ui.artest2.text())==0:
                s22=0
            if int(self.ui.armo2.text())==0:
                s22=0
            else:
                        
                mot2=int(self.ui.armo2.text())/5
                sht2=int(self.ui.arsh2.text())/5
                workt2=int(self.ui.arwork2.text())/5
                testt2=int(self.ui.artest2.text())/5
                s22=(mot2+sht2+workt2+testt2)/2

            sut20=s11+s22

            sut50=int(self.ui.ar30.text())+sut20
            db1=sqlite3.connect('mngschool2a.db')
            db1.row_factory=sqlite3.Row

            db1.execute("update arbic set mo1='{}',mo2='{}',sh1='{}',sh2='{}',test1='{}',test2='{}',work1='{}',work2='{}',s1='{}',s2='{}',su20='{}',su30='{}',su50='{}' where namst='{}' and namero='{}'".format(str(self.ui.armo1.text()),str(self.ui.armo2.text()),str(self.ui.arsh1.text()),str(self.ui.arsh2.text()),str(str(self.ui.artest1.text())),str(self.ui.artest2.text()),str(self.ui.arwork1.text()),str(self.ui.arwork2.text()),str(s11),str(s22),str(sut20),str(self.ui.ar30.text()),str(sut50),namstud,narow))
            db1.commit()
    def modtab2a4(self):
        namrow=str(self.ui.t1t2comrow.currentText()) 
        if namrow=="ثانية علمي":
            narow=str(self.ui.t1t2comnamerow.currentText())
            namstud=str(self.ui.t1t2comnamstud.currentText())
            if int(self.ui.ensh1.text())==0:
                s11=0
            if int(self.ui.enwork1.text())==0:
                s11=0
            if int(self.ui.entest1.text())==0:
                s11=0
            if int(self.ui.enmo1.text())==0:
                s11=0
            else:               
                mot1=int(self.ui.enmo1.text())/5
                sht1=int(self.ui.ensh1.text())/5
                workt1=int(self.ui.enwork1.text())/5
                testt1=int(self.ui.entest1.text())/5
                s11=(mot1+sht1+workt1+testt1)/2

            if int(self.ui.ensh2.text())==0:
                s22=0
            if int(self.ui.enwork2.text())==0:
                s22=0
            if int(self.ui.entest2.text())==0:
                s22=0
            if int(self.ui.enmo2.text())==0:
                s22=0
            else:
                        
                mot2=int(self.ui.enmo2.text())/5
                sht2=int(self.ui.ensh2.text())/5
                workt2=int(self.ui.enwork2.text())/5
                testt2=int(self.ui.entest2.text())/5
                s22=(mot2+sht2+workt2+testt2)/2

            sut20=s11+s22

            sut50=int(self.ui.en30.text())+sut20
            db1=sqlite3.connect('mngschool2a.db')
            db1.row_factory=sqlite3.Row

            db1.execute("update english set mo1='{}',mo2='{}',sh1='{}',sh2='{}',test1='{}',test2='{}',work1='{}',work2='{}',s1='{}',s2='{}',su20='{}',su30='{}',su50='{}' where namst='{}' and namero='{}'".format(str(self.ui.enmo1.text()),str(self.ui.enmo2.text()),str(self.ui.ensh1.text()),str(self.ui.ensh2.text()),str(str(self.ui.entest1.text())),str(self.ui.entest2.text()),str(self.ui.enwork1.text()),str(self.ui.enwork2.text()),str(s11),str(s22),str(sut20),str(self.ui.en30.text()),str(sut50),namstud,narow))
            db1.commit()
    def modtab2a5(self):
        namrow=str(self.ui.t1t2comrow.currentText()) 
        if namrow=="ثانية علمي":
            narow=str(self.ui.t1t2comnamerow.currentText())
            namstud=str(self.ui.t1t2comnamstud.currentText())
            if int(self.ui.ahsh1.text())==0:
                s11=0
            if int(self.ui.ahwork1.text())==0:
                s11=0
            if int(self.ui.ahtest1.text())==0:
                s11=0
            if int(self.ui.ahmo1.text())==0:
                s11=0
            else:               
                mot1=int(self.ui.ahmo1.text())/5
                sht1=int(self.ui.ahsh1.text())/5
                workt1=int(self.ui.ahwork1.text())/5
                testt1=int(self.ui.ahtest1.text())/5
                s11=(mot1+sht1+workt1+testt1)/2

            if int(self.ui.ahsh2.text())==0:
                s22=0
            if int(self.ui.ahwork2.text())==0:
                s22=0
            if int(self.ui.ahtest2.text())==0:
                s22=0
            if int(self.ui.ahmo2.text())==0:
                s22=0
            else:
                        
                mot2=int(self.ui.ahmo2.text())/5
                sht2=int(self.ui.ahsh2.text())/5
                workt2=int(self.ui.ahwork2.text())/5
                testt2=int(self.ui.ahtest2.text())/5
                s22=(mot2+sht2+workt2+testt2)/2

            sut20=s11+s22

            sut50=int(self.ui.ah30.text())+sut20
            db1=sqlite3.connect('mngschool2a.db')
            db1.row_factory=sqlite3.Row

            db1.execute("update ahya set mo1='{}',mo2='{}',sh1='{}',sh2='{}',test1='{}',test2='{}',work1='{}',work2='{}',s1='{}',s2='{}',su20='{}',su30='{}',su50='{}' where namst='{}' and namero='{}'".format(str(self.ui.ahmo1.text()),str(self.ui.ahmo2.text()),str(self.ui.ahsh1.text()),str(self.ui.ahsh2.text()),str(str(self.ui.ahtest1.text())),str(self.ui.ahtest2.text()),str(self.ui.ahwork1.text()),str(self.ui.ahwork2.text()),str(s11),str(s22),str(sut20),str(self.ui.ah30.text()),str(sut50),namstud,narow))
            db1.commit()
    def modtab2a6(self):####readeat
        namrow=str(self.ui.t1t2comrow.currentText()) 
        if namrow=="ثانية علمي":
            narow=str(self.ui.t1t2comnamerow.currentText())
            namstud=str(self.ui.t1t2comnamstud.currentText())
            if int(self.ui.resh1.text())==0:
                s11=0
            if int(self.ui.rework1.text())==0:
                s11=0
            if int(self.ui.retest1.text())==0:
                s11=0
            if int(self.ui.remo1.text())==0:
                s11=0
            else:               
                mot1=int(self.ui.remo1.text())/5
                sht1=int(self.ui.resh1.text())/5
                workt1=int(self.ui.rework1.text())/5
                testt1=int(self.ui.retest1.text())/5
                s11=(mot1+sht1+workt1+testt1)/2

            if int(self.ui.resh2.text())==0:
                s22=0
            if int(self.ui.rework2.text())==0:
                s22=0
            if int(self.ui.retest2.text())==0:
                s22=0
            if int(self.ui.remo2.text())==0:
                s22=0
            else:
                        
                mot2=int(self.ui.remo2.text())/5
                sht2=int(self.ui.resh2.text())/5
                workt2=int(self.ui.rework2.text())/5
                testt2=int(self.ui.retest2.text())/5
                s22=(mot2+sht2+workt2+testt2)/2

            sut20=s11+s22

            sut50=int(self.ui.re30.text())+sut20
            db1=sqlite3.connect('mngschool2a.db')
            db1.row_factory=sqlite3.Row

            db1.execute("update readeat set mo1='{}',mo2='{}',sh1='{}',sh2='{}',test1='{}',test2='{}',work1='{}',work2='{}',s1='{}',s2='{}',su20='{}',su30='{}',su50='{}' where namst='{}' and namero='{}'".format(str(self.ui.remo1.text()),str(self.ui.remo2.text()),str(self.ui.resh1.text()),str(self.ui.resh2.text()),str(str(self.ui.retest1.text())),str(self.ui.retest2.text()),str(self.ui.rework1.text()),str(self.ui.rework2.text()),str(s11),str(s22),str(sut20),str(self.ui.re30.text()),str(sut50),namstud,narow))
            db1.commit()                
    def modtab2a7(self):
        namrow=str(self.ui.t1t2comrow.currentText()) 
        if namrow=="ثانية علمي":
            narow=str(self.ui.t1t2comnamerow.currentText())
            namstud=str(self.ui.t1t2comnamstud.currentText())
            if int(self.ui.kish1.text())==0:
                s11=0
            if int(self.ui.kiwork1.text())==0:
                s11=0
            if int(self.ui.kitest1.text())==0:
                s11=0
            if int(self.ui.kimo1.text())==0:
                s11=0
            else:               
                mot1=int(self.ui.kimo1.text())/5
                sht1=int(self.ui.kish1.text())/5
                workt1=int(self.ui.kiwork1.text())/5
                testt1=int(self.ui.kitest1.text())/5
                s11=(mot1+sht1+workt1+testt1)/2

            if int(self.ui.kish2.text())==0:
                s22=0
            if int(self.ui.kiwork2.text())==0:
                s22=0
            if int(self.ui.kitest2.text())==0:
                s22=0
            if int(self.ui.kimo2.text())==0:
                s22=0
            else:
                        
                mot2=int(self.ui.kimo2.text())/5
                sht2=int(self.ui.kish2.text())/5
                workt2=int(self.ui.kiwork2.text())/5
                testt2=int(self.ui.kitest2.text())/5
                s22=(mot2+sht2+workt2+testt2)/2

            sut20=s11+s22

            sut50=int(self.ui.ki30.text())+sut20
            db1=sqlite3.connect('mngschool2a.db')
            db1.row_factory=sqlite3.Row

            db1.execute("update qimia set mo1='{}',mo2='{}',sh1='{}',sh2='{}',test1='{}',test2='{}',work1='{}',work2='{}',s1='{}',s2='{}',su20='{}',su30='{}',su50='{}' where namst='{}' and namero='{}'".format(str(self.ui.kimo1.text()),str(self.ui.kimo2.text()),str(self.ui.kish1.text()),str(self.ui.kish2.text()),str(str(self.ui.kitest1.text())),str(self.ui.kitest2.text()),str(self.ui.kiwork1.text()),str(self.ui.kiwork2.text()),str(s11),str(s22),str(sut20),str(self.ui.ki30.text()),str(sut50),namstud,narow))
            db1.commit()
    def modtab2a8(self):
        namrow=str(self.ui.t1t2comrow.currentText()) 
        if namrow=="ثانية علمي":
            narow=str(self.ui.t1t2comnamerow.currentText())
            namstud=str(self.ui.t1t2comnamstud.currentText())
            if int(self.ui.vish1.text())==0:
                s11=0
            if int(self.ui.viwork1.text())==0:
                s11=0
            if int(self.ui.vitest1.text())==0:
                s11=0
            if int(self.ui.vimo1.text())==0:
                s11=0
            else:               
                mot1=int(self.ui.vimo1.text())/5
                sht1=int(self.ui.vish1.text())/5
                workt1=int(self.ui.viwork1.text())/5
                testt1=int(self.ui.vitest1.text())/5
                s11=(mot1+sht1+workt1+testt1)/2

            if int(self.ui.vish2.text())==0:
                s22=0
            if int(self.ui.viwork2.text())==0:
                s22=0
            if int(self.ui.vitest2.text())==0:
                s22=0
            if int(self.ui.vimo2.text())==0:
                s22=0
            else:
                        
                mot2=int(self.ui.vimo2.text())/5
                sht2=int(self.ui.vish2.text())/5
                workt2=int(self.ui.viwork2.text())/5
                testt2=int(self.ui.vitest2.text())/5
                s22=(mot2+sht2+workt2+testt2)/2

            sut20=s11+s22

            sut50=int(self.ui.vi30.text())+sut20
            db1=sqlite3.connect('mngschool2a.db')
            db1.row_factory=sqlite3.Row

            db1.execute("update visia set mo1='{}',mo2='{}',sh1='{}',sh2='{}',test1='{}',test2='{}',work1='{}',work2='{}',s1='{}',s2='{}',su20='{}',su30='{}',su50='{}' where namst='{}' and namero='{}'".format(str(self.ui.vimo1.text()),str(self.ui.vimo2.text()),str(self.ui.vish1.text()),str(self.ui.vish2.text()),str(str(self.ui.vitest1.text())),str(self.ui.vitest2.text()),str(self.ui.viwork1.text()),str(self.ui.viwork2.text()),str(s11),str(s22),str(sut20),str(self.ui.vi30.text()),str(sut50),namstud,narow))
            db1.commit()

###################################################################################################################################            
###########################################################the summmmmmm########################################################################################################
    def shosum(self):#function sum all dgry any stuyent
        namrow=str(self.ui.t1t2comrow.currentText()) 
        if namrow=="ثانية علمي":
            narow=str(self.ui.t1t2comnamerow.currentText())
            namstud=str(self.ui.t1t2comnamstud.currentText())
            h=[]
            v=0
            
            db1=sqlite3.connect('mngschool2a.db')
            #db1.row_factory=sqlite3.Row
            cb=db1.cursor()
            cb.execute("select sum(su50) from qran  where namst='{}' and namero='{}' union all select sum(su50) from ahya where namst='{}' and namero='{}' union all select sum(su50) from arbic  where namst='{}' and namero='{}' union all select sum(su50) from aslame  where namst='{}' and namero='{}' union all select sum(su50) from qimia  where namst='{}' and namero='{}' union all select sum(su50) from readeat where namst='{}' and namero='{}' union all select sum(su50) from visia  where namst='{}' and namero='{}' union all select sum(su50) from english where namst='{}' and namero='{}'".format(namstud,narow,namstud,narow,namstud,narow,namstud,narow,namstud,narow,namstud,narow,namstud,narow,namstud,narow))                   
            gg=cb.fetchall()
            for x in gg:
                h.append(int(x[0]))
            self.ui.t1t2ensumall.setText(str(sum(h)))
        if namrow=="ثالثة علمي":
            narow=str(self.ui.t1t2comnamerow.currentText())
            namstud=str(self.ui.t1t2comnamstud.currentText())
            h=[]
            v=0
            
            db1=sqlite3.connect('mngschool3a.db')
            #db1.row_factory=sqlite3.Row
            cb=db1.cursor()
            cb.execute("select sum(su50) from qran  where namst='{}' and namero='{}' union all select sum(su50) from ahya where namst='{}' and namero='{}' union all select sum(su50) from arbic  where namst='{}' and namero='{}' union all select sum(su50) from aslame  where namst='{}' and namero='{}' union all select sum(su50) from qimia  where namst='{}' and namero='{}' union all select sum(su50) from readeat where namst='{}' and namero='{}' union all select sum(su50) from visia  where namst='{}' and namero='{}' union all select sum(su50) from english where namst='{}' and namero='{}'".format(namstud,narow,namstud,narow,namstud,narow,namstud,narow,namstud,narow,namstud,narow,namstud,narow,namstud,narow))                   
            gg=cb.fetchall()
            for x in gg:
                h.append(int(x[0]))
            self.ui.t1t2ensumall.setText(str(sum(h)))    
        if namrow=="اولى ثانوي":
            narow=str(self.ui.t1t2comnamerow.currentText())
            namstud=str(self.ui.t1t2comnamstud.currentText())
            h=[]
            v=0
            
            db1=sqlite3.connect('mngschool.db')
            #db1.row_factory=sqlite3.Row
            cb=db1.cursor()
            cb.execute("select sum(su50) from qran  where namst='{}' and namero='{}' union all select sum(su50) from ahya where namst='{}' and namero='{}' union all select sum(su50) from arbic  where namst='{}' and namero='{}' union all select sum(su50) from aslame  where namst='{}' and namero='{}' union all select sum(su50) from qimia  where namst='{}' and namero='{}' union all select sum(su50) from readeat where namst='{}' and namero='{}' union all select sum(su50) from visia  where namst='{}' and namero='{}' union all select sum(su50) from english where namst='{}' and namero='{}' union all select sum(su50) from treh where namst='{}' and namero='{}' union all select sum(su50) from mjtma where namst='{}' and namero='{}' union all select sum(su50) from gjravi where namst='{}' and namero='{}'".format(namstud,narow,namstud,narow,namstud,narow,namstud,narow,namstud,narow,namstud,narow,namstud,narow,namstud,narow,namstud,narow,namstud,narow,namstud,narow))                   
            gg=cb.fetchall()
            for x in gg:
                h.append(int(x[0]))
            self.ui.t1t2ensumall.setText(str(sum(h)))
        if namrow=="ثانية ادبي":
            narow=str(self.ui.t1t2comnamerow.currentText())
            namstud=str(self.ui.t1t2comnamstud.currentText())
            h=[]
            v=0
            
            db1=sqlite3.connect('mngschool2d.db')
            #db1.row_factory=sqlite3.Row
            cb=db1.cursor()
            cb.execute("select sum(su50) from qran  where namst='{}' and namero='{}' union all select sum(su50) from almaljtma where namst='{}' and namero='{}' union all select sum(su50) from arbic  where namst='{}' and namero='{}' union all select sum(su50) from aslame  where namst='{}' and namero='{}' union all select sum(su50) from mbada  where namst='{}' and namero='{}' union all select sum(su50) from readeat where namst='{}' and namero='{}' union all select sum(su50) from english where namst='{}' and namero='{}' union all select sum(su50) from treh where namst='{}' and namero='{}' union all select sum(su50) from gjravi where namst='{}' and namero='{}'".format(namstud,narow,namstud,narow,namstud,narow,namstud,narow,namstud,narow,namstud,narow,namstud,narow,namstud,narow,namstud,narow))                   
            gg=cb.fetchall()
            for x in gg:
                h.append(int(x[0]))
            self.ui.t1t2ensumall.setText(str(sum(h)))
        if namrow=="ثالثة ادبي":
            narow=str(self.ui.t1t2comnamerow.currentText())
            namstud=str(self.ui.t1t2comnamstud.currentText())
            h=[]
            v=0
            
            db1=sqlite3.connect('mngschool3d.db')
            #db1.row_factory=sqlite3.Row
            cb=db1.cursor()
            cb.execute("select sum(su50) from qran  where namst='{}' and namero='{}' union all select sum(su50) from gjmap where namst='{}' and namero='{}' union all select sum(su50) from arbic  where namst='{}' and namero='{}' union all select sum(su50) from aslame  where namst='{}' and namero='{}' union all select sum(su50) from ffff where namst='{}' and namero='{}' union all select sum(su50) from readeat where namst='{}' and namero='{}' union all select sum(su50) from english where namst='{}' and namero='{}' union all select sum(su50) from treh where namst='{}' and namero='{}'".format(namstud,narow,namstud,narow,namstud,narow,namstud,narow,namstud,narow,namstud,narow,namstud,narow,namstud,narow))                   
            gg=cb.fetchall()
            for x in gg:
                h.append(int(x[0]))
            self.ui.t1t2ensumall.setText(str(sum(h)))        
############################################################ثالث علمي###########################3alme###################################
    def showstu3a2(self):
        namrow=str(self.ui.t1t2comrow.currentText())
        if namrow=="ثالثة علمي": 
            narow=str(self.ui.t1t2comnamerow.currentText())
            namstud=str(self.ui.t1t2comnamstud.currentText())
            db1=sqlite3.connect('mngschool3a.db')
            db1.row_factory=sqlite3.Row
            sa1=db1.execute("select * from aslame where namst='{}' and namero='{}'".format(namstud,narow))
            for n in sa1:
                self.ui.asmo1.setText(n["mo1"])
                self.ui.asmo2.setText(n["mo2"])
                self.ui.assh1.setText(n["sh1"])
                self.ui.assh2.setText(n["sh2"])
                self.ui.astest1.setText(n["test1"])
                self.ui.astest2.setText(n["test2"])
                self.ui.aswork1.setText(n["work1"])
                self.ui.aswork2.setText(n["work2"])
                self.ui.assum1.setText(n["s1"])
                self.ui.assum2.setText(n["s2"])
                self.ui.as20.setText(n["su20"])
                self.ui.as30.setText(n["su30"])
                self.ui.as50.setText(n["su50"])
    def showstu3a3(self):
        namrow=str(self.ui.t1t2comrow.currentText())
        if namrow=="ثالثة علمي": 
            narow=str(self.ui.t1t2comnamerow.currentText())
            namstud=str(self.ui.t1t2comnamstud.currentText())
            db1=sqlite3.connect('mngschool3a.db')
            db1.row_factory=sqlite3.Row
            sa1=db1.execute("select * from arbic where namst='{}' and namero='{}'".format(namstud,narow))
            for n in sa1:
                self.ui.armo1.setText(n["mo1"])
                self.ui.armo2.setText(n["mo2"])
                self.ui.arsh1.setText(n["sh1"])
                self.ui.arsh2.setText(n["sh2"])
                self.ui.artest1.setText(n["test1"])
                self.ui.artest2.setText(n["test2"])
                self.ui.arwork1.setText(n["work1"])
                self.ui.arwork2.setText(n["work2"])
                self.ui.arsum1.setText(n["s1"])
                self.ui.arsum2.setText(n["s2"])
                self.ui.ar20.setText(n["su20"])
                self.ui.ar30.setText(n["su30"])
                self.ui.ar50.setText(n["su50"])
    def showstu3a4(self):
        namrow=str(self.ui.t1t2comrow.currentText())
        if namrow=="ثالثة علمي": 
            narow=str(self.ui.t1t2comnamerow.currentText())
            namstud=str(self.ui.t1t2comnamstud.currentText())
            db1=sqlite3.connect('mngschool3a.db')
            db1.row_factory=sqlite3.Row
            sa1=db1.execute("select * from english where namst='{}' and namero='{}'".format(namstud,narow))
            for n in sa1:
                self.ui.enmo1.setText(n["mo1"])
                self.ui.enmo2.setText(n["mo2"])
                self.ui.ensh1.setText(n["sh1"])
                self.ui.ensh2.setText(n["sh2"])
                self.ui.entest1.setText(n["test1"])
                self.ui.entest2.setText(n["test2"])
                self.ui.enwork1.setText(n["work1"])
                self.ui.enwork2.setText(n["work2"])
                self.ui.ensum1.setText(n["s1"])
                self.ui.ensum2.setText(n["s2"])
                self.ui.en20.setText(n["su20"])
                self.ui.en30.setText(n["su30"])
                self.ui.en50.setText(n["su50"])
    def showstu3a5(self):
        namrow=str(self.ui.t1t2comrow.currentText())
        if namrow=="ثالثة علمي": 
            narow=str(self.ui.t1t2comnamerow.currentText())
            namstud=str(self.ui.t1t2comnamstud.currentText())
            db1=sqlite3.connect('mngschool3a.db')
            db1.row_factory=sqlite3.Row
            sa1=db1.execute("select * from readeat where namst='{}' and namero='{}'".format(namstud,narow))
            for n in sa1:
                self.ui.remo1.setText(n["mo1"])
                self.ui.remo2.setText(n["mo2"])
                self.ui.resh1.setText(n["sh1"])
                self.ui.resh2.setText(n["sh2"])
                self.ui.retest1.setText(n["test1"])
                self.ui.retest2.setText(n["test2"])
                self.ui.rework1.setText(n["work1"])
                self.ui.rework2.setText(n["work2"])
                self.ui.resum1.setText(n["s1"])
                self.ui.resum2.setText(n["s2"])
                self.ui.re20.setText(n["su20"])
                self.ui.re30.setText(n["su30"])
                self.ui.re50.setText(n["su50"])                                   
    def showstu3a6(self):
        namrow=str(self.ui.t1t2comrow.currentText())
        if namrow=="ثالثة علمي": 
            narow=str(self.ui.t1t2comnamerow.currentText())
            namstud=str(self.ui.t1t2comnamstud.currentText())
            db1=sqlite3.connect('mngschool3a.db')
            db1.row_factory=sqlite3.Row
            sa1=db1.execute("select * from ahya where namst='{}' and namero='{}'".format(namstud,narow))
            for n in sa1:
                self.ui.ahmo1.setText(n["mo1"])
                self.ui.ahmo2.setText(n["mo2"])
                self.ui.ahsh1.setText(n["sh1"])
                self.ui.ahsh2.setText(n["sh2"])
                self.ui.ahtest1.setText(n["test1"])
                self.ui.ahtest2.setText(n["test2"])
                self.ui.ahwork1.setText(n["work1"])
                self.ui.ahwork2.setText(n["work2"])
                self.ui.ahsum1.setText(n["s1"])
                self.ui.ahsum2.setText(n["s2"])
                self.ui.ah20.setText(n["su20"])
                self.ui.ah30.setText(n["su30"])
                self.ui.ah50.setText(n["su50"])
    def showstu3a7(self):
        namrow=str(self.ui.t1t2comrow.currentText())
        if namrow=="ثالثة علمي": 
            narow=str(self.ui.t1t2comnamerow.currentText())
            namstud=str(self.ui.t1t2comnamstud.currentText())
            db1=sqlite3.connect('mngschool3a.db')
            db1.row_factory=sqlite3.Row
            sa1=db1.execute("select * from qimia where namst='{}' and namero='{}'".format(namstud,narow))
            for n in sa1:
                self.ui.kimo1.setText(n["mo1"])
                self.ui.kimo2.setText(n["mo2"])
                self.ui.kish1.setText(n["sh1"])
                self.ui.kish2.setText(n["sh2"])
                self.ui.kitest1.setText(n["test1"])
                self.ui.kitest2.setText(n["test2"])
                self.ui.kiwork1.setText(n["work1"])
                self.ui.kiwork2.setText(n["work2"])
                self.ui.kisum1.setText(n["s1"])
                self.ui.kisum2.setText(n["s2"])
                self.ui.ki20.setText(n["su20"])
                self.ui.ki30.setText(n["su30"])
                self.ui.ki50.setText(n["su50"])
    def showstu3a8(self):
        namrow=str(self.ui.t1t2comrow.currentText())
        if namrow=="ثالثة علمي": 
            narow=str(self.ui.t1t2comnamerow.currentText())
            namstud=str(self.ui.t1t2comnamstud.currentText())
            db1=sqlite3.connect('mngschool3a.db')
            db1.row_factory=sqlite3.Row
            sa1=db1.execute("select * from visia where namst='{}' and namero='{}'".format(namstud,narow))
            for n in sa1:
                self.ui.vimo1.setText(n["mo1"])
                self.ui.vimo2.setText(n["mo2"])
                self.ui.vish1.setText(n["sh1"])
                self.ui.vish2.setText(n["sh2"])
                self.ui.vitest1.setText(n["test1"])
                self.ui.vitest2.setText(n["test2"])
                self.ui.viwork1.setText(n["work1"])
                self.ui.viwork2.setText(n["work2"])
                self.ui.visum1.setText(n["s1"])
                self.ui.visum2.setText(n["s2"])
                self.ui.vi20.setText(n["su20"])
                self.ui.vi30.setText(n["su30"])
                self.ui.vi50.setText(n["su50"])

#######################################################################
    def modtab3a2(self):
        namrow=str(self.ui.t1t2comrow.currentText()) 
        if namrow=="ثالثة علمي":
            narow=str(self.ui.t1t2comnamerow.currentText())
            namstud=str(self.ui.t1t2comnamstud.currentText())
            if int(self.ui.assh1.text())==0:
                s11=0
            if int(self.ui.aswork1.text())==0:
                s11=0
            if int(self.ui.astest1.text())==0:
                s11=0
            if int(self.ui.asmo1.text())==0:
                s11=0
            else:               
                mot1=int(self.ui.asmo1.text())/5
                sht1=int(self.ui.assh1.text())/5
                workt1=int(self.ui.aswork1.text())/5
                testt1=int(self.ui.astest1.text())/5
                s11=(mot1+sht1+workt1+testt1)/2

            if int(self.ui.assh2.text())==0:
                s22=0
            if int(self.ui.aswork2.text())==0:
                s22=0
            if int(self.ui.astest2.text())==0:
                s22=0
            if int(self.ui.asmo2.text())==0:
                s22=0
            else:
                        
                mot2=int(self.ui.asmo2.text())/5
                sht2=int(self.ui.assh2.text())/5
                workt2=int(self.ui.aswork2.text())/5
                testt2=int(self.ui.astest2.text())/5
                s22=(mot2+sht2+workt2+testt2)/2

            sut20=s11+s22

            sut50=int(self.ui.as30.text())+sut20
            db1=sqlite3.connect('mngschool3a.db')
            db1.row_factory=sqlite3.Row

            db1.execute("update aslame set mo1='{}',mo2='{}',sh1='{}',sh2='{}',test1='{}',test2='{}',work1='{}',work2='{}',s1='{}',s2='{}',su20='{}',su30='{}',su50='{}' where namst='{}' and namero='{}'".format(str(self.ui.asmo1.text()),str(self.ui.asmo2.text()),str(self.ui.assh1.text()),str(self.ui.assh2.text()),str(str(self.ui.astest1.text())),str(self.ui.astest2.text()),str(self.ui.aswork1.text()),str(self.ui.aswork2.text()),str(s11),str(s22),str(sut20),str(self.ui.as30.text()),str(sut50),namstud,narow))
            db1.commit()
    def modtab3a3(self):
        namrow=str(self.ui.t1t2comrow.currentText()) 
        if namrow=="ثالثة علمي":
            narow=str(self.ui.t1t2comnamerow.currentText())
            namstud=str(self.ui.t1t2comnamstud.currentText())
            if int(self.ui.arsh1.text())==0:
                s11=0
            if int(self.ui.arwork1.text())==0:
                s11=0
            if int(self.ui.artest1.text())==0:
                s11=0
            if int(self.ui.armo1.text())==0:
                s11=0
            else:               
                mot1=int(self.ui.armo1.text())/5
                sht1=int(self.ui.arsh1.text())/5
                workt1=int(self.ui.arwork1.text())/5
                testt1=int(self.ui.artest1.text())/5
                s11=(mot1+sht1+workt1+testt1)/2

            if int(self.ui.arsh2.text())==0:
                s22=0
            if int(self.ui.arwork2.text())==0:
                s22=0
            if int(self.ui.artest2.text())==0:
                s22=0
            if int(self.ui.armo2.text())==0:
                s22=0
            else:
                        
                mot2=int(self.ui.armo2.text())/5
                sht2=int(self.ui.arsh2.text())/5
                workt2=int(self.ui.arwork2.text())/5
                testt2=int(self.ui.artest2.text())/5
                s22=(mot2+sht2+workt2+testt2)/2

            sut20=s11+s22

            sut50=int(self.ui.ar30.text())+sut20
            db1=sqlite3.connect('mngschool3a.db')
            db1.row_factory=sqlite3.Row

            db1.execute("update arbic set mo1='{}',mo2='{}',sh1='{}',sh2='{}',test1='{}',test2='{}',work1='{}',work2='{}',s1='{}',s2='{}',su20='{}',su30='{}',su50='{}' where namst='{}' and namero='{}'".format(str(self.ui.armo1.text()),str(self.ui.armo2.text()),str(self.ui.arsh1.text()),str(self.ui.arsh2.text()),str(str(self.ui.artest1.text())),str(self.ui.artest2.text()),str(self.ui.arwork1.text()),str(self.ui.arwork2.text()),str(s11),str(s22),str(sut20),str(self.ui.ar30.text()),str(sut50),namstud,narow))
            db1.commit()
    def modtab3a4(self):
        namrow=str(self.ui.t1t2comrow.currentText()) 
        if namrow=="ثالثة علمي":
            narow=str(self.ui.t1t2comnamerow.currentText())
            namstud=str(self.ui.t1t2comnamstud.currentText())
            if int(self.ui.ensh1.text())==0:
                s11=0
            if int(self.ui.enwork1.text())==0:
                s11=0
            if int(self.ui.entest1.text())==0:
                s11=0
            if int(self.ui.enmo1.text())==0:
                s11=0
            else:               
                mot1=int(self.ui.enmo1.text())/5
                sht1=int(self.ui.ensh1.text())/5
                workt1=int(self.ui.enwork1.text())/5
                testt1=int(self.ui.entest1.text())/5
                s11=(mot1+sht1+workt1+testt1)/2

            if int(self.ui.ensh2.text())==0:
                s22=0
            if int(self.ui.enwork2.text())==0:
                s22=0
            if int(self.ui.entest2.text())==0:
                s22=0
            if int(self.ui.enmo2.text())==0:
                s22=0
            else:
                        
                mot2=int(self.ui.enmo2.text())/5
                sht2=int(self.ui.ensh2.text())/5
                workt2=int(self.ui.enwork2.text())/5
                testt2=int(self.ui.entest2.text())/5
                s22=(mot2+sht2+workt2+testt2)/2

            sut20=s11+s22

            sut50=int(self.ui.en30.text())+sut20
            db1=sqlite3.connect('mngschool3a.db')
            db1.row_factory=sqlite3.Row

            db1.execute("update english set mo1='{}',mo2='{}',sh1='{}',sh2='{}',test1='{}',test2='{}',work1='{}',work2='{}',s1='{}',s2='{}',su20='{}',su30='{}',su50='{}' where namst='{}' and namero='{}'".format(str(self.ui.enmo1.text()),str(self.ui.enmo2.text()),str(self.ui.ensh1.text()),str(self.ui.ensh2.text()),str(str(self.ui.entest1.text())),str(self.ui.entest2.text()),str(self.ui.enwork1.text()),str(self.ui.enwork2.text()),str(s11),str(s22),str(sut20),str(self.ui.en30.text()),str(sut50),namstud,narow))
            db1.commit()
    def modtab3a5(self):
        namrow=str(self.ui.t1t2comrow.currentText()) 
        if namrow=="ثالثة علمي":
            narow=str(self.ui.t1t2comnamerow.currentText())
            namstud=str(self.ui.t1t2comnamstud.currentText())
            if int(self.ui.ahsh1.text())==0:
                s11=0
            if int(self.ui.ahwork1.text())==0:
                s11=0
            if int(self.ui.ahtest1.text())==0:
                s11=0
            if int(self.ui.ahmo1.text())==0:
                s11=0
            else:               
                mot1=int(self.ui.ahmo1.text())/5
                sht1=int(self.ui.ahsh1.text())/5
                workt1=int(self.ui.ahwork1.text())/5
                testt1=int(self.ui.ahtest1.text())/5
                s11=(mot1+sht1+workt1+testt1)/2

            if int(self.ui.ahsh2.text())==0:
                s22=0
            if int(self.ui.ahwork2.text())==0:
                s22=0
            if int(self.ui.ahtest2.text())==0:
                s22=0
            if int(self.ui.ahmo2.text())==0:
                s22=0
            else:
                        
                mot2=int(self.ui.ahmo2.text())/5
                sht2=int(self.ui.ahsh2.text())/5
                workt2=int(self.ui.ahwork2.text())/5
                testt2=int(self.ui.ahtest2.text())/5
                s22=(mot2+sht2+workt2+testt2)/2

            sut20=s11+s22

            sut50=int(self.ui.ah30.text())+sut20
            db1=sqlite3.connect('mngschool3a.db')
            db1.row_factory=sqlite3.Row

            db1.execute("update ahya set mo1='{}',mo2='{}',sh1='{}',sh2='{}',test1='{}',test2='{}',work1='{}',work2='{}',s1='{}',s2='{}',su20='{}',su30='{}',su50='{}' where namst='{}' and namero='{}'".format(str(self.ui.ahmo1.text()),str(self.ui.ahmo2.text()),str(self.ui.ahsh1.text()),str(self.ui.ahsh2.text()),str(str(self.ui.ahtest1.text())),str(self.ui.ahtest2.text()),str(self.ui.ahwork1.text()),str(self.ui.ahwork2.text()),str(s11),str(s22),str(sut20),str(self.ui.ah30.text()),str(sut50),namstud,narow))
            db1.commit()
    def modtab3a6(self):####readeat
        namrow=str(self.ui.t1t2comrow.currentText()) 
        if namrow=="ثالثة علمي":
            narow=str(self.ui.t1t2comnamerow.currentText())
            namstud=str(self.ui.t1t2comnamstud.currentText())
            if int(self.ui.resh1.text())==0:
                s11=0
            if int(self.ui.rework1.text())==0:
                s11=0
            if int(self.ui.retest1.text())==0:
                s11=0
            if int(self.ui.remo1.text())==0:
                s11=0
            else:               
                mot1=int(self.ui.remo1.text())/5
                sht1=int(self.ui.resh1.text())/5
                workt1=int(self.ui.rework1.text())/5
                testt1=int(self.ui.retest1.text())/5
                s11=(mot1+sht1+workt1+testt1)/2

            if int(self.ui.resh2.text())==0:
                s22=0
            if int(self.ui.rework2.text())==0:
                s22=0
            if int(self.ui.retest2.text())==0:
                s22=0
            if int(self.ui.remo2.text())==0:
                s22=0
            else:
                        
                mot2=int(self.ui.remo2.text())/5
                sht2=int(self.ui.resh2.text())/5
                workt2=int(self.ui.rework2.text())/5
                testt2=int(self.ui.retest2.text())/5
                s22=(mot2+sht2+workt2+testt2)/2

            sut20=s11+s22

            sut50=int(self.ui.re30.text())+sut20
            db1=sqlite3.connect('mngschool3a.db')
            db1.row_factory=sqlite3.Row

            db1.execute("update readeat set mo1='{}',mo2='{}',sh1='{}',sh2='{}',test1='{}',test2='{}',work1='{}',work2='{}',s1='{}',s2='{}',su20='{}',su30='{}',su50='{}' where namst='{}' and namero='{}'".format(str(self.ui.remo1.text()),str(self.ui.remo2.text()),str(self.ui.resh1.text()),str(self.ui.resh2.text()),str(str(self.ui.retest1.text())),str(self.ui.retest2.text()),str(self.ui.rework1.text()),str(self.ui.rework2.text()),str(s11),str(s22),str(sut20),str(self.ui.re30.text()),str(sut50),namstud,narow))
            db1.commit()                
    def modtab3a7(self):
        namrow=str(self.ui.t1t2comrow.currentText()) 
        if namrow=="ثالثة علمي":
            narow=str(self.ui.t1t2comnamerow.currentText())
            namstud=str(self.ui.t1t2comnamstud.currentText())
            if int(self.ui.kish1.text())==0:
                s11=0
            if int(self.ui.kiwork1.text())==0:
                s11=0
            if int(self.ui.kitest1.text())==0:
                s11=0
            if int(self.ui.kimo1.text())==0:
                s11=0
            else:               
                mot1=int(self.ui.kimo1.text())/5
                sht1=int(self.ui.kish1.text())/5
                workt1=int(self.ui.kiwork1.text())/5
                testt1=int(self.ui.kitest1.text())/5
                s11=(mot1+sht1+workt1+testt1)/2

            if int(self.ui.kish2.text())==0:
                s22=0
            if int(self.ui.kiwork2.text())==0:
                s22=0
            if int(self.ui.kitest2.text())==0:
                s22=0
            if int(self.ui.kimo2.text())==0:
                s22=0
            else:
                        
                mot2=int(self.ui.kimo2.text())/5
                sht2=int(self.ui.kish2.text())/5
                workt2=int(self.ui.kiwork2.text())/5
                testt2=int(self.ui.kitest2.text())/5
                s22=(mot2+sht2+workt2+testt2)/2

            sut20=s11+s22

            sut50=int(self.ui.ki30.text())+sut20
            db1=sqlite3.connect('mngschool3a.db')
            db1.row_factory=sqlite3.Row

            db1.execute("update qimia set mo1='{}',mo2='{}',sh1='{}',sh2='{}',test1='{}',test2='{}',work1='{}',work2='{}',s1='{}',s2='{}',su20='{}',su30='{}',su50='{}' where namst='{}' and namero='{}'".format(str(self.ui.kimo1.text()),str(self.ui.kimo2.text()),str(self.ui.kish1.text()),str(self.ui.kish2.text()),str(str(self.ui.kitest1.text())),str(self.ui.kitest2.text()),str(self.ui.kiwork1.text()),str(self.ui.kiwork2.text()),str(s11),str(s22),str(sut20),str(self.ui.ki30.text()),str(sut50),namstud,narow))
            db1.commit()
    def modtab3a8(self):
        namrow=str(self.ui.t1t2comrow.currentText()) 
        if namrow=="ثالثة علمي":
            narow=str(self.ui.t1t2comnamerow.currentText())
            namstud=str(self.ui.t1t2comnamstud.currentText())
            if int(self.ui.vish1.text())==0:
                s11=0
            if int(self.ui.viwork1.text())==0:
                s11=0
            if int(self.ui.vitest1.text())==0:
                s11=0
            if int(self.ui.vimo1.text())==0:
                s11=0
            else:               
                mot1=int(self.ui.vimo1.text())/5
                sht1=int(self.ui.vish1.text())/5
                workt1=int(self.ui.viwork1.text())/5
                testt1=int(self.ui.vitest1.text())/5
                s11=(mot1+sht1+workt1+testt1)/2

            if int(self.ui.vish2.text())==0:
                s22=0
            if int(self.ui.viwork2.text())==0:
                s22=0
            if int(self.ui.vitest2.text())==0:
                s22=0
            if int(self.ui.vimo2.text())==0:
                s22=0
            else:
                        
                mot2=int(self.ui.vimo2.text())/5
                sht2=int(self.ui.vish2.text())/5
                workt2=int(self.ui.viwork2.text())/5
                testt2=int(self.ui.vitest2.text())/5
                s22=(mot2+sht2+workt2+testt2)/2

            sut20=s11+s22

            sut50=int(self.ui.vi30.text())+sut20
            db1=sqlite3.connect('mngschool3a.db')
            db1.row_factory=sqlite3.Row

            db1.execute("update visia set mo1='{}',mo2='{}',sh1='{}',sh2='{}',test1='{}',test2='{}',work1='{}',work2='{}',s1='{}',s2='{}',su20='{}',su30='{}',su50='{}' where namst='{}' and namero='{}'".format(str(self.ui.vimo1.text()),str(self.ui.vimo2.text()),str(self.ui.vish1.text()),str(self.ui.vish2.text()),str(str(self.ui.vitest1.text())),str(self.ui.vitest2.text()),str(self.ui.viwork1.text()),str(self.ui.viwork2.text()),str(s11),str(s22),str(sut20),str(self.ui.vi30.text()),str(sut50),namstud,narow))
            db1.commit()
###################################################2adby###############################################################33
    def showstu2d2(self):
        namrow=str(self.ui.t1t2comrow.currentText())
        if namrow=="ثانية ادبي": 
            narow=str(self.ui.t1t2comnamerow.currentText())
            namstud=str(self.ui.t1t2comnamstud.currentText())
            db1=sqlite3.connect('mngschool2d.db')
            db1.row_factory=sqlite3.Row
            sa1=db1.execute("select * from aslame where namst='{}' and namero='{}'".format(namstud,narow))
            for n in sa1:
                self.ui.asmo1.setText(n["mo1"])
                self.ui.asmo2.setText(n["mo2"])
                self.ui.assh1.setText(n["sh1"])
                self.ui.assh2.setText(n["sh2"])
                self.ui.astest1.setText(n["test1"])
                self.ui.astest2.setText(n["test2"])
                self.ui.aswork1.setText(n["work1"])
                self.ui.aswork2.setText(n["work2"])
                self.ui.assum1.setText(n["s1"])
                self.ui.assum2.setText(n["s2"])
                self.ui.as20.setText(n["su20"])
                self.ui.as30.setText(n["su30"])
                self.ui.as50.setText(n["su50"])
    def showstu2d3(self):
        namrow=str(self.ui.t1t2comrow.currentText())
        if namrow=="ثانية ادبي": 
            narow=str(self.ui.t1t2comnamerow.currentText())
            namstud=str(self.ui.t1t2comnamstud.currentText())
            db1=sqlite3.connect('mngschool2d.db')
            db1.row_factory=sqlite3.Row
            sa1=db1.execute("select * from arbic where namst='{}' and namero='{}'".format(namstud,narow))
            for n in sa1:
                self.ui.armo1.setText(n["mo1"])
                self.ui.armo2.setText(n["mo2"])
                self.ui.arsh1.setText(n["sh1"])
                self.ui.arsh2.setText(n["sh2"])
                self.ui.artest1.setText(n["test1"])
                self.ui.artest2.setText(n["test2"])
                self.ui.arwork1.setText(n["work1"])
                self.ui.arwork2.setText(n["work2"])
                self.ui.arsum1.setText(n["s1"])
                self.ui.arsum2.setText(n["s2"])
                self.ui.ar20.setText(n["su20"])
                self.ui.ar30.setText(n["su30"])
                self.ui.ar50.setText(n["su50"])
    def showstu2d4(self):
        namrow=str(self.ui.t1t2comrow.currentText())
        if namrow=="ثانية ادبي": 
            narow=str(self.ui.t1t2comnamerow.currentText())
            namstud=str(self.ui.t1t2comnamstud.currentText())
            db1=sqlite3.connect('mngschool2d.db')
            db1.row_factory=sqlite3.Row
            sa1=db1.execute("select * from english where namst='{}' and namero='{}'".format(namstud,narow))
            for n in sa1:
                self.ui.enmo1.setText(n["mo1"])
                self.ui.enmo2.setText(n["mo2"])
                self.ui.ensh1.setText(n["sh1"])
                self.ui.ensh2.setText(n["sh2"])
                self.ui.entest1.setText(n["test1"])
                self.ui.entest2.setText(n["test2"])
                self.ui.enwork1.setText(n["work1"])
                self.ui.enwork2.setText(n["work2"])
                self.ui.ensum1.setText(n["s1"])
                self.ui.ensum2.setText(n["s2"])
                self.ui.en20.setText(n["su20"])
                self.ui.en30.setText(n["su30"])
                self.ui.en50.setText(n["su50"])
    def showstu2d5(self):
        namrow=str(self.ui.t1t2comrow.currentText())
        if namrow=="ثانية ادبي": 
            narow=str(self.ui.t1t2comnamerow.currentText())
            namstud=str(self.ui.t1t2comnamstud.currentText())
            db1=sqlite3.connect('mngschool2d.db')
            db1.row_factory=sqlite3.Row
            sa1=db1.execute("select * from readeat where namst='{}' and namero='{}'".format(namstud,narow))
            for n in sa1:
                self.ui.remo1.setText(n["mo1"])
                self.ui.remo2.setText(n["mo2"])
                self.ui.resh1.setText(n["sh1"])
                self.ui.resh2.setText(n["sh2"])
                self.ui.retest1.setText(n["test1"])
                self.ui.retest2.setText(n["test2"])
                self.ui.rework1.setText(n["work1"])
                self.ui.rework2.setText(n["work2"])
                self.ui.resum1.setText(n["s1"])
                self.ui.resum2.setText(n["s2"])
                self.ui.re20.setText(n["su20"])
                self.ui.re30.setText(n["su30"])
                self.ui.re50.setText(n["su50"])                                   
    def showstu2d6(self):
        namrow=str(self.ui.t1t2comrow.currentText())
        if namrow=="ثانية ادبي": 
            narow=str(self.ui.t1t2comnamerow.currentText())
            namstud=str(self.ui.t1t2comnamstud.currentText())
            db1=sqlite3.connect('mngschool2d.db')
            db1.row_factory=sqlite3.Row
            sa1=db1.execute("select * from gjravi where namst='{}' and namero='{}'".format(namstud,narow))
            for n in sa1:
                self.ui.jgmo1.setText(n["mo1"])
                self.ui.jgmo2.setText(n["mo2"])
                self.ui.jgsh1.setText(n["sh1"])
                self.ui.jgsh2.setText(n["sh2"])
                self.ui.jgtest1.setText(n["test1"])
                self.ui.jgtest2.setText(n["test2"])
                self.ui.jgwork1.setText(n["work1"])
                self.ui.jgwork2.setText(n["work2"])
                self.ui.jgsum1.setText(n["s1"])
                self.ui.jgsum2.setText(n["s2"])
                self.ui.jg20.setText(n["su20"])
                self.ui.jg30.setText(n["su30"])
                self.ui.jg50.setText(n["su50"])
    def showstu2d7(self):
        namrow=str(self.ui.t1t2comrow.currentText())
        if namrow=="ثانية ادبي": 
            narow=str(self.ui.t1t2comnamerow.currentText())
            namstud=str(self.ui.t1t2comnamstud.currentText())
            db1=sqlite3.connect('mngschool2d.db')
            db1.row_factory=sqlite3.Row
            sa1=db1.execute("select * from treh where namst='{}' and namero='{}'".format(namstud,narow))
            for n in sa1:
                self.ui.trmo1.setText(n["mo1"])
                self.ui.trmo2.setText(n["mo2"])
                self.ui.trsh1.setText(n["sh1"])
                self.ui.trsh2.setText(n["sh2"])
                self.ui.trtest1.setText(n["test1"])
                self.ui.trtest2.setText(n["test2"])
                self.ui.trwork1.setText(n["work1"])
                self.ui.trwork2.setText(n["work2"])
                self.ui.trsum1.setText(n["s1"])
                self.ui.trsum2.setText(n["s2"])
                self.ui.tr20.setText(n["su20"])
                self.ui.tr30.setText(n["su30"])
                self.ui.tr50.setText(n["su50"])
    def showstu2d8(self):
        namrow=str(self.ui.t1t2comrow.currentText())
        if namrow=="ثانية ادبي": 
            narow=str(self.ui.t1t2comnamerow.currentText())
            namstud=str(self.ui.t1t2comnamstud.currentText())
            db1=sqlite3.connect('mngschool2d.db')
            db1.row_factory=sqlite3.Row
            sa1=db1.execute("select * from mbada where namst='{}' and namero='{}'".format(namstud,narow))
            for n in sa1:
                self.ui.mbmo1.setText(n["mo1"])
                self.ui.mbmo2.setText(n["mo2"])
                self.ui.mbsh1.setText(n["sh1"])
                self.ui.mbsh2.setText(n["sh2"])
                self.ui.mbtest1.setText(n["test1"])
                self.ui.mbtest2.setText(n["test2"])
                self.ui.mbwork1.setText(n["work1"])
                self.ui.mbwork2.setText(n["work2"])
                self.ui.mbsum1.setText(n["s1"])
                self.ui.mbsum2.setText(n["s2"])
                self.ui.mb20.setText(n["su20"])
                self.ui.mb30.setText(n["su30"])
                self.ui.mb50.setText(n["su50"])
    def showstu2d9(self):
        namrow=str(self.ui.t1t2comrow.currentText())
        if namrow=="ثانية ادبي": 
            narow=str(self.ui.t1t2comnamerow.currentText())
            namstud=str(self.ui.t1t2comnamstud.currentText())
            db1=sqlite3.connect('mngschool2d.db')
            db1.row_factory=sqlite3.Row
            sa1=db1.execute("select * from almaljtma where namst='{}' and namero='{}'".format(namstud,narow))
            for n in sa1:
                self.ui.almo1.setText(n["mo1"])
                self.ui.almo2.setText(n["mo2"])
                self.ui.alsh1.setText(n["sh1"])
                self.ui.alsh2.setText(n["sh2"])
                self.ui.altest1.setText(n["test1"])
                self.ui.altest2.setText(n["test2"])
                self.ui.alwork1.setText(n["work1"])
                self.ui.alwork2.setText(n["work2"])
                self.ui.alsum1.setText(n["s1"])
                self.ui.alsum2.setText(n["s2"])
                self.ui.al20.setText(n["su20"])
                self.ui.al30.setText(n["su30"])
                self.ui.al50.setText(n["su50"])


    def modtab2d2(self):
        namrow=str(self.ui.t1t2comrow.currentText()) 
        if namrow=="ثانية ادبي":
            narow=str(self.ui.t1t2comnamerow.currentText())
            namstud=str(self.ui.t1t2comnamstud.currentText())
            if int(self.ui.assh1.text())==0:
                s11=0
            if int(self.ui.aswork1.text())==0:
                s11=0
            if int(self.ui.astest1.text())==0:
                s11=0
            if int(self.ui.asmo1.text())==0:
                s11=0
            else:               
                mot1=int(self.ui.asmo1.text())/5
                sht1=int(self.ui.assh1.text())/5
                workt1=int(self.ui.aswork1.text())/5
                testt1=int(self.ui.astest1.text())/5
                s11=(mot1+sht1+workt1+testt1)/2

            if int(self.ui.assh2.text())==0:
                s22=0
            if int(self.ui.aswork2.text())==0:
                s22=0
            if int(self.ui.astest2.text())==0:
                s22=0
            if int(self.ui.asmo2.text())==0:
                s22=0
            else:
                        
                mot2=int(self.ui.asmo2.text())/5
                sht2=int(self.ui.assh2.text())/5
                workt2=int(self.ui.aswork2.text())/5
                testt2=int(self.ui.astest2.text())/5
                s22=(mot2+sht2+workt2+testt2)/2

            sut20=s11+s22

            sut50=int(self.ui.as30.text())+sut20
            db1=sqlite3.connect('mngschool2d.db')
            db1.row_factory=sqlite3.Row

            db1.execute("update aslame set mo1='{}',mo2='{}',sh1='{}',sh2='{}',test1='{}',test2='{}',work1='{}',work2='{}',s1='{}',s2='{}',su20='{}',su30='{}',su50='{}' where namst='{}' and namero='{}'".format(str(self.ui.asmo1.text()),str(self.ui.asmo2.text()),str(self.ui.assh1.text()),str(self.ui.assh2.text()),str(str(self.ui.astest1.text())),str(self.ui.astest2.text()),str(self.ui.aswork1.text()),str(self.ui.aswork2.text()),str(s11),str(s22),str(sut20),str(self.ui.as30.text()),str(sut50),namstud,narow))
            db1.commit()    

    def modtab2d3(self):
        namrow=str(self.ui.t1t2comrow.currentText()) 
        if namrow=="ثانية ادبي":
            narow=str(self.ui.t1t2comnamerow.currentText())
            namstud=str(self.ui.t1t2comnamstud.currentText())
            if int(self.ui.arsh1.text())==0:
                s11=0
            if int(self.ui.arwork1.text())==0:
                s11=0
            if int(self.ui.artest1.text())==0:
                s11=0
            if int(self.ui.armo1.text())==0:
                s11=0
            else:               
                mot1=int(self.ui.armo1.text())/5
                sht1=int(self.ui.arsh1.text())/5
                workt1=int(self.ui.arwork1.text())/5
                testt1=int(self.ui.artest1.text())/5
                s11=(mot1+sht1+workt1+testt1)/2

            if int(self.ui.arsh2.text())==0:
                s22=0
            if int(self.ui.arwork2.text())==0:
                s22=0
            if int(self.ui.artest2.text())==0:
                s22=0
            if int(self.ui.armo2.text())==0:
                s22=0
            else:
                        
                mot2=int(self.ui.armo2.text())/5
                sht2=int(self.ui.arsh2.text())/5
                workt2=int(self.ui.arwork2.text())/5
                testt2=int(self.ui.artest2.text())/5
                s22=(mot2+sht2+workt2+testt2)/2

            sut20=s11+s22

            sut50=int(self.ui.ar30.text())+sut20
            db1=sqlite3.connect('mngschool2d.db')
            db1.row_factory=sqlite3.Row

            db1.execute("update arbic set mo1='{}',mo2='{}',sh1='{}',sh2='{}',test1='{}',test2='{}',work1='{}',work2='{}',s1='{}',s2='{}',su20='{}',su30='{}',su50='{}' where namst='{}' and namero='{}'".format(str(self.ui.armo1.text()),str(self.ui.armo2.text()),str(self.ui.arsh1.text()),str(self.ui.arsh2.text()),str(str(self.ui.artest1.text())),str(self.ui.artest2.text()),str(self.ui.arwork1.text()),str(self.ui.arwork2.text()),str(s11),str(s22),str(sut20),str(self.ui.ar30.text()),str(sut50),namstud,narow))
            db1.commit()    
    def modtab2d4(self):
        namrow=str(self.ui.t1t2comrow.currentText()) 
        if namrow=="ثانية ادبي":
            narow=str(self.ui.t1t2comnamerow.currentText())
            namstud=str(self.ui.t1t2comnamstud.currentText())
            if int(self.ui.ensh1.text())==0:
                s11=0
            if int(self.ui.enwork1.text())==0:
                s11=0
            if int(self.ui.entest1.text())==0:
                s11=0
            if int(self.ui.enmo1.text())==0:
                s11=0
            else:               
                mot1=int(self.ui.enmo1.text())/5
                sht1=int(self.ui.ensh1.text())/5
                workt1=int(self.ui.enwork1.text())/5
                testt1=int(self.ui.entest1.text())/5
                s11=(mot1+sht1+workt1+testt1)/2

            if int(self.ui.ensh2.text())==0:
                s22=0
            if int(self.ui.enwork2.text())==0:
                s22=0
            if int(self.ui.entest2.text())==0:
                s22=0
            if int(self.ui.enmo2.text())==0:
                s22=0
            else:
                        
                mot2=int(self.ui.enmo2.text())/5
                sht2=int(self.ui.ensh2.text())/5
                workt2=int(self.ui.enwork2.text())/5
                testt2=int(self.ui.entest2.text())/5
                s22=(mot2+sht2+workt2+testt2)/2

            sut20=s11+s22

            sut50=int(self.ui.en30.text())+sut20
            db1=sqlite3.connect('mngschool2d.db')
            db1.row_factory=sqlite3.Row

            db1.execute("update english set mo1='{}',mo2='{}',sh1='{}',sh2='{}',test1='{}',test2='{}',work1='{}',work2='{}',s1='{}',s2='{}',su20='{}',su30='{}',su50='{}' where namst='{}' and namero='{}'".format(str(self.ui.enmo1.text()),str(self.ui.enmo2.text()),str(self.ui.ensh1.text()),str(self.ui.ensh2.text()),str(str(self.ui.entest1.text())),str(self.ui.entest2.text()),str(self.ui.enwork1.text()),str(self.ui.enwork2.text()),str(s11),str(s22),str(sut20),str(self.ui.en30.text()),str(sut50),namstud,narow))
            db1.commit()    
    def modtab2d5(self):
        namrow=str(self.ui.t1t2comrow.currentText()) 
        if namrow=="ثانية ادبي":
            narow=str(self.ui.t1t2comnamerow.currentText())
            namstud=str(self.ui.t1t2comnamstud.currentText())
            if int(self.ui.mbsh1.text())==0:
                s11=0
            if int(self.ui.mbwork1.text())==0:
                s11=0
            if int(self.ui.mbtest1.text())==0:
                s11=0
            if int(self.ui.mbmo1.text())==0:
                s11=0
            else:               
                mot1=int(self.ui.mbmo1.text())/5
                sht1=int(self.ui.mbsh1.text())/5
                workt1=int(self.ui.mbwork1.text())/5
                testt1=int(self.ui.mbtest1.text())/5
                s11=(mot1+sht1+workt1+testt1)/2

            if int(self.ui.mbsh2.text())==0:
                s22=0
            if int(self.ui.mbwork2.text())==0:
                s22=0
            if int(self.ui.mbtest2.text())==0:
                s22=0
            if int(self.ui.mbmo2.text())==0:
                s22=0
            else:
                        
                mot2=int(self.ui.mbmo2.text())/5
                sht2=int(self.ui.mbsh2.text())/5
                workt2=int(self.ui.mbwork2.text())/5
                testt2=int(self.ui.mbtest2.text())/5
                s22=(mot2+sht2+workt2+testt2)/2

            sut20=s11+s22

            sut50=int(self.ui.mb30.text())+sut20
            db1=sqlite3.connect('mngschool2d.db')
            db1.row_factory=sqlite3.Row

            db1.execute("update mbada set mo1='{}',mo2='{}',sh1='{}',sh2='{}',test1='{}',test2='{}',work1='{}',work2='{}',s1='{}',s2='{}',su20='{}',su30='{}',su50='{}' where namst='{}' and namero='{}'".format(str(self.ui.mbmo1.text()),str(self.ui.mbmo2.text()),str(self.ui.mbsh1.text()),str(self.ui.mbsh2.text()),str(str(self.ui.mbtest1.text())),str(self.ui.mbtest2.text()),str(self.ui.mbwork1.text()),str(self.ui.mbwork2.text()),str(s11),str(s22),str(sut20),str(self.ui.mb30.text()),str(sut50),namstud,narow))
            db1.commit()
    def modtab2d6(self):####readeat
        namrow=str(self.ui.t1t2comrow.currentText()) 
        if namrow=="ثانية ادبي":
            narow=str(self.ui.t1t2comnamerow.currentText())
            namstud=str(self.ui.t1t2comnamstud.currentText())
            if int(self.ui.resh1.text())==0:
                s11=0
            if int(self.ui.rework1.text())==0:
                s11=0
            if int(self.ui.retest1.text())==0:
                s11=0
            if int(self.ui.remo1.text())==0:
                s11=0
            else:               
                mot1=int(self.ui.remo1.text())/5
                sht1=int(self.ui.resh1.text())/5
                workt1=int(self.ui.rework1.text())/5
                testt1=int(self.ui.retest1.text())/5
                s11=(mot1+sht1+workt1+testt1)/2

            if int(self.ui.resh2.text())==0:
                s22=0
            if int(self.ui.rework2.text())==0:
                s22=0
            if int(self.ui.retest2.text())==0:
                s22=0
            if int(self.ui.remo2.text())==0:
                s22=0
            else:
                        
                mot2=int(self.ui.remo2.text())/5
                sht2=int(self.ui.resh2.text())/5
                workt2=int(self.ui.rework2.text())/5
                testt2=int(self.ui.retest2.text())/5
                s22=(mot2+sht2+workt2+testt2)/2

            sut20=s11+s22

            sut50=int(self.ui.re30.text())+sut20
            db1=sqlite3.connect('mngschool2d.db')
            db1.row_factory=sqlite3.Row

            db1.execute("update readeat set mo1='{}',mo2='{}',sh1='{}',sh2='{}',test1='{}',test2='{}',work1='{}',work2='{}',s1='{}',s2='{}',su20='{}',su30='{}',su50='{}' where namst='{}' and namero='{}'".format(str(self.ui.remo1.text()),str(self.ui.remo2.text()),str(self.ui.resh1.text()),str(self.ui.resh2.text()),str(str(self.ui.retest1.text())),str(self.ui.retest2.text()),str(self.ui.rework1.text()),str(self.ui.rework2.text()),str(s11),str(s22),str(sut20),str(self.ui.re30.text()),str(sut50),namstud,narow))
            db1.commit()
    def modtab2d7(self):
        namrow=str(self.ui.t1t2comrow.currentText()) 
        if namrow=="ثانية ادبي":
            narow=str(self.ui.t1t2comnamerow.currentText())
            namstud=str(self.ui.t1t2comnamstud.currentText())
            if int(self.ui.alsh1.text())==0:
                s11=0
            if int(self.ui.alwork1.text())==0:
                s11=0
            if int(self.ui.altest1.text())==0:
                s11=0
            if int(self.ui.almo1.text())==0:
                s11=0
            else:               
                mot1=int(self.ui.almo1.text())/5
                sht1=int(self.ui.alsh1.text())/5
                workt1=int(self.ui.alwork1.text())/5
                testt1=int(self.ui.altest1.text())/5
                s11=(mot1+sht1+workt1+testt1)/2

            if int(self.ui.alsh2.text())==0:
                s22=0
            if int(self.ui.alwork2.text())==0:
                s22=0
            if int(self.ui.altest2.text())==0:
                s22=0
            if int(self.ui.almo2.text())==0:
                s22=0
            else:
                        
                mot2=int(self.ui.almo2.text())/5
                sht2=int(self.ui.alsh2.text())/5
                workt2=int(self.ui.alwork2.text())/5
                testt2=int(self.ui.altest2.text())/5
                s22=(mot2+sht2+workt2+testt2)/2

            sut20=s11+s22

            sut50=int(self.ui.al30.text())+sut20
            db1=sqlite3.connect('mngschool2d.db')
            db1.row_factory=sqlite3.Row

            db1.execute("update almaljtma set mo1='{}',mo2='{}',sh1='{}',sh2='{}',test1='{}',test2='{}',work1='{}',work2='{}',s1='{}',s2='{}',su20='{}',su30='{}',su50='{}' where namst='{}' and namero='{}'".format(str(self.ui.almo1.text()),str(self.ui.almo2.text()),str(self.ui.alsh1.text()),str(self.ui.alsh2.text()),str(str(self.ui.altest1.text())),str(self.ui.altest2.text()),str(self.ui.alwork1.text()),str(self.ui.alwork2.text()),str(s11),str(s22),str(sut20),str(self.ui.al30.text()),str(sut50),namstud,narow))
            db1.commit()
    
    def modtab2d8(self):
        namrow=str(self.ui.t1t2comrow.currentText()) 
        if namrow=="ثانية ادبي":
            narow=str(self.ui.t1t2comnamerow.currentText())
            namstud=str(self.ui.t1t2comnamstud.currentText())
            if int(self.ui.jgsh1.text())==0:
                s11=0
            if int(self.ui.jgwork1.text())==0:
                s11=0
            if int(self.ui.jgtest1.text())==0:
                s11=0
            if int(self.ui.jgmo1.text())==0:
                s11=0
            else:               
                mot1=int(self.ui.jgmo1.text())/5
                sht1=int(self.ui.jgsh1.text())/5
                workt1=int(self.ui.jgwork1.text())/5
                testt1=int(self.ui.jgtest1.text())/5
                s11=(mot1+sht1+workt1+testt1)/2

            if int(self.ui.jgsh2.text())==0:
                s22=0
            if int(self.ui.jgwork2.text())==0:
                s22=0
            if int(self.ui.jgtest2.text())==0:
                s22=0
            if int(self.ui.jgmo2.text())==0:
                s22=0
            else:
                        
                mot2=int(self.ui.jgmo2.text())/5
                sht2=int(self.ui.jgsh2.text())/5
                workt2=int(self.ui.jgwork2.text())/5
                testt2=int(self.ui.jgtest2.text())/5
                s22=(mot2+sht2+workt2+testt2)/2

            sut20=s11+s22

            sut50=int(self.ui.jg30.text())+sut20
            db1=sqlite3.connect('mngschool2d.db')
            db1.row_factory=sqlite3.Row

            db1.execute("update gjravi set mo1='{}',mo2='{}',sh1='{}',sh2='{}',test1='{}',test2='{}',work1='{}',work2='{}',s1='{}',s2='{}',su20='{}',su30='{}',su50='{}' where namst='{}' and namero='{}'".format(str(self.ui.jgmo1.text()),str(self.ui.jgmo2.text()),str(self.ui.jgsh1.text()),str(self.ui.jgsh2.text()),str(str(self.ui.jgtest1.text())),str(self.ui.jgtest2.text()),str(self.ui.jgwork1.text()),str(self.ui.jgwork2.text()),str(s11),str(s22),str(sut20),str(self.ui.jg30.text()),str(sut50),namstud,narow))
            db1.commit()
    def modtab2d9(self):
        namrow=str(self.ui.t1t2comrow.currentText()) 
        if namrow=="ثانية ادبي":
            narow=str(self.ui.t1t2comnamerow.currentText())
            namstud=str(self.ui.t1t2comnamstud.currentText())
            if int(self.ui.trsh1.text())==0:
                s11=0
            if int(self.ui.trwork1.text())==0:
                s11=0
            if int(self.ui.trtest1.text())==0:
                s11=0
            if int(self.ui.trmo1.text())==0:
                s11=0
            else:               
                mot1=int(self.ui.trmo1.text())/5
                sht1=int(self.ui.trsh1.text())/5
                workt1=int(self.ui.trwork1.text())/5
                testt1=int(self.ui.trtest1.text())/5
                s11=(mot1+sht1+workt1+testt1)/2

            if int(self.ui.trsh2.text())==0:
                s22=0
            if int(self.ui.trwork2.text())==0:
                s22=0
            if int(self.ui.trtest2.text())==0:
                s22=0
            if int(self.ui.trmo2.text())==0:
                s22=0
            else:
                        
                mot2=int(self.ui.trmo2.text())/5
                sht2=int(self.ui.trsh2.text())/5
                workt2=int(self.ui.trwork2.text())/5
                testt2=int(self.ui.trtest2.text())/5
                s22=(mot2+sht2+workt2+testt2)/2

            sut20=s11+s22

            sut50=int(self.ui.tr30.text())+sut20
            db1=sqlite3.connect('mngschool2d.db')
            db1.row_factory=sqlite3.Row

            db1.execute("update treh set mo1='{}',mo2='{}',sh1='{}',sh2='{}',test1='{}',test2='{}',work1='{}',work2='{}',s1='{}',s2='{}',su20='{}',su30='{}',su50='{}' where namst='{}' and namero='{}'".format(str(self.ui.trmo1.text()),str(self.ui.trmo2.text()),str(self.ui.trsh1.text()),str(self.ui.trsh2.text()),str(str(self.ui.trtest1.text())),str(self.ui.trtest2.text()),str(self.ui.trwork1.text()),str(self.ui.trwork2.text()),str(s11),str(s22),str(sut20),str(self.ui.tr30.text()),str(sut50),namstud,narow))
            db1.commit()    
#################################################3adby####################################################################
###############################################################################################################################
    def showstu3d2(self):
        namrow=str(self.ui.t1t2comrow.currentText())
        if namrow=="ثالثة ادبي": 
            narow=str(self.ui.t1t2comnamerow.currentText())
            namstud=str(self.ui.t1t2comnamstud.currentText())
            db1=sqlite3.connect('mngschool3d.db')
            db1.row_factory=sqlite3.Row
            sa1=db1.execute("select * from aslame where namst='{}' and namero='{}'".format(namstud,narow))
            for n in sa1:
                self.ui.asmo1.setText(n["mo1"])
                self.ui.asmo2.setText(n["mo2"])
                self.ui.assh1.setText(n["sh1"])
                self.ui.assh2.setText(n["sh2"])
                self.ui.astest1.setText(n["test1"])
                self.ui.astest2.setText(n["test2"])
                self.ui.aswork1.setText(n["work1"])
                self.ui.aswork2.setText(n["work2"])
                self.ui.assum1.setText(n["s1"])
                self.ui.assum2.setText(n["s2"])
                self.ui.as20.setText(n["su20"])
                self.ui.as30.setText(n["su30"])
                self.ui.as50.setText(n["su50"])
    def showstu3d3(self):
        namrow=str(self.ui.t1t2comrow.currentText())
        if namrow=="ثالثة ادبي": 
            narow=str(self.ui.t1t2comnamerow.currentText())
            namstud=str(self.ui.t1t2comnamstud.currentText())
            db1=sqlite3.connect('mngschool3d.db')
            db1.row_factory=sqlite3.Row
            sa1=db1.execute("select * from arbic where namst='{}' and namero='{}'".format(namstud,narow))
            for n in sa1:
                self.ui.armo1.setText(n["mo1"])
                self.ui.armo2.setText(n["mo2"])
                self.ui.arsh1.setText(n["sh1"])
                self.ui.arsh2.setText(n["sh2"])
                self.ui.artest1.setText(n["test1"])
                self.ui.artest2.setText(n["test2"])
                self.ui.arwork1.setText(n["work1"])
                self.ui.arwork2.setText(n["work2"])
                self.ui.arsum1.setText(n["s1"])
                self.ui.arsum2.setText(n["s2"])
                self.ui.ar20.setText(n["su20"])
                self.ui.ar30.setText(n["su30"])
                self.ui.ar50.setText(n["su50"])
    def showstu3d4(self):
        namrow=str(self.ui.t1t2comrow.currentText())
        if namrow=="ثالثة ادبي": 
            narow=str(self.ui.t1t2comnamerow.currentText())
            namstud=str(self.ui.t1t2comnamstud.currentText())
            db1=sqlite3.connect('mngschool3d.db')
            db1.row_factory=sqlite3.Row
            sa1=db1.execute("select * from english where namst='{}' and namero='{}'".format(namstud,narow))
            for n in sa1:
                self.ui.enmo1.setText(n["mo1"])
                self.ui.enmo2.setText(n["mo2"])
                self.ui.ensh1.setText(n["sh1"])
                self.ui.ensh2.setText(n["sh2"])
                self.ui.entest1.setText(n["test1"])
                self.ui.entest2.setText(n["test2"])
                self.ui.enwork1.setText(n["work1"])
                self.ui.enwork2.setText(n["work2"])
                self.ui.ensum1.setText(n["s1"])
                self.ui.ensum2.setText(n["s2"])
                self.ui.en20.setText(n["su20"])
                self.ui.en30.setText(n["su30"])
                self.ui.en50.setText(n["su50"])
    def showstu3d5(self):
        namrow=str(self.ui.t1t2comrow.currentText())
        if namrow=="ثالثة ادبي": 
            narow=str(self.ui.t1t2comnamerow.currentText())
            namstud=str(self.ui.t1t2comnamstud.currentText())
            db1=sqlite3.connect('mngschool3d.db')
            db1.row_factory=sqlite3.Row
            sa1=db1.execute("select * from readeat where namst='{}' and namero='{}'".format(namstud,narow))
            for n in sa1:
                self.ui.remo1.setText(n["mo1"])
                self.ui.remo2.setText(n["mo2"])
                self.ui.resh1.setText(n["sh1"])
                self.ui.resh2.setText(n["sh2"])
                self.ui.retest1.setText(n["test1"])
                self.ui.retest2.setText(n["test2"])
                self.ui.rework1.setText(n["work1"])
                self.ui.rework2.setText(n["work2"])
                self.ui.resum1.setText(n["s1"])
                self.ui.resum2.setText(n["s2"])
                self.ui.re20.setText(n["su20"])
                self.ui.re30.setText(n["su30"])
                self.ui.re50.setText(n["su50"])                                   
    def showstu3d6(self):
        namrow=str(self.ui.t1t2comrow.currentText())
        if namrow=="ثالثة ادبي": 
            narow=str(self.ui.t1t2comnamerow.currentText())
            namstud=str(self.ui.t1t2comnamstud.currentText())
            db1=sqlite3.connect('mngschool3d.db')
            db1.row_factory=sqlite3.Row
            sa1=db1.execute("select * from gjmap where namst='{}' and namero='{}'".format(namstud,narow))
            for n in sa1:
                self.ui.jmmo1.setText(n["mo1"])
                self.ui.jmmo2.setText(n["mo2"])
                self.ui.jmsh1.setText(n["sh1"])
                self.ui.jmsh2.setText(n["sh2"])
                self.ui.jmtest1.setText(n["test1"])
                self.ui.jmtest2.setText(n["test2"])
                self.ui.jmwork1.setText(n["work1"])
                self.ui.jmwork2.setText(n["work2"])
                self.ui.jmsum1.setText(n["s1"])
                self.ui.jmsum2.setText(n["s2"])
                self.ui.jm20.setText(n["su20"])
                self.ui.jm30.setText(n["su30"])
                self.ui.jm50.setText(n["su50"])
    def showstu3d7(self):
        namrow=str(self.ui.t1t2comrow.currentText())
        if namrow=="ثالثة ادبي": 
            narow=str(self.ui.t1t2comnamerow.currentText())
            namstud=str(self.ui.t1t2comnamstud.currentText())
            db1=sqlite3.connect('mngschool3d.db')
            db1.row_factory=sqlite3.Row
            sa1=db1.execute("select * from treh where namst='{}' and namero='{}'".format(namstud,narow))
            for n in sa1:
                self.ui.trmo1.setText(n["mo1"])
                self.ui.trmo2.setText(n["mo2"])
                self.ui.trsh1.setText(n["sh1"])
                self.ui.trsh2.setText(n["sh2"])
                self.ui.trtest1.setText(n["test1"])
                self.ui.trtest2.setText(n["test2"])
                self.ui.trwork1.setText(n["work1"])
                self.ui.trwork2.setText(n["work2"])
                self.ui.trsum1.setText(n["s1"])
                self.ui.trsum2.setText(n["s2"])
                self.ui.tr20.setText(n["su20"])
                self.ui.tr30.setText(n["su30"])
                self.ui.tr50.setText(n["su50"])
    def showstu3d8(self):
        namrow=str(self.ui.t1t2comrow.currentText())
        if namrow=="ثالثة ادبي": 
            narow=str(self.ui.t1t2comnamerow.currentText())
            namstud=str(self.ui.t1t2comnamstud.currentText())
            db1=sqlite3.connect('mngschool3d.db')
            db1.row_factory=sqlite3.Row
            sa1=db1.execute("select * from ffff where namst='{}' and namero='{}'".format(namstud,narow))
            for n in sa1:
                self.ui.ffmo1.setText(n["mo1"])
                self.ui.ffmo2.setText(n["mo2"])
                self.ui.ffsh1.setText(n["sh1"])
                self.ui.ffsh2.setText(n["sh2"])
                self.ui.fftest1.setText(n["test1"])
                self.ui.fftest2.setText(n["test2"])
                self.ui.ffwork1.setText(n["work1"])
                self.ui.ffwork2.setText(n["work2"])
                self.ui.ffsum1.setText(n["s1"])
                self.ui.ffsum2.setText(n["s2"])
                self.ui.ff20.setText(n["su20"])
                self.ui.ff30.setText(n["su30"])
                self.ui.ff50.setText(n["su50"])

    def modtab3d2(self):
        namrow=str(self.ui.t1t2comrow.currentText()) 
        if namrow=="ثالثة ادبي":
            narow=str(self.ui.t1t2comnamerow.currentText())
            namstud=str(self.ui.t1t2comnamstud.currentText())
            if int(self.ui.assh1.text())==0:
                s11=0
            if int(self.ui.aswork1.text())==0:
                s11=0
            if int(self.ui.astest1.text())==0:
                s11=0
            if int(self.ui.asmo1.text())==0:
                s11=0
            else:               
                mot1=int(self.ui.asmo1.text())/5
                sht1=int(self.ui.assh1.text())/5
                workt1=int(self.ui.aswork1.text())/5
                testt1=int(self.ui.astest1.text())/5
                s11=(mot1+sht1+workt1+testt1)/2

            if int(self.ui.assh2.text())==0:
                s22=0
            if int(self.ui.aswork2.text())==0:
                s22=0
            if int(self.ui.astest2.text())==0:
                s22=0
            if int(self.ui.asmo2.text())==0:
                s22=0
            else:
                        
                mot2=int(self.ui.asmo2.text())/5
                sht2=int(self.ui.assh2.text())/5
                workt2=int(self.ui.aswork2.text())/5
                testt2=int(self.ui.astest2.text())/5
                s22=(mot2+sht2+workt2+testt2)/2

            sut20=s11+s22

            sut50=int(self.ui.as30.text())+sut20
            db1=sqlite3.connect('mngschool3d.db')
            db1.row_factory=sqlite3.Row

            db1.execute("update aslame set mo1='{}',mo2='{}',sh1='{}',sh2='{}',test1='{}',test2='{}',work1='{}',work2='{}',s1='{}',s2='{}',su20='{}',su30='{}',su50='{}' where namst='{}' and namero='{}'".format(str(self.ui.asmo1.text()),str(self.ui.asmo2.text()),str(self.ui.assh1.text()),str(self.ui.assh2.text()),str(str(self.ui.astest1.text())),str(self.ui.astest2.text()),str(self.ui.aswork1.text()),str(self.ui.aswork2.text()),str(s11),str(s22),str(sut20),str(self.ui.as30.text()),str(sut50),namstud,narow))
            db1.commit()    

    def modtab3d3(self):
        namrow=str(self.ui.t1t2comrow.currentText()) 
        if namrow=="ثالثة ادبي":
            narow=str(self.ui.t1t2comnamerow.currentText())
            namstud=str(self.ui.t1t2comnamstud.currentText())
            if int(self.ui.arsh1.text())==0:
                s11=0
            if int(self.ui.arwork1.text())==0:
                s11=0
            if int(self.ui.artest1.text())==0:
                s11=0
            if int(self.ui.armo1.text())==0:
                s11=0
            else:               
                mot1=int(self.ui.armo1.text())/5
                sht1=int(self.ui.arsh1.text())/5
                workt1=int(self.ui.arwork1.text())/5
                testt1=int(self.ui.artest1.text())/5
                s11=(mot1+sht1+workt1+testt1)/2

            if int(self.ui.arsh2.text())==0:
                s22=0
            if int(self.ui.arwork2.text())==0:
                s22=0
            if int(self.ui.artest2.text())==0:
                s22=0
            if int(self.ui.armo2.text())==0:
                s22=0
            else:
                        
                mot2=int(self.ui.armo2.text())/5
                sht2=int(self.ui.arsh2.text())/5
                workt2=int(self.ui.arwork2.text())/5
                testt2=int(self.ui.artest2.text())/5
                s22=(mot2+sht2+workt2+testt2)/2

            sut20=s11+s22

            sut50=int(self.ui.ar30.text())+sut20
            db1=sqlite3.connect('mngschool3d.db')
            db1.row_factory=sqlite3.Row

            db1.execute("update arbic set mo1='{}',mo2='{}',sh1='{}',sh2='{}',test1='{}',test2='{}',work1='{}',work2='{}',s1='{}',s2='{}',su20='{}',su30='{}',su50='{}' where namst='{}' and namero='{}'".format(str(self.ui.armo1.text()),str(self.ui.armo2.text()),str(self.ui.arsh1.text()),str(self.ui.arsh2.text()),str(str(self.ui.artest1.text())),str(self.ui.artest2.text()),str(self.ui.arwork1.text()),str(self.ui.arwork2.text()),str(s11),str(s22),str(sut20),str(self.ui.ar30.text()),str(sut50),namstud,narow))
            db1.commit()    
    def modtab3d4(self):
        namrow=str(self.ui.t1t2comrow.currentText()) 
        if namrow=="ثالثة ادبي":
            narow=str(self.ui.t1t2comnamerow.currentText())
            namstud=str(self.ui.t1t2comnamstud.currentText())
            if int(self.ui.ensh1.text())==0:
                s11=0
            if int(self.ui.enwork1.text())==0:
                s11=0
            if int(self.ui.entest1.text())==0:
                s11=0
            if int(self.ui.enmo1.text())==0:
                s11=0
            else:               
                mot1=int(self.ui.enmo1.text())/5
                sht1=int(self.ui.ensh1.text())/5
                workt1=int(self.ui.enwork1.text())/5
                testt1=int(self.ui.entest1.text())/5
                s11=(mot1+sht1+workt1+testt1)/2

            if int(self.ui.ensh2.text())==0:
                s22=0
            if int(self.ui.enwork2.text())==0:
                s22=0
            if int(self.ui.entest2.text())==0:
                s22=0
            if int(self.ui.enmo2.text())==0:
                s22=0
            else:
                        
                mot2=int(self.ui.enmo2.text())/5
                sht2=int(self.ui.ensh2.text())/5
                workt2=int(self.ui.enwork2.text())/5
                testt2=int(self.ui.entest2.text())/5
                s22=(mot2+sht2+workt2+testt2)/2

            sut20=s11+s22

            sut50=int(self.ui.en30.text())+sut20
            db1=sqlite3.connect('mngschool3d.db')
            db1.row_factory=sqlite3.Row

            db1.execute("update english set mo1='{}',mo2='{}',sh1='{}',sh2='{}',test1='{}',test2='{}',work1='{}',work2='{}',s1='{}',s2='{}',su20='{}',su30='{}',su50='{}' where namst='{}' and namero='{}'".format(str(self.ui.enmo1.text()),str(self.ui.enmo2.text()),str(self.ui.ensh1.text()),str(self.ui.ensh2.text()),str(str(self.ui.entest1.text())),str(self.ui.entest2.text()),str(self.ui.enwork1.text()),str(self.ui.enwork2.text()),str(s11),str(s22),str(sut20),str(self.ui.en30.text()),str(sut50),namstud,narow))
            db1.commit()    
    def modtab3d5(self):
        namrow=str(self.ui.t1t2comrow.currentText()) 
        if namrow=="ثالثة ادبي":
            narow=str(self.ui.t1t2comnamerow.currentText())
            namstud=str(self.ui.t1t2comnamstud.currentText())
            if int(self.ui.jmsh1.text())==0:
                s11=0
            if int(self.ui.jmwork1.text())==0:
                s11=0
            if int(self.ui.jmtest1.text())==0:
                s11=0
            if int(self.ui.jmmo1.text())==0:
                s11=0
            else:               
                mot1=int(self.ui.jmmo1.text())/5
                sht1=int(self.ui.jmsh1.text())/5
                workt1=int(self.ui.jmwork1.text())/5
                testt1=int(self.ui.jmtest1.text())/5
                s11=(mot1+sht1+workt1+testt1)/2

            if int(self.ui.jmsh2.text())==0:
                s22=0
            if int(self.ui.jmwork2.text())==0:
                s22=0
            if int(self.ui.jmtest2.text())==0:
                s22=0
            if int(self.ui.jmmo2.text())==0:
                s22=0
            else:
                        
                mot2=int(self.ui.jmmo2.text())/5
                sht2=int(self.ui.jmsh2.text())/5
                workt2=int(self.ui.jmwork2.text())/5
                testt2=int(self.ui.jmtest2.text())/5
                s22=(mot2+sht2+workt2+testt2)/2

            sut20=s11+s22

            sut50=int(self.ui.jm30.text())+sut20
            db1=sqlite3.connect('mngschool3d.db')
            db1.row_factory=sqlite3.Row

            db1.execute("update gjmap set mo1='{}',mo2='{}',sh1='{}',sh2='{}',test1='{}',test2='{}',work1='{}',work2='{}',s1='{}',s2='{}',su20='{}',su30='{}',su50='{}' where namst='{}' and namero='{}'".format(str(self.ui.jmmo1.text()),str(self.ui.jmmo2.text()),str(self.ui.jmsh1.text()),str(self.ui.jmsh2.text()),str(str(self.ui.jmtest1.text())),str(self.ui.jmtest2.text()),str(self.ui.jmwork1.text()),str(self.ui.jmwork2.text()),str(s11),str(s22),str(sut20),str(self.ui.jm30.text()),str(sut50),namstud,narow))
            db1.commit()
    def modtab3d6(self):####readeat
        namrow=str(self.ui.t1t2comrow.currentText()) 
        if namrow=="ثالثة ادبي":
            narow=str(self.ui.t1t2comnamerow.currentText())
            namstud=str(self.ui.t1t2comnamstud.currentText())
            if int(self.ui.resh1.text())==0:
                s11=0
            if int(self.ui.rework1.text())==0:
                s11=0
            if int(self.ui.retest1.text())==0:
                s11=0
            if int(self.ui.remo1.text())==0:
                s11=0
            else:               
                mot1=int(self.ui.remo1.text())/5
                sht1=int(self.ui.resh1.text())/5
                workt1=int(self.ui.rework1.text())/5
                testt1=int(self.ui.retest1.text())/5
                s11=(mot1+sht1+workt1+testt1)/2

            if int(self.ui.resh2.text())==0:
                s22=0
            if int(self.ui.rework2.text())==0:
                s22=0
            if int(self.ui.retest2.text())==0:
                s22=0
            if int(self.ui.remo2.text())==0:
                s22=0
            else:
                        
                mot2=int(self.ui.remo2.text())/5
                sht2=int(self.ui.resh2.text())/5
                workt2=int(self.ui.rework2.text())/5
                testt2=int(self.ui.retest2.text())/5
                s22=(mot2+sht2+workt2+testt2)/2

            sut20=s11+s22

            sut50=int(self.ui.re30.text())+sut20
            db1=sqlite3.connect('mngschool3d.db')
            db1.row_factory=sqlite3.Row

            db1.execute("update readeat set mo1='{}',mo2='{}',sh1='{}',sh2='{}',test1='{}',test2='{}',work1='{}',work2='{}',s1='{}',s2='{}',su20='{}',su30='{}',su50='{}' where namst='{}' and namero='{}'".format(str(self.ui.remo1.text()),str(self.ui.remo2.text()),str(self.ui.resh1.text()),str(self.ui.resh2.text()),str(str(self.ui.retest1.text())),str(self.ui.retest2.text()),str(self.ui.rework1.text()),str(self.ui.rework2.text()),str(s11),str(s22),str(sut20),str(self.ui.re30.text()),str(sut50),namstud,narow))
            db1.commit()
    def modtab3d7(self):
        namrow=str(self.ui.t1t2comrow.currentText()) 
        if namrow=="ثالثة ادبي":
            narow=str(self.ui.t1t2comnamerow.currentText())
            namstud=str(self.ui.t1t2comnamstud.currentText())
            if int(self.ui.ffsh1.text())==0:
                s11=0
            if int(self.ui.ffwork1.text())==0:
                s11=0
            if int(self.ui.fftest1.text())==0:
                s11=0
            if int(self.ui.ffmo1.text())==0:
                s11=0
            else:               
                mot1=int(self.ui.ffmo1.text())/5
                sht1=int(self.ui.ffsh1.text())/5
                workt1=int(self.ui.ffwork1.text())/5
                testt1=int(self.ui.fftest1.text())/5
                s11=(mot1+sht1+workt1+testt1)/2

            if int(self.ui.ffsh2.text())==0:
                s22=0
            if int(self.ui.ffwork2.text())==0:
                s22=0
            if int(self.ui.fftest2.text())==0:
                s22=0
            if int(self.ui.ffmo2.text())==0:
                s22=0
            else:
                        
                mot2=int(self.ui.ffmo2.text())/5
                sht2=int(self.ui.ffsh2.text())/5
                workt2=int(self.ui.ffwork2.text())/5
                testt2=int(self.ui.fftest2.text())/5
                s22=(mot2+sht2+workt2+testt2)/2

            sut20=s11+s22

            sut50=int(self.ui.ff30.text())+sut20
            db1=sqlite3.connect('mngschool3d.db')
            db1.row_factory=sqlite3.Row

            db1.execute("update ffff set mo1='{}',mo2='{}',sh1='{}',sh2='{}',test1='{}',test2='{}',work1='{}',work2='{}',s1='{}',s2='{}',su20='{}',su30='{}',su50='{}' where namst='{}' and namero='{}'".format(str(self.ui.ffmo1.text()),str(self.ui.ffmo2.text()),str(self.ui.ffsh1.text()),str(self.ui.ffsh2.text()),str(str(self.ui.fftest1.text())),str(self.ui.fftest2.text()),str(self.ui.ffwork1.text()),str(self.ui.ffwork2.text()),str(s11),str(s22),str(sut20),str(self.ui.ff30.text()),str(sut50),namstud,narow))
            db1.commit()
    
    def modtab3d8(self):
        namrow=str(self.ui.t1t2comrow.currentText()) 
        if namrow=="ثالثة ادبي":
            narow=str(self.ui.t1t2comnamerow.currentText())
            namstud=str(self.ui.t1t2comnamstud.currentText())
            if int(self.ui.trsh1.text())==0:
                s11=0
            if int(self.ui.trwork1.text())==0:
                s11=0
            if int(self.ui.trtest1.text())==0:
                s11=0
            if int(self.ui.trmo1.text())==0:
                s11=0
            else:               
                mot1=int(self.ui.trmo1.text())/5
                sht1=int(self.ui.trsh1.text())/5
                workt1=int(self.ui.trwork1.text())/5
                testt1=int(self.ui.trtest1.text())/5
                s11=(mot1+sht1+workt1+testt1)/2

            if int(self.ui.trsh2.text())==0:
                s22=0
            if int(self.ui.trwork2.text())==0:
                s22=0
            if int(self.ui.trtest2.text())==0:
                s22=0
            if int(self.ui.trmo2.text())==0:
                s22=0
            else:
                        
                mot2=int(self.ui.trmo2.text())/5
                sht2=int(self.ui.trsh2.text())/5
                workt2=int(self.ui.trwork2.text())/5
                testt2=int(self.ui.trtest2.text())/5
                s22=(mot2+sht2+workt2+testt2)/2

            sut20=s11+s22

            sut50=int(self.ui.tr30.text())+sut20
            db1=sqlite3.connect('mngschool3d.db')
            db1.row_factory=sqlite3.Row

            db1.execute("update treh set mo1='{}',mo2='{}',sh1='{}',sh2='{}',test1='{}',test2='{}',work1='{}',work2='{}',s1='{}',s2='{}',su20='{}',su30='{}',su50='{}' where namst='{}' and namero='{}'".format(str(self.ui.trmo1.text()),str(self.ui.trmo2.text()),str(self.ui.trsh1.text()),str(self.ui.trsh2.text()),str(str(self.ui.trtest1.text())),str(self.ui.trtest2.text()),str(self.ui.trwork1.text()),str(self.ui.trwork2.text()),str(s11),str(s22),str(sut20),str(self.ui.tr30.text()),str(sut50),namstud,narow))
            db1.commit()
##################################################stop##############################################################
#################################################stop######################################################################
    def jmmm(self):
        self.ui.jmtest2.setText("X")
        self.ui.jmtest1.setText("X")
        self.ui.jmmo1.setText("X")
        self.ui.jmmo2.setText("X")
        self.ui.jmwork2.setText("X")
        self.ui.jmwork1.setText("X")
        self.ui.jmsh2.setText("X")
        self.ui.jmsh1.setText("X")
        self.ui.jmsum1.setText("X")
        self.ui.jmsum2.setText("X")
        self.ui.jm30 .setText("X")
        self.ui.jm20.setText("X")
        self.ui.jm50.setText("X")
    def jgrr(self):
        self.ui.jgtest2.setText("X")
        self.ui.jgtest1.setText("X")
        self.ui.jgmo1.setText("X")
        self.ui.jgmo2.setText("X")
        self.ui.jgwork2.setText("X")
        self.ui.jgwork1.setText("X")
        self.ui.jgsh2.setText("X")
        self.ui.jgsh1.setText("X")
        self.ui.jgsum1.setText("X")
        self.ui.jgsum2.setText("X")
        self.ui.jg30 .setText("X")
        self.ui.jg20.setText("X")
        self.ui.jg50.setText("X")
    def flsfh(self):
        self.ui.fftest2.setText("X")
        self.ui.fftest1.setText("X")
        self.ui.ffmo1.setText("X")
        self.ui.ffmo2.setText("X")
        self.ui.ffwork2.setText("X")
        self.ui.ffwork1.setText("X")
        self.ui.ffsh2.setText("X")
        self.ui.ffsh1.setText("X")
        self.ui.ffsum1.setText("X")
        self.ui.ffsum2.setText("X")
        self.ui.ff30 .setText("X")
        self.ui.ff20.setText("X")
        self.ui.ff50.setText("X")
    def trehh(self):
        self.ui.trtest2.setText("X")
        self.ui.trtest1.setText("X")
        self.ui.trmo1.setText("X")
        self.ui.trmo2.setText("X")
        self.ui.trwork2.setText("X")
        self.ui.trwork1.setText("X")
        self.ui.trsh2.setText("X")
        self.ui.trsh1.setText("X")
        self.ui.trsum1.setText("X")
        self.ui.trsum2.setText("X")
        self.ui.tr30 .setText("X")
        self.ui.tr20.setText("X")
        self.ui.tr50.setText("X")
    def mjtmaa(self):
        self.ui.mjtest2.setText("X")
        self.ui.mjtest1.setText("X")
        self.ui.mjmo1.setText("X")
        self.ui.mjmo2.setText("X")
        self.ui.mjwork2.setText("X")
        self.ui.mjwork1.setText("X")
        self.ui.mjsh2.setText("X")
        self.ui.mjsh1.setText("X")
        self.ui.mjsum1.setText("X")
        self.ui.mjsum2.setText("X")
        self.ui.mj30 .setText("X")
        self.ui.mj20.setText("X")
        self.ui.mj50.setText("X")
    def mbadaalm(self):
        self.ui.mbtest2.setText("X")
        self.ui.mbtest1.setText("X")
        self.ui.mbmo1.setText("X")
        self.ui.mbmo2.setText("X")
        self.ui.mbwork2.setText("X")
        self.ui.mbwork1.setText("X")
        self.ui.mbsh2.setText("X")
        self.ui.mbsh1.setText("X")
        self.ui.mbsum1.setText("X")
        self.ui.mbsum2.setText("X")
        self.ui.mb30 .setText("X")
        self.ui.mb20.setText("X")
        self.ui.mb50.setText("X")
    def almalajtma(self):
        self.ui.altest2.setText("X")
        self.ui.altest1.setText("X")
        self.ui.almo1.setText("X")
        self.ui.almo2.setText("X")
        self.ui.alwork2.setText("X")
        self.ui.alwork1.setText("X")
        self.ui.alsh2.setText("X")
        self.ui.alsh1.setText("X")
        self.ui.alsum1.setText("X")
        self.ui.alsum2.setText("X")
        self.ui.al30 .setText("X")
        self.ui.al20.setText("X")
        self.ui.al50.setText("X")
    def kimmm(self):
        self.ui.kitest2.setText("X")
        self.ui.kitest1.setText("X")
        self.ui.kimo1.setText("X")
        self.ui.kimo2.setText("X")
        self.ui.kiwork2.setText("X")
        self.ui.kiwork1.setText("X")
        self.ui.kish2.setText("X")
        self.ui.kish1.setText("X")
        self.ui.kisum1.setText("X")
        self.ui.kisum2.setText("X")
        self.ui.ki30 .setText("X")
        self.ui.ki20.setText("X")
        self.ui.ki50.setText("X")
    def visiaaa(self):
        self.ui.vitest2.setText("X")
        self.ui.vitest1.setText("X")
        self.ui.vimo1.setText("X")
        self.ui.vimo2.setText("X")
        self.ui.viwork2.setText("X")
        self.ui.viwork1.setText("X")
        self.ui.vish2.setText("X")
        self.ui.vish1.setText("X")
        self.ui.visum1.setText("X")
        self.ui.visum2.setText("X")
        self.ui.vi30 .setText("X")
        self.ui.vi20.setText("X")
        self.ui.vi50.setText("X")
    def ahyaaa(self):
        self.ui.ahtest2.setText("X")
        self.ui.ahtest1.setText("X")
        self.ui.ahmo1.setText("X")
        self.ui.ahmo2.setText("X")
        self.ui.ahwork2.setText("X")
        self.ui.ahwork1.setText("X")
        self.ui.ahsh2.setText("X")
        self.ui.ahsh1.setText("X")
        self.ui.ahsum1.setText("X")
        self.ui.ahsum2.setText("X")
        self.ui.ah30 .setText("X")
        self.ui.ah20.setText("X")
        self.ui.ah50.setText("X")
########################################################tab3$#####################################################################
#################################################################################################################################
#####################################################################################################################################
    def stocom3(self):
        r1=str(self.ui.t1t3comrow.currentText())
        if r1=="اولى ثانوي":
            db1=sqlite3.connect('mngschool.db')
            db1.row_factory=sqlite3.Row
            d1=db1.execute("select * from tabladdrow")
            self.ui.t1t3comnamerow.clear()
            for x in d1:
                self.ui.t1t3comnamerow.addItem("{}".format(x["namrow"]))
        if r1=="ثاني علمي":
            db1=sqlite3.connect('mngschool2a.db')
            db1.row_factory=sqlite3.Row
            d1=db1.execute("select * from tabladdrow")
            self.ui.t1t3comnamerow.clear()
            for x in d1:
                self.ui.t1t3comnamerow.addItem("{}".format(x["namrow"]))
        if r1=="ثالث علمي":
            db1=sqlite3.connect('mngschool3a.db')
            db1.row_factory=sqlite3.Row
            d1=db1.execute("select * from tabladdrow")
            self.ui.t1t3comnamerow.clear()
            for x in d1:
                self.ui.t1t3comnamerow.addItem("{}".format(x["namrow"]))
        if r1=="ثاني ادبي":
            db1=sqlite3.connect('mngschool2d.db')
            db1.row_factory=sqlite3.Row
            d1=db1.execute("select * from tabladdrow")
            self.ui.t1t3comnamerow.clear()
            for x in d1:
                self.ui.t1t3comnamerow.addItem("{}".format(x["namrow"]))
        if r1=="ثالث ادبي":
            db1=sqlite3.connect('mngschool3d.db')
            db1.row_factory=sqlite3.Row
            d1=db1.execute("select * from tabladdrow")
            self.ui.t1t3comnamerow.clear()
            for x in d1:
                self.ui.t1t3comnamerow.addItem("{}".format(x["namrow"]))

    def stostud3(self):
        r1=str(self.ui.t1t3comrow.currentText())
        r2=str(self.ui.t1t3comnamerow.currentText())
        if r1=="اولى ثانوي":
            db1=sqlite3.connect('mngschool.db')
            db1.row_factory=sqlite3.Row
            dd=db1.execute("select * from tabladdstudynt where rowst='{}'".format(r2))
            self.ui.t1t3comnamstud.clear()
            for x in dd:
                self.ui.t1t3comnamstud.addItem("{}".format(x["namst"]))
        if r1=="ثاني علمي":
            db1=sqlite3.connect('mngschool2a.db')
            db1.row_factory=sqlite3.Row
            dd=db1.execute("select * from tabladdstudynt where rowst='{}'".format(r2))
            self.ui.t1t3comnamstud.clear()
            for x in dd:
                self.ui.t1t3comnamstud.addItem("{}".format(x["namst"]))
        if r1=="ثالث علمي":
            db1=sqlite3.connect('mngschool3a.db')
            db1.row_factory=sqlite3.Row
            dd=db1.execute("select * from tabladdstudynt where rowst='{}'".format(r2))
            self.ui.t1t3comnamstud.clear()
            for x in dd:
                self.ui.t1t3comnamstud.addItem("{}".format(x["namst"]))
        if r1=="ثاني ادبي":
            db1=sqlite3.connect('mngschool2d.db')
            db1.row_factory=sqlite3.Row
            dd=db1.execute("select * from tabladdstudynt where rowst='{}'".format(r2))
            self.ui.t1t3comnamstud.clear()
            for x in dd:
                self.ui.t1t3comnamstud.addItem("{}".format(x["namst"]))
        if r1=="ثالث ادبي":
            db1=sqlite3.connect('mngschool3d.db')
            db1.row_factory=sqlite3.Row
            dd=db1.execute("select * from tabladdstudynt where rowst='{}'".format(r2))
            self.ui.t1t3comnamstud.clear()
            for x in dd:
                self.ui.t1t3comnamstud.addItem("{}".format(x["namst"]))
##############################################show1###################################################################
    def sho1(self):
        dd1=["qran","مجتمع","جغرافيا","تاريخ","ahya","arbic","aslame","qimia","readeat","visia","english"]
        dd2d=["qran","جغرافيا","تاريخ","مبادئ علم الاقتصاد","arbic","aslame","علم الاجتماع","readeat","english"]
        dd3d=["qran","جغرافيا الخرائط","تاريخ","الفلسفة والمنطق","arbic","aslame","readeat","english"]
        dd2a=["qran","ahya","arbic","aslame","qimia","readeat","visia","english"]
        v=0
        d=[]
        r1=str(self.ui.t1t3comrow.currentText())
        r2=str(self.ui.t1t3comnamerow.currentText())
        r3=str(self.ui.t1t3comnamstud.currentText())
        if r1=="اولى ثانوي":
            db1=sqlite3.connect('mngschool.db')
            db1.row_factory=sqlite3.Row
            cb=db1.cursor()
            cb.execute("select * from qran where namst='{}' and namero='{}' union all select * from mjtma where namst='{}' and namero='{}' union all select * from gjravi where namst='{}' and namero='{}' union all select * from treh where namst='{}' and namero='{}' union all select * from ahya where namst='{}' and namero='{}' union all select * from arbic where namst='{}' and namero='{}' union all select * from aslame where namst='{}' and namero='{}' union all select * from qimia where namst='{}' and namero='{}' union all select * from readeat where namst='{}' and namero='{}' union all select * from visia where namst='{}' and namero='{}' union all select * from english where namst='{}' and namero='{}'".format(r3,r2,r3,r2,r3,r2,r3,r2,r3,r2,r3,r2,r3,r2,r3,r2,r3,r2,r3,r2,r3,r2))
            ii=cb.fetchall()
            for f in ii:
                d.append(f[1])
            self.ui.textEdit1.clear()
            self.ui.textEdit1.append("<p><table width='100%' border='1' cellpadding'5' ><caption><b><u><center>جدول علامات الطالب:{}</center></u></b></caption><tr><td width=7.1%><u><center>50</u></center></td><td width=7.1%><u><center>30</center></u></td><td width=7.1%><u><center>20</u></center></td><td width=7.1%><u><center>شهري2</u></center></td><td width=7.1%><u><center>شهري1</u></center></td><td width=7.1%><u><center>تحريري2</u></center></td><td width=7.1%><u><center>شفوي2</u></center></td><td width=7.1%><u><center>واجبات2</u></center></td><td width=7.1%><u><center>مواظبة2</u></center></td><td width=7.1%><u><center>تحريري1</u></center></td><td width=7.1%><u><center>شفوي1</u></center></td><td width=7.1%><u><center>واجبات1</u></center></td><td width=7.1%><u><center>مواضبة1</u></center></td><td width=7.1%><u><center>اسم المادة</u></center></td></tr></table></p>".format(d[0]))
            for n in ii:
                #self.ui.textEdit.append('{}'.format(str(n[1])))
                self.ui.textEdit1.append("<p><table width='100%' border='1' cellpadding'5' ><tr><td width=7.1%><center>{}</center></td><td width=7.1%><center>{}</center></td><td width=7.1%><center>{}</center></td><td width=7.1%><center>{}</center></td><td width=7.1%><center>{}</center></td><td width=7.1%><center>{}</center></td><td width=7.1%><center>{}</center></td><td width=7.1%><center>{}</center></td><td width=7.1%><center>{}</center></td><td width=7.1%><center>{}</center></td><td width=7.1%><center>{}</center></td><td width=7.1%><center>{}</center></td><td width=7.1%><center>{}</center></td><td width=7.1%><center>{}</center></td></tr></table></p>".format(str(n[15]),str(n[14]),str(n[13]),str(n[12]),str(n[11]),str(n[10]),str(n[9]),str(n[8]),str(n[7]),str(n[6]),str(n[5]),str(n[4]),str(n[3]),dd1[v]))
                #self.ui.textEdit.append('{}'":"'{}'.format(dd[v],str(n[10])))
                v+=1

        if r1=="ثاني علمي":
            db1=sqlite3.connect('mngschool2a.db')
            db1.row_factory=sqlite3.Row
            cb=db1.cursor()
            cb.execute("select * from qran where namst='{}' and namero='{}' union all select * from ahya where namst='{}' and namero='{}' union all select * from arbic where namst='{}' and namero='{}' union all select * from aslame where namst='{}' and namero='{}' union all select * from qimia where namst='{}' and namero='{}' union all select * from readeat where namst='{}' and namero='{}' union all select * from visia where namst='{}' and namero='{}' union all select * from english where namst='{}' and namero='{}'".format(r3,r2,r3,r2,r3,r2,r3,r2,r3,r2,r3,r2,r3,r2,r3,r2))
            ii=cb.fetchall()
            for f in ii:
                d.append(f[1])
            self.ui.textEdit1.clear()
            self.ui.textEdit1.append("<p><table width='100%' border='1' cellpadding'5' ><caption><b><u><center>جدول علامات الطالب:{}</center></u></b></caption><tr><td width=7.1%><u><center>50</u></center></td><td width=7.1%><u><center>30</center></u></td><td width=7.1%><u><center>20</u></center></td><td width=7.1%><u><center>شهري2</u></center></td><td width=7.1%><u><center>شهري1</u></center></td><td width=7.1%><u><center>تحريري2</u></center></td><td width=7.1%><u><center>شفوي2</u></center></td><td width=7.1%><u><center>واجبات2</u></center></td><td width=7.1%><u><center>مواظبة2</u></center></td><td width=7.1%><u><center>تحريري1</u></center></td><td width=7.1%><u><center>شفوي1</u></center></td><td width=7.1%><u><center>واجبات1</u></center></td><td width=7.1%><u><center>مواضبة1</u></center></td><td width=7.1%><u><center>اسم المادة</u></center></td></tr></table></p>".format(d[0]))
            for n in ii:
                #self.ui.textEdit.append('{}'.format(str(n[1])))
                self.ui.textEdit1.append("<p><table width='100%' border='1' cellpadding'5' ><tr><td width=7.1%><center>{}</center></td><td width=7.1%><center>{}</center></td><td width=7.1%><center>{}</center></td><td width=7.1%><center>{}</center></td><td width=7.1%><center>{}</center></td><td width=7.1%><center>{}</center></td><td width=7.1%><center>{}</center></td><td width=7.1%><center>{}</center></td><td width=7.1%><center>{}</center></td><td width=7.1%><center>{}</center></td><td width=7.1%><center>{}</center></td><td width=7.1%><center>{}</center></td><td width=7.1%><center>{}</center></td><td width=7.1%><center>{}</center></td></tr></table></p>".format(str(n[15]),str(n[14]),str(n[13]),str(n[12]),str(n[11]),str(n[10]),str(n[9]),str(n[8]),str(n[7]),str(n[6]),str(n[5]),str(n[4]),str(n[3]),dd2a[v]))
                #self.ui.textEdit.append('{}'":"'{}'.format(dd[v],str(n[10])))
                v+=1

        if r1=="ثالث علمي":
            db1=sqlite3.connect('mngschool3a.db')
            db1.row_factory=sqlite3.Row
            cb=db1.cursor()
            cb.execute("select * from qran where namst='{}' and namero='{}' union all select * from ahya where namst='{}' and namero='{}' union all select * from arbic where namst='{}' and namero='{}' union all select * from aslame where namst='{}' and namero='{}' union all select * from qimia where namst='{}' and namero='{}' union all select * from readeat where namst='{}' and namero='{}' union all select * from visia where namst='{}' and namero='{}' union all select * from english where namst='{}' and namero='{}'".format(r3,r2,r3,r2,r3,r2,r3,r2,r3,r2,r3,r2,r3,r2,r3,r2))
            ii=cb.fetchall()
            for f in ii:
                d.append(f[1])
            self.ui.textEdit1.clear()
            self.ui.textEdit1.append("<p><table width='100%' border='1' cellpadding'5' ><caption><b><u><center>جدول علامات الطالب:{}</center></u></b></caption><tr><td width=7.1%><u><center>50</u></center></td><td width=7.1%><u><center>30</center></u></td><td width=7.1%><u><center>20</u></center></td><td width=7.1%><u><center>شهري2</u></center></td><td width=7.1%><u><center>شهري1</u></center></td><td width=7.1%><u><center>تحريري2</u></center></td><td width=7.1%><u><center>شفوي2</u></center></td><td width=7.1%><u><center>واجبات2</u></center></td><td width=7.1%><u><center>مواظبة2</u></center></td><td width=7.1%><u><center>تحريري1</u></center></td><td width=7.1%><u><center>شفوي1</u></center></td><td width=7.1%><u><center>واجبات1</u></center></td><td width=7.1%><u><center>مواضبة1</u></center></td><td width=7.1%><u><center>اسم المادة</u></center></td></tr></table></p>".format(d[0]))
            for n in ii:
                #self.ui.textEdit.append('{}'.format(str(n[1])))
                self.ui.textEdit1.append("<p><table width='100%' border='1' cellpadding'5' ><tr><td width=7.1%><center>{}</center></td><td width=7.1%><center>{}</center></td><td width=7.1%><center>{}</center></td><td width=7.1%><center>{}</center></td><td width=7.1%><center>{}</center></td><td width=7.1%><center>{}</center></td><td width=7.1%><center>{}</center></td><td width=7.1%><center>{}</center></td><td width=7.1%><center>{}</center></td><td width=7.1%><center>{}</center></td><td width=7.1%><center>{}</center></td><td width=7.1%><center>{}</center></td><td width=7.1%><center>{}</center></td><td width=7.1%><center>{}</center></td></tr></table></p>".format(str(n[15]),str(n[14]),str(n[13]),str(n[12]),str(n[11]),str(n[10]),str(n[9]),str(n[8]),str(n[7]),str(n[6]),str(n[5]),str(n[4]),str(n[3]),dd2a[v]))
                #self.ui.textEdit.append('{}'":"'{}'.format(dd[v],str(n[10])))
                v+=1                
        if r1=="ثاني ادبي":
            db1=sqlite3.connect('mngschool2d.db')
            db1.row_factory=sqlite3.Row
            cb=db1.cursor()#dd2d=["qran","جغرافيا","تاريخ","مبادئ علم الاقتصاد","arbic","aslame","علم الاجتماع","readeat","english"]
            cb.execute("select * from qran where namst='{}' and namero='{}' union all select * from gjravi where namst='{}' and namero='{}' union all select * from treh where namst='{}' and namero='{}' union all select * from mbada where namst='{}' and namero='{}' union all select * from arbic where namst='{}' and namero='{}' union all select * from aslame where namst='{}' and namero='{}' union all select * from almaljtma where namst='{}' and namero='{}' union all select * from readeat where namst='{}' and namero='{}' union all select * from english where namst='{}' and namero='{}'".format(r3,r2,r3,r2,r3,r2,r3,r2,r3,r2,r3,r2,r3,r2,r3,r2,r3,r2))
            ii=cb.fetchall()
            for f in ii:
                d.append(f[1])
            self.ui.textEdit1.clear()
            self.ui.textEdit1.append("<p><table width='100%' border='1' cellpadding'5' ><caption><b><u><center>جدول علامات الطالب:{}</center></u></b></caption><tr><td width=7.1%><u><center>50</u></center></td><td width=7.1%><u><center>30</center></u></td><td width=7.1%><u><center>20</u></center></td><td width=7.1%><u><center>شهري2</u></center></td><td width=7.1%><u><center>شهري1</u></center></td><td width=7.1%><u><center>تحريري2</u></center></td><td width=7.1%><u><center>شفوي2</u></center></td><td width=7.1%><u><center>واجبات2</u></center></td><td width=7.1%><u><center>مواظبة2</u></center></td><td width=7.1%><u><center>تحريري1</u></center></td><td width=7.1%><u><center>شفوي1</u></center></td><td width=7.1%><u><center>واجبات1</u></center></td><td width=7.1%><u><center>مواضبة1</u></center></td><td width=7.1%><u><center>اسم المادة</u></center></td></tr></table></p>".format(d[0]))
            for n in ii:
                #self.ui.textEdit.append('{}'.format(str(n[1])))
                self.ui.textEdit1.append("<p><table width='100%' border='1' cellpadding'5' ><tr><td width=7.1%><center>{}</center></td><td width=7.1%><center>{}</center></td><td width=7.1%><center>{}</center></td><td width=7.1%><center>{}</center></td><td width=7.1%><center>{}</center></td><td width=7.1%><center>{}</center></td><td width=7.1%><center>{}</center></td><td width=7.1%><center>{}</center></td><td width=7.1%><center>{}</center></td><td width=7.1%><center>{}</center></td><td width=7.1%><center>{}</center></td><td width=7.1%><center>{}</center></td><td width=7.1%><center>{}</center></td><td width=7.1%><center>{}</center></td></tr></table></p>".format(str(n[15]),str(n[14]),str(n[13]),str(n[12]),str(n[11]),str(n[10]),str(n[9]),str(n[8]),str(n[7]),str(n[6]),str(n[5]),str(n[4]),str(n[3]),dd2d[v]))
                #self.ui.textEdit.append('{}'":"'{}'.format(dd[v],str(n[10])))
                v+=1

        if r1=="ثالث ادبي":
            db1=sqlite3.connect('mngschool3d.db')
            db1.row_factory=sqlite3.Row
            cb=db1.cursor()#dd3d=["qran","جغرافيا الخرائط","تاريخ","الفلسفة والمنطق","arbic","aslame","readeat","english"]
            cb.execute("select * from qran where namst='{}' and namero='{}' union all select * from gjmap where namst='{}' and namero='{}' union all select * from treh where namst='{}' and namero='{}' union all select * from ffff where namst='{}' and namero='{}' union all select * from arbic where namst='{}' and namero='{}' union all select * from aslame where namst='{}' and namero='{}' union all select * from readeat where namst='{}' and namero='{}' union all select * from english where namst='{}' and namero='{}'".format(r3,r2,r3,r2,r3,r2,r3,r2,r3,r2,r3,r2,r3,r2,r3,r2))
            ii=cb.fetchall()
            for f in ii:
                d.append(f[1])
            self.ui.textEdit1.clear()
            self.ui.textEdit1.append("<p><table width='100%' border='1' cellpadding'5' ><caption><b><u><center>جدول علامات الطالب:{}</center></u></b></caption><tr><td width=7.1%><u><center>50</u></center></td><td width=7.1%><u><center>30</center></u></td><td width=7.1%><u><center>20</u></center></td><td width=7.1%><u><center>شهري2</u></center></td><td width=7.1%><u><center>شهري1</u></center></td><td width=7.1%><u><center>تحريري2</u></center></td><td width=7.1%><u><center>شفوي2</u></center></td><td width=7.1%><u><center>واجبات2</u></center></td><td width=7.1%><u><center>مواظبة2</u></center></td><td width=7.1%><u><center>تحريري1</u></center></td><td width=7.1%><u><center>شفوي1</u></center></td><td width=7.1%><u><center>واجبات1</u></center></td><td width=7.1%><u><center>مواضبة1</u></center></td><td width=7.1%><u><center>اسم المادة</u></center></td></tr></table></p>".format(d[0]))
            for n in ii:
                #self.ui.textEdit.append('{}'.format(str(n[1])))
                self.ui.textEdit1.append("<p><table width='100%' border='1' cellpadding'5' ><tr><td width=7.1%><center>{}</center></td><td width=7.1%><center>{}</center></td><td width=7.1%><center>{}</center></td><td width=7.1%><center>{}</center></td><td width=7.1%><center>{}</center></td><td width=7.1%><center>{}</center></td><td width=7.1%><center>{}</center></td><td width=7.1%><center>{}</center></td><td width=7.1%><center>{}</center></td><td width=7.1%><center>{}</center></td><td width=7.1%><center>{}</center></td><td width=7.1%><center>{}</center></td><td width=7.1%><center>{}</center></td><td width=7.1%><center>{}</center></td></tr></table></p>".format(str(n[15]),str(n[14]),str(n[13]),str(n[12]),str(n[11]),str(n[10]),str(n[9]),str(n[8]),str(n[7]),str(n[6]),str(n[5]),str(n[4]),str(n[3]),dd3d[v]))
                #self.ui.textEdit.append('{}'":"'{}'.format(dd[v],str(n[10])))
                v+=1

###############################################tab4########################################################################
################################################################################################################################
    def stocom4(self):
        r1=str(self.ui.t1t4comrow.currentText())
        if r1=="اولى ثانوي":
            db1=sqlite3.connect('mngschool.db')
            db1.row_factory=sqlite3.Row
            d1=db1.execute("select * from tabladdrow")
            self.ui.t1t4comnamerow.clear()
            for x in d1:
                self.ui.t1t4comnamerow.addItem("{}".format(x["namrow"]))
        if r1=="ثاني علمي":
            db1=sqlite3.connect('mngschool2a.db')
            db1.row_factory=sqlite3.Row
            d1=db1.execute("select * from tabladdrow")
            self.ui.t1t4comnamerow.clear()
            for x in d1:
                self.ui.t1t4comnamerow.addItem("{}".format(x["namrow"]))
        if r1=="ثالث علمي":
            db1=sqlite3.connect('mngschool3a.db')
            db1.row_factory=sqlite3.Row
            d1=db1.execute("select * from tabladdrow")
            self.ui.t1t4comnamerow.clear()
            for x in d1:
                self.ui.t1t4comnamerow.addItem("{}".format(x["namrow"]))
        if r1=="ثاني ادبي":
            db1=sqlite3.connect('mngschool2d.db')
            db1.row_factory=sqlite3.Row
            d1=db1.execute("select * from tabladdrow")
            self.ui.t1t4comnamerow.clear()
            for x in d1:
                self.ui.t1t4comnamerow.addItem("{}".format(x["namrow"]))
        if r1=="ثالث ادبي":
            db1=sqlite3.connect('mngschool3d.db')
            db1.row_factory=sqlite3.Row
            d1=db1.execute("select * from tabladdrow")
            self.ui.t1t4comnamerow.clear()
            for x in d1:
                self.ui.t1t4comnamerow.addItem("{}".format(x["namrow"]))

    def stoobject(self):
        dd1=["qran","aslame","arbic","readeat","english","ahya","qimia","visia","mjtma","treh","gjravi"]
        dd2d=["qran","aslame","arbic","readeat","english","almaljtma","mbada","treh","gjravi"]
        dd3d=["qran","aslame","arbic","readeat","english","ffff","treh","gjmap"]
        dd2a=["qran","aslame","arbic","readeat","english","ahya","qimia","visia"]
        r1=str(self.ui.t1t4comrow.currentText())
        if r1=="اولى ثانوي":
            self.ui.t1t4comnameobject.clear()
            for x in dd1:
                self.ui.t1t4comnameobject.addItem("{}".format(x))
        
        if r1=="ثاني علمي":
            self.ui.t1t4comnameobject.clear()
            for x in dd2a:
                self.ui.t1t4comnameobject.addItem("{}".format(x))
        if r1=="ثالث علمي":
            self.ui.t1t4comnameobject.clear()
            for x in dd2a:
                self.ui.t1t4comnameobject.addItem("{}".format(x))
        if r1=="ثاني ادبي":
            self.ui.t1t4comnameobject.clear()
            for x in dd2d:
                self.ui.t1t4comnameobject.addItem("{}".format(x))
        if r1=="ثالث ادبي":
            self.ui.t1t4comnameobject.clear()
            for x in dd3d:
                self.ui.t1t4comnameobject.addItem("{}".format(x))

    def shoobject(self):
        r1=str(self.ui.t1t4comrow.currentText())
        r2=str(self.ui.t1t4comnamerow.currentText())
        r3=str(self.ui.t1t4comnameobject.currentText())
        if r1=="اولى ثانوي":
            db1=sqlite3.connect('mngschool.db')
            #db1.row_factory=sqlite3.Row
            cb=db1.cursor()
            cb.execute("select * from '{}' where namero='{}'".format(r3,r2))
            ii=cb.fetchall()
            self.ui.textEdit2.clear()
            for f in ii:
                self.ui.textEdit2.append("<p><table width='100%' border='1' cellpadding'5' ><caption><b><u><center>جدول علامات طلاب الصف:{}-المادة:{}</center></u></b></caption><tr><td width=7.1%><u><center>50</u></center></td><td width=7.1%><u><center>30</center></u></td><td width=7.1%><u><center>20</u></center></td><td width=7.1%><u><center>شهري2</u></center></td><td width=7.1%><u><center>شهري1</u></center></td><td width=7.1%><u><center>تحريري2</u></center></td><td width=7.1%><u><center>شفوي2</u></center></td><td width=7.1%><u><center>واجبات2</u></center></td><td width=7.1%><u><center>مواظبة2</u></center></td><td width=7.1%><u><center>تحريري1</u></center></td><td width=7.1%><u><center>شفوي1</u></center></td><td width=7.1%><u><center>واجبات1</u></center></td><td width=7.1%><u><center>مواضبة1</u></center></td><td width=7.1%><u><center>اسم الطالب</u></center></td></tr></table></p>".format(str(f[2]),r3))
                break
            for n in ii:
                self.ui.textEdit2.append("<p><table width='100%' border='1' cellpadding'5' ><tr><td width=7.1%><center>{}</center></td><td width=7.1%><center>{}</center></td><td width=7.1%><center>{}</center></td><td width=7.1%><center>{}</center></td><td width=7.1%><center>{}</center></td><td width=7.1%><center>{}</center></td><td width=7.1%><center>{}</center></td><td width=7.1%><center>{}</center></td><td width=7.1%><center>{}</center></td><td width=7.1%><center>{}</center></td><td width=7.1%><center>{}</center></td><td width=7.1%><center>{}</center></td><td width=7.1%><center>{}</center></td><td width=7.1%><center>{}</center></td></tr></table></p>".format(str(n[15]),str(n[14]),str(n[13]),str(n[12]),str(n[11]),str(n[10]),str(n[9]),str(n[8]),str(n[7]),str(n[6]),str(n[5]),str(n[4]),str(n[3]),str(n[1])))
        if r1=="ثاني علمي":
            db1=sqlite3.connect('mngschool2a.db')
            #db1.row_factory=sqlite3.Row
            cb=db1.cursor()
            cb.execute("select * from '{}' where namero='{}'".format(r3,r2))
            ii=cb.fetchall()
            self.ui.textEdit2.clear()
            for f in ii:
                self.ui.textEdit2.append("<p><table width='100%' border='1' cellpadding'5' ><caption><b><u><center>جدول علامات طلاب الصف:{}-المادة:{}</center></u></b></caption><tr><td width=7.1%><u><center>50</u></center></td><td width=7.1%><u><center>30</center></u></td><td width=7.1%><u><center>20</u></center></td><td width=7.1%><u><center>شهري2</u></center></td><td width=7.1%><u><center>شهري1</u></center></td><td width=7.1%><u><center>تحريري2</u></center></td><td width=7.1%><u><center>شفوي2</u></center></td><td width=7.1%><u><center>واجبات2</u></center></td><td width=7.1%><u><center>مواظبة2</u></center></td><td width=7.1%><u><center>تحريري1</u></center></td><td width=7.1%><u><center>شفوي1</u></center></td><td width=7.1%><u><center>واجبات1</u></center></td><td width=7.1%><u><center>مواضبة1</u></center></td><td width=7.1%><u><center>اسم الطالب</u></center></td></tr></table></p>".format(str(f[2]),r3))
                break
            for n in ii:
                self.ui.textEdit2.append("<p><table width='100%' border='1' cellpadding'5' ><tr><td width=7.1%><center>{}</center></td><td width=7.1%><center>{}</center></td><td width=7.1%><center>{}</center></td><td width=7.1%><center>{}</center></td><td width=7.1%><center>{}</center></td><td width=7.1%><center>{}</center></td><td width=7.1%><center>{}</center></td><td width=7.1%><center>{}</center></td><td width=7.1%><center>{}</center></td><td width=7.1%><center>{}</center></td><td width=7.1%><center>{}</center></td><td width=7.1%><center>{}</center></td><td width=7.1%><center>{}</center></td><td width=7.1%><center>{}</center></td></tr></table></p>".format(str(n[15]),str(n[14]),str(n[13]),str(n[12]),str(n[11]),str(n[10]),str(n[9]),str(n[8]),str(n[7]),str(n[6]),str(n[5]),str(n[4]),str(n[3]),str(n[1])))
        
        if r1=="ثالث علمي":
            db1=sqlite3.connect('mngschool3a.db')
            #db1.row_factory=sqlite3.Row
            cb=db1.cursor()
            cb.execute("select * from '{}' where namero='{}'".format(r3,r2))
            ii=cb.fetchall()
            self.ui.textEdit2.clear()
            for f in ii:
                self.ui.textEdit2.append("<p><table width='100%' border='1' cellpadding'5' ><caption><b><u><center>جدول علامات طلاب الصف:{}-المادة:{}</center></u></b></caption><tr><td width=7.1%><u><center>50</u></center></td><td width=7.1%><u><center>30</center></u></td><td width=7.1%><u><center>20</u></center></td><td width=7.1%><u><center>شهري2</u></center></td><td width=7.1%><u><center>شهري1</u></center></td><td width=7.1%><u><center>تحريري2</u></center></td><td width=7.1%><u><center>شفوي2</u></center></td><td width=7.1%><u><center>واجبات2</u></center></td><td width=7.1%><u><center>مواظبة2</u></center></td><td width=7.1%><u><center>تحريري1</u></center></td><td width=7.1%><u><center>شفوي1</u></center></td><td width=7.1%><u><center>واجبات1</u></center></td><td width=7.1%><u><center>مواضبة1</u></center></td><td width=7.1%><u><center>اسم الطالب</u></center></td></tr></table></p>".format(str(f[2]),r3))
                break
            for n in ii:
                self.ui.textEdit2.append("<p><table width='100%' border='1' cellpadding'5' ><tr><td width=7.1%><center>{}</center></td><td width=7.1%><center>{}</center></td><td width=7.1%><center>{}</center></td><td width=7.1%><center>{}</center></td><td width=7.1%><center>{}</center></td><td width=7.1%><center>{}</center></td><td width=7.1%><center>{}</center></td><td width=7.1%><center>{}</center></td><td width=7.1%><center>{}</center></td><td width=7.1%><center>{}</center></td><td width=7.1%><center>{}</center></td><td width=7.1%><center>{}</center></td><td width=7.1%><center>{}</center></td><td width=7.1%><center>{}</center></td></tr></table></p>".format(str(n[15]),str(n[14]),str(n[13]),str(n[12]),str(n[11]),str(n[10]),str(n[9]),str(n[8]),str(n[7]),str(n[6]),str(n[5]),str(n[4]),str(n[3]),str(n[1])))

        if r1=="ثاني ادبي":
            db1=sqlite3.connect('mngschool2d.db')
            #db1.row_factory=sqlite3.Row
            cb=db1.cursor()
            cb.execute("select * from '{}' where namero='{}'".format(r3,r2))
            ii=cb.fetchall()
            self.ui.textEdit2.clear()
            for f in ii:
                self.ui.textEdit2.append("<p><table width='100%' border='1' cellpadding'5' ><caption><b><u><center>جدول علامات طلاب الصف:{}-المادة:{}</center></u></b></caption><tr><td width=7.1%><u><center>50</u></center></td><td width=7.1%><u><center>30</center></u></td><td width=7.1%><u><center>20</u></center></td><td width=7.1%><u><center>شهري2</u></center></td><td width=7.1%><u><center>شهري1</u></center></td><td width=7.1%><u><center>تحريري2</u></center></td><td width=7.1%><u><center>شفوي2</u></center></td><td width=7.1%><u><center>واجبات2</u></center></td><td width=7.1%><u><center>مواظبة2</u></center></td><td width=7.1%><u><center>تحريري1</u></center></td><td width=7.1%><u><center>شفوي1</u></center></td><td width=7.1%><u><center>واجبات1</u></center></td><td width=7.1%><u><center>مواضبة1</u></center></td><td width=7.1%><u><center>اسم الطالب</u></center></td></tr></table></p>".format(str(f[2]),r3))
                break
            for n in ii:
                self.ui.textEdit2.append("<p><table width='100%' border='1' cellpadding'5' ><tr><td width=7.1%><center>{}</center></td><td width=7.1%><center>{}</center></td><td width=7.1%><center>{}</center></td><td width=7.1%><center>{}</center></td><td width=7.1%><center>{}</center></td><td width=7.1%><center>{}</center></td><td width=7.1%><center>{}</center></td><td width=7.1%><center>{}</center></td><td width=7.1%><center>{}</center></td><td width=7.1%><center>{}</center></td><td width=7.1%><center>{}</center></td><td width=7.1%><center>{}</center></td><td width=7.1%><center>{}</center></td><td width=7.1%><center>{}</center></td></tr></table></p>".format(str(n[15]),str(n[14]),str(n[13]),str(n[12]),str(n[11]),str(n[10]),str(n[9]),str(n[8]),str(n[7]),str(n[6]),str(n[5]),str(n[4]),str(n[3]),str(n[1])))

        if r1=="ثالث ادبي":
            db1=sqlite3.connect('mngschool3d.db')
            #db1.row_factory=sqlite3.Row
            cb=db1.cursor()
            cb.execute("select * from '{}' where namero='{}'".format(r3,r2))
            ii=cb.fetchall()
            self.ui.textEdit2.clear()
            for f in ii:
                self.ui.textEdit2.append("<p><table width='100%' border='1' cellpadding'5' ><caption><b><u><center>جدول علامات طلاب الصف:{}-المادة:{}</center></u></b></caption><tr><td width=7.1%><u><center>50</u></center></td><td width=7.1%><u><center>30</center></u></td><td width=7.1%><u><center>20</u></center></td><td width=7.1%><u><center>شهري2</u></center></td><td width=7.1%><u><center>شهري1</u></center></td><td width=7.1%><u><center>تحريري2</u></center></td><td width=7.1%><u><center>شفوي2</u></center></td><td width=7.1%><u><center>واجبات2</u></center></td><td width=7.1%><u><center>مواظبة2</u></center></td><td width=7.1%><u><center>تحريري1</u></center></td><td width=7.1%><u><center>شفوي1</u></center></td><td width=7.1%><u><center>واجبات1</u></center></td><td width=7.1%><u><center>مواضبة1</u></center></td><td width=7.1%><u><center>اسم الطالب</u></center></td></tr></table></p>".format(str(f[2]),r3))
                break
            for n in ii:
                self.ui.textEdit2.append("<p><table width='100%' border='1' cellpadding'5' ><tr><td width=7.1%><center>{}</center></td><td width=7.1%><center>{}</center></td><td width=7.1%><center>{}</center></td><td width=7.1%><center>{}</center></td><td width=7.1%><center>{}</center></td><td width=7.1%><center>{}</center></td><td width=7.1%><center>{}</center></td><td width=7.1%><center>{}</center></td><td width=7.1%><center>{}</center></td><td width=7.1%><center>{}</center></td><td width=7.1%><center>{}</center></td><td width=7.1%><center>{}</center></td><td width=7.1%><center>{}</center></td><td width=7.1%><center>{}</center></td></tr></table></p>".format(str(n[15]),str(n[14]),str(n[13]),str(n[12]),str(n[11]),str(n[10]),str(n[9]),str(n[8]),str(n[7]),str(n[6]),str(n[5]),str(n[4]),str(n[3]),str(n[1])))
#the delete stydant:
    def destud(self):
        namrow=str(self.ui.t1t2comrow.currentText())
        narow=str(self.ui.t1t2comnamerow.currentText())
        namstud=str(self.ui.t1t2comnamstud.currentText())
        if namrow=="اولى ثانوي": 
            db1=sqlite3.connect('mngschool.db')
            db1.row_factory=sqlite3.Row
            #db1.execute("delete from posts where title='{}'".format(titlee))
            db1.execute("delete from tabladdstudynt where namst='{}' and rowst='{}'".format(namstud,narow))
            db1.commit()
            db1.execute("delete from ahya where namst='{}' and namero='{}'".format(namstud,narow))
            db1.commit()
            db1.execute("delete from arbic where namst='{}' and namero='{}'".format(namstud,narow))
            db1.commit()
            db1.execute("delete from aslame where namst='{}' and namero='{}'".format(namstud,narow))
            db1.commit()
            db1.execute("delete from english where namst='{}' and namero='{}'".format(namstud,narow))
            db1.commit()
            db1.execute("delete from gjravi where namst='{}' and namero='{}'".format(namstud,narow))
            db1.commit()
            db1.execute("delete from mjtma where namst='{}' and namero='{}'".format(namstud,narow))
            db1.commit()
            db1.execute("delete from qimia where namst='{}' and namero='{}'".format(namstud,narow))
            db1.commit()
            db1.execute("delete from qran where namst='{}' and namero='{}'".format(namstud,narow))
            db1.commit()
            db1.execute("delete from readeat where namst='{}' and namero='{}'".format(namstud,narow))
            db1.commit()
            db1.execute("delete from treh where namst='{}' and namero='{}'".format(namstud,narow))
            db1.commit()
            db1.execute("delete from visia where namst='{}' and namero='{}'".format(namstud,narow))
            db1.commit()
            message=QtWidgets.QMessageBox.information(self,'information','<FONT size=10 color=blue>تم حذف الطالب بنجاح</FONT>')
        if namrow=="ثانية علمي": 
            db1=sqlite3.connect('mngschool2a.db')
            db1.row_factory=sqlite3.Row
            #db1.execute("delete from posts where title='{}'".format(titlee))
            db1.execute("delete from tabladdstudynt where namst='{}' and rowst='{}'".format(namstud,narow))
            db1.commit()
            db1.execute("delete from ahya where namst='{}' and namero='{}'".format(namstud,narow))
            db1.commit()
            db1.execute("delete from arbic where namst='{}' and namero='{}'".format(namstud,narow))
            db1.commit()
            db1.execute("delete from aslame where namst='{}' and namero='{}'".format(namstud,narow))
            db1.commit()
            db1.execute("delete from english where namst='{}' and namero='{}'".format(namstud,narow))
            db1.commit()
            db1.execute("delete from qimia where namst='{}' and namero='{}'".format(namstud,narow))
            db1.commit()
            db1.execute("delete from qran where namst='{}' and namero='{}'".format(namstud,narow))
            db1.commit()
            db1.execute("delete from readeat where namst='{}' and namero='{}'".format(namstud,narow))
            db1.commit()
            db1.execute("delete from visia where namst='{}' and namero='{}'".format(namstud,narow))
            db1.commit()
            message=QtWidgets.QMessageBox.information(self,'information','<FONT size=10 color=blue>تم حذف الطالب بنجاح</FONT>')
        if namrow=="ثالثة علمي": 
            db1=sqlite3.connect('mngschool3a.db')
            db1.row_factory=sqlite3.Row
            #db1.execute("delete from posts where title='{}'".format(titlee))
            db1.execute("delete from tabladdstudynt where namst='{}' and rowst='{}'".format(namstud,narow))
            db1.commit()
            db1.execute("delete from ahya where namst='{}' and namero='{}'".format(namstud,narow))
            db1.commit()
            db1.execute("delete from arbic where namst='{}' and namero='{}'".format(namstud,narow))
            db1.commit()
            db1.execute("delete from aslame where namst='{}' and namero='{}'".format(namstud,narow))
            db1.commit()
            db1.execute("delete from english where namst='{}' and namero='{}'".format(namstud,narow))
            db1.commit()
            db1.execute("delete from qimia where namst='{}' and namero='{}'".format(namstud,narow))
            db1.commit()
            db1.execute("delete from qran where namst='{}' and namero='{}'".format(namstud,narow))
            db1.commit()
            db1.execute("delete from readeat where namst='{}' and namero='{}'".format(namstud,narow))
            db1.commit()
            db1.execute("delete from visia where namst='{}' and namero='{}'".format(namstud,narow))
            db1.commit()
            message=QtWidgets.QMessageBox.information(self,'information','<FONT size=10 color=blue>تم حذف الطالب بنجاح</FONT>')
        if namrow=="ثانية ادبي": 
            db1=sqlite3.connect('mngschool2d.db')
            db1.row_factory=sqlite3.Row
            #db1.execute("delete from posts where title='{}'".format(titlee))
            db1.execute("delete from tabladdstudynt where namst='{}' and rowst='{}'".format(namstud,narow))
            db1.commit()
            db1.execute("delete from arbic where namst='{}' and namero='{}'".format(namstud,narow))
            db1.commit()
            db1.execute("delete from aslame where namst='{}' and namero='{}'".format(namstud,narow))
            db1.commit()
            db1.execute("delete from english where namst='{}' and namero='{}'".format(namstud,narow))
            db1.commit()
            db1.execute("delete from gjravi where namst='{}' and namero='{}'".format(namstud,narow))
            db1.commit()
            db1.execute("delete from qran where namst='{}' and namero='{}'".format(namstud,narow))
            db1.commit()
            db1.execute("delete from readeat where namst='{}' and namero='{}'".format(namstud,narow))
            db1.commit()
            db1.execute("delete from treh where namst='{}' and namero='{}'".format(namstud,narow))
            db1.commit()
            db1.execute("delete from almaljtma where namst='{}' and namero='{}'".format(namstud,narow))
            db1.commit()
            db1.execute("delete from mbada where namst='{}' and namero='{}'".format(namstud,narow))
            db1.commit()
            message=QtWidgets.QMessageBox.information(self,'information','<FONT size=10 color=blue>تم حذف الطالب بنجاح</FONT>')
        if namrow=="ثالثة ادبي": 
            db1=sqlite3.connect('mngschool3d.db')
            db1.row_factory=sqlite3.Row
            #db1.execute("delete from posts where title='{}'".format(titlee))
            db1.execute("delete from tabladdstudynt where namst='{}' and rowst='{}'".format(namstud,narow))
            db1.commit()
            db1.execute("delete from arbic where namst='{}' and namero='{}'".format(namstud,narow))
            db1.commit()
            db1.execute("delete from aslame where namst='{}' and namero='{}'".format(namstud,narow))
            db1.commit()
            db1.execute("delete from english where namst='{}' and namero='{}'".format(namstud,narow))
            db1.commit()
            db1.execute("delete from gjmap where namst='{}' and namero='{}'".format(namstud,narow))
            db1.commit()
            db1.execute("delete from qran where namst='{}' and namero='{}'".format(namstud,narow))
            db1.commit()
            db1.execute("delete from readeat where namst='{}' and namero='{}'".format(namstud,narow))
            db1.commit()
            db1.execute("delete from treh where namst='{}' and namero='{}'".format(namstud,narow))
            db1.commit()
            db1.execute("delete from ffff where namst='{}' and namero='{}'".format(namstud,narow))
            db1.commit()
            message=QtWidgets.QMessageBox.information(self,'information','<FONT size=10 color=blue>تم حذف الطالب بنجاح</FONT>')
    def alh(self):
    	import best
    def cret(self):
    	#message=QtWidgets.QMessageBox.information(self,'information','<FONT size=10 color=blue>تم حذف الطالب بنجاح</FONT>')
    	#import cretfile
    	salm=NotePad3()
    	salm.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    myapp = NotePad()
myapp.show()
sys.exit(app.exec_())

