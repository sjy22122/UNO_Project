from pygame import  *
import pygame
from pygame.locals import *

#CardAnimation class: Jiayao Song
#animation for user play a card

#a = (y1-y0)/(x1-x0)
#b = y + ax
#x = (b-y)/a

class CardAnimation:
    def __init__(self,file,start,end):
        self.adding = 0
        self.image = pygame.image.load(file).convert()
        self.image_alpha = 255
        self.move_finish = False
        self.start = start
        self.end = end
        self.a = (self.end[1]-self.start[1])/(self.end[0]-self.start[0])
        self.b = -240-(self.a*580)
        


    def move(self,surface,min_y,max_y):
        self.y = -(max_y - self.adding)
        self.x = (self.y-self.b)/self.a
        surface.blit(self.image, (self.x, max_y - self.adding))
        if self.adding < max_y-min_y:
            if self.adding < ((max_y-min_y)/2): #normal speed
                self.image.set_alpha(self.image_alpha)
                self.adding += 15
                self.image_alpha -= 15
                self.move_finish = False
            if self.adding >= ((max_y-min_y)/2): #move slower
                self.image.set_alpha(self.image_alpha)
                self.adding += 5
                self.image_alpha -= 30
                self.move_finish = False

        if self.adding >= max_y-min_y:
            self.move_finish = True
    
    def get_move_finish(self):
        return self.move_finish
        
        

        
        
        
        



