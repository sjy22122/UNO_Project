import pygame
from pygame.locals import *
import globals

#Background class: Jiayao Song
#for backgroun image

class Background:
    def __init__(self,file):
        image_original = pygame.image.load(file)
        scale = globals.screen_current_width/image_original.get_width()
        self.width = int(image_original.get_width()*scale)
        self.height = int(image_original.get_height()*scale)
        self.image = pygame.transform.scale(image_original,(self.width,self.height))
        self.rect = self.image.get_rect()
        self.rect.topleft = (0,0)
    
    def draw(self,surface):
        surface.blit(self.image,(0,0))