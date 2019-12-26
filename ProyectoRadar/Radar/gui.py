import pygame,sys
from pygame.locals import *
import time


class GUI:

    def __init__(self):
        pygame.init()
        self.red   = (255,   0,   0)
        self.green = (  0, 255,   0)
        self.blue  = (  0,   0, 255)

        self.screen = pygame.display.set_mode((600,400), 0, 32)
        pygame.display.set_caption('Sonar')
        self.imageImg  = pygame.image.load('radar_draw_v01.png').convert()
        self.screen.blit(self.imageImg, (0,0))

    def drawDots(self, detectionCount):
        self.screen.blit(self.imageImg, (0,0))
        for i in detectionCount:
            pygame.draw.circle(self.screen, self.red, (int(i[0]), int(i[1])), 5, 0)

        font = pygame.font.Font('freesansbold.ttf', 24)
        text = font.render('Click for Stop the Sonar', True, self.green, self.blue)
        textRect = text.get_rect() 
        textRect.center = (300, 20)
        self.screen.blit(text, textRect)
        pygame.display.update()

    def drawInitial(self):
        self.screen.blit(self.imageImg, (0,0))
        font = pygame.font.Font('freesansbold.ttf', 24)
        text = font.render('Click for Start the Sonar', True, self.green, self.blue) 
        textRect = text.get_rect() 
        textRect.center = (300, 20)
        self.screen.blit(text, textRect)
        pygame.display.update()

    def eventListener(self):
        for evt in pygame.event.get():
            if evt.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evt.type == pygame.MOUSEBUTTONDOWN:
                return True
            else:
                return False

    def closeListener(self):
        for evt in pygame.event.get():
            if evt.type == pygame.QUIT:
                pygame.quit()
                sys.exit()