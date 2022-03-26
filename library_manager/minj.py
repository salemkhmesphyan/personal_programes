import os,sys,shutil
import hashlib
import PyPDF2 as o
from flask import Flask,render_template,request,send_file,flash,redirect,url_for,session
from pdf2image import convert_from_path
import sqlite3
import time
import datetime
from datetime import date
from functools import wraps
from datetime import timedelta
t=time.asctime(time.localtime(time.time()))
x=datetime.datetime.now().hour
s=datetime.datetime.now().minute
a=datetime.datetime.now().second
time1=str(str(x)+":"+str(s)+":"+str(a))
today = str(date.today())

def login_required(function):
    @wraps(function) 
    def wrapper(*args, **kwargs):
        if 'logged_in' in session:
            return function(*args, **kwargs)
        else:
            flash(u'سجّل دخولك أولا')
            return redirect(url_for('login1'))
    return wrapper
app = Flask(__name__)
app.config['SECRET_KEY'] = "Secret"
app.config['USERNAME']   = "admin"
app.config['PASSWORD']   = "password"
APP_ROOT=os.path.dirname(os.path.abspath(__file__))

def shosc(l):
	db1=sqlite3.connect('lib1.db')
	cb=db1.cursor()
	cb.execute("select * from sections")
	v99=cb.fetchall()
	return v99

def sse(o):
	p=[]
	db1=sqlite3.connect('lib1.db')
	cb=db1.cursor()
	if 'logged_in' in session:
		
		cb.execute("select * from log where prerogatives='{}'".format("yes"))
		v99=cb.fetchall()
		for h in v99:
			p.append(h[1])
		u=session['logged_in']
		if u in p:
			jj='tr'
			return jj
		else:jj='y'
		return jj
		
	else:
		jj='p'
		return jj

@app.route("/",methods=['GET','POST'])#methods=['GET']
def login1():
	db1=sqlite3.connect('lib1.db')
	db1.row_factory=sqlite3.Row
	db1.execute('create table if not exists addus(ID integer primary Key autoincrement,nambook text,tybook text,alnsher text,objbook text,homespac text,agespac,alm text,status text)')
	db1.execute('create table if not exists books(ID integer primary Key autoincrement,nambook text,numbook text,alm text,spic text,objbook text,homespac text,agespac text,linkimg text)')
	db1.execute('create table if not exists log(ID integer primary Key autoincrement,username text,pass text,prerogatives text)')
	db1.execute('create table if not exists sections(ID integer primary Key autoincrement,section text)')
	db1.execute('create table if not exists puplichouse(ID integer primary Key autoincrement,housespac text,information text)')
	db1.execute('create table if not exists branchs(ID integer,bransh text primary Key)')
	db1.execute('create table if not exists writtens(ID integer primary Key autoincrement,written text,information text)')
	db1.commit()
	cb=db1.cursor()
	cb.execute("select * from sections")
	pmin=cb.fetchall()
	cb.execute("select * from books order by ID desc limit 4")
	df5=cb.fetchall()
	return render_template(u'post.html',t=u'الصفحة الرئيسية',df5=df5,pmin=pmin,v99=shosc('k'),pp3=sse("k"))


@app.route("/pageaddroot",methods=['GET','POST'])#methods=['GET']
@login_required
def pageaddroot():
	r1=[]
	db1=sqlite3.connect('lib1.db')
	db1.row_factory=sqlite3.Row
	ff=db1.execute("select * from log where prerogatives='{}'".format("yes"))
	for n in ff:
		r1.append(n["username"])
	if session['logged_in'] in r1:
		db1=sqlite3.connect('lib1.db')
		f=db1.cursor()
		ch=f.execute("select max(numbook) from books")#find small value in numbook
		for n in ch:
			y=n[0]
		ch=f.execute("select * from writtens")
		mol=ch.fetchall()
		ch=f.execute("select * from puplichouse")
		pup=ch.fetchall()
		ch=f.execute("select section from sections")
		sect=ch.fetchall()
		ch=f.execute("select bransh from branchs where ID='{}'".format(1))
		brnch=ch.fetchall()
		return render_template(u'sign in.html',t=u'اضافة كتاب من المشرف',y=int(y)+1,pp3=sse("k"),mol=mol,pup=pup,f2=brnch,f1=sect,)
	else:
		flash("ليس لديك صلاحيات الدخول")
		return redirect(url_for('login1'))

@app.route("/addlog",methods=['GET','POST'])#methods=['GET']
def addlog():
	ii=[]
	ii1=[]
	un=request.form["username"]
	ps=request.form["password"]
	db1=sqlite3.connect('lib1.db')
	db1.row_factory=sqlite3.Row
	#sec=hashlib.sha1(ps.encode())
	sec=hashlib.md5(ps.encode()).hexdigest()
	#sec1=sec.hexdigest()
	ch=db1.execute("select * from log where username='{}'".format(un))
	for n in ch:
		ii.append(n["username"])
	if len(ii)==0:
			db1.execute("insert into log(username,pass,prerogatives) values(?,?,?)",(un,ps,"no"))
			db1.commit()
			
			ch1=db1.execute("select * from log")
			for d in ch1:
				ii1.append(d['username'])
			if len(ii1)==1:
					#db1.execute('create table if not exists root(ID integer primary Key autoincrement,username text,pass text)')
					db1.execute("insert into log(username,pass,prerogatives) values(?,?,?)",('admin','12345','yes'))#hashlib.md5('12345'.encode()).hexdigest()
					db1.commit()
			flash(u"تم اضافة الحساب بنجاح")
			return redirect(url_for('login1'))
	else:
		flash(u"اسم المستخدم موجود الرجاء اختيار اسم اخر")
		return redirect(url_for('login1'))

