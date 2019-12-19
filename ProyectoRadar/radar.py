#Libraries 
import RPi.GPIO as GPIO 
import time
import rotation
from interfaz import drawLine, drawDots
import math

#GPIO Mode (BOARD / BCM) 
GPIO.setmode(GPIO.BCM) 
#set GPIO Pins 
GPIO_TRIGGER = 23 
GPIO_ECHO = 24 
#set GPIO direction (IN / OUT) 
GPIO.setup(GPIO_TRIGGER, GPIO.OUT) 
GPIO.setup(GPIO_ECHO, GPIO.IN) 

def distance(): 
    # set Trigger to HIGH 
    GPIO.output(GPIO_TRIGGER, True) 
    # set Trigger after 0.01ms to LOW 
    time.sleep(0.00001) 
    GPIO.output(GPIO_TRIGGER, False) 
    StartTime = time.time() 
    StopTime = time.time() 
    # save StartTime 
    while GPIO.input(GPIO_ECHO) == 0: 
        StartTime = time.time() 
        # save time of arrival 
    while GPIO.input(GPIO_ECHO) == 1: 
        StopTime = time.time() 
        # time difference between start and arrival 
    TimeElapsed = StopTime - StartTime 
    # multiply with the sonic speed (34300 cm/s) # and divide by 2, because there and back 
    distance = (TimeElapsed * 34300) / 2 
    return distance

rotor = rotation.Rotation2()

def calculo(angle, distance):
    rads = math.radians(angle)
    y = distance*math.sin(rads)
    x = distance*math.cos(rads)          
    coordX = 300 - x
    coordY = 400 - y

    return coordX, coordY

    
if __name__ == '__main__':    
    try:
        while True:
            detectionCount = []
            while rotor.getAngle()<150:
                rotor.move(1)
                dist = distance()
                if dist>200:
                    dist = 200
                distPixel = (dist*300)/200
                print ("Measured Distance = %.1f cm" % dist)
                print ("Measured Angle = %.1f º" % rotor.getAngle())
                coord = calculo(rotor.getAngle(), distPixel)
                print(coord[0])
                print(coord[1])
                #drawLine(coord[0], coord[1])
                detectionCount.append([coord[0], coord[1]])
                drawDots(detectionCount)
            
            detectionCount = []
            while rotor.getAngle()>30:
                rotor.move(-1)
                dist = distance()
                if dist>200:
                    dist = 200
                distPixel = (dist*300)/200
                print ("Measured Distance = %.1f cm" % dist)
                print ("Measured Angle = %.1f º" % rotor.getAngle())
                coord = calculo(rotor.getAngle(), distPixel)
                #drawLine(coord[0], coord[1])
                detectionCount.append([coord[0], coord[1]])
                drawDots(detectionCount)

    except KeyboardInterrupt: 
        print("Measurement stopped by User") 
        GPIO.cleanup()
