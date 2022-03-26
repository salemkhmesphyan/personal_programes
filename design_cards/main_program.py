# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'p1.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!
import treepoem
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QBrush, QPainter, QPen, QPixmap, QPolygonF,QImage
import pyqrcode 
from pyqrcode import QRCode 
from PyQt5.QtPrintSupport import QPrintPreviewDialog
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QGraphicsWidget,QGraphicsLineItem,QGraphicsProxyWidget,QColorDialog,QFontDialog,QGraphicsRectItem, QGraphicsScene, QGraphicsView, QGraphicsPixmapItem,QGraphicsItem,QGraphicsTextItem
global rot,st_color,sh_b,st_rect,p,st_tip,tip
tip=0
st_tip=[]
p=[]
st_rect=[]
sh_b=1
st_color=0
rot=0
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1071, 551)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2p1 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2p1.setObjectName("gridLayout_2p1")
        self.splitter = QtWidgets.QSplitter(self.frame)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.but_t_save_pdf = QtWidgets.QToolButton(self.splitter)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("image/filesave.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.but_t_save_pdf.setIcon(icon)
        self.but_t_save_pdf.setObjectName("but_t_save_pdf")
        self.but_t_show_boxtool = QtWidgets.QToolButton(self.splitter)
        self.but_t_show_boxtool.setObjectName("but_t_show_boxtool")
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.but_t_up = QtWidgets.QToolButton(self.layoutWidget)
        self.but_t_up.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("image/back1.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.but_t_up.setIcon(icon1)
        self.but_t_up.setArrowType(QtCore.Qt.NoArrow)
        self.but_t_up.setObjectName("but_t_up")
        self.verticalLayout_3.addWidget(self.but_t_up)
        self.but_t_down = QtWidgets.QToolButton(self.layoutWidget)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("image/back2.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.but_t_down.setIcon(icon2)
        self.but_t_down.setArrowType(QtCore.Qt.NoArrow)
        self.but_t_down.setObjectName("but_t_down")
        self.verticalLayout_3.addWidget(self.but_t_down)
        self.layoutWidget1 = QtWidgets.QWidget(self.splitter)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.en_t_addtext = QtWidgets.QLineEdit(self.layoutWidget1)
        self.en_t_addtext.setObjectName("en_t_addtext")
        self.horizontalLayout.addWidget(self.en_t_addtext)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.but_t_addtext = QtWidgets.QToolButton(self.layoutWidget1)
        self.but_t_addtext.setObjectName("but_t_addtext")
        self.verticalLayout.addWidget(self.but_t_addtext)
        self.layoutWidget2 = QtWidgets.QWidget(self.splitter)
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4)
        self.slid_t_zom = QtWidgets.QSlider(self.layoutWidget2)
        self.slid_t_zom.setSliderPosition(0)
        self.slid_t_zom.setTracking(True)
        self.slid_t_zom.setMinimum(1.0)
        self.slid_t_zom.setMaximum(12.0)
        self.slid_t_zom.setOrientation(QtCore.Qt.Horizontal)
        self.slid_t_zom.setInvertedAppearance(False)
        self.slid_t_zom.setInvertedControls(False)
        self.slid_t_zom.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.slid_t_zom.setObjectName("slid_t_zom")
        self.verticalLayout_4.addWidget(self.slid_t_zom)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.but_t_smll = QtWidgets.QToolButton(self.layoutWidget2)
        self.but_t_smll.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("image/index2.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.but_t_smll.setIcon(icon3)
        self.but_t_smll.setIconSize(QtCore.QSize(24, 20))
        self.but_t_smll.setAutoRepeat(False)
        self.but_t_smll.setAutoExclusive(False)
        self.but_t_smll.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.but_t_smll.setAutoRaise(False)
        self.but_t_smll.setObjectName("but_t_smll")
        self.horizontalLayout_3.addWidget(self.but_t_smll)
        self.but_t_big = QtWidgets.QToolButton(self.layoutWidget2)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("image/index.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.but_t_big.setIcon(icon4)
        self.but_t_big.setIconSize(QtCore.QSize(24, 20))
        self.but_t_big.setObjectName("but_t_big")
        self.horizontalLayout_3.addWidget(self.but_t_big)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.layoutWidget3 = QtWidgets.QWidget(self.splitter)
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.slid_t_rote = QtWidgets.QSlider(self.layoutWidget3)
        self.slid_t_rote.setOrientation(QtCore.Qt.Horizontal)
        self.slid_t_rote.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.slid_t_rote.setObjectName("slid_t_rote")
        self.slid_t_rote.setMinimum(-180.1)
        self.slid_t_rote.setValue(180.1)
        self.slid_t_rote.setMaximum(360.1)
        self.verticalLayout_2.addWidget(self.slid_t_rote)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.but_t_60 = QtWidgets.QToolButton(self.layoutWidget3)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("image/indexu.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.but_t_60.setIcon(icon5)
        self.but_t_60.setObjectName("but_t_60")
        self.horizontalLayout_2.addWidget(self.but_t_60)
        self.but_t_90 = QtWidgets.QToolButton(self.layoutWidget3)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("image/indexف.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.but_t_90.setIcon(icon6)
        self.but_t_90.setObjectName("but_t_90")
        self.horizontalLayout_2.addWidget(self.but_t_90)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.but_t_remov = QtWidgets.QToolButton(self.splitter)
        self.but_t_remov.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("image/indexع.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.but_t_remov.setIcon(icon7)
        self.but_t_remov.setIconSize(QtCore.QSize(26, 38))
        self.but_t_remov.setObjectName("but_t_remov")
        self.layoutWidget4 = QtWidgets.QWidget(self.splitter)
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.layoutWidget4)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.but_t_addrect = QtWidgets.QToolButton(self.layoutWidget4)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("image/index4.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.but_t_addrect.setIcon(icon8)
        self.but_t_addrect.setObjectName("but_t_addrect")
        self.horizontalLayout_4.addWidget(self.but_t_addrect)
        self.but_t_addcircu = QtWidgets.QToolButton(self.layoutWidget4)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("image/index5.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.but_t_addcircu.setIcon(icon9)
        self.but_t_addcircu.setObjectName("but_t_addcircu")
        self.horizontalLayout_4.addWidget(self.but_t_addcircu)
        self.verticalLayout_5.addLayout(self.horizontalLayout_4)
        self.but_t_addimg = QtWidgets.QToolButton(self.layoutWidget4)
        ##################3line
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("image/index3.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.but_t_addimg.setIcon(icon10)
        self.but_t_addimg.setObjectName("but_t_addimg")
        #self.but_t_addlin.setObjectName("but_t_addlin")
        self.verticalLayout_5.addWidget(self.but_t_addimg)
        
        
        self.but_t_show = QtWidgets.QToolButton(self.splitter)
        self.but_t_show.setObjectName("but_t_show")
        
        self.but_t_noshow = QtWidgets.QToolButton(self.splitter)
        self.but_t_noshow.setObjectName("noshow")
        
        self.but_t_transtext = QtWidgets.QToolButton(self.splitter)
        self.but_t_transtext.setObjectName("but_t_transtext")
        
        self.gridLayout_2p1.addWidget(self.splitter, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.frame, 0, 0, 1, 1)
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName("graphicsView")
        self.graphicsView.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)
        self.graphicsView.setFrameShape(QtWidgets.QFrame.Box)
        self.graphicsView.setFrameShadow(QtWidgets.QFrame.Plain)
        self.graphicsView.setLineWidth(7)
        self.graphicsView.setAcceptDrops(True)
        self.scene = QtWidgets.QGraphicsScene(self.centralwidget)
        
        self.scene.setSceneRect(0, 0, 546,464)
        self.graphicsView.setScene(self.scene)
        self.graphicsView.setCursor(QtCore.Qt.CrossCursor)
        #rect_item = QtWidgets.QGraphicsRectItem(QtCore.QRectF(50,50 , 100,100))
        #rect_item.setColor(QColor("blue"))
        #rect_item.setFlag(QtWidgets.QGraphicsItem.ItemIsMovable, True)
        #rect_item.setFlag(QGraphicsItem.ItemIsSelectable, True)
        #rect_item.setBrush(QBrush(QColor(230,190,100,200)))
        #rect_item.setZValue(0)
        #pp=QPen(Qt.black)
        #pp.setWidth(10)
        #rect_item.setPen(pp)
        #st_rect.append(rect_item)
        
        #self.sm=self.scene.createItemGroup([rect_item])
        #self.sm.setFlags(QGraphicsItem.ItemIsSelectable|QGraphicsItem.ItemIsMovable)
        #self.sm.setToolTip("group1")
        #self.graphicsView.fitInView(self.scene.sceneRect(), Qt.KeepAspectRatio)
        #self.graphicsView.setWindowIcon(QtGui.QIcon("2.png"))
        
        
        
        self.gridLayout_5.addWidget(self.graphicsView, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1071, 27))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        self.actionAbout = QtWidgets.QAction("عن المبرمج",MainWindow)##########33
        self.menuFile.addAction(self.actionAbout)
        
        
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.dockWidget1 = QtWidgets.QDockWidget(MainWindow)
        self.dockWidget1.setFeatures(QtWidgets.QDockWidget.DockWidgetFloatable|QtWidgets.QDockWidget.DockWidgetMovable)
        self.dockWidget1.setObjectName("dockWidget1")
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.dockWidgetContents)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.dockWidgetContents)
        self.label.setFrameShape(QtWidgets.QFrame.Panel)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(self.dockWidgetContents)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.East)
        self.tabWidget.setMovable(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.splitter_2 = QtWidgets.QSplitter(self.tab)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.but_b_color_font = QtWidgets.QPushButton(self.splitter_2)
        self.but_b_color_font.setObjectName("but_b_color_font")
        self.but_b_type_font = QtWidgets.QPushButton(self.splitter_2)
        self.but_b_type_font.setObjectName("but_b_type_font")
        self.but_b_edit_font = QtWidgets.QPushButton(self.splitter_2)###font
        self.but_b_edit_font.setObjectName("but_b_edit_font")
        self.but_b_edit_font.setText("تعديل النص")
        self.layoutWidget5 = QtWidgets.QWidget(self.splitter_2)
        self.layoutWidget5.setObjectName("layoutWidget5")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.layoutWidget5)
        self.verticalLayout_6.setSpacing(2)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem)
        self.sp_b_spac_font = QtWidgets.QSpinBox(self.layoutWidget5)
        self.sp_b_spac_font.setValue(100)
        self.sp_b_spac_font.setMinimum(100)
        self.sp_b_spac_font.setMaximum(10000)
        self.sp_b_spac_font.setObjectName("sp_b_spac_font")
        self.verticalLayout_6.addWidget(self.sp_b_spac_font)
        self.but_b_spac_font = QtWidgets.QPushButton(self.layoutWidget5)
        self.but_b_spac_font.setObjectName("but_b_spac_font")
        self.verticalLayout_6.addWidget(self.but_b_spac_font)
        self.gridLayout_2.addWidget(self.splitter_2, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")####################
        self.tab_2.setToolTip("ادوات الشكل")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.splitter_3 = QtWidgets.QSplitter(self.tab_2)
        self.splitter_3.setOrientation(QtCore.Qt.Vertical)
        self.splitter_3.setObjectName("splitter_3")
        self.but_b_bacglor_mod = QtWidgets.QPushButton(self.splitter_3)
        self.but_b_bacglor_mod.setObjectName("but_b_bacglor_mod")
        self.but_b_coloborder_mod = QtWidgets.QPushButton(self.splitter_3)
        self.but_b_coloborder_mod.setObjectName("but_b_coloborder_mod")
        self.but_b_sizsfaf_mod = QtWidgets.QPushButton(self.splitter_3)##################shafih
        self.but_b_sizsfaf_mod.setObjectName("but_b_sizsfaf_mod")
        self.but_t_addlin = QtWidgets.QToolButton(self.splitter_3)
        self.but_t_addlin.setObjectName("but_t_addlin")
        self.but_t_addlin.setText("اضافة خط")
        self.but_b_backimg_mod = QtWidgets.QPushButton(self.splitter_3)
        self.but_b_backimg_mod.setObjectName("but_b_backimg_mod")
        self.but_b_backimg_mod.setText("اضافة صورة للخلفية")
        self.sp_b_sizwidth_mod = QtWidgets.QSpinBox(self.splitter_3)
        self.sp_b_sizwidth_mod.setObjectName("sp_b_sizwidth_mod")
        self.sp_b_sizwidth_mod.setToolTip("حجم العرض")
        self.sp_b_sizhight_mod = QtWidgets.QSpinBox(self.splitter_3)#################33
        self.sp_b_sizhight_mod.setObjectName("sp_b_sizhight_mod")
        self.sp_b_sizhight_mod.setToolTip("حجم الارتفاع")
        self.sp_b_sizwidth_mod.setValue(1000)
        self.sp_b_sizwidth_mod.setMinimum(1)
        self.sp_b_sizwidth_mod.setMaximum(100000)
        self.sp_b_sizhight_mod.setValue(1000)
        self.sp_b_sizhight_mod.setMinimum(1)
        self.sp_b_sizhight_mod.setMaximum(100000)
        
        self.layoutWidget6 = QtWidgets.QWidget(self.splitter_3)
        self.layoutWidget6.setObjectName("layoutWidget6")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.layoutWidget6)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.sp_b_sizborder_mod = QtWidgets.QSpinBox(self.layoutWidget6)
        self.sp_b_sizborder_mod.setObjectName("sp_b_sizborder_mod")
        self.horizontalLayout_5.addWidget(self.sp_b_sizborder_mod)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget6)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.verticalLayout_7.addLayout(self.horizontalLayout_5)
        self.but_b_setborder_mod = QtWidgets.QPushButton(self.layoutWidget6)
        self.but_b_setborder_mod.setObjectName("but_b_setborder_mod")
        self.verticalLayout_7.addWidget(self.but_b_setborder_mod)
        self.gridLayout_3.addWidget(self.splitter_3, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_6 = QtWidgets.QLabel(self.tab_3)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_8.addWidget(self.label_6)
        self.line = QtWidgets.QFrame(self.tab_3)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_8.addWidget(self.line)
        self.verticalLayout_9.addLayout(self.verticalLayout_8)
        self.en_b_text_trans = QtWidgets.QLineEdit(self.tab_3)
        self.en_b_text_trans.setObjectName("en_b_text_trans")
        self.verticalLayout_9.addWidget(self.en_b_text_trans)
        self.but_b_addtext_apac_trans = QtWidgets.QPushButton(self.tab_3)
        self.but_b_addtext_apac_trans.setObjectName("but_b_addtext_apac_trans")
        self.verticalLayout_9.addWidget(self.but_b_addtext_apac_trans)
        self.verticalLayout_13.addLayout(self.verticalLayout_9)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_13.addItem(spacerItem2)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.line_2 = QtWidgets.QFrame(self.tab_3)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_10.addWidget(self.line_2)
        self.line_3 = QtWidgets.QFrame(self.tab_3)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_10.addWidget(self.line_3)
        self.verticalLayout_13.addLayout(self.verticalLayout_10)
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.verticalLayout_12.addLayout(self.verticalLayout_11)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_12.addLayout(self.horizontalLayout_6)
        self.verticalLayout_13.addLayout(self.verticalLayout_12)
        self.gridLayout_4.addLayout(self.verticalLayout_13, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tab_4)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.splitter_4 = QtWidgets.QSplitter(self.tab_4)
        self.splitter_4.setOrientation(QtCore.Qt.Vertical)
        self.splitter_4.setObjectName("splitter_4")
        self.but_b_addgroup_group = QtWidgets.QPushButton(self.splitter_4)
        self.but_b_addgroup_group.setObjectName("but_b_addgroup_group")
        self.but_b_additme_group = QtWidgets.QPushButton(self.splitter_4)
        self.but_b_additme_group.setObjectName("but_b_additme_group")
        self.but_b_remvgroup_group = QtWidgets.QPushButton(self.splitter_4)
        self.but_b_remvgroup_group.setObjectName("but_b_remvgroup_group")
        self.gridLayout_6.addWidget(self.splitter_4, 0, 0, 1, 1)
        self.but_b_note_group = QtWidgets.QPushButton(self.tab_4)
        self.but_b_note_group.setObjectName("but_b_note_group")
        self.gridLayout_6.addWidget(self.but_b_note_group, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab_4, "")
        self.gridLayout.addWidget(self.tabWidget, 1, 0, 1, 1)
        self.dockWidget1.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockWidget1)
        self.menubar.addAction(self.menuFile.menuAction())
        self.toolBar.addWidget(self.splitter)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "برنامج تصميم كروت اكترونية"))
        self.but_t_save_pdf.setText(_translate("MainWindow", "حفظ"))
        self.but_t_show_boxtool.setText(_translate("MainWindow", "اخفاء صندوق الادوات"))
        self.but_t_up.setToolTip(_translate("MainWindow", "<html><head/><body><p>اظهار العنصر على جميع العناصر</p></body></html>"))
        self.but_t_down.setToolTip(_translate("MainWindow", "<html><head/><body><p>اخفاء عن العنصر</p></body></html>"))
        self.but_t_down.setText(_translate("MainWindow", "..."))
        self.label_2.setText(_translate("MainWindow", "اضافة نص:"))
        self.but_t_addtext.setText(_translate("MainWindow", "اضافة نص"))
        self.label_4.setText(_translate("MainWindow", "التكبير"))
        self.but_t_big.setText(_translate("MainWindow", "+"))
        self.label_3.setText(_translate("MainWindow", "التدوير"))
        self.but_t_60.setToolTip(_translate("MainWindow", "<html><head/><body><p>90درجة</p></body></html>"))
        self.but_t_60.setText(_translate("MainWindow", ">"))
        self.but_t_90.setToolTip(_translate("MainWindow", "<html><head/><body><p>-90درجة</p></body></html>"))
        self.but_t_90.setText(_translate("MainWindow", "<"))
        self.but_t_remov.setToolTip(_translate("MainWindow", "<html><head/><body><p>حذف العناصر المحددة</p></body></html>"))
        self.but_t_addrect.setToolTip(_translate("MainWindow", "<html><head/><body><p>اضافة مربع</p></body></html>"))
        self.but_t_addrect.setText(_translate("MainWindow", "مربع"))
        self.but_t_addcircu.setToolTip(_translate("MainWindow", "<html><head/><body><p>اضافة دائرة</p></body></html>"))
        self.but_t_addcircu.setText(_translate("MainWindow", "دائرة"))
        self.but_t_addimg.setToolTip(_translate("MainWindow", "<html><head/><body><p>اضافة صورة</p></body></html>"))
        self.but_t_addlin.setToolTip(_translate("MainWindow", "<html><head/><body><p>اضافة خط مستقيم</p></body></html>"))
        
        self.but_t_addimg.setText(_translate("MainWindow", "صورة"))
        self.but_t_transtext.setText(_translate("MainWindow", "تحويل النص مباشرة الى باركود"))
        self.menuFile.setTitle(_translate("MainWindow", "حول"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.label.setText(_translate("MainWindow", "صندوق الادوات"))
        self.tabWidget.setToolTip(_translate("MainWindow", "<html><head/><body><p>ولا:حدد العنصر المناسب ثم اضف التغيرات علية</p></body></html>"))
        self.but_b_color_font.setToolTip(_translate("MainWindow", "<html><head/><body><p>اختار لون الخط</p></body></html>"))
        self.but_b_color_font.setText(_translate("MainWindow", "لون النص"))
        self.but_b_type_font.setToolTip(_translate("MainWindow", "<html><head/><body><p>اختار حجم ونوع الخط</p></body></html>"))
        self.but_b_type_font.setText(_translate("MainWindow", "حجم ونوع الخط"))
        self.sp_b_spac_font.setToolTip(_translate("MainWindow", "<html><head/><body><p>حدد مساحة النص في شاشة العمل</p></body></html>"))
        self.but_b_spac_font.setText(_translate("MainWindow", "مساحة النص"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow","ادوات النص"))
        #self.tabWidget.indexOf(self.tab).setToolTip(_translate("MainWindow", "<html><head/><body><p>ادوات النص</p></body></html>"))
        self.but_b_bacglor_mod.setText(_translate("MainWindow", "لون الخلفية"))
        self.but_b_coloborder_mod.setText(_translate("MainWindow", "لون الحدود"))
        self.but_b_sizsfaf_mod.setToolTip(_translate("MainWindow", "<html><head/><body><p>اولا:اختار لون الشكل ثم حدد الشفافية</p></body></html>"))
        self.but_b_sizsfaf_mod.setText(_translate("MainWindow", "الشفافية"))
        self.sp_b_sizborder_mod.setToolTip(_translate("MainWindow", "<html><head/><body><p>ضبط حجم الحدود او border</p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "عرض الحدود:"))
        self.but_b_setborder_mod.setText(_translate("MainWindow", "ملاحظة"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "ادوات الشكل"))
        #setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow","ادوات النص"))
        self.label_6.setText(_translate("MainWindow", "تحويل النص الى باركود:"))
        self.but_b_addtext_apac_trans.setText(_translate("MainWindow", "تحويل الى باركود واضافتة"+"\n"+"الى مساحة العمل"))
        self.but_t_noshow.setText(_translate("MainWindow", "اخفاء العنصر"))
        self.but_t_show.setText(_translate("MainWindow", "اظهار العناصر المخفية"))
        self.but_b_addgroup_group.setText(_translate("MainWindow", "اضافة غلاف"))
        self.but_b_additme_group.setText(_translate("MainWindow", "اضافة العنصر الى الغلاف"))
        self.but_b_remvgroup_group.setText(_translate("MainWindow", "حذف او فك الغلاف"))
        self.but_b_note_group.setText(_translate("MainWindow", "ملاحظة"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "ادوات الغلاف"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "التحويلات"))

class NotePad(QtWidgets.QMainWindow):
	
	def __init__(self, parent=None):
		QtWidgets.QWidget.__init__(self, parent)#lambda:تضعها عند اسم الزر
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.ui.but_t_addtext.clicked.connect(self.addtext_int_spac)
		self.ui.but_b_color_font.clicked.connect(self.add_color_text)
		self.ui.but_t_addimg.clicked.connect(self.addimg)
		self.ui.but_b_type_font.clicked.connect(self.chosfont)
		self.ui.but_b_edit_font.clicked.connect(self.edit_text)
		#self.ui.but_b_spac_font.clicked.connect(self.save_img)
		self.ui.sp_b_spac_font.valueChanged.connect(self.bord_text)
		self.ui.slid_t_zom.valueChanged.connect(self.zomon1)
		self.ui.but_t_big.clicked.connect(self.zomon)
		self.ui.but_t_smll.clicked.connect(self.zomof)
		self.ui.slid_t_rote.valueChanged.connect(self.roteion)
		self.ui.but_t_90.clicked.connect(self.roteion1)
		self.ui.but_t_60.clicked.connect(self.roteion2)
		self.ui.but_t_addcircu.clicked.connect(self.add_circul)
		self.ui.but_t_addrect.clicked.connect(self.add_rect)
		self.ui.but_t_save_pdf.clicked.connect(self.selectedd)
		self.ui.but_b_addtext_apac_trans.clicked.connect(self.addbarcod)
		self.ui.but_b_sizsfaf_mod.clicked.connect(self.color_sfaf)
		self.ui.but_b_bacglor_mod.clicked.connect(self.back_color)
		self.ui.but_b_coloborder_mod.clicked.connect(self.color_border)
		self.ui.sp_b_sizborder_mod.valueChanged.connect(self.width_border)
		self.ui.sp_b_sizwidth_mod.valueChanged.connect(self.sizwidth)
		self.ui.sp_b_sizhight_mod.valueChanged.connect(self.sizhight)
		self.ui.but_t_down.clicked.connect(self.down_itm)
		self.ui.but_t_up.clicked.connect(self.up_itm)
		self.ui.but_b_backimg_mod.clicked.connect(self.addback_img)
		self.ui.but_b_setborder_mod.clicked.connect(self.notforms)
		#self.ui.but_b_setborder_mod.keyPressEvent=self.keyPressEvent
		self.ui.but_t_remov.clicked.connect(self.remove_itms)
		self.ui.but_t_show_boxtool.clicked.connect(self.sho_hid)
		self.ui.but_b_addgroup_group.clicked.connect(self.addgroup)
		self.ui.but_b_additme_group.clicked.connect(self.additem1)
		self.ui.but_b_remvgroup_group.clicked.connect(self.destory)
		self.ui.but_b_note_group.clicked.connect(self.notes)
		self.ui.but_t_addlin.clicked.connect(self.addline)
		self.ui.but_t_noshow.clicked.connect(self.shoitm)
		self.ui.but_t_show.clicked.connect(self.hiditm)
		self.ui.but_t_transtext.clicked.connect(self.addbarcod2)
		#self.ui.graphicsView.mouseMoveEventMoveEvent=self.selectedd
		self.ui.menuFile.triggered.connect(self.hel)
#######################################################################text$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
	def addtext_int_spac(self):
		tex=str(self.ui.en_t_addtext.text())
		#t=QGraphicsItem(tex)
		#s=t.setPos(100, 200)
		textItem = QGraphicsTextItem()
		textItem.color = QColor(QColor("black"))
		textItem.setFont(QFont("Segoe UI", 20))
		textItem.setDefaultTextColor(QColor("black"))
		textItem.setHtml("<b>{}</b>".format(tex))
		textItem.setTextWidth(100)
		#textItem.setToolTip("dsadasdad")
		textItem.setPos(100, 200)
		textItem.setZValue(0)
		
		f=self.ui.scene.addItem(textItem)
		#f=self.ui.scene.addText(tex)
		#f.setPos(100, 200)
		for itm in self.ui.scene.items():
			itm.setFlags(QGraphicsItem.ItemIsSelectable|QGraphicsItem.ItemIsMovable)
	def add_color_text(self):
		co_tex=QColorDialog.getColor()
		#t1=t.getRgb()
		#print(t1)
		
		itms=self.ui.scene.selectedItems()
		for itm in range(0,len(itms)):
			if type(itms[itm]) == QGraphicsTextItem:
				itms[itm].setDefaultTextColor(QColor(co_tex))
			else:message=QtWidgets.QMessageBox.information(self,'information','<FONT size=10 color=blue>اختار صندوق الادوات المناسب للعنصر</FONT>')
	def chosfont(self):
		a,ok=QFontDialog.getFont()
		itms=self.ui.scene.selectedItems()
		if ok:
			for itm in range(0,len(itms)):
				if type(itms[itm]) == QGraphicsTextItem:
					itms[itm].setFont(a)
				else:message=QtWidgets.QMessageBox.information(self,'information','<FONT size=10 color=blue>اختار صندوق الادوات المناسب للعنصر</FONT>')
	def edit_text(self):
		itms=self.ui.scene.selectedItems()
		for itm in range(0,len(itms)):
			if type(itms[itm]) == QGraphicsTextItem:
				gf=itms[itm].font()
				#gc=itms[itm].textColor()
				gw=itms[itm].textWidth()
				text, ok = QInputDialog.getText(self, 'ادخل النص', 'ادخل النص الجديد',QLineEdit.Normal,itms[itm].toPlainText())
				if ok:
					
					itms[itm].setHtml(text)
					itms[itm].setFont(gf)
					#itms[itm].setDefaultTextColor(QColor(gc))
					itms[itm].setTextWidth(gw)
				
	def bord_text(self):
		si_border=self.ui.sp_b_spac_font.value()
		itms=self.ui.scene.selectedItems()
		for itm in range(0,len(itms)):
			if type(itms[itm]) == QGraphicsTextItem:
				rt=itms[itm].textWidth()
				itms[itm].setTextWidth(si_border)
				#itms[itm].setTextWidth(rt+si_border-rt)
#######################################################################baisc tool$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
	def zomon1(self):
		itms=self.ui.scene.selectedItems()
		for itm in itms:
			d=(itm.scale())
			#self.ui.slid_t_zom.setValue(20)
		itms=self.ui.scene.selectedItems()
		for itm in itms:
			
			itm.setScale(self.ui.slid_t_zom.value())
	def zomon(self):
		itms=self.ui.scene.selectedItems()
		for itm in itms:
			d=(itm.scale())
			itm.setScale(d+0.1)
	def zomof(self):
		itms=self.ui.scene.selectedItems()
		for itm in itms:
			d=(itm.scale())
			itm.setScale(d-0.1)
	def roteion(self):
		
		itms=self.ui.scene.selectedItems()
		for itm in range(0,len(itms)):
			itms[itm].setRotation(self.ui.slid_t_rote.value())
	def roteion1(self):
		global rot
		rot+=90
		itms=self.ui.scene.selectedItems()
		for itm in range(0,len(itms)):
			itms[itm].setRotation(rot)
	def roteion2(self):
		global rot
		rot-=90
		itms=self.ui.scene.selectedItems()
		for itm in range(0,len(itms)):
			itms[itm].setRotation(rot)
	def handlePreview(self):
		# dialog = QtPrintSupport.QPrintPreviewDialog() # PyQt5
		dialog = QPrintPreviewDialog()
		dialog.paintRequested.connect(self.handlePaintRequest)
		dialog.exec_()
	def handlePaintRequest(self, printer):
		pr=QPrinter(QPrinter.HighResolution)
		pr.setPageSize(QPrinter.A4)
		pt=QPainter(pr)
		self.ui.graphicsView.render(QtGui.QPainter(printer))
	def up_itm(self):
		itms=self.ui.scene.selectedItems()
		for itm in range(0,len(itms)):
			e=itms[itm].zValue()
			itms[itm].setZValue(e+1)
	def down_itm(self):
		itms=self.ui.scene.selectedItems()
		for itm in range(0,len(itms)):
			e=itms[itm].zValue()
			itms[itm].setZValue(e-1)
	def remove_itms(self):
		itms=self.ui.scene.selectedItems()
		for itm in range(0,len(itms)):
				self.ui.scene.removeItem(itms[itm])
	def sho_hid(self):
		global sh_b
		if sh_b==0:
			self.ui.dockWidget1.show()
			self.ui.but_t_show_boxtool.setText("اخفاء صندوق الادوات")
			sh_b=1
		else:
			self.ui.dockWidget1.hide()
			sh_b=0
			self.ui.but_t_show_boxtool.setText("اظهار صندوق الادوات")
	def shoitm(self):
		itms=self.ui.scene.selectedItems()
		for itm in range(0,len(itms)):
			itms[itm].hide()
	def hiditm(self):
		itms=self.ui.scene.items()
		for itm in itms:
			itm.show()
		 
#######################################################################forms$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
	def add_circul(self):
		global tip,st_tip
		#outerCircle =QtWidgets.QGraphicsEllipseItem(90, 90, 100,100)
		outerCircle=cuircuit(0, 0, 100,100)
		outerCircle.setSelected(True)
		outerCircle.setFlag(QtWidgets.QGraphicsItem.ItemIsMovable, True)
		outerCircle.setFlag(QGraphicsItem.ItemIsSelectable, True)
		outerCircle.setZValue(0)
		outerCircle.setCursor(Qt.OpenHandCursor)
		outerCircle.setAcceptHoverEvents(True)
		outerCircle.setAcceptDrops(True)
		self.sto_tip("<class '__main__.cuircuit'>")
		if tip==0:
			tip=1
			
		outerCircle.setToolTip("circuit:"+str(tip))
		#pp=QBrush()
		#pp.setStyle("border:2px solid red")
		#outerCircle.setBrush(pp)
		#pp=QPen(Qt.black)
		#pp.setWidth(10)
		#outerCircle.setPen(pp)
		self.ui.scene.addItem(outerCircle)
	def add_rect(self):
		global tip
		rect_item =tt(50,50 , 100,100)
		#rect_item.setColor(QColor("blue"))
		rect_item.setFlag(QtWidgets.QGraphicsItem.ItemIsMovable, True)
		rect_item.setFlag(QGraphicsItem.ItemIsSelectable, True)
		rect_item.setAcceptHoverEvents(True)
		rect_item.setCursor(Qt.OpenHandCursor)
		#rect_item.setBrush(QBrush(QColor(230,190,100,200)))
		rect_item.setZValue(0)
		pp=QPen(Qt.black)
		pp.setWidth(5)
		rect_item.setPen(pp)
		#pp=QPen(QColor('blue'))
		#pp.setWidth(10)#setWidth(10)
		#rect_item.setPen(pp)
		
		self.sto_tip("<class '__main__.tt'>")
		if tip==0:
			tip=1
		rect_item.setToolTip("مربع:"+str(tip))
		self.ui.scene.addItem(rect_item)
	def bik(self):##no use
		itms=self.ui.scene.selectedItems()
		for itm in range(0,len(itms)):
			g=itms[itm].rect()
			#print(itms[itm].sceneMatrix())
			itms[itm].setRect(g.x(),g.y(),g.width()+1,g.height())
			#print(itms[itm].boundingRect())
	def addline(self):
		global tip
		line=QGraphicsLineItem(10,100,200,100)
		pp=QPen(QColor('blue'))
		pp.setWidth(10)#setWidth(10)
		line.setPen(pp)
		line.setFlag(QtWidgets.QGraphicsItem.ItemIsMovable, True)
		line.setFlag(QGraphicsItem.ItemIsSelectable, True)
		line.setAcceptHoverEvents(True)
		line.setCursor(Qt.OpenHandCursor)
		#rect_item.setBrush(QBrush(QColor(230,190,100,200)))
		line.setZValue(0)
		self.sto_tip("<class 'PyQt5.QtWidgets.QGraphicsLineItem'>")
		if tip==0:
			tip=1
		line.setToolTip("خط:"+str(tip))
		self.ui.scene.addItem(line)
	def back_color(self):
		global st_color,sto_tip,st_rect
		t=QColorDialog.getColor()
		t1=t.getRgb()
		st_color=t1
		#print(t1)
		itms=self.ui.scene.selectedItems()
		for itm in range(0,len(itms)):
			print(type(itms[itm]))
			#itms[itm].setBrush(QBrush(QColor(t)))
			#itms[itm].setDefaultTextColor(QColor(t))
			if (type(itms[itm]) == QGraphicsEllipseItem or (type(itms[itm])==QGraphicsRectItem)):
				itms[itm].setBrush(QBrush(QColor(t)))
				#itms[itm].setBrush(QBrush(QPixmap("image/logo.png")))
			#if (type(itms[itm]) != QGraphicsEllipseItem and (type(itms[itm])!=QGraphicsRectItem)):
			if (str(type(itms[itm])) ==("<class '__main__.tt'>") or str(type(itms[itm]))==("<class '__main__.cuircuit'>")):
				itms[itm].setBrush(QBrush(QColor(t)))
			if type(itms[itm])==QGraphicsItemGroup:
				p33=itms[itm].collidingItems()
				for h in p33:
					if h in st_rect:
						h.setBrush(QBrush(QColor(t)))
				
			
				
	def addback_img(self):
		global st_rect
		fileName= QtWidgets.QFileDialog.getOpenFileName(self)
		itms=self.ui.scene.selectedItems()
		for itm in range(0,len(itms)):
				#itms[itm].setDefaultTextColor(QColor(t))
			if (type(itms[itm]) == QGraphicsEllipseItem or (type(itms[itm])==QGraphicsRectItem)):
				g=itms[itm].rect()
				itms[itm].setBrush(QBrush(QPixmap(fileName[0]).scaled(g.width(),g.height())))
			if (str(type(itms[itm])) ==("<class '__main__.tt'>") or str(type(itms[itm]))==("<class '__main__.cuircuit'>")):
				g=itms[itm].rect()
				itms[itm].setBrush(QBrush(QPixmap(fileName[0]).scaled(g.width(),g.height())))
				#itms[itm].setRect(0,0,g.width(),g.height())
			if type(itms[itm])==QGraphicsItemGroup:
				p33=itms[itm].collidingItems()
				for h in p33:
					if h in st_rect:
						g=h.rect()
						h.setBrush(QBrush(QPixmap(fileName[0]).scaled(g.width(),g.height())))
						#st_rect[0].setRect(0,0,g.width(),g.height())
			
		
	def color_border(self):
		global st_rect
		t=QColorDialog.getColor()
		#t1=t.getRgb()
		#print(t1)
		itms=self.ui.scene.selectedItems()
		for itm in range(0,len(itms)):
			#itms[itm].setDefaultTextColor(QColor(t))
			if (type(itms[itm]) == QGraphicsEllipseItem or (type(itms[itm])==QGraphicsRectItem)):
				itms[itm].setPen(QPen(QColor(t),itms[itm].pen().width()))
			if (str(type(itms[itm])) ==("<class '__main__.tt'>") or str(type(itms[itm]))==("<class '__main__.cuircuit'>")):
				itms[itm].setPen(QPen(QColor(t),itms[itm].pen().width()))
			if type(itms[itm])==QGraphicsItemGroup:
				p33=itms[itm].collidingItems()
				for h in p33:
					if h in st_rect:
						g=h.rect()
						h.setPen(QPen(QColor(t),h.pen().width()))
			if type(itms[itm])==QGraphicsLineItem:
				
				#a=(t.find(",",24,30))
				#print(a)
				itms[itm].setPen(QPen(QColor(t),itms[itm].pen().width()))
	def width_border(self):
		global st_rect
		yy=self.ui.sp_b_sizborder_mod.value()
		itms=self.ui.scene.selectedItems()
		for itm in range(0,len(itms)):
			if (type(itms[itm]) == QGraphicsEllipseItem or (type(itms[itm])==QGraphicsRectItem)):
				pp=QPen(QColor(itms[itm].pen().color()))
				pp.setWidth(yy)
				itms[itm].setPen(pp)
			if (str(type(itms[itm])) ==("<class '__main__.tt'>") or str(type(itms[itm]))==("<class '__main__.cuircuit'>")):
				pp=QPen(QColor(itms[itm].pen().color()))
				pp.setWidth(yy)
				itms[itm].setPen(pp)
			if type(itms[itm])==QGraphicsItemGroup:
				p33=itms[itm].collidingItems()
				for h in p33:
					if h in st_rect:
						pp=QPen(QColor(h.pen().color()))
						pp.setWidth(yy)
						h.setPen(pp)
			if type(itms[itm])==QGraphicsLineItem:
				t=(itms[itm].boundingRect())
				pp=QPen(QColor(itms[itm].pen().color()))
				pp.setWidth(yy)
				itms[itm].setPen(pp)
	def sizwidth(self):
		global st_rect
		yy=self.ui.sp_b_sizwidth_mod.value()
		itms=self.ui.scene.selectedItems()
		for itm in range(0,len(itms)):
			type(itms[itm])
			if (type(itms[itm]) == QGraphicsEllipseItem or (type(itms[itm])==QGraphicsRectItem)):
				g=itms[itm].rect()
				#print(itms[itm].sceneMatrix())
				itms[itm].setRect(g.x(),g.y(),g.width()+yy-g.width(),g.height())
			if (str(type(itms[itm])) ==("<class '__main__.tt'>") or str(type(itms[itm]))==("<class '__main__.cuircuit'>")):
				g=itms[itm].rect()
				#print(itms[itm].sceneMatrix())
				itms[itm].setRect(g.x(),g.y(),g.width()+yy-g.width(),g.height())
			if type(itms[itm]) == QGraphicsPixmapItem:
				
				r=itms[itm].pixmap()
				r1=itms[itm].pixmap().height()
				itms[itm].setFlag(QGraphicsItem.ItemSendsGeometryChanges,True)
				itms[itm].setPixmap(r.scaled(yy,r1,transformMode=Qt.SmoothTransformation))
			if type(itms[itm])==QGraphicsItemGroup:
				p33=itms[itm].collidingItems()
				for h in p33:
					if h in st_rect:
						g=h.rect()
						#print(itms[itm].sceneMatrix())
						h.setRect(g.x(),g.y(),g.width()+yy-g.width(),g.height())
			if type(itms[itm])==QGraphicsLineItem:
				t=(itms[itm].boundingRect())
				#a=(t.find(",",24,30))
				#print(a)
				#itms[itm].boundingRect.setRight(90)
				itms[itm].setLine(itms[itm].x(),itms[itm].y(),t.width(),yy)
				
	def sizhight(self):
		global st_rect
		yy=self.ui.sp_b_sizhight_mod.value()
		itms=self.ui.scene.selectedItems()
		for itm in range(0,len(itms)):
			if (type(itms[itm]) == QGraphicsEllipseItem or (type(itms[itm])==QGraphicsRectItem)):
				g=itms[itm].rect()
				##print(itms[itm].sceneMatrix())
				itms[itm].setRect(g.x(),g.y(),g.width(),g.height()+yy-g.height())
			if (str(type(itms[itm])) ==("<class '__main__.tt'>") or str(type(itms[itm]))==("<class '__main__.cuircuit'>")):
				g=itms[itm].rect()
				##print(itms[itm].sceneMatrix())
				itms[itm].setRect(g.x(),g.y(),g.width(),g.height()+yy-g.height())
			if type(itms[itm]) == QGraphicsPixmapItem:
				
				r=itms[itm].pixmap()
				r1=itms[itm].pixmap().width()
				itms[itm].setPixmap(r.scaled(r1,yy))
			if type(itms[itm])==QGraphicsItemGroup:
				p33=itms[itm].collidingItems()
				for h in p33:
					if h in st_rect:
						g=h.rect()
						#print(itms[itm].sceneMatrix())
						h.setRect(g.x(),g.y(),g.width(),g.height()+yy-g.height())
			if type(itms[itm])==QGraphicsLineItem:
				t=(itms[itm].boundingRect())
				#a=(t.find(",",24,30))
				#print(a)
				#itms[itm].boundingRect.setRight(90)
				itms[itm].setLine(itms[itm].x(),itms[itm].y(),yy,t.height())
	def color_sfaf(self):
		itms=self.ui.scene.selectedItems()
		for itm in range(0,len(itms)):
		#itms[itm].setDefaultTextColor(QColor(t))
			if (type(itms[itm]) == QGraphicsEllipseItem or (type(itms[itm])==QGraphicsRectItem)):
				r=(itms[itm].brush().color().getRgb())
				num,ok = QInputDialog.getInt(self,"integer input dualog","enter anumber",r[3])
				#if ok:
				for itm in range(0,len(itms)):
				#itms[itm].setDefaultTextColor(QColor(t))
					if (type(itms[itm]) == QGraphicsEllipseItem or (type(itms[itm])==QGraphicsRectItem)):
						r=(itms[itm].brush().color().getRgb())
						#t1=t.getRgb()
						itms[itm].setBrush(QBrush(QColor(r[0],r[1],r[2],num)))
						#itms[itm].setBrush(QBrush(QColor(t1[0],t1[1],t1[2],num)))
			if (str(type(itms[itm])) ==("<class '__main__.tt'>") or str(type(itms[itm]))==("<class '__main__.cuircuit'>")):
				r=(itms[itm].brush().color().getRgb())
				num,ok = QInputDialog.getInt(self,"integer input dualog","enter anumber",r[3])
				r=(itms[itm].brush().color().getRgb())

				#t1=t.getRgb()
				itms[itm].setBrush(QBrush(QColor(r[0],r[1],r[2],num)))
			if type(itms[itm])==QGraphicsItemGroup:
				p33=itms[itm].collidingItems()
				for h in p33:
					if h in st_rect:
						r=(h.brush().color().getRgb())
						
						h.setBrush(QBrush(QColor(r[0],r[1],r[2],num)))
		
	def notforms(self):
		gr="""
		تستطيع التحكم بحميع الاشكال بدون بالماوس او صندوق الادوات ماعد الخط المستقيم 
		بعض الاحيان لايعطيك الارتفاع المحدد وافضل تستخدم التكبير
		لزيادة طول الخط .
		وايضا بعد اضافة اي شكل الى القروب ثم فصلة من القروب يتم فقد التحكم بة من الماوس ماعد صندوق الادوات فقط.
		"""	
		message=QtWidgets.QMessageBox.about(self,'information',gr)
#######################################################################image$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
	def addimg(self):
		global tip
		fileName= QtWidgets.QFileDialog.getOpenFileName(self)
		#item = QGraphicsPixmapItem(QPixmap(fileName[0]))
		item=GraphicLayer(78,99,QPixmap(fileName[0]))
		item.setPos(100, 200)
		item.setZValue(0)
		item.setFlags(QGraphicsItem.ItemIsSelectable|QGraphicsItem.ItemIsMovable)
		item.setCursor(Qt.OpenHandCursor)
		self.ui.scene.clearSelection()
		self.ui.scene.addItem(item)
		item.setSelected(True)
		self.sto_tip("<class '__main__.GraphicLayer'>")
		if tip==0:
			tip=1
			
		item.setToolTip("صورة:"+str(tip))
		#fileName= QtWidgets.QFileDialog.getOpenFileName(self)
		#self.ui.en_img.setText(fileName[0])
		#item = QGraphicsPixmapItem(QPixmap(fileName[0]).scaled(50,50))
		#item.pixmap().width()+90
		#item.setPos(100, 200)
		
		
		#tt=QPixmap(fileName[0])
		#rect_item = QtWidgets.QGraphicsEllipseItem(QtCore.QRectF(0,0 , tt.width(),tt.height()))
		##rect_item.setColor(QColor("blue"))
		#rect_item.setZValue(0)
		#rect_item.setFlag(QtWidgets.QGraphicsItem.ItemIsMovable, True)
		#rect_item.setFlag(QGraphicsItem.ItemIsSelectable, True)
		#rect_item.setBrush(QBrush(QPixmap(fileName[0])))
		#rect_item.setFlags(QGraphicsItem.ItemIsSelectable|QGraphicsItem.ItemIsMovable)
		#self.ui.scene.clearSelection()
		self.ui.scene.addItem(item)
		item.setSelected(True)
#######################################################################transform$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
	def addbarcod(self):
		global tip
		te=str( self.ui.en_b_text_trans.text())
		
		d=["QR","Barcode"]
		item, ok = QInputDialog.getItem(self, "اختار","نوع الباركود", d, 0, False)
		if ok and item:
			if item=="QR":
				
				f="image/"+te+".svg"
				s = te
				url = pyqrcode.create(s)
				url.svg(f, scale = 4)
				item =GraphicLayer(78,99,QPixmap(f).scaled(50,50))
				#GraphicLayer(78,99,QPixmap(fileName[0]))
				item.setPos(100, 200)
				item.setZValue(0)
				self.sto_tip("<class '__main__.GraphicLayer'>")
				if tip==0:
					tip=1
					
				item.setToolTip("صورة:"+str(tip))
				item.setFlags(QGraphicsItem.ItemIsSelectable|QGraphicsItem.ItemIsMovable)
				item.setCursor(Qt.OpenHandCursor)
				self.ui.scene.clearSelection()
				self.ui.scene.addItem(item)
				item.setSelected(True)
			else:
				f="image/"+te+".png"
				image = treepoem.generate_barcode(
				barcode_type="code128",data=(te))
				image.convert("1").save(f)
				item =GraphicLayer(78,99,QPixmap(f).scaled(50,50))
				#GraphicLayer(78,99,QPixmap(fileName[0]))
				item.setPos(100, 200)
				item.setZValue(0)
				item.setCursor(Qt.OpenHandCursor)
				self.sto_tip("<class '__main__.GraphicLayer'>")
				if tip==0:
					tip=1
					
				item.setToolTip("صورة:"+str(tip))
				item.setFlags(QGraphicsItem.ItemIsSelectable|QGraphicsItem.ItemIsMovable)
				self.ui.scene.clearSelection()
				self.ui.scene.addItem(item)
				item.setSelected(True)
	def addbarcod2(self):
		text, ok = QInputDialog.getText(self, 'ادخل النص', 'ادخل النص الجديد',QLineEdit.Normal)
		if ok:
			d=["QR","Barcode"]
			item, ok = QInputDialog.getItem(self, "اختار","نوع الباركود", d, 0, False)
			if ok and item:
					if item=="QR":
						
						#f="image/"+te+".svg"
						url = pyqrcode.create(text)
						(s,filtre)=QFileDialog.getSaveFileName(self,"حفظ الصورة",filter="SVG(*.svg)")
						if s:
							url.svg(s+".svg", scale = 4)
						
					else:
						#f="image/"+te+".png"
						image = treepoem.generate_barcode(
						barcode_type="code128",data=(text))
						(s,filtre)=QFileDialog.getSaveFileName(self,"حفظ الصورة",filter="PNG(*.png)")
						if s:
							image.convert("1").save(s+".png")
	def coll(self):
		global p
		#itms=self.ui.scene.selectedItems()
		#for itm in range(0,len(itms)):
		#itms[itm].setDefaultTextColor(QColor(t))	
			#print(itms[itm].collidingItems())
			#r=(itms[itm].brush().color().getRgb())
			##t1=t.getRgb()
			#itms[itm].setBrush(QBrush(QColor(r[0],r[1],r[2],30)))
		itms=self.ui.scene.items()
		#for itm in range(0,len(itms)):
		for itm in itms:
			#self.ui.sm.addToGroup(itm)
			if type(itm)==QGraphicsItemGroup:
				p=itm.collidingItems()
		if len(p)>0:
			
			for h in p:
				self.ui.sm.addToGroup(h)
			#if itm.group():
				##itm.setSelected(False)
				#self.ui.sm.addToGroup(itm)
			
			#itms[itm].setPixmap(r.scaled(r1+1,6))
	def coll2(self):
		#self.ui.scene.addWidget( self.ui.en_b_text_trans)
		#self.ui.scene.clear()
		#print(self.ui.scene.width())
		itms=self.ui.scene.selectedItems()
		#button = QtWidgets.QPushButton('dummy')
		#d = self.ui.scene.addWidget((button), Qt.Window)
		#d.setFlag(QtWidgets.QGraphicsItem.ItemIgnoresTransformations)
		##d=QGraphicsProxyWidget(itms[1])
		#d.setPos(100, 200)
		#d.setSelected(True)
		#d.setZValue(0)
		#d.setFlags(QGraphicsItem.ItemIsSelectable|QGraphicsItem.ItemIsMovable)
		#d.setGeometry(QtCore.QRectF(90,90,1000,1000))
		#self.ui.scene.addItem(d)

		
		#itms=self.ui.scene.items()

		#for itm in range(0,len(itms)):
		for itm in itms:
			#if type(itm)==QGraphicsItemGroup:
			#	self.ui.scene.destroyItemGroup(itm)
			print(itm.focusItem())
			#if itm.group():
				##itm.setSelected(False)
			#if type(itm)==QGraphicsPixmapItem:
					#d=(itm.scale())
					#itm.setScale(d+0.1)
			
				# r=itm.pixmap()
				# outerCircle =QtWidgets.QGraphicsEllipseItem(0, 0, itm.pixmap().width(),itm.pixmap().height())
				# outerCircle.setSelected(True)
				# outerCircle.setFlag(QtWidgets.QGraphicsItem.ItemIsMovable, True)
				# outerCircle.setFlag(QGraphicsItem.ItemIsSelectable, True)
				# outerCircle.setBrush(QBrush(QPixmap(r)))
				# self.ui.scene.addItem(outerCircle)
				# print(itm.boundingRect().bottomRight())
	def save_img(self):
		""" Continue tracking movement while the mouse is pressed. """
		# Calculate how much the mouse has moved since the click.
		#pos =self.ui.graphicsView.scenePos()
		#d=st_rect[0].shape()
		#print(self.ui.graphicsView.grab())
		(s,filtre)=QFileDialog.getSaveFileName(self,"حفظ الصورة",filter="PNG(*.png);;JPEG(*.jpg);;BMP(*.bmp)")
		if s:
			if "png" in filtre:
				m=(".png")
			if "jpg" in filtre:
				m=".jpg" 
			if "bmp" in filtre:
				m=".bmp"
			pixmap = QPixmap(self.ui.graphicsView.grab())
		#pixmap = QPixmap(d)
			pixmap.save(s+m)
		#x = event.pos()
		#y= event.pos.y()
		#self.ui.statusbar.showMessage("The mouse is at\nQPoint(%d, %d) " %(x,y))
	def selectedd(self):
		items=("pdf","صورة")
		item, ok = QInputDialog.getItem(self, "اختيار",
		"اختار نوع الحفظ", items, 0, False)
		if ok and item:
			if item=="صورة":
				self.save_img()
			else:
				self.handlePreview()
	def sto_tip(self,g):
		global tip,st_tip
		st_tip.clear()
		itms=self.ui.scene.items()
		for itm in itms:
			print(type(itm))
			if str(type(itm))==g:
				
				st_tip.append(1)
				tip=len(st_tip)+1
#########################################################groups$$$$$$$$$$$$$#######################################3
	def addgroup(self):
		global st_rect,tip,p1,p2
		rect_item = QtWidgets.QGraphicsRectItem(QtCore.QRectF(50,50 , 100,100))
		#rect_item.setColor(QColor("blue"))
		rect_item.setFlag(QtWidgets.QGraphicsItem.ItemIsMovable, True)
		rect_item.setFlag(QGraphicsItem.ItemIsSelectable, True)
		
		#rect_item.setBrush(QBrush(QColor(230,190,100,200)))
		rect_item.setZValue(0)
		pp=QPen(Qt.black)
		pp.setWidth(10)
		rect_item.setPen(pp)
		st_rect.append(rect_item)
		self.sto_tip("<class 'PyQt5.QtWidgets.QGraphicsItemGroup'>")
		if tip==0:
			tip=1
		sm=self.ui.scene.createItemGroup([rect_item])
		sm.setFlags(QGraphicsItem.ItemIsSelectable|QGraphicsItem.ItemIsMovable)
		sm.setCursor(Qt.OpenHandCursor)
		sm.setToolTip("group:"+str(tip))
	def additem1(self):
		itms=self.ui.scene.selectedItems()
		for itm in itms:
			#print(itm)
			#self.ui.sm.addToGroup(itm)
			if type(itm)==QGraphicsItemGroup:
				p1=itm
				p2=itm.collidingItems()
				print(p2)
				if len(p2)>1:
					for h in p2:
						p1.addToGroup(h)
	def destory(self):
		global st_rect
		itms=self.ui.scene.selectedItems()
		for itm in itms:
			#print(itm)
			#self.ui.sm.addToGroup(itm)
			if type(itm)==QGraphicsItemGroup:
				p1=itm
				p2=itm.collidingItems()
				for h in p2:
					if h in st_rect:
						yr=st_rect.index(h)
						del st_rect[yr]
						self.ui.scene.removeItem(h)
						self.ui.scene.destroyItemGroup(itm)
	def notes(self):
		er="""
		الغلاف او الاطار:عبارة عن قروب تضع فية العناصر او تثبتهن,
		بعد اضافة العنصر الى القروب لا تستطيع التحكم بالعنصر الا الغلاف فقط,
		وتستطيع حذف القروب وعند ذالاك تتحكم في العناصر الموجودة.
		"""
		message=QtWidgets.QMessageBox.information(self,'information',er)
	def hel(self):
		w="""
		تم البرمجة بواسطةالمهندس سالم خميس بهيان
		"""
		message=QtWidgets.QMessageBox.information(self,'information',w)
########################################class rect##############################################
class tt(QGraphicsRectItem):

    handleTopLeft = 1
    handleTopMiddle = 2
    handleTopRight = 3
    handleMiddleLeft = 4
    handleMiddleRight = 5
    handleBottomLeft = 6
    handleBottomMiddle = 7
    handleBottomRight = 8

    handleSize = +8.0
    handleSpace = -4.0

    handleCursors = {
        handleTopLeft: Qt.SizeFDiagCursor,
        handleTopMiddle: Qt.SizeVerCursor,
        handleTopRight: Qt.SizeBDiagCursor,
        handleMiddleLeft: Qt.SizeHorCursor,
        handleMiddleRight: Qt.SizeHorCursor,
        handleBottomLeft: Qt.SizeBDiagCursor,
        handleBottomMiddle: Qt.SizeVerCursor,
        handleBottomRight: Qt.SizeFDiagCursor,
    }

    def __init__(self, *args):
        """
        Initialize the shape.
        """
        super().__init__(*args)
        self.handles = {}
        self.handleSelected = None
        self.mousePressPos = None
        self.mousePressRect = None
        self.setAcceptHoverEvents(True)
        self.setFlag(QGraphicsItem.ItemIsMovable, True)
        self.setFlag(QGraphicsItem.ItemIsSelectable, True)
        self.setFlag(QGraphicsItem.ItemSendsGeometryChanges, True)
        self.setFlag(QGraphicsItem.ItemIsFocusable, True)
        self.setBrush(QBrush(QColor(255, 0, 0, 100)))
        self.setPen(QPen(QColor(0, 0, 0), 1.0, Qt.SolidLine))
        self.updateHandlesPos()

    def handleAt(self, point):
        """
        Returns the resize handle below the given point.
        """
        for k, v, in self.handles.items():
            if v.contains(point):
                return k
        return None

    def hoverMoveEvent(self, moveEvent):
        """
        Executed when the mouse moves over the shape (NOT PRESSED).
        """
        if self.isSelected():
            #self.mousePressPos=mouseEvent.pos()
            handle = self.handleAt(moveEvent.pos())
            cursor = Qt.ArrowCursor if handle is None else self.handleCursors[handle]
            self.setCursor(cursor)
        super().hoverMoveEvent(moveEvent)

    def hoverLeaveEvent(self, moveEvent):
        """
        Executed when the mouse leaves the shape (NOT PRESSED).
        """
        
        self.setCursor(Qt.ArrowCursor)
        super().hoverLeaveEvent(moveEvent)
        #self.handles[0].hide()
        #if self.isSelected():
		#	pass
    def mousePressEvent(self, mouseEvent):
        """
        Executed when the mouse is pressed on the item.
        """
        self.handleSelected = self.handleAt(mouseEvent.pos())
        if self.handleSelected:
            self.mousePressPos = mouseEvent.pos()
            self.mousePressRect = self.boundingRect()
        super().mousePressEvent(mouseEvent)

    def mouseMoveEvent(self, mouseEvent):
        """
        Executed when the mouse is being moved over the item while being pressed.
        """
        #if self.isSelected():
        #    self.mousePressPos=mouseEvent.pos()
        if self.handleSelected is not None:
            self.interactiveResize(mouseEvent.pos())
        else:
            super().mouseMoveEvent(mouseEvent)

    def mouseReleaseEvent(self, mouseEvent):
        """
        Executed when the mouse is released from the item.
        """
        super().mouseReleaseEvent(mouseEvent)
        self.handleSelected = None
        self.mousePressPos = None
        self.mousePressRect = None
        self.update()

    def boundingRect(self):
        """
        Returns the bounding rect of the shape (including the resize handles).
        """
        o = self.handleSize + self.handleSpace
        return self.rect().adjusted(-o, -o, o, o)

    def updateHandlesPos(self):
        """
        Update current resize handles according to the shape size and position.
        """
        s = self.handleSize
        b = self.boundingRect()
        self.handles[self.handleTopLeft] = QRectF(b.left(), b.top(), s, s)
        self.handles[self.handleTopMiddle] = QRectF(b.center().x() - s / 2, b.top(), s, s)
        self.handles[self.handleTopRight] = QRectF(b.right() - s, b.top(), s, s)
        self.handles[self.handleMiddleLeft] = QRectF(b.left(), b.center().y() - s / 2, s, s)
        self.handles[self.handleMiddleRight] = QRectF(b.right() - s, b.center().y() - s / 2, s, s)
        self.handles[self.handleBottomLeft] = QRectF(b.left(), b.bottom() - s, s, s)
        self.handles[self.handleBottomMiddle] = QRectF(b.center().x() - s / 2, b.bottom() - s, s, s)
        self.handles[self.handleBottomRight] = QRectF(b.right() - s, b.bottom() - s, s, s)

    def interactiveResize(self, mousePos):
        """
        Perform shape interactive resize.
        """
        offset = self.handleSize + self.handleSpace
        boundingRect = self.boundingRect()
        rect = self.rect()
        diff = QPointF(0, 0)

        self.prepareGeometryChange()

        if self.handleSelected == self.handleTopLeft:

            fromX = self.mousePressRect.left()
            fromY = self.mousePressRect.top()
            toX = fromX + mousePos.x() - self.mousePressPos.x()
            toY = fromY + mousePos.y() - self.mousePressPos.y()
            diff.setX(toX - fromX)
            diff.setY(toY - fromY)
            boundingRect.setLeft(toX)
            boundingRect.setTop(toY)
            rect.setLeft(boundingRect.left() + offset)
            rect.setTop(boundingRect.top() + offset)
            self.setRect(rect)

        elif self.handleSelected == self.handleTopMiddle:

            fromY = self.mousePressRect.top()
            toY = fromY + mousePos.y() - self.mousePressPos.y()
            diff.setY(toY - fromY)
            boundingRect.setTop(toY)
            rect.setTop(boundingRect.top() + offset)
            self.setRect(rect)

        elif self.handleSelected == self.handleTopRight:

            fromX = self.mousePressRect.right()
            fromY = self.mousePressRect.top()
            toX = fromX + mousePos.x() - self.mousePressPos.x()
            toY = fromY + mousePos.y() - self.mousePressPos.y()
            diff.setX(toX - fromX)
            diff.setY(toY - fromY)
            boundingRect.setRight(toX)
            boundingRect.setTop(toY)
            rect.setRight(boundingRect.right() - offset)
            rect.setTop(boundingRect.top() + offset)
            self.setRect(rect)

        elif self.handleSelected == self.handleMiddleLeft:

            fromX = self.mousePressRect.left()
            toX = fromX + mousePos.x() - self.mousePressPos.x()
            diff.setX(toX - fromX)
            boundingRect.setLeft(toX)
            rect.setLeft(boundingRect.left() + offset)
            self.setRect(rect)

        elif self.handleSelected == self.handleMiddleRight:
            print("MR")
            fromX = self.mousePressRect.right()
            toX = fromX + mousePos.x() - self.mousePressPos.x()
            diff.setX(toX - fromX)
            boundingRect.setRight(toX)
            rect.setRight(boundingRect.right() - offset)
            self.setRect(rect)

        elif self.handleSelected == self.handleBottomLeft:

            fromX = self.mousePressRect.left()
            fromY = self.mousePressRect.bottom()
            toX = fromX + mousePos.x() - self.mousePressPos.x()
            toY = fromY + mousePos.y() - self.mousePressPos.y()
            diff.setX(toX - fromX)
            diff.setY(toY - fromY)
            boundingRect.setLeft(toX)
            boundingRect.setBottom(toY)
            rect.setLeft(boundingRect.left() + offset)
            rect.setBottom(boundingRect.bottom() - offset)
            self.setRect(rect)

        elif self.handleSelected == self.handleBottomMiddle:

            fromY = self.mousePressRect.bottom()
            toY = fromY + mousePos.y() - self.mousePressPos.y()
            diff.setY(toY - fromY)
            boundingRect.setBottom(toY)
            rect.setBottom(boundingRect.bottom() - offset)
            self.setRect(rect)

        elif self.handleSelected == self.handleBottomRight:

            fromX = self.mousePressRect.right()
            fromY = self.mousePressRect.bottom()
            toX = fromX + mousePos.x() - self.mousePressPos.x()
            toY = fromY + mousePos.y() - self.mousePressPos.y()
            diff.setX(toX - fromX)
            diff.setY(toY - fromY)
            boundingRect.setRight(toX)
            boundingRect.setBottom(toY)
            rect.setRight(boundingRect.right() - offset)
            rect.setBottom(boundingRect.bottom() - offset)
            self.setRect(rect)

        self.updateHandlesPos()

    #def shape(self):
        """
        Returns the shape of this item as a QPainterPath in local coordinates.
        """
        #path = QPainterPath()
        #path.addRect(self.rect())
        #if self.isSelected():
         #   for shape in self.handles.values():
         #       path.addEllipse(shape)
        #return path

    def paint(self, painter, option, widget=None):
        """
        Paint the node in the graphic view.
        """
        #option.state &= ~QStyle.State_Selected
        super().paint(painter, option, widget)
        painter.setBrush(QBrush(QColor("blue")))
        painter.setPen(QPen(QColor(0, 0, 0), 1.0, Qt.SolidLine))
        painter.setPen(QPen(QColor(0, 0, 0), 1.0, Qt.SolidLine))
        #painter.drawEllipse(self.rect())
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setBrush(QBrush(QColor(255, 0, 0, 255)))
        painter.setPen(QPen(QColor(0, 0, 0, 255), 1.0, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
        for handle, rect in self.handles.items():
            if handle == self.handleSelected:
                painter.drawEllipse(rect)
    def contextMenuEvent(self, event):
        menu =QtWidgets.QMenu()
        color_action = menu.addAction("تغيير لون الخلفية")
        color_action2 = menu.addAction("تغيير لون الحدود")
        color_action3 = menu.addAction("اضافة صورة للخلفية")
        selected_action = menu.exec_(event.screenPos())
        if selected_action == color_action:
            color = QtWidgets.QColorDialog.getColor()
            self.setBrush(QBrush(color))
        if selected_action == color_action2:
            color = QtWidgets.QColorDialog.getColor()
            self.setPen(QPen(QColor(color)))
        if selected_action == color_action3:
            fileName= QtWidgets.QFileDialog.getOpenFileName()
            g=self.rect()
            d=QPixmap(fileName[0])
            g1=d.width()
            g2=d.height()
            #self.setRect(0,0,self.x(),self.y())
            self.setBrush(QBrush(QPixmap(fileName[0])))
########################################class cuirtct###########################################3
class cuircuit(QGraphicsEllipseItem):

    handleTopLeft = 1
    handleTopMiddle = 2
    handleTopRight = 3
    handleMiddleLeft = 4
    handleMiddleRight = 5
    handleBottomLeft = 6
    handleBottomMiddle = 7
    handleBottomRight = 8

    handleSize = +8.0
    handleSpace = -4.0

    handleCursors = {
        handleTopLeft: Qt.SizeFDiagCursor,
        handleTopMiddle: Qt.SizeVerCursor,
        handleTopRight: Qt.SizeBDiagCursor,
        handleMiddleLeft: Qt.SizeHorCursor,
        handleMiddleRight: Qt.SizeHorCursor,
        handleBottomLeft: Qt.SizeBDiagCursor,
        handleBottomMiddle: Qt.SizeVerCursor,
        handleBottomRight: Qt.SizeFDiagCursor,
    }

    def __init__(self, *args):
        """
        Initialize the shape.
        """
        super().__init__(*args)
        self.handles = {}
        self.handleSelected = None
        self.mousePressPos = None
        self.mousePressRect = None
        self.setAcceptHoverEvents(True)
        self.setFlag(QGraphicsItem.ItemIsMovable, True)
        self.setFlag(QGraphicsItem.ItemIsSelectable, True)
        self.setFlag(QGraphicsItem.ItemSendsGeometryChanges, True)
        self.setFlag(QGraphicsItem.ItemIsFocusable, True)
        self.setBrush(QBrush(QColor(255, 0, 0, 100)))
        self.setPen(QPen(QColor(0, 0, 0), 1.0, Qt.SolidLine))
        self.updateHandlesPos()

    def handleAt(self, point):
        """
        Returns the resize handle below the given point.
        """
        for k, v, in self.handles.items():
            if v.contains(point):
                return k
        return None

    def hoverMoveEvent(self, moveEvent):
        """
        Executed when the mouse moves over the shape (NOT PRESSED).
        """
        if self.isSelected():
            #self.mousePressPos=mouseEvent.pos()
            handle = self.handleAt(moveEvent.pos())
            cursor = Qt.ArrowCursor if handle is None else self.handleCursors[handle]
            self.setCursor(cursor)
        super().hoverMoveEvent(moveEvent)

    def hoverLeaveEvent(self, moveEvent):
        """
        Executed when the mouse leaves the shape (NOT PRESSED).
        """
        
        self.setCursor(Qt.ArrowCursor)
        super().hoverLeaveEvent(moveEvent)
        #self.handles[0].hide()
        #if self.isSelected():
		#	pass
    def mousePressEvent(self, mouseEvent):
        """
        Executed when the mouse is pressed on the item.
        """
        self.handleSelected = self.handleAt(mouseEvent.pos())
        if self.handleSelected:
            self.mousePressPos = mouseEvent.pos()
            self.mousePressRect = self.boundingRect()
        super().mousePressEvent(mouseEvent)

    def mouseMoveEvent(self, mouseEvent):
        """
        Executed when the mouse is being moved over the item while being pressed.
        """
        #if self.isSelected():
        #    self.mousePressPos=mouseEvent.pos()
        if self.handleSelected is not None:
            self.interactiveResize(mouseEvent.pos())
        else:
            super().mouseMoveEvent(mouseEvent)

    def mouseReleaseEvent(self, mouseEvent):
        """
        Executed when the mouse is released from the item.
        """
        super().mouseReleaseEvent(mouseEvent)
        self.handleSelected = None
        self.mousePressPos = None
        self.mousePressRect = None
        self.update()

    def boundingRect(self):
        """
        Returns the bounding rect of the shape (including the resize handles).
        """
        o = self.handleSize + self.handleSpace
        return self.rect().adjusted(-o, -o, o, o)

    def updateHandlesPos(self):
        """
        Update current resize handles according to the shape size and position.
        """
        s = self.handleSize
        b = self.boundingRect()
        self.handles[self.handleTopLeft] = QRectF(b.left(), b.top(), s, s)
        self.handles[self.handleTopMiddle] = QRectF(b.center().x() - s / 2, b.top(), s, s)
        self.handles[self.handleTopRight] = QRectF(b.right() - s, b.top(), s, s)
        self.handles[self.handleMiddleLeft] = QRectF(b.left(), b.center().y() - s / 2, s, s)
        self.handles[self.handleMiddleRight] = QRectF(b.right() - s, b.center().y() - s / 2, s, s)
        self.handles[self.handleBottomLeft] = QRectF(b.left(), b.bottom() - s, s, s)
        self.handles[self.handleBottomMiddle] = QRectF(b.center().x() - s / 2, b.bottom() - s, s, s)
        self.handles[self.handleBottomRight] = QRectF(b.right() - s, b.bottom() - s, s, s)

    def interactiveResize(self, mousePos):
        """
        Perform shape interactive resize.
        """
        offset = self.handleSize + self.handleSpace
        boundingRect = self.boundingRect()
        rect = self.rect()
        diff = QPointF(0, 0)

        self.prepareGeometryChange()

        if self.handleSelected == self.handleTopLeft:

            fromX = self.mousePressRect.left()
            fromY = self.mousePressRect.top()
            toX = fromX + mousePos.x() - self.mousePressPos.x()
            toY = fromY + mousePos.y() - self.mousePressPos.y()
            diff.setX(toX - fromX)
            diff.setY(toY - fromY)
            boundingRect.setLeft(toX)
            boundingRect.setTop(toY)
            rect.setLeft(boundingRect.left() + offset)
            rect.setTop(boundingRect.top() + offset)
            self.setRect(rect)

        elif self.handleSelected == self.handleTopMiddle:

            fromY = self.mousePressRect.top()
            toY = fromY + mousePos.y() - self.mousePressPos.y()
            diff.setY(toY - fromY)
            boundingRect.setTop(toY)
            rect.setTop(boundingRect.top() + offset)
            self.setRect(rect)

        elif self.handleSelected == self.handleTopRight:

            fromX = self.mousePressRect.right()
            fromY = self.mousePressRect.top()
            toX = fromX + mousePos.x() - self.mousePressPos.x()
            toY = fromY + mousePos.y() - self.mousePressPos.y()
            diff.setX(toX - fromX)
            diff.setY(toY - fromY)
            boundingRect.setRight(toX)
            boundingRect.setTop(toY)
            rect.setRight(boundingRect.right() - offset)
            rect.setTop(boundingRect.top() + offset)
            self.setRect(rect)

        elif self.handleSelected == self.handleMiddleLeft:

            fromX = self.mousePressRect.left()
            toX = fromX + mousePos.x() - self.mousePressPos.x()
            diff.setX(toX - fromX)
            boundingRect.setLeft(toX)
            rect.setLeft(boundingRect.left() + offset)
            self.setRect(rect)

        elif self.handleSelected == self.handleMiddleRight:
            print("MR")
            fromX = self.mousePressRect.right()
            toX = fromX + mousePos.x() - self.mousePressPos.x()
            diff.setX(toX - fromX)
            boundingRect.setRight(toX)
            rect.setRight(boundingRect.right() - offset)
            self.setRect(rect)

        elif self.handleSelected == self.handleBottomLeft:

            fromX = self.mousePressRect.left()
            fromY = self.mousePressRect.bottom()
            toX = fromX + mousePos.x() - self.mousePressPos.x()
            toY = fromY + mousePos.y() - self.mousePressPos.y()
            diff.setX(toX - fromX)
            diff.setY(toY - fromY)
            boundingRect.setLeft(toX)
            boundingRect.setBottom(toY)
            rect.setLeft(boundingRect.left() + offset)
            rect.setBottom(boundingRect.bottom() - offset)
            self.setRect(rect)

        elif self.handleSelected == self.handleBottomMiddle:

            fromY = self.mousePressRect.bottom()
            toY = fromY + mousePos.y() - self.mousePressPos.y()
            diff.setY(toY - fromY)
            boundingRect.setBottom(toY)
            rect.setBottom(boundingRect.bottom() - offset)
            self.setRect(rect)

        elif self.handleSelected == self.handleBottomRight:

            fromX = self.mousePressRect.right()
            fromY = self.mousePressRect.bottom()
            toX = fromX + mousePos.x() - self.mousePressPos.x()
            toY = fromY + mousePos.y() - self.mousePressPos.y()
            diff.setX(toX - fromX)
            diff.setY(toY - fromY)
            boundingRect.setRight(toX)
            boundingRect.setBottom(toY)
            rect.setRight(boundingRect.right() - offset)
            rect.setBottom(boundingRect.bottom() - offset)
            self.setRect(rect)

        self.updateHandlesPos()

    #def shape(self):
        """
        Returns the shape of this item as a QPainterPath in local coordinates.
        """
        #path = QPainterPath()
        #path.addRect(self.rect())
        #if self.isSelected():
         #   for shape in self.handles.values():
         #       path.addEllipse(shape)
        #return path

    def paint(self, painter, option, widget=None):
        """
        Paint the node in the graphic view.
        """
        #option.state &= ~QStyle.State_Selected
        super().paint(painter, option, widget)
        painter.setBrush(QBrush(QColor("blue")))
        painter.setPen(QPen(QColor(0, 0, 0), 1.0, Qt.SolidLine))
        painter.setPen(QPen(QColor(0, 0, 0), 1.0, Qt.SolidLine))
        #painter.drawEllipse(self.rect())
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setBrush(QBrush(QColor(255, 0, 0, 255)))
        painter.setPen(QPen(QColor(0, 0, 0, 255), 1.0, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
        for handle, rect in self.handles.items():
            if handle == self.handleSelected:
                painter.drawEllipse(rect)
    def contextMenuEvent(self, event):
        menu =QtWidgets.QMenu()
        color_action = menu.addAction("تغيير لون الخلفية")
        color_action2 = menu.addAction("تغيير لون الحدود")
        color_action3 = menu.addAction("اضافة صورة للخلفية")
        selected_action = menu.exec_(event.screenPos())
        if selected_action == color_action:
            color = QtWidgets.QColorDialog.getColor()
            self.setBrush(QBrush(color))
        if selected_action == color_action2:
            color = QtWidgets.QColorDialog.getColor()
            self.setPen(QPen(QColor(color)))
        if selected_action == color_action3:
            fileName= QtWidgets.QFileDialog.getOpenFileName()
            g=self.rect()
            d=QPixmap(fileName[0])
            g1=d.width()
            g2=d.height()
            #self.setRect(0,0,self.x(),self.y())
            self.setBrush(QBrush(QPixmap(fileName[0])))
        
################################################img#################################################################################################3
class Resizer(QGraphicsObject):
	resizeSignal = pyqtSignal(QGraphicsItem.GraphicsItemChange,QPointF)
	def __init__(self,rect = QRectF(0,0,10,10),parent=None):
		super().__init__(parent)
		self.setFlag(QGraphicsItem.ItemIsMovable,True)
		self.setFlag(QGraphicsItem.ItemIsSelectable,True)
		self.setFlag(QGraphicsItem.ItemSendsGeometryChanges,True)
		self.setCursor(Qt.SizeFDiagCursor)
		self.rect = rect
		self.hide()

	def boundingRect(self):
		return self.rect

	def paint(self,painter,option,widget=None):
		if self.isSelected():
			#pen = QPen()
			#pen.setStyle(Qt.DotLine)
			painter.setPen(QPen(QColor('blue')))
			painter.setRenderHint(QPainter.Antialiasing)
		painter.drawEllipse(self.rect)
		self.update()

	def itemChange(self,change,value):
		self.prepareGeometryChange()
		if change == QGraphicsItem.ItemPositionChange:
			if self.isSelected():
				self.resizeSignal.emit(change,self.pos())
		return super(Resizer,self).itemChange(change,value)

	'''END CLASS'''

class GraphicLayer(QGraphicsPixmapItem):
	def __init__(self,top_left_x,top_left_y,graphic,rect=QRectF(0,0,100,100),parent=None,scene=None):
		super().__init__(parent=parent)
		self.rect = rect
		self.setPixmap(graphic)
		self.graphic = graphic
		self.mousePressPos = None
		self.mousePressRect = None
		self.setAcceptHoverEvents(True)
		self.setFlag(QGraphicsItem.ItemIsMovable,True)
		self.setFlag(QGraphicsItem.ItemIsSelectable,True)
		self.setFlag(QGraphicsItem.ItemSendsGeometryChanges,True)
		self.setFlag(QGraphicsItem.ItemIsFocusable,True)
		self.setPos(top_left_x,top_left_y)

		# Resizer actions
		self.resizer = Resizer(parent=self)
		r_width = self.resizer.boundingRect().width() - 2
		self.r_offset = QPointF(r_width,r_width)
		self.resizer.setPos(self.boundingRect().bottomRight()-self.r_offset)
		self.resizer.resizeSignal.connect(self.resize)

	def set_tag(self,item_id):
		self.tag = item_id

	def get_tag(self):
		return self.tag

	def hoverMoveEvent(self,event):
		if self.isSelected():
			self.resizer.show()
		else:
			self.resizer.hide()

	def hoverLeave(self,event):
		self.resizer.hide()


	def resize(self,change,value):
		pixmap = self.graphic.scaled(value.x(),value.y(),transformMode=Qt.SmoothTransformation)
		self.setPixmap(pixmap)
		self.prepareGeometryChange()
		self.update()

	"""END OF CLASS"""
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    myapp = NotePad()
    st="""
    QWidget{font-family:KacstQurn,Suruma;}
    QPushButton{border-radius:10px;font-family:KacstFarsi;border:2px solid #624B4B;background-color:#BDBDBD;font-size:20px;}
	QPushButton:hover{background-color:#FFFFFF;border:2px solid green;color:#495370;font-size:15px;}
    QLineEdit{background-color:#FFFFFF;font-size:20px;border-radius:5px;border:2px solid #624B4B;}
		QLineEdit:hover{background-color:#97DE94;color:black;border:2px solid #624B4B;}
		QToolButton{font-family:KacstFarsi;border-radius:10px;border:2px solid #624B4B;background-color:#BDBDBD;font-size:20px;}
		QToolButton:hover{background-color:#FFFFFF;border:2px solid green;color:#495370;font-size:15px;}
		QComboBox{background-color:white;font-size:13px;border-radius:5px;border:2px solid white;}
		QListWidget:hover{background-color:#97DE94;color:white;border:2px solid #588C56;}
		QListWidget{border:2px solid #624B4B;font-size:13px;}
		QTextEdit{background-color:#EADBBC;}
		
		QLabel{border-radius:5px;border:2px solid #624B4B;}
		QMenu{border-radius:5px;border:2px solid white;}
		QMenuBar{border-radius:5px;border:2px solid #624B4B;}
		QMenuBar:hover{border-radius:5px;border:2px ridge red;background-color:#7fb0b7;}
    """
    app.setStyleSheet(st)
myapp.show()
sys.exit(app.exec_())

