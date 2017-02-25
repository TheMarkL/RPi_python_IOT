#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD) #BCM -- GPIO Number ; BOARD -- Pin Number
GPIO.setup(12,GPIO.OUT)
GPIO.setup(23, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(24, GPIO.IN, pull_up_down = GPIO.PUD_UP)


try:
	while True:


		GPIO.wait_for_edge(23, GPIO.RISING)
		print("Button 1 Pressed")
		GPIO.output(12,True)

		GPIO.wait_for_edge(23, GPIO.FALLING)
		print("Button 1 released")

		GPIO.wait_for_edge(24, GPIO.FALLING)
		print("Button 2 Pressed")
		GPIO.output(12,False)
		GPIO.wait_for_edge(24, GPIO.RISING)
		print("Button 2 released")

		

except KeyboardInterrupt: # wait for ctrl+C Command
	GPIO.cleanup() # Will delete GPIO Setup  
 	print "hello World"


	
