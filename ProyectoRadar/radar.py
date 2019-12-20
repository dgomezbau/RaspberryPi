#Libraries 
import RPi.GPIO as GPIO 
import time
import rotation
from interfaz import drawLine, drawDots, waitForKey, drawInitial
import math
import pygame
import sys
from multiprocessing import Process
from display7segmentos import display, setup
import queue
import threading

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

rotor = rotation.Rotation()

def calculo(angle, distance):
    rads = math.radians(angle)
    y = distance*math.sin(rads)
    x = distance*math.cos(rads)          
    coordX = 300 - x
    coordY = 400 - y

    return coordX, coordY

def loopDiplay(dist_queue):
    while True:
        instant_dis = dist_queue.get()
        while dist_queue.empty():
            display(instant_dis)
    
if __name__ == '__main__':    
    try:
        setup()
        run = False
        drawInitial()
        #setup()
        #p1 = Process(target=loopDiplay)
        dist_queue = queue.Queue()
        tdisp = threading.Thread(target=loopDiplay, args=(dist_queue,))
        tdisp.start()
        while True:
            for evt in pygame.event.get():
                if evt.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if evt.type == pygame.MOUSEBUTTONDOWN:
                    run = False
            detectionCount = []
            while rotor.getAngle()<150 and run:
                for evt in pygame.event.get():
                    if evt.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if evt.type == pygame.MOUSEBUTTONDOWN:
                        run = False
                rotor.move(1)
                dist = distance()
                if dist>200:
                    dist = 200
                distPixel = (dist*300)/200
                dist_queue.put(dist)
                print ("Measured Distance = %.1f cm" % dist)
                print ("Measured Angle = %.1f º" % rotor.getAngle())
                coord = calculo(rotor.getAngle(), distPixel)
                #p1.start()
                print(coord[0])
                print(coord[1])
                detectionCount.append([coord[0], coord[1]])
                drawDots(detectionCount)
                time.sleep(0.5)

            
            detectionCount = []
            while rotor.getAngle()>30 and run:
                for evt in pygame.event.get():
                    if evt.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if evt.type == pygame.MOUSEBUTTONDOWN:
                        run = False
                rotor.move(-1)
                dist = distance()
                if dist>200:
                    dist = 200
                distPixel = (dist*300)/200
                dist_queue.put(dist)
                print ("Measured Distance = %.1f cm" % dist)
                print ("Measured Angle = %.1f º" % rotor.getAngle())
                coord = calculo(rotor.getAngle(), distPixel)
                detectionCount.append([coord[0], coord[1]])
                drawDots(detectionCount)
                time.sleep(0.5)

            while not run:
                rotor.setAngle(30)
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
        GPIO.cleanup()