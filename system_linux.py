#!/usr/bin/python3

"""
programmer by en:salem khmes phyan
"""
"""
programmer by en:salem khmes phyan
البرنامج يحتوي على 20 دالة او وضيف في نظام لينكس





"""
import os
import shutil
import time
import calendar
#import termcolor
#import pyfiglet
#function path file

#gg=termcolor.colored(pyfiglet.figlet_format(sdf), color="yellow")
#print(gg)
def hlp():#1
    print("##########################################################################")
    print("# the programe is provid processes blew:")                                 
    print("# 1-(ls)is show all files in dir.")                                       
    print("# 2-(cp)is copy files to other file after write name file now and new.::cp(old,new)") 
    print("# 3-(cat)is open files after write name file.::cat(name file)")                          
    print("# 4-(help)is show information about programe.")                          
    print("# 5-(exit)is close programe.")
    print("# 6-(mkdir)is create dir.::mkdir(name_dir)")
    print("# 7-(mv)is move files and dir.::mv old new")
    print("# 8-(rm)is remove files.::rm name_file")
    print("# 9-(vi)is create new file and write it.::vi name_file")
    print("# 10-(man)is show information about commands.::man ls")
    print("# 11-(pwd)is show pathe local now.")
    print("# 12-(cal)is show calendar local now.")
    print("# 12-(cal -m)is show calendar with input month.:cal -m 7")
    print("# 13-(date)is show time now.")
    print("# 14-(>)is creat new empty file.:>sss.py")
    print("# 15-( > )is redirect and replace the context file.:ls > ee.txt")
    print("# 16-(>>)is creat new empty file.:>>sss.py.")
    print("# 17-( >> )is redirect and append the to file.:ls >> ee.txt")
    print("# 18-(cd)is change path.")
    print("# 19-(cd ..)is back path.")
    print("# 20-(wc)is show numbers the lines and words and charcters.:wc ss.py")
    print("# 21-(clear)is remove screen.")
    print("# 22-(bc)is open calculator.")
    print("##########################################################################")
    ##

    
    ##
##############################################this is function commands##########################333
def ex():#2
    exit()
def rd():#3
	try:
		jj=1
		a=x[4:]
		red=open(a,'r')
		t=red.readlines()
		print('#'*40+'START'+'#'*35)
		nl=0
		for d in t:
			sd=len(d)
			print(str(jj)+'-'+d,end="\n")
			jj+=1
			nl+=sd
		print('#'*40+'END'+'#'*35)
		print('the line is>>'+str(jj),'the crctr is>>'+str(nl))
		print('#'*40+'END'+'#'*35)
		red.close()
	except:
		print("file is not found")
def pth():#4
    try:

        y=os.listdir()
        print(" files\t\t\t ","size\n",50*"-",100*"-")
        for n in y:
            print(n+"\t",(str(os.path.getsize(n))+"bytes").strip())
    except:
        print("check command")        
#function copy file
def copy():#5
    try:
        e=x[3:]
        m=" "
        
        s=e.find(m)
        o=e[:s]#file old
        r=e[s:]
        g=r.strip()#file new
        
        fs = open(o, 'r')
        fd = open(g, 'w')
        while 1:
            txt = fs.read(50)
            if txt =="":
                break
            fd.write(txt)
            
        fs.close()
        fd.close()
        print("coping is sussecc")
    except:
        print("file is not found")
def mkdir1():#6
    try:
        e=x[6:]
        g=e.strip()#file new
        os.mkdir(g)
        print("create directry is sussess")
    except:
        print("check the command")
def mvv():#7
    f=os.getcwd()
    e=x[3:]
    m=" "
    s=e.find(m)
    o=e[:s]#file old
    q=os.path.isdir(o)
    if q==False:

        print(q,"dir") 
        try:
            f=os.getcwd()
            e=x[3:]
            m=" "
            
            s=e.find(m)
            o=e[:s]#file old 
            r=e[s:]
            g=r.strip()#file new
            
            fs = open(o, 'r')
            fd = open(g, 'w')
            while 1:
                txt = fs.read(50)
                if txt =="":
                    break
                fd.write(txt)
                
            fs.close()
            fd.close()
            os.remove(f+"/"+o)
            print("coping is sussecc")
        except:
            print("file is not found")
    else:
        f=os.getcwd()
        try:
            e=x[3:]
            m=" "    
            s=e.find(m)
            o=e[:s]#file old
            r=e[s:]
            g=r.strip()#file new
            os.mkdir(g)
            os.rmdir(f+"/"+o)
           
            print("ok")
        except:
            print("check the command")
