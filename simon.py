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

sequence = []
gameOver = False

#Set the pins as inputs and outputs
GPIO.setup(LEFT_LED, GPIO.OUT)
GPIO.setup(RIGHT_LED, GPIO.OUT)
GPIO.setup(LEFT_SW, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(RIGHT_SW, GPIO.IN, GPIO.PUD_UP)

print ("Welcome to Simon Says!")

while gameOver == False:
    #Add a new step to the flashing sequence
    randNum = randint(0, 1)

    if randNum == 0:
        sequence.append(LEFT_LED)
    else:
        sequence.append(RIGHT_LED)

    #Flash the sequence for the player
    for i in sequence:
        print ("Playing Sequence...")
        time.sleep(FLASH_TIME)
        GPIO.output(i, GPIO.HIGH)
        time.sleep(FLASH_TIME)
        GPIO.output(i, GPIO.LOW)

    #Read in the player's sequence
    for i in sequence:
        btnPressed = 0

        #Read inputs
        GPIO.add_event_detect(LEFT_SW, GPIO.FALLING)
        GPIO.add_event_detect(RIGHT_SW, GPIO.FALLING)

        startTime = time.time()

        while btnPressed == 0:
            if GPIO.event_detected(LEFT_SW):
                print ("Left Button Pressed")
                btnPressed = LEFT_SW
            if GPIO.event_detected(RIGHT_SW):
                print ("Right Button Pressed")
                btnPressed = RIGHT_SW
            if time.time() - startTime > TIMEOUT_TIME:
                print ("Time is up!!")
                gameOver = True
                break
            time.sleep(0.0001)

        GPIO.remove_event_detect(LEFT_SW)
        GPIO.remove_event_detect(RIGHT_SW)

        time.sleep(0.5)
        
        #Does input match the sequence step?
        if btnPressed != switchLEDMap[i]:
            print ("Game Over")
            gameOver = True
            break

print ("Thanks for playing!")

GPIO.cleanup()
