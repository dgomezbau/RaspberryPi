#!/usr/bin/python

import RPi.GPIO as GPIO
import time

LEDPIN = 18

def setup():
    global p
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LEDPIN, GPIO.OUT, initial = GPIO.LOW)

    #set LEDPIN as PWN output, and frecuency = 100Hz
    p = GPIO.PWN(LEDPIN, 100)
    #set p begin with value 0
    p.start(0)
    pass

def main():
    while True:
        for dc in range(0,101,4):
            #change duty cycle to dc
            p.ChangeDutyCycle(dc)
            time.sleep(0.1)
            pass

        for dc in range(100,-1,-4):
            #change duty cycle to dc
            p.ChangeDutyCycle(dc)
            time.sleep(0.1)
            pass
        pass
    pass

def destroy():
    GPIO.output(LEDPIN, GPIO.LOW)
    GPIO.cleanup()

#if run this script directly, do:

if __name__ == '__main__':
    setup()
    try:
        main()

    #when Ctrl+C is pressed, child program destroy() will be executed.
    except KeyboardInterrupt:
        destroy()