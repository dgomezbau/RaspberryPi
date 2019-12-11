#!/usr/bin/python

import RPi.GPIO as GPIO
import time

BuzzerPin = 16

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(BuzzerPin, GPIO.OUT, initial = GPIO.HIGH)

def main():
    while True:
        GPIO.output(BuzzerPin, GPIO.LOW)
        time.sleep(0.3)
        GPIO.output(BuzzerPin, GPIO.HIGH)
        time.sleep(0.3)

def destroy():
    GPIO.output(BuzzerPin, GPIO.LOW)
    GPIO.cleanup()

#if run this script directly, do:

if __name__ == '__main__':
    setup()
    try:
        main()

    #when Ctrl+C is pressed, child program destroy() will be executed.
    except KeyboardInterrupt:
        destroy()
