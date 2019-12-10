#!/usr/bin/python

import RPi.GPIO as GPIO
import time
import random

BuzzerPin = 6

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(BuzzerPin, GPIO.OUT, initial = GPIO.LOW)

def signal():
    setup()
    time.sleep(random.randrange(5, 10, 1))
    GPIO.output(BuzzerPin, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(BuzzerPin, GPIO.LOW)
