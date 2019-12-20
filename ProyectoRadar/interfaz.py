import pygame,sys
from pygame.locals import *
import time

pygame.init()

#set up the colors
black = (  0,   0,   0)
white = (255, 255, 255)
red   = (255,   0,   0)
green = (  0, 255,   0)
blue  = (  0,   0, 255)

#set up the window
screen = pygame.display.set_mode((600,400), 0, 32)
pygame.display.set_caption('Sonar')

imageImg  = pygame.image.load('radar_draw_v01.png').convert()

screen.blit(imageImg, (0,0))

#screen.fill(white)

'''for event in pygame.event.get():
    if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
        is_moving = True
    elif event.type == pygame.KEYUP and event.key == pygame.K_d:
        is_moving = False'''

def waitForKey():
    pressedKey = pygame.key.get_pressed()
    return pressedKey[K_SPACE]

def drawLine(coordX, coordY):
    screen.blit(imageImg, (0,0))
    pygame.draw.line(screen, blue, (300, 400), (coordX, coordY), 10)
    pygame.display.update()

def drawDots(detectionCount):
    screen.blit(imageImg, (0,0))
    for i in detectionCount:
        pygame.draw.circle(screen, red, (int(i[0]), int(i[1])), 5, 0)

    font = pygame.font.Font('freesansbold.ttf', 24)
    text = font.render('Click for Stop the Sonar', True, green, blue)
    textRect = text.get_rect() 
    textRect.center = (300, 20)
    screen.blit(text, textRect)

    pygame.display.update()

def drawInitial():
    screen.blit(imageImg, (0,0))
    font = pygame.font.Font('freesansbold.ttf', 24)
    text = font.render('Click for Start the Sonar', True, green, blue) 
    textRect = text.get_rect() 
    textRect.center = (300, 20)
    screen.blit(text, textRect)
    pygame.display.update()



'''while True:
    screen.blit(imageImg, (0,0))
    pygame.draw.line(screen, blue, (300, 400), (cont, 60), 4)
    pygame.display.update()
    time.sleep(1)

    cont +=10'''