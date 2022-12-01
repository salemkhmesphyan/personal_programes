import random
"""
programmer by en:salem khmes phyan
"""
"""
فكرة هذة العبة هو اختيار رقم في قلبك ثم تذكر رقم المجموعة المتواجد فيها
وهكذا تستمر العملية ثلاث مرات ثم في الاخير يظهر مجموعة من الارقام والرقم
السابع هو الرقم الذي اخترتة

"""
sho=['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21']
print(sho)
a1=[]#set 1 in operation 1
a2=[]#set 2 in operation 1
a3=[]#set 3 in operation 1
aa1=[]#set 1 in operation 2
aa2=[]#set 2 in operation 2
aa3=[]#set 3 in operation 2
aaa1=[]#set 1 in operation 3
aaa2=[]#set 2 in operation 3
aaa3=[]#set 3 in operation 3
ok=['1','2']
ww=1
dd=25
ww1=1
dd1=25
ww2=1
dd2=25

while dd>ww:#loop order random
		
	rr=random.choice(sho)
	if ww<8:
		a1.append(rr)
		d=sho.index(rr)
		del sho[d]
		print(d)

		print("a1",a1)
	if (ww>9) and (ww<17):
		a2.append(rr)
		d=sho.index(rr)
		del sho[d]
		print(d)
		print("a2",a2)
	if ww>17:
		a3.append(rr)
		d=sho.index(rr)
		del sho[d]
		print (d)
		print("a3",a3)
	ww+=1
print("start oparetion 1")	
print("1-",a1)			
print("2-",a2)
print("3-",a3)

en1=input("chooise number set>>")#enter number set you >>operation 1
def set1():
	for y in a2:
		sho.append(y)
	for y in a1:
		sho.append(y)
	for y in a3:
		sho.append(y)
	print(sho)
def set2():
	for y in a1:
		sho.append(y)
	for y in a2:
		sho.append(y)
	for y in a3:
		sho.append(y)
	print(sho)
def set3():
	for y in a1:
		sho.append(y)
	for y in a3:
		sho.append(y)
	for y in a2:
		sho.append(y)
	print(sho)		
if en1==str(1):
	set1()
if en1==str(2):
	set2()
if en1==str(3):
	set3()
print("finshed oparetion 1")
print("start oparetion 2")
	
#################################################################finshed oparetion 1####################################################
#################################################################started oparetion 2####################################################
				
for n in sho:
	f=sho.index(n)
	if f==0:
		aa1.append(n)
	if f==3:
		aa1.append(n)
	if f==6:
		aa1.append(n)
	if f==9:
		aa1.append(n)
	if f==12:
		aa1.append(n)
	if f==15:
		aa1.append(n)
	if f==18:
		aa1.append(n)
	if f==1:
		aa2.append(n)
	if f==4:
		aa2.append(n)
	if f==7:
		aa2.append(n)
	if f==10:
		aa2.append(n)
	if f==13:
		aa2.append(n)
	if f==16:
		aa2.append(n)
	if f==19:
		aa2.append(n)
	if f==2:
		aa3.append(n)
	if f==5:
		aa3.append(n)
	if f==8:
		aa3.append(n)
	if f==11:
		aa3.append(n)
	if f==14:
		aa3.append(n)
	if f==17:
		aa3.append(n)
	if f==20:
		aa3.append(n)
	
print("1-",aa1)			
print("2-",aa2)
print("3-",aa3)
print(sho)

sho1=[]#list new 2
en2=input("chooise number set>>")#enter number set you >>operation 2
def set11():
	for y in aa2:
		sho1.append(y)
	for y in aa1:
		sho1.append(y)
	for y in aa3:
		sho1.append(y)
	print(sho1)
def set22():
	for y in aa1:
		sho1.append(y)
	for y in aa2:
		sho1.append(y)
	for y in aa3:
		sho1.append(y)
	print(sho1)
def set33():
	for y in aa1:
		sho1.append(y)
	for y in aa3:
		sho1.append(y)
	for y in aa2:
		sho1.append(y)
	print(sho1)		
if en2==str(1):
	set11()
if en2==str(2):
	set22()
if en2==str(3):
	set33()
print("finshed oparetion 2")
print("start oparetion 3")	

##########################################################finshed opartion 2##################################################
##########################################################start opartion 3####################################################
for n in sho1:
	
	f=sho1.index(n)
	if f==0:
		aaa1.append(n)
	if f==3:
		aaa1.append(n)
	if f==6:
		aaa1.append(n)
	if f==9:
		aaa1.append(n)
	if f==12:
		aaa1.append(n)
	if f==15:
		aaa1.append(n)
	if f==18:
		aaa1.append(n)
	if f==1:
		aaa2.append(n)
	if f==4:
		aaa2.append(n)
	if f==7:
		aaa2.append(n)
	if f==10:
		aaa2.append(n)
	if f==13:
		aaa2.append(n)
	if f==16:
		aaa2.append(n)
	if f==19:
		aaa2.append(n)
	if f==2:
		aaa3.append(n)
	if f==5:
		aaa3.append(n)
	if f==8:
		aaa3.append(n)
	if f==11:
		aaa3.append(n)
	if f==14:
		aaa3.append(n)
	if f==17:
		aaa3.append(n)
	if f==20:
		aaa3.append(n)
print("1-",aaa1)			
print("2-",aaa2)
print("3-",aaa3)
#del sho[0]
#del sho[1]
#del sho[2]
#del sho[3]
#del sho[4]
#del sho[5]
#del sho[6]
#del sho[7]
#del sho[8]
#del sho[9]
#del sho[10]
#del sho[11]
#del sho[12]
#del sho[13]
#del sho[14]
#del sho[15]
#del sho[16]
#del sho[17]
#del sho[18]
#del sho[19]
#del sho[20]		
sho2=[]#list new 3
en3=input("chooise number set>>")#enter number set you >>operation 3
def set111():
	for y in aaa2:
		sho2.append(y)
	for y in aaa1:
		sho2.append(y)
	for y in aaa3:
		sho2.append(y)
	print(sho2)
def set222():
	for y in aaa1:
		sho2.append(y)
	for y in aaa2:
		sho2.append(y)
	for y in aaa3:
		sho2.append(y)
	print(sho2)
def set333():
	for y in aaa1:
		sho2.append(y)
	for y in aaa3:
		sho2.append(y)
	for y in aaa2:
		sho2.append(y)
	print(sho2)		
if en3==str(1):
	set111()
if en3==str(2):
	set222()
if en3==str(3):
	set333()
print("finshed oparetion 3")
####################################################finshed operation 3##############################################



