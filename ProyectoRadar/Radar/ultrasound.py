import RPi.GPIO as GPIO 
import time

class UltraSound:
    def __init__(self):
        self.setup()

    def setup(self):
        GPIO.setmode(GPIO.BCM)  
        self.GPIO_TRIGGER = 23 
        self.GPIO_ECHO = 24 
        GPIO.setup(self.GPIO_TRIGGER, GPIO.OUT) 
        GPIO.setup(self.GPIO_ECHO, GPIO.IN)

    def distance(self):
        GPIO.output(self.GPIO_TRIGGER, True)
        time.sleep(0.00001) 
        GPIO.output(self.GPIO_TRIGGER, False) 
        StartTime = time.time() 
        StopTime = time.time() 
        while GPIO.input(self.GPIO_ECHO) == 0: 
            StartTime = time.time() 
        while GPIO.input(self.GPIO_ECHO) == 1: 
            StopTime = time.time()
        TimeElapsed = StopTime - StartTime 
        # multiply with the sonic speed (34300 cm/s) # and divide by 2, because there and back 
        distance = (TimeElapsed * 34300) / 2 
        return distance