@app.route("/addbook",methods=['GET','POST'])#methods=['GET']
@login_required
def addbook():
	u3=[]
	f=os.getcwd()
	r1=[]
	d="/static/img/"
	d1="/static/addbooks/"
	nam=request.form["namebook"]
	num=request.form["numberbook"]
	almm=request.form["almolf"]
	spishl=request.form["specialism"]
	obj=request.form["objbook"]
	home=request.form["homespac"]
	age=request.form["agespac"]
	link=request.form["linkimg"]
	db1=sqlite3.connect('lib1.db')
	db1.row_factory=sqlite3.Row
	ff=db1.execute("select * from log where prerogatives='{}'".format("yes"))
	for n in ff:
		r1.append(n["username"])
	if session['logged_in'] in r1:
		if nam[-3:]!='pdf':
			flash("لايمكن اضافة هذا الملف")
			return redirect(url_for('pageaddroot'))
		#db1.execute("insert into books(nambook,numbook,alm,spic,objbook,homespac,agespac,linkimg) values(?,?,?,?,?,?,?,?)",(nam,num,almm,spishl,obj,home,age,d+link))
		#db1.commit()
		target=os.path.join(APP_ROOT,'static/addbooks/')
		if not os.path.isdir(target):
			os.mkdir(target)
		for fill in request.files.getlist("chose"):
			filename=fill.filename
			dest="/".join([target,filename])
			fill.save(dest)
			#if namebook[-3:]=='pdf':
			pages = convert_from_path('static/addbooks/'+nam, 50,first_page=1,last_page=1)
			for page in pages:
				page.save('static/addbooks/'+link, 'JPEG')
			tt=db1.execute("select * from books")#chcik found book###############
			y=open(f+d1+link,"rb")
			t=y.read()
			y.close()
			for h in tt:
				y2=open(f+h["linkimg"],"rb")
				t2=y2.read()
				y2.close()
				if t2==t:
					u3.append("1")
					break
			if len(u3)>0:
				os.remove(f+d1+link)###
				os.remove(f+d1+nam)
				
				#db1.execute("delete from books where nambook='{}' limit 1".format(nam))
				#db1.commit()
				flash("هذا الكتاب مضاف من قبل")
				return redirect(url_for('pageaddroot'))
			else:
				db1.execute("insert into books(nambook,numbook,alm,spic,objbook,homespac,agespac,linkimg) values(?,?,?,?,?,?,?,?)",(nam,num,almm,spishl,obj,home,age,d+link))
				db1.commit()
				shutil.move(f+d1+link,f+d+link)
				shutil.move(f+d1+nam,f+d+nam)
				flash("تم اضافة الكتاب بنجاح")
				return redirect(url_for('pageaddroot'))
	else:
		flash("ليس لديك صلاحيات الدخول")
		return redirect(url_for('login1'))

@app.route("/showbook",methods=['GET','POST'])#methods=['GET']##################3
def showbook():
	df=[3,5,6,7,4]
	db1=sqlite3.connect('lib1.db')
	db1.row_factory=sqlite3.Row
	sh=db1.execute("select * from books")
	return render_template(u'p2.html',sh=sh,t=u'صفحة تسجيل الدخول',pp3=sse("k"))
@app.route("/sh1<id1>",methods=['GET','POST'])#methods=['GET']
def go(id1):
	j="static/img/"+str(id1)
	pp=open(j,"rb")
	pr=o.PdfFileReader(pp)
	gepg=(pr.getNumPages())
	g=os.path.getsize(j)
	size=str(float(g/1048576))
	f='.'
	t=size.find(f)
	t1=size[:t]
	o1=size[t:]
	j=o1[:3]
	ii=t1+j+"MB"
	db1=sqlite3.connect('lib1.db')
	db1.row_factory=sqlite3.Row
	
	post1=db1.execute("select * from books where nambook='{}'".format(id1))
	return render_template('shbok.html',post1=post1,s="static/img/"+str(id1),gepg=gepg,ii=ii,pp3=sse("k")) 
	
@app.route("/searchp1",methods=['GET','POST'])#methods=['GET']
def searchp1():
	db1=sqlite3.connect('lib1.db')
	cb=db1.cursor()
	cb.execute("select section from sections")
	f1=cb.fetchall()
	cb.execute("select bransh from branchs where ID=1")
	f2=cb.fetchall()
	return render_template('pageserch.html',f1=f1,f2=f2,v99=shosc('k'),pp3=sse("k"),t="بحث عن كتاب")
@app.route("/searchp2",methods=['GET','POST'])#methods=['GET']
def searchp2():
	t1=[]
	s1= request.form['s11']
	s2= request.form['s22']
	s3= request.form['s33']
	s4= request.form['s44']
	if s1=="خاص":
		db1=sqlite3.connect('lib1.db')
		cb=db1.cursor()
		cb.execute("select * from books where spic='{}' and objbook='{}'and nambook like '%{}%'".format(s2,s3,s4))
		se=cb.fetchall()
		for n in se:
			t1.append(n[1])
		f=len(t1)
		flash(f)
		cb.execute("select * from books where spic='{}' and objbook='{}'and nambook like '%{}%'".format(s2,s3,s4))
		se=cb.fetchall()
		cb.execute("select section from sections")
		f1=cb.fetchall()
		cb.execute("select bransh from branchs where ID=1")
		f2=cb.fetchall()
		return render_template('pageserch.html',se=se,f1=f1,f2=f2,pp3=sse("k"),s4=s4)
	else:
		db1=sqlite3.connect('lib1.db')
		cb=db1.cursor()
		cb.execute("select * from books where nambook like '%{}%'".format(s4))
		se=cb.fetchall()
		for n in se:
			t1.append(n[1])
		f=len(t1)
		flash(f)
		cb.execute("select * from books where nambook like '%{}%'".format(s4))
		se=cb.fetchall()
		cb.execute("select section from sections")
		f1=cb.fetchall()
		cb.execute("select bransh from branchs where ID=1")
		f2=cb.fetchall()
		return render_template('pageserch.html',se=se,f1=f1,f2=f2,pp3=sse("k"),s4=s4)

