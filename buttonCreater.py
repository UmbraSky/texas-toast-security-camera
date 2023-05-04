import pygame
from colors import *

class Button():
    def __init__(self, x, y, width, height, buttonContent='Button', altContent = None, buttonType="text", onclickFunction=None, mode = "main", onePress=False):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.onclickFunction = onclickFunction
        self.onePress = onePress
        self.alreadyPressed = False
        self.font = pygame.font.SysFont('Arial', 40)
        self.buttonSurface = pygame.Surface((self.width, self.height))
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)
        if buttonType == "icon":
            self.buttonContent = pygame.image.load(buttonContent)
            self.buttonContent = pygame.transform.scale(self.buttonContent, (self.width/2, self.width/2))
            self.altContent = pygame.image.load(altContent)
            self.altContent = pygame.transform.scale(self.altContent, (self.width/2, self.width/2))
        else:
            self.buttonContent = self.font.render(self.buttonContent, True, (20, 20, 20))
            self.altContent = self.font.render(self.altContent, True, (20, 20, 20))
        self.buttonType = buttonType
        self.mode = mode

        self.fillColors = {
            'normal': DARKERGRAY,
            'hover': DARKERGRAY,
            'pressed': LIGHTERGRAY,
        }
    


    def process(self, screen):
        mousePos = pygame.mouse.get_pos()
        self.buttonSurface.fill(self.fillColors['normal'])
        if self.buttonRect.collidepoint(mousePos):
            self.buttonSurface.fill(self.fillColors['hover'])
            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                self.buttonSurface.fill(self.fillColors['pressed'])
                if self.onePress:
                    self.onclickFunction()
                elif not self.alreadyPressed:
                    self.onclickFunction()
                    self.alreadyPressed = True
            else:
                self.alreadyPressed = False
        
        if self.mode == "alt":
            self.buttonSurface.blit(self.altContent, [
                self.buttonRect.width/2 - self.altContent.get_rect().width/2,
                self.buttonRect.height/2 - self.altContent.get_rect().height/2
            ])
        else:
            self.buttonSurface.blit(self.buttonContent, [
                self.buttonRect.width/2 - self.buttonContent.get_rect().width/2,
                self.buttonRect.height/2 - self.buttonContent.get_rect().height/2
            ])
        screen.blit(self.buttonSurface, self.buttonRect)