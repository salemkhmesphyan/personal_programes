# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'com1.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!
"""
programmer by en:salem khmes phyan
"""
from PyQt5 import QtCore, QtGui, QtWidgets, QtPrintSupport
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sqlite3
import datetime
from datetime import date
import time
t=time.asctime(time.localtime(time.time()))
x=datetime.datetime.now().hour
s=datetime.datetime.now().minute
a=datetime.datetime.now().second
m=str(x)+":"+str(s)
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(796, 605)
        #MainWindow.setStyleSheet("background-color: qlineargradient(spread:reflect, x1:0.941, y1:0.165, x2:0.945, y2:0.17, stop:1 rgba(244, 141, 102, 255));")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("font: 12pt \"Sahadeva\";\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.page)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.page)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.ent1name = QtWidgets.QLineEdit(self.page)
        self.ent1name.setObjectName("ent1name")
        self.horizontalLayout.addWidget(self.ent1name)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.page)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.ent1time = QtWidgets.QLineEdit(self.page)
        self.ent1time.setObjectName("ent1time")
        self.horizontalLayout_2.addWidget(self.ent1time)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.page)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.ent1date = QtWidgets.QLineEdit(self.page)
        self.ent1date.setFrame(True)
        self.ent1date.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.ent1date.setAlignment(QtCore.Qt.AlignCenter)
        self.ent1date.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.ent1date.setObjectName("ent1date")
        self.horizontalLayout_3.addWidget(self.ent1date)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.page)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.ent1reson = QtWidgets.QLineEdit(self.page)
        self.ent1reson.setObjectName("ent1reson")
        self.horizontalLayout_4.addWidget(self.ent1reson)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.page)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.ent1remark = QtWidgets.QLineEdit(self.page)
        self.ent1remark.setObjectName("ent1remark")
        self.horizontalLayout_5.addWidget(self.ent1remark)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_6 = QtWidgets.QLabel(self.page)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.label_6)
        self.ent1job = QtWidgets.QTextEdit(self.page)
        self.ent1job.setStyleSheet("background-color:white;")
        self.ent1job.setFrameShape(QtWidgets.QFrame.Box)
        self.ent1job.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ent1job.setLineWidth(1)
        self.ent1job.setMidLineWidth(0)
        self.ent1job.setLineWrapMode(QtWidgets.QTextEdit.WidgetWidth)
        self.ent1job.setOverwriteMode(False)
        self.ent1job.setTabStopWidth(80)
        self.ent1job.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextEditable|QtCore.Qt.TextEditorInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.ent1job.setObjectName("ent1job")
        self.horizontalLayout_6.addWidget(self.ent1job)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.butt1add = QtWidgets.QPushButton(self.page)
        #self.butt1add.setStyleSheet("border:2px solid white;\n""background-color:rgb(84, 158, 255);")
        self.butt1add.setDefault(False)
        self.butt1add.setFlat(False)
        self.butt1add.setObjectName("butt1add")
        self.verticalLayout.addWidget(self.butt1add)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.gridLayout_5.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.page_2)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.splitter_2 = QtWidgets.QSplitter(self.page_2)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.layoutWidget = QtWidgets.QWidget(self.splitter_2)
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.frame_3 = QtWidgets.QFrame(self.layoutWidget)
        self.frame_3.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.splitter_3 = QtWidgets.QSplitter(self.frame_3)
        self.splitter_3.setOrientation(QtCore.Qt.Vertical)
        self.splitter_3.setObjectName("splitter_3")
        self.layoutWidget1 = QtWidgets.QWidget(self.splitter_3)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_7 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_8.addWidget(self.label_7)
        self.ent2search = QtWidgets.QLineEdit(self.layoutWidget1)
        self.ent2search.setText("")
        self.ent2search.setObjectName("ent2search")
        self.horizontalLayout_8.addWidget(self.ent2search)
        self.lit2shoserh = QtWidgets.QListWidget(self.splitter_3)
        self.lit2shoserh.setObjectName("lit2shoserh")
        self.gridLayout_7.addWidget(self.splitter_3, 0, 0, 1, 1)
        self.horizontalLayout_7.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.layoutWidget)
        self.frame_4.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.splitter_4 = QtWidgets.QSplitter(self.frame_4)
        self.splitter_4.setOrientation(QtCore.Qt.Vertical)
        self.splitter_4.setObjectName("splitter_4")
        self.layoutWidget2 = QtWidgets.QWidget(self.splitter_4)
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_8 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_9.addWidget(self.label_8)
        self.comt2typdesin = QtWidgets.QComboBox(self.layoutWidget2)
        self.comt2typdesin.setObjectName("comt2typdesin")
        self.comt2typdesin.addItem("")
        self.comt2typdesin.addItem("")
        self.horizontalLayout_9.addWidget(self.comt2typdesin)
        self.layoutWidget3 = QtWidgets.QWidget(self.splitter_4)
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_9 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_10.addWidget(self.label_9)
        self.comt2font = QtWidgets.QFontComboBox(self.layoutWidget3)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.comt2font.setCurrentFont(font)
        self.comt2font.setObjectName("comt2font")
        self.horizontalLayout_10.addWidget(self.comt2font)
        self.layoutWidget4 = QtWidgets.QWidget(self.splitter_4)
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.layoutWidget4)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.butt2sho = QtWidgets.QPushButton(self.layoutWidget4)
        self.butt2sho.setObjectName("butt2sho")
        self.horizontalLayout_11.addWidget(self.butt2sho)
        self.butt2print = QtWidgets.QPushButton(self.layoutWidget4)
        self.butt2print.setObjectName("butt2print")
        self.horizontalLayout_11.addWidget(self.butt2print)
        self.gridLayout_8.addWidget(self.splitter_4, 0, 0, 1, 1)
        self.horizontalLayout_7.addWidget(self.frame_4)
        self.ent2sho = QtWidgets.QTextEdit(self.splitter_2)
        self.ent2sho.setFrameShape(QtWidgets.QFrame.Box)
        self.ent2sho.setOverwriteMode(False)
        self.ent2sho.setObjectName("ent2sho")
        self.gridLayout_6.addWidget(self.splitter_2, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.page_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.splitter_5 = QtWidgets.QSplitter(self.page_3)
        self.splitter_5.setOrientation(QtCore.Qt.Vertical)
        self.splitter_5.setObjectName("splitter_5")
        self.frame_5 = QtWidgets.QFrame(self.splitter_5)
        self.frame_5.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.frame_5)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.splitter_6 = QtWidgets.QSplitter(self.frame_5)
        self.splitter_6.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_6.setObjectName("splitter_6")
        self.frame_6 = QtWidgets.QFrame(self.splitter_6)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.frame_6)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_10 = QtWidgets.QLabel(self.frame_6)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_12.addWidget(self.label_10)
        self.ent3ensearch = QtWidgets.QLineEdit(self.frame_6)
        self.ent3ensearch.setObjectName("ent3ensearch")
        self.horizontalLayout_12.addWidget(self.ent3ensearch)
        self.verticalLayout_4.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.pushButton_7 = QtWidgets.QPushButton(self.frame_6)
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout_13.addWidget(self.pushButton_7)
        self.butt3print = QtWidgets.QPushButton(self.frame_6)
        self.butt3print.setObjectName("butt3print")
        self.horizontalLayout_13.addWidget(self.butt3print)
        self.verticalLayout_4.addLayout(self.horizontalLayout_13)
        self.gridLayout_11.addLayout(self.verticalLayout_4, 0, 0, 1, 1)
        self.frame_7 = QtWidgets.QFrame(self.splitter_6)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.frame_7)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.comt3typesearch = QtWidgets.QComboBox(self.frame_7)
        self.comt3typesearch.setEditable(False)
        self.comt3typesearch.setObjectName("comt3typesearch")
        self.comt3typesearch.addItem("")
        self.comt3typesearch.addItem("")
        self.comt3typesearch.addItem("")
        self.comt3typesearch.addItem("")
        self.comt3typesearch.addItem("")
        self.gridLayout_10.addWidget(self.comt3typesearch, 0, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.frame_7)
        self.label_11.setObjectName("label_11")
        self.gridLayout_10.addWidget(self.label_11, 0, 1, 1, 1)
        self.gridLayout_9.addWidget(self.splitter_6, 0, 0, 1, 1)
        self.txtt3 = QtWidgets.QTextEdit(self.splitter_5)
        self.txtt3.setFrameShape(QtWidgets.QFrame.Box)
        self.txtt3.setObjectName("txtt3")
        self.verticalLayout_3.addWidget(self.splitter_5)
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.page_4)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_9 = QtWidgets.QFrame(self.page_4)
        self.frame_9.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.gridLayout_15 = QtWidgets.QGridLayout(self.frame_9)
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.frame_14 = QtWidgets.QFrame(self.frame_9)
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.gridLayout_17 = QtWidgets.QGridLayout(self.frame_14)
        self.gridLayout_17.setObjectName("gridLayout_17")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.label_18 = QtWidgets.QLabel(self.frame_14)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_20.addWidget(self.label_18)
        self.ent4enternamwell = QtWidgets.QLineEdit(self.frame_14)
        self.ent4enternamwell.setObjectName("ent4enternamwell")
        self.horizontalLayout_20.addWidget(self.ent4enternamwell)
        self.verticalLayout_7.addLayout(self.horizontalLayout_20)
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.pushButton_9 = QtWidgets.QPushButton(self.frame_14)
        self.pushButton_9.setObjectName("pushButton_9")
        self.horizontalLayout_21.addWidget(self.pushButton_9)
        self.pushButton_8 = QtWidgets.QPushButton(self.frame_14)
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout_21.addWidget(self.pushButton_8)
        self.pushButton_6 = QtWidgets.QPushButton(self.frame_14)
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_21.addWidget(self.pushButton_6)
        self.verticalLayout_7.addLayout(self.horizontalLayout_21)
        self.gridLayout_17.addLayout(self.verticalLayout_7, 0, 0, 1, 1)
        self.horizontalLayout_14.addWidget(self.frame_14)
        self.frame_13 = QtWidgets.QFrame(self.frame_9)
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.gridLayout_16 = QtWidgets.QGridLayout(self.frame_13)
        self.gridLayout_16.setObjectName("gridLayout_16")
        self.list4 = QtWidgets.QListWidget(self.frame_13)
        self.list4.setObjectName("list4")
        self.gridLayout_16.addWidget(self.list4, 0, 0, 1, 1)
        self.horizontalLayout_14.addWidget(self.frame_13)
        self.gridLayout_15.addLayout(self.horizontalLayout_14, 0, 0, 1, 1)
        self.verticalLayout_5.addWidget(self.frame_9)
        self.frame_8 = QtWidgets.QFrame(self.page_4)
        self.frame_8.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.frame_8)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.frame_11 = QtWidgets.QFrame(self.frame_8)
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.gridLayout_19 = QtWidgets.QGridLayout(self.frame_11)
        self.gridLayout_19.setObjectName("gridLayout_19")
        self.frame_10 = QtWidgets.QFrame(self.frame_11)
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.gridLayout_14 = QtWidgets.QGridLayout(self.frame_10)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_13 = QtWidgets.QLabel(self.frame_10)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_15.addWidget(self.label_13)
        self.ent4namewell = QtWidgets.QLineEdit(self.frame_10)
        self.ent4namewell.setObjectName("ent4namewell")
        self.horizontalLayout_15.addWidget(self.ent4namewell)
        self.verticalLayout_6.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.label_14 = QtWidgets.QLabel(self.frame_10)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_16.addWidget(self.label_14)
        self.ent4time = QtWidgets.QLineEdit(self.frame_10)
        self.ent4time.setObjectName("ent4time")
        self.horizontalLayout_16.addWidget(self.ent4time)
        self.verticalLayout_6.addLayout(self.horizontalLayout_16)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.label_15 = QtWidgets.QLabel(self.frame_10)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_17.addWidget(self.label_15)
        self.ent4date = QtWidgets.QLineEdit(self.frame_10)
        self.ent4date.setObjectName("ent4date")
        self.horizontalLayout_17.addWidget(self.ent4date)
        self.verticalLayout_6.addLayout(self.horizontalLayout_17)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.label_16 = QtWidgets.QLabel(self.frame_10)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_18.addWidget(self.label_16)
        self.ent4reson = QtWidgets.QLineEdit(self.frame_10)
        self.ent4reson.setObjectName("ent4reson")
        self.horizontalLayout_18.addWidget(self.ent4reson)
        self.verticalLayout_6.addLayout(self.horizontalLayout_18)
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.label_17 = QtWidgets.QLabel(self.frame_10)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_19.addWidget(self.label_17)
        self.ent4remark = QtWidgets.QLineEdit(self.frame_10)
        self.ent4remark.setObjectName("ent4remark")
        self.horizontalLayout_19.addWidget(self.ent4remark)
        self.verticalLayout_6.addLayout(self.horizontalLayout_19)
        self.gridLayout_14.addLayout(self.verticalLayout_6, 0, 0, 1, 1)
        self.gridLayout_19.addWidget(self.frame_10, 0, 0, 1, 1)
        self.gridLayout_13.addWidget(self.frame_11, 0, 0, 1, 1)
        self.frame_12 = QtWidgets.QFrame(self.frame_8)
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.gridLayout_18 = QtWidgets.QGridLayout(self.frame_12)
        self.gridLayout_18.setObjectName("gridLayout_18")
        self.label_12 = QtWidgets.QLabel(self.frame_12)
        self.label_12.setObjectName("label_12")
        self.gridLayout_18.addWidget(self.label_12, 0, 0, 1, 1)
        self.txtt4 = QtWidgets.QTextEdit(self.frame_12)
        self.txtt4.setObjectName("txtt4")
        self.gridLayout_18.addWidget(self.txtt4, 0, 1, 1, 1)
        self.gridLayout_13.addWidget(self.frame_12, 0, 1, 1, 1)
        self.verticalLayout_5.addWidget(self.frame_8)
        self.gridLayout_12.addLayout(self.verticalLayout_5, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_4)
        self.gridLayout_4.addWidget(self.stackedWidget, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 796, 27))
        self.menubar.setObjectName("menubar")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.dockWidget_2 = QtWidgets.QDockWidget(MainWindow)
        self.dockWidget_2.setFeatures(QtWidgets.QDockWidget.DockWidgetFloatable|QtWidgets.QDockWidget.DockWidgetMovable)
        self.dockWidget_2.setObjectName("dockWidget_2")
        self.dockWidgetContents_2 = QtWidgets.QWidget()
        self.dockWidgetContents_2.setObjectName("dockWidgetContents_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.dockWidgetContents_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame_2 = QtWidgets.QFrame(self.dockWidgetContents_2)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.splitter = QtWidgets.QSplitter(self.frame_2)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.butt1 = QtWidgets.QPushButton(self.splitter)
        self.butt1.setCheckable(False)
        self.butt1.setDefault(False)
        self.butt1.setObjectName("butt1")
        self.butt2 = QtWidgets.QPushButton(self.splitter)
        self.butt2.setObjectName("butt2")
        self.butt3 = QtWidgets.QPushButton(self.splitter)
        self.butt3.setObjectName("butt3")
        self.butt4 = QtWidgets.QPushButton(self.splitter)
        self.butt4.setObjectName("butt4")
        self.butclose = QtWidgets.QPushButton(self.splitter)
        self.butclose.setObjectName("butclose")
        self.gridLayout_3.addWidget(self.splitter, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame_2, 0, 0, 1, 1)
        self.dockWidget_2.setWidget(self.dockWidgetContents_2)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockWidget_2)
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionClose = QtWidgets.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionClose)
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Name well:"))
        self.label_2.setText(_translate("MainWindow", "Time:"))
        self.label_3.setText(_translate("MainWindow", "Date:"))
        self.label_4.setText(_translate("MainWindow", "Resoun:"))
        self.label_5.setText(_translate("MainWindow", "Remark:"))
        self.label_6.setText(_translate("MainWindow", "Job Discription:"))
        self.ent1job.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sahadeva\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.butt1add.setText(_translate("MainWindow", "ADD"))
        self.label_7.setText(_translate("MainWindow", "search:"))
        self.label_8.setText(_translate("MainWindow", "Type disging:"))
        self.comt2typdesin.setItemText(0, _translate("MainWindow", "Normal"))
        self.comt2typdesin.setItemText(1, _translate("MainWindow", "Table"))
        self.label_9.setText(_translate("MainWindow", "Font:"))
        self.butt2sho.setText(_translate("MainWindow", "show"))
        self.butt2print.setText(_translate("MainWindow", "print"))
        self.ent2sho.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sahadeva\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_10.setText(_translate("MainWindow", "Enter Serarch:"))
        self.pushButton_7.setText(_translate("MainWindow", "show"))
        self.butt3print.setText(_translate("MainWindow", "print"))
        self.comt3typesearch.setItemText(0, _translate("MainWindow", "NameWell"))
        self.comt3typesearch.setItemText(1, _translate("MainWindow", "Data"))
        self.comt3typesearch.setItemText(2, _translate("MainWindow", "Reason"))
        self.comt3typesearch.setItemText(3, _translate("MainWindow", "Remark"))
        self.comt3typesearch.setItemText(4, _translate("MainWindow", "JobDiscripsion"))
        self.label_11.setText(_translate("MainWindow", "choos type serach:"))
        self.label_18.setText(_translate("MainWindow", "enter name well:"))
        self.pushButton_9.setText(_translate("MainWindow", "delete"))
        self.pushButton_8.setText(_translate("MainWindow", "show"))
        self.pushButton_6.setText(_translate("MainWindow", "modify"))
        self.label_13.setText(_translate("MainWindow", "Name well:"))
        self.label_14.setText(_translate("MainWindow", "Time:"))
        self.label_15.setText(_translate("MainWindow", "Date:"))
        self.label_16.setText(_translate("MainWindow", "Reson:"))
        self.label_17.setText(_translate("MainWindow", "Remark:"))
        self.label_12.setText(_translate("MainWindow", "job discription:"))
        self.menuHelp.setTitle(_translate("MainWindow", "help"))
        self.butt1.setText(_translate("MainWindow", "ADDS"))
        self.butt2.setText(_translate("MainWindow", "printer"))
        self.butt3.setText(_translate("MainWindow", "Search"))
        self.butt4.setText(_translate("MainWindow", "Modifcation"))
        self.butclose.setText(_translate("MainWindow", "CLOSE"))
        self.actionAbout.setText(_translate("MainWindow", "about"))
        self.actionClose.setText(_translate("MainWindow", "close"))