@app.route("/login", methods=['GET', 'POST'])
def login():
	rr=[]
	session['logged_in'] = True
	session.permanent =  True
	app.permanent_session_lifetime = timedelta(minutes=5)
	if request.method == 'POST':
		db1=sqlite3.connect('lib1.db')
		db1.row_factory=sqlite3.Row
		db1.execute('create table if not exists log(ID integer primary Key autoincrement,username text,pass text,prerogatives text)')
		db1.commit()
		d=db1.execute("select * from log")
		for n in d:
			rr.append((n['username'],n['pass']))
		username = request.form['username']
		password = request.form['password']
		#dd=hashlib.sha1(password.encode())
		#ff=dd.hexdigest()
		#gg=hashlib.md5(password.encode()).hexdigest()
		if (username,password) in rr:
			session['logged_in'] = username
			flash(u'سُجّل دخولك بنجاح')
			#flash(session['logged_in'])
			return redirect(url_for('login1'))
		else:
			#session['logged_in'] = False
			session.pop('logged_in', None)
			flash("خطاء في تسجيل الدخول الرجاء حاول مرة اخرى")
			return redirect(url_for('login1'))
	

# Logout Route
@app.route("/logout")
def logout():
	h=session['logged_in']
	session.pop('logged_in', None)
	flash(str(h)+":"+u'تم تسجل خروجك بنجاح')
	return redirect(url_for('login1'))

@app.route("/err")
def err():
	db1=sqlite3.connect('lib1.db')
	db1.row_factory=sqlite3.Row
	d=db1.execute("select * from log")
	for n in d:
		if n['username']==session['logged_in']:
			g=n['pass']
			return render_template('datauser.html',ff=session['logged_in'],tt=g,pp3=sse("k"))
		#else:
			##session.pop('logged_in', None)
			#return redirect(url_for('wrnng'))
			

@app.route("/wrnng")
def wrnng():
	session.pop('logged_in', None)
	return render_template('p3.html')
###################################################
@app.route("/pgaddus",methods=['GET','POST'])
def pgaddus():
	db1=sqlite3.connect('lib1.db')
	cb=db1.cursor()
	cb.execute("select section from sections")
	f1=cb.fetchall()
	cb.execute("select bransh from branchs where ID=1")
	f2=cb.fetchall()
	cb.execute("select housespac from puplichouse")
	f3=cb.fetchall()
	cb.execute("select written from writtens")
	f4=cb.fetchall()
	
	return render_template('pagadduser.html',f1=f1,f2=f2,f3=f3,f4=f4,v99=shosc('k'),pp3=sse("k"),t="اضافة كتاب")
	
@app.route("/pgaddus2",methods=['GET','POST'])
@login_required
def pgaddus2():
	f=os.getcwd()
	namebook = request.form['nabok']
	typebook = request.form['ty']
	br = request.form['bran']
	hosp = request.form['homesp']
	agsp = request.form['agesp']
	alm= request.form['alm']
	
	#li = request.form['data']
	jlsa=session['logged_in']
	if namebook[-3:]=='pdf':
		
		db1=sqlite3.connect('lib1.db')
		db1.row_factory=sqlite3.Row
		#db1.execute('create table if not exists addus(ID integer primary Key autoincrement,nambook text,tybook text,alnsher text)')
		#objbook text,homespac text,agespac)
		db1.execute('''insert into addus(nambook,tybook,alnsher,objbook,homespac,agespac,alm,status) values(?,?,?,?,?,?,?,?)''',(namebook,typebook,jlsa,br,hosp,agsp,alm,"1"))
		db1.commit()
		target=os.path.join(APP_ROOT,'static/addbooks/')
		
		if not os.path.isdir(target):
			os.mkdir(target)
		for fill in request.files.getlist("data"):
			
			filename=fill.filename
			dest="/".join([target,filename])
			fill.save(dest)
			if namebook[-3:]=='pdf':
				pages = convert_from_path('static/addbooks/'+namebook, 50,first_page=1,last_page=1)
				for page in pages:
					page.save('static/addbooks/'+namebook[:-3]+'jpg', 'JPEG')
			flash(u"تم اضافة الملف بنجاح")	
		return redirect(url_for('pgaddus'))
	else:
		flash(u"ارجاء اختيار ملف من نوع بي دي اف فقط")
		return redirect(url_for('pgaddus'))	
@app.route("/lowroot",methods=['GET','POST'])
@login_required
def lowroot():#######################root
	r1=[]
	j1=[]
	db1=sqlite3.connect('lib1.db')
	db1.row_factory=sqlite3.Row
	ff=db1.execute("select * from log where prerogatives='{}'".format("yes"))
	for n in ff:
		r1.append(n["username"])
	if session['logged_in'] in r1:
		jj=db1.execute("select * from addus where status=1")
		for g in jj:
			j1.append(g["nambook"])
		g1=len(j1)
		ff1=db1.execute("select * from log where username='{}' and username is not'{}'".format(session['logged_in'],'admin'))	
		return render_template('root.html',t="صلاحيات المشرف",ff1=ff1,g1=g1,v99=shosc('k'),pp3=sse("k"))
	else:
		flash("ليس لديك صلاحيات الدخول")
		return redirect(url_for('login1'))
		
