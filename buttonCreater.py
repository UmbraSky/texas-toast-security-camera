import pygame
from colors import *

class Button():
    def __init__(self, x, y, width, height, buttonContent='Button', buttonType="text", onclickFunction=None, onePress=False):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.onclickFunction = onclickFunction
        self.onePress = onePress
        self.alreadyPressed = False
        self.font = pygame.font.SysFont('Arial', 40)
        self.buttonContent = buttonContent
        self.buttonType = buttonType

        self.fillColors = {
            'normal': DARKERGRAY,
            'hover': DARKERGRAY,
            'pressed': LIGHTERGRAY,
        }
    
    def render(self):
        self.buttonSurface = pygame.Surface((self.width, self.height))
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)

        if self.buttonType == "text":
            self.buttonSurf = self.font.render(self.buttonContent, True, (20, 20, 20))
        elif self.buttonType == "icon":
            self.buttonSurf = pygame.image.load(self.buttonContent)
            self.buttonSurf = pygame.transform.scale(self.buttonSurf, (self.buttonRect.width/2, self.buttonRect.width/2))

    
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
        
        self.buttonSurface.blit(self.buttonSurf, [
            self.buttonRect.width/2 - self.buttonSurf.get_rect().width/2,
            self.buttonRect.height/2 - self.buttonSurf.get_rect().height/2
        ])
        screen.blit(self.buttonSurface, self.buttonRect)