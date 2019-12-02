#!/usr/bin/python

import RPi.GPIO as GPIO
import time
import os

SPICLK = 11
SPIMISO = 9
SPIMOSI = 10
SPICS = 8

def setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(SPIMOSI, GPIO.OUT)
    GPIO.setup(SPIMISO, GPIO.IN)
    GPIO.setup(SPICLK, GPIO.OUT)
    GPIO.setup(SPICS, GPIO.OUT)

def readadc(adcnum, clockin, mosipin, misopin, cspin):
    if((adcnum > 7) or (adcnum < 0)):
        return -1
    GPIO.output(cspin, True)
    GPIO.output(clockin, False)
    GPIO.output(cspin, False)

    commandout = adcnum
    commandout |= 0x18
    commandout <<=3

    for i in range(5):
        if (commandout & 0x80):
            GPIO.output(mosipin, True)
        else:
            GPIO.output(mosipin, False)
        commandout <<= 1
        GPIO.output(clockin, True)
        GPIO.output(clockin, False)

    adcout = 0

    for i in range(12):
        GPIO.output(clockin, True)
        GPIO.output(clockin, False)
        adcout <<=1 
        if (GPIO.input(misopin)): 
            adcout |= 0x1 
            GPIO.output(cspin, True) 
            adcout >>= 1
    return adcout

def main():
    analogChannel = int(input())
    if (analogChannel < 0) or (analogChannel > 7):
        print ('input error analogChannel number!')
        print ('please input 0 to 7...')
    else:
        adc = readadc(analogChannel, SPICLK, SPIMOSI, SPIMISO, SPICS)
        print ('analogChannel %d = %d'%(analogChannel,adc))


def destroy():
    GPIO.cleanup()

if __name__ == '__main__':
    setup()
    try:
        main()
    except KeyboardInterrupt:
        destroy()

