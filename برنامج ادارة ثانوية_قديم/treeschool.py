################################################################################                                                                                
#   Copyright (c) 2019-2020 Administrating School data Software Foundation     #                    #                                  
#    All Rights Reserved.                                                      #                     #
#                                                                              #
#                             @@@@                                             #   #
#                                 @@                                           # #
#                             @@@@@@                                           #  #
#                            @ @ @ @                                           #  #
#                            @ @@@                                             #   #
#                                                                              #
#                                                                              #
#                                                                              #
################################################################################


from tkinter import *
from tkinter import ttk
from sql3 import DBschool
dbSchool=DBschool()
class ListTicket:
    def __init__(self):
        self._root=Tk()
        self._dbSchool=DBschool()
        scrollbar = Scrollbar(self._root)
        scrollbar.pack( side = RIGHT, fill=Y )
        scroll= Scrollbar(self._root)
        scroll.pack( side =BOTTOM, fill=X )
        tv=ttk.Treeview(self._root,yscrollcommand = scrollbar.set,xscrollcommand=scroll.set)
        tv.pack(fill=BOTH)
        tv.heading('#0',text='ID')
        tv.configure(column=('#Name','#Number','#grade','#qran','#islamy','#englis','#arbic','#maths','#ahaya','#kimia','#visia','#gravea','#date','#majtmh','#total','#relatd'))
        tv.heading('#Name',text='اسم الطالب')
        tv.heading('#Number',text='رقم الطالب')
        tv.heading('#grade',text='الصف')
        tv.heading('#qran',text='الفران الكريم')
        tv.heading('#islamy',text='الاسلامية')
        tv.heading('#englis',text='انجليزي')
        tv.heading('#arbic',text='اللغة العربية')
        tv.heading('#maths',text='الرياضيات')
        tv.heading('#ahaya',text='الاحياء')
        tv.heading('#kimia',text='الكيمياء')
        tv.heading('#visia',text='الفيزياء')
        tv.heading('#gravea',text='جغرافيا')
        tv.heading('#date',text='التاريخ')
        tv.heading('#majtmh',text='مجتمع')
        tv.heading('#total',text='المجموع')
        tv.heading('#relatd',text='النسبة')
        
        tv.column('#total',width=50,anchor='center')
        tv.column('#gravea',width=50,anchor='center')
        tv.column('#date',width=50,anchor='center')
        tv.column('#majtmh',width=50,anchor='center')
        tv.column('#0',width=50,anchor='center')
        tv.column('#Name',width=150,anchor='center')
        #tv.column('#Gender',width=50,anchor='center')
        tv.column('#Number',width=50,anchor='center')
        tv.column('#grade',width=70,anchor='center')
        tv.column('#qran',width=50,anchor='center')
        tv.column('#islamy',width=50,anchor='center')
        tv.column('#englis',width=50,anchor='center')
        tv.column('#arbic',width=50,anchor='center')
        tv.column('#maths',width=50,anchor='center')
        tv.column('#ahaya',width=50,anchor='center')
        tv.column('#kimia',width=50,anchor='center')
        tv.column('#visia',width=50,anchor='center')
        tv.column('#relatd',width=50,anchor='center')
        
        coursor=self._dbSchool.ListRequest()
##        coursors=self._dbconnect.mal()
        for row in coursor:#Name,Number,Grader,qran,isalamy,english,arbic,maths,ahya,kimia,veisia,gravea,date,majtmh
            tv.insert('','end','#{}'.format(row['ID']),text=row['ID'])
            tv.set('#{}'.format(row['ID']),'#Name',row['Name'])
            tv.set('#{}'.format(row['ID']),'#Number',row['Number'])#englis','#arbic','#maths','#ahaya','#kimia','#visia','#gravea','#date','#majtmh
            tv.set('#{}'.format(row['ID']),'#grade',row['Grader'])
            tv.set('#{}'.format(row['ID']),'#qran',row['qran'])
            tv.set('#{}'.format(row['ID']),'#islamy',row['isalamy'])
            tv.set('#{}'.format(row['ID']),'#englis',row['english'])
            tv.set('#{}'.format(row['ID']),'#arbic',row['arbic'])
            tv.set('#{}'.format(row['ID']),'#maths',row['maths'])
            tv.set('#{}'.format(row['ID']),'#ahaya',row['ahya'])
            tv.set('#{}'.format(row['ID']),'#kimia',row['kimia'])
            tv.set('#{}'.format(row['ID']),'#visia',row['veisia'])
            tv.set('#{}'.format(row['ID']),'#gravea',row['gravea'])
            tv.set('#{}'.format(row['ID']),'#date',row['date'])
            tv.set('#{}'.format(row['ID']),'#majtmh',row['majtmh'])
            tv.set('#{}'.format(row['ID']),'#total',row['total'])
            tv.set('#{}'.format(row['ID']),'#relatd',row['relatd'])






        scrollbar.config( command = tv.yview,orient=VERTICAL)
        scroll.config( command = tv.xview,orient=HORIZONTAL)