def erm():#8
    try:
        f=os.getcwd()
        e=x[2:]
        g=e.strip()
        os.remove(f+"/"+g)
        print("coping is sussecc")
    except:
        print("file is not found")
def vi():#10
    try:
        
        f=os.getcwd()
        e=x[2:]
        g=e.strip()
        en=input(">>enter text:")
        fd = open(g, 'w')
        fd.write(en)
        fd.close()
        print("create is sussecc")
    except:
        print("check your name")
def clu():
    while 1:
        try:

            y=input(">>")
            if y=="out":
                break
            else:
                print(eval(y))
        except:
            print("error in inputs")
def date():
    
    print(time.asctime( time.localtime(time.time())))
def cal():
    try:
        
        if len(x)>3:
            w=str(x[7:])
            print(calendar.month(2022,int(w)))
        else:
            print(calendar.calendar(2022))
    except:
        print("error in inputs")
def inform():
    w=x[4:]
    if w=="ls":
        print("(ls)is show all files in dir.")
    elif w=="cat":
        print("(cat)is open files after write name file.::cat(name file)")
    elif w=="cp":
        print("(cp)is copy files to other file after write name file now and new.::cp(old,new)")
    elif w=="help":
        print("(help)is show information about programe.")
    elif w=="mkdir":
        print("(mkdir)is create dir.::mkdir(name_dir)")
    elif w=="mv":
        print("(mv)is move files.::mv old new")
def addnewfile1():
    w=x[1:]
    fd = open(w, 'w')
    fd.close()
    print("create new file ("+str(w)+")")
def addnewfile2():
    w=x[2:]
    fd = open(w, 'w')
    fd.close()
    print("create new file ("+str(w)+")")
def addn1():
    
    s=x.find(" > ")
    a=x[:s]
    o=x[s+3:]#name_file
    mm=os.path.exists(o)
    print(mm,o)
    if mm==True:
        if a=="ls":
            y=os.listdir()
            fd = open(o, 'w')
            #fd.write(" files\t\t\t "+"size\n"+50*"-"+100*"-")
            for n in y:
                fd.write(n+"\t"+(str(os.path.getsize(n))+"bytes").strip()+"\n")    
            fd.close()
        elif a=="date":
            fd = open(o, 'w')
            fd.write(time.asctime( time.localtime(time.time())))    
            fd.close()
        elif a=="cal":
            fd = open(o, 'w')
            fd.write(calendar.calendar(2022))    
            fd.close()
        elif "cal -m " in x:
            w=str(x[7:])
            fd = open(o, 'w')
            fd.write((calendar.month(2022,int(w[:1].strip()))))    
            fd.close()
        elif a=="pwd":
            fd = open(o, 'w')
            fd.write(os.getcwd())    
            fd.close()
        elif a=="help":
            fd = open(o, 'w')
            fd.write("##########################################################################"+"\n")
            fd.write("# the programe is provid processes blew:"+"\n")                                 
            fd.write("# 1-(ls)is show all files in dir."+"\n")                                       
            fd.write("# 2-(cp)is copy files to other file after write name file now and new.::cp(old,new)"+"\n") 
            fd.write("# 3-(cat)is open files after write name file.::cat(name file)"+"\n")                          
            fd.write("# 4-(help)is show information about programe."+"\n")                          
            fd.write("# 5-(exit)is close programe."+"\n")
            fd.write("# 6-(mkdir)is create dir.::mkdir(name_dir)"+"\n")
            fd.write("# 7-(mv)is move files and dir.::mv old new"+"\n")
            fd.write("# 8-(rm)is remove files.::rm name_file")
            fd.write("# 9-(vi)is create new file and write it.::vi name_file"+"\n")
            fd.write("# 10-(man)is show information about commands.::man ls"+"\n")
            fd.write("# 11-(pwd)is show pathe local now."+"\n")
            fd.write("# 12-(cal)is show calendar local now."+"\n")
            fd.write("# 12-(cal -m)is show calendar with input month.:cal -m 7"+"\n")
            fd.write("# 13-(date)is show time now."+"\n")
            fd.write("# 14-(>)is creat new empty file.:>sss.py"+"\n")
            fd.write("# 15-( > )is redirect and replace the context file.:ls > ee.txt"+"\n")
            fd.write("# 16-(>>)is creat new empty file.:>>sss.py."+"\n")
            fd.write("# 17-( >> )is redirect and append the to file.:ls >> ee.txt"+"\n")
            fd.write("# 18-(cd)is change path."+"\n")
            fd.write("# 19-(cd ..)is back path."+"\n")
            fd.write("# 20-(wc)is show numbers the lines and words and charcters.:wc ss.py"+"\n")
            fd.write("# 21-(clear)is remove screen."+"\n")
            fd.write("# 22-(bc)is open calculator."+"\n")
            fd.write("##########################################################################")    
            fd.close()

    else:
        print("file is not found")
