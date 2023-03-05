##TEAM BDC
##WRITTEN BY BRYCE, PUYA & SAAD

import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BOARD)

GPIO.setup(11, GPIO.OUT) #PIN 11 (GPIO 17) IS DECODER ADDRESS 0
GPIO.setup(13, GPIO.OUT) #PIN 13 (GPIO 27) IS DECODER ADDRESS 1
GPIO.setup(15, GPIO.OUT) #PIN 15 (GPIO 22) IS DECODER ADDRESS 2
##FOR OPEN FRET IT IS 000
##FIRST FRET IS 001
##SECOND FRET IS 010
##...SEVENTH FRET IS 111
## the pattern for the frets is 2, 2, 2, 4, 5, 5, 5, 4, 2, 2.
## the timing must be figured out by listening to the song and adjusting the delays.


#THIS IS FRET 2 (010). 
GPIO.output(11, GPIO.LOW)
GPIO.output(13, GPIO.HIGH)
GPIO.output(15, GPIO.LOW)
#SERVO FUNCTION (WRITE THIS)
time.sleep(0.3) ##find sleep time
GPIO.output(11, GPIO.LOW)
GPIO.output(13, GPIO.LOW)
GPIO.output(15, GPIO.LOW)

#THIS IS FRET 2 (010). 
GPIO.output(11, GPIO.LOW)
GPIO.output(13, GPIO.HIGH)
GPIO.output(15, GPIO.LOW)
#SERVO FUNCTION (WRITE THIS)
time.sleep(0.3) ##find sleep time
GPIO.output(11, GPIO.LOW)
GPIO.output(13, GPIO.LOW)
GPIO.output(15, GPIO.LOW)

#THIS IS FRET 2 (010). 
GPIO.output(11, GPIO.LOW)
GPIO.output(13, GPIO.HIGH)
GPIO.output(15, GPIO.LOW)
#SERVO FUNCTION (WRITE THIS)
time.sleep(0.3) ##find sleep time
GPIO.output(11, GPIO.LOW)
GPIO.output(13, GPIO.LOW)
GPIO.output(15, GPIO.LOW)

#THIS IS FRET 4 (100). 
GPIO.output(11, GPIO.LOW)
GPIO.output(13, GPIO.LOW)
GPIO.output(15, GPIO.HIGH)
#SERVO FUNCTION (WRITE THIS)
time.sleep(0.3) ##find sleep time
GPIO.output(11, GPIO.LOW)
GPIO.output(13, GPIO.LOW)
GPIO.output(15, GPIO.LOW)

#THIS IS FRET 5 (101).
GPIO.output(11, GPIO.HIGH)
GPIO.output(13, GPIO.LOW)
GPIO.output(15, GPIO.HIGH)
#SERVO FUNCTION *(WRITE THIS)
time.sleep(0.3) ##find sleep time
GPIO.output(11, GPIO.LOW)
GPIO.output(13, GPIO.LOW)
GPIO.output(15, GPIO.LOW)
time.sleep(0.3)
#THIS IS FRET 5 (101). 
GPIO.output(11, GPIO.HIGH)
GPIO.output(13, GPIO.LOW)
GPIO.output(15, GPIO.HIGH)
#SERVO FUNCTION (WWRITE THIS)
time.sleep(0.3) ##find sleep time
GPIO.output(11, GPIO.LOW)
GPIO.output(13, GPIO.LOW)
GPIO.output(15, GPIO.LOW)

#THIS IS FRET 5 (101). 
GPIO.output(11, GPIO.HIGH)
GPIO.output(13, GPIO.LOW)
GPIO.output(15, GPIO.HIGH)
#SERVO FUNCTION (WRITE THIS)
time.sleep(0.3) ##find sleep time
GPIO.output(11, GPIO.LOW)
GPIO.output(13, GPIO.LOW)
GPIO.output(15, GPIO.LOW)

#THIS IS FRET 4 (100). 
GPIO.output(11, GPIO.LOW)
GPIO.output(13, GPIO.LOW)
GPIO.output(15, GPIO.HIGH)
#SERVO FUNCTION (WRITE THIS)
time.sleep(0.3) ##find sleep time
GPIO.output(11, GPIO.LOW)
GPIO.output(13, GPIO.LOW)
GPIO.output(15, GPIO.LOW)

#THIS IS FRET 2 (010). 
GPIO.output(11, GPIO.LOW)
GPIO.output(13, GPIO.HIGH)
GPIO.output(15, GPIO.LOW)
#SERVO FUNCTION (WRITE THIS)
time.sleep(0.3) ##find sleep time
GPIO.output(11, GPIO.LOW)
GPIO.output(13, GPIO.LOW)
GPIO.output(15, GPIO.LOW)

#THIS IS FRET 2 (010). 
GPIO.output(11, GPIO.LOW)
GPIO.output(13, GPIO.HIGH)
GPIO.output(15, GPIO.LOW)
#SERVO FUNCTION (WWRITE THIS)
time.sleep(0.3) ##find sleep time
GPIO.output(11, GPIO.LOW)
GPIO.output(13, GPIO.LOW)
GPIO.output(15, GPIO.LOW)

pwm.doDutyCycle()