#ثاني علميييي######################################################################
class ListTicket2c:
    def __init__(self):
        self._root=Tk()
        self._dbSchool=DBschool()
        scrollbar = Scrollbar(self._root)
        scrollbar.pack( side = RIGHT, fill=Y )
        scroll= Scrollbar(self._root)
        scroll.pack( side =BOTTOM, fill=X )
        tv=ttk.Treeview(self._root,yscrollcommand = scrollbar.set,xscrollcommand=scroll.set)
        tv.pack(fill=BOTH)
        tv.heading('#0',text='ID')
        tv.configure(column=('#Name','#Number','#grade','#qran','#islamy','#arbic','#englis','#maths','#visia','#kimia','#ahaya','#total','#relatd'))
        tv.heading('#Name',text='اسم الطالب')
        tv.heading('#Number',text='رقم الطالب')
        tv.heading('#grade',text='الصف')
        tv.heading('#qran',text='الفران الكريم')
        tv.heading('#islamy',text='الاسلامية')
        tv.heading('#arbic',text='اللغة العربية')
        tv.heading('#englis',text='اللغة الانجليزية')
        tv.heading('#maths',text='الرياضيات')
        tv.heading('#visia',text='الفيزياء')
        tv.heading('#kimia',text='الكيمياء')
        tv.heading('#ahaya',text='الاحياء')#relatd
        tv.heading('#total',text='المجموع')
        tv.heading('#relatd',text='النسبة')
       
        tv.column('#0',width=50,anchor='center')
        tv.column('#Name',width=150,anchor='center')
        #tv.column('#Gender',width=50,anchor='center')
        tv.column('#Number',width=50,anchor='center')
        tv.column('#grade',width=70,anchor='center')
        tv.column('#qran',width=50,anchor='center')
        tv.column('#islamy',width=50,anchor='center')
        tv.column('#englis',width=50,anchor='center')
        tv.column('#arbic',width=50,anchor='center')
        tv.column('#maths',width=50,anchor='center')
        tv.column('#ahaya',width=50,anchor='center')
        tv.column('#kimia',width=50,anchor='center')
        tv.column('#visia',width=50,anchor='center')
        tv.column('#total',width=50,anchor='center')
        tv.column('#relatd',width=50,anchor='center')
        coursor=self._dbSchool.ListRequest2c()
##        coursors=self._dbconnect.mal()
        for row in coursor:#Name,Number,Grader,qran,isalamy,english,arbic,maths,ahya,kimia,veisia,gravea,date,majtmh
            tv.insert('','end','#{}'.format(row['ID']),text=row['ID'])
            tv.set('#{}'.format(row['ID']),'#Name',row['Name'])
            tv.set('#{}'.format(row['ID']),'#Number',row['Number'])#englis','#arbic','#maths','#ahaya','#kimia','#visia','#gravea','#date','#majtmh
            tv.set('#{}'.format(row['ID']),'#grade',row['Grader'])
            tv.set('#{}'.format(row['ID']),'#qran',row['qran'])
            tv.set('#{}'.format(row['ID']),'#islamy',row['isalamy'])
            tv.set('#{}'.format(row['ID']),'#arbic',row['arbic'])
            tv.set('#{}'.format(row['ID']),'#englis',row['english'])
            tv.set('#{}'.format(row['ID']),'#maths',row['maths'])
            tv.set('#{}'.format(row['ID']),'#visia',row['visia'])
            tv.set('#{}'.format(row['ID']),'#kimia',row['kimia'])
            tv.set('#{}'.format(row['ID']),'#ahaya',row['ahya'])
            tv.set('#{}'.format(row['ID']),'#total',row['total'])
            tv.set('#{}'.format(row['ID']),'#relatd',row['relatd'])





        scrollbar.config( command = tv.yview,orient=VERTICAL )
        scroll.config( command = tv.xview,orient=HORIZONTAL)
