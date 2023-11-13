import pygame
from pygame.locals import *
import globals

#Turntable class: Jiayao Song
#for player matching screen, do the animation of the turntable
#have watched the tutorial for rotate: https://www.youtube.com/watch?v=_TU6BEyBieE&t=171s

class Turntable:
    def __init__(self,file,scale):
        self.image_original = pygame.image.load(file).convert_alpha()
        self.width = int(self.image_original.get_width()*scale)
        self.height = int(self.image_original.get_height()*scale)
        self.image = pygame.transform.scale(self.image_original,(self.width,self.height))
        self.rect = self.image.get_rect()
        self.current_degree = 0
        self.degree_adding = 0
        self.rotate_finish = False

    def draw(self,surface,degree):
        self.image_copy = pygame.transform.rotate(self.image,self.degree_adding)
        surface.blit(self.image_copy, ((globals.screen_current_width/2)-int(self.image_copy.get_width()/2),-int(self.image_copy.get_height()/2)))
        if self.degree_adding < degree:
            self.degree_adding += 1
            self.rotate_finish = False
            
        if self.degree_adding == degree:
            self.rotate_finish = True

        
        
        
        



