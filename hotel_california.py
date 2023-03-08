import RPi.GPIO as GPIO
import time
import datetime
import requests
import json
import threading


""" 
NO_PLAY=[0, 0, 0, 0]
FRET1=[0, 0, 0, 1]
FRET2=[0, 0, 1, 0]
FRET3=[0, 0, 1, 1]
FRET4=[0, 1, 0, 0]
FRET5=[0, 1, 0, 1]
FRET6=[0,1, 1, 0]
FRET7=[0, 1, 1, 1]

FRET8=[1, 0, 0, 0]
FRET9=[1, 0, 0, 1]
FRET10=[1, 0, 1, 0]
FRET11=[1, 0, 1, 1]
FRET12=[1, 1, 0, 0]
FRET13=[1, 1, 0, 1]
FRET14=[1, 1, 1, 0]
OPEN_FRET=[1, 1, 1, 1] = 15
"""

#en, a2, a1, a0. 
frets=[[0, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0], [0, 0, 1, 1], [0, 1, 0, 0], [0, 1, 0, 1], [0,1, 1, 0], [0, 1, 1, 1], [1, 0, 0, 0], [1, 0, 0, 1], [1, 0, 1, 0], [1, 0, 1, 1], [1, 1, 0, 0], [1, 1, 0, 1], [1, 1, 1, 0], [1, 1, 1, 1]]

#Pins connected to decoders en, a2, a1, a0. strings 1 to 6
stringPins=[[17, 4, 3, 2], [9, 10, 22, 27], [6, 5, 0, 11], [21, 26, 19, 13], [23, 18, 15, 14], [7, 8, 25, 24]]

def playNote(string, fret):
    currentString=stringPins[string-1]
    currentFret=frets[fret]
    ledSwitch(currentString[0], currentFret[0]) #en
    ledSwitch(currentString[1], currentFret[1]) #a2
    ledSwitch(currentString[2], currentFret[2]) #a1
    ledSwitch(currentString[3], currentFret[3]) #a0

def setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)      # use extension GPIO Numbering

    #set all pins to output pins
    for string in stringPins:
        for pin in string:
            GPIO.setup(pin, GPIO.OUT, initial=False)

#lights up whole fret one by one
def startUp():
    for fret in frets:
        for string in stringPins:
            ledSwitch(string[0], fret[0])
            ledSwitch(string[1], fret[1])
            ledSwitch(string[2], fret[2])
            ledSwitch(string[3], fret[3])
        time.sleep(3)

#turns all LEDs off
def allOff():
    for string in stringPins:
        for pin in string:
            GPIO.output(pin, GPIO.LOW)

#clears LEDs for string
def stringClear(string):
    playNote(string, 0)

#switches LED state
def ledSwitch(pin, state):
    if(state==1):
        GPIO.output(pin, GPIO.HIGH)
    else: 
        GPIO.output(pin, GPIO.LOW)