#ثالث علميي################################################################################################

class ListTicket3c:
    def __init__(self):
        self._root=Tk()
        self._dbSchool=DBschool()
        scrollbar = Scrollbar(self._root)
        scrollbar.pack( side = RIGHT, fill=Y )
        scroll= Scrollbar(self._root)
        scroll.pack( side =BOTTOM, fill=X )
        tv=ttk.Treeview(self._root,yscrollcommand = scrollbar.set,xscrollcommand=scroll.set)
        tv.pack(fill=BOTH)
        tv.heading('#0',text='ID')
        tv.configure(column=('#Name','#Number','#grade','#qran','#islamy','#arbic','#englis','#maths','#visia','#kimia','#ahaya','#total','#relatd'))
        tv.heading('#Name',text='اسم الطالب')
        tv.heading('#Number',text='رقم الطالب')
        tv.heading('#grade',text='الصف')
        tv.heading('#qran',text='الفران الكريم')
        tv.heading('#islamy',text='الاسلامية')
        tv.heading('#arbic',text='اللغة العربية')
        tv.heading('#englis',text='اللغة الانجليزية')
        tv.heading('#maths',text='الرياضيات')
        tv.heading('#visia',text='الفيزياء')
        tv.heading('#kimia',text='الكيمياء')
        tv.heading('#ahaya',text='الاحياء')
        tv.heading('#total',text='المجموع')
        tv.heading('#relatd',text='النسبة')
        tv.column('#0',width=50,anchor='center')
        tv.column('#Name',width=150,anchor='center')
        #tv.column('#Gender',width=50,anchor='center')
        tv.column('#Number',width=50,anchor='center')
        tv.column('#grade',width=70,anchor='center')
        tv.column('#qran',width=50,anchor='center')
        tv.column('#islamy',width=50,anchor='center')
        tv.column('#englis',width=50,anchor='center')
        tv.column('#arbic',width=50,anchor='center')
        tv.column('#maths',width=50,anchor='center')
        tv.column('#ahaya',width=50,anchor='center')
        tv.column('#kimia',width=50,anchor='center')
        tv.column('#visia',width=50,anchor='center')
        tv.column('#total',width=50,anchor='center')
        tv.column('#relatd',width=50,anchor='center')
        coursor=self._dbSchool.ListRequest3c()
##        coursors=self._dbconnect.mal()
        for row in coursor:#Name,Number,Grader,qran,isalamy,english,arbic,maths,ahya,kimia,veisia,gravea,date,majtmh
            tv.insert('','end','#{}'.format(row['ID']),text=row['ID'])
            tv.set('#{}'.format(row['ID']),'#Name',row['Name'])
            tv.set('#{}'.format(row['ID']),'#Number',row['Number'])#englis','#arbic','#maths','#ahaya','#kimia','#visia','#gravea','#date','#majtmh
            tv.set('#{}'.format(row['ID']),'#grade',row['Grader'])
            tv.set('#{}'.format(row['ID']),'#qran',row['qran'])
            tv.set('#{}'.format(row['ID']),'#islamy',row['isalamy'])
            tv.set('#{}'.format(row['ID']),'#arbic',row['arbic'])
            tv.set('#{}'.format(row['ID']),'#englis',row['english'])
            tv.set('#{}'.format(row['ID']),'#maths',row['maths'])
            tv.set('#{}'.format(row['ID']),'#visia',row['visia'])
            tv.set('#{}'.format(row['ID']),'#kimia',row['kimia'])
            tv.set('#{}'.format(row['ID']),'#ahaya',row['ahya'])
            tv.set('#{}'.format(row['ID']),'#total',row['total'])
            tv.set('#{}'.format(row['ID']),'#relatd',row['relatd'])





        scrollbar.config( command = tv.yview,orient=VERTICAL )
        scroll.config( command = tv.xview,orient=HORIZONTAL)
