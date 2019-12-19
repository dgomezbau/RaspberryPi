#Libraries 
#import RPi.GPIO as GPIO 
import time
#import rotation
from interfaz import drawLine, drawDots, waitForKey, drawInitial
import math
import pygame
import sys
import random


'''def distance(): 
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

rotor = rotation.Rotation2()'''

def calculo(angle, distance):
    rads = math.radians(angle)
    y = distance*math.sin(rads)
    x = distance*math.cos(rads)          
    coordX = 300 - x
    coordY = 400 - y

    return coordX, coordY

    
if __name__ == '__main__':    
    try:
        run = False
        drawInitial()
        while True:
            for evt in pygame.event.get():
                if evt.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if evt.type == pygame.MOUSEBUTTONDOWN:
                    run = False
            detectionCount = []
            anglev = 30
            while anglev<150 and run:
                for evt in pygame.event.get():
                    if evt.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                if evt.type == pygame.MOUSEBUTTONDOWN:
                    run = False
                time.sleep(0.5)
                dist = random.randrange(200)
                if dist>200:
                    dist = 200
                distPixel = (dist*300)/200
                print ("Measured Distance = %.1f cm" % dist)
                print ("Measured Angle = %.1f º" % anglev)
                coord = calculo(anglev, distPixel)
                print(coord[0])
                print(coord[1])
                #drawLine(coord[0], coord[1])
                detectionCount.append([coord[0], coord[1]])
                print(detectionCount)
                drawDots(detectionCount)
                anglev+=2
            
            detectionCount = []
            while anglev>30 and run:
                for evt in pygame.event.get():
                    if evt.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                if evt.type == pygame.MOUSEBUTTONDOWN:
                    run = False
                dist = random.randrange(200)
                if dist>200:
                    dist = 200
                distPixel = (dist*300)/200
                print ("Measured Distance = %.1f cm" % dist)
                print ("Measured Angle = %.1f º" % anglev)
                coord = calculo(anglev, distPixel)
                #drawLine(coord[0], coord[1])
                detectionCount.append([coord[0], coord[1]])
                drawDots(detectionCount)
                anglev-=2

            while not run:
                drawInitial()
                for evt in pygame.event.get():
                    if evt.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if evt.type == pygame.MOUSEBUTTONDOWN:
                        run = True
                        time.sleep(0.5)

    except KeyboardInterrupt: 
        print("Measurement stopped by User") 
        #GPIO.cleanup()