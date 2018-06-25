#!/usr/bin/python

import RPi.GPIO as GPIO

#Setup GPIO using BCM Numbering for I/O
GPIO.setmode(GPIO.BCM)

#Defind the pins that are used for the LEDs
LEFT_LED = 16
RIGHT_LED = 21

#Set the pins as outputs
GPIO.setup(LEFT_LED, GPIO.OUT)
GPIO.setup(RIGHT_LED, GPIO.OUT)

print ("Welcome to Simon Says!")

GPIO.cleanup()
