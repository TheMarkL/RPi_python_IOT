#! /usr/bin/python
 
import serial
from time import sleep
 
bluetoothSerial = serial.Serial( "/dev/rfcomm1", baudrate=9600 )
 
print bluetoothSerial.readline()