@app.route("/modroot",methods=['GET','POST'])
def modroot():
	nameroot= request.form['nroot']
	passroot= request.form['proot']
	prroot= request.form['rroot']
	db1=sqlite3.connect('lib1.db')
	db1.row_factory=sqlite3.Row
	db1.execute("update log set username='{}',pass='{}',prerogatives='{}' where username='{}'".format(nameroot,passroot,prroot,session['logged_in']))
	db1.commit()
	flash(u"تم تعديل البيانات بنجاح")
	return redirect(url_for('lowroot'))
@app.route("/addroot",methods=['GET','POST'])
def addroot():
	o=[]
	nus=request.form['adn']
	pss=request.form['adp']
	db1=sqlite3.connect('lib1.db')
	db1.row_factory=sqlite3.Row
	sec=hashlib.md5(pss.encode()).hexdigest()
	p=db1.execute("select * from log where username='{}'".format(nus))
	for h in p:
		o.append(h['username'])
	if len(o)==0:
		db1.execute("insert into log(username,pass,prerogatives) values(?,?,?)",(nus,pss,"yes"))
		db1.commit()
		flash(u"تم اضافة مشرف جديد")
		return redirect(url_for('lowroot'))
	else:
		flash(u"الرجاء اختيار اسم اخر")
		return redirect(url_for('lowroot'))
@app.route("/moduser",methods=['GET','POST'])
def moduser():
	o=[]
	nus= request.form['n1']
	paus= request.form['p1']
	u=session['logged_in']
	db1=sqlite3.connect('lib1.db')
	db1.row_factory=sqlite3.Row
	p=db1.execute("select * from log where username='{}' and username is not'{}'".format(nus,u))
	for h in p:
		o.append(h['username'])
	if len(o)==0:
		db1.execute("update log set username='{}',pass='{}' where username='{}'".format(nus,paus,session['logged_in']))
		db1.commit()
		flash(u"تم تعديل البيانات بنجاح")
		session.pop('logged_in', None)
		session['logged_in'] = True
		session.permanent =  True
		app.permanent_session_lifetime = timedelta(minutes=5)
		session['logged_in'] = nus
		return redirect(url_for('err'))
	else:
		flash("الرجاء غير الاسم الى اسم اخر")
		return redirect(url_for('err'))
@app.route("/deluser",methods=['GET','POST'])
def deluser():
	db1=sqlite3.connect('lib1.db')
	db1.row_factory=sqlite3.Row
	db1.execute("delete from log where username='{}'".format(session['logged_in']))
	db1.commit()
	session.pop('logged_in', None)
	flash("تم حذف حسابك بنجاح")
	return redirect(url_for('login1'))

@app.route("/runuser",methods=['GET','POST'])
@login_required
def runuser():
	o=[]
	y1=[]
	db1=sqlite3.connect('lib1.db')
	db1.row_factory=sqlite3.Row
	p=db1.execute("select * from log where prerogatives='{}'".format("yes"))
	for h in p:
		o.append(h['username'])
	if session['logged_in'] in o:
		
		db1=sqlite3.connect('lib1.db')
		db1.row_factory=sqlite3.Row
		d1=db1.execute("select * from log where username is not'{}'".format("admin"))
		for n in d1:
			y1.append(n["username"])
		t=len(y1)
		d1=db1.execute("select * from log where username is not'{}'".format("admin"))
		return render_template('manguser.html',d1=d1,t=t,pp3=sse("k"))
	else:
		flash("ليس لديك صلاحيات الدخول")
		return redirect(url_for('login1'))
@app.route("/del/<gg>",methods=['GET','POST'])
@login_required
def remov(gg):
	db1=sqlite3.connect('lib1.db')
	db1.row_factory=sqlite3.Row
	db1.execute("delete from log where username='{}'".format(gg))
	db1.commit()
	flash("تم حذف الحساب بنجاح")
	return redirect(url_for('runuser'))
	
@app.route("/addbooks",methods=['GET','POST'])
@login_required
def addbooks():
	r1=[]
	db1=sqlite3.connect('lib1.db')
	db1.row_factory=sqlite3.Row
	ff=db1.execute("select * from log where prerogatives='{}'".format("yes"))
	for n in ff:
		r1.append(n["username"])
	if session['logged_in'] in r1:
		c1=db1.execute("select * from addus where status=1")
		return render_template('bookadds.html',c1=c1,pp3=sse("k"))
	else:
		flash("ليس لديك صلاحيات الدخول")
		return redirect(url_for('login1'))

