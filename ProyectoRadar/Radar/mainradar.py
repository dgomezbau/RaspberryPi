import display7seg
import gui
import rotationwithpigpio
import ultrasound
import time
import queue
import threading
import math
import sys
import pygame

rotor = rotationwithpigpio.Rotationpig()
interfaz = gui.GUI()
display = display7seg.Display()
ultrasonido = ultrasound.UltraSound()

def calculo(angle, distance):
    rads = math.radians(angle)
    y = distance*math.sin(rads)
    x = distance*math.cos(rads)          
    coordX = 300 + x
    coordY = 400 - y

    return coordX, coordY

def loopDiplay(dist_queue):
    while True:
        instant_dis = dist_queue.get()
        while dist_queue.empty():
            display.display(instant_dis)

if __name__ == '__main__':
    try:
        run = False
        interfaz.drawInitial()
        dist_queue = queue.Queue()
        tdisp = threading.Thread(target=loopDiplay, args=(dist_queue,))
        tdisp.start()
        while True:            
            for evt in pygame.event.get():
                if evt.type == pygame.QUIT:
                    rotor.destroy()
                    display.destroy()
                    pygame.quit()
                    sys.exit()
                if evt.type == pygame.MOUSEBUTTONDOWN:
                    run = False
            detectionCount = []
            while rotor.getAngle()<150 and run:
                for evt in pygame.event.get():
                    if evt.type == pygame.QUIT:
                        rotor.destroy()
                        display.destroy()
                        pygame.quit()
                        sys.exit()
                    if evt.type == pygame.MOUSEBUTTONDOWN:
                        run = False
                rotor.move(1)
                dist = ultrasonido.distance()
                if dist>200:
                    dist = 200
                distPixel = (dist*300)/200
                dist_queue.put(dist)
                print ("Measured Distance = %.1f cm" % dist)
                print ("Measured Angle = %.1f º" % rotor.getAngle())
                coord = calculo(rotor.getAngle(), distPixel)
                detectionCount.append([coord[0], coord[1]])
                interfaz.drawDots(detectionCount)
                time.sleep(0.5)

            
            detectionCount = []
            while rotor.getAngle()>30 and run:
                for evt in pygame.event.get():
                    if evt.type == pygame.QUIT:
                        rotor.destroy()
                        display.destroy()
                        pygame.quit()
                        sys.exit()
                    if evt.type == pygame.MOUSEBUTTONDOWN:
                        run = False
                rotor.move(-1)
                dist = ultrasonido.distance()
                if dist>200:
                    dist = 200
                distPixel = (dist*300)/200
                dist_queue.put(dist)
                print ("Measured Distance = %.1f cm" % dist)
                print ("Measured Angle = %.1f º" % rotor.getAngle())
                coord = calculo(rotor.getAngle(), distPixel)
                detectionCount.append([coord[0], coord[1]])
                interfaz.drawDots(detectionCount)
                time.sleep(0.5)

            while not run:
                rotor.setAngle(30)
                interfaz.drawInitial()
                for evt in pygame.event.get():
                    if evt.type == pygame.QUIT:
                        rotor.destroy()
                        display.destroy()
                        pygame.quit()
                        sys.exit()
                    if evt.type == pygame.MOUSEBUTTONDOWN:
                        run = True
                time.sleep(0.5)

    except KeyboardInterrupt:
        rotor.destroy()
        display.destroy()