def hotel():
    playNote(1, 11)
    stringClear()
    playNote(2, 10)
    time.sleep(0.003)
    playNote(2, 12)
    stringClear()

    playNote(2, 10)
    playNote(2, 11)
    playNote(2, 12)
    stringClear(2)

    playNote(3, 9)
    
    playNote(3, 7)
    playNote(3, 9)
    stringClear(3)

    playNote(2, 7)
    stringClear(2)
    playNote(3, 7)
    stringClear(3)
    playNote(4, 8)
    stringClear(4)

    playNote(4, 9)
    playNote(4, 12)
    playNote(4, 9)
    playNote(4, 7)
    stringClear(4)

    playNote(3, 7)
    playNote(3, 9)
    stringClear(3)

    playNote(2, 7)
    stringClear(2)
    playNote(3, 7)
    stringClear(3)

    playNote(4, 9)
    playNote(4, 7)
    playNote(4, 9)
    playNote(4, 7)
    stringClear(4)

    playNote(2, 10)
    stringClear(2)
    playNote(1, 10)
    stringClear(1)

    playNote(2, 10)
    playNote(2, 7)
    playNote(2, 10)
    playNote(2, 8)
    stringClear(2)

    playNote(1,7)
    playNote(2,7)
    playNote(1,10)
    playNote(1,10)
    playNote(1,10)
    playNote(1,7)
    playNote(2,10)
    playNote(1,10)
    playNote(2,10)
    playNote(2,8)
    playNote(3,9)
    playNote(1,10)
    playNote(3,9)
    playNote(3,7)
    playNote(3,7)
    playNote(3,6)
    playNote(3,7)

    playNote(3,7)
    playNote(3,9)
    playNote(2,7)
    playNote(2,7)
    playNote(3,9)
    playNote(3,7)
    playNote(3,9)
    playNote(2,7)
    playNote(2,7)
    playNote(2,7)
    playNote(3,9)
    playNote(3,7)
    playNote(3,9)
    playNote(2,7)
    playNote(2,10)
    playNote(3,9)
    playNote(2,7)
    playNote(1,7)
    playNote(3,9)
    playNote(3,9)
    playNote(3,7)
    playNote(3,9)
    playNote(2,7)
    playNote(2,10)
    playNote(3,9)
        #part 2 (vid)
    playNote(2,7)
    playNote(1,7)
    playNote(3,9)
    playNote(1,7)
    playNote(2,7)
    playNote(3,9)
    playNote(2,7)
    playNote(2,7)
    playNote(3,9)
    playNote(3,9)
    playNote(3,7)
    playNote(3,9)
    playNote(3,7)
    playNote(3,9)

    playNote(3,12)
    playNote(3,9)
    playNote(3,11)
    playNote(3,7)
    playNote(4,9)
    playNote(2,10)
    playNote(1,7)
    playNote(2,10)
    playNote(2,7)
    playNote(2,10)
    playNote(2,11)
    playNote(2,12)
    playNote(1,10)
    playNote(2,12)
    playNote(2,11)
    playNote(2,10)
    playNote(2,9)

    playNote(3,14)
    playNote(2,12)
    playNote(2,15)
    playNote(1,12)
    playNote(2,15)
    playNote(2,17)
    playNote(1,17)
    playNote(2,17)
    playNote(2,15)
    playNote(2,17)
    playNote(2,15)
    
    playNote(2,17)
    playNote(1,15)
    playNote(1,16)
    playNote(1,17)
    playNote(2,17)
    playNote(2,15)
    playNote(2,17)
    playNote(2,17)
    playNote(2,15)
    playNote(2,17)
    playNote(1,17)
    playNote(1,17)
    playNote(2,17)
    playNote(2,17)

    playNote(2,17)
    playNote(2,15)
    playNote(2,17)
    playNote(1,17)
    playNote(1,17)
    playNote(2,17)
    playNote(2,17)
    playNote(2,17)
    playNote(2,15)
    playNote(1,17)

    playNote(1,9)
    playNote(1,9)
    playNote(1,7)
    playNote(1,9)
        #part 3 (vid)
    playNote(2,12)
    playNote(1,10)
    playNote(2,12)
    playNote(1,10)
    playNote(3,11)
    playNote(3,10)
    playNote(3,9)
    playNote(3,8)
    playNote(3,7)
    playNote(4,9)
    playNote(4,8)
    playNote(2,9)
    playNote(2,10)
    playNote(2,11)

    playNote(2,17)
    playNote(2,17)
    playNote(2,17)
    playNote(2,17)
    playNote(2,17)
    playNote(2,17)
    playNote(2,17)
    playNote(2,17)
    playNote(2,17)
    playNote(2,17)
    playNote(2,17)
    playNote(2,15)
    playNote(3,16)
    playNote(2,17)
    playNote(2,15)
    playNote(3,16)

    playNote(3,14)
    playNote(4,16)
    playNote(4,15)
    playNote(4,14)
    playNote(4,12)
    playNote(4,14)
    playNote(4,15)
    playNote(4,16)
    playNote(3,14)

    playNote(3,9)
    playNote(1,7)
    playNote(2,7)
    playNote(2,10)
    playNote(3,9)
    playNote(2,7)
    playNote(3,7)
    playNote(3,9)
    playNote(4,9)
    playNote(3,7)
    playNote(5,9)
    playNote(4,7)
    playNote(5,9)
    playNote(5,8)
    playNote(5,7)
    playNote(5,5)
    playNote(5,7)
    playNote(5,8)
    playNote(5,9)
    playNote(4,7)
    playNote(1,10)
    playNote(1,7)
    playNote(2,10)
    playNote(3,9)
    playNote(3,9)
    playNote(3,7)

    playNote(3,7)
    playNote(3,9)
    playNote(3,9)
    playNote(2,7)
    playNote(2,7)
    playNote(2,7)
    playNote(1,6)
    playNote(1,7)
    playNote(1,9)

    playNote(2,12)
    playNote(1,10)
    playNote(4,12)
    playNote(2,12)
    playNote(4,12)
    playNote(2,10)
    playNote(5,12)
    playNote(3,12)
    playNote(5,12)
    playNote(3,11)
    playNote(5,12)
    playNote(4,12)
    playNote(5,12)
    playNote(5,11)
    playNote(5,10)
    playNote(5,9)
    playNote(5,10)
    playNote(5,11)
    playNote(5,12)
    playNote(3,11)

    playNote(1,12)
    playNote(1,10)
    playNote(2,10)
    playNote(3,12)
    playNote(3,12)
    playNote(3,11)
    playNote(3,11)
    playNote(3,12)
    playNote(3,12)
    playNote(2,10)
    playNote(2,12)
    playNote(2,11)
    playNote(2,14)
    playNote(2,15)
    playNote(2,17)
        #part 4 (vid)
    playNote(1,10)
    playNote(1,7)
    playNote(2,7)
    playNote(1,10)
    playNote(1,7)
    playNote(2,7)
    playNote(1,10)
    playNote(1,7)
    playNote(2,7)
    playNote(1,10)
    playNote(1,7)
    playNote(2,7)
    playNote(1,10)
    playNote(1,7)
    playNote(2,7)
    playNote(1,9)
    playNote(1,6)
    playNote(2,7)
    playNote(1,9)
    playNote(1,6)
    playNote(2,7)
    playNote(1,9)
    playNote(1,6)
    playNote(1,9)
    playNote(1,10)
    playNote(1,11)
    playNote(1,12)
    playNote(1,13)
    playNote(1,14)

    playNote(1,9)
    playNote(1,5)
    playNote(2,5)
    playNote(1,9)
    playNote(1,5)
    playNote(2,5)
    playNote(1,9)
    playNote(1,5)
    playNote(2,5)
    playNote(1,9)
    playNote(1,5)
    playNote(2,5)
    playNote(1,9)
    playNote(1,5)
    playNote(2,5)
    playNote(1,7)
    playNote(1,4)
    playNote(2,5)
    playNote(1,7)
    playNote(1,4)
    playNote(2,5)
    playNote(1,7)
    playNote(1,4)
    playNote(1,7)
    playNote(1,8)
    playNote(1,9)
    playNote(1,10)
    playNote(1,11)
    playNote(1,12)

    playNote(1,7)
    playNote(1,3)
    playNote(2,3)
    playNote(1,7)
    playNote(1,3)
    playNote(2,3)
    playNote(1,7)
    playNote(1,3)
    playNote(2,3)
    playNote(1,7)
    playNote(1,3)
    playNote(2,3)
    playNote(1,7)
    playNote(1,3)
    playNote(2,3)
    playNote(1,5)
    playNote(1,2)
    playNote(2,3)
    playNote(1,5)
    playNote(1,2)
    playNote(2,3)
    playNote(1,5)
    playNote(1,2)
    playNote(1,5)
    playNote(1,6)
    playNote(1,7)
    playNote(1,8)
    playNote(1,9)
    playNote(1,10)

    playNote(1,3)
    playNote(1,15) #0 (these 15 are = 0, previous 15s were 15 itself)
    playNote(2,15) #0
    playNote(1,3)
    playNote(1,15) #0
    playNote(2,15) #0
    playNote(1,3)
    playNote(1,15) #0
    playNote(2,15) #0
    playNote(1,3)
    playNote(1,15) #0
    playNote(2,15)
    playNote(1,3)
    playNote(1,15) #0
    playNote(2,15) #0
    playNote(1,6)
    playNote(1,2)
    playNote(2,2)
    playNote(1,6)
    playNote(1,2)
    playNote(2,2)
    playNote(1,6)
    playNote(1,2)
    playNote(1,6)
    playNote(1,7)
    playNote(1,8)
    playNote(1,9)

    # up to 2 minute and 58 seconds

    







    






