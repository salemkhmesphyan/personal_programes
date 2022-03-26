import time
from pydub import AudioSegment
from pydub.playback import play
from playsound import playsound
print ("End : %s" % time.ctime())
#song = AudioSegment.from_mp3("hors.mp3",format="mp3" )
#play(song)
playsound("1.mp3")
