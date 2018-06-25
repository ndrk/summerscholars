#!/usr/bin/python

import RPi.GPIO as GPIO
import time
from random import randint

#Setup GPIO using BCM Numbering for I/O
GPIO.setmode(GPIO.BCM)

#Defind the pins that are used for the LEDs and switches
numLEDs = 3
leds = [16, 12, 21]
switches = [19, 13, 26]
FLASH_TIME = 0.5
TIMEOUT_TIME = 2

switchLEDMap = dict(zip(leds, switches))

sequence = []
gameOver = False

#Set the pins as inputs and outputs
for j in leds:
    GPIO.setup(j, GPIO.OUT)
for j in switches:
    GPIO.setup(switches, GPIO.IN, GPIO.PUD_UP)

print ("Welcome to Simon Says!")

while gameOver == False:
    #Add a new step to the flashing sequence
    randNum = randint(0, numLEDs-1)

    sequence.append(leds[randNum])

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
        for j in switches:
            GPIO.add_event_detect(j, GPIO.FALLING)

        startTime = time.time()

        while btnPressed == 0:
            for j in switches:
                if GPIO.event_detected(j):
                    print ("Button Pressed")
                    btnPressed = j
                    break
            if time.time() - startTime > TIMEOUT_TIME:
                print ("Time is up!!")
                gameOver = True
                break
            time.sleep(0.0001)

        for j in switches:
            GPIO.remove_event_detect(j)

        time.sleep(FLASH_TIME)
        
        #Does input match the sequence step?
        if btnPressed != switchLEDMap[i]:
            print ("Game Over")
            gameOver = True
            break
        else:
            GPIO.output(i, GPIO.HIGH)
            time.sleep(FLASH_TIME)
            GPIO.output(i, GPIO.LOW)
    
for i in range(3):
    for j in leds:
        GPIO.output(j, GPIO.HIGH)
    time.sleep(FLASH_TIME)
    for j in leds:
        GPIO.output(j, GPIO.LOW)
    time.sleep(FLASH_TIME)

print ("Thanks for playing!")

GPIO.cleanup()