###############ثاني ادبي#####################################################################
        
class ListTicket2d:
    def __init__(self):
        self._root=Tk()
        self._dbSchool=DBschool()
        scrollbar = Scrollbar(self._root)
        scrollbar.pack( side = RIGHT, fill=Y )
        scroll= Scrollbar(self._root)
        scroll.pack( side =BOTTOM, fill=X )
        tv=ttk.Treeview(self._root,yscrollcommand = scrollbar.set,xscrollcommand=scroll.set)
        tv.pack(fill=BOTH)
        tv.heading('#0',text='ID')
        tv.configure(column=('#Name','#Number','#grade','#qran','#islamy','#arbic','#englis','#maths','#gravea','#date','#alagtsad','#alajtma','#total','#relatd'))
        tv.heading('#Name',text='اسم الطالب')
        tv.heading('#Number',text='رقم الطالب')
        tv.heading('#grade',text='الصف')
        tv.heading('#qran',text='الفران الكريم')
        tv.heading('#islamy',text='الاسلامية')
        tv.heading('#englis',text='انجليزي')
        tv.heading('#arbic',text='اللغة العربية')
        tv.heading('#maths',text='الرياضيات')
        tv.heading('#gravea',text='جغرافيا')
        tv.heading('#date',text='التاريخ')
        tv.heading('#alajtma',text='علم الاجتماع')#alagtsad','#alajtma
        tv.heading('#alagtsad',text='علم الاقتصاد')
        tv.heading('#total',text='المجموع')
        tv.heading('#relatd',text='النسبة')
        
        tv.column('#gravea',width=50,anchor='center')

        
        tv.column('#0',width=50,anchor='center')
        tv.column('#Name',width=150,anchor='center')
        #tv.column('#Gender',width=50,anchor='center')
        tv.column('#Number',width=50,anchor='center')
        tv.column('#grade',width=70,anchor='center')
        tv.column('#qran',width=50,anchor='center')
        tv.column('#islamy',width=50,anchor='center')
        tv.column('#englis',width=50,anchor='center')
        tv.column('#arbic',width=50,anchor='center')
        tv.column('#maths',width=50,anchor='center')
        tv.column('#alajtma',width=50,anchor='center')
        tv.column('#alagtsad',width=50,anchor='center')
        tv.column('#date',width=50,anchor='center')
        tv.column('#total',width=50,anchor='center')
        tv.column('#relatd',width=50,anchor='center')
        
        coursor=self._dbSchool.ListRequest2d()
##        coursors=self._dbconnect.mal()
        for row in coursor:#Name,Number,Grader,qran,isalamy,english,arbic,maths,ahya,kimia,veisia,gravea,date,majtmh
            tv.insert('','end','#{}'.format(row['ID']),text=row['ID'])
            tv.set('#{}'.format(row['ID']),'#Name',row['Name'])
            tv.set('#{}'.format(row['ID']),'#Number',row['Number'])#englis','#arbic','#maths','#ahaya','#kimia','#visia','#gravea','#date','#majtmh
            tv.set('#{}'.format(row['ID']),'#grade',row['Grader'])
            tv.set('#{}'.format(row['ID']),'#qran',row['qran'])
            tv.set('#{}'.format(row['ID']),'#islamy',row['isalamy'])
            tv.set('#{}'.format(row['ID']),'#englis',row['english'])
            tv.set('#{}'.format(row['ID']),'#arbic',row['arbic'])
            tv.set('#{}'.format(row['ID']),'#maths',row['maths'])
            tv.set('#{}'.format(row['ID']),'#gravea',row['gravea'])
            tv.set('#{}'.format(row['ID']),'#date',row['date'])
            tv.set('#{}'.format(row['ID']),'#alagtsad',row['alagtsad'])
            tv.set('#{}'.format(row['ID']),'#alajtma',row['alajtma'])
            tv.set('#{}'.format(row['ID']),'#total',row['total'])
            tv.set('#{}'.format(row['ID']),'#relatd',row['relatd'])






        scrollbar.config( command = tv.yview,orient=VERTICAL )
        scroll.config( command = tv.xview,orient=HORIZONTAL)
