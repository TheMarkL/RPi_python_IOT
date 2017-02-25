
#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD) #BCM -- GPIO Number ; BOARD -- Pin Number
GPIO.setup(12,GPIO.OUT)

try:
	while True:
		GPIO.output(12,True)
		time.sleep(0.5)
		GPIO.output(12,False)
		time.sleep(0.5)

except KeyboardInterrupt: # wait for ctrl+C Command
	GPIO.cleanup() # Will delete GPIO Setup  
 	print "hello World"


	


print "hello world"
