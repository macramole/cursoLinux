#!/usr/bin/env python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import subprocess
from threading import Timer

PIN_SHUTDOWN = 19
BUTTON_SHUTDOWN = 13

shutdownPressedTime = 0
shutdownCurrentTimer = None
TIME_SHUTDOWN = 2


def _shutDownPressed(channel):
	global shutdownPressedTime
	if ( GPIO.input(channel) == 0 ):
		#print "started"
		shutdownPressedTime = 0
		_countPlayPressed()

def _countPlayPressed():
	global shutdownCurrentTimer
	shutdownCurrentTimer = Timer(1.0, _countPlayPressedTick)
	shutdownCurrentTimer.start()
def _countPlayPressedTick():
	global shutdownCurrentTimer, shutdownPressedTime
	#print "tick"
	if ( GPIO.input(BUTTON_SHUTDOWN) == 0 ):
		shutdownPressedTime += 1
		if ( shutdownPressedTime <= TIME_SHUTDOWN ):
			shutdownCurrentTimer = Timer(1.0, _countPlayPressedTick)
			shutdownCurrentTimer.start()
		else:
			print "shutdown"
			_shutdownTTY()
			t = Timer(1.0, _shutdownRaspi)
			t.start()

def _setupGPIO():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup( BUTTON_SHUTDOWN, GPIO.IN )
	GPIO.setup( PIN_SHUTDOWN, GPIO.OUT )

	GPIO.output( PIN_SHUTDOWN, True )

	GPIO.add_event_detect(BUTTON_SHUTDOWN, GPIO.BOTH, callback=_shutDownPressed, bouncetime=30)

def _setupTTY():
	subprocess.call( ["/home/pi/tty_on.sh"] )
def _shutdownTTY():
	subprocess.call( ["/home/pi/tty_off.sh"] )
def _shutdownRaspi():
	subprocess.call( ["shutdown","now"] )


_setupTTY()
_setupGPIO()


while(True):
	pass
