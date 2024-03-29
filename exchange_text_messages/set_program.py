# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'set_program.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(664, 537)
        MainWindow.setDockNestingEnabled(False)
        MainWindow.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 235, 235, 206), stop:0.35 rgba(255, 188, 188, 80), stop:0.4 rgba(255, 162, 162, 80), stop:0.425 rgba(255, 132, 132, 156), stop:0.44 rgba(252, 128, 128, 80), stop:1 rgba(255, 255, 255, 0));")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setMovable(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame = QtWidgets.QFrame(self.tab)
        self.frame.setStyleSheet("background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(214, 255, 170, 255), stop:1 rgba(255, 255, 255, 255));")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.splitter = QtWidgets.QSplitter(self.frame)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.label = QtWidgets.QLabel(self.splitter)
        self.label.setStyleSheet("font: 75 18pt \"Noto Sans\";")
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(self.splitter)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.widget = QtWidgets.QWidget(self.splitter)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.en_user_old = QtWidgets.QLineEdit(self.widget)
        self.en_user_old.setObjectName("en_user_old")
        self.horizontalLayout.addWidget(self.en_user_old)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.widget1 = QtWidgets.QWidget(self.splitter)
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.en_user_new = QtWidgets.QLineEdit(self.widget1)
        self.en_user_new.setObjectName("en_user_new")
        self.horizontalLayout_2.addWidget(self.en_user_new)
        self.label_3 = QtWidgets.QLabel(self.widget1)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.but_chang_user = QtWidgets.QPushButton(self.splitter)
        self.but_chang_user.setObjectName("but_chang_user")
        self.gridLayout_4.addWidget(self.splitter, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)
        self.frame_2 = QtWidgets.QFrame(self.tab)
        self.frame_2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(40, 154, 244, 255), stop:1 rgba(255, 255, 255, 255));")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.splitter_2 = QtWidgets.QSplitter(self.frame_2)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.label_4 = QtWidgets.QLabel(self.splitter_2)
        self.label_4.setStyleSheet("font: 75 18pt \"Noto Sans\";")
        self.label_4.setObjectName("label_4")
        self.line_2 = QtWidgets.QFrame(self.splitter_2)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.widget2 = QtWidgets.QWidget(self.splitter_2)
        self.widget2.setObjectName("widget2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.en_pass_old = QtWidgets.QLineEdit(self.widget2)
        self.en_pass_old.setObjectName("en_pass_old")
        self.horizontalLayout_3.addWidget(self.en_pass_old)
        self.label_6 = QtWidgets.QLabel(self.widget2)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.label_6)
        self.widget3 = QtWidgets.QWidget(self.splitter_2)
        self.widget3.setObjectName("widget3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget3)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.en_pass_new = QtWidgets.QLineEdit(self.widget3)
        self.en_pass_new.setObjectName("en_pass_new")
        self.horizontalLayout_4.addWidget(self.en_pass_new)
        self.label_5 = QtWidgets.QLabel(self.widget3)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.but_chang_pass = QtWidgets.QPushButton(self.splitter_2)
        self.but_chang_pass.setObjectName("but_chang_pass")
        self.gridLayout_3.addWidget(self.splitter_2, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame_2, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.frame_3 = QtWidgets.QFrame(self.tab_2)
        self.frame_3.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(0, 0, 0, 0), stop:0.52 rgba(0, 0, 0, 0), stop:0.565 rgba(82, 121, 76, 33), stop:0.65 rgba(159, 235, 148, 64), stop:0.721925 rgba(255, 238, 150, 129), stop:0.77 rgba(255, 128, 128, 204), stop:0.89 rgba(191, 128, 255, 64), stop:1 rgba(0, 0, 0, 0));")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.splitter_3 = QtWidgets.QSplitter(self.frame_3)
        self.splitter_3.setOrientation(QtCore.Qt.Vertical)
        self.splitter_3.setObjectName("splitter_3")
        self.widget4 = QtWidgets.QWidget(self.splitter_3)
        self.widget4.setObjectName("widget4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget4)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.radio_nourmal = QtWidgets.QRadioButton(self.widget4)
        self.radio_nourmal.setChecked(True)
        self.radio_nourmal.setIcon(QIcon("nourml1.png"))
        self.radio_nourmal.setObjectName("radio_nourmal")
        self.horizontalLayout_5.addWidget(self.radio_nourmal)
        self.radio_dark = QtWidgets.QRadioButton(self.widget4)
        self.radio_dark.setIcon(QIcon("night.png"))
        self.radio_dark.setObjectName("radio_dark")
        self.horizontalLayout_5.addWidget(self.radio_dark)
        self.gridLayout_5.addWidget(self.splitter_3, 0, 0, 1, 1)
        self.gridLayout_7.addWidget(self.frame_3, 0, 0, 1, 1)
        self.frame_4 = QtWidgets.QFrame(self.tab_2)
        self.frame_4.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(245, 224, 176, 255), stop:0.09 rgba(246, 189, 237, 255), stop:0.14 rgba(194, 207, 246, 255), stop:0.19 rgba(184, 160, 168, 255), stop:0.25 rgba(171, 186, 248, 255), stop:0.32 rgba(243, 248, 224, 255), stop:0.385 rgba(249, 162, 183, 255), stop:0.47 rgba(100, 115, 124, 255), stop:0.58 rgba(251, 205, 202, 255), stop:0.65 rgba(170, 128, 185, 255), stop:0.75 rgba(252, 222, 204, 255), stop:0.805 rgba(206, 122, 218, 255), stop:0.86 rgba(254, 223, 175, 255), stop:0.91 rgba(254, 236, 244, 255), stop:1 rgba(255, 191, 221, 255));")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.splitter_4 = QtWidgets.QSplitter(self.frame_4)
        self.splitter_4.setOrientation(QtCore.Qt.Vertical)
        self.splitter_4.setObjectName("splitter_4")
        self.widget5 = QtWidgets.QWidget(self.splitter_4)
        self.widget5.setObjectName("widget5")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.widget5)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.spin_drdsh = QtWidgets.QSpinBox(self.widget5)
        self.spin_drdsh.setAccelerated(False)
        self.spin_drdsh.setMinimum(10)
        self.spin_drdsh.setObjectName("spin_drdsh")
        self.horizontalLayout_7.addWidget(self.spin_drdsh)
        self.label_9 = QtWidgets.QLabel(self.widget5)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_7.addWidget(self.label_9)
        self.widget6 = QtWidgets.QWidget(self.splitter_4)
        self.widget6.setObjectName("widget6")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.widget6)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.spin_list = QtWidgets.QSpinBox(self.widget6)
        self.spin_list.setAccelerated(False)
        self.spin_list.setMinimum(10)
        self.spin_list.setObjectName("spin_list")
        self.horizontalLayout_8.addWidget(self.spin_list)
        self.label_10 = QtWidgets.QLabel(self.widget6)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_8.addWidget(self.label_10)
        self.widget7 = QtWidgets.QWidget(self.splitter_4)
        self.widget7.setObjectName("widget7")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.widget7)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.spin_text_search = QtWidgets.QSpinBox(self.widget7)
        self.spin_text_search.setAccelerated(False)
        self.spin_text_search.setMinimum(10)
        self.spin_text_search.setObjectName("spin_text_search")
        self.horizontalLayout_9.addWidget(self.spin_text_search)
        self.label_11 = QtWidgets.QLabel(self.widget7)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_9.addWidget(self.label_11)
        self.but_save_all = QtWidgets.QPushButton(self.splitter_4)
        self.but_save_all.setObjectName("but_save_all")
        self.gridLayout_6.addWidget(self.splitter_4, 0, 0, 1, 1)
        self.gridLayout_7.addWidget(self.frame_4, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 664, 27))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "الضبط"))
        self.label.setText(_translate("MainWindow", "تغير اسم المستخدم"))
        self.label_2.setText(_translate("MainWindow", "اسم المستخدم القديم:"))
        self.label_3.setText(_translate("MainWindow", "اسم المستخدم الجديد:"))
        self.but_chang_user.setText(_translate("MainWindow", "تغيير اسم المستخدم"))
        self.label_4.setText(_translate("MainWindow", "تغير كلمة المرور"))
        self.label_6.setText(_translate("MainWindow", "كلمة المرورالقديم:"))
        self.label_5.setText(_translate("MainWindow", "كلمة المرور الجديد:"))
        self.but_chang_pass.setText(_translate("MainWindow", "تغيير كلمة المرور"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "الحساب"))
        self.radio_nourmal.setText(_translate("MainWindow", "الوضع الطبيعي"))
        self.radio_dark.setText(_translate("MainWindow", "الوضع اليلي"))
        self.label_9.setText(_translate("MainWindow", "حجم خط المحادثة:"))
        self.label_10.setText(_translate("MainWindow", "حجم خط قوائم العرض:"))
        self.label_11.setText(_translate("MainWindow", "حجم خط نص البحث:"))
        self.but_save_all.setText(_translate("MainWindow", "حفظ التغيرات"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "عام"))
