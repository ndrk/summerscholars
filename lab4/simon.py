#!/usr/bin/python

import RPi.GPIO as GPIO
import time
from random import randint

#Setup GPIO using BCM Numbering for I/O
GPIO.setmode(GPIO.BCM)

#Defind the pins that are used for the LEDs and switches
LEFT_LED = 16
RIGHT_LED = 21
LEFT_SW = 19
RIGHT_SW = 26
FLASH_TIME = 1
TIMEOUT_TIME = 2

switchLEDMap = { LEFT_LED:LEFT_SW, RIGHT_LED:RIGHT_SW }

#Set the pins as inputs and outputs
GPIO.setup(LEFT_LED, GPIO.OUT)
GPIO.setup(RIGHT_LED, GPIO.OUT)
GPIO.setup(LEFT_SW, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(RIGHT_SW, GPIO.IN, GPIO.PUD_UP)

print ("Welcome to Simon Says!")

#Flash the randomly selected LED to the user
randNum = randint(0, 1)

if randNum == 0:
    led = LEFT_LED
else:
    led = RIGHT_LED

#Flash the sequence for the player
GPIO.output(led, GPIO.HIGH)
time.sleep(FLASH_TIME)
GPIO.output(led, GPIO.LOW)
time.sleep(FLASH_TIME)

btnPressed = 0

#Read inputs
GPIO.add_event_detect(LEFT_SW, GPIO.FALLING)
GPIO.add_event_detect(RIGHT_SW, GPIO.FALLING)

startTime = time.time()

while True:
    if GPIO.event_detected(LEFT_SW):
        print ("Left Button Pressed")
        btnPressed = LEFT_SW
        break
    if GPIO.event_detected(RIGHT_SW):
        print ("Right Button Pressed")
        btnPressed = RIGHT_SW
        break
    if time.time() - startTime > TIMEOUT_TIME:
        print ("Time is up!!")
        gameOver = True
        break
    time.sleep(0.0001)

GPIO.remove_event_detect(LEFT_SW)
GPIO.remove_event_detect(RIGHT_SW)

#Does input match the sequence step?
if btnPressed != switchLEDMap[led]:
    print ("You Lost")
else:
    print ("You Win!")

print ("Thanks for playing!")

GPIO.cleanup()