@app.route("/add<y1y1>",methods=['GET','POST'])
@login_required
def nowaddbook(y1y1):
	r1=[]
	db1=sqlite3.connect('lib1.db')
	db1.row_factory=sqlite3.Row
	ff=db1.execute("select * from log where prerogatives='{}'".format("yes"))
	for n in ff:
		r1.append(n["username"])
	if session['logged_in'] in r1:
		j1=db1.execute("select * from addus where nambook='{}'".format(y1y1))
		for n1 in j1:
			b=n1['tybook']
			b1=n1['objbook']
			b2=n1['alm']
			b3=n1['homespac']
			b4=n1['agespac']
		if y1y1[-3:]=='pdf':
			h=y1y1[:-3]+'jpg'
		else:
			h=y1y1
		db1.close()
		db2=sqlite3.connect('lib1.db')
		f=db2.cursor()
		ch=f.execute("select max(numbook) from books")#find small value in numbook
		for n in ch:
			y=n[0]
		f.execute("select * from sections where section='{}'".format(b))
		df=f.fetchall()
		for n in df:
			h9=n[0]
		cb=db2.cursor()
		cb.execute("select bransh from branchs where ID='{}'".format(h9))
		f9=cb.fetchall()
		cb.execute("select * from sections")
		f1=cb.fetchall()
		cb.execute("select * from branchs")
		f2=cb.fetchall()
		cb.execute("select * from writtens")
		f3=cb.fetchall()
		cb.execute("select * from puplichouse")
		f4=cb.fetchall()
		return render_template('nowaddbook.html',f1=f1,f2=f2,f3=f3,f4=f4,a1=y1y1,g=b,h=h,l=int(y)+1,b1=b1,b2=b2,b3=b3,b4=b4,f9=f9,pp3=sse("k"))
	else:
		flash("ليس لديك صلاحيات الدخول")
		return redirect(url_for('login1'))

@app.route("/stobook",methods=['GET','POST'])
@login_required
def stobook():
	f=os.getcwd()
	r1=[]
	u3=[]
	d="/static/img/"
	d1="/static/addbooks/"
	nam=request.form["namebook"]
	num=request.form["numberbook"]
	almm=request.form["almolf"]
	spishl=request.form["specialism"]
	obj=request.form["objbook"]
	home=request.form["homespac"]
	age=request.form["agespac"]
	link=request.form["linkimg"]
	db1=sqlite3.connect('lib1.db')
	db1.row_factory=sqlite3.Row
	ff=db1.execute("select * from log where prerogatives='{}'".format("yes"))
	for n in ff:
		r1.append(n["username"])
	if session['logged_in'] in r1:
		tt=db1.execute("select * from books")
		y=open(f+d1+link,"rb")
		t=y.read()
		y.close()
		for h in tt:
			y2=open(f+h["linkimg"],"rb")
			t2=y2.read()
			y2.close()
			if t2==t:
				u3.append("1")
				break
		if len(u3)>0:
			os.remove(f+d1+link)
			os.remove(f+d1+nam)
			#shutil.move(f+d1+link,f+d+link)
			#shutil.move(f+d1+nam,f+d+nam)
			db1.execute("update addus set status=0 where nambook='{}'".format(nam))
			db1.commit()
			flash("هذا الكتاب مضاف من قبل")
			return redirect(url_for('addbooks'))
		else:
			
			db1.execute("insert into books(nambook,numbook,alm,spic,objbook,homespac,agespac,linkimg) values(?,?,?,?,?,?,?,?)",(nam,num,almm,spishl,obj,home,age,d+link))
			db1.commit()
			shutil.move(f+d1+link,f+d+link)
			shutil.move(f+d1+nam,f+d+nam)
			db1.execute("update addus set status=0 where nambook='{}'".format(nam))
			db1.commit()
			#db1.execute('create table if not exists books(ID integer primary Key autoincrement,nambook text,numbook text,alm text,spic text,objbook text,homespac text,agespac text,linkimg text)')
			flash("تم اضافة الكتاب بنجاح")
			return redirect(url_for('addbooks'))
	else:
		flash("ليس لديك صلاحيات الدخول")
		return redirect(url_for('login1'))


@app.route("/de<y2y2>",methods=['GET','POST'])
@login_required
def nowdebook(y2y2):
	f=os.getcwd()
	d1="/static/addbooks/"
	r1=[]
	db1=sqlite3.connect('lib1.db')
	db1.row_factory=sqlite3.Row
	ff=db1.execute("select * from log where prerogatives='{}'".format("yes"))
	for n in ff:
		r1.append(n["username"])
	if session['logged_in'] in r1:
		db1.execute("delete from addus where nambook='{}'".format(y2y2))
		db1.commit()
		os.remove(f+d1+y2y2)
		if y2y2[-3:]=='pdf':
			u='.'
			#h=y2y2.find(u)
		
			os.remove(f+d1+y2y2[:-3]+'jpg')
		flash("تم حذف الملف بنجاح")	
		return redirect(url_for('addbooks'))
	else:
		flash("ليس لديك صلاحيات الدخول")
		return redirect(url_for('login1'))

@app.route("/rename<y3y3>",methods=['GET','POST'])
@login_required
def unfile(y3y3):
	f=os.getcwd()
	d1="/static/addbooks/"
	r1=[]
	db1=sqlite3.connect('lib1.db')
	db1.row_factory=sqlite3.Row
	ff=db1.execute("select * from log where prerogatives='{}'".format("yes"))
	for n in ff:
		r1.append(n["username"])
	if session['logged_in'] in r1:
		#os.renames(ap1m[co],apm[co])
		return render_template('renamefile.html',c1=y3y3,pp3=sse("k"))#,g='.'+y3y3[-3:]
	else:
		flash("ليس لديك صلاحيات الدخول")
		return redirect(url_for('login1'))
