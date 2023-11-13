import pygame
from pygame.locals import *
from CardAnimationModule import *

#StackAnimation class: Jiayao Song
#animation for user draw card from the stack

class StackAnimation(CardAnimation):
    def __init__(self):
        self.adding = 0
        self.image = pygame.image.load("images/Back.png").convert()
        self.image_alpha = 255
        self.move_finish = False

    def move(self,surface,final_y):
        surface.blit(self.image, (340,240+self.adding))

        if self.adding < final_y-240:
            if self.adding < ((final_y-240)/2):
                self.image.set_alpha(self.image_alpha)
                self.adding += 15
                self.image_alpha -= 15
                self.move_finish = False
            if self.adding > ((final_y-240)/2):
                self.image.set_alpha(self.image_alpha)
                self.adding += 5
                self.image_alpha -= 30
                self.move_finish = False
            
        if self.adding >= final_y-240:
            
            self.move_finish = True
        
        

        
        
        
        



