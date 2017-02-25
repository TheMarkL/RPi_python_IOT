#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM) #BCM -- GPIO Number ; BOARD -- Pin Number
GPIO.setup(12,GPIO.OUT)
GPIO.setup(23, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(24, GPIO.IN, pull_up_down = GPIO.PUD_UP)


try:
	while True:

		if(GPIO.input(23) == 1):
			print "Button 1 pressed"
			GPIO.output(12,True)

		if(GPIO.input(24) == 0):
			print "Button 2 pressed"
			GPIO.output(12,False)


		

except KeyboardInterrupt: # wait for ctrl+C Command
	GPIO.cleanup() # Will delete GPIO Setup  
 	print "hello World"


	
