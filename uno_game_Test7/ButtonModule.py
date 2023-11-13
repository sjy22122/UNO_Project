import pygame
from pygame.locals import *
import globals

#Button class: Jiayao Song
#for button
#can get the result of whether the button is clicked
#has watch the Youtube Tutorial: https://www.youtube.com/watch?v=G8MYGDf_9ho

class Button:
    def __init__(self,x,y,file,scale,style):
        self.image_original = pygame.image.load(file).convert_alpha()
        self.width = int(self.image_original.get_width()*scale)
        self.height = int(self.image_original.get_height()*scale)
        self.image = pygame.transform.scale(self.image_original,(self.width,self.height))
        self.rect = self.image.get_rect()

        if style =="center":
            self.startPoint = ((globals.screen_current_width-self.width)/2,y)
        else:
            self.startPoint = (x,y)
        
        self.rect.topleft = self.startPoint
        self.clicked = False
    
    
    def draw(self,surface):
        self.action = False
        #get mouse position
        pos = pygame.mouse.get_pos()
        #check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0]==1:
                if self.clicked == False:
                    self.clicked = True
                    self.action = True
            if pygame.mouse.get_pressed()[0]==0:
                self.clicked = False
        surface.blit(self.image, (self.startPoint))

    def get_result(self):
        return self.action


