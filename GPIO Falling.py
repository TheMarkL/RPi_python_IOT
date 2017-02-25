#!/usr/bin/env python

import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM) #BCM -- GPIO Number ; BOARD -- Pin Number
GPIO.setup(23, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(24, GPIO.IN, pull_up_down = GPIO.PUD_UP)

while True:
	
	GPIO.wait_for_edge(23, GPIO.RISING)
	print("Button 1 Pressed")
	GPIO.wait_for_edge(23, GPIO.FALLING)
	print("Button 1 released")

	GPIO.wait_for_edge(24, GPIO.FALLING)
	print("Button 2 Pressed")
	GPIO.wait_for_edge(24, GPIO.RISING)
	print("Button 2 released")

GPIO.cleanup()

