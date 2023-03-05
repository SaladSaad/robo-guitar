## Author: Bryce Perry
## Association: Senior Design Project; Team BDC; RoboGuitar
## This program will run a physical testbench to confirm correct wiring of 74HC238 type decoders with raspberry pi. The output terminal 
## should print the active decoder output concurrently with the expected output. This program is written for a specific circuit, so the 
## output statements will need to be changed for general use (see output table for in documentation for the 74HC238).
## For specific circuit this test bench correlates to, see wiring diagram
## write "16" as the command line argument when running this script to test the decoder as a 4 to 16 decoder. else it will run as 3 to 8
import sys
import os
from time import sleep
try:
    import RPi.GPIO as GPIO #written on a windows machine, sorry.
except:
    print("Caution: This program will only work on a Raspberry Pi with RPi.GPIO installed\nOnly output statements will be shown if not run on a Pi & no I/O pins will be toggled")
    sleep(1.5)
    os.system('clear')
    class RPi():    
        pass
    class GPIO():
        OUT= False
        BCM= False
        def setup(a, b): pass
        def setmode(c): pass
        def output(d,e): pass
    Rpi= GPIO()


GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(4, GPIO.OUT)
try:
    n = int(sys.argv[1])
except:
    n= 0

if (n==16): GPIO.setup(17, GPIO.OUT)
while True:
    print("Test bench begin:")
    sleep(0.1)
    os.system('clear')

    #state 0 (inactive)
    GPIO.output(2, False)
    GPIO.output(3, False)
    GPIO.output(4, False)
    if (n==16): GPIO.output(17, False) 
    os.system('clear')
    print("All lights off")
    sleep(1.5)
    #state 1
    GPIO.output(4, True)
    os.system('clear')
    print("1st fret and string")
    sleep(1.5)
    #state 2
    GPIO.output(3, True)
    GPIO.output(4, False)
    os.system('clear')
    print("2nd fret and string")
    sleep(1.5)
    #state 3
    GPIO.output(4, True)
    os.system('clear')
    print("3rd fret and string")
    sleep(1.5)
    #state 4
    GPIO.output(2, True)
    GPIO.output(3, False)
    GPIO.output(4, False)
    os.system('clear')
    print("4th fret and string")
    sleep(1.5)
    #state 5
    GPIO.output(4, True)
    os.system('clear')
    print("5th fret and string")
    sleep(1.5)
    #state 6
    GPIO.output(3, True)
    GPIO.output(4, False)
    os.system('clear')
    print("6th fret and string")
    sleep(1.5)
    #state 7
    GPIO.output(4, True)
    os.system('clear')
    print("7th fret and string")
    sleep(1.5)
    if(n==16):
    #state 8
        GPIO.output(17, True)
        GPIO.output(2, False)
        GPIO.output(3, False)
        GPIO.output(4, False)
        os.system('clear')
        print("8th fret and string")
        sleep(1.5)
    #state 9
        GPIO.output(4, True)
        os.system('clear')
        print("9th fret and string")
        sleep(1.5)
    #state 10
        GPIO.output(3, True)
        GPIO.output(4, False)
        os.system('clear')
        print("10th fret and string")
        sleep(1.5)
    #state 11
        GPIO.output(4, True)
        os.system('clear')
        print("11th fret and string")
        sleep(1.5)
    #state 12
        GPIO.output(2, True)
        GPIO.output(3, False)
        GPIO.output(4, False)
        os.system('clear')
        print("12th fret and string")
        sleep(1.5)
    #state 13
        GPIO.output(4, True)
        os.system('clear')
        print("13th fret and string")
        sleep(1.5)
    #state 14
        GPIO.output(3, True)
        GPIO.output(4, False)
        os.system('clear')
        print("14th fret and string")
        sleep(1.5)
    #state 15 (open string)
        GPIO.output(4, True)
        os.system('clear')
        print("only string, fret open")
        sleep(1.5)














