import pygame
from pygame.locals import *
import globals

#ProfilePhoto class: Jiayao Song
#for profile photo of each player

class ProfilePhoto:
    def __init__(self,x,y,file,file_disable,file_active,scale,style):
        self.x = x
        self.y = y
        self.image_original = pygame.image.load(file).convert_alpha()
        self.image_original_disable = pygame.image.load(file_disable).convert_alpha()
        self.image_original_active = pygame.image.load(file_active).convert_alpha()
        self.width = int(self.image_original.get_width()*scale)
        self.height = int(self.image_original.get_height()*scale)
        self.image = pygame.transform.scale(self.image_original,(self.width,self.height))
        self.rect = self.image.get_rect()

        if style =="center":
            self.startPoint = ((globals.screen_current_width-self.width)/2,self.y)
        else:
            self.startPoint = (self.x,self.y)
        
        #self.rect.topleft = self.startPoint
        self.clicked = False
    
    
    def draw(self,surface):
        surface.blit(self.image, (self.startPoint))


        
        
        
        