class NotePad1(QtWidgets.QMainWindow):
	def __init__(self, parent=None):
		QtWidgets.QWidget.__init__(self, parent)#lambda:تضعها عند اسم الزر
		self.ui1 = Ui_MainWindow()
		self.ui1.setupUi(self)
		
		
#if __name__ == "__main__":
	#import sys
	#app1 = QtWidgets.QApplication(sys.argv)
	#myapp = NotePad()
	
	#st="""QPushButton{border-radius:10px;border:2px solid white;background-color:rgb(84, 158, 255);}
	#QPushButton:hover{background-color:green;border:2px solid red;}
	#QLineEdit{background-color:white;border-radius:5px;}
	#QLineEdit:hover{background-color:green;color:white;border:2px solid red;}
	#QComboBox:hover{background-color:green;color:white;border:2px solid red;}
	#QComboBox{border-radius:5px;}
	#QListWidget:hover{background-color:#EADBBC;color:white;border:2px solid red;}
	#QTextEdit{background-color:#EADBBC;text-align:center;}
	
	#QLabel{border-radius:5px;border:2px solid white;}
	#QMenu{border-radius:5px;border:2px solid white;}
	#QMenuBar{border-radius:5px;border:2px solid white;}
	#QMenuBar:hover{border-radius:5px;border:2px ridge red;background-color:#65CF5B;}"""
	#app.setStyleSheet(st)
	#myapp.show()