def addn2():
    
    s=x.find(" >> ")
    a=x[:s]
    o=x[s+4:]#name_file
    mm=os.path.exists(o)
    if mm==True:
        if a=="ls":
            y=os.listdir()
            fd = open(o, 'a')
            #fd.write(" files\t\t\t "+"size\n"+50*"-"+100*"-")
            fd.write("\n")
            for n in y:
                fd.write(n+"\t"+(str(os.path.getsize(n))+"bytes").strip()+"\n")    
            fd.close()
        elif a=="date":
            fd = open(o, 'a')
            fd.write("\n")
            fd.write(time.asctime( time.localtime(time.time())))    
            fd.close()
        elif a=="cal":
            fd = open(o, 'a')
            fd.write("\n")
            fd.write(calendar.calendar(2022))    
            fd.close()
        elif "cal -m " in x:
            w=str(x[7:])
            fd = open(o, 'a')
            fd.write("\n")
            fd.write((calendar.month(2022,int(w[:1].strip()))))    
            fd.close()
        elif a=="pwd":
            fd = open(o, 'a')
            fd.write("\n")
            fd.write(os.getcwd())    
            fd.close()
    else:
        print("file is not found")
def chpath2():
    try:

        re=[]
        f=os.getcwd()
        w=x[3:]
        if x=="cd ..":
            for a in f:
                if a=="\\":
                    re.append(f.rfind(a))
            nl=int(re[0])
            print(f[:nl])
            os.chdir(f[:nl])
        else:
            os.chdir(f+"/"+w)
            print(os.getcwd())
    except:
        print("error in cmmand")
def inline_ch():
    try:

        nw=0
        jj=1
        a=x[3:]
        red=open(a,'r')
        t=red.readlines()
        nl=0
        for d in t:
            sd=len(d.strip())
            jj+=1
            nl+=sd
            for q in d:
                if q==" ":
                    nw+=1
        print('#'*40+'@@@'+'#'*35)
        print('the lines is>>'+str(jj),'the characters is>>'+str(nl),"the words is>>"+str(nw+1))
        print('#'*40+'@@@'+'#'*35)
        red.close()
    except:
        print("file is not found")
########################################################
###############the loop in command #####################    
while 1:
    x=input("python>>")
    d=x.find("cat")
    c=x.find("cp")
    mk=x.find("mkdir")
    mv=x.find("mv")
    rm=x.find("rm")
    vii=x.find("vi")
    rmd=x.find("remdir")
    bc=x.find("bc")
    cal1=x.find("cal")
    man=x.find("man")
    addf1=x.find("> ")
    addn11=x.find(" > ")
    addn22=x.find(" >> ")
    addf2=x.find(">> ")
    cd=x.find("cd")
    wc=x.find("wc")
    if d==0:
        rd()
    elif c==0:
        copy()
    elif mk==0:
        mkdir1()
    elif mv==0:
        mvv()
    elif rm==0:
        erm()
    elif vii==0:
        vi()
    elif rmd==0:
        rmdir1()
    elif bc==0:
        clu()
    elif cd==0:
        chpath2()
    elif addf1==0:
        addnewfile1()
    elif addf2==0:
        addnewfile2()
    elif wc==0:
        inline_ch()
    elif " > " in x:
        addn1()
    elif " >> " in x:
        addn2()
    elif x=='ls':
        pth()
    elif x=='date':
        date()
    elif x=="pwd":#9
        print(os.getcwd())
    elif cal1==0:
        cal()
    elif man==0:
        inform()
    elif x=="exit":
            ex()
    elif x=="clear":
        os.system("cls")
    elif x=='help':
        hlp()        
    else:    
        print("unknow"+"-->"+x)
    

