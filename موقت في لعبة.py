from Tkinter import *
from random import sample
#from Tkinter import messagebox
import random
"""
programmer by en:salem khmes phyan
"""
r=Tk()
ti=1
lb1=Label(r,text='what the small chracter?')
lb1.grid(row=0,column=1)
# lb2=Label(r,text='0000000000000')
# lb2.grid(row=0,column=2)
but=Button(r,text='ok')
but.grid(row=1,column=0)
but2=Button(r,text='start')
but2.grid(row=4,column=0)
but3=Button(r,text='stop')
but3.grid(row=5,column=0)
ent=Entry(r)
ent.grid(row=0,column=0)
ent2=Entry(r)
ent2.grid(row=0,column=2)
ent3=Entry(r)
ent3.grid(row=2,column=2)
ent4=Entry(r)
ent4.grid(row=3,column=2)
ent5=Entry(r)
ent5.grid(row=4,column=1)

f=sample(range(1,12),1)
g=sample(range(1,12),1)
cho=['A','B','C',"D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
f=random.choice(cho)
ent.insert('end',f)
ent3.insert('end','0')
ent4.insert('end','0')
ent5.insert('end','0')
def strr():
	global ti

	if int(ent4.get())>=5:
		ent4.delete(0,"end")

		#messagebox.showinfo("@","the relus is="+str(ent3.get()))
		print"the relus is "+str(ent3.get())
		ti=0
		ent5.delete(0,"end")
		ent5.insert('end',"0")
		ti=1
	else:
		p=int(ent4.get())
		p+=1
		ent4.delete(0,"end")
		ent4.insert('end',str(p))
	d=ent.get()
	h=d.lower()
	s=ent2.get()
	if h==s:
		g=int(ent3.get())
		g+=10
		ent3.delete(0,"end")
		ent3.insert('end',str(g))
	else:
		g=int(ent3.get())
		g-=10
		ent3.delete(0,"end")
		ent3.insert('end',str(g))	
	ent.delete(0,"end")
	ent2.delete(0,"end")	
	f=random.choice(cho)
	ent.insert('end',f)
	if str(ent4.get())=="":
		ent3.delete(0,"end")	
		ent3.insert("end","0")
		ent4.insert("end","0")
def aft():
	global ti
	if ti==1:
		f1=int(ent5.get())
		if f1>=60:
			ti=0
			print'finsh time'
			print"the relus is "+str(ent3.get())
			ent5.delete(0,"end")			
		ent5.delete(0,"end")
		f1+=1
		ent5.insert("end",str(f1))
		r.after(1000,aft)
	else:
		print"stoooop"
		ti=1
def stp():
	global ti
	ti=0
but3.configure(command=stp)				
but2.configure(command=aft)				
but.configure(command=strr)	















r.mainloop()
