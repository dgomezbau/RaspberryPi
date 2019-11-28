#!/usr/bin/python

import RPi.GPIO as GPIO
import time

#set GPIO 0 as LED pin

LEDPIN = 17

#setup function some setup --- custom function

def setup():
    GPIO.setwarnings(False)
    #set the gpio modes to BCN numbering
    GPIO.setmode(GPIO.BCM)
    #set LEDPIN's mode to output, and initial level to LOW(0V)
    GPIO.setup(LEDPIN, GPIO.OUT, initial = GPIO.LOW)

#main function

def main():
    #print info
    #print_message()
    while True:
        GPIO.output(LEDPIN, GPIO.HIGH)
        print('...LED ON\n')
        time.sleep(0.5)

        GPIO.output(LEDPIN, GPIO.LOW)
        print('LED OFF...\n')
        time.sleep(0.5)
        pass
    pass

    #define destroy function for clean up everything after the script finished

def destroy():
    #turn off LED
    GPIO.output(LEDPIN, GPIO.LOW)
    #release resource
    GPIO.cleanup()

#if run this script directly, do:

if __name__ == '__main__':
    setup()
    try:
        main()

    #when Ctrl+C is pressed, child program destroy() will be executed.
    except KeyboardInterrupt:
        destroy()