####################ثالث ادبي####################################
        ###############################
class ListTicket3d:
    def __init__(self):
        self._root=Tk()
        self._dbSchool=DBschool()
        scrollbar = Scrollbar(self._root)
        scrollbar.pack( side = RIGHT, fill=Y )
        scroll= Scrollbar(self._root)
        scroll.pack( side =BOTTOM, fill=X )
        tv=ttk.Treeview(self._root,yscrollcommand = scrollbar.set,xscrollcommand=scroll.set)
        tv.pack(fill=BOTH)
        tv.heading('#0',text='ID')
        tv.configure(column=('#Name','#Number','#grade','#qran','#islamy','#arbic','#englis','#gravea','#date','#logic','#maths','#total','#relatd'))
        tv.heading('#Name',text='اسم الطالب')
        tv.heading('#Number',text='رقم الطالب')
        tv.heading('#grade',text='الصف')
        tv.heading('#qran',text='الفران الكريم')
        tv.heading('#islamy',text='الاسلامية')
        tv.heading('#englis',text='انجليزي')
        tv.heading('#arbic',text='اللغة العربية')
        tv.heading('#maths',text='الرياضيات')
        tv.heading('#gravea',text='جغرافيا والخرائط')
        tv.heading('#date',text='التاريخ')
        tv.heading('#logic',text='الفلسفة والمنطق')
        tv.heading('#total',text='المجموع')
        tv.heading('#relatd',text='النسبة')#alagtsad','#alajtma
        
        
        tv.column('#gravea',width=50,anchor='center')

        
        tv.column('#0',width=50,anchor='center')
        tv.column('#Name',width=150,anchor='center')
        #tv.column('#Gender',width=50,anchor='center')
        tv.column('#Number',width=50,anchor='center')
        tv.column('#grade',width=70,anchor='center')
        tv.column('#qran',width=50,anchor='center')
        tv.column('#islamy',width=50,anchor='center')
        tv.column('#englis',width=50,anchor='center')
        tv.column('#arbic',width=50,anchor='center')
        tv.column('#maths',width=50,anchor='center')
        tv.column('#logic',width=50,anchor='center')
        tv.column('#date',width=50,anchor='center')
        tv.column('#total',width=50,anchor='center')
        tv.column('#relatd',width=50,anchor='center')
        
        coursor=self._dbSchool.ListRequest3d()
##        coursors=self._dbconnect.mal()
        for row in coursor:#Name,Number,Grader,qran,isalamy,english,arbic,maths,ahya,kimia,veisia,gravea,date,majtmh
            tv.insert('','end','#{}'.format(row['ID']),text=row['ID'])
            tv.set('#{}'.format(row['ID']),'#Name',row['Name'])
            tv.set('#{}'.format(row['ID']),'#Number',row['Number'])#englis','#arbic','#maths','#ahaya','#kimia','#visia','#gravea','#date','#majtmh
            tv.set('#{}'.format(row['ID']),'#grade',row['Grader'])
            tv.set('#{}'.format(row['ID']),'#qran',row['qran'])
            tv.set('#{}'.format(row['ID']),'#islamy',row['isalamy'])
            tv.set('#{}'.format(row['ID']),'#englis',row['english'])
            tv.set('#{}'.format(row['ID']),'#arbic',row['arbic'])
            tv.set('#{}'.format(row['ID']),'#maths',row['maths'])
            tv.set('#{}'.format(row['ID']),'#gravea',row['gravea'])
            tv.set('#{}'.format(row['ID']),'#date',row['date'])
            tv.set('#{}'.format(row['ID']),'#logic',row['logic'])
            tv.set('#{}'.format(row['ID']),'#total',row['total'])
            tv.set('#{}'.format(row['ID']),'#relatd',row['relatd'])
        






        scrollbar.config( command = tv.yview,orient=VERTICAL )
        scroll.config( command = tv.xview,orient=HORIZONTAL)        
        
        self._root.mainloop()
