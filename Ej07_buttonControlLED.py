#!/usr/bin/python

import RPi.GPIO as GPIO
import time

#set BCM_GPIO 17(GPIO0) as button pin
ButtonPin = 17
#set BCM_GPIO 18(GPIO1) as LED pin
LedPin = 18

#set led status to True(OFF)
led_status = True

def setup():
    GPIO.setwarnings(False)
    #set the gpio modes to BCM numbering
    GPIO.setmode(GPIO.BCM)
    #set all LedPin's mode to output,and initial level to HIGH(3.3V)
    GPIO.setup(LedPin,GPIO.OUT,initial=GPIO.HIGH)
    #set ButtonPin's mode to input,and pull up to high(3.3v)
    GPIO.setup(ButtonPin,GPIO.IN,pull_up_down = GPIO.PUD_UP)
    #set up a falling detect on ButtonPin,and callback function to ButtonLed
    GPIO.add_event_detect(ButtonPin,GPIO.FALLING,callback = ButtonLed)
    pass

def ButtonLed(ev=None):
    global led_status
    # Switch led status(on-->off; off-->on)
    led_status = not led_status
    GPIO.output(LedPin, led_status)
    if led_status:
        print('|*************|')
        print('|  LED OFF... |')
        print('|*************|')
        print('\n')
    else:
        print('|*************|')
        print('|  ...LED ON  |')
        print('|*************|')
        print('\n')

def main():
    while True:
        # Don't do anything.
        time.sleep(1)

def destroy():
    GPIO.output(LedPin, GPIO.LOW)
    GPIO.output(ButtonPin, GPIO.LOW)
    GPIO.cleanup()

#if run this script directly, do:

if __name__ == '__main__':
    setup()
    try:
        main()

    #when Ctrl+C is pressed, child program destroy() will be executed.
    except KeyboardInterrupt:
        destroy()