@app.route("/nowrenam",methods=['GET','POST'])
@login_required
def nowrenam():
	nao=request.form["ebook1"]
	k1=request.form["amebook"]
	nan=k1+'.pdf'
	f=os.getcwd()
	d1="/static/addbooks/"
	r1=[]
	
	db1=sqlite3.connect('lib1.db')
	db1.row_factory=sqlite3.Row
	ff=db1.execute("select * from log where prerogatives='{}'".format("yes"))
	for n in ff:
		r1.append(n["username"])
	if session['logged_in'] in r1:
		os.renames(f+d1+nao,f+d1+nan)
		if nao[-3:]=='pdf':
			u='.'
			h=nao.find(u)
			y=nan.find(u)
			os.renames(f+d1+nao[:-3]+'jpg',f+d1+nan[:-3]+'jpg')
		db1.execute("update addus set nambook='{}' where nambook='{}'".format(nan,nao))
		db1.commit()
		flash("تم تغيير اسم الملف بنجاح")
		return redirect(url_for('addbooks'))
		
		
	else:
		flash("ليس لديك صلاحيات الدخول")
		return redirect(url_for('login1'))
@app.route("/seci<getid>",methods=['GET','POST'])
def showlist(getid):
	r1=[]
	#nb= request.form['gh']
	db1=sqlite3.connect('lib1.db')
	cb=db1.cursor()
	cb.execute("select * from books where spic='{}'".format(getid))
	ff=cb.fetchall()
	for n in ff:
		r1.append(n[1])
	rr=len(r1)
	#ff=db1.execute("select * from books where spic='{}'".format(getid))
	cb.execute("select * from sections")
	pmin=cb.fetchall()
	return render_template('sholist.html',ff=ff,rr=rr,pmin=pmin,pp=getid,pp3=sse("k"))
@app.route("/addbookuser2",methods=['GET','POST'])
def addbookuser2():
	nb= request.form['tybok']
	db1=sqlite3.connect('lib1.db')
	cb=db1.cursor()
	cb.execute("select * from sections where section='{}'".format(nb))
	df=cb.fetchall()
	for n in df:
		h=n[0]
	cb=db1.cursor()
	cb.execute("select bransh from branchs where ID='{}'".format(h))
	f2=cb.fetchall()
	cb.execute("select housespac from puplichouse")
	f3=cb.fetchall()
	cb.execute("select written from writtens")
	f4=cb.fetchall()
	#cb.execute("select distinct section from sections where section='{}'".format(nb))
	#f1=cb.fetchall()
	
	return render_template('pagadduser.html',f3=f3,f4=f4,f2=f2,f11=nb,pp3=sse("k"))	

@app.route("/addsec",methods=['GET','POST'])
def addsec():
	db1=sqlite3.connect('lib1.db')
	cb=db1.cursor()
	cb.execute("select section from sections")
	f1=cb.fetchall()
	return render_template('addsection.html',f1=f1,pp3=sse("k"))
@app.route("/addsec2",methods=['GET','POST'])
def addsec2():
	r=[]
	nb1= request.form['u0']
	nb2= request.form['u1']
	nb3= request.form['u2']
	nb4= request.form['u3']
	if nb1=="قسم جديد":
		db1=sqlite3.connect('lib1.db')
		cb=db1.cursor()
		cb.execute('select section from sections')
		f=cb.fetchall()
		for d in f:
			r.append(d[0])
		if nb2 in r:
			flash("اسم القسم موجود")
			return redirect(url_for("addsec"))
		else:
			
			cb.execute("insert into sections(section) values('{}')".format(nb2))
			db1.commit()
			flash("تم اضافة القسم بنجاح")
			return redirect(url_for("addsec"))
	else:
		db1=sqlite3.connect('lib1.db')
		gr=db1.execute("select * from sections where section='{}'".format(nb3))
		for n in gr:
			h=n[0]
		cb=db1.cursor()
		cb.execute('select bransh from branchs')
		f=cb.fetchall()
		for d in f:
			r.append(d[0])
		if nb4 in r:
			flash("اسم الفرع موجود")
			return redirect(url_for("addsec"))
		else:
			
			db1.execute("insert into branchs(ID,bransh)values(?,?)",(h,nb4))
			db1.commit()
			flash("تم اضافة الفرع بنجاح")
			return redirect(url_for("addsec"))
@app.route("/serr1",methods=['GET','POST'])
def serr1():
	nb= request.form['s22']
	db1=sqlite3.connect('lib1.db')
	cb=db1.cursor()
	cb.execute("select * from sections where section='{}'".format(nb))
	df=cb.fetchall()
	for n in df:
		h=n[0]
	cb=db1.cursor()
	cb.execute("select bransh from branchs where ID='{}'".format(h))
	f2=cb.fetchall()
	#cb.execute("select distinct section from sections where section='{}'".format(nb))
	#f1=cb.fetchall()
	
	return render_template('pageserch.html',f2=f2,f11=nb,pp3=sse("k"))
@app.route("/moddatbok1",methods=['GET','POST'])
def moddatbok1():
	return render_template('moddatabook.html',pp3=sse("k"))
@app.route("/moddatbok2",methods=['GET','POST'])
def moddatbok2():
	nk= request.form['namebook']
	db1=sqlite3.connect('lib1.db')
	cb=db1.cursor()
	cb.execute("select * from books where nambook like '%{}%' or alm like '%{}%'".format(nk,nk))
	df=cb.fetchall()
	g1=str(len(df))
	flash(g1+"عدد نتائج البحث")
	return render_template('moddatabook.html',df=df,pp3=sse("k"))

@app.route("/moddatbok3<mdb>",methods=['GET','POST'])
def moddatbok3(mdb):
	db1=sqlite3.connect('lib1.db')
	cb=db1.cursor()
	cb.execute("select * from books where nambook='{}'".format(mdb))
	df=cb.fetchall()
	cb.execute("select * from sections")
	f1=cb.fetchall()
	cb.execute("select * from branchs")
	f2=cb.fetchall()
	cb.execute("select * from writtens")
	f3=cb.fetchall()
	cb.execute("select * from puplichouse")
	f4=cb.fetchall()
	
	return render_template('mod2databook.html',df=df,f1=f1,f2=f2,f3=f3,f4=f4,k=mdb,pp3=sse("k"))
