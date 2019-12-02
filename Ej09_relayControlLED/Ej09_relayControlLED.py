#!/usr/bin/python

import RPi.GPIO as GPIO
import time

RelayPin = 17

def setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(RelayPin,GPIO.OUT, initial=GPIO.LOW)

def main():
    while True:
        GPIO.output(RelayPin, GPIO.LOW)
        time.sleep(1)

        GPIO.output(RelayPin, GPIO.HIGH)
        time.sleep(1)

def destroy():
    GPIO.output(RelayPin, GPIO.LOW)
    GPIO.cleanup()

if __name__ == '__main__':
    setup()
    try:
        main()
    except KeyboardInterrupt:
        destroy()
