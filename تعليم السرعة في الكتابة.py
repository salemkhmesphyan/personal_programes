import random
import time
"""
programmer by en:salem khmes phyan
"""
"""
الهدف من البرنامج تعلم سرعة في الكتابة على الكيبورد
"""
s=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
global y,o,o1,c1,en1
y=[]
o=''
en=0
c1=0
def tt():
	global y,o,o1,c1,en1
	q=str(input("are you countin?(n)or(y)"))
	if q=='n':
		print(20*"*"+"finshed"+20*"*")
	if q=='y':
		o=''
		o1=''
		y=[]
		dd()
def dd():
	global y,o,o1,c1,en1
	
	o1=''
	en=int(input("enter how number replicate:"))
	c1=int(input("enter how number characters:"))
	
	print(20*"*"+"start"+20*"*")
	print("ready after 5 mintes...............")
	time.sleep(5)
	r1=time.time()
	for d in range(0,en):
		e=random.sample(s,c1)
		
		for w in e:
			o1+=w+" "
			o+=w
		print(o1+"\n")
		r=str(input("enter>"))
		if o==r:
			y.append("1")
		else:
			y.append("0")
		o=''
		o1=''
	print("\n")
	print(50*"*")
	if "0" in y:
		print("mstak>>",y,"  >>no good")
	else:
		print("mstak>>",y,"  >>good")
	r2=time.time()-r1
	if r2>9.0:
		print("produc>>loss in time")
	else:print("produc>>good in time")
	print("time>>",time.time()-r1)
	print(50*"*")
	tt()


if len(y)==0:
	dd()
