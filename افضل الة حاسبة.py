#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  lern lue.py
#  
#  Copyright 2020 salemphyan <@salemlaptop>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
"""
programmer by en:salem khmes phyan
"""
import sys
from PyQt5 import QtCore, QtWidgets
app=QtWidgets.QApplication(sys.argv)    
w=QtWidgets.QWidget()  
st="""QWidget{background:#262D37;}
"""
app.setStyleSheet(st)
txt1=QtWidgets.QTextBrowser(w)
txt1.setStyleSheet("color:white;")
txt2=QtWidgets.QLineEdit(w)
txt2.setStyleSheet("color:white;")
but1=QtWidgets.QPushButton(w)
but1.setText("1")
but1.setProperty('name','but1')
s='''QPushButton{background-color:green;padding:2px;margin:5px;font-size:24px;border-radius:5px;}
QPushButton:hover{background-color:red;}'''
#but1.setStyleSheet("background-color:green;border:2px solid #fff;")
but1.setStyleSheet(s)
but2=QtWidgets.QPushButton(w)
but2.setText("2")
but2.setProperty('name','but2')
but2.setStyleSheet(s)
but3=QtWidgets.QPushButton(w)
but3.setText("3")
but3.setProperty('name','but3')
but3.setStyleSheet(s)

but4=QtWidgets.QPushButton(w)
but4.setText("4")

but4.setStyleSheet(s)
but5=QtWidgets.QPushButton(w)
but5.setText("5")
but5.setStyleSheet(s)
but6=QtWidgets.QPushButton(w)
but6.setText("6")
but7=QtWidgets.QPushButton(w)
but7.setText("7")
but8=QtWidgets.QPushButton(w)
but8.setText("8")
but9=QtWidgets.QPushButton(w)
but9.setText("9")
but0=QtWidgets.QPushButton(w)
but0.setText("0")
bls=QtWidgets.QPushButton(w)
bls.setText("+")
myns=QtWidgets.QPushButton(w)
myns.setText("-")
drb=QtWidgets.QPushButton(w)
drb.setText("*")
div=QtWidgets.QPushButton(w)
div.setText("/")
equl=QtWidgets.QPushButton(w)
equl.setText("=")
dele=QtWidgets.QPushButton(w)
dele.setText("C")
clo=QtWidgets.QPushButton(w)
clo.setText("اغلاق")
##################
but6.setStyleSheet(s)
but7.setStyleSheet(s)
but8.setStyleSheet(s)
but9.setStyleSheet(s)
but0.setStyleSheet(s)
bls.setStyleSheet(s)
myns.setStyleSheet(s)
drb.setStyleSheet(s)
div.setStyleSheet(s)
equl.setStyleSheet(s)
dele.setStyleSheet(s)
clo.setStyleSheet(s)
###########################  
  
fbox=QtWidgets.QFormLayout()
fbox.addRow(txt1)
fbox.addRow(txt2)
#vbox=QtWidgets.QVBoxLayout()
#vbox.addWidget(txt1) 
#vbox.addWidget(txt2)
hbox1=QtWidgets.QHBoxLayout()

hbox1.addWidget(but1)
hbox1.addWidget(but2)
hbox1.addWidget(but3)
fbox.addRow(hbox1)

hbox2=QtWidgets.QHBoxLayout()

hbox2.addWidget(but4)
hbox2.addWidget(but5)
hbox2.addWidget(but6)
fbox.addRow(hbox2)

hbox3=QtWidgets.QHBoxLayout()

hbox3.addWidget(but7)
hbox3.addWidget(but8)
hbox3.addWidget(but9)

fbox.addRow(hbox3)
hbox4=QtWidgets.QHBoxLayout()

hbox4.addWidget(but0)
hbox4.addWidget(bls)
hbox4.addWidget(myns)
fbox.addRow(hbox4)

hbox5=QtWidgets.QHBoxLayout()

hbox5.addWidget(drb)
hbox5.addWidget(div)
hbox5.addWidget(dele)
fbox.addRow(hbox5)

hbox6=QtWidgets.QHBoxLayout()

hbox6.addWidget(equl)
hbox6.addWidget(clo)
fbox.addRow(hbox6)
def show1(v):
	s=txt2.text()
	txt2.setText(s+v)
but1.clicked.connect(lambda : show1("1"))
but2.clicked.connect(lambda : show1("2"))
but3.clicked.connect(lambda : show1("3"))
but4.clicked.connect(lambda : show1("4"))
but5.clicked.connect(lambda : show1("5"))
but6.clicked.connect(lambda : show1("6"))
but7.clicked.connect(lambda : show1("7"))
but8.clicked.connect(lambda : show1("8"))
but9.clicked.connect(lambda : show1("9"))
but0.clicked.connect(lambda : show1("0"))
bls.clicked.connect(lambda : show1("+"))
myns.clicked.connect(lambda : show1("-"))
drb.clicked.connect(lambda : show1("*"))
div.clicked.connect(lambda : show1("/"))



def ex():
	exit()
clo.clicked.connect(ex)

def delee():
	txt2.clear()
dele.clicked.connect(delee)

def eq():
	try:
			text=txt2.text()
			txt1.append("%s = <font color=blue><b>%s</b><f/ont>" % (text, eval(text)))
	except:
			txt1.append("<font color=red>%s is invalid!</font>" % text)	

txt2.returnPressed.connect(eq)
equl.clicked.connect(eq)
   
#w.setLayout(vbox)
w.setLayout(fbox)    
w.resize(250,250)
w.show()
sys.exit(app.exec_())

    

