#!/usr/bin/python

import RPi.GPIO as GPIO

#Setup GPIO using BCM Numbering for I/O
GPIO.setmode(GPIO.BCM)

#Defind the pins that are used for the LEDs and switches
LEFT_LED = 16
RIGHT_LED = 21
LEFT_SW = 19
RIGHT_SW = 26

#Set the pins as inputs and outputs
GPIO.setup(LEFT_LED, GPIO.OUT)
GPIO.setup(RIGHT_LED, GPIO.OUT)
GPIO.setup(LEFT_SW, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(RIGHT_SW, GPIO.IN, GPIO.PUD_UP)

print ("Welcome to Simon Says!")

GPIO.cleanup()
