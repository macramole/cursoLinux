import serial
import subprocess
import time

def hacer():
	#subprocess.call([ "cvlc", "--play-and-exit", "../../python_games/beep1.ogg" ])
	#subprocess.call(["aplay","-f","cd","../../python_games/match1.wav"])
	subprocess.call(["omxplayer","../../Python_Eyetracker_Ur3/Eyetracker_Ur3_Realtime_Final_Imagenes/images/track/1.jpg"])
	time.sleep( 2 )

sArduino = serial.Serial("/dev/ttyACM0", 9600)

while True:
	res = sArduino.readline()
	res = res.strip("\n").strip("\r")
	#print res
	if res == "0":
		print("haciendo")
		hacer()
		sArduino.flush()
