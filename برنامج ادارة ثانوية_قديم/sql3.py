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

import sqlite3
class DBschool:
    def __init__(self):
        self._db=sqlite3.connect('dataschool.db')
        self._db.row_factory=sqlite3.Row
        self._db.execute('create table if not exists SC1(ID integer primary Key autoincrement, Name text,Number text,Grader text,qran text,isalamy text,english text,arbic text,maths text,ahya text,kimia text,veisia text,gravea text,date text,majtmh text,total text,relatd text)')
        self._db.commit()
        self._db.execute('create table if not exists SC2c(ID integer primary Key autoincrement, Name text,Number text,Grader text,qran text,isalamy text,arbic text,english text,maths text,visia text,kimia text,ahya text,total text,relatd text)')
        self._db.commit()
        self._db.execute('create table if not exists SC3c(ID integer primary Key autoincrement, Name text,Number text,Grader text,qran text,isalamy text,arbic text,english text,maths text,visia text,kimia text,ahya text,total text,relatd text)')
        self._db.commit()
        self._db.execute('create table if not exists SC2d(ID integer primary Key autoincrement, Name text,Number text,Grader text,qran text,isalamy text,arbic text,english text,maths text,gravea text,date text,alagtsad text,alajtma text,total text,relatd text)')
        self._db.commit()
        self._db.execute('create table if not exists SC3d(ID integer primary Key autoincrement, Name text,Number text,Grader text,qran text,isalamy text,arbic text,english text,gravea text,date text,logic text,maths text,total text,relatd text)')
        self._db.commit()
#اولى ثانوي#####################################
    def Add(self,Name,Number,Grader,qran,isalamy,english,arbic,maths,ahya,kimia,veisia,gravea,date,majtmh,total,relatd):
        self._db.execute('insert into SC1(Name,Number,Grader,qran,isalamy,english,arbic,maths,ahya,kimia,veisia,gravea,date,majtmh,total,relatd) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',(Name,Number,Grader,qran,isalamy,english,arbic,maths,ahya,kimia,veisia,gravea,date,majtmh,total,relatd))
        self._db.commit()
        return 'request is submitted'
    def deles1(self,ID):
        self._db.execute('delete from SC1 where ID={}'.format(ID))
        self._db.commit()
        return 'request is delete'

    def updats1(self,Name,ID):
        self._db.execute('update SC1 set Name=? where ID=?',(Name,ID))
##        self._db.execute('update Ticket set Comment=? where Name=?',(Comment,Name),)
        self._db.commit()
        return 'request is update'
    def ListRequest(self):
        cursor=self._db.execute('select * from SC1')#relatd
        self._db.commit()
        return cursor;
#ثاني علمي#############################################################    
    def Add2c(self,Name,Number,Grader,qran,isalamy,arbic,english,maths,visia,kimia,ahya,total,relatd):
        self._db.execute('insert into SC2c(Name,Number,Grader,qran,isalamy,arbic,english,maths,visia,kimia,ahya,total,relatd) values(?,?,?,?,?,?,?,?,?,?,?,?,?)',(Name,Number,Grader,qran,isalamy,arbic,english,maths,visia,kimia,ahya,total,relatd))
        self._db.commit()
        return 'request is submitted'
    def deles2c(self,ID):
        self._db.execute('delete from SC2c where ID={}'.format(ID))
        self._db.commit()
        return 'request is delete'

    def updats2c(self,Name,ID):
        self._db.execute('update SC2c set Name=? where ID=?',(Name,ID))
##        self._db.execute('update Ticket set Comment=? where Name=?',(Comment,Name),)
        self._db.commit()
        return 'request is update'
    def ListRequest2c(self):
        cursor=self._db.execute('select * from SC2c')
        self._db.commit()
        return cursor;

#ثالث علميي####################################################################
    def Add3c(self,Name,Number,Grader,qran,isalamy,arbic,english,maths,visia,kimia,ahya,total,relatd):
        self._db.execute('insert into SC3c(Name,Number,Grader,qran,isalamy,arbic,english,maths,visia,kimia,ahya,total,relatd) values(?,?,?,?,?,?,?,?,?,?,?,?,?)',(Name,Number,Grader,qran,isalamy,arbic,english,maths,visia,kimia,ahya,total,relatd))
        self._db.commit()
        return 'request is submitted'
    #deleet
    def deles3c(self,ID):
        self._db.execute('delete from SC3c where ID={}'.format(ID))
        self._db.commit()
        return 'request is delete'
#updattttttttttt
    def updats3c(self,Name,ID):
        self._db.execute('update SC3c set Name=? where ID=?',(Name,ID))
##        self._db.execute('update Ticket set Comment=? where Name=?',(Comment,Name),)
        self._db.commit()
        return 'request is update'    
    def ListRequest3c(self):
        cursor=self._db.execute('select * from SC3c')
        self._db.commit()
        return cursor;
#########ثاني ادبي#######################################################################3    
    def Add2d(self,Name,Number,Grader,qran,isalamy,arbic,english,maths,gravea,date,alagtsad,alajtma,total,relatd):
        self._db.execute('insert into SC2d(Name,Number,Grader,qran,isalamy,arbic,english,maths,gravea,date,alagtsad,alajtma,total,relatd) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?)',(Name,Number,Grader,qran,isalamy,arbic,english,maths,gravea,date,alagtsad,alajtma,total,relatd))
        self._db.commit()
        return 'request is submitted'
    #deleet
    def deles2d(self,ID):
        self._db.execute('delete from SC2d where ID={}'.format(ID))
        self._db.commit()
        return 'request is delete'
#updattttttttttt
    def updats2d(self,Name,ID):
        self._db.execute('update SC2d set Name=? where ID=?',(Name,ID))
##        self._db.execute('update Ticket set Comment=? where Name=?',(Comment,Name),)
        self._db.commit()
        return 'request is update'  

    def ListRequest2d(self):
        cursor=self._db.execute('select * from SC2d')
        self._db.commit()
        return cursor;
####################################################################################
############ثالث ادبي####################################################
    def Add3d(self,Name,Number,Grader,qran,isalamy,arbic,english,gravea,date,logic,maths,total,relatd):
        self._db.execute('insert into SC3d(Name,Number,Grader,qran,isalamy,arbic,english,gravea,date,logic,maths,total,relatd) values(?,?,?,?,?,?,?,?,?,?,?,?,?)',(Name,Number,Grader,qran,isalamy,arbic,english,gravea,date,logic,maths,total,relatd))
        self._db.commit()
        return 'request is submitted'
       #deleet
    def deles3d(self,ID):
        self._db.execute('delete from SC3d where ID={}'.format(ID))
        self._db.commit()
        return 'request is delete'
#updattttttttttt
    def updats3d(self,Name,ID):
        self._db.execute('update SC3d set Name=? where ID=?',(Name,ID))
##        self._db.execute('update Ticket set Comment=? where Name=?',(Comment,Name),)
        self._db.commit()
        return 'request is update'  
    
    def ListRequest3d(self):
        cursor=self._db.execute('select * from SC3d')
        self._db.commit()
        return cursor;
