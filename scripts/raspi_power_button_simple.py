#!/usr/bin/env python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import subprocess

BUTTON_SHUTDOWN = 13

def shutDownPressed(channel):
	#shutDownRaspi()
	print("shutdown")

def setupGPIO():
	GPIO.setmode(GPIO.BCM)

	# hay un tercer parámetro que puede ser pull_up_down=GPIO.PUD_UP
	GPIO.setup( BUTTON_SHUTDOWN, GPIO.IN, pull_up_down=GPIO.PUD_UP )

	# el segundo parametro puede ser GPIO.RISING, GPIO.FALLING or GPIO.BOTH. 	
	GPIO.add_event_detect(BUTTON_SHUTDOWN, GPIO.RISING, callback=shutDownPressed, bouncetime=30)


def shutdownRaspi():
	subprocess.call( ["shutdown","now"] )

setupGPIO()

# otra opcion
# wait for up to 5 seconds for a rising edge (timeout is in milliseconds)
#channel = GPIO.wait_for_edge(channel, GPIO_RISING, timeout=5000)
#if channel is None:
#    print('Timeout occurred')
#else:
#    print('Edge detected on channel', channel)


while(True):
	pass
