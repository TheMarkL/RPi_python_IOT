# Python 3
from Tkinter import *
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12,GPIO.OUT)

class App:
  def __init__(self, master):
    frame = Frame(master)
    frame.pack()
    self.button = Button(frame, 
                         text="ON",
                         command=turn_on)
    self.button.pack(side=LEFT)
    self.slogan = Button(frame,
                         text="OFF",
                         command=self.turn_off)
    self.slogan.pack(side=LEFT)

def turn_on():
	GPIO.output(12,True)
	status="ON"
	
def turn_off():
	GPIO.output(12,False)
	status="OFF"


root = Tk()

w = Label(root, text="status")
w.pack()

root.mainloop()