class NotePad(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)#lambda:تضعها عند اسم الزر
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        x=datetime.datetime.now().hour
        s=datetime.datetime.now().minute
        a=datetime.datetime.now().second
        today = date.today()
        m=str(x)+":"+str(s)
        self.ui.ent1time.setText(m)
        self.ui.ent1date.setText(str(today))
        self.ui.butt1.clicked.connect(self.s1)
        self.ui.butt2.clicked.connect(self.s2)
        self.ui.butt3.clicked.connect(self.s3)
        self.ui.butt4.clicked.connect(self.s4)
        self.ui.butclose.clicked.connect(self.out1)
        self.ui.butt1add.clicked.connect(self.add)
        self.ui.lit2shoserh.itemClicked.connect(self.choosser)
        self.ui.list4.itemClicked.connect(self.serm2)
        self.serach1()
        self.ui.ent2search.textChanged.connect(self.serach2)
        self.ui.butt2sho.clicked.connect(self.db11)
        self.ui.ent3ensearch.textChanged.connect(self.shoser)
        self.ui.ent4enternamwell.textChanged.connect(self.serm1)
        self.ui.pushButton_8.clicked.connect(self.serm3)
        self.ui.pushButton_6.clicked.connect(self.serm4)
        self.ui.pushButton_9.clicked.connect(self.dele)
        self.ui.butt2print.clicked.connect(self.print1)
        self.ui.butt3print.clicked.connect(self.print2)
        self.ui.actionClose.triggered.connect(self.out1)
        self.ui.actionAbout.triggered.connect(self.instr)

    ###############################################################3
    def s1(self):
   	    self.ui.stackedWidget.setCurrentIndex(0)
    def s2(self):
        self.ui.stackedWidget.setCurrentIndex(1)
    def s3(self):
        self.ui.stackedWidget.setCurrentIndex(2)
    def s4(self):
        self.ui.stackedWidget.setCurrentIndex(3)

    def out1(self):
        exit()
    ##########################################################################
    ##############################tab1#############################################################3
    ################################################################################################
    def add(self):
    	a=str(self.ui.ent1name.text())
    	b=str(self.ui.ent1time.text())
    	c=str(self.ui.ent1date.text())
    	d=str(self.ui.ent1reson.text())
    	e=str(self.ui.ent1remark.text())
    	f=str(self.ui.ent1job.toPlainText())
    	if a=="":
    		entname.setText("Please Enter name well")
    	elif d=="":
    		entreason.setText("Please Enter reason")
    	elif e=="":
    		entremark.setText("Please Enter remark")
    	elif f=="":
    		entjob.setText("Please Enter Job Discripsion")
    	else:
    		db1=sqlite3.connect('compny2.db')
    		db1.row_factory=sqlite3.Row
    		db1.execute('create table if not exists adds2(ID integer primary Key autoincrement,NameWell text,Time text,Data text,Reason text,Remark text,JobDiscripsion text)')
    		db1.execute("insert into adds2(NameWell ,Time,Data,Reason,Remark,JobDiscripsion ) values(?,?,?,?,?,?)",(a,b,c,d,e,f))
    		db1.commit()
    		self.ui.ent1name.clear()
    		self.ui.ent1time.clear()
    		self.ui.ent1reson.clear()
    		self.ui.ent1remark.clear()
    		self.ui.ent1job.clear()
    		self.ui.ent1time.setText(m)


    		message=QtWidgets.QMessageBox.information(self,'information','<FONT size=10 color=blue>Add Successfully</FONT>')


    ###############################3finshed tab1####################################################
    ##################################################################################################
    ##################################tab2################################################################
    ######################################################################################################
    def serach1(self):
    	try:
    		self.ui.lit2shoserh.clear()
    		db=sqlite3.connect("compny2.db")
    		db.row_factory=sqlite3.Row
    		sh=db.execute('select NameWell from adds2')
    		for n in sh:
    			self.ui.lit2shoserh.insertItem(0,'{}'.format(n['NameWell']))
    			self.ui.list4.insertItem(0,'{}'.format(n['NameWell']))
    		sh2=db.execute("select * from adds2")
    		for m in sh2:
    			#self.ui.txtt3.append("<p><table width='100%' border='2' cellpadding'5' bgcolor='green'><caption><b><u><center>Name Well: {}</center></u></b></caption><tr><td><u><center>NameWell</center></u></td><td><u><center>Time</u></center></td><td><u><center>Date</u></center></td><td><u><center>Reason</u></center></td><td><u><center>Remark</u></center></td><td><u><center>JobDiscripsion</u></center></td></tr><tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr></table></p><br>".format(m['NameWell'],m['NameWell'],m['Time'],m['Data'],m['Reason'],m['Remark'],m['JobDiscripsion']))
    			self.ui.txtt3.append("""<html lange="zh-CN">
    <head>
        <meta charset="utf-8">
      <link rel="stylesheet" type="text/css" href="f.css">
    </head>
    <body id="gg">
    
      <table width=100% border='1'><caption><b><u><center>Name Well: {}</center></u></b></caption>
      <tr><th>NameWell</th><th>Time</th><th>Date</th><th>Reason</th><th>Remark</th><th>JobDiscripsion</th></tr>
      <tr ><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr> 
      </table>
    </body>
</html>""".format(m['NameWell'],m['NameWell'],m['Time'],m['Data'],m['Reason'],m['Remark'],m['JobDiscripsion']))
    	except:
    		self.ui.lit2shoserh.insertItem(0,"the database is empty")
    	
    def serach2(self):
    	try:
    		self.ui.lit2shoserh.clear()
    		d=str(self.ui.ent2search .text())
    		db=sqlite3.connect("compny2.db")
    		db.row_factory=sqlite3.Row
    		sh=db.execute('select * from adds2 where NameWell like "%{}%"or Data like "%{}%"'.format(d,d))
    		for n in sh:
    			self.ui.lit2shoserh.insertItem(0,'{}'.format(n['NameWell']))
    	except:
    		self.ui.lit2shoserh.insertItem(0,"the database is empty")
    def choosser(self):
    	item = self.ui.lit2shoserh.currentItem()
    	r=str(item.text())
    	self.ui.ent2search.setText(r)
    def db2(self):
    	d=str(self.ui.ent2search.text())
    	if d=='':
    		message=QtWidgets.QMessageBox.information(self,'information','<FONT size=10 color=blue>please Enter name well</FONT>')
    	else:
    		self.ui.ent2sho.clear()
    		db=sqlite3.connect('compny2.db')
    		db.row_factory=sqlite3.Row
    		sd=db.execute('select * from adds2 where NameWell="{}"'.format(d))
    		for m in sd:
    			# self.ui.ent2sho.append("<p align=right><img src='logo.png'></p><br>")
    			# self.ui.ent2sho.append("<FONT size=5>------|DateTime:{}|------</FONT>".format(t))
    			# self.ui.ent2sho.append("<FONT size=9>--------------------------------------------------------------------------</FONT><br>")
    			# self.ui.ent2sho.append("<FONT size=7>Name well:</FONT> <font color=blue size=7>{}</font><br>".format(m['NameWell']))
    			# self.ui.ent2sho.append("<FONT size=7>Time:</FONT> <font color=blue size=7>{}</font><br>".format(m['Time']))
    			# self.ui.ent2sho.append("<FONT size=7>date:</FONT> <font color=blue size=7>{}</font><br>".format(m['Data']))
    			# self.ui.ent2sho.append("<FONT size=7>reason:</FONT> <font color=blue size=7>{}</font><br>".format(m['Reason']))
    			# self.ui.ent2sho.append("<FONT size=7>remark:</FONT> <font color=blue size=7>{}</font><br>".format(m['Remark']))
    			# self.ui.ent2sho.append("<FONT size=7>job discripsion:</FONT> <font color=blue size=7>{}</font><br>---------------------------------------------------------------------------------------".format(m['JobDiscripsion']))
    			# #entprint.append("<p><table width='100%' border='5' cellpadding'5' bgcolor='green'><caption><b><u><center>{}</center></u></b></caption><tr><td><u><center>NameWell</center></u></td><td><u><center>Time</u></center></td><td><u><center>Date</u></center></td><td><u><center>Reason</u></center></td><td><u><center>Remark</u></center></td><td><u><center>JobDiscripsion</u></center></td></tr><tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr></table></p><br>".format(t,m['NameWell'],m['Time'],m['Data'],m['Reason'],m['Remark'],m['JobDiscripsion']))
    			self.ui.ent2sho.append("""<html lange="zh-CN">
    <head>
        <meta charset="utf-8">
      <link rel="stylesheet" type="text/css" href="f.css">
    </head>
    <body class="gg">
    <center><img  src="logo.png"></center>
    <hr>
    <p style="text-align:center;">------|DateTime:{}|------</p>
    
    <p>Name well:{}</p>
    <p>Time:{}</p>
    <p>Date:{}</p>
    <p>Reason:{}</p>
    <p>Remark:{}</p>
    <p>job discripsion:{}</p>
    
      <hr>
    </body>
</html>""".format(t,m['NameWell'],m['Time'],m['Data'],m['Reason'],m['Remark'],m['JobDiscripsion']))
    def db3(self):
    	today = date.today()
    	d=str(self.ui.ent2search.text())
    	if d=='':
    		message=QtWidgets.QMessageBox.information(self,'information','<FONT size=10 color=blue>please Enter name well</FONT>')
    	else:
    		self.ui.ent2sho.clear()
    		db=sqlite3.connect('compny2.db')
    		db.row_factory=sqlite3.Row
    		sd=db.execute('select * from adds2 where NameWell="{}"'.format(d))
    		for m in sd:
    			#self.ui.ent2sho.append("<p align=right><img src='logo.png'></p><br>")
    			#elf.ui.ent2sho.append("<p><table width='100%' border='1' cellpadding'1' bgcolor='green'><caption><b><u><center>Data Time: {}</center></u></b></caption><tr><td><u><center>NameWell</center></u></td><td><u><center>Time</u></center></td><td><u><center>Date</u></center></td><td><u><center>Reason</u></center></td><td><u><center>Remark</u></center></td><td><u><center>JobDiscripsion</u></center></td></tr><tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr></table></p><br>".format(t,m['NameWell'],m['Time'],m['Data'],m['Reason'],m['Remark'],m['JobDiscripsion']))
    			self.ui.ent2sho.append("""<html lange="zh-CN">
    <head>
        <meta charset="utf-8">
      <link rel="stylesheet" type="text/css" href="f.css">
    </head>
    <body id="gg">
    <img  src="logo.png" width=30 height=30><br>
      <table width=100% border='1'><caption><b><u><center>Data Time: {}</center></u></b></caption>
      <tr><th>NameWell</th><th>Time</th><th>Date</th><th>Reason</th><th>Remark</th><th>JobDiscripsion</th></tr>
      <tr ><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr> 
      </table>
    </body>
</html>""".format(t,m['NameWell'],m['Time'],m['Data'],m['Reason'],m['Remark'],m['JobDiscripsion']))
    def db11(self):
    	co1=str(self.ui.comt2typdesin.currentText())
    	co2=str(self.ui.comt2font.currentText())
    	self.ui.ent2sho.setFont(QFont(co2,16))
    	if co1=="Normal":
    		self.db2()
    	else:
    		self.db3()

    	
    ###############################3###finsh tab2##############################################################
    ############################################################################################################
    ####################################TAB 33###################################################################
    #############################################################################################################
    def shoser(self):
    	self.ui.txtt3.clear()
    	d=str(self.ui.ent3ensearch .text())
    	d2=str(self.ui.comt3typesearch .currentText())
    	db=sqlite3.connect("compny2.db")
    	db.row_factory=sqlite3.Row
    	sh=db.execute('select * from adds2 where "{}" like "%{}%"'.format(d2,d))
    	for m in sh:
    		#self.ui.txtt3.append("<p><table width='100%' border='1' cellpadding'1' bgcolor='green'><caption><b><u><center>Name Well: {}</center></u></b></caption><tr><td><u><center>NameWell</center></u></td><td><u><center>Time</u></center></td><td><u><center>Date</u></center></td><td><u><center>Reason</u></center></td><td><u><center>Remark</u></center></td><td><u><center>JobDiscripsion</u></center></td></tr><tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr></table></p><br>".format(m['NameWell'],m['NameWell'],m['Time'],m['Data'],m['Reason'],m['Remark'],m['JobDiscripsion']))
    		self.ui.txtt3.append("""<html lange="zh-CN">
    <head>
        <meta charset="utf-8">
      <link rel="stylesheet" type="text/css" href="f.css">
    </head>
    <body id="gg">
    <hr>
      <table width=100% border='1'><caption><b><u><center>Name Well: {}</center></u></b></caption>
      <tr><th>NameWell</th><th>Time</th><th>Date</th><th>Reason</th><th>Remark</th><th>JobDiscripsion</th></tr>
      <tr ><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr> 
      </table>
      <hr>
    </body>
</html>""".format(m['NameWell'],m['NameWell'],m['Time'],m['Data'],m['Reason'],m['Remark'],m['JobDiscripsion']))
    	
    #####################################FINSH TAB3 ################################################################
    ##################################################################################################################
    ######################################tab4 $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$########################################
    ###################################################################################################################
    def serm1(self):
    	try:
    		self.ui.list4.clear()
    		d=str(self.ui.ent4enternamwell .text())
    		db=sqlite3.connect("compny2.db")
    		db.row_factory=sqlite3.Row
    		sh=db.execute('select * from adds2 where NameWell like "%{}%"or Data like "%{}%"'.format(d,d))
    		for n in sh:
    			self.ui.list4.insertItem(0,'{}'.format(n['NameWell']))
    	except:
    		self.ui.list4.insertItem(0,"the database is empty")
    def serm2(self):
    	item = self.ui.list4.currentItem()
    	r=str(item.text())
    	self.ui.ent4enternamwell.setText(r)
    def serm3(self):
    	try:
    		self.ui.ent4namewell.clear()
    		self.ui.ent4remark.clear()
    		self.ui.ent4reson.clear()
    		self.ui.ent4date.clear()
    		self.ui.txtt4.clear()
    		self.ui.ent4time.clear()
    		d=str(self.ui.ent4enternamwell .text())
    		db=sqlite3.connect("compny2.db")
    		db.row_factory=sqlite3.Row
    		sh=db.execute('select * from adds2 where NameWell="{}"'.format(d))
    		for n in sh:
    			self.ui.ent4reson.setText(n["Reason"])
    			self.ui.ent4remark.setText(n["Remark"])
    			self.ui.ent4time.setText(n["Time"])
    			self.ui.ent4date.setText(n["Data"])
    			self.ui.ent4namewell.setText(n["NameWell"])
    			self.ui.txtt4.append(n["JobDiscripsion"])
    	except:
    		self.ui.list4.insertItem(0,"the database is empty")
    def serm4(self):
    	d=(self.ui.ent4enternamwell.text())
    	d1=(self.ui.ent4namewell.text())
    	d2=(self.ui.ent4time.text())
    	d3=(self.ui.ent4date.text())
    	d4=(self.ui.ent4reson.text())
    	d5=(self.ui.ent4remark.text())
    	d6=(self.ui.txtt4.toPlainText())

    	db=sqlite3.connect("compny2.db")
    	db.row_factory=sqlite3.Row
    	sh=db.execute('update adds2 set NameWell="{}",Time="{}",Data="{}",Reason="{}",Remark="{}",JobDiscripsion="{}" where NameWell="{}"'.format(d1,d2,d3,d4,d5,d6,d))
    	db.commit()		
    	QtWidgets.QMessageBox.information(self,'information','<FONT size=10 color=blue>تم التعديل بنجاح</FONT>')
    def dele(self):
    	d=str(self.ui.ent4enternamwell.text())
    	db=sqlite3.connect("compny2.db")
    	db.row_factory=sqlite3.Row
    	db.execute("delete from adds2 where NameWell='{}'".format(d))
    	db.commit()
    	QtWidgets.QMessageBox.information(self,'information','<FONT size=10 color=blue>ok delete</FONT>')
    #######################################finshed tab4###################################################################
    #######################################################################################################################
    def print1(self):#printer##################################printer##################################################
        if self.ui.ent2sho.toPlainText() !="":
            printer =QtPrintSupport.QPrintDialog()
            #printer.setFullPage(True)
            #dialog = QtGui.QPrintDialog(printer)
            if printer.exec_() == QtWidgets.QDialog.Accepted:
                self.ui.ent2sho.document().print_(printer.printer())
                printer.exec_()
    def print2(self):#printer##################################printer##################################################
        if self.ui.txtt3.toPlainText() !="":
            printer =QtPrintSupport.QPrintDialog()
            #printer.setFullPage(True)
            #dialog = QtGui.QPrintDialog(printer)
            if printer.exec_() == QtWidgets.QDialog.Accepted:
                self.ui.txtt3.document().print_(printer.printer())
                printer.exec_()
    def instr(self):
    	message=QtWidgets.QMessageBox.information(self,'about programmer','<FONT size=5 color=black>Copyright (C) 2020,By The programmer Salem khamis Bahien</FONT><br><p>Email:99zzz52@gmail.com</p><p>Telephon:713151679</p>')
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

