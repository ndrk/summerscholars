#!/usr/bin/python

import RPi.GPIO as GPIO
import time
from random import randint

#Setup GPIO using BCM Numbering for I/O
GPIO.setmode(GPIO.BCM)

#Defind the pins that are used for the LEDs
LEFT_LED = 16
RIGHT_LED = 21

FLASH_TIME = 1

#Set the pins as outputs
GPIO.setup(LEFT_LED, GPIO.OUT)
GPIO.setup(RIGHT_LED, GPIO.OUT)

print ("Welcome to Simon Says!")

#Flash the randomly selected LED to the user
randNum = randint(0, 1)

if randNum == 0:
    led = LEFT_LED
else:
    led = RIGHT_LED

#Flash a LED
GPIO.output(led, GPIO.HIGH)
time.sleep(FLASH_TIME)
GPIO.output(led, GPIO.LOW)
time.sleep(FLASH_TIME)

print ("Thanks for playing!")

GPIO.cleanup()
