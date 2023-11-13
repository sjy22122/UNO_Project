from classes import *
from func1 import *
from special_card import *
from AI_logic import *
import globals
from GameStartMenuScreenModule import GameStartMenuScreen


# Dealing the cards
create(globals.ess)

pygame.init()

#create screen
screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption('UNO')
pygame.display.set_icon(globals.img.icon)


globals.current_screen = GameStartMenuScreen()
globals.active = True

# Game Loop
while globals.active:

    # Checking for all the occurring events
    for inp in pygame.event.get():

        # Quit button Check
        if inp.type == pygame.QUIT:
            globals.active = False   
            
    globals.current_screen.draw(screen)
    pygame.display.flip()

pygame.quit()
