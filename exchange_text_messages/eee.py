import os
#y=open(".us.text","r")
#t=y.readlines()
#y.close()
#u=[]
#for n in t:
	#u.append(n)
#print(len(u[0].strip()))
#y=open(".us.text","w")
#y.write("ok")
#y.close()
#sqlite3.connect('drdshprogram/dr1.db')
e=os.path.exists(".us.text")
if e==1:
	print("ok")
else:print("no")
