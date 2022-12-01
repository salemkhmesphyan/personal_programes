import termcolor
"""
programmer by en:salem khmes phyan
"""
class mem:
	"""
	wellcom in programe
	"""
	def __init__(self,*ps):
		self.tup=ps
		
		
		
		
		print("hello inin")
		if (len(self.tup))>1:
			self.check()
			
		else:
			print("error:the number input is less 1")
	def check(self):
		self.er=1
		e=[]
		e1=("w","e")
		for n in self.tup:
			if (type(n))==type(e) or (type(n))==type(e1):
				e.append(type(n))
				
			else:
				self.er=0
				print("error:this is not vaible")
				print(n)
				break
		if self.er==0:
			pass
		else:
			
			print(20*"*"+"details"+20*"*")
			print("number input data is >>",len(e))
			print("\n"+40*"-")
			print(termcolor.colored("input",color="blue")+"|"+termcolor.colored("   type       ",color="green")+"|"+termcolor.colored(" number elments",color="red")+"|")
			print(40*"-")
			for a in self.tup:
				print(termcolor.colored(str(int(self.tup.index(a)+1)),color="blue"),end="    |")
				print(termcolor.colored(type(a),color="green"),end="|      ")
				print(termcolor.colored(len(a),color="red"),end="              |")
				print("\n"+40*"-")
			print(20*"*"+"finshed details"+20*"*")
			print("\n")
		self.show_e()
	def show_e(self):
		
		print(15*"*"+"show elements in inputs"+15*"*")
		for g in self.tup:
			print(str(int(self.tup.index(g)+1))+"-",g)
	def helped(self):
		i="""
		hhhh
		"""
		return print(i)
	def deffr(self):
		ste=[]
		t=0
		u=1
		if self.er==0:
			pass
		else:
			for g in self.tup:
				if t==0:
					t=len(g)
				else:
					if t!=len(g):
						u=0
						print("no")
						break
		if u==1:
			print(20*"-"+"show deffernt"+20*"-")
			
			print(50*"-")
			for i1 in self.tup:
				print(int(self.tup.index(i1)+1),end="- ")
				
				for i2 in i1:
					if len(ste)!=len(self.tup[0]):
						ste.append(i2)
						#if i2 in ste:
							#print(termcolor.colored(i2,"green"),end=" | ")
						if len(self.tup)>2:
							if (i2 in self.tup[2]) or (i2 in self.tup[1]):
								print(termcolor.colored(i2,"green"),end=" | ")
							else:
								print(termcolor.colored(i2,"red"),end=" | ")
						#else:
							#if i2 in self.tup[1]:
								#print(termcolor.colored(i2,"green"),end=" | ")
							#else:
								#print(termcolor.colored(i2,"red"),end=" | ")
								
					else:
						if i2 in ste:
							print(termcolor.colored(i2,"green"),end=" | ")
						else:
							print(termcolor.colored(i2,color="red"),end=" | ")
				print("\n")
				print(50*"-")

d=['ds1','ds2','ds3',"trgreg"]
e=("ds1","ds2",424,"dfsdf")
w=("ds1","ds3",86,"dsf")
w1=("ds1","ds4",86,"dsf")
q=1	
e=mem(d,e,w,w1)
#e.helped()
e.deffr()

