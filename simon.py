#!/usr/bin/python

import RPi.GPIO as GPIO
import time
from random import randint

#Setup GPIO using BCM Numbering for I/O
GPIO.setmode(GPIO.BCM)

#Defind the pins that are used for the LEDs and switches
LEFT_LED = 16
RIGHT_LED = 21
LEFT_BTN = 19
RIGHT_BTN = 26
FLASH_TIME = 1

switchLEDMap = { LEFT_LED:LEFT_BTN, RIGHT_LED:RIGHT_BTN }

#Set the pins as inputs and outputs
GPIO.setup(LEFT_LED, GPIO.OUT)
GPIO.setup(RIGHT_LED, GPIO.OUT)
GPIO.setup(LEFT_BTN, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(RIGHT_BTN, GPIO.IN, GPIO.PUD_UP)

sequence = []
gameOver = False

while gameOver == False:
  #Add a new step to the flashing sequence
  led = randint(0, 1)
  if led == 0:
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

  for i in sequence:
    btnPressed = 0
    
    #Read inputs
    GPIO.add_event_detect(LEFT_BTN, GPIO.FALLING)
    GPIO.add_event_detect(RIGHT_BTN, GPIO.FALLING)
  
    startTime = time.time()
  
    while True:
      if GPIO.event_detected(LEFT_BTN):
        print ("Left Button Pressed")
        btnPressed = LEFT_BTN
        break
      if GPIO.event_detected(RIGHT_BTN):
        print ("Right Button Pressed")
        btnPressed = RIGHT_BTN
        break
      if time.time() - startTime > 2*FLASH_TIME:
        print ("Time is up!!")
        gameOver = True
        break
      time.sleep(0.0001)
    
    GPIO.remove_event_detect(LEFT_BTN)
    GPIO.remove_event_detect(RIGHT_BTN)
    
    time.sleep(0.5)
      
    #Does input match the sequence step?
    if btnPressed != switchLEDMap[i]:
      print ("Game Over")
      gameOver = True
      break

GPIO.cleanup()
