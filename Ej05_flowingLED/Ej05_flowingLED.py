import RPi.GPIO as GPIO
import time

#set 8 pins for 8 leds
LedPins = [17,18,27,22,23,24,25,4]

#setup function for some setup --- custom function
def setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LedPins, GPIO.OUT, initial=GPIO.HIGH)

def main():
    while(True):
        #turn LED on from left to right
        for pin in LedPins:
            GPIO.output(pin, GPIO.LOW)
            time.sleep(0.2)
            GPIO.output(pin,GPIO.HIGH)
            pass
        #turn LED on from right to left
        for pin in reversed(LedPins):
            GPIO.output(pin, GPIO.LOW)
            time.sleep(0.2)
            GPIO.output(pin,GPIO.HIGH)
            pass

def destroy():
    #turn off LED
    GPIO.output(LedPins, GPIO.LOW)
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


