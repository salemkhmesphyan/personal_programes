import threading
global x
x=1
def printit():
	
	if x==5:
		print("stop")
	else:
		print("Hello, World!")	  
		x+=1
		threading.Timer(5.0, printit).start()

printit()
#from playsound import playsound
#playsound('audio.mp3')