@app.route("/moddatbok4",methods=['GET','POST'])
def moddatbok4():
	f=os.getcwd()
	d1="/static/img/"
	nk0= request.form['namebook0']
	g1= request.form['namebook1']
	nk1=g1+'.pdf'
	nk2= request.form['namebook2']
	nk3= request.form['namebook3']
	nk4= request.form['namebook4']
	nk5= request.form['namebook5']
	nk6= request.form['namebook6']
	db1=sqlite3.connect('lib1.db')
	cb=db1.cursor()#update log set username='{}',
	cb.execute("update books set nambook='{}',alm='{}',spic='{}',objbook='{}',homespac='{}',agespac='{}',linkimg='{}' where nambook='{}'".format(nk1,nk2,nk3,nk4,nk5,nk6,d1+nk1[:-3]+'jpg',nk0))
	db1.commit()
	os.renames(f+d1+nk0,f+d1+nk1)
	os.renames(f+d1+nk0[:-3]+'jpg',f+d1+nk1[:-3]+'jpg')
	flash("تم تعديل الكتاب")
	return redirect(url_for("moddatbok1"))
@app.route("/ddb<dddd>",methods=['GET','POST'])
def rebok(dddd):
	f=os.getcwd()
	d1="/static/img/"
	db1=sqlite3.connect('lib1.db')
	cb=db1.cursor()
	cb.execute("delete from books where nambook='{}'".format(dddd))
	db1.commit()
	os.remove(f+d1+dddd)
	os.remove(f+d1+dddd[:-3]+'jpg')
	flash("تم حذف الكتاب")
	return redirect(url_for("moddatbok1"))
@app.route("/serinmin",methods=['GET','POST'])#search in page main
def serinmin():
	nk5= request.form['ll1']
	db1=sqlite3.connect('lib1.db')
	cb=db1.cursor()
	cb.execute("select * from books where  nambook like '%{}%'or alm like '%{}%'".format(nk5,nk5))
	se=cb.fetchall()
	pl=str(len(se))
	return render_template('mser.html',gm=nk5,pl=pl,se=se,pp3=sse("k"),tp='page main')

@app.route("/addmolf1",methods=['GET','POST'])#search in page main
def addmolf1():
	return render_template('addmolf.html',pp3=sse("k"))


@app.route("/addmolf2",methods=['GET','POST'])#search in page main
def addmolf2():
	r=[]
	nk1= request.form['wri']
	nk2= request.form['infw']
	db1=sqlite3.connect('lib1.db')
	cb=db1.cursor()
	cb.execute('select written from writtens')
	f=cb.fetchall()
	for d in f:
		r.append(d[0])
	if nk1 in r:
		flash("اسم المؤلف موجود")
		return redirect(url_for("addmolf1"))
	else:
			
		db1.execute("insert into writtens(written,information)values(?,?)",(nk1,nk2))
		db1.commit()
		flash("تم اضافة مؤلف جديد")
		return redirect(url_for("addmolf1"))
@app.route("/addhouse",methods=['GET','POST'])#search in page main
def addhouse():
	r=[]
	nk1= request.form['nhous']
	nk2= request.form['infhous']
	db1=sqlite3.connect('lib1.db')
	cb=db1.cursor()
	cb.execute('select housespac from puplichouse')
	f=cb.fetchall()
	for d in f:
		r.append(d[0])
	if nk1 in r:
		flash("اسم دار النشر موجودة")
		return redirect(url_for("addmolf1"))
	else:
		db1.execute("insert into puplichouse(housespac,information)values(?,?)",(nk1,nk2))
		db1.commit()
		flash("تم اضافة دار نشر جديدة")
		return redirect(url_for("addmolf1"))
@app.route("/modsection",methods=['GET','POST'])#search in page main
def modsection():
	db1=sqlite3.connect('lib1.db')
	cb=db1.cursor()
	cb.execute("select * from sections")
	se=cb.fetchall()
	cb.execute("select * from branchs")
	pl=cb.fetchall()
	return render_template('mod section.html',pl=pl,se=se,pp3=sse("k"),tp='page main')
@app.route("/modsection2",methods=['GET','POST'])#search in page main
def modsection2():
	sc1= request.form['smodc1']
	sc2= request.form['smodc2']
	db1=sqlite3.connect('lib1.db')
	cb=db1.cursor()
	cb.execute("update sections set section='{}' where section='{}'".format(sc2,sc1))
	db1.commit()
	cb.execute("update books set spic='{}' where spic='{}'".format(sc2,sc1))
	db1.commit()
	cb.execute("update addus set tybook='{}' where tybook='{}'".format(sc2,sc1))
	db1.commit()
	flash("تم تعديل القسم بنجاح")
	return redirect(url_for("modsection"))
@app.route("/modbranch",methods=['GET','POST'])#search in page main
def modbranch():
	sc1= request.form['smodb1']
	sc2= request.form['smodb2']
	db1=sqlite3.connect('lib1.db')
	cb=db1.cursor()
	cb.execute("update branchs set bransh='{}' where bransh='{}'".format(sc2,sc1))
	db1.commit()
	cb.execute("update books set objbook='{}' where objbook='{}'".format(sc2,sc1))
	db1.commit()
	cb.execute("update addus set objbook='{}' where objbook='{}'".format(sc2,sc1))
	db1.commit()
	flash("تم تعديل الفرع بنجاح")
	return redirect(url_for("modsection"))
