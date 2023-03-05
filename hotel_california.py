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
OPEN_FRET=[1, 1, 1, 1] 
"""

frets=[[0, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0], [0, 0, 1, 1], [0, 1, 0, 0], [0, 1, 0, 1], [0,1, 1, 0], [0, 1, 1, 1], [1, 0, 0, 0], [1, 0, 0, 1], [1, 0, 1, 0], [1, 0, 1, 1], [1, 1, 0, 0], [1, 1, 0, 1], [1, 1, 1, 0], [1, 1, 1, 1]]

#Pins connected to decoders en, a2, a1, a0. strings 1 to 6
stringPins=[[17, 4, 3, 2], [9, 10, 22, 27], [6, 5, 0, 11], [21, 26, 19, 13], [23, 18, 15, 14], [7, 8, 25, 24]]

def playFret(string, fret):
    print()

def setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)      # use extension GPIO Numbering

    #set all pins to output pins
    for string in stringPins:
        for pin in string:
            GPIO.setup(pin, GPIO.OUT, initial=False)

def startUp():
    for fret in frets:
        for string in stringPins:
            ledSwitch()
def ledSwitch(pin, toggle):
    if(toggle==1):
        GPIO.output(pin, GPIO.HIGH)
    else: 
        GPIO.output(pin, LOW)