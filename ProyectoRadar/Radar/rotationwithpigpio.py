import time

import pigpio

#For initializing the pigpio Daemon run: sudo pigpio

class Rotationpig:
    def __init__(self):
        self.pi = pigpio.pi() # Connect to local Pi.
        self.angle = 30
        self.step = 2

    def move(self, sentido):
        self.pi.set_servo_pulsewidth(18, self.calcSec(self.angle))
        self.angle = self.angle+(sentido*self.step)
    
    def calcSec(self, angle):
        return ((angle*1500)/180)+750

    def getAngle(self):
        return self.angle

    def setAngle(self, newAngle):
        self.angle = newAngle

    def destroy(self):
        self.pi.set_servo_pulsewidth(18, 0)
        self.pi.stop()