@app.route("/modwriten1",methods=['GET','POST'])#search in page main
def modwriten1():
	db1=sqlite3.connect('lib1.db')
	cb=db1.cursor()
	cb.execute("select * from writtens")
	se=cb.fetchall()
	cb.execute("select * from puplichouse")
	pl=cb.fetchall()
	return render_template('modmolf.html',pl=pl,se=se,pp3=sse("k"),tp='page main')
@app.route("/modwriten2",methods=['GET','POST'])#search in page main
def modwriten2():
	sc1= request.form['smw1']
	sc2= request.form['smw2']
	sc3= request.form['smw3']
	db1=sqlite3.connect('lib1.db')
	cb=db1.cursor()
	cb.execute("update writtens set written='{}', information='{}' where written='{}'".format(sc2,sc3,sc1))
	db1.commit()
	cb.execute("update books set alm='{}' where alm='{}'".format(sc2,sc1))
	db1.commit()
	cb.execute("update addus set alm='{}' where alm='{}'".format(sc2,sc1))
	db1.commit()
	flash("تم تعديل المؤلف بنجاح")
	return redirect(url_for("modwriten1"))

@app.route("/modhous",methods=['GET','POST'])#search in page main
def modhous():
	sc1= request.form['smh1']
	sc2= request.form['smh2']
	sc3= request.form['smh3']
	db1=sqlite3.connect('lib1.db')
	cb=db1.cursor()
	cb.execute("update puplichouse set housespac='{}', information='{}' where housespac='{}'".format(sc2,sc3,sc1))
	db1.commit()
	cb.execute("update books set homespac='{}' where homespac='{}'".format(sc2,sc1))
	db1.commit()
	cb.execute("update addus set homespac='{}' where homespac='{}'".format(sc2,sc1))
	db1.commit()
	flash("تم تعديل دار النشر بنجاح")
	return redirect(url_for("modwriten1"))
@app.route("/addbookroot",methods=['GET','POST'])
def addbookroot():
	nb= request.form['tybok']
	db1=sqlite3.connect('lib1.db')
	cb=db1.cursor()
	cb.execute("select * from sections where section='{}'".format(nb))
	df=cb.fetchall()
	for n in df:
		h=n[0]
	cb=db1.cursor()
	ch=cb.execute("select max(numbook) from books")#find small value in numbook
	for n in ch:
		y=n[0]
	cb.execute("select bransh from branchs where ID='{}'".format(h))
	f2=cb.fetchall()
	ch=cb.execute("select * from writtens")
	mol=ch.fetchall()
	ch=cb.execute("select * from puplichouse")
	pup=ch.fetchall()
	#cb.execute("select distinct section from sections where section='{}'".format(nb))
	#f1=cb.fetchall()
	
	return render_template('sign in.html',mol=mol,y=int(y)+1,pup=pup,f2=f2,f11=nb,pp3=sse("k"))
@app.route("/showwrit",methods=['GET','POST'])
def showwrit():
	db1=sqlite3.connect('lib1.db')
	cb=db1.cursor()
	cb.execute("select * from writtens")
	df=cb.fetchall()
	return render_template('writtenn.html',df=df,pp3=sse("k"))
@app.route("/showspac",methods=['GET','POST'])
def showspac():
	db1=sqlite3.connect('lib1.db')
	cb=db1.cursor()
	cb.execute("select * from puplichouse")
	df=cb.fetchall()
	return render_template('spachous.html',df=df,pp3=sse("k"))
@app.route("/admin",methods=['GET','POST'])
@login_required
def admin():
	r1=[]
	db1=sqlite3.connect('lib1.db')
	db1.row_factory=sqlite3.Row
	ff=db1.execute("select * from log where prerogatives='{}'".format("yes"))
	for n in ff:
		r1.append(n["username"])
	if session['logged_in'] in r1:
		if session['logged_in']=='admin':
			db1=sqlite3.connect('lib1.db')
			cb=db1.cursor()
			cb.execute("select * from log where username is not'{}'".format('admin'))
			df=cb.fetchall()
			return render_template('admin.html',df=df,pp3=sse("k"))
		else:
			flash("ليس لديك صلاحيات الدخول")
			return redirect(url_for('login1'))
	else:
		flash("ليس لديك صلاحيات الدخول")
		return redirect(url_for('login1'))
@app.route("/admin1<h1>",methods=['GET','POST'])
def addmod(h1):
	db1=sqlite3.connect('lib1.db')
	cb=db1.cursor()
	cb.execute("select prerogatives from log where username='{}'".format(h1)) 
	df=cb.fetchall()
	for n in df:
		y=n[0]
	if y=='yes':
		cb.execute("update log set prerogatives='{}' where username='{}'".format('no',h1))
		db1.commit()
		flash("تم حذف الصلاحيات")
		return redirect(url_for('admin'))
	else:
		cb.execute("update log set prerogatives='{}' where username='{}'".format('yes',h1))
		db1.commit()
		flash("تم اضافة الصلاحيات")
		return redirect(url_for('admin'))
@app.route("/rep",methods=['GET','POST'])
@login_required
def rep():
	db1=sqlite3.connect('lib1.db')
	cb=db1.cursor()
	cb.execute("select count(nambook),objbook,spic from books left join branchs on books.objbook= branchs.bransh group by objbook")
	ff3=cb.fetchall()
	return render_template('report.html',ff3=ff3,pp3=sse("k"))	
if __name__ == "__main__":
	app.run(debug=False,host='0.0.0.0', port=5000)
