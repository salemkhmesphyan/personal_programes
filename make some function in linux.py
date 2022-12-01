#!/usr/bin/python3
"""
programmer by en:salem khmes phyan
"""
import os
import termcolor
import pyfiglet
#function path file
sdf='program personl'#termcolor.colored("##########################################################################", color="yellow")
gg=termcolor.colored(pyfiglet.figlet_format(sdf), color="yellow")
print(gg)

def hlp():
    print(termcolor.colored("##########################################################################", color="yellow"))
    print("# the programe is provid processes blew:                                 #")
    print("# 1-(dir)is show all files in dir.                                              #")
    print("# 2-(copy)is copy files to other file after write name file now and new. #")
    print("# 3-(type)is open files after write name file.                           #")
    print("# 4-(help)is show information about programe.                            #")
    print("# 5-(exit)is close programe.                                             #")
    print(termcolor.colored("##########################################################################", color="yellow"))
    ##

    
    ##
def ex():
    exit()
def rd():
	try:
		jj=1
		a=x[5:]
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
		print(termcolor.colored("file is not found",color="red"))
def pth():
    y=os.listdir()
    print(" files\t\t\t ",termcolor.colored("size\n",color="green"),50*"-",100*"-")
    for n in y:
        print(n+"\t",termcolor.colored("("+(str(os.path.getsize(n))+")bytes").strip(),color="green"))
#function copy file
def copy():
    try:
        e=x[5:]
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
        print(termcolor.colored("coping is sussecc",color="green"))
    except:
        print(termcolor.colored("file is not found",color="red"))
        
#enter opeartion    
x=input(termcolor.colored("python>>",color="white"))
d=x.find("type")
c=x.find("copy")
if d==0:
    rd()    
elif c==0:
    #nowfile=input("enter the name now file:")
    #newfile=input("enter the name new file:")
    copy()
elif x=='dir':
    pth()

elif x=='help':
    hlp()
while x!="dir"or"exit"or"help" and d!=0 and c!=0:
    x=input(termcolor.colored("python>>",color="white"))
    d=x.find("type")
    c=x.find("copy")
    if d==0:
        rd()
    elif c==0:
        
        copy()
    elif x=='dir':
        pth()
        
    elif x=="exit":
            ex()
    elif x=='help':
        hlp()        
    else:    
        print(termcolor.colored("unknow",color="red"))        
    continue
    

