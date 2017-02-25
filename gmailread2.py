import feedparser
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(16,GPIO.OUT)
unread_count=0

USERNAME = "jokeman.santos@gmail.com" 
PASSWORD = "petermark" 

try:
	while True:
		response = feedparser.parse("https://" + USERNAME + ":" + PASSWORD + "@mail.google.com/gmail/feed/atom")  
		unread_count=int(response["feed"]["fullcount"])

		for i in range(0,unread_count): 
			print "(" + str((i+1)) + "/" + str(unread_count) + "): " + response['items'][i].title

		if (unread_count == 0):
			print "You have no email"
			GPIO.output(16,False)
		else:
			GPIO.output(16,True)
	
except	KeyboardInterrupt:
	GPIO.cleanup()
